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

## 25/08/2026, prova di completezza e riordino della radice

Prima di archiviare il documento sorgente e' stata costruita una prova di completezza della conversione, perche' il conteggio dei titoli garantisce che nessuna sezione sia sparita ma non dice nulla sul contenuto dentro le sezioni. Il confronto e' paragrafo per paragrafo, su testo ridotto a soli caratteri alfanumerici minuscoli e con le stesse redazioni applicate al sorgente. Esito finale: 1591 paragrafi su 1591 ritrovati, zero mancanti.

La prima corsa dava quarantacinque paragrafi mancanti, tutti contenenti indirizzi web, e non era una perdita: il convertitore rende un collegamento come testo fra parentesi quadre seguito dall'indirizzo fra parentesi tonde, e quando il testo visibile e' l'indirizzo stesso questo compare due volte e interrompe la corrispondenza. Il confronto e' stato corretto riducendo i collegamenti al solo testo visibile. Restano trentacinque righe di sola punteggiatura, fra cui le righe verticali dei diagrammi ASCII e i separatori del blocco whois, verificate presenti una per una invece di essere date per perse.

La verifica ha portato alla luce un difetto vero nella pulizia opzionale del convertitore. L'espressione che rimuove le righe segnaposto accettava anche il prefisso di intestazione, quindi cancellava i titoli composti da una lettera ripetuta insieme al corpo: sette sezioni finivano come file completamente vuoti mentre il report continuava a dichiararle preservate verbatim. Corretta perche' rimuova solo le righe di corpo. Un titolo segnaposto e' struttura del documento ed e' l'unica traccia che quella sezione esiste ed e' da scrivere.

Esaminato `quickprint.docx`, che era rimasto l'unica fonte dichiarata come non aperta: contiene due loghi e l'illustrazione della release, nessun contenuto tecnico. La voce in `docs/fonti-e-materiali.md` e' stata corretta da lacuna dichiarata a fatto verificato.

Riordino della radice del progetto. Tutto il materiale grezzo e' stato spostato sotto `_notes/sorgenti/`, che e' ignorato da git, con un proprio `LEGGIMI.md` che ne indicizza il contenuto e dice dove il contenuto di ciascun file e' confluito. Nessun file e' stato cancellato: l'operazione e' interamente reversibile e invisibile al repository, perche' nessuno di quei file era tracciato. Le trentuno fotografie sono state ridotte a 1600 pixel in una copia leggibile sotto `_notes/verbale-installazione-opnsense/`, da 187 a 7,5 megabyte, con gli originali conservati accanto: la riduzione non perde nulla, perche' sono scatti da telefono di uno schermo e a quella risoluzione ogni carattere resta leggibile, numeri di serie compresi.

Aggiornati di conseguenza i riferimenti al percorso del sorgente nei sette file tracciati che lo citavano, e rigenerato l'albero dal nuovo percorso per verificare che la catena funzioni ancora. I tre controlli restano verdi.

## 25/08/2026, la fonte passa dal documento Word al repository

Decisione dell'autore, registrata come ADR-010 e sostitutiva di ADR-008. Il criterio non e' il formato ma dove vive la continuita' del lavoro: se la fonte e' un binario da ventun megabyte modificabile solo in un elaboratore di testi, una sessione nuova deve ricostruirsi il contesto prima di poter lavorare; se la fonte e' il repository, la continuita' e' gia' nei file che la sessione legge comunque all'avvio.

L'albero e' stato scongelato. Rimossi i sei marcatori che lo escludevano dalla normalizzazione Markdown, perche' non e' piu' testo verbatim di una fonte esterna ma documentazione del progetto come tutto il resto, e normalizzato di conseguenza: undici file, quarantadue righe unite, nessun cambiamento di resa.

Messo un lucchetto nel codice invece che una nota nella documentazione. Il convertitore scrive nella destinazione un timbro `.generato-da-docx` e si rifiuta di scrivere in una cartella che contiene documenti senza quel timbro; congelare l'albero e' consistito nel rimuoverlo. La ragione e' concreta: la procedura di rigenerazione era scritta in quattro file diversi, e una sessione futura che ne avesse letto uno l'avrebbe eseguita in buona fede cancellando tutto il lavoro manuale. Verificato che il rifiuto scatta con codice 2 su `docs/` e che il convertitore resta funzionante su una destinazione nuova.

Scritto `tools/check-docs-tree.py`, che sostituisce la rimozione degli orfani discussa prima del cambio di modello. La feature originale serviva a tenere pulito un albero rigenerato e con il congelamento perdeva senso, mentre restava aperta una lacuna vera, gia' annotata nella scheda di verifica: nessuno controllava che i documenti fossero raggiungibili dagli indici e che i collegamenti relativi risolvessero. Lo strumento cerca esattamente quelle due cose ed e' in sola lettura, perche' un orfano puo' essere un errore o una scelta.

Alla prima corsa segnalava settantatre documenti irraggiungibili su centoventisei, ed era interamente un falso allarme dello strumento: l'espressione che riconosce i collegamenti vietava la parentesi quadra dentro il testo, mentre negli indici molte voci hanno il marcatore fra parentesi quadre premesso al titolo. Corretta, l'esito e' sceso a sei orfani reali, cioe' i cinque documenti trasversali e il report, che la home dell'albero non collegava. Riscritta la home come indice mantenuto a mano, che li include e che spiega come si aggiunge qualcosa. Esito finale: 126 su 126 raggiungibili, zero collegamenti rotti, zero orfani.

Aggiornate le istruzioni che una sessione nuova legge, perche' erano tutte scritte per il modello precedente: `CLAUDE.md`, la scheda di esecuzione, la scheda di verifica, lo stack, la regola di anonimizzazione, la home dell'albero, la guida ai percorsi di lettura, il README e l'indice di memoria. La modifica sostanziale nella regola di anonimizzazione e' che la redazione non e' piu' una regola di generazione: il contenuto nuovo si scrive gia' anonimizzato, e la voce va aggiunta alla mappa e ai pattern prima di scrivere il testo, non dopo.

## 01/09/2026, il consolidamento NAS entra nel repository, e una falla del guard-rail

La cartella `nas-consolidation/`, materiale di una sessione precedente, conteneva un `HANDOFF.md` non tracciato ma non ignorato: `.gitignore` esclude per estensione i `.txt` e i binari, non i `.md`, quindi un `git add -A` lo avrebbe pubblicato su un remoto pubblico con sei password in chiaro, i nomi propri di quattro persone e la topologia di una rete che non e' quella del lab. Il file e' ora escluso per nome.

Il fatto che conta piu' della singola svista e' che il guard-rail dichiarava zero riscontri bloccanti su quel file. La categoria `SEGRETO LETTERALE` esisteva, ma la sua lista in `_notes/.anonymization-patterns.json` era vuota, e in `nomi_propri` non c'era nessuno dei quattro nomi. E' esattamente il caso che la regola descrive come non indovinabile: lo script cerca cio' che qualcuno gli ha insegnato, e a nessuno era stato insegnato questo. Popolate entrambe le liste, quattro segreti e sette nomi, e verificato che scattino contro il testo dell'handoff. Il confronto sui segreti e' per sottostringa letterale e il riscontro si presenta come valore oscurato, quindi popolare la lista non riespone nulla nell'output. Scartato un solo candidato, una parola italiana comune di tre lettere, perche' come pattern bloccante produrrebbe falsi positivi sulla prosa.

Corretto un difetto vero nello script del guard-rail. La console di Windows apre lo standard output in cp1252, e la stampa di un riscontro contenente un emoji interrompeva il controllo con un errore di codifica invece di darne l'esito: il cancello pre-commit crashava sul file che aveva qualcosa da segnalare. Forzato UTF-8 con sostituzione dell'inrappresentabile sui due flussi.

Prodotta la versione pubblicabile del lavoro, `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/03-consolidamento-di-quattro-desktop-dismessi-in-un-nas.md`, con segnaposto propri per le quattro macchine, distinti dal censimento domestico perche' quella non e' la rete di casa. Nessuna credenziale, nessun indirizzo, nessun nome proprio: verificato per grep sui valori reali. I segnaposto sono registrati nella mappa privata, dove le password non sono trascritte: la mappa annota che il guard-rail le conosce, la loro sede resta un gestore di password.

Tre affermazioni tecniche sono state verificate sul manuale del costruttore invece di essere dedotte, e due cambiano il piano di montaggio. La prima smentisce un sospetto: sulla H170-PRO un dispositivo M.2 in modalita' PCIe non sottrae nessuna porta SATA, perche' la limitazione riguarda i soli M.2 in modalita' SATA; tutte e sei restano disponibili, e questo apre spazio a un mirror di avvio sui due SSD SATA gia' posseduti, entrambi sani e con usura nulla, al posto del disco singolo previsto. La seconda fissa l'allocazione degli slot: il secondo x16 opera a x4, che e' esattamente cio' che un NVMe usa, quindi vi va l'adattatore, e la scheda di rete va su un x1. La terza chiude una porta: la scheda dichiara memoria non-ECC, quindi l'assenza di ECC non e' un limite della CPU ma della piattaforma, e la scelta di ZFS senza ECC e' definitiva.

Corretta una raccomandazione sbagliata ereditata dall'handoff, l'uso di un NVMe come L2ARC. Quella cache serve le letture casuali che l'ARC non ha trattenuto, mentre il tetto di questa macchina e' un collegamento gigabit che un singolo disco meccanico satura gia' in sequenziale: su condivisione file e archivio il guadagno e' nullo. L'uso che rende e' un pool separato di NVMe per le applicazioni in container e le macchine virtuali.

Rilevata infine, e non corretta perche' ridefinirebbe una convenzione, un'incoerenza nel secondo dei quattro controlli: il comando documentato percorre l'intero albero di lavoro invece dei soli file tracciati, quindi resta rosso per il materiale grezzo avvolto sotto `_notes/`, che non e' versionato e non lo sara'. Sui 238 documenti tracciati e' pulito. Da decidere se restringerlo a `git ls-files`.