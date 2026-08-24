# Work-log

> Registro append-only dei passi compiuti e delle riconciliazioni fra documentazione e stato reale. Non si riscrive: si aggiunge in fondo. Le voci datate prima del 24/08/2026 sono ricostruite dalle evidenze presenti nel materiale, cioe' date scritte nel documento sorgente e metadati delle fotografie, e sono marcate come tali.

## 16/01/2026, installazione di OPNsense 25.7 (ricostruita)

Fonte: trentuno fotografie della sessione, con orari dalle 16:37 alle 17:39, piu' la descrizione della procedura nel documento sorgente.

Preparata la chiavetta con l'immagine `OPNsense-25.7-vga-amd64`, estratta con 7-Zip dall'archivio compresso e scritta con Rufus 4.11.2285, dopo verifica del checksum SHA-256 dell'archivio. Avviato l'ambiente live sulla macchina con i3 di settima generazione, 8 GB di RAM e SSD SATA da 120 GB. Rilevato durante il boot l'avviso `Generating configuration: templates...failed`, non bloccante e da riverificare sul sistema installato. Assegnata nell'ambiente live la sola interfaccia LAN, che ha ricevuto l'indirizzo di fabbrica. Selezionato il keymap italiano con prova positiva. Installato con filesystem ZFS su schema GPT con avvio ibrido, pool in stripe su disco singolo, unica opzione possibile con un solo disco. Impostata la password di root e completata l'installazione, con spegnimento a fine procedura. Durata complessiva della sessione: un'ora e due minuti.

Stato al termine: sistema operativo installato, rete non configurata. L'assegnazione a tre zone descritta nel progetto non e' stata eseguita.

Dettaglio in `docs/verbale-installazione-opnsense.md`.

## 19/01/2026, diagnostica del portatile Windows (ricostruita)

Fonte: intestazione dell'output diagnostico e sezione corrispondente del documento sorgente.

Raccolto l'output completo dello strumento diagnostico DirectX sul portatile del censimento, e analizzato un errore ricorrente della piattaforma componenti di Windows, con la sequenza di comandi di riparazione dell'archivio componenti annotata come rimedio. Il dato utile al progetto e' la parte di censimento hardware, che confluisce nella scheda dispositivi.

## 26/02/2026, apertura del ticket all'operatore (ricostruita)

Fonte: date scritte nel documento sorgente.

Aperto ticket con due richieste: conferma sulla possibilita' di interporre un firewall fra ONT e modem, e assegnazione di un indirizzo pubblico statico. La prima richiesta ha ricevuto risposta negativa. La seconda e' stata accolta, senza costi, trattandosi di profilo residenziale.

## 28/02/2026, conferma del vincolo architetturale (ricostruita)

L'assistenza conferma che non e' possibile collegare il firewall direttamente all'ONT. La conferma converge con la prova indipendente condotta da un fornitore, riportata nel documento sorgente. Da questo momento la topologia a cascata dietro il modem diventa un dato di progetto e non un ripiego temporaneo.

Contestualmente si registra un'anomalia nella lettura dello stato della connessione: l'interfaccia attiva risultava quella mobile di riserva e non la fibra, quindi i parametri di accesso letti in quella occasione non descrivono la linea in fibra. La rilettura resta aperta.

## 05/03/2026, conferma dell'indirizzo pubblico statico (ricostruita)

L'informazione sull'indirizzo assegnato non era pervenuta nei tempi indicati ed e' stata sollecitata. Ricevuta e consolidata. Da questo momento decade la linea di lavoro sull'esposizione di servizi con indirizzo dinamico e DNS dinamico, che resta nella documentazione come analisi e non come piano.

## 27/04/2026, configurazione della programmazione wireless sul modem (ricostruita)

Fonte: data annotata nel documento sorgente accanto alla sezione sulla programmazione della radio. Il contenuto della configurazione non e' descritto nel testo, che rimanda a immagini.

## 24/08/2026, riorganizzazione documentale e messa in sicurezza

Allineato il sistema di progetto al template di riferimento, che era indietro di alcuni commit: aggiornate le regole sull'identita' git e sull'economia di contesto, la scheda di sistema, due skill e i pacchetti, e istanziati il pacchetto di normalizzazione Markdown e il linter dei comandi di shell, prima assenti.

Censiti i dati reali presenti nel materiale, con scansione sistematica su indirizzi, indirizzi hardware, contatti, identificativi, numeri di serie, frammenti di ubicazione, riferimenti contrattuali e nomi propri. Il censimento dei nomi propri ha richiesto tre passaggi successivi: una prima scansione sui soli nomi fra parentesi ne ha trovati due, una scansione per coppie di parole maiuscole ne ha trovato un terzo, una scansione per soggetti di verbo e una lettura integrale del testo ne hanno trovati altri sei, fra conviventi citati come etichetta di dispositivo e autori di articoli e corsi citati come fonte. E' il motivo per cui il censimento non si fa a campione.

Costruito l'impianto di anonimizzazione: regola modulare, mappa privata dei segnaposto, file privato dei pattern, sidecar di redazione applicato in fase di conversione, guard-rail eseguibile sui file tracciati.

Modificato il convertitore rispetto alla versione del pacchetto di origine perche' applichi la redazione anche ai titoli: senza quella modifica due nomi propri finivano negli slug dei file e nei nomi delle cartelle, dove nessuna redazione del corpo li avrebbe raggiunti. Corretto inoltre il testo del report, che citava il caso studio del pacchetto di origine invece della motivazione reale, e il titolo di radice predefinito, che era quello del progetto da cui il pacchetto deriva.

Convertito il documento sorgente in 120 file Markdown, con 338 titoli su 338 preservati, 74 immagini estratte e non versionate, e cinquantaquattro sostituzioni di anonimizzazione di cui cinque su titoli. Verificata l'assenza di valori reali residui nell'albero generato, confrontando tutti i valori della mappa privata contro tutti i file prodotti.

Scritto il layer curato: hub di navigazione, verbale fotografico dell'installazione ricavato dalla lettura di tutte e trentuno le fotografie, trascrizione degli appunti sulle alternative privacy, inventario delle fonti, registro delle pendenze con cinquanta voci rilevate automaticamente, due diagrammi testuali, sei schede tecniche di contesto e la memoria di progetto con nove decisioni registrate.

Riconciliazione documentazione contro stato reale eseguita in questa sessione. Esito: la documentazione descriveva come progetto quello che il verbale fotografico mostra essere fermo all'installazione del sistema operativo. La discrepanza e' ora esplicita in `docs/pendenze-aperte.md` e nella scheda di roadmap, e non e' piu' deducibile solo leggendo tutto.
