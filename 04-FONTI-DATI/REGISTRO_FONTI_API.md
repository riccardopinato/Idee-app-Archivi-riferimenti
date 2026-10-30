# Provider e dataset: fonte, uso, limiti

> Snapshot di fonte storica al 30 ottobre 2026. Le sigle [E]/[V]/[C]/[R] riportano provenienza, non certificazione corrente. Originale preservato in 90-STORICO.

Le fonti in questa sezione sono CANDIDATI DI INTEGRAZIONE, non provider automaticamente approvati. Dove [V], almeno una fonte ufficiale/policy è stata controllata il 2026-10-30.

MAPPE, POI, GEOCODING, ATTRAZIONI
[V] OpenStreetMap data | https://www.openstreetmap.org/copyright | strade, sentieri, servizi, parcheggi, campeggi, punti interesse | TrailPath, CamperBoss, Wonderlog, Parking Buddy, Web | ODbL con attribuzione e obblighi per DB derivati; NON confondere dati con tile gratuiti.
[V] Geofabrik OSM extracts | https://download.geofabrik.de/ | estratti OSM per regione, aggiornati spesso quotidianamente, bulk/offline | TrailPath, CamperBoss, POI own DB | ODbL; dimensioni/granularità e responsabilità hosting.
[V] Overpass API | https://wiki.openstreetmap.org/wiki/Overpass_API | query geografiche/tag OSM e POI | prototipi, aggiornamenti circoscritti | public endpoint NON per query massicce sostenute; preferire estratti/self-host/provider.
[V] Nominatim | https://operations.osmfoundation.org/policies/nominatim/ | geocoding e reverse-geocoding | location search | SERVER PUBBLICO massimo 1 request/sec, no autocomplete lato client, no estrazione massiva POI; valutare self-host/provider commerciale.
[V] OSM tile server policy | https://operations.osmfoundation.org/policies/tiles/ | mappe tile standard | app mappe | vietato bulk download/offline map prefetch su tile.openstreetmap.org; tile commerciali/self-host per distribuzione/offline.
[V] Overture Maps Places | https://docs.overturemaps.org/guides/places/ | grandi dataset POI, business, edifici, indirizzi, transportation via GeoParquet | CamperBoss, Wonderlog, WEB local discovery | verificare licenza per TEMA: Places CDLA-Permissive 2.0/Apache, altri temi possono avere ODbL; provenance a livello record.
[V] Overture Maps data repo | https://github.com/OvertureMaps/data | dataset bulk S3/Azure, IDs GERS, release con data | GeoData Core condiviso | schema/versioni/licenze per tema e fonte.
[V] Wikidata Query Service | https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service | entità, monumenti, luoghi e relazioni enciclopediche | Wonderlog, World Days, CamperBoss | 2026–27 migrazione backend in corso; limiti query e dati incompleti; attribuzione fonti per media.
[C][R] Wikimedia Commons / MediaWiki | https://commons.wikimedia.org/ | fotografie/descrizioni per luoghi, heritage | Wonderlog, World Days, CamperBoss | controllare licenza di OGNI immagine, credit e derivati; una pagina pubblica non significa riuso libero.
[C][R] OpenTripMap | https://opentripmap.io/ | POI turistici e attrazioni | Wonderlog/CamperBoss | verificare API key, piani, licenza commerciale e qualità.
[C][R] MapTiler API | https://docs.maptiler.com/cloud/api/reference/ | tiles, satellite, geocoding | TrailPath, CamperBoss | API key, piano commerciale, attribuzione; mai assumere tiles/offline free.
[C][R] MapLibre | https://maplibre.org/ | RENDERER cartografico, NON dataset POI | TrailPath, app maps | differenziare SDK mappe da provider dati/tiles.
[C][R] Geonames | https://www.geonames.org/ | località, CAP/ZIP, coordinate | WEB-011, geocoding/locale | controllare licenza per dataset, precisione/freschezza.

ROUTING, SENTIERI, ALTIMETRIA, TRASPORTI
[C][R] Valhalla | https://github.com/valhalla/valhalla | routing OSM, map matching/trace, matrice, isocrone | TrailPath, WEB-009, CamperBoss | engine OSS; costo hosting e dataset, verify routing mountain paths.
[C][R] OSRM | https://project-osrm.org/ | routing rapido su rete OSM | WEB-009, trip cost | self-host/provider, profili e map matching da scegliere.
[C][R] GraphHopper | https://www.graphhopper.com/ | routing/optimization, engine/provider | TrailPath, CamperBoss | API hosted vs OSS, licenze/costi distinti.
[V] OpenTopoData | https://www.opentopodata.org/ | quota altimetrica da DEM; self-host | TrailPath profilo altimetrico | selezione dataset/risoluzione/licenze/limiti API.
[V] Open-Elevation | https://open-elevation.com/ | alternative elevation API | TrailPath | GPL del server se usato come codice, dataset e limiti da validare.
[V] GTFS/GTFS Realtime | https://gtfs.org/ | orari, fermate, ritardi, disservizi, alert | WEB-010, CamperBoss/viaggi | standard NON provider: acquisire feed per operatore/mercato e relativi diritti.
[C][R] operatori/regioni/ministeri trasporti | portali ufficiali locali | scioperi, orari, lavori, alert | WEB-010 | refresh e copertura geografica, non inventare stato live.

METEO, CLIMA, ARIA, SOLE
[V] Open-Meteo forecast | https://open-meteo.com/ | meteo orario/giornaliero globale | TrailPath, CamperBoss, GrillBoss, Wonderlog, WEB-008 | API pubblica gratuita SOLO NON COMMERCIALE (pubblicità e abbonamenti sono uso commerciale); usare piano commerciale o hosting proprio a condizioni verificate.
[V] Open-Meteo terms | https://open-meteo.com/en/terms | diritti, quote, attribution | tutti i progetti meteo | distinguere API terms da licenza dei dati; attribution dei modelli inclusi.
[V] Open-Meteo Air Quality | https://open-meteo.com/en/docs/air-quality-api | PM2.5, PM10, NO2, ozono, UV, pollini dove disponibili | WEB-014, TrailPath, CamperBoss | copertura pollini non globale, reportare disponibilità.
[V] Open-Meteo Marine | https://open-meteo.com/en/docs/marine-weather-api | onde, direzione/periodo, superficie mare, correnti | CamperBoss costa, Wonderlog, app marine future | stessa verifica commerciale, granularità incerta per alcuni dati.
[V] OpenAQ v3 | https://docs.openaq.org/about/about | misure qualità aria rete mondiale | WEB-014, TrailPath | API pubblica; rispettare condizioni dei provider terzi, non copertura totale.
[V] Meteostat | https://dev.meteostat.net/ | serie meteo storiche orarie/giornaliere, stazioni | analitica meteo, storico outdoor | licenza/provenance e qualità serie da controllare.
[V] Copernicus Climate Data Store | https://cds.climate.copernicus.eu/en/ | dataset climatici/reanalysis | ricerca/analisi storica per app meteo | troppo pesante per meteo consumer in diretta; consultare dataset-specific licenses.
[C][R] CAMS/Copernicus Atmosphere | https://atmosphere.copernicus.eu/ | qualità aria, pollini e modelli ambientali | WEB-014 | limiti copertura, licenze dataset.
[C][R] NOAA / NWS | https://www.weather.gov/documentation/services-web-api | allerte e meteo US | servizi USA in WEB-008 | termini/geografie/config da verificare.
[C][R] MET Norway | https://api.met.no/ | forecast meteorologici, avvisi | fallback meteo app | User-Agent/termini di attribuzione e caching da verificare.
[C][R] SunCalc | https://github.com/mourner/suncalc | calcolo locale sole/luna/golden hour | WEB-012, FrameLab, TrailPath, Wonderlog | libreria, NON API esterna; controllare licenza repo prima di copiare.

ALTRI DATASET: CARBURANTE, FARMACIE, TASSE, TELEFONI, TRACKING
[C][R] MIMIT Open Data carburanti | https://www.mimit.gov.it/index.php/it/open-data/elenco-dataset/carburanti-prezzi-praticati-e-anagrafica-degli-impianti | impianti e prezzi carburanti Italia | WEB-002, WEB-009, CamperBoss/auto | fonte istituzionale; verificare rilascio, licenza, freshness.
[C][R] France fuel data | https://www.data.gouv.fr/ | impianti/prezzi Francia | WEB-002, WEB-009 | identificare dataset canonico e riuso.
[C][R] Tankerkönig / MTS-K | https://www.tankerkoenig.de/ | prezzi carburanti Germania | WEB-002 | restrizioni commerciali/ridistribuzione, verificare condizioni.
[C][R] Ministero Salute Farmacie | https://www.dati.salute.gov.it/it/dataset/farmacie/ | anagrafica farmacia Italia | WEB-005 | NON comprende automaticamente turni aggiornati; aggregare autorità locali.
[C][R] UK DVSA MOT History | https://findtransportdata.dft.gov.uk/dataset/mot-history-api | MOT e storico veicoli UK | WEB-007 | credenziali, accesso e API terms.
[C][R] HMRC income tax | https://www.gov.uk/income-tax-rates | aliquote UK | WEB-004 | versionare per anno fiscale; utilizzare enti ufficiali per ogni paese.
[C][R] Cloudflare Radar | https://developers.cloudflare.com/radar/investigate/outages/ | anomalie Internet/ASN/outage | WEB-003 | non conferma da solo un downtime di singola app.
[C][R] Status pages ufficiali | per singolo servizio | disponibilità incidenti programmati | WEB-003 | licenze, no scraping vietato, timestamp e severity.
[C][R] 17TRACK | https://www.17track.net/ | tracking pacchi multi-corriere | WEB-006, Parcel Inbox | API commerciale, quote, privacy tracking.
[C][R] AfterShip | https://www.aftership.com/ | tracking API/webhook | WEB-006 | costi, webhooks, conservazione dati.
[C][R] libphonenumber | https://github.com/google/libphonenumber | validazione e parsing numeri, carrier originario approssimato | WEB-001, Anti-Truffa | NON dà identità privata reale né reputazione spam.
[C][R] Ofcom numbering data | https://www.ofcom.org.uk/ | blocchi numerici UK | WEB-001 | aggiornamento e autorizzazioni per dataset.
[C][R] GeoNames postal | https://www.geonames.org/postal-codes-sources.html | CAP/ZIP, città | WEB-011 | verifica dataset nazione.
[C][R] Nager.Date | https://github.com/nager/Nager.Date | festività per paese/regione | WEB-013, World Days | differenziare festivi ufficiali dalle giornate mondiali, validare copertura divisioni.
[C][R] ONU days/weeks | https://www.un.org/en/observances/international-days-and-weeks | giornate e settimane riconosciute dall'ONU | World Days | verificare ricorrenza, stato ufficiale e data; metadati/provenance.
[C][R] UNESCO Days | https://www.unesco.org/en/days | giorni internazionali UNESCO | World Days | originalità testo, fonte della data.
[C][R] WHO campaigns | https://www.who.int/campaigns | campagne, giornate e settimane | World Days | distingue campagne da festività ONU.
[C][R] FAO Days | https://www.fao.org/ | giornate FAO, ad es. alimentazione | World Days | verifica calendario ufficiale.

DATASET EDITORIALI, CATALOGHI, PRODUCT SCAN
[C][R] Open Food Facts | https://world.openfoodfacts.org/ | alimenti, ingredienti, EAN/UPC, nutrienti e foto dove presenti | BeerClass, MealMate, Cooking Anime | ODbL per dati, diritti immagini e attribuzione; verificare categorie birra e cache.
[C][R] OpenStreetMap POI categories | https://wiki.openstreetmap.org/wiki/Map_features | amenity/tourism/shop/leisure/natural | CamperBoss, TrailPath, WEB local | schema tags e completezza per nazione variabili.
[C][R] Wikimedia Commons | https://commons.wikimedia.org/ | immagini su luoghi/eventi | World Days, Wonderlog | obbligatorio licensing asset-by-asset.

====================================================================
