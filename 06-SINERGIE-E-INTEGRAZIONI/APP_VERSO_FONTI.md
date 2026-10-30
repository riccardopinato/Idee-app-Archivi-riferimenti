# Matrice app → fonti/donor

> Snapshot di fonte storica al 30 ottobre 2026. Le sigle [E]/[V]/[C]/[R] riportano provenienza, non certificazione corrente. Originale preservato in 90-STORICO.

TrailPath -> OSM/Geofabrik (sentieri e topologia), Valhalla trace/routing, MapLibre rendering, MapTiler eventuali basemap satellite, Overture Places POI, OpenTopoData elevazione, Open-Meteo weather/alerts, GTFS solo se utile. Routing OSM/Valhalla con evidenza storica di smoke; provider e disponibilità reali da verificare per release.
CamperBoss -> OSM/Overture (aree sosta, camping, servizi, POI), Open-Meteo forecast/marine se costa, GeoNames località, GTFS/trasporti, prezzi carburanti dataset nazionale; verifica qualità dei POI (non tutti hanno servizi e aperture).
Wonderlog -> Overture + Wikidata + OSM (luoghi/attrazioni), Wikimedia Commons con diritti per foto, Open-Meteo meteo viaggi, SunCalc golden hour, Shared Ecosystem Core con Anna/TrailPath.
World Days -> ONU/UNESCO/WHO/FAO come autorità, Nager.Date distinto per festivi, Commons per asset sotto licenza, catalogo editoriale versionato e source provenance.
FrameLab -> SunCalc golden hour, Open-Meteo previsioni per shooting, palette da foto/Colorwaver reference, catalogo editoriale multilingua.
GrillBoss -> Open-Meteo 'BBQ today' come feature secondaria; NO dipendenza dal meteo per guida di sicurezza alimentare; database originali tagli/temperature da fonti autorevoli.
Cooking Anime -> dataset ricette originali revisionati, immagini licenziate o create appositamente, ricerca per opere con attenzione diritti/trademark; niente scraping indiscriminato di libri.
BeerClass -> Open Food Facts quando prodotti supportati, CameraX/ML Kit, barcode decoding; dataset non necessariamente esaustivo per birre.
MealMate -> Open Food Facts + catalogo ricette originale e scadenze; dati personali local-first.
Battery Guard -> Android BatteryManager/sensori di sistema, grafici storici locali; non necessita API meteo o POI.
CleanOS -> Android package manager, local ADB/Shizuku bridge, profili OEM basati su verifica reale per modello; privacy, reversibilità e differenza fra disable/uninstall per user.
Notification Control -> NotificationListener, schedulazione e permessi Android, niente acquisizione cloud indiscriminata del contenuto privato.
SafeShare -> URL cleaning rules, EXIF parser, PDF metadata parser locale; le liste tracking vanno versionate con test.
Phone Guard -> accelerometro/prossimità, modalità background compatibili e test fisici; non serve API remota.
PDF Pocket Tools -> libreria PDF compatibile con licenza commerciale/Android, no cloud forzato.
World/Web-008 -> Open-Meteo con licenza commerciale o self-host; usare OSM/Overture per geografie e luoghi.
WEB-014 -> Open-Meteo Air Quality + OpenAQ per qualità aria e freshness, non inventare pollini mancanti.
WEB-009 -> OSM + Valhalla/OSRM + dataset carburante + provider toll dove serve; esplicitare stime.
WEB-002 -> feed ufficiali prezzi fuel per mercato; refresh timestamp.
WEB-005 -> ministero/anagrafica + feed regionale turni e orari; 'aperta ora' solo con prova dei turni.
WEB-006 -> 17TRACK/AfterShip e carrier API; valutare costi per tracking/call e privacy.
WEB-011 -> GeoNames + autorità postali; gestire variabilità copertura.
WEB-012 -> SunCalc locale, quasi nessun provider.

====================================================================
