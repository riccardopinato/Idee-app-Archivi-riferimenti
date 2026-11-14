/* Browser-free Gateway feed security test: uses the actual extracted Site code.
 * Node built-ins only. Never reads browser storage, network or GitHub live.
 */
'use strict';
const fs = require('node:fs');
const assert = require('node:assert/strict');
const path = require('node:path');
const root = path.resolve(__dirname, '..', '16-APP-FACTORY-SITE');
const html = fs.readFileSync(path.join(root, 'src/index.html'), 'utf8');
const data = JSON.parse(fs.readFileSync(path.join(root, 'data/gateway_progress.json'), 'utf8'));
const begin = html.indexOf('async function loadGatewayStatus()');
const end = html.indexOf('function commonPage()', begin);
assert(begin !== -1 && end > begin, 'Gateway functions not found');
const code = html.slice(begin, end);
const clone = x => JSON.parse(JSON.stringify(x));

function makeHarness() {
  let next = clone(data), renders = 0;
  const fetch = async () => ({ok: true, json: async () => clone(next)});
  const esc = x => String(x ?? '').replace(/[&<>"']/g, c =>
    ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const heading = (_a, title) => title;
  const metric = (label, value) => '<div>' + label + ':' + value + '</div>';
  const panel = (_title, body) => body;
  const table = (_cols, rows) => rows.join('');
  const link = (url, title) => '<a href="' + esc(url) + '">' + esc(title) + '</a>';
  const stateBadge = value => esc(value);
  const render = () => {renders++;};
  const body = [
    'let gatewayData=null,gatewayError=null,gatewayQuery="",gatewayFilter="",section="notgateway";',
    code,
    'return {loadGatewayStatus, gatewayPage, getData:()=>gatewayData,',
    'getError:()=>gatewayError, countRenders:()=>renderCalls()};'
  ].join('\n').replace('countRenders:()=>renderCalls()', 'countRenders:()=>0');
  const create = new Function('fetch','REMOTE_GATEWAY','esc','heading','metric','panel','table','link','stateBadge','render',body);
  const app = create(fetch, 'https://example.invalid/gateway.json', esc, heading,
    metric, panel, table, link, stateBadge, render);
  return {...app, setData: v => {next = v;}};
}

async function main() {
  const h = makeHarness();
  await h.loadGatewayStatus();
  assert.equal(h.getData().prs.length, 9);
  assert.equal(h.getError(), null);
  assert(h.gatewayPage().includes('Gateway MCP'));

  for (const changed of [
    d => {d.observed_pr_ci_pass = '<img src=x onerror=alert(1)>';},
    d => {d.merged_count = '<svg onload=alert(1)>';},
    d => {d.prs[0].depends_on = null;},
    d => {d.prs[0].depends_on = 'evil';},
    d => {d.prs[0].depends_on = [d.prs[0].number];},
    d => {d.prs[0].blockers = ['<img src=x onerror=alert(1)>'];},
    d => {d.prs[0].url = 'javascript:alert(1)';},
  ]) {
    const bad = clone(data); changed(bad);
    h.setData(bad);
    await h.loadGatewayStatus();
    assert(h.getError(), 'An invalid feed must return an error');
    assert.equal(h.getData().prs.length, 9, 'Valid previous snapshot must be kept');
    const htmlOut = h.gatewayPage();
    assert(htmlOut.includes('snapshot valida precedente'), 'Error banner must explain stale data');
    assert(!htmlOut.includes('onerror=alert(1)'), 'Injection payload must never render');
    assert(!htmlOut.includes('<svg onload=alert(1)>'), 'SVG injection must never render');
  }
  console.log('PASS: Gateway feed rejects XSS/invalid dependency shapes and preserves last valid snapshot');
}
main().catch(e => {console.error(e);process.exitCode=1;});
