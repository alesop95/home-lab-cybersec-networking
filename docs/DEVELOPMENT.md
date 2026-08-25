# Guida alla documentazione del lab

> Punto di ingresso ragionato all'albero `docs/`. Questo file e' scritto a mano e non viene toccato dalla rigenerazione; tutto il resto sotto `docs/`, con l'eccezione degli altri documenti curati elencati piu' sotto, e' prodotto da `tools/docx-to-md.py` a partire dal documento sorgente e va considerato di sola lettura.

## Che cos'e' questo progetto, in una riga

La progettazione documentata di una rete domestica segmentata con firewall dedicato, monitoraggio di sicurezza e servizi self-hosted, costruita sopra una linea FTTH di un operatore che non consente di sostituire il proprio modem. Il vincolo dell'operatore non e' un dettaglio marginale: e' il fatto architetturale che determina l'intera topologia, e capirlo e' il prerequisito per leggere qualunque altra parte della documentazione.

## Il vincolo che spiega tutto il resto

L'ONT dell'operatore accetta traffico solo dal MAC address del modem fornito in comodato. Una prova condotta da un fornitore, riportata nella documentazione, e la conferma esplicita dell'assistenza tecnica nel ticket di fine febbraio 2026 convergono sullo stesso esito: collegare il firewall direttamente all'ONT non funziona, e il modem dell'operatore non espone alcuna modalita' bridge, PPPoE passthrough o VLAN passthrough che permetta di aggirarlo. Da qui discende la topologia adottata, in cui il firewall sta a valle del modem invece che al suo posto, con il doppio NAT che ne consegue e con la Wi-Fi del modem che resta strutturalmente fuori dal perimetro del firewall, ragione per cui la copertura wireless viene rifatta con access point appesi allo switch a valle.

La topologia bersaglio, i suoi tre livelli e le sue due zone sono disegnati in `../.claude/context/diagrams/topologia-di-rete.md`.

## Come e' organizzato l'albero generato

Le sei cartelle numerate sotto `docs/` corrispondono alle sei sezioni di primo livello del documento sorgente, nello stesso ordine.

| Cartella | Cosa contiene | Quando leggerla |
|---|---|---|
| `01-introduzione/` | i punti di attenzione su un contratto FTTH, dalla durata al recesso al modem in comodato | prima di firmare o disdire una linea, non per lavorare sulla rete |
| `02-ftth-fastweb/` | modem e ONT, offerta, posatura della fibra, ticket all'operatore, richiesta di IP statico, lettura completa dell'interfaccia del modem, parametri di accesso WAN | ogni volta che serve capire cosa fa il lato operatore e cosa il firewall puo' o non puo' fare |
| `03-spunti-di-sviluppo/` | la parte piu' ampia: storage e NAS, server e virtualizzazione, RMM, backup, malware analysis, monitoraggio e SIEM, firewall OPNsense, DNS privato, VPN, switch, access point, VLAN, VA e pentesting, telecamere, ispirazioni esterne | e' il catalogo dei componenti del lab, si legge per componente |
| `04-concetti-generali/` | livelli 2 e 3, DHCP contro PPPoE, cablaggio fisico, telefonia su cavo dati, VLAN tagging, LAN WAN e DMZ, che cosa non e' una VPN | quando serve il fondamento teorico dietro una scelta, non la scelta stessa |
| `05-analisi-del-caso/` | censimento dei dispositivi domestici con le rispettive schede di rete | per sapere quale endpoint puo' realmente sfruttare quale velocita' |
| `06-progetto-rete-domestica-effettivamente-implementato/` | vuota nel sorgente | e' il posto della rete realizzata, oggi non ancora scritta |

Dentro ogni cartella, il `README.md` e' l'indice generato che elenca e collega i figli, quindi si naviga da li'.

## I percorsi di lettura consigliati

Per capire perche' il firewall e' dove e', si legge `02-ftth-fastweb/05-prima-del-design-della-rete-privata/` e poi `02-ftth-fastweb/07-tbc-new-i-parametri-di-accesso-wan-su-ont/`, in quest'ordine: il primo pone il problema, il secondo lo chiude con i parametri di livello 2 e 3 che servirebbero e con la ragione per cui in questa topologia non servono.

Per il firewall come apparato, `03-spunti-di-sviluppo/10-firewall-before-the-switch/` copre il confronto con le alternative, i requisiti hardware reali contrapposti a quelli dichiarati, la macchina scelta, l'installazione passo per passo e la stima del consumo elettrico. Il verbale fotografico della sessione di installazione, che e' la prova di cio' che e' stato realmente fatto e non solo pianificato, sta in `verbale-installazione-opnsense.md`.

Per la segmentazione, si parte dalla teoria in `04-concetti-generali/` sui livelli 2 e 3 e sul VLAN tagging, e si arriva alla scelta dell'apparato in `03-spunti-di-sviluppo/13-switch/`, dove sono documentate anche le due alternative scartate e il motivo per cui lo sono.

Per il monitoraggio, `03-spunti-di-sviluppo/09-monitoraggio/` descrive il workflow SIEM completo, che e' anche disegnato in `../.claude/context/diagrams/monitoraggio-open-source.md`.

## I documenti curati, scritti a mano

Questi file stanno dentro `docs/` ma non sono generati: raccolgono il materiale che non vive nel documento sorgente, oppure ne offrono una vista trasversale che la conversione per sezioni non puo' dare.

| File | Che cosa e' |
|---|---|
| `DEVELOPMENT.md` | questo file |
| `verbale-installazione-opnsense.md` | catalogo commentato delle trentuno fotografie della sessione di installazione del 16/01/2026 |
| `alternative-privacy-oriented.md` | il confronto fra servizi mainstream e alternative rispettose della privacy, che orienta la scelta di che cosa self-hostare |
| `fonti-e-materiali.md` | inventario delle fonti, distinguendo quelle pubbliche raggiungibili da quelle locali non versionate |
| `pendenze-aperte.md` | vista consolidata delle sezioni marcate come da chiarire, abbandonate o rimaste segnaposto |

## Perche' non si modifica a mano l'albero generato

La conversione e' deterministica e ripetibile: si rilancia con `python tools/docx-to-md.py "_notes/sorgenti/PROGETTO rete e networking domestica.docx" --out docs --clean` e riscrive tutto. Una correzione applicata direttamente a un file generato sopravvive fino alla prima rigenerazione e poi sparisce senza lasciare traccia, il che e' peggio di non averla fatta, perche' nel frattempo qualcuno ci avra' fatto affidamento.

Il convertitore sovrascrive i file che produce ma non svuota la cartella, quindi i documenti curati elencati sopra sopravvivono a una rigenerazione. Cio' che non sopravvive a un cambio di titolo nel sorgente e' il file generato con il vecchio slug, che resta orfano: quando si rigenera dopo aver rinominato una sezione si cancellano prima le sole cartelle numerate e il `README.md` di radice, mai l'intera cartella `docs/`, perche' li' dentro vivono anche i documenti scritti a mano. Le tre vie legittime per intervenire sono correggere il documento sorgente, aggiungere un banner in `tools/annotations.json`, oppure aggiungere una sostituzione in `tools/redactions.json` quando si tratta di anonimizzazione. Il `_CONVERSION-REPORT.md` in fondo all'albero riporta a ogni corsa i conteggi di titoli, immagini e sostituzioni, ed e' il modo per accorgersi che qualcosa e' cambiato senza volerlo.

## Le immagini

Il sorgente contiene settantaquattro immagini, estratte in cartelle `assets/` accanto ai documenti che le citano. Non sono versionate, perche' sono screenshot di interfacce reali che mostrano indirizzi, seriali e stati della linea, e perche' il `.gitignore` esclude i formati immagine per scelta. Chi clona il repository vede quindi i riferimenti alle immagini ma non le immagini: per ottenerle rigenera l'albero dal `.docx` sorgente, che resta locale. La mappa completa immagine-percorso e' nel report di conversione.
