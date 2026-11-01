# CAP-0111 — Anna Flutter reuse-first plan

1. Leggere Product Bible/roadmap corrente e rispettare v1.07 C1/C2 ancora pianificati. Proposta fuori roadmap per ora.
2. Mappare *solo* `AgendaItem` privati dal `AgendaStore.items` al semplice `AnnaReviewTask`. Non leggere `SharedEntry`, Account diversi, private vault, ciclo, E2EE o contenuti nascosti.
3. Esporre l'anteprima settimanale in Today/diario, idealmente vicino al preesistente `WeekData` per evitare un nuovo store o motore produttivita.
4. Al salvataggio di riflessioni o priorita, usare i writer AgendaStore gia esistenti con account/revision guard. No cancellazione, ri-pianificazione o push impliciti.
5. QA su task ricorrenti, dati Trash, localizzazione, login switch, restore/sync, blocchi Vault e prestazioni su settimana lunga.

Il pure Dart kit non chiama né modifica API Flutter/Anna e non certifica il risultato runtime.
