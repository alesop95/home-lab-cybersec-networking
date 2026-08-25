# Guida alla documentazione del lab

> Percorsi di lettura per argomento. L'indice dell'albero e' `README.md`; questo file dice da dove cominciare a seconda della domanda che ci si sta ponendo. Tutto l'albero e' scritto e manutenuto a mano: la struttura viene da una conversione iniziale del documento Word, il contenuto si aggiorna qui.

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

## Come si scrive dentro l'albero

L'albero si modifica direttamente. Il documento Word da cui e' nato e' archiviato in `../_notes/sorgenti/` e non e' piu' una fonte: modificarlo non cambia niente qui, e rigenerare sopra `docs/` e' impedito da un timbro nel convertitore, che si rifiuta di sovrascrivere un albero scritto a mano.

Un elemento di studio nuovo e' un file dentro l'area pertinente, quasi sempre `03-spunti-di-sviluppo/`, aggiunto all'indice della sua cartella. Un dispositivo nuovo e' un sottotitolo dentro `05-analisi-del-caso/01-tbc-studio-dispositivi-domestici.md`, senza creare file. Un intervento eseguito davvero e' un documento trasversale nuovo, sul modello del verbale di installazione, collegato da `README.md`.

Due vincoli che non sono stilistici. I prefissi numerici sono nomi stabili, quindi per inserire si usa il primo numero libero e non si rinumera, perche' rinumerare rompe tutti i collegamenti. I valori reali si anonimizzano mentre si scrive, secondo `../.claude/rules/anonymization.md`, perche' non c'e' piu' nessuna sostituzione automatica a valle.

Dopo ogni modifica, `python tools/check-docs-tree.py` verifica che non restino documenti scollegati dagli indici ne' collegamenti che puntano nel vuoto. Il `_CONVERSION-REPORT.md` resta come documento storico della conversione iniziale, con i conteggi che ne provano la completezza, e non descrive piu' lo stato corrente.

## Le immagini

L'albero cita settantaquattro immagini in cartelle `assets/`, estratte dal documento Word durante la conversione iniziale. Non sono versionate, perche' sono schermate di interfacce reali che mostrano indirizzi, seriali e stati della linea, e perche' il `.gitignore` esclude i formati immagine per scelta. Chi clona il repository vede quindi i riferimenti ma non le immagini. Le copie locali restano sul disco dell'autore accanto ai documenti; la mappa completa immagine-percorso e' nel report di conversione.
