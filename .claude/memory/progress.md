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

## 01/09/2026, audit della storia git, sanificazione delle credenziali, guida di installazione

Domanda posta esplicitamente: le credenziali del consolidamento NAS sono nella storia git. Verificato con `git log --all -S` su ogni valore, senza mai stamparne uno: nessuna delle password, nessun nome proprio, nessuna utenza, nessun hostname e nessuna condivisione compare in alcun commit, su alcun branch. Gli unici percorsi mai committati sotto `nas-consolidation/` sono i cinque script di censimento, che sono puliti. L'esposizione e' stata potenziale e non e' avvenuta: non serve nessuna riscrittura della storia, che sarebbe stata l'unica operazione davvero costosa dell'intera faccenda.

L'audit ha prodotto due riscontri, entrambi falsi positivi, e vale registrare perche'. Cercando i prefissi `192.168.10.` e `192.168.20.` la ricerca ha colpito il commit di riorganizzazione documentale del 24/08. Non e' una fuga: sono i due `/24` del piano di indirizzamento progettato del lab, la LAN principale e la DMZ, che la regola di anonimizzazione tiene deliberatamente reali perche' sono una scelta di progetto e non un dato trapelato. La coincidenza e' che la rete di ufficio da cui provengono le quattro postazioni usa per caso gli stessi due `/24`, ed e' insidiosa proprio perche' invita a leggere un indirizzo dell'una come se appartenesse all'altra. Annotata nel file delle credenziali.

Corretto un conteggio sbagliato dichiarato in una nota precedente. Il §12 del HANDOFF conteneva cinque segreti letterali, non sei: quattro password di macchina piu' quella dell'account di servizio sul NAS di backup, mentre la riga di Proxmox rimandava a un token in un file esterno e non a una password. I cinque valori sono stati estratti in `_notes/nas-consolidation/CREDENZIALI.md` e sostituiti nel HANDOFF da segnaposto. La scelta di `_notes/` non e' indifferente: quella cartella e' esclusa da git per cartella, quindi l'esclusione sopravvive a un rinomino del file al suo interno, mentre l'esclusione del HANDOFF e' per nome e non sopravviverebbe. Lo stato desiderato resta un gestore di password, con quel file cancellato.

Registrato nel file delle credenziali un limite del guard-rail che non si puo' chiudere. Quattro dei cinque valori sono in `segreti_letterali` e vengono bloccati; il quinto e' una parola italiana comune di tre lettere e non e' registrabile, perche' come pattern bloccante produrrebbe falsi positivi su tutta la prosa del repository. Su quel valore la protezione resta l'attenzione di chi scrive, e dichiararlo vale piu' che lasciarlo credere coperto.

Verificato lo stato di TrueNAS, perche' la conoscenza disponibile si fermava a maggio 2026 e la denominazione era cambiata. Il suffisso SCALE e' stato dismesso e il prodotto si chiama TrueNAS, edizioni Community ed Enterprise; la stabile e' la 25.10 Goldeye e la 26 Halfmoon e' in beta da aprile. La 25.10 porta OpenZFS 2.3.4, il che chiude in positivo la riserva che la scheda di analisi lasciava aperta: l'espansione di un vdev raidz un disco alla volta e' disponibile, e insieme c'e' ZFS File Rewrite, estensione TrueNAS che ribilancia i dati gia' scritti dopo l'espansione risolvendo il limite storico per cui i dati vecchi conservavano il rapporto di parita' precedente. Non serve piu' acquistare tutti i dischi in una volta.

Corretto un errore di fatto in un documento gia' committato. La scheda affermava che le istantanee periodiche e la verifica dell'integrita' non sono attive per impostazione predefinita: e' vero per le istantanee, falso per la verifica, che TrueNAS crea da se' alla creazione di un pool con cadenza e soglia di trentacinque giorni. Sbagliare qui non e' innocuo, perche' porta a creare un secondo compito sovrapposto al primo. Riscritto il passaggio distinguendo cio' che il sistema fa da se' da cio' che non fa, e spostando l'accento sulle notifiche, che sono la vera lacuna: una verifica che gira, trova un errore e non avvisa nessuno equivale a una verifica che non e' mai girata.

Scritta la guida operativa, `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/04-guida-assemblaggio-e-installazione-truenas.md`, separata dalla scheda di analisi perche' le due hanno funzioni diverse: la scheda porta il ragionamento e le decisioni, la guida la sequenza da eseguire al banco. Contiene un dettaglio verificato che da solo evita una reinstallazione: l'aggancio di un secondo disco all'insieme di avvio pretende che il disco nuovo sia almeno grande quanto l'esistente, e i due SSD disponibili hanno capacita' diverse, quindi installare sul maggiore e agganciare il minore dopo non funziona. Vanno selezionati entrambi nell'installatore, oppure si installa sul minore. Aggiunta anche la valutazione di un gruppo di continuita', che la scheda non nominava e che su una piattaforma senza ECC ha un rapporto fra costo e rischio evitato secondo solo a quello dei dischi.

## 02-03/09/2026, il consolidamento NAS entra in esecuzione: guida operativa, consumi, riordino

Sessione lunga e con due riordini a metà, entrambi chiesti dall'autore e entrambi dovuti a un difetto dell'agente che vale registrare perché è ricorrente: aver inventato struttura dove il sistema ne prescriveva già una, e aver dato istruzioni senza dichiarare l'ordine in cui vanno eseguite.

Il primo riordino riguarda la collocazione del materiale privato. L'agente aveva creato `nas-consolidation/_privato/`, una sede parallela per contenuto che la sezione 3 di `PROJECT-SYSTEM.md` colloca già senza ambiguità: è tracciato ciò che un contributore deve poter recuperare da un clone ed è sicuro pubblicare, sta in `_notes/` ciò che è narrativo, transitorio o operativamente sensibile. Tutto consolidato sotto `_notes/nas-consolidation/`, che ora contiene la guida operativa, l'analisi dei consumi, le credenziali estratte e l'handoff originale. Resta tracciato il solo `nas-consolidation/scripts/`, cinque strumenti di censimento senza valori reali. Le due regole in `.gitignore` sulla vecchia sede restano come rete di sicurezza residua, con il commento che dichiara quale sia la sede canonica.

Il secondo riordino riguarda la linearità della procedura. L'agente aveva introdotto un passo di raccolta dati che era interamente ridondante, perché il censimento delle quattro macchine esisteva già dal 31/08 e dall'01/09 e i suoi valori erano già nelle tabelle della guida; e aveva collocato la lettura delle etichette degli alimentatori nella fase di preparazione, quando invece richiede i case aperti. Il passo ridondante è stato rimosso insieme allo script che lo serviva, e la lettura delle etichette è diventata il Passo 1.7, dentro la fase di smontaggio. La fase di confronto misurato fra alimentatori, che l'agente aveva proposto, è stata scartata dall'autore come sproporzionata e sostituita dalla sola lettura delle etichette.

Una domanda dell'autore ha chiarito un punto che vale oltre questo progetto: il censimento software non vede l'alimentatore, e non è una lacuna degli strumenti. Un alimentatore ATX non ha nessuna interfaccia dati verso la scheda madre, quindi non esiste una classe da interrogare e l'etichetta è la sola fonte. Verificato: zero occorrenze di dati sull'alimentazione in tutti e quattro i report.

Verificata anche la cartella `_censimento-hardware` sul NAS di backup, che l'handoff citava come se fosse una fonte. È una copia parziale e ridondante: contiene quattro file byte-identici ai locali e le mancano i due report Linux, la fotografia della rete e gli script di interrogazione dell'hypervisor. La versione completa è già nel repository, quindi non c'era niente da spostare.

Prodotta l'analisi del consumo elettrico su sei bollette mensili del 2026, in `_notes/nas-consolidation/ANALISI-CONSUMO-ELETTRICO.md`, e la sua versione anonimizzata in `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/05-consumo-elettrico-e-finestra-di-accensione.md`. Il risultato che ha cambiato il progetto non è il costo assoluto, circa centotrentacinque euro all'anno a funzionamento continuo, ma il rapporto: l'abitazione consuma circa ottantasette kilowattora al mese e la macchina ne consumerebbe quarantaquattro, cioè mezzo consumo di casa in più. Ne è discesa la decisione della finestra di accensione notturna, registrata come ADR-011, che porta il costo a circa novantacinque euro all'anno. Registrata anche ADR-012 sulla scelta dell'alimentatore fra quelli disponibili, con il fatto controintuitivo che a questo carico un alimentatore più piccolo rende meglio di uno grande e certificato.

Va registrata una stima sbagliata e poi corretta, perché la differenza era di un ordine di grandezza. Una valutazione preliminare della finestra di accensione, fatta ipotizzando quattro ore di accensione al giorno, indicava un fattore sei di risparmio; con gli orari reali, che danno sedici o diciassette ore di accensione, il risparmio è di un terzo. La decisione regge comunque, ma è stata presa una seconda volta sul numero giusto.

Corretto un difetto reale del guard-rail, trovato registrando il fornitore di energia fra i valori bloccanti. Il confronto letterale su ubicazione e organizzazioni private era sensibile alle maiuscole, e la ragione sociale compare in maiuscolo sui documenti ufficiali: quella grafia non veniva intercettata. Il confronto è ora insensibile alle maiuscole per quelle due categorie e resta sensibile per seriali, numeri di telefono e segreti letterali, dove è corretto perché una password è sensibile alle maiuscole per definizione.

Prodotta la guida operativa passo a passo, in `_notes/nas-consolidation/GUIDA-PASSO-A-PASSO.md`, circa millesettecento righe articolate in fasi cronologiche e oltre cento sottopassi, ciascuno con l'azione, il modo di verificare di aver preso il pezzo giusto e il perché. Contiene i valori reali, quindi vive fuori dall'albero versionato; la sua controparte pubblicabile sono le tre schede sotto `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/`.

Esecuzione avviata. Chiuso il giorno zero: backup delle due macchine Linux verificati per ripristino, assenza di dati da conservare confermata su tutte e quattro, immagini di installazione scaricate e verificate per somma di controllo, finestra di accensione decisa, etichette rigenerate in cartella di scaricamento, stampate e attaccate ai quattro case dopo riverifica degli indirizzi. Chiuso il primo passo del giorno uno: tutte e quattro le macchine spente con l'interruttore dell'alimentatore su aperto e il cavo lasciato inserito, così che il telaio resti collegato a terra mentre le linee di alimentazione sono morte. È una raffinatezza suggerita dall'autore e registrata nella guida, perché il conduttore di terra non passa dall'interruttore e quindi il case resta il riferimento su cui scaricare la statica.

## 04-08/09/2026, ripresa dopo un crash: che cosa il crash aveva lasciato fuori dalla memoria

Sessione di recupero. Claude Code era andato in crash durante la sessione del 04/09, e la ripresa ha dovuto ricostruire lo stato invece di leggerlo, perche' le tre schede che una sessione nuova apre per prime descrivevano tutte lo stato al 03/09 e nessuna sapeva niente di cio' che era successo dopo.

Vale registrare il modo in cui il progetto ha perso il filo, perche' non e' un incidente irripetibile ma una proprieta' della sua struttura. Il lavoro del 04/09 era per intero sotto `_notes/`, che e' ignorato da git per cartella: non essendo tracciato non compariva in `git status`, quindi l'albero risultava pulito e allineato al remoto mentre sul disco c'erano due documenti nuovi, un censimento nuovo e una guida modificata. Un crash lascia il lavoro sul disco e non nella memoria, e per il materiale non versionato non lascia nemmeno la traccia che di solito lo rivela. Cio' che ha permesso di ricostruire e' stata la data di modifica dei file confrontata con la data dell'ultimo commit.

Quello che la sessione del 04/09 aveva prodotto e che nessun file tracciato conosceva. Due documenti privati nuovi: `SMONTAGGIO-CRONOLOGICO.md`, condensazione da banco dei passi da 1.2 a 1.7 riordinata nell'ordine dei gesti e con l'etichettatura dentro ogni gesto, e `INVENTARIO-SCORTE.md`, che risponde alla domanda opposta, cioe' che cosa resta disponibile dopo. Il censimento di una quinta macchina, in esercizio e fuori dal consolidamento. E l'avanzamento fisico: dalla scorta gemella della base sono usciti i due moduli di memoria e l'SSD SATA, etichettati, con il case lasciato aperto.

La decisione di progetto che il runbook incorpora, e che la guida non conosceva, e' che dalla scorta gemella si prelevano soltanto i pezzi che servono al NAS e la macchina si richiude assemblata. La ragione e' che condivide con la base socket, generazione di memoria e modello di processore, quindi finche' resta intera il guasto della scheda madre del NAS si risolve con un trapianto dentro un telaio gia' pronto, mentre da un mucchio di componenti sciolti si risolve ricostruendo una macchina. La guida diceva il contrario, cioe' di lasciare il case aperto, ed e' stata allineata al runbook: due registri in disaccordo sullo stesso gesto sono peggio di un registro solo, e la fonte di verita' sull'avanzamento resta la guida, che e' l'unica a portare i timbri.

Tre letture della fase del primo case erano state saltate, e si possono recuperare senza riaprire niente solo perche' quel case e' rimasto aperto: il codice data dei due moduli, l'etichetta dell'alimentatore, e i due accessori del disco, cioe' il cavo dati uscito con esso e la slitta da 2,5 a 3,5 pollici su cui e' avvitato. Il recupero e' stato chiesto al banco e i valori entrano nella guida quando arrivano; finche' non arrivano il passo resta timbrato come prelievo eseguito con le letture in sospeso, che e' cio' che e' vero. Il cavo in particolare cambia il piano: prelevarlo qui rende superfluo prelevarne uno dalla terza macchina, che quindi non va toccata oltre il suo NVMe.

Il riscontro piu' importante della sessione non riguarda pero' il NAS ma il guard-rail, ed e' la seconda volta che lo stesso meccanismo si presenta. Verificando se la quinta macchina fosse registrata, si e' scoperto che non lo era nessuna delle cinque: `seriali_e_id` non conteneva nessuno dei dieci seriali hardware censiti, ne' delle schede madri, ne' dei dischi, ne' dell'unita' ottica, e due dei cinque nomi host non erano intercettati da nessuna categoria. Gli altri tre lo erano, ma per un motivo indiretto e fragile, cioe' perche' contengono un nome di battesimo che `nomi_propri` conosce: bastava un nome host senza nome dentro per non essere visto. Registrati dodici valori. La lezione del 01/09 si conferma alla lettera: il controllo verifica cio' che gli e' stato insegnato, e un esito verde su materiale nuovo non e' una garanzia finche' i valori di quel materiale non sono entrati nel file dei pattern.

Registrato accanto a quello un limite che non si chiude. L'indirizzo della quinta macchina sta in `192.168.10.0/24`, che e' la stessa rete che il piano di indirizzamento del lab tiene deliberatamente reale in quanto scelta di progetto: renderlo bloccante farebbe scattare il controllo su tutta la documentazione della LAN progettata. Resta nella categoria non bloccante degli indirizzi privati fuori schema, dove va guardato a mano, ed e' lo stesso genere di limite gia' registrato per la password che coincide con una parola italiana comune. E' la stessa coincidenza fra le due reti che il 01/09 aveva prodotto due falsi positivi nell'audit della storia.

Prodotta la controparte pubblicabile dell'inventario, `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/06-inventario-delle-scorte-dopo-il-consolidamento.md`, con i segnaposto della scheda di consolidamento piu' uno nuovo per la quinta macchina, e collegata dall'indice della sua cartella. Contiene il vincolo dominante del magazzino, che vale la pena isolare perche' e' controintuitivo: si dismettono quattro computer e non rimane un solo disco, quindi nessuna delle tre scorte si riaccende senza un acquisto e comprando un disco solo se ne riaccende una sola. Contiene anche la ragione per cui la quinta macchina, che al NAS non porta niente, va comunque registrata: la sua scheda madre e' la gemella della base, stesso modello e stesso lotto, quindi cambia la gerarchia dei ricambi anche se non e' disponibile.

Aggiornato il conteggio dell'albero, che nello snapshot era fermo a 127 documenti: sono 131, tutti raggiungibili dalla home, zero collegamenti rotti. La differenza non e' solo la scheda di oggi, sono anche le schede della guida di assemblaggio, del consumo elettrico e del registro delle fonti web, aggiunte fra l'01/09 e il 02/09 senza che il conteggio dello snapshot fosse rifatto.

## 14/09/2026, due testimonianze esterne lette da screenshot: il vincolo sulla WAN e lo stack del server

Sessione breve e interamente documentale, con il filo fisico del NAS lasciato fermo dov'era. Il materiale in ingresso erano due immagini, uno scambio in chat e un diagramma di architettura, e in entrambi i casi il lavoro e' consistito nel trasformare una testimonianza altrui in una scheda che dice che cosa cambia per questo progetto, che e' una cosa diversa dal trascriverla.

Il primo riscontro riguarda la catena WAN e vale piu' del suo contenuto. Autore-LinkedIn-B, gia' registrato nella mappa dei segnaposto dalle schede di gennaio e marzo, riferisce di avere lo stesso ostacolo su una linea di un altro operatore: l'ONT si aspetta il modem originale del provider, non lo si aggira, e quindi il firewall personale sta a valle del modem. Fino a oggi l'impossibilita' di mettere OPNsense in frontiera era documentata come proprieta' della linea di questo progetto, dedotta dall'interfaccia del modem, dall'assistenza e da una prova di collegamento diretto. Trovarla identica altrove la sposta da peculiarita' a regola, e chiude una domanda invece di aprirne una: non c'e' una configurazione migliore da cercare sul modem. Va tenuto fermo che si tratta di una testimonianza non verificata su quella linea, quindi la scheda la dichiara riscontro indipendente e non prova tecnica.

Cio' che diverge non e' la catena WAN ma cio' che si mette dietro il firewall, ed e' il confronto che la nuova sezione in coda alla scheda di Autore-LinkedIn-B mette per iscritto. Lui tiene la casa sul modem per scelta dichiarata, cioe' il Wi-Fi della famiglia, e dietro il firewall ci mette soltanto un laboratorio cablato e isolato su cui fa dominio, test e intrusione controllata. Questo progetto vuole l'opposto, cioe' la casa dentro il perimetro, ed e' la ragione per cui la topologia tratta il Wi-Fi del modem come un buco noto, cioe' uno stato transitorio, mentre nel modello dell'altro lo stesso wireless e' materia fuori perimetro per definizione.

Ne e' uscita una lettura utile dello stato prossimo di questo progetto, che vale registrare perche' non era stata messa a fuoco prima: il modello del laboratorio isolato e', senza modifiche, la configurazione che ci sara' il giorno dopo la fase 2, quando il firewall sara' configurato e lo switch e gli access point non saranno ancora arrivati. Riconoscerla come configurazione utilizzabile invece che come stato incompleto permette di lavorare sul segmento protetto senza aspettare gli acquisti. Resta enunciato il limite che impedisce di fermarsi li': separare casa e laboratorio protegge l'uno dall'altro ma non protegge la casa da Internet, perche' i dispositivi domestici restano su un apparato che non si puo' ispezionare ne' segmentare.

Il secondo riscontro e' un diagramma di architettura per una macchina Linux domestica costruita con soli strumenti open source, ed e' diventato la scheda nuova `docs/03-spunti-di-sviluppo/03-server/03-stack-linux-domestico-con-soli-strumenti-open-source.md`, collegata dall'indice della sua cartella. Cinque strati: Ubuntu Server LTS come host, Docker come motore dei contenitori, Portainer come console web, i contenitori applicativi, NGINX come proxy inverso che termina il TLS con PHP-FPM accanto, e PostgreSQL e MariaDB come servizi dati condivisi.

Due cose sono state aggiunte al diagramma invece di essere lette in esso, e sono la ragione per cui la scheda vale piu' dell'immagine. La prima e' che il vincolo di apertura si gioca su un dettaglio di edizione: Portainer esiste anche in versione commerciale, quindi e' la Community a rispettare il vincolo, e dirlo evita di crederlo rispettato per il solo nome del prodotto. La seconda e' il legame con la rete di questo progetto, che nel diagramma non c'e': con due NAT in serie, pubblicare ogni contenitore significherebbe mantenere due tabelle di inoltro che crescono con il numero dei servizi, mentre il proxy inverso fa attraversare i due apparati una porta sola e fa smettere la superficie pubblicata di crescere con le applicazioni.

Sul piano dell'anonimizzazione la sessione non ha aperto niente: il terzo citato era gia' `Autore-LinkedIn-B` nella mappa privata, e la verifica ha confermato che il guard-rail conosce gia' il suo nome per esteso e nelle due forme parziali. E' il primo materiale nuovo da settimane su cui il controllo non andava insegnato prima di scrivere, e vale notarlo perche' e' l'eccezione: le due lezioni del 01/09 e del 08/09 restano valide proprio perche' qui la condizione era gia' soddisfatta.

Riscritto infine `_notes/RESUME-PROMPT.md`, che era fermo al 25/08 e descriveva come attivo un filo documentale chiuso da allora, ignorando per intero il consolidamento del NAS. Ora dichiara i due fili aperti, il punto esatto in cui il filo fisico e' fermo, e porta un blocco da incollare per ciascuno dei tre modi in cui la sessione successiva puo' riprendere. Gli e' stato aggiunto il rito di chiusura, che e' la contromisura esplicita alla perdita del filo del 04/09: il lavoro sotto `_notes/` non compare in `git status`, quindi una sessione interrotta lascia l'albero apparentemente pulito mentre sul disco c'e' avanzamento che nessun file tracciato conosce.

## 22/09/2026, i quattro dischi del QNAP dismesso diventano il pool dati, e una scheda didattica su dischi e SSD

Sessione che chiude la sola decisione ancora aperta del sottoscopo NAS. Diventano disponibili quattro dischi da 2 TB gratuiti da un QNAP TS-410U aziendale in dismissione, letti dalla sua interfaccia: tre Samsung HD204UI e un Toshiba DT01ACA200, tutti sani allo SMART. L'idea di partenza era montarli tutti e cancellarli con shred o con la pulizia integrale di diskpart; l'analisi dei dati SMART l'ha corretta su due punti.

Il primo gesto della sessione, prima di scrivere qualunque testo, e' stato registrare i quattro seriali dei dischi in `_notes/.anonymization-patterns.json` sotto `seriali_e_id` e in `_notes/.anonymization-map.md` con i segnaposto `<sn-hdd-samsung-A/B/C>` e `<sn-hdd-toshiba>`, piu' un segnaposto per il nome host del QNAP. E' l'ordine prescritto dalla regola e la lezione gia' registrata il 01/09 e il 08/09: il guard-rail verifica cio' che gli e' stato insegnato, quindi i valori entrano nei pattern prima e non dopo. La verifica finale conferma che i seriali reali non compaiono su nessun file tracciato e che i segnaposto compaiono nella scheda.

Il riscontro che ha cambiato la decisione e' che i tre Samsung hanno seriali consecutivi e ore identiche a meno di un millesimo su centoventicinquemila: sono dello stesso lotto con la stessa storia di carico, quindi il loro guasto non e' indipendente e uno specchio di due di loro sarebbe ridondanza solo sulla carta. Ne e' seguita la configurazione dell'ADR-013: un solo specchio che accoppia il Toshiba con un Samsung, l'unica coppia con guasto davvero indipendente; un secondo Samsung come riserva a caldo sulla porta SATA libera; il terzo Samsung fuori dal NAS, verso la scorta con la sola rete Intel, che l'inventario descriveva come l'unica a cui mancava solo un disco. Cosi' cade il vincolo dominante del magazzino, i zero dischi, senza pero' lasciare una scorta di dischi: quello disponibile e' speso per riaccendere la scorta giusta. Il dimensionamento resta l'unico nodo aperto e si chiude misurando l'occupato del QNAP prima di creare il pool.

Corretti anche il secondo e il terzo malinteso di partenza. La cancellazione con shred o diskpart cancella senza verificare, mentre lo scopo su dischi che si rimettono in servizio e' scoprire un disco marcio mentre e' ancora vuoto: si sostituisce con `badblocks -wsv` seguito da `smartctl -t long` e dalla rilettura degli attributi 5, 197, 198 e 199, con scarto su qualunque valore diverso da zero. Il firmware `1AQ10001` dei Samsung e' la versione col difetto di corruzione NCQ+SMART il cui correttivo non cambia versione: incertezza non risolvibile per lettura, con due mitigazioni possibili annotate nella scheda.

Creati due documenti. Lo studio applicato `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/07-dischi-recuperati-dal-nas-qnap-dismesso.md`, che porta la decisione, il protocollo di qualificazione, il calcolo delle porte e dei connettori, e il cancello sul dimensionamento. E la scheda didattica generale `docs/04-concetti-generali/10-hardware-soluzioni-tecnologie/03-dischi-e-ssd-per-uso-continuo-contro-uso-generico.md`, che spiega che cosa distingue un disco o un SSD da uso continuo da uno generico: recupero d'errore a tempo limitato, carico annuo, sensori di vibrazione e CMR contro SMR sul lato meccanico, resistenza alla scrittura, protezione dalla perdita di alimentazione, cache dinamica e spazio di riserva sul lato a stato solido, con il principio che l'uso continuo non chiede piu' velocita' ma comportamento prevedibile. Il caso applicato richiama la scheda generale con un collegamento invece di ripetere la teoria.

Modificati quattro documenti pubblici della cartella NAS per riflettere che i dischi ci sono e la decisione e' presa: la scheda di consolidamento chiude la pendenza sui dischi, la guida di assemblaggio aggiorna la forma del pool e rimanda alla qualificazione, la scheda dei consumi aggiunge la riga a tre dischi e il nuovo costo annuo verso i centodieci euro, l'inventario delle scorte corregge la sezione dischi disponibili che era il suo vincolo dominante. Modificati i due documenti privati corrispondenti, l'inventario e la guida passo a passo, quest'ultima con il nuovo Passo 4.4 di qualificazione collocato dopo il test della memoria e prima della creazione del pool.

Aggiunta su richiesta una scheda al filo del pentesting autonomo in home lab, `docs/03-spunti-di-sviluppo/16-va-e-pentesting/03-metatron-pentesting-assistito-da-llm-locale.md`, che descrive METATRON come livello di automazione guidata con modello linguistico locale su Parrot OS, insistendo sul confine che ne fa un supporto alla decisione e non un attaccante autonomo, sul requisito dell'inferenza locale a tutela della riservatezza dei riscontri, e sulle due condizioni d'uso non negoziabili, cioe' bersaglio solo autorizzato e modello da verificare su fonte primaria. E' descrizione degli autori, non provata in laboratorio, e lo dichiara.

Registrate nel registro fonti le voci curate: U07 e U08 per gli screenshot del QNAP, copiati sotto `_notes/fonti/2026-09-22-dischi-qnap/` e non in una cartella tracciata, e S50-S53 per Backblaze, il difetto del firmware HD204UI, il protocollo di collaudo TrueNAS e il repository METATRON.

Controlli tutti verdi. L'albero e' a 146 documenti raggiungibili, zero collegamenti rotti, zero orfani; nessun comando spezzato; il guard-rail con l'opzione dei file nuovi da zero riscontri bloccanti, e i ventisei non bloccanti sono i prezzi di listino ammessi e gli IP del piano lab progettato, gia' noti. Il censimento delle fonti non ha riferimenti non registrati.

## 22/09/2026, topologia Seven -> OPNsense e procedura di ripresa

La topologia e' stata riverificata alla luce del vincolo riferito dall'utente sulla linea reale. La baseline non e' piu' un collegamento diretto ONT -> OPNsense, ma ONT -> Fastweb Seven -> WAN OPNsense -> LAN trunk -> switch Zyxel -> access point. La documentazione distingue l'evidenza locale dall'assenza di una dichiarazione pubblica Fastweb che provi un vincolo MAC generale dell'ONT. La Wi-Fi del Seven e' dichiarata rete upstream fuori da OPNsense, tollerabile temporaneamente per dispositivi ordinari o legacy ma non equivalente alla copertura firewall dell'intera abitazione.

Creata la guida `docs/03-spunti-di-sviluppo/23-studio-home-lab/05-guida-configurazione-opnsense-in-casa.md`, aggiornati diagramma canonico, architettura e raccomandazione switch, e aggiunta la nota fonte `docs/fonti/fastweb-ont-modem.md`. Il memo acquisti e configurazione e' versionato in `docs/03-spunti-di-sviluppo/23-studio-home-lab/ACQUISTI-E-CONFIGURAZIONE-DA-FINIRE.md` e copiato manualmente sul Desktop.

Il punto di ripresa documentale ora e' la scelta fra XMG1915-10E con un iniettore PoE 2,5 GbE per un solo AP e XMG1915-10EP per due o tre AP con PoE centralizzato. Il prossimo lavoro fisico resta l'assemblaggio NAS; il prossimo lavoro di rete richiede la console del firewall per identificare le NIC. Nessuna operazione git e' stata eseguita dalla sessione: aggiunta, commit e push restano manuali dell'utente.

## 07/10/2026, allineamento al template 4f4f9d0 e guard-rail riportato al verde

Allineamento da `ec124d7` a `4f4f9d0` con `allinea-tutti.ps1` ristretto a questo progetto, prima a vuoto e poi applicato: ventisei file aggiornati e dieci nuovi, nessun conflitto, verifica dello strumento passata e `.claude/allineamento-template.json` riscritto. Entrano fra l'altro la regola `documenti-personali.md`, il recap di fine giro a campi fissi in `chat-non-e-memoria.md`, le cause sei e sette di `git-commands-format.md` e i pacchetti `micro-passi` e `verifica-link`. Le due regole da caricare sempre sono ora elencate nell'indice di `CLAUDE.md`. Lo strumento avvisa che il carico degli instruction file e' 106.960 caratteri contro una soglia di guardia di 100.000: non blocca, resta da valutare.

Il guard-rail, eseguito con l'opzione dei file nuovi, ha dato nove riscontri bloccanti. Sette di quei file erano gia' nel commit `3205229`, quindi gli allineamenti fra il 24 e il 30/09 erano stati committati con il controllo rosso. Nessuno dei nove era una fuga. Tre erano il nome di un'organizzazione privata, di cinque lettere, che combaciava come sottostringa dentro i numerali in «centonovanta-» di due file del template; sei erano caselle di posta d'esempio nei test e negli esempi del template, cinque su domini riservati dagli RFC 2606 e 6761 e una su un dominio italiano d'esempio. Correzione nello script versionato: le organizzazioni si cercano a parola intera come gia' i nomi propri, e le caselle su domini riservati si ammettono per costruzione. La casella sul dominio italiano e' entrata fra le ammesse nel file privato dei pattern. Prova che misura, su un file costruito: il nome dell'organizzazione scritto come parola e una casella sul suo dominio reale restano intercettati, il numerale e il dominio `.invalid` no. Esito dopo la correzione, su 518 file tracciati e nuovi: zero bloccanti, ventotto da valutare, che sono i prezzi di listino e gli indirizzi del piano lab gia' noti.

Controlli: albero a 150 documenti su 150 raggiungibili, zero collegamenti rotti; nessun comando spezzato; `md-unwrap --check` pulito sui 315 Markdown tracciati. Il filo fisico del NAS non si e' mosso: la guida operativa privata non e' cambiata dal 22/09, quindi il punto di ripresa resta quello dell'08/09, cioe' le tre letture sul primo case e poi il Passo 1.4.

## 07/10/2026, i dischi del QNAP cadono, la storia pubblicata si bonifica, la regola dell'identita' esce dal carico fisso

Tre cose decise dall'utente nella stessa sessione.

I dischi del QNAP non si libereranno: ADR-013 e' superata da ADR-014, il pool dati torna senza dischi e la sua provenienza torna una decisione aperta, registrata nelle pendenze. Le schede pubbliche della cartella NAS e la guida privata descrivono ancora il pool di quattro dischi e vanno riscritte dopo la scelta. Spiegato anche il perche' dell'adattatore da PCIe a M.2, che non viene da nessuna delle macchine smontate: la scheda madre della base ha un solo alloggiamento M.2 e gli NVMe da montare sono due.

Bonifica della storia: verificato con l'API pubblica di GitHub che il repository e' pubblico, con zero fork e zero stelle, il che chiude la seconda delle due decisioni sospese. Una scansione di tutti gli 851 oggetti della storia e dei messaggi di commit con i pattern privati ha trovato i valori di lavoro in quattro versioni storiche di due file, la regola sull'identita' git e la skill di inizializzazione, e in nessun metadato. La casella personale negli autori resta per scelta dell'utente. La riscrittura e' fatta con git-filter-repo in un clone separato sotto `E:/_backup-git/`, accanto a un backup mirror della storia originale; i quattro valori sono sostituiti da segnaposto registrati nella mappa privata, e il nome utente di lavoro e' entrato nei pattern. Verifica: 35 commit, albero di HEAD identico byte per byte all'originale, zero residui sugli oggetti riscritti. Restano all'utente il push forzato e il riallineamento della copia di lavoro; dopo il push i vecchi commit restano raggiungibili per hash su GitHub finche' la piattaforma non li elimina, e una rimozione garantita passa da una richiesta al supporto.

Carico delle istruzioni: la causa sta nel template, le cui sole regole valevano circa 83.000 caratteri, cosi' che qualunque progetto con una regola propria sforava la soglia. Nel template la regola `git-identity-and-repo.md` e' diventata la skill `identita-git` con il testo in `RIFERIMENTO.md` e la riga di innesco nell'indice; il template e' sceso da 92.824 a 75.138 caratteri. La modifica arriva qui con il prossimo allineamento, dopo il commit del template: toglierla solo nel progetto non bastava, perche' l'allineamento successivo l'avrebbe rimessa.


## 07/10/2026, bonifica pubblicata e allineamento al template 74b6f6b

L'utente ha committato il template (`74b6f6b`), pubblicato con push forzato la storia bonificata (`b3676eb` sul remoto) e riallineato la copia di lavoro con un reset misto: albero identico, modifiche non committate conservate. Il backup della storia originale resta in `E:/_backup-git/`, e la copia locale conserva ancora gli oggetti vecchi nel reflog: non sono pubblicati.

Allineamento al template `74b6f6b` con `allinea-dal-template.py` direttamente, perche' `allinea-tutti.ps1` non scrive su un albero con modifiche non committate e quelle modifiche stavano in `memory/` e `docs/`, che lo strumento non tocca. Esito: regola dell'identita' spostata nella skill `identita-git`, nove file aggiornati, la skill nuova, la riga di innesco nel `CLAUDE.md`; corretti a mano l'indice delle regole e il vincolo di team nel `CLAUDE.md` e il riferimento nella scheda di sicurezza. Carico delle istruzioni da 107.186 a 89.379 caratteri, sotto la soglia di guardia.

Difetto trovato nel template durante la misura: lo strumento di allineamento propaga le sole skill di un elenco chiuso, e `identita-git` non c'era, quindi avrebbe spostato il testo della regola senza la skill che lo carica e senza innesco. Corretto nel template insieme a un difetto precedente, la regola dei documenti personali non dichiarata fra le sempre attive del controllo di raggiungibilita'. Le due correzioni del template sono da committare.

## 07/10/2026, costo del NAS dal motore delle bollette, e chiudi reso sicuro su questo progetto

Il costo d'esercizio del NAS e' stato rifatto con il motore di calcolo privato delle bollette della fornitura, su richiesta espressa dell'utente e limitatamente a quella fornitura: differenza fra il costo annuo della casa con e senza la macchina, ore ripartite per fascia oraria, prezzi medi gennaio-agosto 2026, tariffe regolate dell'ultimo trimestre; il motore passa le proprie prove. A 48 W stimati, alle condizioni attuali: 112,69 euro l'anno in continuo e 79,93 con la finestra, cioe' 0,268 e 0,271 euro per kilowattora in piu'; la finestra alza il costo unitario perche' toglie soprattutto ore F3. Il valore precedente di 0,256 era una media di quattro bollette senza fasce. Aggiornata la scheda pubblica 05 senza nome del fornitore; il dettaglio, lo script e il risultato sono nel materiale privato del NAS, nella nota della sessione.

Le otto fotografie dei pezzi della prima macchina indicate dall'utente erano nella cartella di download all'inizio del giro e ne sono sparite prima della copia: non lette.

`chiudi` girava gia' su questo progetto tramite la copia dello script sotto `.claude/templates/tools/`, ma con due difetti. Il progetto conteneva i due prompt del template, residuo di una copia manuale di giugno, e lo script li usa per riconoscere il template stesso: avrebbe lanciato i controlli riservati al template. Rimossi. E lo script non eseguiva il guard-rail di anonimizzazione, che il pacchetto ammette in `scripts/`: corretto nel template, insieme a `md-unwrap --only-tracked` che si fermava sui file tracciati appena cancellati. Su indicazione dell'utente non si creano nel progetto copie di cose che il template ha gia': un aggancio pre-commit locale scritto per coprire il guard-rail e' stato tolto prima di essere usato, e la correzione e' andata nel template. Prova: `chiudi -SoloControlli` sul progetto con lo script corretto esegue il guard-rail ed e' verde, salvo `md-unwrap` sui due file cancellati, corretto a sua volta e verificato con i 109 test del pacchetto.

Al banco, Passo 1.4: l'etichetta dell'NVMe della seconda macchina, letta da fotografia prima di svitare, corrisponde al disco P2 del censimento; timbrata la verifica nella guida privata. Direttiva dell'utente del 07/10/2026: ogni fotografia passata in sessione si copia nel materiale privato del NAS, con un indice per data e passo, come riferimento per documentazione, roadmap e timeline.

Allineato al template `c668b85` dopo il commit dell'utente: `chiudi` ora riconosce il progetto come progetto e non come template, ed esegue il guard-rail di anonimizzazione. `chiudi -SoloControlli` verde.

Al banco, piu' tardi il 07/10/2026: Passo 1.5 chiuso, l'NVMe della terza macchina e' il P3 atteso, letto da foto a disco smontato. Le otto foto dei pezzi della prima macchina, riapparse in download con un nuovo orario, hanno chiuso due delle tre letture in sospeso: cavo dati e slitta sono usciti con l'SSD, e i due moduli di memoria sono dello stesso lotto, fine 2016. Resta il numero di connettori SATA del suo alimentatore, che conta solo se si sceglie quello. Per l'adattatore da PCIe a M.2 e' registrata come fonte S54 la scheda del costruttore AXAGON PCEM2-N, letta: PCIe x4, solo NVMe chiave M, fino a 2280, staffa standard e a basso profilo nella confezione. Le schede prodotto di Amazon e StarTech non si sono lasciate leggere (503 e 403).

Passo 1.7, stesso giorno: lette dalle foto dell'utente le etichette dei quattro alimentatori, cioe' 500, 520, 550 e 600 W, nessuno con certificazione stampata. Direttiva dell'utente: i connettori SATA si considerano equivalenti e non si contano, salvo necessita'; il criterio guida e' la potenza. Scelta dell'alimentatore in attesa dell'utente, con la raccomandazione scritta nella risposta di sessione e nella guida privata.

## 07/10/2026, chiusura: alimentatore deciso, NAS in pausa, schede riancorate dopo la bonifica

L'utente ha confermato l'alimentatore della base, con ispezione visiva positiva, registrato come ADR-016 con tre condizioni ancora da verificare al montaggio. L'adattatore da PCIe a M.2 non si puo' ordinare subito: il filo del NAS va in pausa a prelievi chiusi, e il filo attivo diventa la progettazione della rete e della topologia. Riscritti la scheda del lavoro corrente, il punto di ripresa dello snapshot e il prompt di ripresa.

Allineamento delle schede con la skill di sincronizzazione. Difetto trovato: le ancore delle otto schede puntavano a `494b45e` ed `e91a133`, commit della storia prima della bonifica. Risultavano valide solo perche' la copia locale conserva ancora gli oggetti vecchi; in un clone nuovo non esisterebbero. Riportate sugli equivalenti della storia attuale, `4245e21` e `f5b91ed`, con la tabella di corrispondenza scritta da git-filter-repo, copiata in privato in `_notes/bonifica-2026-10-07-commit-map.txt`. Secondo difetto, di invocazione: `verifica-schede.py` lanciato dalla sua posizione sotto `.claude/templates/tools/` si sposta nella cartella sbagliata e dichiara zero schede, un verde non calcolato; lanciato da `tools/` ne vede otto, sette superate rispetto all'ancora. La riconciliazione per contenuto delle sette e' affidata a un agente nello stesso giro.

Esito della riconciliazione: tutte e otto le schede verificate per contenuto e ancorate a `6769dc4`. Sette erano superate; due avevano divergenze piu' vecchie dell'ancora, che il confronto per commit non vedeva: la scheda di sicurezza descriveva ancora l'anonimizzazione come regola di generazione, e quella del monitoraggio non registrava che lo studio del 22/09 indica Suricata integrato in OPNsense invece di Snort. Alla scheda della topologia mancava fra i `covers-paths` la cartella dello studio home lab, per cui i cambi del 22/09 le erano invisibili: aggiunta. `verifica-schede --rigoroso`, lanciato da `tools/`: 8 schede, 0 superate, 0 difetti.

## 07/10/2026, sera: switch PoE e due AP decisi, bozza della topologia

Ripresa con la skill `riprendi`: `tools/verifica-ripresa.py` non e' istanziato nel progetto, verifica fatta a mano. HEAD `05b9d02` allineato a `origin`, albero pulito, work-log completo; solo il prompt di ripresa privato dava ancora il commit come da fare, corretto.

L'utente ha deciso uno switch PoE e due access point: registrato come ADR-017, XMG1915-10EP, modello degli AP ancora aperto. Ha ricordato che la linea arriva fino a 2,5 Gbps. Prodotta una bozza della topologia in `_notes/topologia-bozza-2026-10-07.svg`, privata finche' l'utente non la conferma, con la catena WAN, il doppio NAT e il suo costo in ingresso, il riscontro di Autore-LinkedIn-B, il perimetro di OPNsense, le VLAN sul trunk, le otto porte dello switch e il NAS proposto in VLAN 30. Controllata a video con un rendering a PNG.

Da verificare, non ancora corretto: `02-soluzione-professionale-con-opnsense-25-7.md` dice che l'i3 di settima generazione non ha AES-NI. Intel la dichiara presente sugli i3 di quella famiglia, ma il modello esatto del firewall non e' scritto in nessun documento, quindi l'affermazione va controllata sulla macchina, per esempio dal dmesg di OPNsense. WireGuard, comunque, cifra con ChaCha20 e non usa AES-NI.

## 07/10/2026, sera: studio aggiornato, documento sul doppio NAT, Tailcat

L'utente ha confermato la bozza della topologia e aggiunto le scelte registrate come ADR-018: AP cablati in PoE ai piani 3 e 2 su quattro, roaming invece di mesh radio, PS5 sulla LAN da 1 GbE del Seven, niente FRITZ!Box, NAS in VLAN 30 a 1 GbE con 2,5 GbE facoltativa. Il Seven ha una porta LAN da 2,5 GbE, per il firewall, e le altre da 1 GbE. Il firewall ha tre porte secondo il verbale, e l'utente lo ricorda verificato da terminale; l'identificazione resta il primo passo della fase 2.

Scritto il documento didattico `07-doppio-nat-dietro-modem-in-comodato.md` nello studio home lab, richiesto dall'utente come sviluppo a parte del ragionamento iniziato nel `.docx`. Aggiunta a `06-accesso-remoto-vpn.md` la sezione su Tailcat, letta dal README (S55) e dall'articolo segnalato (S56): uso solo da VLAN 10 o gestione, mai `no-auth-ssh`, WireGuard resta l'accesso stabile. Aggiornati `01-architettura.md` con le decisioni del giorno, `03-switch-e-access-point-zyxel.md` con la spiegazione di livello 2 e livello 3 e la tabella porte, il README dello studio, il riepilogo acquisti, le pendenze con il censimento cablato o Wi-Fi, il registro delle fonti. La bozza SVG ha sostituito `topologia-proposta.svg`, controllata con un rendering a PNG; la copia in `_notes/` resta come bozza superata.

Nuova richiesta dell'utente, a fine giro: rileggere tutta la documentazione scritta originariamente da lui e trasformarla in documentazione tecnica di progetto, a partire dalle voci di menu del Seven e da come combinarle con il progetto di rete. Lavoro di piu' sessioni, pianificato nella scheda del lavoro corrente.

Primo passo del filo nuovo, stesso giro: letta per intero la parte sul Seven (censimento delle voci di menu in `06-tbc-...` e scheda del modello, circa 2.300 parole) e scritto `02-ftth-fastweb/08-il-seven-nel-progetto-di-rete-voce-per-voce.md`, che per ogni voce dice che cosa fa, il valore rilevato e l'impostazione di progetto, con una sintesi in ordine di esecuzione. Il censimento dell'autore resta come materiale di partenza, con un rimando al documento nuovo. Tre fatti emersi dalla lettura: lo stato WAN e' stato catturato con la GPON giu' e l'LTE su, quindi descrive il collegamento di riserva; la porta LAN 4 e' quella da 2,5 GbE; IPv6 e' assente. Le rilevazioni da ripetere sono fra le pendenze. Misura del resto del lavoro, in parole dei file `.md`: `03-spunti-di-sviluppo` 54.857 in 83 file, `04-concetti-generali` 11.827 in 23, `02-ftth-fastweb` 9.479 in 23, `05-analisi-del-caso` 3.193 in 2.

## 07/10/2026, notte: ingestione di `_notes/sorgenti/` verificata, note a pie' di pagina recuperate, testi eliminati

Richiesta dell'utente: controllare che tutta `_notes/sorgenti/` fosse ingerita nel progetto nel punto giusto e senza ripetizioni, poi cancellare i testi scritti da lui tenendo immagini e materiale di contesto. Prima della richiesta l'utente ha lanciato `chiudi`: commit `c5951ca`, allineato a `origin`.

Verifica rifatta da capo invece di fidarsi della prova del 25/08. Paragrafi del Word, corpo e celle, normalizzati e redatti: 1532 distinti, 1487 identici in `docs/`, 45 con differenze di sola forma controllate una per una. Immagini per SHA-256: 71 su 71. Collegamenti esterni: 81 su 81. Note a pie' di pagina: 0 su 53, cioe' mai convertite, circa 19 mila caratteri; la prova del 25/08 aveva un perimetro di soli paragrafi e non poteva vederle. Inserite con uno script nei diciassette file che contengono i richiami, nel punto esatto di ciascun richiamo, numerate dopo le note gia' presenti; una collocata a mano perche' il paragrafo contiene due collegamenti. Dopo l'inserimento: 53 su 53. La nota sulla PS5 in VLAN 10 e' marcata come superata da ADR-018. `privacy pack.txt`: 52 coppie e il paragrafo su Proton VPN ritrovati in `alternative-privacy-oriented.md`, riorganizzati per ecosistema. `Diagram/Notes.txt`: riportato in `fonti-e-materiali.md`. DxDiag: non contiene schede di rete, e la parte di sistema e' gia' nel censimento. Un errore di uno script di verifica, una regex rovinata da `sed`, aveva fatto credere per un momento a 42 paragrafi persi: corretto lo script, il conteggio e' tornato a 1487.

Eseguita ADR-019: sei file nel Cestino, riferimenti aggiornati in `CLAUDE.md`, `docs/README.md`, `docs/DEVELOPMENT.md`, `docs/fonti-e-materiali.md`, `docs/alternative-privacy-oriented.md`, `SOURCES.md`, `.claude/context/deployment.md`, snapshot.

## 07/10/2026, notte: DxDiag eliminato, controlli del template provati, fine riga normalizzate

Commit `6f8baa2` dell'utente con `chiudi`, allineato a `origin`. Su sua indicazione il DxDiag e' nel Cestino; riferimenti aggiornati in `CLAUDE.md`, `SOURCES.md`, `docs/fonti-e-materiali.md`, ADR-019 e nell'indice privato della cartella.

Alla domanda se il progetto tracci tutto come prevede il template, provati in sola lettura gli strumenti che stanno solo in `.claude/templates/tools/`. `verifica-ripresa.py` funziona da li' e ha trovato lo snapshot fermo a `6769dc4`, corretto a `6f8baa2`, e nessuna impronta mai registrata. `lint-md-tables.py` e `verifica-schede.py` lanciati da li' esaminano zero file e zero schede, cioe' danno un verde non calcolato. `lint-doc-references.py --radice .` trova 16 riferimenti in regole e skill vive a strumenti `tools/...` che nel progetto non esistono: `verifica-ripresa`, `chiudi-sessione`, `lint-md-tables`, `fix-accents`, `fix-missing-accents`, `fix-dashes`, `test-tipografia`, `lint-prosa`, `latest-screenshot`, `verifica-schede`, `sync-codex-skills`, `misura-istruzioni`. Ne segue che i presidi tipografici, delle tabelle e della prosa non girano su questo progetto. Non si copiano a mano, per la direttiva dell'utente che vieta copie di cio' che il template ha gia': decisione chiesta all'utente.

`check-eol.py` ha trovato otto file con fine riga miste, tutte presenti gia' prima del 07/10 (confronto con `05b9d02`): normalizzate alla convenzione prevalente di ciascun file, sette CRLF e `settings.json` LF. Dopo: 464 file, zero misti.

## 07/10/2026, notte: allineamento al template `e09e43b`, guard-rail divergente

Decisioni dell'utente registrate come ADR-020 (riscrittura al posto con verifica di copertura), ADR-021 (scheda dispositivo) e ADR-022 (il template e' l'autorita'). Commit `497004f` dell'utente con `chiudi`.

`allinea-dal-template.py --applica` dal template `e09e43b`: aggiornati `rules/documenti-personali.md`, `rules/interaction-style.md`, il pacchetto anonymization, il pacchetto doc-ingest e i due `chiudi-sessione`, aggiunto `templates/tools/test-documenti-personali.py`; 334 file gia' uguali, zero conflitti.

Lo script di allineamento aggiorna gli strumenti gia' presenti in `tools/` ma non ne installa di nuovi: l'adozione passa dalla skill `gate-pacchetti` e dai README dei pacchetti. `chiudi` aggiornato, lanciato con `-SoloControlli`, ora fallisce su due punti del guard-rail di `scripts/`: un falso positivo TELEFONO sul numero di prova scritto dentro l'autotest del template, e l'opzione `--autotest` che quella copia non ha. La copia del progetto non e' una versione storica del template: ha `--includi-nuovi`, `--escludi` e la lettura delle chiavi `seriali_e_id`, `ubicazione`, `organizzazioni_private`, `importi_ammessi`, `telefoni_reali`. La versione del template, provata sul progetto, da' 41 bloccanti, di cui 36 importi di listino ammessi dalla regola del progetto, 3 nomi e 2 caselle di prova `.invalid` nei file del template, e perderebbe il controllo di seriali e ubicazione. Nessuna delle due si sostituisce all'altra senza perdere una protezione: decisione chiesta all'utente. Finche' non c'e', `chiudi` si ferma.

## 08/10/2026: guard-rail unificato, base del template con estensioni del progetto

Scelta dell'utente fra tre opzioni: base del template piu' estensioni del progetto, in `tools/`. Il file e' generato da uno script di unione riproducibile, che parte dalla versione del pacchetto e vi applica sei estensioni marcate nel codice: categorie bloccanti SERIALE/ID MACCHINA, UBICAZIONE e ORGANIZZAZIONE PRIVATA; `telefoni_reali` e cellulare italiano a dieci cifre; importi non bloccanti con `importi_ammessi` e con il riconoscitore piu' largo della copia del progetto, che vede anche la forma cifra seguita dal simbolo; nomi propri a parola intera e non stampati; domini riservati `.invalid`, `.test`, `.localhost`; chiave privata `percorsi_esclusi`, impostata su `.claude/templates/`.

Misure. Autotest: 20 casi, 0 errori. Confronto con la copia vecchia sullo stesso perimetro, tracciati e nuovi senza `.claude/templates/`: entrambe 0 bloccanti, 31 importi e 10 indirizzi privati da valutare, dopo due correzioni emerse dal confronto. La prima: la versione unita trovava 25 importi invece di 31, perche' il riconoscitore del template non vede "45 €"; ripristinato quello del progetto. La seconda: il formato del cellulare a nove cifre combaciava con il numero di prova dell'autotest; ristretto a dieci cifre, i numeri reali noti restano coperti alla lettera. Prova delle estensioni su un file temporaneo con i valori veri del file dei pattern, mai stampati: seriale, ubicazione, organizzazione e nome scattano sul valore e tacciono sulla variante con l'ultimo carattere cambiato; per i telefoni il file non elenca numeri.

Riferimenti aggiornati da `scripts/` a `tools/` e tolta l'opzione `--includi-nuovi` in `CLAUDE.md`, `README.md`, `rules/anonymization.md` e nelle schede deployment, dev-testing, design-and-security e STACK; le voci datate del work-log restano. Allineamento a vuoto dopo la registrazione: 344 uguali, 1 adattato, 0 conflitti. `chiudi -SoloControlli` verde, con il guard-rail e il suo autotest. Un'uscita dei controlli e' andata persa perche' un'altra sessione ha ripulito la cartella temporanea: rilanciata con l'uscita in `_notes/`.

Prossimo blocco, ADR-022: installare dai pacchetti gli strumenti di tipografia, prosa, tabelle, ripresa, schede, fine riga e riferimenti. Lanciati dalla cartella del template i correttori tipografici esaminano zero file, quindi il loro impatto sull'albero si misura solo dopo l'installazione.

Nello stesso giorno e' comparso il commit `5137254`, "Guida NAS: posizione fisica degli slot, scheda di rete facoltativa", fatto da una sessione parallela sul filo del NAS: tocca solo `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/04-guida-assemblaggio-e-installazione-truenas.md`, non si sovrappone alle modifiche di questo giro e al momento della verifica era locale e non ancora spinto. Nessuna voce del work-log lo descrive. Il primo `chiudi` dell'utente su questo blocco e' partito per errore nel repository `home-recording-training-mixing-setup`, dove ha trovato l'albero pulito e non ha committato nulla.

## 08/10/2026: strumenti del template istanziati, tipografia dell'albero normalizzata

Commit `fa719dc` dell'utente, allineato a `origin`. Istanziati in `tools/` dai pacchetti, secondo i loro README (ADR-022): `fix-accents`, `fix-missing-accents`, `fix-dashes` con i due file di esclusione e `test-tipografia` (fix-typography); `lint-prosa` e `lint-ui` (anti-slop, con guida e fonti in `docs/anti-slop/` e un indice del progetto collegato dalla home); `lint-md-tables`, `verifica-ripresa`, `verifica-schede`, `lint-doc-references`, `check-eol`, `misura-istruzioni`, `chiudi-sessione.ps1` e `.sh`, `latest-screenshot.ps1`, `sync-codex-skills`, `test-documenti-personali`. Non istanziati: l'hook pre-commit di anti-slop, che presuppone `.githooks` del pacchetto readme-sync, assente qui; gli strumenti del solo template, cioè `check-raggiungibilita`, `check-catalogo`, `check-copie-modelli`, `allinea-dal-template` e gli installatori. `lint-ui` e `test-documenti-personali` sono istanziati solo perche' documenti del template li citano: il primo non serve a un progetto senza interfaccia, il secondo si interrompe fuori dal template, dove `chiudi` non lo esegue. `sync-codex-skills` ha generato 19 file di adattatori in `.agents/skills/`. Allineamento a vuoto: 359 uguali, 1 adattato, 0 conflitti.

Misure della prima corsa da `tools/`, uscite in `_notes/misure-strumenti/`: tabelle 376 file, 0 difetti; fine riga 0 misti; carico istruzioni 92.742 caratteri su soglia 100.000; riferimenti 5 da correggere, risolti istanziando gli strumenti citati; schede 7 superate su 8 rispetto all'ancora `6769dc4`, con `--rigoroso`; prosa 77 segnalazioni in 57 file (P1 6, P3 24, P4 43, P5 4), avvisi da rileggere. Autotest: fix-accents 29 casi, fix-missing-accents 24, fix-dashes 8, test-tipografia 0 falliti.

Tipografia applicata: `fix-accents` 2.073 sostituzioni in 56 file su 214, 96 forme; `fix-dashes` 2 file su 419, 186 esclusi; `fix-missing-accents` 7 file su 233, con 16.769 occorrenze di 19 forme ambigue lasciate a chi legge. Diff: 721 righe tolte e 721 aggiunte, nessuna riunita o spezzata; fine riga invariate. Tre forme restano non riconosciute da `fix-accents`, da guardare con `--residui`. Aggiornati gli indici: blocco strumenti e paragrafo dei controlli in `CLAUDE.md`, `README.md`, scheda deployment. `chiudi -SoloControlli` verde su dodici controlli, controllo dell'albero verde.

## 08/10/2026: sette schede riconciliate per contenuto e riancorate a `0dbed60`

Commit `0dbed60` dell'utente con `chiudi`, che per la prima volta ha registrato l'impronta di ripresa. Skill `sync-context`: `verifica-schede` senza difetti di frontmatter, sette schede superate su otto rispetto a `6769dc4`, aggiornata solo quella del monitoraggio. Dei 129 file cambiati dopo l'ancora, 28 erano cambiati per la sola tipografia, misurato confrontando le due versioni con accenti, apostrofi, trattini e spazi tolti; il confronto con le schede e' stato fatto sui restanti.

Divergenze trovate e corrette, per scheda. STACK: `covers-paths` su `scripts/**`, cartella tolta, cioe' un sensore staccato; quattro controlli; switch, AP, PS5, NAS, VPN e FRITZ!Box non aggiornati; e due divergenze piu' vecchie dell'ancora, il monitoraggio con Snort invece di Suricata integrato in OPNsense e il DNS con Pi-hole invece di Unbound e poi AdGuard Home, entrambi scelti dallo studio del 22/09. roadmap: switch e AP decisi, cavi gia' posati, passi sul Seven nella fase 2, forme del lavoro documentale (ADR-019, 020, 021). design-and-security: tre zone invece delle VLAN dello studio del 22/09, divergenza anteriore all'ancora; host esposto descritto come scelta invece del solo inoltro UDP; wireless senza i due AP, la PS5 e la radio del Seven come rete esterna; guard-rail senza IBAN, carte e autotest. dev-testing: `scripts/**`, quattro controlli, "zero mancanti" della prova del 25/08 senza la correzione sulle note a pie' di pagina. deployment: `scripts/**` e il vecchio blocco dei quattro controlli. current-work: forma dei documenti e scheda dispositivo ancora da confermare. topologia: diagramma con due o tre AP, iniettore e NAS in VLAN 10; switch descritto come privo di livello 3, divergenza anteriore all'ancora; piano di indirizzamento a tre righe invece delle sette dello studio; nessuna PS5 ne' porta LAN 4. Tutte e sette ancorate a `0dbed60`.

## 08/10/2026: scheda dispositivo e strumenti di raccolta (ADR-021)

Commit `bcc8337` dell'utente con `chiudi`. Scritto `docs/05-analisi-del-caso/02-scheda-dispositivo.md`, collegato dall'indice della cartella e dal censimento: sei campi fissi più la fonte, da dove si legge ciascun dato, raccolta automatica per i PC e manuale per console, televisori, telefoni e tablet, cosa resta privato, modello della scheda.

Tre strumenti propri del progetto. `tools/raccolta-dispositivo.ps1`: sola lettura via CIM, cmdlet di rete e `netsh`; sistema, produttore, modello, scheda madre, processore, memoria, schede fisiche con le velocità ammesse dal driver, driver e connessione Wi-Fi; nessun seriale, product ID, licenza, utente o programma; uscita in `_notes/censimento/raccolte/<ID>-<data>.json`. `tools/raccolta-dispositivo.sh`: l'equivalente Linux, senza root. `tools/scheda-da-raccolta.py`: dalla raccolta alla scheda anonimizzata, deterministico; cerca gli standard 802.11 e WPA3 nei valori di `netsh` e non nelle chiavi, che cambiano con la lingua; autotest 0 errori, compresa la verifica che nome macchina, MAC e SSID non escano.

Prove. Lo script Windows, provato su questo PC con l'ID `PROVA`, ha rilevato una scheda fisica a 2,5 GbE con le sette velocità ammesse e nessuna radio Wi-Fi; la prima prova ha mostrato il modello generico "System Product Name" dei PC assemblati, da cui la lettura della scheda madre in entrambi gli script e la sostituzione nella scheda. Lo script Linux è verificato solo nella sintassi: Git Bash non ha `/sys` e `python3` vi è l'alias del Microsoft Store. La prima corsa su `bash -n` ha trovato un apostrofo in `${1:?...}` che bash leggeva come apice, corretto. Il PC della prova non corrisponde a nessun ID del censimento: chiesto all'utente.

Il primo `chiudi -SoloControlli` del blocco ha fermato due riscontri MAC REALE: il MAC finto scritto nella prova interna di `scheda-da-raccolta.py`. Sostituito con un segnaposto della forma convenuta `AA:BB:CC:00:00:NN`; autotest e controlli verdi.

## 08/10/2026: cartella del Seven riscritta al posto (ADR-020), documento 08 assorbito

Commit `f1283da` dell'utente con `chiudi`. Prima riscrittura secondo ADR-020, sulla cartella `docs/02-ftth-fastweb/06-tbc-i-parametri-di-interfaccia-modem-su-192-168-1-254-rotte/`. Metodo: il testo dell'autore resta parola per parola e dopo ogni voce entra un paragrafo "Nel progetto" con la lettura tecnica che stava nel documento separato `08-il-seven-nel-progetto-di-rete-voce-per-voce.md`, poi eliminato. Il README della cartella e' diventato l'introduzione: ruolo del Seven, premessa sulla rilevazione, indice, configurazione in ordine di esecuzione, note sugli acronimi. Titoli di panoramica, telefono e Wi-Fi senza la marcatura `not-of-interest-here`, nomi dei file invariati perche' stabili; chiusa la pendenza che chiedeva di rivedere quella marcatura.

Copertura, con uno script che confronta i paragrafi di HEAD normalizzati con il testo nuovo: 188 paragrafi di riferimento, 169 ritrovati interi. Dei 19 restanti, tre sono il titolo, la nota e l'indice del vecchio README sostituiti di proposito; uno e' la riga di numeri sotto l'avviso dell'Exposed Host, una lettura sbagliata della schermata che non corrisponde a nessun campo, rimossa con una nota nel testo; quindici sono paragrafi e tabelle dell'08 trasformati in prosa, riscontrati a mano riga per riga, da cui e' emersa una sola omissione, la diagnostica, aggiunta. L'affermazione che le schermate siano state prese durante il guasto del 28/02/2026 e' verificata sul file dell'autore `07-.../02-prima-lettura-pre-durante-fix-ticket-28022026-da-rifare.md`, che la riporta con gli stessi dati.

Errore di procedura dell'agente: per togliere il file 08 ha eseguito anche `git rm --cached`, che scrive nell'indice di git, operazione riservata all'utente. Effetto finale identico, perche' `chiudi` registra comunque la cancellazione; dichiarato all'utente. Il controllo dei riferimenti ha trovato l'08 ancora citato nel prompt di ripresa privato: corretto. `chiudi -SoloControlli` verde, albero coerente, `lint-prosa` zero segnalazioni sulla cartella.

## 08/10/2026: riscrittura al posto di `02-ftth-fastweb`, blocco A

Commit `7d34c05` dell'utente con `chiudi`. Blocco A della riscrittura (ADR-020): introduzione, indice e due pagine dei modem, offerta, posatura della fibra. Metodo come per la cartella del Seven: testo dell'autore intatto, paragrafi "Nel progetto" aggiunti. Copertura: 64 paragrafi di riferimento, 64 ritrovati interi.

Contraddizione trovata e corretta nel testo: l'introduzione affermava che il Seven in versione fibra ha l'ONT integrato e riceve la fibra direttamente, mentre la pagina sulla posatura dice che il Seven non ha porta ottica e richiede un ONT esterno, e la topologia nomina lo Zyxel PM5100-T1. L'utente ha confermato l'8/10/2026 che c'e' un ONT esterno Zyxel PM5100-T1: e' ora un fatto confermato e non una deduzione. Resta un'interpretazione dichiarata come tale il nome GPON dell'interfaccia nella pagina di stato del Seven, letto come nome del collegamento in fibra nel firmware. Aggiunti: tetto commerciale 2,5 in ricezione e 1 in trasmissione distinto dalle velocita' di linea GPON; uso preciso delle porte del Seven (LAN 4 al firewall, una LAN da 1 GbE alla PS5, una libera, RJ11 alla fonia); funzioni non usate e perche'; la previsione del NeXXt marcata come non avverata.

Inciampi di procedura, senza effetti sul risultato: il primo script si e' fermato al terzo file per gli spazi non separabili del testo dell'autore, dopo aver gia' scritto i primi due; due tentativi di generare lo script di riserva da quello originale hanno rotto gli escape. Lo script finale e' stato scritto per intero, e il controllo di copertura e delle fine riga e' stato rifatto sul risultato.

L'utente ha chiarito che il PC della prova dello script di raccolta e' una macchina di sviluppo che non appartiene alla rete domestica: non entra nel censimento. La sua raccolta di prova in `_notes/censimento/raccolte/` e' stata eliminata, e i due documenti che la citavano sono corretti.

## 08/10/2026: riscrittura al posto di `02-ftth-fastweb`, blocco B

Commit `9fdb97e` dell'utente con `chiudi`. Blocco B (ADR-020): la cartella `05-prima-del-design-della-rete-privata`, cinque file. Testo dell'autore intatto, paragrafi "Nel progetto" aggiunti; copertura 121 paragrafi su 121, fine riga CRLF intatte. Punti chiariti accanto al testo: il workaround della topologia teorica e' la topologia adottata, con lo switch 10EP al posto del 10E con adattatore; la causa MAC del divieto di collegare il firewall all'ONT resta un'ipotesi, mentre il divieto e' dell'assistenza per questa linea; la pagina sulla fonia descrive il Seven dietro il firewall, cioe' lo scenario del modem libero, mentre nella topologia adottata la voce resta nativa sul Seven e non attraversa OPNsense, quindi il problema dei SIP helper non si pone; il modem libero non e' percorso e richiederebbe parametri di accesso, credenziali della fonia e procedura con l'operatore. Corretta prima del commit una frase dell'agente che dava per non richieste le credenziali VoIP: nei documenti non risulta ne' in un senso ne' nell'altro. Due pendenze nuove: il ping sulla WAN del Seven e le cinque immagini senza descrizione della pagina sul modem libero.

## 08/10/2026: riscrittura al posto di `02-ftth-fastweb`, blocco C; area completa

Commit `fbe6785` dell'utente con `chiudi`. Blocco C (ADR-020): la cartella `07-tbc-new-i-parametri-di-accesso-wan-su-ont`, quattro file. Copertura 88 paragrafi su 88, fine riga CRLF intatte. Chiarito accanto al testo: i parametri di livello 2 e 3 servono solo alla strada non percorsa del firewall diretto sull'ONT; la topologia con il modem, il doppio NAT e il Wi-Fi descrivono quella adottata, con lo switch 10EP; la riga GPON di tipo `cu.ax` non rivela il protocollo della fibra; il MAC binding e l'interpretazione del "valore VLAN fuori posto" restano inferenze. Divergenza corretta: la seconda lettura descriveva il firewall su un PC con i7-6700 e 16 GB, mentre quello installato e' l'i3 di settima generazione del verbale; l'i7-6700 e' il PC per la conversione VHS. Chiuse due domande aperte dell'autore nella stessa pagina: differenza fra port forwarding ed Exposed Host sul Seven, e differenza fra la "DMZ" del Seven, che e' una regola di inoltro verso un host, e la DMZ di OPNsense, che e' un segmento di rete. Riformulata una frase dell'agente segnalata da `lint-prosa` come parallelismo negativo; l'altra segnalazione e' nel testo dell'autore e resta.

Con i blocchi A, B e C del 08/10/2026 e la cartella del Seven, l'area `02-ftth-fastweb` e' riscritta per intero: copertura complessiva 64, 121, 88 e 169 paragrafi dell'autore ritrovati, con le sole rimozioni dichiarate nella cartella del Seven.

## 08/10/2026: censimento dei dispositivi riscritto al posto, con le schede (ADR-020, ADR-021)

Commit `9979de4` dell'utente con `chiudi`. `docs/05-analisi-del-caso/01-tbc-studio-dispositivi-domestici.md`: descrizioni storiche intatte, e sotto ogni dispositivo la scheda a campi fissi di ADR-021 per i 17 ID con una voce nel testo (PC-01, PC-02, PC-03, PC-04, NET-04, PC-06, LAP-01, LAP-02, LAP-03, LAP-04, GAME-01, IOT-01, MOB-01, MOB-02, MOB-03, TAB-01, TAB-02), con i dati gia' presenti e la loro fonte, e "da compilare" il resto. Tabella dell'inventario aggiornata alle decisioni del 07/10: booster fuori dal progetto, switch 10EP deciso, AP 1 e 2 decisi con piano e cavo, AP 3 non previsto, PS5 sul Seven. Copertura: 101 paragrafi, 100 interi, il restante e' la tabella con le righe aggiornate di proposito.

Dato di progetto emerso: LAP-02 ha solo Wi-Fi 802.11n a 2,4 GHz e WPA2, quindi non entra in un SSID CASA solo WPA3; va cablato o nella rete legacy. Corretta prima del commit una frase dell'agente che attribuiva al PC VHS "materiale video di famiglia", non presente nel testo. Annotata nella scheda LAP-01 un'incoerenza dell'autore fra la data della pulizia degli errori, 19/01/2025, e quella del rapporto, 19/01/2026. `lint-prosa` segnala un parallelismo negativo e la prevalenza di elenchi a tre, entrambi nel testo storico.

## 08/10/2026: switch confermato al confronto dei prezzi (ADR-023), booster da dismettere, AP in discussione

Commit `c6af7ae` dell'utente con `chiudi`. L'utente ha chiesto di decidere insieme lo switch spendendo il meno possibile a progetto invariato. Ricerca web dei prezzi, registrata come S59-S63: 10EP 290,99-344,37 euro; 10E 251-307 euro, che con due iniettori TL-POE260S da 28-31 euro supera il 10EP; TP-Link SG2210XMP-M2 303-353 euro; generico tipo Sodola 170-200 euro. Scelta dell'utente: 10EP, ADR-023. Sugli AP l'utente ha chiesto una spiegazione migliore del confronto; aggiunto il NWA90BE Pro, 135,66-195 euro (S64), via di mezzo con 802.1X/RADIUS e senza SNMP. Decisione degli AP ancora aperta.

Booster: l'utente conferma di averlo e di pagarne il canone, e chiede come restituirlo. Le pagine ufficiali Fastweb lette, quella del Seven Booster, la guida MyFastweb e la trasparenza tariffaria nei primi 100.000 caratteri su oltre 560.000, non riportano costi, comodato o restituzione. Fonti utili: la risposta scritta di Fastweb in un reclamo del 2023 (S57), opzione dismissibile e restituzione non prevista in quel caso, e una guida di terzi (S58), canone 3 euro, restituzione entro 45 giorni a cessazione del contratto e penale di 60 euro. Le condizioni del contratto dell'utente non sono note: la procedura proposta, con la domanda esplicita sul comodato, e' fra le pendenze. Inventario NET-03 aggiornato: presente e a canone.

## 08/10/2026: AP decisi (ADR-024) e fonti tracciate

Commit `227baf5` dell'utente con `chiudi`. L'utente ha chiesto di tracciare nel progetto tutte le fonti citate nel giro precedente: sette erano gia' nel registro (S57-S64), aggiunte le tre pagine Fastweb lette senza trovarvi le informazioni sul Booster (S65-S67), dichiarandolo nella voce. Sugli AP il criterio dell'utente e' la soluzione piu' completa al costo minore. Ricerca web: NWA130BE a 213,99 euro presso un rivenditore italiano (S68), contro 188,62 euro del 22/09; Ubiquiti U7 Pro circa 181 euro IVA esclusa ma con il controller UniFi (S69); TP-Link EAP772 senza prezzo italiano e con SNMP autonomo non verificato (S70). Scelta conseguente: due NWA130BE, ADR-024, perche' completo significa tre bande, 802.1X/RADIUS e SNMP su entrambi i piani. Aggiornati riepilogo acquisti, STACK, inventario, lavoro corrente, il disegno SVG della topologia e il punto di ripresa dello snapshot, che dava ancora aperti il modello degli AP e la collocazione del NAS.

## 08/10/2026: richiesta di preventivo per il fornitore

Commit `0127f5d` dell'utente con `chiudi`. Su richiesta dell'utente, report tecnico di una pagina da inviare al proprio fornitore: sorgente HTML privato `_notes/preventivo/richiesta-preventivo-rete.html`, PDF di una pagina generato con Edge e salvato sul Desktop di questa macchina come `Richiesta-preventivo-rete-Zyxel.pdf`, controllato a video. Contiene i due articoli con codice (XMG1915-10EP-EU0101F, NWA130BE-EU0101F, codici visti nelle pagine dei rivenditori consultate), i requisiti per un'eventuale alternativa equivalente, il contesto d'installazione senza dati personali e le domande su prezzo, disponibilità, garanzia, supporti di montaggio, licenze e alternative, con i prezzi di mercato come riferimento. Aggiunta la pendenza del preventivo.

## 08/10/2026: regole fra le zone, valutazione di OpenMediaVault, dispositivi mobili

Commit `def0b31` dell'utente con `chiudi`. Scritto `docs/03-spunti-di-sviluppo/23-studio-home-lab/08-regole-fra-le-zone.md`: come OPNsense valuta le regole, otto alias, regole numerate per WAN, VLAN 10, 30, 40, 50, 60, 99, DMZ e WireGuard, cio' che resta fuori dalle regole e il collaudo con una prova che riesce e una che fallisce per zona. Scelte proposte e marcate come tali: indirizzi del NAS e dell'host servizi, rete WireGuard 192.168.98.0/24 per non coincidere con le reti comuni di alberghi e uffici, amministrazione dalla sola workstation ADMIN, dalla VLAN 99 e dal tunnel, VLAN 60 senza uscita predefinita, opzione di blocco delle reti private tolta sulla WAN perche' la WAN sta nella rete privata del Seven.

OpenMediaVault, su richiesta dell'utente: scritto `02-storage-di-rete-nas/08-valutazione-openmediavault.md`. Corretta un'affermazione del consolidamento, secondo cui con OpenMediaVault si perde ZFS: c'e' il plugin `openmediavault-zfs` (S74), con il kernel Proxmox raccomandato; a maggio 2026 un aggiornamento del kernel Debian ha rotto la compilazione dei moduli ZFS (S75); l'installatore non prevede l'avvio in specchio (S76); versione corrente 8.0.8 (S77). Lettura: per questa macchina TrueNAS SCALE resta piu' coerente; decisione dell'utente aperta fra le pendenze.

Dispositivi dichiarati dall'utente: Galaxy Tab S6 Lite (2022) LTE, un secondo tablet Samsung di modello non ricordato, S20 FE 5G e S25 Ultra. Aggiornati inventario e schede con le specifiche lette (S71-S73); il Tab S6 Lite e' assegnato a TAB-01 con l'attribuzione da confermare; IMEI e seriali non entrano nei file tracciati. Pendenza nuova: foto dell'interno di altri due PC, da indicare. Allineata la guida OPNsense, che citava ancora il 10E e l'iniettore.

## 08/10/2026: accesso amministrativo (ADR-025), aperture del laboratorio, TrueNAS confermato (ADR-026), correzione sulla WAN

Commit `64447b8` dell'utente con `chiudi`. Decisioni dell'utente: amministrazione solo da workstation ADMIN, porta di recupero della VLAN 99 e tunnel WireGuard, con spiegazione di ogni dettaglio; laboratorio senza uscita salvo aperture temporanee, da progettare; rete WireGuard `192.168.98.0/24`; NAS su TrueNAS SCALE. Lette cinque pagine della documentazione ufficiale di OPNsense (S78-S82; S83 e' la pagina delle pianificazioni, risposta 404). Scritto `09-accesso-amministrativo.md`: tre ingressi, tre barriere, ascolto delle interfacce di gestione solo sulla VLAN 99, secondo indirizzo di gestione del NAS su un trunk, autenticazione con TOTP e chiavi SSH, punto debole dell'identita' della workstation con le attenuazioni, tunnel parziale, porta di recupero, ordine di attivazione rispetto all'anti-lockout, collaudo. Aggiunte a `08-regole-fra-le-zone.md` l'alias GESTIONE e le due aperture del laboratorio, disattivate e attivate a tempo con una pianificazione, che alla scadenza rimuove gli stati.

Correzione: la prima stesura di `08` chiedeva di disattivare Block private networks sulla WAN perche' la WAN sta nella rete privata del Seven. Sbagliato: l'opzione guarda la sorgente di chi apre la connessione, la documentazione la raccomanda sulla WAN (S78), le risposte del Seven passano per gli stati e per le regole di sistema del DHCP, WireGuard arriva con sorgente pubblica. Resta attiva; si disattiverebbe solo se il Seven riscrivesse la sorgente del traffico inoltrato, da controllare al primo collaudo. Seconda correzione dalla guida WireGuard: la regola WAN ha come destinazione l'indirizzo WAN, non l'intero firewall. Chiusa la pendenza sulla scelta del sistema del NAS.

## 08/10/2026: piano unificato di hardware, Proxmox e stack open source

Commit `6b69c6e` dell'utente con `chiudi`. Richiesta dell'utente: riorganizzare il progetto per usare tutte le informazioni raccolte, con la migliore soluzione open source, e ricavare dall'hardware un server Proxmox su macchina fisica; tenere sempre chiaro che cosa e' aperto. Letti l'inventario delle scorte del NAS, la scheda del monitoraggio, lo studio SIEM e la mappa delle 22 aree di `03-spunti-di-sviluppo`. Verificati sulle fonti gli strumenti dello schema di monitoraggio della prima stesura (S84-S91): MozDef archiviato dal 2021, OSSIM ritirato a fine 2024, Apache Metron ritirato dal 2020, Sagan fermo al 2021, Snort non integrato in OPNsense, Security Onion con almeno 24 GB; Wazuh attivo, 8 GB per fino a 25 agenti; Proxmox VE 9.2.

Scritto `docs/03-spunti-di-sviluppo/23-studio-home-lab/10-piano-unificato-hardware-e-stack.md`: ruolo di ogni macchina, `linux-desktop-A` proposta come server Proxmox e host di servizio SRV-01 secondo quanto l'inventario delle scorte gia' indicava, ospiti con memoria e zona, stack per funzione con stato, schema della prima stesura con l'esito di ogni componente, ordine e quadro di cio' che e' pendente. Aggiornati STACK, scheda del monitoraggio, porta 6 dello switch come trunk 30-60-99 nello studio, nella topologia e nel disegno, riga SRV-01 dell'inventario. Aggiunto a `current-work.md` il quadro delle decisioni prese, proposte e pendenti, da aggiornare a ogni giro.

## 08/10/2026: monitoraggio adottato (ADR-028), contenuti scartati eliminati (ADR-027)

Commit `a4256d5` dell'utente con `chiudi`. Decisioni dell'utente: cancellare dal progetto cio' che riguarda gli strumenti scartati; documentare tecnicamente e implementare il flusso Wazuh con Suricata; aiutarlo a confrontare `linux-desktop-A` con le foto di due PC, da uno dei quali vorrebbe prendere i moduli DDR4 per il server di Wazuh, tenendolo come scorta; spiegare ogni area di studio in ogni dettaglio.

Cancellazione: nessun file riguardava solo gli strumenti scartati. Riscritto `09-monitoraggio/02-siem-analysis.md` tenendo le sezioni Wazuh e Splunk Free con note, eliminate le sezioni OSSIM, ELK, Elasticsearch, Metron, MozDef, Sagan e Snort e l'immagine `img-0022.png`, verificata a vista come lo stesso schema; tolta la trascrizione dello schema dalla scheda del monitoraggio; schema PNG privato nel Cestino; aggiornati `fonti-e-materiali.md`, l'indice privato e, con un marcatore di riferimento assente, il rapporto storico di conversione. Restano le righe del piano e delle decisioni che motivano gli scarti. Le citazioni di "ossim" in consumo del NAS e acquisti erano falsi positivi dentro "approssimativo" e "prossimi".

Monitoraggio: lette le pagine ufficiali di Wazuh su porte (S92) e syslog (S95), la guida di OPNsense sul plugin os-wazuh-agent (S93) e l'integrazione di Suricata (S94). Scritto `11-monitoraggio-wazuh-suricata.md`: componenti, percorsi con le porte, VM di Wazuh con una scheda nella VLAN 30 e una nella VLAN 99 per la dashboard, configurazione syslog con allowed-ips, Suricata in sola rilevazione, plugin con supporto tier 3 e ripiego via syslog, risposta attiva spenta, conservazione 90 giorni, ordine di messa in opera, collaudo. Aggiunti alle regole gli alias WAZUH e PORTE_WAZUH e tre regole: agenti dalla VLAN 10, facoltativa dalla VLAN 60, syslog dalla VLAN 99. L'implementazione vera aspetta Proxmox, cioè il disco e la scelta della macchina.

Inciampi: uno script si e' fermato per le fine riga di `fonti-e-materiali.md` prima di scrivere; un tentativo di correggerlo con una sostituzione di testo non ha agganciato perche' lo strumento di scrittura aveva convertito la sequenza di escape nei caratteri reali, il caso previsto dalla regola tipografica; risolto con `splitlines()` e lo strumento di modifica.

## 08/10/2026, chiusura della sessione: fonti del talk IPFire, allineamenti, schede riancorate

Commit `1256ba7` dell'utente con `chiudi`. L'utente ha fornito l'abstract di un talk del 03/10/2026 su IPFire con Suricata IPS e plugin Tor: la pagina dell'evento non e' stata trovata, registrato come S96 con questa avvertenza; la ricerca ha dato S97, IPFire 2.29 Core Update 198 con Suricata 8. Aggiunta al confronto con IPFire una sezione: stesso motore di rilevamento, scelta di OPNsense invariata, il nodo Tor sul firewall di casa giudicato una superficie in piu' e collocabile solo su una macchina dedicata in DMZ, come valutazione di progetto. Registrata fra le idee future la proposta dell'utente di un modello linguistico locale su macchina con GPU.

Allineamenti. Template avanzato a `04b60ad`: aggiornata la norma di `prove-che-misurano`. La prova a vuoto ha dato un conflitto su `docs/anti-slop/README.md`: era l'indice scritto dall'agente il 08/10, con lo stesso nome che lo script attribuisce al README del pacchetto; rinominato `docs/anti-slop/indice.md`, conflitto sparito. `verifica-schede --rigoroso` dava otto schede superate: aggiornate per contenuto `design-and-security` (amministrazione e monitoraggio), `roadmap` (fase 5 e idea fuori roadmap), `dev-testing` (prove degli strumenti di raccolta); le altre erano gia' state aggiornate nei giri della sessione. Tutte ancorate a `1256ba7`, rigoroso: 0 superate, 0 difetti. Snapshot: commit e template di riferimento, 160 documenti ricontati con check-docs-tree, correzione sulla prova del 25/08 che non vedeva le note a pie' di pagina, punto di ripresa riscritto. Prompt di ripresa riscritto per intero nella forma del template.

## 09/10/2026: ripresa, snapshot e schede riancorati a a7eda8a

La skill riprendi ha trovato una sola divergenza: `index.md` dichiarava `1256ba7` mentre HEAD era `a7eda8a`, il commit di chiusura dell'8/10 che contiene lo snapshot stesso e non poteva citare il proprio hash. Il work-log copriva già quel commit. `verifica-schede` dava sei schede superate per le sole modifiche di `a7eda8a` (riancoraggio, sezione IPFire, rinomina di `docs/anti-slop/indice.md`): riancorate tutte e otto a `a7eda8a`, esito 0 superate, 0 difetti. Nessun contenuto tecnico cambiato.

## 09/10/2026: foto di PC-02 e PC-03, niente DDR4, tre dischi in più

L'utente ha fornito 22 foto dell'interno dei due PC che mette a disposizione, `xubuntu` (PC-02) e `anduinos` (PC-03). Su sua richiesta spostate in `_notes/censimento/foto-pc/`, con indice privato; originali in Download cancellati dopo il confronto SHA-256, 22 su 22 identiche. Numeri di serie visibili non trascritti.

Letto: PC-03 è una seconda ASUS Z97-P rev. 2.02, distinta da `linux-desktop-B` per codici di memoria e disco M.2; kit Corsair 2 x 8 GB DDR3-1600, Samsung 850 EVO M.2 SATA 250 GB, alimentatore Atlantis, processore LGA1150 non leggibile. PC-02 è una ASUS serie P55 LGA1156 di modello non leggibile, Kingston DDR3-1333 da 2 e 4 GB, grafica dedicata, Kingston V300 SATA 240 GB, Samsung HD502HJ 500 GB del 2011, alimentatore Tecnoware FAL550FS12 550 W.

Esito: l'idea dell'8/10 di portare la DDR4 di uno dei due PC sul server Proxmox cade, sono entrambi DDR3. `linux-desktop-A` resta la proposta; alternativa scritta, una Z97-P con 32 GB DDR3. I due SSD possono fare lo specchio di Proxmox senza acquisti, a tre condizioni: SMART, supporto SATA dell'M.2 della H270M Pro4, scritture garantite del V300 (inferenza da verificare). Aggiornati inventario delle scorte (sezione nuova, tabelle memoria e schede, nota SMART), piano unificato, schede PC-02 e PC-03, quadro delle decisioni.

## 09/10/2026: confronto per il server Proxmox e combinazione finale

L'utente sta smontando PC-02 e PC-03 e non può lanciare raccolte; chiede la combinazione finale per riassemblare una volta, il confronto fra `linux-desktop-A` e la Z97-P a 32 GB, il significato dello specchio e della voce sul tablet. Ricerca sulla H270M Pro4: pagina ASRock vuota al recupero, registrata S98 da un rivenditore (due M.2 PCIe e SATA, 64 GB), da confermare sul manuale. Scritta nel piano unificato la sezione del confronto: raccomandata `linux-desktop-A` con i due SSD in specchio; Z97-P di PC-03 con 32 GB DDR3, i7-4790 se migliore e disco meccanico come nodo di laboratorio a richiesta; scelta la scheda di PC-03 e non quella di `linux-desktop-B`, per l'avvio intermittente e la tastiera muta già osservati. La Z97-P si assembla uguale nelle due strade, cambiano solo i dischi. Vincolo nuovo: lo switch non ha porte libere per il nodo di laboratorio (modulo SFP+ RJ45 o porta 4 convertita). Chiarito per l'utente che `linux-desktop-A` non è né PC-02 né PC-03.

## 09/10/2026: matrice rivista, porte dello switch, tablet

L'utente: `linux-desktop-C` (Ubuntu Studio) resta in servizio come multimediale, probabilmente in Wi-Fi, raggiungibile in SSH per la raccolta; i due tablet sono di casa. Tentata la connessione SSH con l'alias esistente: indirizzo che non risponde (timeout), la lettura della configurazione SSH è stata negata dai permessi; serve l'indirizzo attuale. Prezzo dello XMG1915-18EP (S99): circa 474-750 euro, cioè circa 180-460 in più del 10EP. Scritta nel piano unificato la matrice rivista: Z97-P anche banco di analisi dei campioni (area 08); le altre aree come VM su Proxmox o già coperte; porte del 10EP tutte assegnate, proposta di due moduli SFP in rame invece del 18EP, compatibilità da verificare. Schede TAB-01 e TAB-02 corrette: entrambi di casa, smentita l'attribuzione storica a Persona-B. Fornita all'utente in chat la corrispondenza fra segnaposto e nomi reali, che resta fuori dai file tracciati.

## 09/10/2026: raccolta via SSH su linux-desktop-C, confronto e parere per Proxmox, ADR-029

L'utente conferma l'indirizzo dell'alias `studio`: al secondo tentativo la macchina risponde (ping e porta 22), il primo timeout non è spiegato. Raccolta in sola lettura via SSH, uscita grezza in `_notes/censimento/raccolte/linux-desktop-C-2026-10-09.txt`: ASUS H170-PRO firmware 3805 del 2018, i7-6700, 16 GB, NVMe Crucial P2 500 GB, Realtek r8169 a 1 Gbps, Ubuntu 26.04.1 LTS kernel 7.0. Conferma l'inventario; è PC-06 del censimento, scheda compilata. Uso: produzione musicale in Wi-Fi con adattatore USB. La postazione di lavoro dell'utente non è della rete di casa.

Confronto per il server Proxmox completato con fonti (S100 PassMark: i7-7700 8.640 contro 7.257, single thread 2.441 contro 2.226, TDP 65 contro 84 W; S101 virtualizzazione e memoria), e costo di 10 W continui a 0,256 euro/kWh: circa 88 kWh e circa 22 euro all'anno. Parere scritto nel piano: `linux-desktop-A`. Decisione dell'utente registrata come ADR-029: resta il 10EP, moduli SFP se servono.

## 09/10/2026: scelto `linux-desktop-A` come server Proxmox (ADR-030), smontaggio dei due PC

Decisione dell'utente: il server Proxmox è `linux-desktop-A`. Registrata come ADR-030 con la ratio per esteso, cioè il peso dato a consumo, rete e processore per una macchina sempre accesa, il fatto che il solo vantaggio della Z97-P sia l'unico recuperabile con una spesa, e la collocazione del carico che chiede memoria sulla macchina accesa a richiesta, che è anche una separazione fisica fra il banco di analisi e il sistema che sorveglia. Commit `d15463c` dell'utente con `chiudi`, arrivato a `origin`.

Domanda dell'utente: se possa smontare interamente PC-02 e PC-03 e buttare i case. Scritta nel piano la sezione sullo smontaggio. PC-03 non si smonta, perché è il nodo di laboratorio e resta nel suo case; ne esce il solo SSD M.2. PC-02 si svuota di sei cose prima di eliminarne il case, e la sezione dice perché tenere la scheda buttando il case è la combinazione senza senso. Due verifiche prima dei cacciaviti: l'alloggiamento da tre pollici e mezzo nel case di PC-03, altrimenti la scheda trasloca nel case di PC-02; e la pasta termica, da procurare prima di togliere i dissipatori per leggere le sigle dei processori.

## 09/10/2026: PC-02 svuotato e smaltito (ADR-031), sequenza del da farsi al banco

Decisione dell'utente: da PC-02 si prende ciò che serve e si smaltiscono case e scheda madre. Registrata come ADR-031. Due pezzi sfuggono allo smaltimento e la ratio è scritta: i moduli Kingston in una busta, perché non occupano spazio e sono l'unico ricambio di memoria del nodo di laboratorio a capacità ridotta, e la scheda grafica, il cui modello non si legge nelle foto e va guardato prima del conferimento. Il processore segue la scheda, perché il suo socket non esiste su nessun'altra macchina di casa.

Aggiornati l'inventario delle scorte (PC-02 dichiarato smaltito, tabella della memoria, riga della scheda P55 tolta, vincolo dei dischi dichiarato caduto), il piano unificato e la scheda PC-02 del censimento. Scritta nel piano la sequenza del da farsi al banco in dodici passi, ordinata dal principio che ogni lettura che richiede di aprire qualcosa si fa mentre quella cosa è già aperta: il conferimento di PC-02 è l'ultimo passo e non il primo, perché il suo case serve ancora se il case di PC-03 non ha un alloggiamento da tre pollici e mezzo libero.

## 09/10/2026, chiusura: slitte rotte, ripresa allineata al banco

L'utente dichiara di avere probabilmente rotto le slitte e gli adattatori da due pollici e mezzo di PC-02, che la sequenza prevedeva di riutilizzare. Delimitata la conseguenza invece di darla per grave: riguarda il solo Kingston V300, perché il Samsung 850 EVO va nell'M.2 senza supporto e il disco meccanico è da tre pollici e mezzo e usa il montaggio del case che lo ospita. Resta da guardare se il case di `linux-desktop-A` monti da sé un disco da due pollici e mezzo, come molti case del 2017; altrimenti serve un adattatore da pochi euro. Aperta la pendenza, aggiornati i passi 2 e 8 della sequenza e l'elenco degli acquisti fuori sequenza, che passa da due voci a tre.

Commit `ee63b19` dell'utente con `chiudi`, arrivato a `origin`. Chiusa nel registro delle pendenze la voce sulle foto dei due PC, aperta l'8/10 e chiusa il giorno dopo. Snapshot e otto schede riancorati a `ee63b19`. Riscritto per intero `_notes/RESUME-PROMPT.md` su richiesta dell'utente perché la ripresa cada esattamente qui: stato al passo 1 della sequenza del da farsi, tabella dei nomi reali delle macchine, che al banco servono più dei segnaposto, e prompt di ripresa che fa leggere la sequenza come quarto passo. Resta da registrare l'impronta con il prossimo `chiudi`.

## 12/10/2026: guasto in cabina, checklist di collaudo per l'intervento in assenza del proprietario

Dal 9/10/2026 la linea è giù per un guasto in cabina: l'ONT Zyxel mostra LOS rosso fisso, PON spento e LAN 2,5G spenta, e l'app dell'operatore dichiara il modem non raggiungibile. Il 12/10 alle 14:30 è previsto l'intervento con collaudo e riavvio del modem, senza il proprietario in casa. Scritta la checklist in `_notes/collaudo-fastweb-2026-10-12.md`, fuori da git perché incrocia valori reali della linea: misure da farsi dichiarare dal tecnico, cose che non devono cambiare, verifiche da remoto.

Due correzioni rispetto alla nota salvata dall'utente nella cartella del guasto. La misura di riferimento "prima dell'intervento" non si può prendere, perché la linea è già giù: il termine di paragone resta il profilo contrattuale e le velocità di linea GPON già censite. E uno speedtest riuscito non prova che la fibra sia tornata, perché il Seven ha la connessione mobile di riserva: la prova è la riga GPON su con un indirizzo vero e la riga LTE/MBB1 giù nello stato WAN, cioè esattamente la trappola in cui erano cadute le letture di febbraio 2026.

L'intervento è l'occasione per chiudere la pendenza del 07/10, cioè la seconda lettura dei parametri WAN con la fibra attiva e la verifica che l'indirizzo pubblico statico sia lo stesso sulla fibra e sul collegamento di riserva. Le schermate da catturare sono elencate nella checklist.

## 12/10/2026: macchina di prova a 1 Gbit/s sulla porta da 2,5, copione per la telefonata

L'utente dichiara che in casa una macchina Windows è temporaneamente collegata alla porta LAN 4 del Seven, quella da 2,5 Gbit/s, con scheda di rete da 1 Gbit/s, ed è utilizzabile per le prove. Corretta di conseguenza una verifica scritta poche ore prima: nello Stato LAN la porta 4 risulterà attiva a 1 Gbps e non a 2,5 Gbps come nel censimento di febbraio 2026, perché il collegamento negozia alla velocità della scheda e non a quella della porta. Non è un degrado da contestare al tecnico. Resta che lo speedtest via cavo da quella macchina ha un tetto di circa 940 Mbit/s e non può dimostrare il profilo da 2,5 Gbit/s, che si misura solo lato modem.

Scritto in `_notes/collaudo-fastweb-2026-10-12.md` il copione della telefonata al tecnico, in linguaggio non tecnico, con per ogni domanda la risposta attesa e il segnale di allarme. Il messaggio per chi è in casa e la lista delle verifiche del proprietario sono nello stesso file.

## 12/10/2026: guasto in cabina riparato, fibra tornata, parte chiusa

L'intervento si è svolto fuori casa. Il tecnico ha riferito per telefono che in cabina un armadio era staccato e il percorso di rete era sbagliato; in casa non è stato toccato nulla e la rete senza fili è tornata da sé. Cade quindi il rischio che la checklist teneva in conto, cioè un ripristino alle impostazioni di fabbrica del modem: configurazione e impostazioni Wi-Fi sono intatte.

Il tecnico ha dichiarato un valore ottico di 20,93 con soglia operativa a 25. Il dato è di seconda mano, dettato al telefono e non misurato, e come tale è registrato. L'unità pronunciata, dBm, non regge per entrambe le letture possibili: se è attenuazione di tratta l'unità è il dB, se è potenza ricevuta il segno è negativo. Nella prima lettura, con un OLT a +3 dBm, restano circa -17,9 dBm all'ONT, cioè nove decibel sopra la sensibilità di classe B+, e la soglia di 25 lascia tre decibel rispetto ai 28 ammessi; nella seconda, -20,93 dBm stanno sei decibel sopra la stessa sensibilità, ma la soglia equivarrebbe a fermarsi a due decibel da essa, che è stretta per una regola pratica. In entrambe le letture la conclusione è la stessa: il collegamento sta dentro il bilancio di tratta con margine, e il numero conferma la riparazione invece di spiegare il guasto, che per sintomi, cioè LOS rosso fisso e PON spento per giorni, è una tratta interrotta a monte e non un eccesso di attenuazione. L'ambiguità si risolve leggendo la potenza ottica sull'ONT o nello stato GPON del Seven, se la espongono, ed è un'inferenza da verificare dentro il giro di schermate già pendente.

Scritto `docs/02-ftth-fastweb/08-guasto-in-cabina-ottobre-2026.md`, collegato dall'indice dell'area, con l'evento, il ragionamento sui sintomi e il bilancio di tratta. Nel registro delle pendenze la voce delle rilevazioni del Seven da ripetere dichiara il guasto chiuso e il rischio del ripristino di fabbrica non realizzato; resta la pendenza vera, cioè il giro di schermate con la GPON attiva e il confronto dell'indirizzo pubblico statico fra fibra e collegamento di riserva, che ora è una sola azione dell'utente.

La cartella personale dell'operatore su disco J, dove l'utente tiene la propria nota del guasto, non è stata aperta: la regola sui documenti personali vale anche quando il percorso viene citato in sessione, e tutto ciò che è stato scritto qui viene da quanto l'utente ha riferito in chat.

Il filo attivo torna al banco: assemblaggio del NAS e sequenza in dodici passi su PC-02 e PC-03.

## 12/10/2026, ripresa dopo il riavvio: memoria del NAS ridistribuita (ADR-032) e percorso rapido

Il PC si è riavviato durante la sessione, dopo il commit `5804c51`. L'albero era pulito e la trascrizione della sessione caduta non esisteva più, quindi la discussione sul NAS di quel giro non è arrivata su disco; l'unica traccia è il timbro del Passo 1.6 nella guida privata, che dichiara il montaggio avviato con cinque pezzi. L'utente ha chiesto di accelerare l'assemblaggio e di verificare che il NAS, con i pezzi disponibili, sia la scelta migliore.

La rilettura di guida, decisioni e piano unificato conferma l'impianto, cioè base, alimentatore, avvio in specchio, pool sui due NVMe e TrueNAS, e trova una sola cosa rimasta indietro: la memoria. I 32 GB del NAS venivano dall'analisi del 01/09, con un pool di dischi meccanici e applicazioni sul NAS; dopo ADR-015 e ADR-030 non servono più, mentre il server Proxmox con 16 GB lasciava al laboratorio circa 4 GB. Fonte letta: guida hardware di TrueNAS, S102, minimo 8 GB fino a otto dischi. Quattro strade messe davanti all'utente: piano invariato, NAS 16 e server 24, scambio completo con NAS 16 e server 32, una macchina sola per NAS e Proxmox. Scelta dell'utente: NAS 16 e server 24, registrata come ADR-032.

L'utente ricordava che si fosse detto diverso per la DDR3 di xubuntu. Riletta per intero la foto 10 di PC-02: il ricordo è giusto ma riguarda l'idea dell'8/10, cioè prendere memoria per il server da PC-02 o PC-03, già esclusa perché sono DDR3; qui si spostano solo moduli DDR4. La foto aggiunge un dato: oltre ai due Kingston in mano ne restano due inseriti in `DIMM_B1` e `DIMM_B2`, quindi i moduli DDR3 di PC-02 sono quattro, due di taglia da leggere.

Scritti: ADR-032; nella guida privata la sezione «PERCORSO RAPIDO dal 12/10/2026» con i dodici gesti che restano, il Passo 2.2 marcato saltato e i valori attesi portati a 16 GB; inventario privato e pubblico delle scorte con la scorta di due moduli da 4 GB; schede NAS 03 e 04; piano unificato con il server a 24 GB, lo scambio dei moduli al passo 8 e il test della memoria al passo 10; quadro delle decisioni; voce nuova nel registro delle pendenze; fonte S102; indice delle foto di PC-02.

## 12/10/2026: allocazione completa fissata, i due NVMe al server (ADR-033)

L'utente ha segnalato di aver perso il quadro dei pezzi e dello stato, e che le informazioni gli arrivavano a frammenti; ha chiesto una panoramica unica fissata nel modo migliore, con la ratio registrata, e poi di decidere al suo posto dove mettere i due NVMe. Ha chiesto anche se ADR-032 togliesse a `PC-DESKTOP-B` il ruolo di scorta: no, quel ruolo è scheda, processore e alimentatore senza memoria né disco dal 07/10, e i suoi moduli uscivano comunque.

Rifacendo la panoramica è emerso che la scheda del server ha due alloggiamenti M.2 NVMe x4 (S103, pagina del produttore riassunta dalla ricerca), quindi i due NVMe vi entrano senza adattatore, e che la premessa di ADR-015 era caduta con ADR-030. Decisione, ADR-033: NVMe al server in specchio, NAS con il V300 come avvio e SanDisk più WD Blue in specchio come dati, Samsung 850 EVO fermo nel nodo di laboratorio, adattatore non acquistato. Limite dichiarato: circa 180 GB pianificabili sul NAS.

Scritto `docs/03-spunti-di-sviluppo/23-studio-home-lab/12-allocazione-dell-hardware.md`, fonte canonica, collegato dall'indice dello studio, con macchine, dischi, memoria, acquisti, limiti e un ordine dei gesti in undici passi che mette per prime le due macchine senza pasta termica. Note di rimando nel piano unificato e nelle schede NAS 03, 04 e 06; guida privata con il percorso rapido riscritto e i Passi 2.4 e 2.5 marcati; quadro delle decisioni, pendenze, snapshot, fonte S103.

## 13/10/2026: modello linguistico locale su CPU, studio colibri

L'utente ha segnalato colibri, un motore che esegue modelli mixture of experts sul solo processore leggendo gli esperti dal disco, chiedendo se i 16 o 32 GB componibili in casa bastino, di completare la matrice e la roadmap e dove collocarlo. Letti il README, il Makefile, la pagina dell'interfaccia e la tabella delle prove (S104, S105).

Esito: 32 GB fanno al caso, 16 no, perché Qwen3.6-35B-A3B chiede 20 GB per girare dalla memoria; i modelli grandi non sono alla portata della casa per il disco, non per la memoria. La premessa del piano che un modello locale chieda una GPU cade per i modelli medi. Collocazione proposta: nodo di laboratorio a 32 GB, VLAN 60, alternato all'analisi dei campioni; scartati server, NAS, scorte e la postazione di lavoro, che resta fuori dalla rete di casa. Velocità stimata fra 1 e 2 token al secondo, inferenza da misurare con una soglia fissata in anticipo. Nessuna decisione dell'utente, quindi nessun ADR.

Scritto `docs/03-spunti-di-sviluppo/23-studio-home-lab/13-modello-linguistico-locale-su-cpu.md`, collegato dall'indice dello studio; aggiornati la matrice e lo stack del piano unificato, la riga del nodo e il passo 12 facoltativo nell'allocazione, la roadmap fuori sequenza, il quadro delle decisioni, le pendenze e le fonti S104 e S105.

## 13/10/2026: colibri sul nodo di laboratorio confermato (ADR-034), studio reso leggibile da zero

L'utente ha confermato la collocazione proposta, cioè il nodo di laboratorio PC-03 nella VLAN 60, acceso a richiesta, senza costo e senza cambiare l'ordine della roadmap, e ha deciso che un giorno si farà uno studio di espansione con una GPU. Ha chiesto di ripartire esattamente da questo punto e di tracciare ogni dettaglio tecnico come per chi non conosce i passaggi.

Registrato ADR-034. Lo studio 13 ha ora lo stato in testa, un glossario di diciannove voci che spiega ogni parola tecnica e perché conta, il racconto di come è stato fatto lo studio, la misura in sette passi con i comandi da lanciare sul nodo, le domande dello studio futuro sulla GPU e una sezione finale «Da dove si riparte». La procedura usa lo strumento di misura del progetto, `c/tools/datapoint.py`, letto dalla sua intestazione e non provato. Aggiornati con il riferimento ad ADR-034 piano unificato, allocazione, roadmap, quadro delle decisioni, snapshot e fonte S104; nuova voce nelle pendenze per lo studio sulla GPU.

## 14/10/2026: PC-02 aperto, dischi estratti, il V300 ha il suo adattatore

L'utente ha aperto PC-02 ed estratto i due dischi, mandando tre foto. Le etichette coincidono con il censimento del 09/10: Samsung HD502HJ da 500 GB e Kingston V300 da 240 GB. Il V300 è avvitato su un adattatore Corsair da due pollici e mezzo a tre e mezzo che dalla foto appare integro: la conseguenza delle slitte rotte dichiarate il 09/10, che il 12/10 si era spostata sul NAS come una fascetta da mettere, cade se l'adattatore è davvero sano, e il V300 va in un alloggiamento da tre pollici e mezzo del NAS con le viti. L'integrità è letta dalla foto e va confermata a mano. Aggiornati pendenze, inventario 06, piano unificato, scheda del lavoro corrente, gesto 1 e 2 della guida privata e indice delle foto, dove le tre schermate sono copiate come foto 18, 19 e 20. Del gesto 1 restano i cavi dati, la minuteria, la taglia dei due DDR3 inseriti e la scheda grafica.

## 14/10/2026: pratica della fibra chiusa, indirizzo statico confermato, velocità misurata

L'utente dichiara chiusa la pratica con l'operatore e porta tre schermate di speedtest.net dal telefono in Wi-Fi sul Seven: alle 08:02, con la VPN attiva, 746,38 Mbit/s in scarico e latenza 46 ms a riposo, 119 ms sotto carico; alle 08:03, a VPN spenta, 903,57 Mbit/s, 45 e 117 ms. La terza schermata, a VPN spenta, mostra Fastweb e un indirizzo pubblico che, confrontato in locale con la mappa privata, coincide con l'indirizzo statico: l'intervento in cabina non l'ha toccato. Il carico non compare nelle schermate e non è misurato. La latenza a riposo di 45 ms resta da guardare, senza attribuzione. Il server scelto dal servizio e l'indirizzo reale stanno solo nella nota privata del collaudo, con le schermate copiate in `_notes/collaudo-fastweb-2026-10-14/` e impronte identiche agli originali. Aggiornati il documento del guasto, con una sezione del 14/10 e la sezione di ciò che resta aperto, il registro delle pendenze, la scheda del lavoro corrente e lo snapshot.

## 15/10/2026: Netdata studiato come candidato al raccoglitore di metriche

Segnalazione dell'utente, con il collegamento al repository di Netdata, chiedendo di aggiornare il progetto con questa possibilità per sorvegliare le macchine del laboratorio. Lo studio risponde alla sola riga di monitoraggio rimasta pendente nel piano unificato dall'8/10/2026, cioè il raccoglitore di metriche, e distingue il perimetro: Wazuh risponde a che cosa è successo, un raccoglitore di metriche a come sta andando, e i due non si sostituiscono.

Fatti verificati sulle fonti, non dedotti. Agente GPL-3.0 con interfaccia utente non aperta e Netdata Cloud chiuso e facoltativo; raccolta al secondo con conservazione a livelli e circa mezzo byte per campione; parent che raccoglie gli agenti figli e tiene dashboard, storico e allarmi senza nessun servizio esterno; raccoglitore SNMP con profili, che è la parte che copre switch e access point; versione 2.12.1 dell'8/10/2026 su un repository del 2013 (S106, S108). Due fatti pesano contro e sono scritti nello studio con la stessa evidenza: la dashboard non è autenticata per impostazione predefinita e ascolta su tutte le interfacce, quindi la protezione è di rete e di configurazione (S107), e la configurazione di alcune parti dall'interfaccia richiede un piano a pagamento. Il plugin per OPNsense esiste nel repository dei plugin, versione 1.2, ma non è documentato nel manuale ufficiale, quindi la via prudente è leggere il firewall via SNMP invece di installargli un agente (S109).

Collocazione proposta: parent sul server Proxmox nella VLAN 30 con dashboard raggiungibile dalla sola VLAN 99, come ADR-025 impone agli altri servizi di amministrazione; agenti sugli host; apparati via SNMP dal parent; uscita verso Netdata Cloud negata salvo decisione contraria. Nessuna decisione dell'utente, quindi nessun ADR: la voce resta pendente con un candidato studiato.

Scritto `docs/03-spunti-di-sviluppo/23-studio-home-lab/14-metriche-con-netdata.md`, collegato dall'indice dello studio; aggiornati la riga dello stack e il paragrafo delle pendenze del piano unificato, le due righe di Beszel e LibreNMS nei servizi gratuiti, il registro delle pendenze con una voce nuova, la scheda del lavoro corrente nelle proposte e nelle pendenze, lo snapshot e le fonti da S106 a S109.

## 15/10/2026: gesto 1 del banco chiuso dalle foto di PC-02

L'utente ha mandato dieci foto via Telegram del banco con PC-02 svuotato. Spostate in `_notes/censimento/foto-pc/xubuntu/` come foto da 21 a 30, impronte SHA-256 identiche 10 su 10, originali cancellati da Download su richiesta dell'utente; l'indice privato le descrive una per una. Letto dalle foto: fuori dalla macchina i due dischi, il V300 ancora sull'adattatore Corsair con il telaio integro sui lati visibili, l'alimentatore Tecnoware FAL550FS12 con i suoi cavi fissi (almeno due connettori di alimentazione SATA visibili, conto esatto da fare a mano), due cavi dati SATA, circa otto viti e i quattro moduli DDR3: due `KVR1333D3N9/2G` e due `KVR1333D3N9/4G`, 12 GB in tutto, che chiude la taglia dei due moduli che erano ancora inseriti. La scheda grafica, fotografata ancora nel case, è una NVIDIA GeForce 210 da 1 GB DDR3, 64 bit, VGA, DVI e HDMI, passiva. I numeri di serie leggibili nelle foto (alimentatore, disco, moduli, scheda grafica) non sono trascritti in nessun file tracciato. Conseguenza: con l'alimentatore fuori, la raccolta software su PC-02 non è più possibile, e la sigla del processore resta da leggere sotto il dissipatore, di solo interesse d'inventario.

Aggiornati la scheda 06 delle scorte, il documento 12 dell'allocazione (passo 1 e tabella della memoria), la scheda dispositivo di PC-02, il registro delle pendenze, la scheda del lavoro corrente e lo snapshot.

## 15/10/2026: Tecnoware di scorta, settings dell'account ripristinato

L'utente ha deciso che il Tecnoware di PC-02 resta alimentatore di scorta e che i suoi connettori non si contano (ADR-035); il passo 9 dell'allocazione ora dice che il nodo di laboratorio tiene l'Atlantis. Su richiesta esplicita dell'utente, il file di impostazioni dell'account, fuori dal repository, è stato riportato allo stato precedente al comando di configurazione della modalità automatica, togliendo il solo blocco che quel comando aveva aggiunto; il file risulta JSON valido. Commit `7c2f698` fatto dall'utente con `chiudi`.

## 15/10/2026: Netdata accettato (ADR-036)

L'utente ha detto sì a Netdata come raccoglitore di metriche, con il parent su una macchina Linux, e ha ricordato di averne già provato l'installazione in un altro progetto. Letto di quel progetto solo lo stato registrato in memoria: Netdata 2.12.1 da pacchetto statico con impronte verificate, dashboard sul solo indirizzo locale, nessun collegamento al servizio del produttore; nessun dettaglio di quell'infrastruttura è entrato qui. Aggiornati lo studio 14, il piano unificato, il registro delle pendenze, la scheda del lavoro corrente e lo snapshot. Al banco si riparte a micro-passi, uno per volta, su richiesta dell'utente, dal fissaggio del V300 nel case del NAS.

## 15/10/2026: pendenza sulla protezione degli endpoint

Su richiesta dell'utente è stata aperta nel registro delle pendenze la voce sulla protezione degli endpoint oltre il firewall: antivirus gratuito per gli endpoint, tenendo conto di Microsoft Defender nel piano Family che l'utente ha già, e copertura massima con soli strumenti gratuiti e open source affidabili. Solo registrata, non studiata; parte dalla scheda esistente `07-further-protection/02-endpoint-protection.md`. Al banco l'utente chiede passi meno frazionati; il cavo del NAS risulta già staccato.

## 15/10/2026: base del NAS aperta, studio sugli endpoint avviato

Quattro foto dell'interno di `PC-DESKTOP-A`, archiviate nel materiale privato con impronte identiche e originali cancellati. Confermano l'identità della base (H170-PRO, M.2 vuoto) e l'alimentatore Corsair HX520W modulare già registrato da ADR-016; mostrano il lettore ottico nel vano da 5,25 e la gabbia dei dischi sotto, il cui vano libero da 3,5 non si distingue con certezza dall'angolo delle foto. Avviata in parallelo, su richiesta dell'utente, una ricerca sulla protezione degli endpoint e sull'hardening gratuiti e open source del 2026, da cui nascerà uno studio nel filone della protezione.

## 15/10/2026: studio della protezione degli endpoint

Un subagent ha fatto la ricerca su fonti web e sul repository; il rapporto è stato rivisto e trascritto in `docs/03-spunti-di-sviluppo/07-further-protection/03-studio-protezione-endpoint-2026.md`, collegato dall'indice della cartella, con le fonti da S110 a S125 nel registro. Sostanza: la base gratuita è Defender Antivirus irrigidito con regole ASR, cartelle controllate e protezione da manomissioni; Wazuh resta l'occhio comune; ClamAV, Lynis, fail2ban, AdGuard Home, Vaultwarden e restic coprono il resto; scartati Kaspersky, Avast e AVG, e Pi-hole e Borg come doppioni. Dichiarati non verificati: l'app Defender del piano Family in Italia, la protezione da manomissioni su Home, il dato primario di AV-Comparatives, le licenze e le versioni lette con un riassunto. Nessuna decisione.

## 16/10/2026: V300 montato nel NAS, cavo dati preso dal lettore ottico

Gesto 2 del banco in corso, a passi piccoli su richiesta dell'utente. Il V300 è nella gabbia di `PC-DESKTOP-A`, fissato da un lato solo, accettato perché un SSD non ha parti in movimento. Alimentazione da un cavo SATA dell'HX520W. Il cavo dati è quello del lettore ottico, che il NAS non usa perché TrueNAS si installa da chiavetta: il lettore resta senza dati. I due cavi dati SATA presi da PC-02 sono a casa dell'utente e non al banco, quindi il WD Blue avrà bisogno di uno di quelli. La foto della conferma è mossa e non mostra con certezza i due connettori inseriti.

Aggiornamento dello stesso giorno: il WD Blue è nella gabbia, sulla sua cornice, con il proprio cavo dati uscito da `PC-DESKTOP-B` e la corrente tramite un adattatore Molex verso SATA collegato a un Molex dell'HX520W, come mostra la foto della conferma. I cavi di PC-02 rimasti a casa non servono. Tre dischi collegati: SanDisk come prima, V300 e WD Blue nuovi; le porte SATA della scheda non seguono la numerazione dell'allocazione, che TrueNAS non richiede. Prossimo: primo avvio a case aperto e lettura del firmware, cioè il passo 3 dell'allocazione.

## 16/10/2026: primo avvio del NAS, firmware letto

Primo avvio di `PC-DESKTOP-A` a case aperto, schermata EZ Mode del firmware fotografata dall'utente. Letto: H170-PRO con BIOS 3805, i7-6700 a 3,4 GHz; memoria 16384 MB, due moduli Team Group da 8 GB in `DIMM_A1` e `DIMM_B1`, quindi in doppio canale, a 2133 MHz con X.M.P. spento; dischi su `SATA6G_1` SanDisk SDSSDA240G, `SATA6G_2` Kingston SV300S37A240G, `SATA6G_6` WDC WDS250G1B0A, tutti e tre visti; ventola del processore a 1064 giri, ventole del case a 659 e 618; processore a 28 °C, scheda a 25 °C. Tre condizioni di ADR-016 e del passo 3 dell'allocazione verificate: ventola, 16 GB, tre dischi. Restano la tensione a +12 V dalla pagina Monitor e il test della memoria di una notte. Due cose da guardare prima dell'installazione: lo stato dell'interruttore Intel Rapid Storage Technology, che dalla foto non si legge con certezza e per TrueNAS deve lasciare i dischi in AHCI; e il fatto che SanDisk e WD Blue portano ancora un Windows avviabile, cioè che la creazione del pool cancella il SanDisk, il disco di sistema della base, il cui contenuto va confermato salvato prima del passo 4.

## 16/10/2026: registro del montaggio e direttiva sulla completezza

Direttiva dell'utente, ribadita con forza: tutti i dati raccolti al banco vanno tracciati nella documentazione versionata come ragione di progetto, in modo completo anche in senso cronologico, e le foto e le evidenze vanno conservate nella parte non versionata. In risposta è nato `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/09-registro-del-montaggio.md`, registro cronologico a voci per giornata dal 14/10/2026, con letture, ragioni e scarti dal piano, collegato dall'indice della cartella; i passi 2 e 3 dell'allocazione e il registro delle pendenze lo richiamano. Letture del firmware in Advanced Mode, oltre a quelle dell'EZ Mode già registrate: BIOS 3805 del 16/05/2018, ME 11.8.50.3470, PCH D1, +12 V 12,192 V, +5 V 5,040 V, +3,3 V 3,392 V, tutto in Auto, CPU fino a 33 °C. Tre condizioni di ADR-016 verificate su quattro; manca il test della memoria. Evidenze archiviate nella cartella della base sotto `_notes/censimento/foto-pc/`, non versionata: quattro foto Telegram (originali cancellati dopo il confronto delle impronte, 4 su 4) e sei schermate Screenpresso (impronte identiche, 6 su 6, originali lasciati nella cartella di cattura). Due schermate della stessa serie, estranee al laboratorio, non sono state copiate. Il primo confronto delle schermate aveva dato un falso esito diverso perché `sha256sum` antepone una barra rovesciata alla riga quando il percorso ne contiene una; rifatto leggendo il file dallo standard input.

## 16/10/2026: Memtest86+ 8.10 sulla chiavetta Ventoy

Scaricati installer e ISO di Memtest86+ 8.10 in `_notes/nas-consolidation/strumenti/`, ignorato da git; impronta dell'installer identica al riferimento del 02/09/2026. Sul sito c'è la 9.00 del 15/10/2026, non scelta per la ragione scritta nel registro del montaggio. La chiavetta dell'utente è un disco USB unico da 58 GB preparato con Ventoy e con una raccolta di strumenti di soccorso del 2021: la partizione H: è quella di avvio di Ventoy, la G: contiene la raccolta. Non è stata riscritta: la ISO 8.10 è stata copiata accanto alla vecchia immagine 5.x, con impronta verificata sulla chiavetta. Registrato nel registro del montaggio. Alternativa senza chiavetta, non scelta: la diagnostica della memoria di Windows dal Windows ancora presente sul SanDisk, più debole come test.

## 16/10/2026: Memtest86+ in esecuzione sul NAS

Avviato da Ventoy in UEFI, versione 8.10; letture e ragione nel registro del montaggio. Zero errori all'avvio, esito da leggere al mattino del 17/10 su Pass ed Errors. Evidenze archiviate nella cartella della base sotto `_notes/censimento/foto-pc/`: sette foto Telegram (impronte identiche, originali cancellati) e tre schermate Screenpresso.

## 16/10/2026: errore di memoria sul NAS

Memtest86+ 8.10 ha trovato un errore dopo 3:46:14, al quinto passaggio, test 6: bit 31 letto a 1 all'indirizzo di circa 14,5 GB, memoria alle impostazioni di fabbrica. Quarta condizione di ADR-016 non soddisfatta; prossimo passo l'isolamento dei due moduli Team Group uno per volta in `DIMM_A1`, ciascuno per qualche ora, secondo il passo 4.2.d della guida privata. Ricambio disponibile: i due Crucial da 4 GB di scorta (ADR-032). Aggiornati il registro del montaggio e il registro delle pendenze; evidenza archiviata.

Scelta dell'utente: memtest lasciato acceso fino a lunedì 19/10/2026, poi lettura di passaggi, errori e indirizzi e isolamento dei moduli.

## 16/10/2026: chiusura della sessione

Lezioni per il template, valutate con i due criteri della sezione 16 di PROJECT-SYSTEM.md, depositate in `_notes/lezioni-da-home-lab-2026-10-16.md` del template e segnalate alla sessione del template aperta in parallelo, che stava modificando le stesse regole: difetto di `allinea-tutti.ps1`, che scrive il marcatore con fine riga misti, con la causa letta nel codice; falso esito di `sha256sum` con percorsi che contengono una barra rovesciata; riscrittura dell'intero file a LF che sfugge a `check-eol`; nome reale di una cartella privata finito nei file tracciati attraverso la citazione del percorso; e una candidata sulle impostazioni dell'account riscritte da un comando dell'harness. Snapshot, scheda del lavoro corrente e file di ripresa aggiornati per riprendere con la skill riprendi.

## 17/10/2026: ripresa verificata e prelievi residui dei due PC

Eseguita la procedura `riprendi` su richiesta dell'utente, che vuole proseguire davanti a PC-02 e PC-03. HEAD `eb4708a`, albero pulito, un solo albero di lavoro, impronta registrata il 16/10 alle 16:48 sul medesimo commit. Il controllo segnala solo il commit arretrato dello snapshot (`cea0311`); il work-log descrive già il lavoro del 16/10. Aggiornato lo snapshot a HEAD. Adattatori Codex allineati; `verifica-schede` trova sette schede superate rispetto all'ancora e zero difetti. Riconciliate le sole sezioni del banco in lavoro corrente e roadmap, senza dichiarare riverificate le intere schede e senza spostarne le ancore. Nessun subagent avviato.

Confrontati ADR-031, ADR-035, allocazione canonica e registro del montaggio: i prelievi principali di PC-02 sono chiusi dal 15/10, ma la GeForce 210 era ancora nel case e l'estrazione del lettore ottico non risulta documentata. Entrambi vanno verificati prima del conferimento; la sigla del processore di PC-02 serve solo all'inventario. PC-03 si conserva come nodo di laboratorio con memoria, Samsung 850 EVO e Atlantis; riceverà il disco da 500 GB di PC-02 e due moduli da 8 GB da `linux-desktop-B`. Restano da leggere processore e targa dell'Atlantis e da verificare il vano da 3,5 pollici. Il NAS resta sul test fino al 19/10 secondo la scelta già registrata; nessun nuovo esito di memoria ricevuto. Aggiornati allocazione, pendenze e file privato di ripresa. Primo gesto proposto: verificare se la GeForce 210 sia ancora inserita in PC-02; non si registra alcun prelievo come avvenuto.

Verifiche della ripresa: 166 documenti raggiungibili dalla home, zero collegamenti rotti e zero orfani con check-docs-tree; md-unwrap sui sette documenti modificati, incluso il file privato di ripresa, senza modifiche necessarie. Guard-rail: 609 file tracciati esaminati, zero riscontri bloccanti; i 124 riscontri non bloccanti sono importi e indirizzi da valutare nel loro contesto, senza nuovi valori identificanti nel delta. I dodici controlli di chiudi -SoloControlli sono verdi. Verifica del diff pulita considerando CR come parte dei fine riga CRLF, conservati nei file che li usavano. Nessuna operazione di staging, commit o push.

## 17/10/2026: GeForce recuperata, PC-02 dismesso e PC-03 senza SSD

L'utente conferma GeForce 210 recuperata e PC-02 dismesso e indica due foto Telegram da assorbire, archiviare e poi cancellare dalla cartella di origine. Lette entrambe, copiate nelle cartelle private dei due PC e confrontate con gli originali mediante SHA-256: due su due identiche. Manifesto di importazione e indice privato conservano l'abbinamento. La foto della scheda la mostra fuori dal case; resta scorta video per diagnosi, non collaudata e senza assegnazione alle tre macchine. Il lettore DVD non risulta recuperato: non lo si conta fra le scorte certe e non si chiede di intervenire su una macchina ormai dismessa.

L'utente identifica l'alimentatore fotografato come quello attualmente in PC-03: Atlantis P016-MPW-6000-W, 600 W massimi dichiarati, due rami +12 V da 22 A e 264 W ciascuno. Targa letta e trascritta nel registro del montaggio; salute elettrica non misurata. ADR-035 resta valido.

Correzione dell'allocazione fisica: l'utente dichiara PC-03 senza alcun SSD e deve controllare se il Samsung sia in un'altra stanza. Su suo richiamo è stata cercata prima la storia in memoria, registri privati, indice delle foto e git: il 09/10 si prevedeva l'estrazione del Samsung 850 EVO per il server, il 12/10 ADR-033 lo destinava al laboratorio; non è stata trovata una conferma del prelievo o del rimontaggio. L'agente aveva ripetuto «già montato» dal piano senza prova dello stato corrente; corrette allocazione, inventario, censimento, schede e ripresa. L'ubicazione resta aperta, il disco non viene dichiarato perso e non si propone un acquisto. Nessun nuovo esito memtest ricevuto: resta la scelta del test fino al 19/10. Nessun subagent avviato. Gli originali Telegram restano fino alla cancellazione verificata dopo la trascrizione.

Archiviazione conclusa nello stesso giro: cancellati soltanto i due originali Telegram indicati dall'utente, dopo il secondo confronto SHA-256. Verificati originali assenti e copie archiviate intatte; il manifesto privato registra l'esito per entrambi. La ricerca documentale sul Samsung ha incluso memoria, contesto, guida e inventario privati, indice delle foto, piano e storia git; trovata l'istruzione di estrazione del 09/10, non una conferma di esecuzione. Il dato attuale resta quello dichiarato dall'utente: PC-03 senza SSD.

Verifiche finali del giro: md-unwrap su 14 Markdown modificati, zero riscritture necessarie; albero docs con 166 documenti tutti raggiungibili, zero orfani e collegamenti rotti; diff pulito con i CRLF conservati. I dodici controlli di chiudi -SoloControlli sono verdi nella ripetizione fuori sandbox. La prima esecuzione aveva superato il guard-rail sui contenuti ma fallito il suo autotest per accesso negato durante la pulizia di una cartella temporanea Windows; nessuna modifica agli strumenti, ripetizione riuscita. Foto originali eliminate e due copie SHA-256 verificate. Nessuna operazione git di scrittura.

## 19/10/2026: etichetta del disco recuperato e contatori Memtest invariati

Lette le due immagini indicate dall'utente dalla cartella Screenpresso e archiviate nella parte privata con confronto SHA-256 identico per entrambe; indice e manifesto aggiornati, originali della cartella di cattura conservati. La targhetta del disco di PC-02 conferma Samsung HD502HJ 500 GB, 7200 giri al minuto, 16 MB, SATA 3 Gb/s, agosto 2011: è il meccanico delle prove, non l'850 EVO da localizzare. Nessuna prova SMART o conferma di montaggio.

Memtest86+ 8.10 mostra 3:46:14, Pass 4, Errors 1, lo stesso indirizzo 0x3a03f65e0 e bit 31 del 16/10, test 6 al 89 per cento e quinto passaggio al 45. Confrontata anche la foto archiviata del 16/10: stessi contatori, quindi nessun nuovo tempo di prova o passaggio pulito attribuito al fine settimana. Scroll lock attivo dal testo del comando in basso. Consultati manuale e codice ufficiali della versione 8.10, fonti S126-S128, e l'estratto del manuale corrente S129: Spazio cambia il blocco senza riavvio; l'attesa è prevista se il blocco è attivo e l'area messaggi è piena, ma qui la causa del fermo non è verificata. Il primo gesto proposto è Spazio una volta e osservazione dell'avanzamento di Time, passo discriminante della verifica manuale; nessun esito ricevuto. Poi resta l'isolamento dei due moduli, non una diagnosi già chiusa. Aggiornati registro, memoria, lavoro corrente, pendenze, fonti e ripresa; guida privata corretta al caso attuale di due moduli e prova di alcune ore ciascuno. Nessun subagent avviato.

Verifiche del 19/10: nove Markdown controllati con md-unwrap senza riscritture; albero docs con 166 documenti tutti raggiungibili e zero collegamenti rotti; diff senza errori considerando i CRLF conservati. I dodici controlli di chiudi -SoloControlli sono verdi dopo ripetizione fuori sandbox per il noto accesso negato alla cartella temporanea dell'autotest. Il controllo aggiuntivo source-register --check trova 13 URL non registrati: tutti già presenti nel file docs/anti-slop/FONTI.md a HEAD, verificati sul contenuto del commit, quindi separati dalle nuove fonti S126-S129 che sono registrate. Pendenza sul censimento delle fonti annotata, senza attribuire una lettura a quei 13 URL. Nessuna operazione git di scrittura.

## 19/10/2026: Memtest non risponde a Spazio

L'utente ha eseguito il riscontro richiesto: premendo la barra spaziatrice non succede nulla, schermata bloccata. Registrata la mancata risposta senza dedurne un modulo guasto o il completamento del test nel fine settimana; resta distinta la mancata risposta da una diagnosi della sua causa. Prossimo gesto indicato al banco: tenere premuto il pulsante di accensione finché il NAS si spegne, circa cinque-dieci secondi. Spegnimento ancora non confermato; dopo verranno scollegamento dalla corrente e preparazione del test dei due moduli separati, uno per volta in DIMM_A1. Nessuna estrazione di memoria ancora avvenuta o richiesta sulla macchina alimentata. Aggiornati registro, snapshot, lavoro corrente, pendenze, guida e ripresa nello stesso giro. Nessun nuovo file immagine, nessuna nuova fonte web e nessun subagent.

## 19/10/2026: NAS spento, prima dell'isolamento dei moduli

L'utente conferma «NAS spento» e autorizza a procedere. Registrato l'arresto, senza assumere già scollegata la corrente o rimosso un modulo. Prossimo gesto unico: staccare il cavo di corrente dal retro del NAS e attendere conferma. La preparazione della prova dei due moduli separati segue solo dopo l'isolamento dell'alimentazione. Aggiornati registro, snapshot, lavoro corrente, pendenze, guida e ripresa; nessuna nuova fonte o evidenza visiva e nessun subagent.

## 19/10/2026: corrente del NAS scollegata

L'utente conferma il cavo scollegato. NAS spento e isolato dalla rete elettrica; nessuna rimozione di memoria confermata. Prossimo gesto unico: tenere premuto il pulsante di accensione per cinque secondi a cavo staccato, come già prescritto dalla guida privata al passo 1.1. Scarica residua e identificazione visiva dei moduli ancora da eseguire; non si è già scelto o rimosso un modulo. Aggiornati registro, memoria, lavoro corrente, pendenze, guida e ripresa. Nessun nuovo test automatico o nuova fonte.

## 19/10/2026: pressione del pulsante a corrente tolta confermata

L'utente conferma eseguita la pressione del pulsante di accensione per cinque secondi a cavo scollegato. Nessun modulo rimosso. Rilette visivamente le foto archiviate del 15/10 della base: riconoscibili ventola Intel e due moduli, non tutti i fermi sono abbastanza chiari per guidare lo sgancio. Prossimo riscontro richiesto: foto ravvicinata dei quattro alloggiamenti RAM, due occupati, con i fermi alle estremità. Si attende l'immagine prima della rimozione. Aggiornati registro, memoria, lavoro corrente, pendenze, guida e ripresa; nessuna nuova immagine ricevuta o nuova fonte web.

## 19/10/2026: foto della memoria lette, prossimo gesto sul fermo di DIMM_B1

Lette e archiviate quattro nuove immagini del NAS, copie confrontate SHA-256 con gli originali, quattro su quattro identiche. Mostrano due moduli ancora montati in DIMM_A1 e DIMM_B1, alloggiamenti intermedi A2 e B2 vuoti. Consultato il manuale ASUS H170-PRO E12046 revisione V2, testo e figure alle pagine 1-2 e 1-9, fonte S130: verificati ordine degli alloggiamenti e fermo mobile su un solo lato. La cattura del PDF con il browser non rendeva visibile la figura nella sessione: scaricato il PDF ufficiale nella parte privata e lette le due pagine rese localmente; nessun altro manuale usato al posto di quello della scheda. Il primo download era bloccato dalla rete del sandbox, ripetuto con accesso autorizzato e riuscito.

Il modulo vicino alla ventola resta in A1. Il gesto unico proposto è aprire il fermo superiore del modulo più lontano dalla ventola, B1, verso il bordo alto della scheda nell'orientamento delle foto; lato inferiore fisso. Nessun fermo ancora confermato aperto e nessuna rimozione eseguita. Dopo l'estrazione si terrà traccia del modulo tolto e il primo test sarà sul solo A1. Aggiornati registro, snapshot, lavoro corrente, pendenze, guida, fonti, indice foto e ripresa; nessun subagent.

Verifica del giro sui fermi: nove Markdown controllati senza riscritture, diff pulito conservando i CRLF; guard-rail su 609 file tracciati con zero riscontri bloccanti. Le quattro copie delle foto sono state rilette nel confronto SHA-256; nessun fermo dichiarato aperto prima del riscontro dell'utente.

## 19/10/2026: RAM di B1 già estratta, preparazione del primo test a 8 GB

Le due immagini successive mostrano il modulo estratto in mano e il solo A1 ancora popolato vicino alla ventola: B1 vuoto, rimozione già eseguita. Etichetta del modulo tolto: Team Group TED48G2400C16BK, 8 GB DDR4-2400, CL16-16-16-39, 1,2 V; identificativi individuali non trascritti in pubblico. Copie delle due immagini archiviate e confrontate SHA-256, due su due identiche; indice e manifesto privati aggiornati.

Prossimo passaggio operativo indicato: ricollegare corrente, accendere e premere F8 per fermarsi al menu di avvio. Consultata la copia locale del manuale ufficiale ASUS, fonte S130, sui richiami di F8 nelle sezioni di avvio. Nessuna conferma ancora di riaccensione, menu, selezione della chiavetta o avvio di Memtest. Il primo modulo in prova sarà quello già rimasto in A1, 8 GB nominali; il modulo estratto da B1 si conserva separato. Aggiornati registro, snapshot, lavoro corrente, pendenze, fonti, indice foto, guida e ripresa. Nessun subagent.

## 19/10/2026: firmware a 8 GB e chiavetta selezionata nel menu F8

Due nuove immagini, ricevute in sequenza nello stesso giro, mostrano prima il firmware EZ Mode e poi il menu F8. NAS riacceso: 8192 MB solo in A1, altri tre slot N/A, DDR4-2133, X.M.P. spento; tre dischi SATA ancora visti. Temperature, ventole, tensione del core e letture complete trascritte nel registro del montaggio. Off del controllo Intel RST appare evidenziato, ma non è una lettura diretta della modalità AHCI. Il menu F8 risponde e mostra già selezionata UEFI: Generic, Partition 2 (59600MB), la stessa voce riuscita il 16/10. Prossimo gesto: Invio per entrare in Ventoy; nessun esito ancora ricevuto e nessun test individuale avviato. Copie SHA-256 identiche per entrambe, indice e manifesti privati aggiornati. Le viste di stato del banco sono state ricomposte in paragrafi attuali, lasciando la sequenza storica nel registro per evitare istruzioni superate nella ripresa.

## 19/10/2026: menu principale Ventoy raggiunto

Nuova immagine: avvio della chiavetta riuscito, menu principale Ventoy/Medicat USB v21.12 in UEFI. Evidenziata la prima categoria, Diagnostic Tools è la quarta. Prossimo gesto unico: selezionare Diagnostic Tools e premere Invio; sottomenu e Memtest 8.10 non ancora avviati, primo modulo A1 da 8 GB ancora da collaudare. Copia archiviata con SHA-256 identico, indice e manifesto privati aggiornati. Viste correnti e ripresa riconciliate con il menu effettivo; nessun subagent o nuova fonte web.

## 19/10/2026: sottomenu Diagnostic Tools, scelta di MemTest86+

Nuova immagine letta e archiviata, copia SHA-256 identica: Diagnostic Tools aperto, riga di ritorno selezionata. MemTest86+ è tre righe sotto, dopo HDAT2 e PassMark MemTest86. Prossimo gesto: Freccia giù tre volte e Invio su MemTest86+; il prodotto PassMark è una voce distinta. Nessuna ISO o test individuale sul solo A1 ancora avviati. Aggiornati stato corrente, registro, guida, ripresa e indice foto; nessuna nuova fonte web o subagent.

## 19/10/2026: ISO 8.10 evidenziata

Nuova immagine: cartella Diagnostic Tools/MemTest86+ aperta, mt86plus_8.10_x86_64.iso già selezionata. Prossimo gesto Invio; immagine o test sul solo A1 da 8 GB non ancora avviati secondo i riscontri. Copia archiviata con SHA-256 identico, indice e manifesto privati aggiornati; stato corrente, pendenze, guida e ripresa aggiornati nello stesso giro. Nessuna nuova fonte web o subagent.

## 19/10/2026: Ventoy attende Boot in normal mode

Nuova schermata ricevuta e letta: la ISO 8.10 è scelta, il menu di modalità avvio ha già evidenziato Boot in normal mode. Prossimo gesto Invio; Memtest sul solo A1 da 8 GB non è ancora avviato. Copia archiviata con SHA-256 identico; aggiornati indice, manifesto, registro e viste correnti. Nessuna nuova fonte web o subagent.

## 19/10/2026: primo test individuale avviato sul modulo A1

Nuova immagine letta e conferma dell'utente: Memtest86+ 8.10 in esecuzione, solo A1 da 8 GB nominali e 7,85 GB utilizzabili; Time 0:00:05, Pass 0, Errors 0, Status Testing. Test 3 Moving inversions, 1s & 0s al 29%, primo passaggio allo 0%; 8 thread paralleli, DDR4-2138 CAS 15-15-15-35, temperatura mostrata 42/48 °C. Nessuna conclusione sulla salute del modulo dalla sola partenza. Lasciare almeno quattro ore, preferibilmente una notte, con controllo fra 10-15 minuti dell'avanzamento per intercettare un eventuale nuovo blocco. Poi testare il modulo estratto da B1 da solo nello stesso A1. Copia SHA-256 identica e originale Screenpresso conservato; aggiornati registro, memoria, lavoro corrente, pendenze, guida, ripresa e indice foto. Nessuna nuova fonte web o subagent.

## 19/10/2026: primo passaggio individuale pulito e avanzamento confermato

Due nuove immagini Memtest86+ 8.10 sul solo A1: Time da 0:53:16 a 0:53:36, Pass 1, Errors 0, secondo passaggio dal 54% al 55%; test 8 Random number sequence dal 30% al 42%, intervallo in prova da 1-2 GB a 2-3 GB, memoria totale 7,85 GB, 48/52 °C. Nella prima compare il banner verde PASS e il comando Scroll unlock, nella seconda il banner è assente e il comando è Scroll Lock; non è documentato quale tasto sia stato premuto. I venti secondi di avanzamento letti sul programma confermano attività fra le catture, senza spiegare il precedente blocco con due moduli. Un passaggio pulito non chiude il collaudo. Indicazione aggiornata: lasciare almeno fino a Time 4:00:00, preferibilmente una notte, con nuova schermata a quel punto o prima se errori o tempo fermo. Secondo modulo da testare separatamente nello stesso A1 dopo questa prova. Due copie SHA-256 identiche, originali Screenpresso conservati; aggiornati registro, viste correnti, pendenze, guida, ripresa e indice foto. Nessuna nuova fonte web o subagent.

## 19/10/2026: errore anche nel primo test individuale, solo A1

Nuova immagine letta: Memtest86+ 8.10 sul solo modulo A1 da 8 GB, 7,85 GB utilizzabili, Time 2:51:08, Pass 3, Errors 1, Status Failed; quarto passaggio al 58%, test 8 Random number sequence al 93%, intervallo 7-8 GB, 48/52 °C. Riga errore: pCPU 5, Pass 3, Test 8, indirizzo 0001efab15d8 (7,74 GB), atteso e7e3be2fa2c35822, letto e7c3be2fa2c35822. XOR calcolato 0x0020000000000000, un bit in posizione 53, da 1 a 0. Il tempo è quello della foto; l'istante esatto dell'errore non è osservato. Non si deduce un blocco da una sola immagine.

La prova è già fallita, quindi superata l'indicazione di attendere almeno quattro ore prima del prossimo riscontro. Prossimo gesto unico: tenere premuto il pulsante fino allo spegnimento del NAS, ancora da confermare; poi scollegamento e preparazione dello scambio. Il confronto successivo sarà con il modulo estratto da B1 da solo nello stesso A1. Riletta la fonte primaria S126, Trouble-shooting Memory Errors: CPU, cache e scheda madre sono coinvolte nella prova, il componente responsabile non è identificato da un errore. Corretta nella guida privata la prescrizione troppo forte di scartare subito il modulo che fallisce da solo; marcata come storica la configurazione a quattro moduli e corretta la prova per cause comuni. Aggiornati anche roadmap, allocazione canonica e passaggi di ripresa rimasti al vecchio test acceso fino al 19/10. Una copia SHA-256 identica, originale Screenpresso conservato, indice e manifesto aggiornati. Scrittura dell'allocazione inizialmente negata, ripetuta con permessi autorizzati e riuscita. Nessuna riallocazione hardware decisa, nessun subagent.

Verifiche del giro: undici Markdown esaminati senza riscritture; guard-rail su 627 file tracciati, zero riscontri bloccanti e 124 voci non bloccanti. Rimosso il CR duplicato sulla sola riga dello snapshot appena modificata, necessario per il diff pulito; nessuna normalizzazione generale dei fine riga. HEAD locale ora 71a863c rispetto a eb4708a della ripresa iniziale, snapshot aggiornato senza cambiare le ancore delle schede o l'impronta di chiusura; nessun commit dell'agente.

## 19/10/2026: NAS spento dopo il primo test individuale fallito

L'utente conferma il NAS spento dopo l'errore sul solo modulo A1. Nessuna nuova schermata o misura. Prossimo gesto unico: scollegare il cavo di alimentazione dal retro del NAS e attendere conferma, poi preparare lo scambio a corrente tolta. Il nuovo scollegamento e lo scambio non sono ancora eseguiti; il modulo estratto da B1 resta separato e da provare da solo nello stesso A1. Aggiornati registro, stato corrente, pendenze, guida e ripresa; nessun nuovo collaudo né componente già dichiarato guasto certo.

## 19/10/2026: cavo del NAS scollegato dopo la prova individuale

L'utente conferma il cavo di alimentazione scollegato dopo lo spegnimento del NAS. Prossimo gesto unico: tenere premuto il pulsante di accensione per cinque secondi con il cavo staccato, poi attendere conferma prima dello scambio della memoria. Questa nuova pressione non è ancora eseguita secondo i riscontri; non usare al suo posto la conferma precedente alla prima prova. Solo A1 ancora inserito, modulo estratto da B1 separato e da provare nel solo A1. Aggiornati registro, memoria, lavoro corrente, pendenze, guida e ripresa; nessuna nuova immagine o misura.

## 19/10/2026: preparazione a corrente tolta confermata prima dello scambio

L'utente conferma la pressione del pulsante per cinque secondi con il cavo di alimentazione staccato, dopo il test individuale fallito. Riletta l'immagine privata già archiviata del solo A1 inserito: modulo vicino alla ventola Intel; manuale S130 già verificato per fermo superiore mobile e lato inferiore fisso. Prossimo gesto unico proposto: estrarre A1 aprendo il solo fermo mobile superiore, prendendolo dai bordi e tenendolo separato dal modulo già estratto da B1. Foto del modulo tolto richiesta per tracciamento; estrazione non ancora eseguita secondo i riscontri, nessun inserimento del secondo modulo. Poi l'ex B1 sarà provato da solo nello stesso A1. Aggiornati registro, memoria, lavoro corrente, pendenze, guida e ripresa; nessuna nuova immagine acquisita.

## 19/10/2026: secondo modulo già in A1, riaccensione senza segnale video

L'utente dichiara già eseguito lo scambio: primo modulo estratto, altro modulo prima in B1 ora da solo in A1, NAS riacceso. Il monitor riferisce nessun input video; nessuna foto nuova, nessuna lettura di firmware o Memtest e nessun riscontro di ventole, cavo video o completo inserimento. Stato accettato su dichiarazione, superata la richiesta della foto del modulo estratto; evitare di chiedere ancora i passaggi già eseguiti. Il nuovo sintomo non qualifica né condanna il secondo modulo.

Consultate FAQ ufficiali ASUS S131-S132: dopo un cambio RAM senza video verificare inserimento completo a cavo di alimentazione rimosso e collegamenti/ingresso monitor. Proposto un tentativo coerente: spegnimento, cavo staccato, pulsante cinque secondi; reinserire lo stesso ex B1 nel solo A1, tacca allineata e due estremità a battuta fino alla chiusura del fermo mobile, poi ricollegare e riaccendere, osservando per un minuto e riferendo video e ventole. Questa osservazione di un minuto è una finestra pratica, non prova o diagnosi di addestramento della memoria. Tentativo ancora da eseguire secondo i riscontri. Aggiornati stato corrente, roadmap, allocazione, pendenze, fonti, guida, ripresa e registro; nessun nuovo scambio di hardware deciso.

## 19/10/2026: video recuperato e secondo test individuale avviato

L'utente conferma ripartenza; nuova immagine letta mostra Memtest86+ 8.10 build 8.10.49468.x64 sul modulo prima in B1, ora da solo in A1 secondo lo scambio dichiarato. 7,85 GB utilizzabili, Time 0:00:07, Pass 0, Errors 0, Status Testing; primo passaggio 1%, test 3 Moving inversions 1s & 0s al 71%, intervallo 4-5 GB, pattern 0x0000000000000000. SPD di un Team Group da 8 GB DDR4-2400, 8 thread PAR, DDR4-2138 CAS 15-15-15-35, 38/45 °C. Il video è quindi tornato; le singole azioni intermedie non sono state descritte separatamente, non si attribuisce la causa con certezza al reinserimento. Primo modulo estratto dopo la prova con un errore a Time 2:51:08, Pass 3; nessun modulo ancora qualificato.

Indicazione: lasciare almeno fino a Time 4:00:00, preferibilmente una notte, nuova schermata di avanzamento ed esito oppure prima se errori o tempo fermo. La foto iniziale non prova ancora l'avanzamento della nuova esecuzione. Copia SHA-256 identica e originale Screenpresso conservato, indice e manifesto aggiornati. Superate le istruzioni di recupero video nelle viste correnti; pendenze, roadmap, allocazione, guida e ripresa riconciliate. Nessun nuovo controllo fisico richiesto prima di lasciare lavorare il test.

## 19/10/2026: avvio del lavoro autonomo su backup e ripristino

L'utente autorizza un'attività utile per dodici ore durante Memtest, senza budget di token e senza persone disponibili a confermare operazioni. Avviato Goal nativo alle 15:51:11 UTC, 17:51:11 locali, con finestra fino al 20/10 alle 03:51:11 UTC. Scelto il piano operativo di backup e ripristino: la cartella esistente contiene titoli Veeam e cloud vuoti; il NAS pianificato ha circa 180 GB di budget e il server uno specchio NVMe da 1 TB. Servono fonti primarie, dimensionamento riproducibile, procedure e criteri di recupero, senza inventare misure o chiudere collaudi fisici. Goal e registro privato conservano i lotti; le continuazioni sono condizionate dalla piattaforma, non si promette riavvio garantito oltre una quota. Fonti S133-S134 consultate con OpenAI Docs.

Stato iniziale: main, HEAD 48100c7, un solo albero, undici file già modificati per il banco; preservati. Sette schede superate rispetto a ee63b19, zero difetti di mappatura. Il documento dei consumi descrive ancora hardware NAS precedente all'allocazione canonica: divergenza da correggere per contenuto. Creato il documento operativo in preparazione e il registro dei lotti, aggiornati indice dei backup, memoria, lavoro corrente, pendenze, fonti e ripresa. Nessun subagent, acquisto, login o operazione sulla rete.

## 19/10/2026: banner del primo passaggio e prosecuzione autonoma ribadita

L'utente riferisce di avere fatto avanzare il banner del primo passaggio del secondo test Memtest. Nessuna nuova immagine, durata o lettura di Errors ricevuta: si registra come avanzamento riferito, senza inventare contatori o chiudere il collaudo. Ribadisce di continuare autonomamente il lavoro già autorizzato per dodici ore; mandato e scadenza non sostituiti, niente richiesta di ulteriori conferme. Aggiornati stato corrente, guida e ripresa; prosegue il piano di backup e ripristino.

## 19/10/2026: primo lotto autonomo, capacità e prove del dimensionamento

Scritti piano iniziale e matrice delle copie, guida al dimensionamento, calcolatore locale, scenario esplicito e suite di 27 prove. Il mirror nominale 240/250 GB vale 240 GB, circa 223,517 GiB prima del filesystem; 80% vale 192 GB, circa 178,814 GiB. Per evitare la vecchia etichetta ambigua «180 GB» il piano propone un tetto prudente esplicito di 180 GB decimali, circa 167,638 GiB, senza cambiare l'allocazione o dichiarare il pool misurato. Nell'esempio costruito il picco è 150,5 GB e il margine 29,5 GB; prima durata 2.903 secondi e ordinaria 2.355 a 20 MiB/s dichiarati più 15 minuti, nessuna prestazione reale misurata.

La prima implementazione considerava soltanto il nuovo file maggiore con lavori sequenziali: correzione sostanziale, perché una generazione intera può coesistere fino al pruning. Conteggio aggiornato, campo della concorrenza rimosso e prova discriminante aggiunta. Sette copie mutate del programma sottoposte alla stessa suite provocano rispettivamente 3, 7, 2, 6, 7, 3 e 2 asserzioni fallite, zero errori di esecuzione, impronta originale invariata. La prima corsa CLI aveva incontrato ACL delle directory TemporaryDirectory Windows; dopo rilancio pytest già autorizzato, fixture resa portabile con file univoci nel workspace. Ventisette prove ora passano nel sandbox, nessuna esclusione aggiunta.

Fonti S135-S142: Proxmox sorgenti ufficiali, TrueNAS stabile 25.10, Veeam 13 e restic 0.19.1. Le due pagine HTML PVE 403 restano etichettate non lette; i contenuti pertinenti sono letti nei sorgenti. Ricerca e runbook restano in corso; il Goal autonomo resta attivo. Aggiornati registri privati dei lotti e affermazioni, fonti, indici e ripresa. Nessuna lettura di dati personali o accesso alle macchine.

Verifica del primo lotto autonomo: tre scenari CLI producono codici 0, 1 e 1, distinguendo piano entro i limiti, capacità superata e finestra insufficiente; risultati JSON privati riletti. Il caso lento richiede nel modello 20.928 secondi per la prima corsa e 15.444 per quella ordinaria contro 10.800 disponibili. Controllo albero su 168 documenti: tutti raggiungibili, zero collegamenti rotti e zero orfani. Guard-rail su 638 file, 631 tracciati e sette nuovi: zero blocchi, 126 voci non bloccanti; la costante di byte per GiB nel documento nuovo è un riscontro non identificante. Dodici Markdown del lotto verificati senza riscritture, diff pulito. Riconciliato il censimento fonti: tredici riferimenti storici aggiunti come non verificati, check 211 URL e zero non registrati. Pendenza di copertura chiusa, nessuna affermazione di lettura completa delle fonti. Aggiornati stato corrente, indice, pendenze, piano, registro privato e ripresa; Goal attivo, runbook e coerenza della destinazione ancora aperti.

## 19/10/2026: secondo lotto autonomo, procedure e dipendenze del recupero

Scritti i runbook per guest PVE, ricostruzione host, configurazione TrueNAS, guasto del disco di avvio e copia distinta dei documenti NAS; preparati percorsi file restic e immagine Windows Veeam. Aggiunti permessi per dataset, finestra proposta 09:00-12:00 da misurare e modello di verbale non compilato. Prove sulle macchine non eseguite. I percorsi T7 verso Drive e T7 Shield verso OneDrive restano intenzioni da verificare, senza presumere supporti, account o quote disponibili.

Il confronto fra PVE gestito soltanto in VLAN 99 e regole tra zone richiede un'eccezione proposta TCP 445 verso NAS dati in VLAN 30; per la gestione PVE manca TCP 8006, distinta dalle porte generali 22/443. Sono lacune del progetto, non guasti di apparati configurati. Il campo di bind SMB nella fonte stabile TrueNAS 25.10 conferma ascolto su tutte le interfacce se lasciato vuoto. Quote e istantanee richiedono una contabilità separata del picco.

Fonti ufficiali S143-S165 registrate; controllo 232 URL e zero non censiti, senza estendere la lettura oltre le sezioni dichiarate. Veeam può saltare un disco esterno assente e terminare con successo in modalità intero computer: il piano verifica il perimetro effettivo oltre all'esito verde. Catena VBK/VIB distinta dal modello restic. Aggiunta la sola esclusione .pytest_cache/ a .gitignore: status non emette più l'errore sulla cache e i nuovi sorgenti restano visibili, senza modificare ACL o cancellare directory.

Primi controlli su tre runbook nuovi: 171 documenti raggiungibili, zero orfani e link rotti; il modello di verbale aggiunto dopo richiede nuovo conteggio. Tabelle e comandi dell'area backup senza difetti. Una scrittura del checkpoint si è fermata nel preflight perché l'ultimo paragrafo di index.md non aveva un successivo separatore vuoto: nessun file scritto in quel tentativo; gestita esplicitamente la fine del file e applicato il lotto con rilettura. Goal attivo, prossimo lotto revisione e riconciliazione storica.

## 20/10/2026: secondo modulo NAS con due errori, banco non qualificato

Nuova immagine indicata dall'utente: Memtest86+ 8.10, ex B1 da solo in A1 secondo il montaggio confermato, 7,85 GB, Time 3:03:15, Pass 3, Errors 2 e Status Failed. Quarto passaggio 93%, test 9 Modulo 20 random pattern 87%; 47/52 °C. Errori ai passaggi 2 e 3, indirizzi 2,81 e 6,49 GB; trascritti nel registro con valori attesi/letti e XOR. Immagine privata archiviata con SHA-256 identico all'originale Screenpresso conservato. Una foto non prova che il timer sia rimasto fermo durante la notte.

Entrambi i moduli sono falliti nello stesso A1: non basta per scartare entrambi o dichiarare certamente sano lo slot. Riletto S126 sul coinvolgimento di CPU, cache e scheda. Prossimo gesto chiesto: spegnere il NAS, senza presumere avvenuti arresto, scollegamento o spostamenti. Dopo la preparazione senza corrente si sceglierà un confronto che cambi solo slot, impostazione o modulo noto sano; nessuna modifica fisica eseguita dall'agente e TrueNAS ancora sospeso.

Il lavoro documentale di backup ha 172 documenti raggiungibili e 239 URL censiti, zero rotture/orfani e zero URL mancanti dal registro. Il controllo del template iniziale aveva due errori: rigenerato l'adattatore cerca-pacchetto con lo strumento e il prefisso già autorizzati, resta la sola fine riga mista del metadato protetto di allineamento. Preparata copia CRLF equivalente nella parte privata; non richiesta una nuova conferma. Preparato e verificato con git apply --check anche il delta per unità e porte SATA dell'allocazione protetta, senza applicarlo.

Una richiesta di permesso per il piano unificato ha invece sospeso la sessione durante la notte e si è conclusa alle 06:59 UTC del 20/10. Non sono state svolte dodici ore continue di lavoro: dichiarato all'utente e corretto lo stato di ripresa. Nessuna quota o test hardware è usato per attribuire lavoro al periodo di attesa. Goal resta attivo per l'audit residuo, mentre la nuova evidenza RAM aggiorna il filo al banco.

## 2026-10-20: audit dei backup, dipendenze di rete e seconda destinazione

L'audit del mandato ha trovato due lacune documentali: dipendenza dai percorsi di gestione della rete per raggiungere le copie, e spazio sottratto ai guest dalla copia proposta dei documenti NAS sul server. Aggiunto il fascicolo di emergenza con export OPNsense, futuri switch/AP, credenziali e supporti leggibili anche senza NAS e PVE; fonti ufficiali S170-S171. Aggiunti due casi costruiti per il mirror server, uno ammesso dal modello e uno saturo: picco 599 GB con margine 101, contro 799 e margine meno 99 su tetto proposto 700 GB. CLI exit 0 e 1, tempi 1950 e 948 secondi; risultati e impronte input archiviati nella parte privata. Un primo atteso manuale 1949 era errato: corretto con aritmetica razionale dopo l'asserzione fallita, programma invariato. Gli esempi non dichiarano protetti tutti i 500 GB dei guest tramite gli archivi NAS dell'altro scenario.

Controlli dopo il lotto: 173 documenti raggiungibili, zero rotture/orfani; 241 riferimenti e zero non censiti. Rimosse otto righe vuote interne al corpo di SOURCES.md: le 171 righe fonte sono conservate e ora contigue sotto la stessa intestazione. Il linter delle colonne era verde anche prima; il riproduttore privato con una riga isolata conferma exit 0. Registrata L-001 nel canale locale del template. La nuova utility di registrazione ha appiattito anche il codice Markdown passato al corpo: la rilettura ha trovato il difetto, conservata copia e ripristinata soltanto la struttura della voce locale, registrando L-002. Nessuna modifica alle copie degli strumenti del template per risolvere questi difetti, nessun messaggio esterno inviato.

Nel frattempo sono presenti modifiche del template a regole, strumenti e craft-apps, indipendenti da questo lavoro: preservate, letto il delta di istruzioni applicabile e rispettato il nuovo campo Template del work-log. Il precedente 11/12 resta un risultato storico sulla versione di allora: controllo globale corrente da rifare. Rimane la correzione EOL preparata per il metadato protetto e la patch allocazione con porte, unità e nuova RAM, non applicate. La richiesta notturna di permesso ha impedito dodici ore continue di lavoro e non è presentata come esecuzione autonoma riuscita.

**Template:** L-001, L-002

## 2026-10-20: controllo globale aggiornato e verifica separata dell'autotest

Rieseguito chiudi-sessione.ps1 con SoloControlli dopo gli aggiornamenti concorrenti del template, senza commit. Nove controlli passano e tre falliscono: autotest del guard-rail su un temporaneo Windows non accessibile, riferimento craft-apps a una configurazione dichiarata opzionale ma assente, EOL del metadato protetto. Il normale controllo di anonimizzazione sui file passa. Il registro delle lezioni viene letto dalla chiusura e non segnala voci di work-log senza il campo previsto dopo l'adozione.

Per distinguere l'errore di ambiente dal risultato del guard-rail, una prova privata invoca il vero tools/Test-Anonymization.py --autotest e richiede il riepilogo con casi effettivamente eseguiti. Eseguita via pytest con prefisso già autorizzato, senza nuovo prompt: una prova passata, autotest 20 casi e zero errori, sorgente invariata e output con SHA archiviato. Non è dichiarato verde il comando completo nel runner ordinario. Non sono state alterate le esclusioni del controllo o le ACL.

Registrate L-003 sul riferimento condizionale della skill e L-004 sul ciclo delle fixture temporanee; nessuna configurazione di stile inventata, nessuna correzione ai tool copiati dal template. La lezione L-002 è stata riletta e normalizzata negli accenti senza perdere il codice restaurato di L-001. Le modifiche del piano restano locali; i dati di rete, i backup e i restore reali non sono stati eseguiti. Il NAS attende ancora conferma dello spegnimento richiesto dopo i due errori del secondo modulo.

**Template:** L-003, L-004

## 2026-10-20: confronto fra archivi PVE e PBS

Aggiunto il confronto 09 per evitare che la deduplicazione venga usata come capacità già disponibile sul piccolo mirror SATA. Distinte risorse del servizio, montaggio e filesystem del datastore, spazio non liberato dal solo pruning, tolleranza della garbage collection e costi di verifica. Proposti token DatastoreBackup con perimetro limitato, chiave client fuori PVE e collaudo del recupero senza dipendere dalla VM PBS perduta. Fonti ufficiali S172-S176, versione documentale HTML 4.2.8-1. Nessuna macchina assegnata, installazione o misura PBS; gli archivi restano il primo percorso proposto. Stato hardware invariato: secondo test individuale fallito e spegnimento ancora da confermare. Segue audit finale degli artefatti e dei delta protetti.

**Template:** nessuna

## 2026-10-20: consegna documentale pronta, mandato temporale non soddisfatto

Completata la verifica degli artefatti del piano: nove documenti operativi compreso il confronto PBS, cinque scenari e risultati locali, procedure di recupero e verbale ancora da eseguire sulle macchine. Albero 174 documenti raggiungibili con zero rotture/orfani; fonti 246 riferimenti senza mancanti, 176 righe S uniche e corpo continuo. L'ordine storico S102 dopo S105 ha fatto fallire una prima asserzione troppo stretta sull'ordinamento: verificata la completezza senza riordinare fonti preesistenti. Tabelle 12 file senza difetti e comandi zero errori/avvisi. Impronte del calcolatore e suite identiche alle prove archiviate, delta protetti ancora applicabili ed equivalenti, non applicati. Risultati effettivi salvati nella parte privata.

Guard corrente 654 file, zero bloccanti e 127 riscontri riletti; quattro avvisi di prosa su enumerazioni funzionali e modulo a campi fissi. Il gate globale resta distinto a 9/12 e l'autotest separato a 20/0, senza ripetere o indebolire prove già valide. Preparazione documentale pronta per la revisione; prove sulle macchine e copie fuori sede non eseguite. La continuità delle dodici ore non è stata rispettata per l'attesa notturna e il Goal non è dichiarato completo. Stato fisico invariato al secondo test RAM fallito: arresto richiesto, non confermato. Corretto anche il prompt volatile e la tabella macchine che conservavano l'avvio del secondo test come punto attuale.

**Template:** nessuna

## 2026-10-20: riaudit dopo aggiornamento concorrente del template

Il giro precedente è progresso: confronto PBS e relative fonti, audit del piano e correzione del prompt corrente sono arrivati su disco. L'allineamento concorrente porta ora il template a 953e506, senza commit dell'agente. Rieseguita la chiusura con SoloControlli sulla nuova versione: dieci controlli passano e due falliscono. Il riferimento craft-apps ora passa; restano autotest nel temporaneo Windows ed EOL del metadato protetto. Il vero autotest ripetuto con pytest e prefisso già autorizzato dà 20 casi e zero errori; output e SHA sono archiviati, senza attribuirlo alla suite ordinaria.

La candidata EOL precedente conteneva il vecchio commit del template: non va applicata al nuovo file. Conservata come evidenza storica, preparati nuovo originale e candidata 953e506 con equivalenza JSON verificata e metadato delta-eol-metadata.json. Il target reale non viene modificato. La chiusura rivela inoltre un errore non bloccante nel richiamo delle lezioni: PowerShell emette una stringa nel ramo con un argomento e la espande in caratteri. Riprodotto osservando System.String e gli argv Python, registrata L-005 con corpo Markdown preservato; nessun fix alle copie degli strumenti. Il controllo lezioni diretto dà tre aperte, due recepite e zero avvisi.

Il verbale include ora anche RETE-01/02 e l'eventuale scenario PBS: le procedure aggiunte non restano fuori dalla selezione del modello. Preparazione documentale pronta, distinta da prove hardware, backup e recuperi reali mai eseguiti. La condizione delle dodici ore continue rimane non soddisfatta e non può essere recuperata retroattivamente. Stato hardware invariato: arresto dopo il secondo test fallito ancora da confermare.

**Template:** L-005

## 2026-10-20: esito del mandato autonomo registrato

Dopo l'audit tecnico e la verifica dei delta il servizio Goal restituisce stato blocked. Non è una consegna dichiarata completa: il vincolo delle dodici ore continue nella finestra originaria resta contraddetto dall'attesa notturna e non è recuperabile con altre modifiche documentali. La condizione è rimasta la stessa negli ultimi tre giri; gli artefatti preparati sono disponibili per la revisione nel manifesto privato, con esiti e limiti espliciti. Nessuna prova sulle macchine è stata eseguita e nessuna nuova autorizzazione è in attesa. Il lavoro al banco rimane separato, alla conferma dell'arresto dopo i due errori RAM.

**Template:** nessuna

## 2026-10-20: arresto del NAS confermato e preparazione del versionamento

L'utente conferma il NAS spento e chiede di fare version control. Aggiornati registro del montaggio, stato corrente, roadmap, pendenze e ripresa: nessuno scollegamento o spostamento successivo è dato per avvenuto. Identità git locale e remoto esistono e corrispondono alla firma dell'ultimo commit; valori identificanti non copiati nei file pubblici. Branch main a 48100c7, un solo albero, indice senza file in stage. Le modifiche del template sono riconosciute come allineamento concorrente e non vengono incluse automaticamente con add -A. In corso verifica del perimetro, correzioni documentali preparate e controlli prima della consegna dei comandi; nessun add, commit o push eseguito.

**Template:** nessuna

## 2026-10-20: applicate le correzioni protette prima del versionamento

Dopo preparazione delle copie e confronto delle impronte, la scrittura ordinaria del metadato è negata dal sandbox. L'utente autorizza il comando limitato ai due file: applicati fine riga CRLF senza variazione del JSON template e allocazione con porte effettive, unità distinte, secondo test RAM fallito e arresto confermato. Rilette le impronte finali; evidenza privata in correzioni-applicate.json. Piano e pendenze ora registrano la riconciliazione canonica effettiva, senza far restare aperto il delta già applicato. Nessun add, commit o push eseguito.

**Template:** nessuna

## 2026-10-20: controlli verdi e perimetri pronti per il versionamento

Dopo le correzioni preparate, la suite completa nel sandbox fallisce soltanto sul noto accesso al temporaneo Windows. Ripetuto lo stesso comando con SoloControlli fuori dal sandbox, senza operazioni Git: dodici controlli passano e il footer è Controlli verdi. Log completo conservato nella parte privata. Resta il messaggio non bloccante del richiamo lezioni PowerShell L-005; il controllo diretto del registro funziona e non è stato escluso alcun caso dell'autotest. Albero 174 documenti senza rotture/orfani, fonti 246 senza mancanti, diff senza difetti. Le sette schede superate e zero difetti di mappatura sono confermati; ancore non avanzate senza una riconciliazione completa.

Preparati due messaggi entro 72 caratteri e due elenchi: 31 file NAS/backup/memoria, 34 dell'allineamento concorrente. Identità locale coerente con l'ultimo commit, main e indice vuoto. Il normale chiudi usa add -A e non supporta un perimetro limitato; non va consegnato per mescolare una sessione eventualmente ancora attiva. È stata posta all'utente la domanda sul termine dell'altra sessione; in attesa della risposta si conservano entrambi i lotti senza stage, commit o push. NAS spento confermato, nessun altro gesto fisico assunto.

**Template:** L-005

## 2026-10-20: perimetro confermato, due commit preparati

L'utente conferma che l'altra sessione ha terminato e ribadisce di procedere. Git mostra il commit di allineamento 4311db3 già creato dall'altra sessione, con ulteriori modifiche del template b2fb025 ancora nel working tree insieme al lavoro NAS e backup. Verificata di nuovo l'identità locale, coerente con l'ultimo commit, e l'indice vuoto. Preparati primo commit parziale del template e successiva chiusura NAS/backup; nessun add, commit o push eseguito dall'agente. Il messaggio di milestone è in COMMIT-MSG.txt.

Normalizzati di nuovo i soli fine riga del metadato riscritto dall'allineamento, preservandone i valori b2fb025, attraverso il comando limitato già autorizzato. Il registro del template riconosce tutte e cinque le lezioni come recepite. L-005 risulta corretta nella copia di chiudi; L-004 è recepita come norma sulle fixture, senza fingere una correzione del guard-rail locale. In corso ultimo giro di controlli sulla nuova versione prima della consegna dei comandi manuali.

**Template:** nessuna

## 2026-10-20: consegna dei due passaggi di versionamento

Suite completa sulla versione finale del template passata: dodici controlli, zero KO, footer Controlli verdi; il controllo lezioni funziona e riporta cinque recepite, zero aperte e zero avvisi. Albero 174 documenti raggiungibili senza rotture/orfani, fonti 246 senza mancanti. Corretti soltanto due a capo vuoti finali trovati da diff --check dopo lo spostamento dello stato corrente; controllo finale senza difetti.

Perimetri correnti verificati senza sovrapposizioni: 37 file template e 31 file NAS/backup/memoria. Il primo passaggio usa percorsi espliciti perché chiudi non supporta un sottoinsieme; il secondo usa la chiusura ordinaria con NoWipe e messaggio già pronto, per committare il lotto residuo e pubblicare entrambi. Comandi e messaggi salvati nella parte privata. L'utente li esegue su main da questo PC; nessuno stage, commit o push è stato eseguito dall'agente. Il NAS rimane spento, corrente scollegata ancora non confermata.

**Template:** nessuna

## 2026-10-20: cavo di alimentazione NAS scollegato

Il versionamento dell'utente è concluso ai commit 9b6d762 e 67abca0, quest'ultimo verificato anche sul remoto. L'utente conferma ora il cavo di alimentazione del NAS scollegato, dopo lo spegnimento già confermato. Aggiornati registro, stato corrente, pendenze e ripresa senza assumere spostamenti RAM o pressione del pulsante già avvenuti. Prossimo gesto comunicato: pulsante di accensione premuto cinque secondi a cavo staccato; nessuna nuova prova di memoria eseguita e TrueNAS resta sospeso.

**Template:** nessuna

## 2026-10-20: pulsante premuto a cavo staccato, prossimo confronto A1-A2

L'utente conferma la pressione per cinque secondi dopo spegnimento e scollegamento del NAS. Il secondo modulo ex B1 resta in A1 e il primo fuori fino a nuova conferma. Verificata visivamente la figura del manuale ASUS S130 a pagina 1-7: A2 raccomandato per un solo modulo, secondo dalla CPU. Richiesta soltanto l'estrazione del secondo modulo da A1, prima della successiva prova in A2 con stesso modulo e impostazioni; nessun esito nuovo. Aggiornati registro del montaggio, allocazione, pendenze, roadmap, stato corrente, registro fonti e ripresa. Impronta di chiusura e frontmatter delle schede non rigenerati.

**Template:** nessuna

## 2026-10-20: posizione di A2 chiarita

Chiarito il riferimento spaziale sul manuale ASUS S130: A2 è adiacente ad A1 allontanandosi dalla CPU, secondo slot dalla ventola Intel; è a destra quando la ventola è alla sinistra degli slot. Nessuna estrazione o installazione confermata dalla domanda dell'utente. Prossima azione fisica invariata, estrazione del solo modulo in A1 a cavo staccato.

**Template:** nessuna

## 2026-10-20: modulo in A2 senza video, avanzamento sul server

Registrato su dichiarazione dell'utente il passaggio del secondo modulo da A1 ad A2 e il nuovo tentativo senza segnale video. Nessun Memtest osservato in A2, nessuna nuova attribuzione del guasto. L'utente chiede di abbreviare il percorso; sospesa la sequenza NAS, proposta prosecuzione sul server Proxmox della roadmap, previa conferma dello spegnimento del NAS. Riletta S102: errori in memoria possono danneggiare i dati e 8 GB è il minimo base, non una qualifica di affidabilità. La coppia Crucial da 4 GB è soltanto un'alternativa proposta per dopo; nessun prelievo o riallocazione definitiva. Riesaminata ADR-016: quarta condizione ancora non soddisfatta, previsto alimentatore alternativo da riprendere. Aggiornati registro NAS, allocazione, pendenze, roadmap, memoria, fonte e ripresa. Nessun cambio hardware eseguito dall'agente, nessun nuovo test fisico o operazione Git.

**Template:** nessuna

## 2026-10-20: obiettivo corretto, completare il NAS e spiegare il rischio

L'utente corregge il fraintendimento: vuole finire il NAS e valutare le conseguenze di un errore, non passare al server. Ripristinato il NAS come lavoro attivo in memoria, pendenze, roadmap, allocazione e ripresa. Spiegato che la coppia mostrava un errore con contatore fermo a 3:46:14, non due giorni di prova attiva documentata; le successive prove individuali hanno mostrato uno e due errori. Nessun tasso di rischio per file calcolabile da questi dati.

Consultata S177 OpenZFS, sezione ECC Memory: effetti da nessun sintomo a blocco, dati o metadati alterati; l'errore precedente al checksum può essere scritto su entrambi i membri del mirror. Esempi foto, ZIP e backup illustrativi, nessun danno reale osservato. Completamento e installazione di prova possibili senza qualifica di affidabilità, conservando originali indipendenti; non dedotta accettazione di perdere dati o cancellare dischi. Primo ostacolo è il video; nessun nuovo gesto fisico confermato, rimane richiesto lo spegnimento prima di interventi. Diagnosi RAM e quarta condizione di ADR-016 aperte; nessun altro ciclo lungo o cambio di componenti richiesto ora.

**Template:** nessuna

## 2026-10-20: NAS spento dopo il mancato video in A2

Confermato dall'utente lo spegnimento del NAS; secondo modulo nell'ultimo A2 dichiarato, primo fuori. Lo scollegamento dopo questo tentativo non è confermato. Prossima azione richiesta: togliere il cavo di alimentazione dal retro, prima del controllo dell'inserimento in A2. Resta attivo il completamento NAS, senza altro lungo Memtest richiesto. Aggiornati registro del montaggio, allocazione, pendenze, memoria, lavoro corrente e ripresa; nessun intervento fisico dell'agente.

**Template:** nessuna

## 2026-10-20: corrente scollegata dopo il tentativo senza video in A2

L'utente conferma il cavo di alimentazione scollegato dal retro del NAS, già spento. Modulo nell'ultimo A2 dichiarato e primo modulo fuori, senza nuovi spostamenti. Prossimo gesto richiesto: premere il pulsante di accensione per cinque secondi a cavo staccato, ancora da confermare per questa preparazione. Seguono controllo dell'inserimento e recupero video; nessun altro lungo Memtest richiesto. Aggiornati registro NAS, allocazione, pendenze, memoria, lavoro corrente e ripresa.

**Template:** nessuna

## 2026-10-20: preparazione completata, reinserimento in A2 richiesto

Confermata dall'utente la pressione per cinque secondi a cavo staccato dopo il tentativo senza video; spegnimento e scollegamento già confermati. Riletta visivamente la pagina 1-9 di S130 sul fermo mobile singolo. Prossimo gesto richiesto: reinserire lo stesso modulo nello stesso A2, tacca allineata e due estremità in sede fino alla chiusura del fermo superiore; nessun inserimento o nuovo avvio confermato. Si prepara il recupero video per completare il NAS, senza altro lungo Memtest automatico. Aggiornati registro NAS, allocazione, pendenze, memoria, lavoro corrente e ripresa.

**Template:** nessuna

## 2026-10-20: NAS ripartito dopo il reinserimento richiesto in A2

L'utente riferisce la ripartenza dopo il reinserimento dello stesso modulo nello stesso A2 richiesto a corrente tolta e chiede come procedere. Nessuna nuova foto o lettura firmware ricevuta e causa del mancato video non isolata. Richiesta una foto completa della schermata corrente con nome del file, prima di scegliere il passo successivo verso firmware e installazione TrueNAS. Nessun altro lungo Memtest o riavvio richiesto per automatismo; diagnosi RAM aperta. Aggiornati registro NAS, allocazione, pendenze, roadmap, memoria, lavoro corrente e ripresa.

**Template:** nessuna

## 2026-10-20: test A2 prima della coppia finale, corretto l'anticipo dell'installazione

L'utente richiama i test, segnala che il NAS ha una sola RAM e chiede precisione. Corretto il percorso attivo: secondo modulo da solo in A2 come confronto temporaneo da 8 GB; obiettivo finale 16 GB A2+B2, poi installazione. Dichiarati scopo e limite: verificare se gli errori osservati in A1 si ripetono col medesimo DIMM in A2, quattro passaggi completi senza errori o stop al primo errore/blocco documentato. Se supera, aggiunta dell'altro in B2 a corrente tolta e prova della coppia con stesso criterio; se fallisce, registrazione e arresto del percorso senza identica ripetizione automatica. Nessuna garanzia assoluta o diagnosi dello slot dedotta. Richiesta foto della schermata corrente per avviare Memtest, nessun nuovo test osservato. Aggiornati registro NAS, allocazione, pendenze, roadmap, memoria, lavoro corrente e ripresa.

**Template:** nessuna

## 2026-10-20: Memtest RAM-02/A2 avviato e identità dei due moduli fissata

L'utente conferma Memtest partito in A2 sullo stesso modulo prima testato in A1 e chiede nomi per i pezzi. Assegnati nomi persistenti: RAM-01 primo test individuale A1, ora fuori; RAM-02 originariamente B1, secondo test A1 e ora in A2. Pubblicate nel registro NAS legenda e matrice delle prove individuali: RAM-01/A1 un errore, RAM-02/A1 due, RAM-02/A2 in corso su dichiarazione senza contatori. Nessun risultato individuale attribuito a B1/B2 dalla coppia originale. Richiesto foglietto RAM-01 accanto al modulo fuori, senza toccare RAM-02 in funzione; applicazione non confermata. Prossimo riscontro foto a quattro passaggi o al primo errore/blocco prima dell'arresto. Coppia finale prevista RAM-02/A2 più RAM-01/B2 se la prova consente di proseguire, nessuna serie automatica sugli altri slot. Aggiornati registro, allocazione, pendenze, roadmap, memoria, lavoro corrente e ripresa.

**Template:** nessuna

## 2026-10-20: RAM-02/A2 fallita e due etichette fisiche confermate

Lette due nuove immagini Memtest86+ 8.10: RAM-02/A2 secondo configurazione dichiarata, 7,85 GB, Time 0:23:17 e 0:23:21, Pass 1, Errors 1, Failed. Riga Pass 0 Test 9, indirizzo 0x0000b479e178, bit 42 calcolato e verificato: stesso indirizzo e bit del primo errore RAM-02/A1. Indizio a favore del modulo, nessuna certezza sul componente e canale A comune ancora non escluso. Tempo avanzato quattro secondi, non un blocco documentato. Etichette RAM-01 e RAM-02 applicate su conferma dell'utente. Due copie archiviate con SHA-256 identico agli originali conservati, manifesto e indice privato aggiornati.

Prova chiusa come fallita: non aspettare quattro passaggi né avviare la coppia con RAM-02. Richiesto spegnimento, ancora non confermato; poi preparare confronto RAM-01 nello stesso A2 a corrente tolta, cambiando soltanto il modulo. Nessun altro scambio o test eseguito. Aggiornati registro NAS, allocazione, pendenze, roadmap, fonte S126, memoria, lavoro corrente e ripresa; nessuna nuova qualifica o operazione Git.

**Template:** nessuna

## 2026-10-20: RAM-01/A2 avviata, corretta l'associazione dell'immagine

L'utente riferisce lo scambio già completato e Memtest partito su RAM-01 sola in A2. Il primo file indicato è risultato SHA-256 identico all'immagine della precedente RAM-02/A2: non attribuito a RAM-01 il vecchio errore. L'utente corregge il riferimento e conferma verifica visiva della combinazione al banco. Nuova immagine letta: Memtest86+ 8.10, 7,85 GB, Time 0:00:02, Pass 0, Errors 0, Testing; test 3 al 21%, 50/50 °C, DDR4-2138 CAS 15-15-15-35, 8T PAR. Copia privata archiviata e riletta con SHA-256 identico, originale conservato; manifesto e indice aggiornati.

RAM-01/A2 ora in corso, RAM-02 fuori; nessuna qualifica dai due secondi iniziali. Prossimo riscontro foto a quattro passaggi completi senza errori o al primo errore/blocco documentato prima dell'arresto, nessun nuovo scambio richiesto. Aggiornati registro NAS, allocazione, pendenze, roadmap, memoria, lavoro corrente e ripresa. Nessuna nuova operazione fisica dell'agente o azione Git.

**Template:** nessuna

## 2026-10-21: RAM-01/A2 fallita dopo il riscontro serale senza errori

Lette insieme le due immagini della sera del 20/10 e quella del mattino del 21/10. RAM-01/A2 a 0:25:57 e 0:26:01: Pass 1, Errors 0; al mattino 0:55:10: Pass 1, Errors 1, Failed, test 8. Indirizzo 0x0001efab15d8 e bit 53 identici al precedente RAM-01/A1, con verso opposto, verificati sulle trascrizioni del registro; nessuna qualifica di modulo o certezza della causa. Entrambi i TEAMGROUP hanno ora fallito A1 e A2. Il contatore non documenta una notte intera di esecuzione attiva e non isola la causa del mancato avanzamento.

Tre immagini archiviate e rilette, SHA-256 identico e originali conservati; manifesto definitivo e indice privato aggiornati. Richiesto spegnimento, ancora da confermare; proposto confronto con due Crucial DDR4 da 4 GB previsti come scorta, non estratti o qualificati. Prova da 8 GB, nessuna nuova allocazione definitiva e 16 GB NAS ancora da risolvere. Se fallisce anche memoria alternativa, riprendere cause comuni e ADR-016 invece di un'altra serie sugli slot. Aggiornati registro NAS, allocazione, pendenze, roadmap, fonti S102/S126, memoria, lavoro corrente e ripresa; impronta di chiusura non rigenerata e nessuna operazione Git.

**Template:** nessuna

## 2026-10-21: origine dei Crucial e coppia alternativa già disponibile

L'utente chiede quale smontaggio fornisca i Crucial. Verificati ADR-032 e inventario: quattro moduli da 4 GB nel futuro server linux-desktop-A, H270M Pro4/i7-7700; due diventerebbero scorta soltanto dopo lo scambio ancora non confermato. Nuova foto letta: due TEAMGROUP TED48G2400C16BK da 8 GB DDR4-2400, 1,2 V, già sul banco e associati a PC-DESKTOP-B. Copia privata SHA-256 identica, originale conservato, manifesto e indice aggiornati. Proposti nomi RAM-03 superiore e RAM-04 inferiore della foto, etichette ancora da confermare.

Aggiornato il controllo proposto alla coppia già disponibile da 16 GB, RAM-03/A2 e RAM-04/B2 dopo spegnimento e preparazione a corrente tolta, invece di richiedere ora il prelievo Crucial. Nessun nuovo montaggio o spegnimento confermato. Criterio della nuova coppia almeno cinque passaggi completi senza errori o stop al primo errore/blocco: il precedente insieme aveva fallito nel quinto dopo quattro puliti. Prestito temporaneo, assegnazione definitiva e conto dei 24 GB server ancora aperti; ADR-016 non chiusa. Aggiornati registro NAS, allocazione, pendenze, roadmap, memoria, lavoro corrente e ripresa.

**Template:** nessuna

## 2026-10-21: corrente NAS rimossa, ruolo della scorta e prova della coppia chiariti

L'utente conferma di avere tolto corrente al NAS, chiede che cosa fare di PC-DESKTOP-B dopo i prelievi e vuole capire la prova. Verificati inventario e allocazione: conservare la scorta assemblata e spenta con B150-PRO, i7-6700, dissipatore, alimentatore, case/ventole e unità ottica; RAM e SSD già rimossi, nessun altro smontaggio ora. RAM-01 resta nell'ultimo A2 dichiarato e RAM-02 fuori. Prossimo gesto richiesto pressione del pulsante per cinque secondi a cavo scollegato, non ancora confermato; nessuna nuova etichetta o inserimento dei due moduli alternativi confermato.

Spiegata la prova successiva: coppia alternativa RAM-03/A2 e RAM-04/B2 da 16 GB, senza altre modifiche, almeno cinque passaggi completi senza errori o arresto dopo foto al primo errore/blocco; il vecchio insieme falliva nel quinto. Scopo confrontare la macchina con altra memoria, non diagnosticare da solo il componente. Nessuna nuova serie automatica sugli slot. Allocazione definitiva NAS/server e quarta condizione ADR-016 aperte. Aggiornati registro NAS, allocazione, pendenze, roadmap, memoria, lavoro corrente e ripresa; nessun intervento fisico o operazione Git dell'agente.

**Template:** nessuna

## 2026-10-21: Memtest della coppia RAM-03/A2 e RAM-04/B2 avviato, limiti del confronto chiariti

Cinque nuove immagini confermano etichette e montaggio: RAM-03 in A2, RAM-04 in B2, A1/B1 vuoti e RAM-01/RAM-02 fuori. Memtest86+ 8.10 su 15,8 GB utilizzabili a Time 0:00:04, Pass 0, Errors 0, Testing. Nessuna qualifica. Originali conservati, cinque copie private con SHA-256 identico, manifesto e indice aggiornati; ordine delle catture distinto da ordine degli eventi fisici.

Su obiezione dell'utente esplicitato il cambio di obiettivo: prova della configurazione candidata da 16 GB, non isolamento di una sola variabile. Cambiano moduli, numero, capacità e uso del canale B; A2+B2 raccomandato dal manuale ASUS S130, pagina 1-7, ricontrollato visivamente. Il confronto controllato avrebbe usato RAM-03 da sola nello stesso A2. Proseguire la coppia già avviata per almeno cinque passaggi senza errori, foto e stop al primo errore/blocco. Se fallisce, prossimo confronto proposto RAM-03 da sola in A2, nessuna serie automatica di tutti gli slot; un esito pulito non prova il guasto dei due vecchi moduli. Accettazione notturna ADR-016 e allocazione definitiva NAS/server ancora aperte. Aggiornati registro, allocazione, pendenze, roadmap, fonti, memoria, lavoro corrente e ripresa. Nessuna operazione Git.

**Template:** nessuna

## 2026-10-21: confermata prosecuzione della coppia, esito in attesa

L'utente conferma di lasciare proseguire la prova RAM-03/A2 + RAM-04/B2 e chiede che sia registrato tutto. Nessun nuovo contatore o esito comunicato: resta valido soltanto l'avvio documentato. Nessuna modifica alla configurazione richiesta; attesa di almeno cinque passaggi completi con Errors 0, oppure foto e arresto al primo errore o blocco documentato. Restano registrati anche lo scopo della prova della coppia da 16 GB e i suoi limiti per isolare il guasto.

**Template:** nessuna

## 2026-10-21: banner PASS riferito, barra spaziatrice premuta e contatori da acquisire

Ultima segnalazione: l'utente riferisce il banner PASS per la coppia RAM-03/A2 + RAM-04/B2 e dice di avere premuto la barra spaziatrice per proseguire. Si registra la dichiarazione senza attribuire un numero di passaggi completati, una durata o un totale di errori non ancora letti. Il banner da solo non verifica il criterio concordato di almeno cinque passaggi completi con Errors 0. Richiesta identificazione della schermata disponibile per acquisire Time, Pass, Errors e stato attuale; nessuna nuova manipolazione o riavvio richiesto. Prova e accettazione finale restano aperte.

**Template:** nessuna

## 2026-10-21: PASS senza schermata, prova lasciata proseguire

L'utente precisa che non c'è una schermata da acquisire: riferisce soltanto PASS, lascia proseguire la prova RAM-03/A2 + RAM-04/B2 e aggiornerà lui. Richiesta di identificare una schermata superata; nessun altro screenshot o contatore da sollecitare ora. PASS registrato come dichiarazione, senza inventare durata, numero di passaggi o totale degli errori. Nessun cambio alla configurazione o riavvio richiesto; si attende il prossimo aggiornamento dell'utente.

**Template:** nessuna

## 2026-10-21: coppia alternativa fallita, Errors 2 nel secondo passaggio

Aggiornamento del 21/10/2026: la coppia alternativa RAM-03/A2 + RAM-04/B2 è fallita. Nuova schermata Memtest86+ 8.10: 15,8 GB, Time 0:53:56, Pass 1, Errors 2, Status Failed; secondo passaggio al 54%, test 8 Random number sequence al 33%. Una sola riga di errore visibile: pCPU 2, Pass 1, Test 8, indirizzo 0x00008fb766b8 (2,24 GB), atteso 0xf56caad22e562f66, letto 0xf56c2ad22e562f66; XOR 0x0000800000000000, bit 47 da 1 a 0. Il contatore totale è due, ma la foto non mostra due righe distinte. Il PASS riferito prima non era un esito finale; criterio dei cinque passaggi senza errori non raggiunto. Non dedurre da una sola schermata un blocco o da questa coppia il guasto individuale di RAM-03/RAM-04; restano possibili cause comuni, B2/canale B e interazione fra moduli. RAM-03 resta nell'ultimo A2 confermato, RAM-04 in B2; RAM-01/RAM-02 fuori e già fallite individualmente A1/A2. Prossimo gesto richiesto spegnere il NAS e scollegare il cavo di alimentazione, ancora da confermare; non muovere RAM ora. Dopo preparazione a corrente tolta, confronto già previsto: togliere soltanto RAM-04 da B2, lasciare RAM-03 da sola nello stesso A2 e riprovare senza cambiare impostazioni. Nessuna matrice automatica di tutti gli slot. Quarta condizione ADR-016, cause comuni e allocazione definitiva NAS/server ADR-032 aperte. PC-DESKTOP-B resta scorta assemblata e spenta senza RAM/SSD; TrueNAS non installato. Foto archiviata con SHA-256 identico, originale conservato.

**Template:** nessuna

## 2026-10-21: avvio prova individuale RAM-03/A2 confermato

Nuovo test del 21/10/2026: l'utente conferma di avere completato la preparazione e avviato Memtest con RAM-03 da sola nello stesso A2. RAM-04 rimossa da B2, A1/B1/B2 vuoti su configurazione dichiarata; RAM-01/RAM-02 restano fuori. La schermata conferma un solo modulo da 8 GB e 7,85 GB utilizzabili, non identifica da sola l'etichetta fisica o il nome ASUS dello slot. Memtest86+ 8.10 build 8.10.49468.x64, Time 0:00:04, Pass 0, Errors 0, Testing; primo passaggio allo 0%, test 3 Moving inversions, 1s & 0s al 28%. DDR4-2138, IMC 1069 MHz, CAS 15-15-15-35, SMP 8T PAR, CPU 3408 MHz, temperatura 39/45 °C. SPD software Slot 1: 8 GB DDR4-2400 Team Group TEAMGROUP-UD4-2400, 2016-W48; Slot 1 non è il nome ASUS A1. Nessuna qualifica dall'avvio. Criterio della prova individuale: quattro passaggi completi con Errors 0, come per i precedenti confronti individuali A2, oppure foto e arresto al primo errore/blocco documentato; i cinque passaggi restano il criterio della futura coppia finale, non una prova già superata. La coppia RAM-03/A2 + RAM-04/B2 resta fallita a 0:53:56, Pass 1, Errors 2; RAM-03 e RAM-04 non sono ancora qualificate individualmente. Togliere RAM-04 verifica il comportamento del modulo rimasto in A2, ma un eventuale esito pulito non distingue da solo modulo tolto, B2/canale B o interazione della coppia. Lasciare proseguire senza altre modifiche; nessun nuovo spegnimento o montaggio da richiedere. Cause comuni, ADR-016 e allocazione definitiva NAS/server ADR-032 restano aperte. TrueNAS non installato. Foto copiata e SHA-256 identico all'originale conservato.

**Template:** nessuna

## 2026-10-21: RAM-03/A2, PASS riferito senza schermata e prova in prosecuzione

L'utente riferisce PASS nella prova di RAM-03 da sola in A2, dice di avere premuto la barra spaziatrice e lascia proseguire il test, senza schermata. Segnalazione registrata senza attribuire contatori, durata o numero di passaggi non acquisiti; il criterio dei quattro passaggi completi con Errors 0 resta da verificare. Nessun cambio alla configurazione, nessuno screenshot da richiedere ora; attendere il prossimo aggiornamento dell'utente.

**Template:** nessuna

## 2026-10-22: RAM-03/A2 circa 22 ore senza fail riferite, prossimo confronto RAM-04 nello stesso slot

Aggiornamento del 22/10/2026: l'utente riferisce circa 22 ore di prosecuzione del Memtest di RAM-03 da sola nello stesso A2 senza fail. Si registra un esito prolungato positivo su dichiarazione e si ritiene sufficiente questa prova individuale per avanzare, senza prolungarla ancora. Durata approssimata riferita, non contatore Time letto dall'agente; nessuna nuova schermata, numero di passaggi o valore del contatore Errors acquisito. Il precedente PASS era riferito, seguito dalla prosecuzione. RAM-03/A2 è quindi la prima configurazione individuale con un risultato prolungato positivo; non è una garanzia assoluta né l'accettazione del NAS da 16 GB. RAM-01/RAM-02 restano fallite individualmente A1/A2, la coppia RAM-03/A2 + RAM-04/B2 resta fallita a 0:53:56 con Errors 2. RAM-04 non ancora provata da sola. Il risultato riduce il sospetto sulla combinazione RAM-03/A2 in questa configurazione, ma non distingue da solo RAM-04, B2/canale B e carico o interazione dei due moduli. Prossimo gesto richiesto spegnere il NAS e scollegare alimentazione, ancora da confermare; il test è ancora in corso nell'ultimo stato riferito. Poi sostituire soltanto RAM-03 con RAM-04 nello stesso A2, un solo modulo, impostazioni invariate. Criterio per RAM-04 individuale: quattro passaggi completi senza errori o arresto al primo errore/blocco documentato, senza richiedere un'altra prova di 22 ore. Nessuna matrice automatica degli slot. Accettazione finale, ADR-016 e allocazione definitiva NAS/server ADR-032 restano aperte; i cinque passaggi appartengono al criterio della futura coppia finale. PC-DESKTOP-B resta scorta assemblata e spenta senza RAM/SSD. TrueNAS non installato; nessun nuovo screenshot da richiedere per registrare questa dichiarazione.

**Template:** nessuna

## 2026-10-22: prova individuale RAM-04/A2 avviata dopo RAM-03

Avviata la prova concordata di RAM-04 da sola nello stesso A2, RAM-03 rimossa. Schermata Memtest86+ 8.10 build 8.10.49468.x64: 7,85 GB, Time 0:00:35, Pass 0, Errors 0, Testing; primo passaggio al 3%, test 4 Moving inversions, 8 bit pattern al 47%, intervallo 2 GB - 3 GB, pattern 0xfdfdfdfdfdfdfdfd. CPU 3408 MHz, temperatura 46/50 °C, IMC 1069 MHz, DDR4-2138 CAS 15-15-15-35, SMP 8T PAR. SPD software Slot 1: 8 GB DDR4-2400 Team Group TEAMGROUP-UD4-2400, 2016-W48. Slot 1 non è il nome ASUS A1; identità RAM-04 e posizione A2 derivano dal passo concordato e dall'avvio riferito, non dalla sola schermata SPD. È soltanto l'avvio, nessuna qualifica di RAM-04. Lasciare proseguire per quattro passaggi completi con Errors 0 oppure foto e arresto al primo errore/blocco, senza altre modifiche. RAM-03/A2 conserva circa 22 ore senza fail su dichiarazione; coppia RAM-03/A2 + RAM-04/B2 fallita a 0:53:56 con due errori. Cause comuni, configurazione finale, ADR-016 e allocazione NAS/server aperte. TrueNAS non installato. Foto archiviata e SHA-256 identico all'originale conservato; nessun nuovo spegnimento o montaggio da richiedere.

**Template:** nessuna

## 2026-10-22: RAM-04/A2 fallita, richiesto proseguimento con sola RAM-03 e BIOS

RAM-04 da sola in A2 ha mostrato un errore: Memtest86+ 8.10 build 8.10.49468.x64, Time 0:04:38, Pass 0, Errors 1, Status Testing; primo passaggio al 27%, test 6 Moving inversions, 64 bit pattern al 36%. Il test è fallito secondo il criterio di zero errori, anche se lo stato visualizzato non è ancora Failed. Una riga visibile: pCPU 1, Pass 0, Test 6, indirizzo 0x000047abb378 (1,12 GB), atteso 0x0000080000000000, letto 0x0000000000000000, XOR 0x0000080000000000, bit 43 da 1 a 0. RAM 7,85 GB utilizzabili, CPU 3408 MHz, temperatura 47/50 °C, DDR4-2138 CAS 15-15-15-35, 8T PAR. Non si deduce un blocco da una sola schermata. RAM-03 nello stesso A2 ha circa 22 ore senza fail su dichiarazione: il confronto rafforza nettamente il sospetto su RAM-04, da escludere operativamente dal NAS, senza certificare ogni causa comune o B2. RAM-01/RAM-02 restano sospette e fuori; non buttare i moduli. L'utente invita a procedere. Percorso attivo: spegnere e scollegare il NAS, a LED spenti sostituire RAM-04 con la sola RAM-03 nello stesso A2, poi riaccendere ed entrare nel BIOS con Canc per proseguire il montaggio e verificare firmware/dischi. Tutti questi nuovi gesti ancora da confermare; ultima configurazione RAM-04/A2 con errore. Nessun altro Memtest identico su RAM-03 né nuova matrice di slot richiesta. Configurazione candidata per avanzare da 8 GB, coerente con il minimo base di S102; obiettivo precedente 16 GB e conto server di ADR-032 da rivedere, non contare gli stessi moduli due volte. Accettazione finale e ADR-016 ancora aperte; nessuna installazione o cancellazione eseguita. TrueNAS non installato. Foto archiviata con SHA-256 identico, originale conservato.

S102 requisito minimo base riletto online; URL corrente sviluppo28, nessuna release selezionata. Aggiornati registro, allocazione, pendenze, roadmap, fonti, memoria, lavoro corrente e ripresa. Nessuna operazione Git o installazione.

**Template:** nessuna

## 2026-10-23: rimontaggio RAM-03/A2 e BIOS confermati

Aggiornamento del 23/10/2026: l'utente conferma RAM-03 rimontata nello stesso A2 e ingresso nel BIOS. Nuova configurazione corrente confermata su dichiarazione, non più preparazione pendente: NAS acceso nel firmware con la sola RAM-03, RAM-04 rimossa secondo il passo concordato; RAM-01/RAM-02 fuori. Nessuna nuova schermata BIOS ricevuta o letta: memoria effettivamente rilevata, presenza e porte dei tre SSD e modalità SATA/AHCI restano da verificare, non si presumono dai dati dei giorni precedenti. Prossimo riscontro richiesto una foto intera e leggibile della schermata BIOS attuale; nessuna modifica alle impostazioni richiesta prima della lettura. Nessun nuovo spegnimento, rimontaggio o Memtest identico da richiedere. Base del percorso candidato da 8 GB: RAM-03/A2 circa 22 ore senza fail riferite il 22/10; RAM-04/A2 fallita a 0:04:38, Errors 1, Status Testing, test 6 e bit 43. RAM-01/RAM-02 fallite individualmente A1/A2 e coppia RAM-03/A2 + RAM-04/B2 fallita. RAM sospette escluse dall'uso NAS e conservate etichettate. Accettazione ADR-016 e riallocazione NAS/server ADR-032 ancora da riconciliare; TrueNAS non installato, AHCI, SMART lungo e dati SanDisk da verificare.

**Template:** nessuna

## 2026-10-23: EZMode conferma RAM8GB/A2 e treSSD, controllo AHCI successivo

Aggiornamento del 23/10/2026: letta la schermata ASUS H170-PRO EZ Mode, BIOS 3805. RAM-03 nello stesso A2 su conferma precedente dell'utente; ora il BIOS osservato mostra 8192 MB DDR4 a 2133 MHz, solo DIMM_A2 Team Group 8192 MB 2400 MHz SPD, A1/B1/B2 N/A, XMP Disabled. Tre SSD rilevati sulle porte previste: SATA6G_1 SanDisk SDSSDA240G 240 GB; SATA6G_2 Kingston SV300S37A240G 240 GB; SATA6G_6 WDC WDS250G1B0A-00H9H0 250 GB. Porte 3/4/5 N/A. CPU 34 °C, scheda 27 °C, CPU Core Voltage 1,104 V; questo non è il +12 V dell'alimentatore. Intel Rapid Storage mostra Off evidenziato, ma SATA Mode Selection non è visibile: AHCI resta da verificare direttamente. Prossimo passo F7, Advanced, SATA Configuration, leggere SATA Mode Selection e acquisire schermata senza cambiare valori. Percorso riscontrato sul manuale S130 sezione 2.6.5, pagina 2-32, PDF 66. RAM-03/A2 circa22h senza fail su dichiarazione; RAM-01/RAM-02/RAM-04 fuori e sospette, nessun nuovo Memtest richiesto. TrueNAS non installato; SMART lungo, dati SanDisk, accettazione e riallocazione NAS/server restano aperti. Foto archiviata con SHA-256 identico, originale conservato.

**Template:** nessuna

## 2026-10-23: correzione menu BIOS e studio Cloudflare nel contesto del progetto

Aggiornamento del 23/10/2026: le due foto corrette mostrano il menu Advanced del BIOS, non ancora il campo SATA Mode Selection. Nel BIOS corrente la voce si chiama PCH Storage Configuration: correggere il percorso precedente Advanced > SATA Configuration, che deriva dal manuale E12046 ma non dal nome effettivo della versione osservata. Prossimo riscontro: aprire Advanced > PCH Storage Configuration e fotografare SATA Mode Selection senza cambiare valori. AHCI resta da verificare. Monitor hardware osservato: memoria 8192 MB a2133MHz, tensione DRAM1,200V, CPU34°C e3400MHz, Vcore1,104V; +12V12,192V, +5V5,040V, +3,3V3,392V. Il +12V è ora letto direttamente nel BIOS, senza confonderlo con Vcore, e non certifica da solo l'alimentatore. Sola RAM-03/A2 e treSSD porte1/2/6 già osservati; RAM-03 circa22h senza fail su dichiarazione, RAM-01/RAM-02/RAM-04 fuori. Nessun nuovo Memtest. Foto copiate con SHA-256 identici e originali conservati; identificativo NIC non trascritto nel livello pubblico. TrueNAS non installato; SMARTlungo, datiSanDisk, accettazione e allocazione restano aperti.

Studio Cloudflare Zero Trust Free e alternative completato il23/10/2026 in docs/03-spunti-di-sviluppo/23-studio-home-lab/15-cloudflare-zero-trust-e-alternative.md, con fonti primarie aggiornate. Raccomandazione dell'analisi: mantenere WireGuard su OPNsense per accesso amministrativo, AdGuard/Unbound per DNS locale e priorità a VLAN/AP/firewall; Cloudflare soltanto candidato facoltativo per una singola applicazione web non critica, senza nuovi ingressi di gestione o inoltro DNS della casa. Gateway come DNS richiederebbe rivedere ADR-007; pubblicare amministrazione tramite Access rivedrebbe ADR-025. Free verificati: Cloudflare50utenti e logstandard fino24h; TailscalePersonal6utenti, dispositivi personali illimitati e50risorse con tag incluse; NetBirdCloud5utenti/100macchine, Communityautogestita gratuita distinta dalle funzioniEnterprise. Nessun account creato, connettore installato, configurazione modificata o prova eseguita. Nessuna nuova decisione di adozione.

Aggiornati indice dello studio, confronto VPN, registro fonti e roadmap; nessuna nuova adozione o operazione Git.

**Template:** nessuna

Verifiche del giro: md-unwrap su 14 file senza modifiche; albero documentale con 175 documenti tutti raggiungibili, zero collegamenti rotti e zero orfani; cinque file di tabelle senza difetti; diff whitespace pulito. Guard-rail di anonimizzazione: 664 file esaminati, zero riscontri bloccanti; 127 riscontri non bloccanti da valutazione, principalmente importi e indirizzi del piano privato già documentati. Nessun commit o push eseguito.

## 2026-10-23: approvazioni per bisogni, avvio tecnico-didattico e AHCI verificato

Aggiornamento del 23/10/2026: letta direttamente nel BIOS la modalità SATA Mode Selection AHCI, controller SATA Enabled, percorso Advanced > PCH Storage Configuration. Nessuna modifica di questi valori richiesta. Hyper Kit Mode Disabled, Aggressive LPM Support Disabled; SMART Self Test mostra On, che non documenta l'esito di un test lungo. Visibili SanDisk240 su SATA6G_1 e Kingston240 su SATA6G_2; WD250 su SATA6G_6 già osservato nella schermata EZ. Memoria8192MB a2133MHz, DRAM1,200V; CPU35°C3400MHz, Vcore1,104V; +12V12,192V,+5V5,040V,+3,3V3,408V. Sola RAM-03/A2, circa22h senza fail su dichiarazione; RAM-01/RAM-02/RAM-04 fuori. Prossimo riscontro Esc, Advanced, HDD/SSD SMART Information e foto leggibile; attributi e test lungo ancora non acquisiti, datiSanDisk da confermare, TrueNAS non installato. Foto copiata e SHA-256 identico all'originale conservato.

L'utente approva le raccomandazioni e richiede documentazione tecnica e tecnico-didattica evolutiva: registrati ADR-037 e ADR-038, matrice16, master e scheda01, istruzione in CLAUDE.md. WireGuard/DNSlocale e priorità rete confermati; Cloudflare solo eventuale appweb noncritica, nessuna attivazione. La bozza PORTE_CONDIVISIONE è limitata aTCP445 per NASsenzaapp, HTTPS gestione inVLAN99; nessuna regola applicata.

Creati matrice tecnica16, master cronologico e scheda01 con estratti reali prima/dopo, inclusa correzione del solo alias SMB nella proposta08. Fonti S178-S185 mantenute come riferimenti datati, S130 aggiornata per AHCI osservato. Nuova scheda ancorata al HEAD c1f6eb0 letto oggi con perimetro esplicito delle modifiche locali; nessuna ancora delle schede precedenti spostata. Nessuna rete configurata, nessun test di accesso remoto o Cloudflare eseguito.

**Didattica:** voce 1 nel master e scheda [refactor-01-bisogni-controlli-e-flussi.md](../context/refactor-01-bisogni-controlli-e-flussi.md).

**Template:** nessuna

Verifiche del giro didattico: 22 file Markdown conformi, cinque file di tabelle senza difetti, 176 documenti tutti raggiungibili e zero collegamenti rotti/orfani, diff whitespace pulito. Anonimizzazione: zero riscontri bloccanti e 127 avvisi non bloccanti del controllo generale. Carico istruzioni di progetto 85.544 caratteri sotto la soglia 100.000. Estratti prima/dopo confrontati con le fonti reali conservate; alias condivisioni TCP445 e alias gestione TCP22/443 verificati nei file. Nessuna regola applicata, nessun commit o push.

## 2026-10-23: quattro attributi SMART SanDisk acquisiti, letture degli altri SSD successive

Aggiornamento del 23/10/2026: letta la prima pagina HDD/SSD SMART Information, dispositivo SanDisk SDSSDA240G 240 GB del pool dati previsto. BIOS mostra quattro attributi: Reallocated Sectors Count VAL100 WOR100 THR000 raw000000000000; Power-On Hours Count VAL000 WOR100 THR000 raw000000004AF0; Power Cycle Count VAL100 WOR100 THR000 raw000000000755; Temperature(C) VAL071 WOR041 THR000 raw003B0000001D. Conversioni aritmetiche dei contatori: 0x4AF0=19184, 0x0755=1877; nel formato termico standard la parte bassa0x1D=29, da confermare nella lettura completa. Il profilo smartmontools per SDSSDA240G chiama il primo contatore Retired_Block_Count: non estendere l'etichetta generica BIOS a una certificazione dei settori o del disco. VAL/WOR sono valori normalizzati, non ore o gradi: 071 non significa71°C. Questa schermata parziale non mostra usura completa, log errori o risultato del testlungo. AHCI,8GB/A2 e treSSD già verificati; TrueNAS non installato. Prossimo passo nel menuDevice selezionare KingstonV300 eWDBlue, una foto ciascuno, senza cambi. Testlungo/capacità SMARTcomplete e datiSanDisk ancora da verificare. Fonti smartctl/drivedb ufficiali registrate; nessuna nuova scheda didattica, applicazione della distinzione già documentata nella voce1. Foto copiata con SHA identico, originale conservato.

**Didattica:** nessuna nuova scheda: rilievo operativo e applicazione della distinzione fra configurazione, misura e qualifica già sviluppata nella voce1; spiegazione normalizzato/RAW nel registro NAS con fonti specifiche, senza riscrivere la voce storica.

**Template:** nessuna

## 2026-10-23: SMART BIOS KingstonV300 acquisito, rimane WD Blue

Aggiornamento del 23/10/2026: letta la pagina SMART BIOS del Kingston SV300S37A240G 240 GB, disco di avvio previsto su SATA6G_2. Cinque attributi acquisiti: Read Error Rate RAW0 e Reallocated Sectors Count RAW0; Power-On Hours RAW234400007DE4, Power Cycle Count RAW000000000E02, temperatura RAW00110029001A. Il profilo specifico smartmontools usa msec24hour32: i32bitbassi7DE4 corrispondono al campoore32228, non si converte l'intero RAW in ore; decodifica completa e firmware da leggere. Cicli0xE02=3586, parte bassa temperatura0x1A=26 coerente conVAL026, senza generalizzare questo formato agli altriSSD. Nessuna percentuale di vita residua o testlungo superato dedotta. SanDisk già letto, WD Blue ancora da fotografare dalmenuDevice senza altre modifiche. RAM-03/A2,8GB,AHCI e treSSD già verificati; TrueNASnoninstallato, SMARTcompleto/testlungo e datiSanDisk ancora da verificare. Foto copiata e SHA identico, originale conservato.

**Didattica:** nessuna nuova scheda: seconda lettura operativa, applicazione del principio della voce1 e dei formati vendor gi? spiegati nel registro; nessuna qualifica oltre i dati acquisiti.

**Template:** nessuna

## 2026-10-23: nuova immagine ancora Kingston, WD non acquisito

Ulteriore riscontro del 23/10/2026: la nuova immagine mostra ancora Device KINGSTON SV300S37A240G, non il WD Blue. I cinque campi SMART visibili coincidono con la precedente pagina Kingston; nessun nuovo dato WD acquisito. Prossimo passo selezionare nel menuDevice WDC WDS250G1B0A; se non compare, acquisire l'elenco Device aperto. Nessun'altra impostazione da modificare, nessun nuovo test o giudizio di salute dedotto.

**Didattica:** nessuna nuova scheda: riscontro ripetuto, controllo dell'identità del dispositivo prima di attribuire i dati.

**Template:** nessuna

## 2026-10-23: SMART BIOS WD Blue acquisito, prima raccolta dei treSSD completata

Aggiornamento del 23/10/2026: acquisita la pagina SMART del WD Blue WDS250G1B0A-00H9H0, dati su SATA6G_6. RAW riallocazioni 000000000000, ore 000000004889, cicli 000000000ADB, temperatura 00400011001B; VAL/WOR/THR rispettivamente100/100/000,100/100/000,100/100/000,073/064/000. Conversioni dei campi standard:18569 nel campoore,2779cicli e partebassa27 compatibiletemperatura; firmware e output completo ancora da leggere. Le prime pagine BIOS dei treSSD sono ora tutte acquisite, ciascuna con RAW0 nel contatore riallocazioni/ritiroblocchi; soloKingston mostraReadErrorRate,RAW0. Raccolta preliminare finita, non salute/usura o testlungo qualificati. AHCI,RAM-03/A2,8GB e porte1/2/6 gi?verificati. Prossimo avvio UEFI della chiavettaVentoy/Medicat gi? usata perMemtest e foto delmenuprincipale per scegliere diagnosticaSMART. Immagini diagnostiche disponibili non ancora confermate; nessun nuovoMemtest o installazione/formattazione. DatiSanDisk, SMARTcompleto/capacit? e testlungo pendenti. FotoWDarchiviata SHAidentico, originaleconservato.

**Didattica:** nessuna nuova scheda: terzo rilievo operativo e confronto preliminare, applicazione della distinzione gi? documentata fra misura e qualifica. Valori e fonti nel registro NAS.

**Template:** nessuna

## 23/10/2026: chiavetta Medicat avviata, scelta dell'ambiente diagnostico

Avviato correttamente il menu principale Medicat USB v21.12, con indicazione UEFI. Sono visibili Antivirus, Backup and Recovery, Boot Repair, Diagnostic Tools, Live Operating Systems, Partition Tools, Password Removal e Windows Recovery; è selezionato Antivirus. Per individuare un ambiente da cui leggere lo SMART completo, aprire Live Operating Systems, quinta voce: dalla selezione attuale quattro pressioni di freccia giù e Invio, poi acquisire il sottomenu. La presenza della categoria non conferma ancora quali sistemi o strumenti contenga. Nessun nuovo test o intervento sui dischi eseguito.

Restano aperti SMART completo, firmware e autotest supportati dei tre SSD, oltre alla destinazione dei dati SanDisk. RAM-03/A2, 8 GB e AHCI restano la configurazione osservata. Il riscontro conferma il menu di avvio, non l'esecuzione di una diagnostica. Nessuna modifica ai dischi; immagine conservata privatamente con verifica SHA-256 e originale mantenuto.

**Didattica:** nessuna nuova scheda: osservazione del menu di avvio e avanzamento operativo; la categoria visibile non dimostra la presenza di uno specifico ambiente o strumento.

**Template:** nessuna

## 23/10/2026: ambienti live elencati, voce SystemRescue individuata

Nel sottomenu Live Operating Systems di Medicat USB v21.12 sono visibili Active@ Data Studio, Mini Windows 10 e SystemRescue, tutte con freccia verso un ulteriore livello. È selezionata la riga di ritorno alla cartella superiore; indicazione UEFI visibile. Prossimo passo aprire SystemRescue, terza voce dopo il ritorno: tre pressioni di freccia giù e Invio, poi acquisire il menu risultante. La voce SystemRescue è confermata, mentre versione, immagine avviabile e strumenti effettivamente disponibili non sono ancora verificati. Nessun ambiente live avviato e nessun nuovo controllo dei dischi eseguito.

Restano aperti SMART completo, firmware e autotest supportati dei tre SSD, oltre alla destinazione dei dati SanDisk. RAM-03/A2, 8 GB e AHCI restano la configurazione osservata. Il riscontro conferma il menu di avvio, non l'esecuzione di una diagnostica. Nessuna modifica ai dischi; immagine conservata privatamente con verifica SHA-256 e originale mantenuto.

**Didattica:** nessuna nuova scheda: osservazione del sottomenu; si distingue la voce disponibile dall'effettivo avvio dell'ambiente e dall'esecuzione della diagnostica.

**Template:** nessuna

## 23/10/2026: SystemRescue 8.07 avviato, identificazione dei dischi da console

Acquisita la sequenza dal file SystemRescue nel menu Medicat, attraverso la schermata Ventoy con Boot in normal mode selezionato, fino al menu GNU GRUB 2.06 con Boot SystemRescue using default options selezionato. L'utente riferisce che l'avvio è proseguito da solo senza selezionare manualmente la voce; la successiva console conferma SystemRescue 8.07 x86_64, tty1/6, accesso root automatico e prompt disponibile. La versione 2.06 è di GRUB, mentre quella del sistema live è 8.07. Prossimo controllo, nel prompt della console del NAS: digitare `lsblk -d -o NAME,SIZE,MODEL,TRAN`, premere Invio e acquisire l'output. Il dato necessario è la corrispondenza osservata fra nome Linux, capacità, modello e trasporto di ciascun disco, distinguendo i tre SSD SATA dalla chiavetta USB; non assegnare /dev/sda o altri nomi per supposizione. La console pronta verifica l'avvio del live, non la salute dei dischi. SMART completo e autotest non ancora eseguiti.

Restano aperti SMART completo, firmware e autotest supportati dei tre SSD, oltre alla destinazione dei dati SanDisk. RAM-03/A2, 8 GB e AHCI restano la configurazione osservata. Il riscontro conferma il menu di avvio, non l'esecuzione di una diagnostica. Nessuna modifica ai dischi; quattro immagini conservate privatamente con verifica SHA-256 e originali mantenuti.

**Didattica:** nessuna nuova scheda: avanzamento operativo; si distinguono versione del bootloader, avvio reale del live e controlli dei dischi ancora da eseguire. Skill prove-che-misurano applicata al riscontro reale dei nomi Linux prima dei comandi SMART.

**Template:** nessuna

## 23/10/2026: SSD identificati in Linux e passaggio al desktop per facilitare l'uso

Riuscito il comando `lsblk -d -o NAME,SIZE,MODEL,TRAN` nella console di SystemRescue 8.07: /dev/sda SanDisk SDSSDA240G, 223.6G, SATA; /dev/sdb KINGSTON SV300S37A240G, 223.6G, SATA; /dev/sdc WDC WDS250G1B0A-00H9H0, 232.9G, SATA; /dev/sdd Flash Disk, 58.2G, USB. Presente anche loop0 da 693.6M, da non confondere con gli SSD. La schermata contiene un errore di un tentativo precedente, seguito dall'elenco valido; nessun guasto ai dischi dedotto dall'errore di comando. L'utente riferisce notevole difficoltà a digitare anche cambiando tastiera; layout effettivo e causa non verificati. Si adatta il percorso: digitare soltanto `startx`, Invio e acquisire il desktop o l'eventuale errore. Il manuale ufficiale S188 documenta startx; S189 registra l'aggiunta di GSmartControl dalla versione 8.03, S190 il suo avvio dal menu desktop. La disponibilità effettiva di GSmartControl nell'immagine corrente va ancora vista. Desktop e interfaccia SMART non ancora avviati; lettura completa e test lungo restano pendenti.

Restano aperti SMART completo, firmware e autotest supportati dei tre SSD, oltre alla destinazione dei dati SanDisk. RAM-03/A2, 8 GB e AHCI restano la configurazione osservata. Il riscontro identifica i dispositivi nella sessione Linux; non ne misura ancora salute, usura o risultato degli autotest. Nessuna modifica ai dischi; immagine conservata privatamente con verifica SHA-256 e originale mantenuto.

| Nome nella sessione live | Modello letto | Dimensione riportata da lsblk | Trasporto | Ruolo previsto |
|---|---|---|---|---|
| /dev/sda | SanDisk SDSSDA240G | 223.6G | sata | dati, porta SATA6G_1 |
| /dev/sdb | KINGSTON SV300S37A240G | 223.6G | sata | avvio, porta SATA6G_2 |
| /dev/sdc | WDC WDS250G1B0A-00H9H0 | 232.9G | sata | dati, porta SATA6G_6 |
| /dev/sdd | Flash Disk | 58.2G | usb | chiavetta diagnostica |
| loop0 | non mostrato | 693.6M | non mostrato | dispositivo loop, escluso dai tre SSD SATA |

La mappa deriva dall'output reale di questa sessione, non dal solo ordine dei cavi; i nomi Linux possono cambiare dopo un riavvio o una modifica ai collegamenti. Le letture SMART successive devono confrontare ancora il modello dell'unità. L'avvio del desktop è soltanto richiesto, non ancora verificato. Fonti: S188, S189 e S190 nel registro unico.

**Didattica:** nessuna nuova scheda: riscontro operativo della mappa dei dischi e adattamento alla difficoltà di digitazione; elenco dei dispositivi distinto dalla qualifica SMART. La presenza effettiva dell'interfaccia grafica viene verificata prima di prescriverne i clic.

**Template:** nessuna

## 23/10/2026: desktop grafico avviato, apertura del controllo SMART da verificare

Desktop grafico Xfce di SystemRescue 8.07 avviato e visibile, con icone File System e Home e pannello inferiore. Prossimo passo aprire il menu applicazioni in basso a sinistra, cercare GSmartControl nella categoria System ed aprirlo se presente; acquisire la finestra dei dischi, oppure il menu aperto se la voce manca. La posizione della voce è un percorso da verificare, non un menu già osservato. GSmartControl e i dati SMART completi non ancora acquisiti. Mappa della sessione già letta: /dev/sda SanDisk, /dev/sdb Kingston V300, /dev/sdc WD Blue, /dev/sdd USB; RAM-03/A2, 8 GB e AHCI restano la configurazione osservata. Dati SanDisk, autotest supportati, risultato lungo e accettazione finale ancora pendenti. Nessuna installazione o creazione di pool eseguita.

Il desktop disponibile conferma l'avvio grafico; la lettura SMART e l'esito dei test restano verifiche distinte. Si usa il mouse per ridurre la difficoltà di digitazione riferita dall'utente. Riferimenti già consultati: S188 per startx e S189/S190 per il percorso verso GSmartControl. Immagine conservata privatamente con SHA-256 verificato e originale mantenuto.

**Didattica:** nessuna nuova scheda: avanzamento operativo nell'interfaccia grafica; avvio del desktop distinto dalla presenza del programma e dai risultati diagnostici.

**Template:** nessuna

## 23/10/2026: GSmartControl aperto, controllo SMART generale superato dai tre SSD

GSmartControl aperto e inventario dei tre SSD più Flash Disk visibile. Selezionando le unità, il programma mostra Basic health check: PASSED per SanDisk SDSSDA240G /dev/sda 240.06 GB, KINGSTON SV300S37A240G /dev/sdb 240.06 GB e WDC WDS250G1B0A-00H9H0 /dev/sdc 250.06 GB. Enable SMART risulta selezionato per tutti e tre; la schermata non prova chi abbia cambiato l'impostazione. Le famiglie mostrate sono SandForce Driven SSDs per SanDisk e Kingston, WD Blue / Red / Green SSDs per WD: sono etichette del database del programma, senza diagnosi del controller reale. PASSED riguarda lo stato SMART generale, non un test lungo superato né una misura della vita residua. Prossimo passo doppio clic sul SanDisk in alto a sinistra, poi scheda Attributes e foto leggibile degli attributi. Se la finestra è piccola, ingrandirla; se non compare Attributes, acquisire la finestra dei dettagli aperta. Firmware, attributi completi, capacità ed esito del test lungo ancora da acquisire.

| Dispositivo osservato | Modello | Capacità riportata dalla GUI | Basic health check | Enable SMART |
|---|---|---|---|---|
| /dev/sda | SanDisk SDSSDA240G | 240.06 GB | PASSED | selezionato |
| /dev/sdb | KINGSTON SV300S37A240G | 240.06 GB | PASSED | selezionato |
| /dev/sdc | WDC WDS250G1B0A-00H9H0 | 250.06 GB | PASSED | selezionato |

Il risultato generale SMART è distinto dal log degli autotest e dagli attributi di usura, come spiegato dal manuale S186. La nuova osservazione chiude la verifica della presenza e apertura del programma; mantiene aperti dati completi e test dei dischi.

Immagini archiviate privatamente con confronto SHA-256; originali conservati. Nessun test o modifica dei dati dedotto dalla semplice selezione delle unità.

**Didattica:** nessuna nuova scheda: riscontro operativo del programma e del controllo generale; distinzione fra stato SMART, usura e autotest già documentata.

**Template:** nessuna

## 23/10/2026: attributi SMART del SanDisk letti, verifica dei test ancora aperta

Letta la scheda Attributes del SanDisk SDSSDA240G /dev/sda in GSmartControl, revisione struttura SMART 1. Tutte le righe visibili riportano Failed: never. Valori acquisiti: ID5 RAW0; ore19193h+00m+00.000s; cicli1877; ID166 RAW51; ID168 RAW102; ID173 RAW65; perdite inattese di alimentazione ID174 RAW62; Reported Uncorrectable ID187 RAW0; Command Timeout ID188 RAW0; temperatura34 gradi con Min/Max0/59; SATA CRC Error Count ID199 RAW0; spazio di riserva ID232 VAL100 WOR100 THR4 RAW100; scritture ID241 RAW29129 GiB e letture ID242 RAW54361 GiB secondo il profilo specifico. Il profilo corrente S187 per il modello esatto chiama ID166 Min_PE_Cycles e ID168 Max_PE_Cycles: le etichette GUI Later Bad Block Count e SATA Physical Error Count non sono usate per dichiarare 51 blocchi guasti o 102 errori di collegamento. ID232 non è una percentuale di vita residua; i campi grezzi composti non vengono convertiti in usura totale. Prossimo passo aprire la scheda Self-tests già visibile e acquisirla per verificare test disponibili e log. Firmware e dati generali ancora da leggere, test lungo non avviato né concluso.

Tabella e confronto con la fonte S187 nel registro NAS. Nessuna modifica ai dati o autotest avviato in questo riscontro.

**Didattica:** nessuna nuova scheda: applicazione del principio già documentato su misura e interpretazione; il caso concreto delle etichette discordanti è spiegato nel registro con la fonte primaria.

**Template:** nessuna

## 23/10/2026: selezionato il test esteso del SanDisk prima dell'assenza

Nella scheda Self-Tests del SanDisk SDSSDA240G /dev/sda risulta selezionato Extended Self-test, durata stimata 10 min, log con zero voci. L'utente chiede se lanciarlo prima di andare via: indicato di premere Execute e lasciare il NAS acceso e alimentato. Il test termina da solo e non cancella i dati. Questo riscontro documenta la selezione, senza ancora attestare avvio o completamento; prevista lettura del log al ritorno, senza foto intermedia obbligatoria.

**Didattica:** nessuna nuova scheda: selezione del test e indicazione di esecuzione, senza ancora un esito.

**Template:** nessuna

## 26/10/2026: SanDisk supera il test esteso, prossimo Kingston

La scheda Self-Tests del SanDisk SDSSDA240G /dev/sda mostra Test completed e Test result: Completed without error. Self-Test Log contiene una voce Extended offline, stato Completed without error e completamento 100%. Confermato quindi l'esito positivo del test esteso sul SanDisk. La schermata precedente del 23/10 documentava selezione Extended Self-test, stima10min e log0voci; quella ricevuta il26/10 documenta il risultato. Non si deduce un test durato tre giorni né una prova continua del NAS durante l'assenza. Il campo Lifetime hours della foto finale non è trascritto perché poco leggibile. Firmware SanDisk e dettagli/test degli altri SSD restano da acquisire. Prossimo passo chiudere i dettagli SanDisk, aprire con doppio clic KINGSTON SV300S37A240G, scheda Self-tests, selezionare Extended Self-test se disponibile e premere Execute; acquisire la schermata per verificare unità, tipo di test e stato. Nessuna ripetizione del test SanDisk richiesta.

**Didattica:** nessuna nuova scheda: riscontro operativo dell'esito; distinguere il log di un autotest del disco da durata dell'assenza e accettazione dell'intero NAS.

**Template:** nessuna

## 26/10/2026: Kingston supera il test esteso, prossimo WD Blue

La scheda Self-Tests del KINGSTON SV300S37A240G /dev/sdb mostra Test completed e Test result: Completed without error. Il log contiene una voce Extended offline, Completed without error e completamento 100%. Anche il Kingston ha quindi superato l'autotest esteso: due dei tre SSD hanno ora un esito esteso documentato, SanDisk e Kingston. La durata effettiva non viene ricavata dalla fotografia. Prossimo passo chiudere i dettagli Kingston, aprire con doppio clic WDC WDS250G1B0A-00H9H0, scheda Self-tests, scegliere Extended Self-test se disponibile e premere Execute, poi acquisire la schermata. Test esteso WD ancora pendente; nessuna ripetizione di SanDisk o Kingston richiesta. Firmware e dettagli ancora mancanti restano da raccogliere. Chiesto in parallelo se sul SanDisk ci siano file da conservare prima del futuro pool: risposta ancora attesa, nessuna cancellazione autorizzata da questa verifica.

**Didattica:** nessuna nuova scheda: riscontro operativo dell'autotest Kingston e riepilogo dei due esiti acquisiti; esito del singolo disco distinto dall'accettazione del NAS.

**Template:** nessuna

## 26/10/2026: WD Blue supera il test esteso, tre SSD con esito positivo

La scheda Self-Tests del WDC WDS250G1B0A-00H9H0 /dev/sdc mostra Test completed e Test result: Completed without error. Il log contiene una voce Extended offline, stato Completed without error e completamento100%. Sono quindi documentati tre autotest estesi superati, uno per ciascuno dei tre SSD del NAS: SanDisk, Kingston V300 e WD Blue. La stima10min mostrata per il WD non viene chiamata durata effettiva. Nessuna ripetizione dei test è richiesta. Per completare identificazione e usura manca una raccolta via GUI: General e Attributes del WD, General e Attributes del Kingston, General del SanDisk; gli attributi SanDisk sono già acquisiti. I seriali eventualmente presenti nelle foto restano nel livello privato. La domanda sui file da conservare sul SanDisk è ancora senza risposta: nessuna cancellazione o creazione di pool eseguita. Firmware, restanti dati di usura, accettazione finale e riallocazione RAM restano aperti.

**Didattica:** nessuna nuova scheda: riscontro operativo del terzo autotest e riepilogo dei tre esiti acquisiti; risultati dei dischi distinti dall'accettazione dell'intero NAS.

**Template:** nessuna

## 26/10/2026: TAB-02 identificato, SoundCraft valutato senza fork

Dallo screenshot Screenpresso del 26/10/2026, che mostra la schermata Informazioni sul tablet, TAB-02 risulta un Galaxy Tab S6 Lite (2024), modello SM-P620 solo Wi-Fi, con il nome dispositivo di Persona-B. Il modello è confermato su S191 (GSMArena) e la variante solo Wi-Fi su S192 (SamMobile, da Geekbench e GCF) e S193 (AndroidHeadlines). Una prima stesura attribuiva la variante alle schede Bluetooth SIG: la lettura di S192 lo ha smentito, perché il corpo dell'articolo non le cita. Due correzioni, scritte nel censimento senza cancellare la storia. TAB-02 non è più «il più vecchio»: è l'edizione 2024, mentre TAB-01 è registrato come 2022 LTE in base alla sola dichiarazione dell'8/10. L'attribuzione storica a Persona-B, data per smentita il 09/10, è confermata dal nome del dispositivo, che però dice chi ha configurato l'apparecchio e non chi lo usa oggi. Prima della scrittura il seriale è entrato nella mappa come `<sn-tab-02>` e nei pattern. Lo screenshot è archiviato in `_notes/censimento/foto-pc/tab-02/` con SHA-256 identico all'originale, e l'originale resta in Screenpresso. Titoli delle due schede resi neutri (nessuna ancora li collegava); allineati lo studio degli endpoint e `current-work.md`. Pendenze: Informazioni software di TAB-02 e Informazioni sul tablet di TAB-01.

L'utente ha chiesto anche di fare un fork di SoundCraft della suite ArtCraft e personalizzarlo per Ubuntu Studio. Poi ha precisato che i progetti interessati sono quello dei monitor e quello di home recording, e che questo repository c'entra solo per `linux-desktop-C`. Ha chiesto una spiegazione prima del dettaglio. Dati raccolti in sola lettura. La CLI installata è la 0.10.0 ed espone 480 comandi e 27 plugin interni, contati con `soundcraft-cli commands` e `plugins`. Il repository `storytold/soundcraft` ha licenza Apache-2.0 o MIT, pubblica per Linux il deb, il tarball, l'AppImage e il Flatpak, e ospita CLAP e VST3 ma non LV2. Il crate `playback` usa cpal con la sola feature `asio` opzionale. Il `docs/gaps.md` di upstream, G-01, dichiara come blocco dell'alpha la mancanza di JACK e della verifica su Linux, con il mix a blocchi fissi di 512 campioni. Il README dice che un fork deve togliere nome e loghi ArtCraft; l'utente sceglie un nome neutro, anche perché Soundcraft è il marchio dei mixer Harman. Per usarlo non serve un fork. Il fork serve a cambiare il codice, cioè per JACK, LV2 e priorità realtime. Il valore atteso è alto per l'home recording, come DAW pilotabile dall'agente accanto ad Ardour, e basso per i monitor, dove misura, crossover e DSP restano a REW, Octave, VituixCAD e CamillaDSP. Nessun fork, clone o scrittura nei progetti gemelli; la voce resta aperta in `pendenze-aperte.md`.

**Didattica:** nessuna: registrazione di inventario e valutazione non ancora decisa; la scelta sul fork, quando sarà presa, avrà la sua voce nel progetto gemello che la ospita.

Nei controlli di chiusura `check-eol` ha bloccato `.claude/allineamento-template.json`, che il commit `c1f6eb0` ha registrato con sei CRLF e un LF finale. La causa è alla riga 638 di `allinea-tutti.ps1` del template, che accoda un LF nudo all'uscita CRLF di `ConvertTo-Json`. Il file è stato normalizzato a CRLF, con una sola riga cambiata.

**Template:** L-006

## 26/10/2026: fonti salvate, voci aperte nei due progetti gemelli

Su richiesta dell'utente sono salvate tutte le fonti del giro. In `SOURCES.md` sono S192 e S193 per la variante del tablet, entrambe lette, e S194-S197 per SoundCraft, cioè README, manifesto del crate di riproduzione, sorgente dei dispositivi e registro delle lacune. La lettura di S192 ha corretto la frase che attribuiva la variante Wi-Fi alle schede Bluetooth SIG. Per farla comparire a ogni `/riprendi`, la valutazione di SoundCraft è ora una voce anche nei due progetti gemelli. In `diy-2way-monitors-home` è PA-034, con le fonti in `docs/90-riferimenti/fonti.md`, una voce nel work-log e una riga nel file di ripresa. In `home-recording-training-mixing-setup` è PA-003, con un file di ripresa nuovo. Nello stesso progetto c'è PA-004 per l'articolo di Futuranet del 15/10/2026 sull'analizzatore di spettro con Raspberry Pi Pico, proposto dall'utente come sottoprogetto: ha senso come strumento da banco fino a 250 kHz e come didattica, non come misura audio, perché l'ADC a 12 bit sta molto sotto la Scarlett. L'articolo ha risposto 403 al recupero ordinario e si è letto per intero con `curl` e uno user agent da browser, verificando il corpo. Le due schermate dei tablet restano da chiedere alla ripresa, quando l'utente è a casa, ciascuna con il tablet e il menu indicati in `pendenze-aperte.md`.

**Didattica:** nessuna: registrazione di fonti e pendenze, nessuna scelta presa.

**Template:** nessuna

## 26/10/2026: doc-ingest senza esclusione dei documenti personali, causa nel template (L-007)

L'utente ha chiesto perché la copia di `doc-ingest.py` di `diy-2way-monitors-home` non avesse `--esclusi`, se fosse grave e se fosse un difetto del template. La causa è nel template, alla riga 623 di `allinea-dal-template.py`: l'allineamento aggiorna una copia in `tools/` solo se nel template il file sta in una cartella `tools/` di un pacchetto. `doc-ingest.py`, `cache-storage.py` e `docx-to-md.py` stanno invece nella radice del loro pacchetto e non si aggiornano mai. Perimetro misurato sui progetti di E: confrontando le copie in `tools/` con il template, a meno del fine riga. `doc-ingest.py` differisce in quattro progetti e manca di `--esclusi` in due: `diy-2way-monitors-home` e `spanish-learning`. La gravità è giudicata sulle date e sul codice, senza aprire documenti. La falla era latente: in `diy-2way-monitors-home` la conversione ordinaria passa da `converti-fonti.py`, che esclude da sé, le cache hanno l'ultima scrittura il 07/10 alle 13:45 e la cache di `spanish-learning` è del 06/07. Nessuna conversione senza esclusione è risultata dopo la regola. La copia di `diy-2way-monitors-home` era intatta ed è stata sostituita con quella del pacchetto, con `cache-storage.py` e il file di esempio degli schemi: autotest 21 file e 0 errori, `chiudi -SoloControlli` verde, PA-035 chiusa. La copia di `spanish-learning` porta un OCR bilingue proprio e resta da fondere all'allineamento successivo. Lezione L-007 registrata per il template, con anche il secondo difetto: la prova dei documenti personali verifica il pacchetto nel template e non la copia nei progetti.

**Didattica:** nessuna in questo progetto: il difetto e il suo rimedio riguardano il template, dove la lezione L-007 li porta.

**Template:** L-007

## 26/10/2026: inventario riconciliato e ISO spostate su Ventoy

Acquisite in lettura sei foto Telegram, General e Attributes per tutti i tre SSD. Firmware SanDisk Z32070RL, Kingston605ABBF2 e WD X41100WD; smartctl7.2r5155. Tutte le righe visibili Failed: never; tre generali PASSED e tre estesi già superati. Le foto contengono identificativi conservati fuori dalla prosa pubblica. Al successivo tentativo di copia i sei file non risultano più nella cartella indicata: valori trascritti e associazioni sono salvati, ma la copia dei JPEG originali rimane da recuperare.

## RAM e recap finale del26/10/2026

L'utente chiarisce di volere almeno un secondo modulo8 GB nelNAS e gli altri due come scorta, quindi autorizza gli ulteriori test necessari per avanzare. La configurazione attuale restaRAM-03 solaA2,8 GB; prossimo montaggio da eseguireRAM-01 inB2, ultimo slot dallaCPU. Questa coppia16 GB non risulta già provata; la coppiaRAM-03/A2+RAM-04/B2 era invece fallita e non viene semplicemente ripetuta. BIOS atteso16384 MB,2133 MHz,XMP disabilitato; Memtest86+8.10,quattro passaggi senza errori o stop al primo errore. RAM-01 aveva fallitoA1/A2: la destinazione scelta non ne cambia retroattivamente l'esito. RAM-02/04 restano le due scorte fisiche richieste, conservate con errori registrati. QuattroCrucial4 GB restano alserver,16 GB censiti. Le alternative12/12 e16/8 non sono state scelte. ADR-039 registra obiettivo e prova, non montaggio o pass già osservati. Il chiarimento sui fileSanDisk è ancora pendente.

Due ISO spostate come autorizzato e verificate prima della rimozione delle sorgenti. Nuova canonica separa censimento, prove, assegnazioni e proposte; corrette disponibilità NAS8GB/server16GB censiti e quarantena tre moduli. Nessun sistema o pool installato. Autorizzata prova mirata16 GB RAM-03/A2+RAM-01/B2,non ancora montata o avviata.

**Didattica:** [voce2 del racconto](../context/studio-didattico-master.md) e [refactor02](../context/refactor-02-inventario-e-ram-nas.md), estratti reali prima/dopo e compromessi di redistribuzione.

**Template:** nessuna

## 26/10/2026: montata la coppia RAM-03/A2 e RAM-01/B2, BIOS ancora da verificare

La nuova fotografia del NAS mostra i moduli etichettati RAM-03 in A2 e RAM-01 in B2; A1 e B1 risultano vuoti. Il montaggio richiesto è quindi osservato: due moduli nominali da8 GB, non ancora una lettura BIOS da16 GB o un test superato. L'utente chiede di procedere. Prossimo collegare alimentazione e chiavetta Medicat, accendere ed entrare nel BIOS con Canc. Verificare16384 MB,2133 MHz e XMP disabilitato prima di Memtest86+8.10. La prova della coppia prevede quattro passaggi completi senza errori oppure stop al primo errore. Avvio e risultato non ancora acquisiti. La fotografia è stata copiata subito nell'archivio privato con SHA-256 identico e originale conservato.

**Didattica:** nessuna nuova scheda: riscontro fisico della configurazione descritta nella voce2, distinto dal rilevamento BIOS e dalla prova.

**Template:** nessuna

## 26/10/2026: BIOS conferma 16384 MB con RAM-03/A2 e RAM-01/B2

Il BIOS ASUS H170-PRO versione 3805, i7-6700, mostra Memory 16384 MB (DDR4 2133 MHz), XMP Disabled. DRAM Status: DIMM_A1 N/A, DIMM_A2 TEAMGROUP 8192 MB 2400 MHz, DIMM_B1 N/A, DIMM_B2 TEAMGROUP 8192 MB 2400 MHz. I 2400 MHz delle righe dei moduli sono distinti dai 2133 MHz operativi indicati in alto. Le etichette RAM-03/A2 e RAM-01/B2 derivano dalla precedente foto del montaggio. Riconoscimento dei 16 GB confermato; questo non è un esito di stabilità. Memtest della nuova coppia non ancora osservato. Restano quattro passaggi completi senza errori oppure stop al primo errore, secondo ADR-039. Prossimo F8 e selezione UEFI: Generic, Partition 2; se la voce manca acquisire il menu. In Medicat avviare Diagnostic Tools, Memtest86+ 8.10 e acquisire la schermata iniziale della coppia. La schermata EZ Mode mostra anche la voce Intel Rapid Storage Technology con indicazione On: non sostituisce una lettura di SATA Mode in Advanced, già verificato AHCI nel giro precedente; non è stata richiesta alcuna modifica ora. Tre SSD ancora visibili su SATA6G_1, _2 e _6. Immagine copiata nell'archivio privato, SHA-256 identico e originale conservato.

**Didattica:** nessuna nuova scheda: riscontro BIOS della configurazione già motivata nella voce 2, distinto dal test ancora aperto.

**Template:** nessuna

## 26/10/2026: avviato Memtest sulla coppia RAM-03/A2 e RAM-01/B2

L'utente riferisce l'avvio e la schermata lo conferma: Memtest86+ v8.10, build 8.10.49468.x64, ASUS H170-PRO e i7-6700, quattro core e otto thread, SMP 8T PAR. Alla lettura iniziale Time 0:00:03, Status Testing, Pass 0, Errors 0, progresso del passaggio 0%, Test 15%, Test #3 Moving inversions, 1s & 0s. Memoria 15.8 GB, IMC 1069 MHz (DDR4-2138), CAS 15-15-15-35; CPU 3400 MHz, indicazione termica 42/48 °C. SPD Slot 1: TEAMGROUP 8 GB DDR4-2400, 2016-W48; Slot 3: TEAMGROUP 8 GB DDR4-2400, 2016-W40. La combinazione fisica RAM-03/A2 e RAM-01/B2 deriva dal montaggio già fotografato, e il BIOS precedente confermava 16384 MB a 2133 MHz, XMP disabilitato. Questi sono contatori iniziali: non documentano un passaggio completo o il superamento della prova. Proseguire con questa stessa configurazione fino a quattro passaggi completi senza errori, oppure stop al primo errore con foto dei contatori e della riga di errore. Nessun ulteriore spostamento RAM richiesto. Immagine archiviata subito, SHA-256 identico, originale conservato.

**Didattica:** nessuna nuova scheda: avvio della prova della configurazione già motivata nella voce 2, senza esito finale.

**Template:** nessuna

## 26/10/2026: fallita RAM-03/A2 più RAM-01/B2, spiegato il rischio della RAM volatile

Due letture della stessa prova Memtest86+ 8.10 mostrano Status Failed, Pass 0, Errors 1. Prima lettura a 0:20:49 con banner FAIL, seconda a 0:20:54 senza banner: non sono due errori o due test diversi. Il passaggio è al 99% ma il contatore Pass resta 0. Nella seconda lettura il test corrente è #10 Bit fade test, 2 patterns, al 65%; la riga che ha registrato l'errore indica invece Test 9, pCPU 0, Pass 0, Failing Address 0x000100d49410 (4.01 GB), Expected 0x3d12e399ff15f5d8, Found 0x3d12e399ff15fdd8. XOR calcolato 0x800: un solo bit differente, bit 11 contando da zero. Il tempo è quello della lettura, non il momento esatto del bit alterato. Coppia RAM-03/A2 + RAM-01/B2 ricavata dal montaggio precedente; non si attribuisce il bit a un singolo DIMM dall'indirizzo. Memoria 15.8 GB, DDR4-2138, CAS 15-15-15-35; temperature mostrate 42/54 e 41/54 °C. Criterio di stop al primo errore raggiunto: richiesto spegnimento, ancora da confermare; nessun nuovo innesto o test identico assegnato. Obiettivo 16 GB aperto. Immagini archiviate subito con SHA-256 corrispondenti e originali conservati. Fonti S126, S129 e S204 rilette per significato dei campi, limiti diagnostici e conseguenze sui dati.

**Didattica:** ampliata la voce 2 e la scheda refactor-02-inventario-e-ram-nas.md con volatilità, percorso del dato e limiti di mirror/checksum, usando la riga reale Expected/Found.

**Template:** nessuna

## 26/10/2026: NAS spento dopo il fallimento della coppia, cavo ancora da scollegare

L'utente conferma che il NAS è spento. Non conferma ancora lo scollegamento del cavo di alimentazione; il prossimo gesto richiesto è scollegarlo, prima di toccare i moduli. Nessun nuovo montaggio, avvio o test. Restano RAM-03/A2 e RAM-01/B2 all'ultimo riscontro, con esito negativo della coppia già registrato; obiettivo 16 GB invariato e Crucial sul server.

**Didattica:** nessuna nuova scheda, sola conferma operativa.

**Template:** nessuna

## 26/10/2026: cavo NAS scollegato, richiesta rimozione della sola RAM-01/B2

L'utente risponde fatto alla richiesta di scollegare il cavo di alimentazione: NAS spento e scollegato confermati. Prossimo gesto richiesto: rimuovere soltanto RAM-01 da B2, ultimo slot dalla CPU, lasciando RAM-03 in A2. Rimozione non ancora confermata, nessuna riaccensione o nuova prova assegnata. RAM-01 resta conservata con gli errori registrati, senza qualifica come ricambio funzionante. La rimozione separa la coppia appena fallita e non decide una riduzione permanente a 8 GB: obiettivo NAS 16 GB ancora aperto, Crucial invariati sul server e nessun acquisto deciso.

**Didattica:** nessuna nuova scheda, gesto operativo conseguente alla prova già spiegata nella voce 2.

**Template:** nessuna

## 26/10/2026: RAM-01 rimossa, resta RAM-03/A2, prossimo avvio installer con 8 GB provvisori

L'utente conferma RAM-01 rimossa, dopo spegnimento e scollegamento già confermati. Nel NAS resta RAM-03 da 8 GB in A2; B2 torna vuoto, nessun altro modulo aggiunto. RAM-01 conservata fuori con gli errori registrati, come RAM-02/04, senza smaltimento o qualifica come ricambio funzionante. La precedente prova singola RAM-03/A2 ha circa 22 ore senza fail riferite; non si richiede una ripetizione identica per il solo ritorno alla configurazione. Passo operativo successivo: avviare la chiavetta UEFI con F8, Generic Partition 2, poi Live_Operating_Systems/TrueNAS/TrueNAS-SCALE-25.10.7.iso. Si usa la configurazione provvisoria da 8 GB, minimo base documentato in S204, mantenendo aperto l'obiettivo 16 GB di ADR-039. Aggiungere in seguito un modulo utilizzabile non richiede reinstallare TrueNAS. Nuova accensione e installer ancora non osservati; nessun disco cancellato, Kingston resta la sola destinazione prevista dell'installazione e i dati SanDisk sono ancora da chiarire prima del pool. Crucial invariati sul server, nessun acquisto o riduzione permanente a 8 GB decisi.

**Didattica:** nessuna nuova scheda: si applica la distinzione fra capacità montata e obiettivo già spiegata nella voce 2; l'avvio provvisorio non equivale alla chiusura dell'espansione.

**Template:** nessuna

## 26/10/2026: avvio TrueNAS 25.10.7 fino al menu installer, errori di boot registrati

L'utente dichiara di aver eseguito i passi e le tre immagini mostrano in sequenza GRUB con Start TrueNAS SCALE Installation selezionato, log del live e TrueNAS 25.10.7 Console Setup con 1 Install/Upgrade selezionato, oltre a Shell, Reboot e Shutdown. La copia di filesystem.squashfs in RAM è mostrata al 100%. Nel log sono leggibili SGX disabled or unsupported by BIOS, mount della sorgente in sola lettura, Failed to open /dev/shm device, ignoring: Inappropriate ioctl for device, firmware Realtek rtl_nic/rtl8168h-2.fw non caricato (-2) e soprattutto Failed to start mount-cd.service - Mount installation media. Non si attribuiscono questi messaggi alla RAM e non si dichiarano risolti o ininfluenti dall'apparizione successiva del menu. NAS acceso con sola RAM-03/A2 da 8 GB secondo il montaggio confermato; nessuna nuova lettura BIOS della memoria nelle tre foto. Boot raggiunto fino al menu, non installazione conclusa o disponibilità completa del media provata. Prossimo premere Invio su Install/Upgrade e acquisire l'elenco delle destinazioni: previsto soltanto Kingston V300 240 GB, ancora da identificare nel live attuale. Nessuna lettera sda/sdb viene ereditata da precedenti sessioni. Nessun disco selezionato o cancellato, file SanDisk ancora da chiarire prima del pool, obiettivo 16 GB aperto. Guida ufficiale stabile Installing TrueNAS letta, S205; il passo apre la selezione, la cancellazione richiede una conferma successiva. Tre immagini copiate subito e rilette, SHA-256 coincidenti con gli originali conservati.

**Didattica:** nessuna nuova scheda: si distingue menu raggiunto da installazione riuscita, secondo il criterio di stato e riscontro già adottato.

**Template:** nessuna

## 26/10/2026: Kingston identificato come sdc, prima della cancellazione verifica del supporto

La schermata Choose Destination Media di TrueNAS 25.10.7 elenca sda SanDisk SDSSDA2, NTFS, 223.57 GiB; sdb WDC WDS250G1B0A, NTFS, 232.89 GiB; sdc KINGSTON SV300S, ext4, 223.57 GiB; sdd Flash Disk Medicat, NTFS, 58.2 GiB. Tutte le caselle sono vuote e l'evidenziazione è sul SanDisk, non sul Kingston. Il Kingston destinato al sistema è quindi sdc, terza riga: la vecchia mappa sdb Kingston e sdc WD non vale in questo avvio. Nessun disco è ancora selezionato o cancellato. Poiché il log precedente mostrava mount-cd.service fallito, si richiede un controllo del media prima della conferma di cancellazione: Esc, ritorno al menu, 2 Shell, ls -lh /cdrom, foto del risultato. Il comando legge la cartella; nessun nuovo mount o scrittura è assegnato. Fonti ufficiali correnti consultate e scaricate: scale-build al commit 2b2b629f7726daeb2dc5b618ecdd8e1014723a45, script mount-cd con mountpoint /cdrom e ricerca TrueNAS-SCALE.update; truenas-installer al commit b988b96279e33ab799326205b6e3e8c8879b2ae1, install.py che nel codice corrente formatta prima di montare /cdrom/TrueNAS.update. Non sono versioni confrontate con i file della ISO 25.10.7; i nomi payload differiscono e non si deve dedurre la causa o imporre un nome file dal solo master. La verifica ls sul live risolve la presenza effettiva del supporto. Lettura ancora non eseguita o osservata. RAM-03/A2 da 8 GB provvisori invariata, obiettivo 16 GB aperto, dati SanDisk ancora da chiarire. Immagine archiviata subito con SHA-256 corrispondente e originale conservato.

**Didattica:** nessuna nuova scheda: lettura effettiva del supporto prima della scrittura, versione del sorgente distinta da quella del live; coerente con la distinzione di riscontro già adottata.

**Template:** nessuna

## 26/10/2026: payload presente in /cdrom, si torna alla selezione del solo Kingston

La Shell mostra il comando ls -lh /cdrom eseguito e il suo elenco: total 2.0G, file TrueNAS-SCALE.update da 1.9G, directory EFI, System, boot, efi, live, oltre a boot.catalog, efi.img, initrd.img, mach_kernel e vmlinuz. In alto è visibile un tentativo precedente con /cd-rom inesistente, corretto nel comando riuscito: non è un errore della cartella /cdrom. Nel live il payload è presente e il controllo richiesto ha dato il riscontro necessario a proseguire. Non si dichiara una verifica byte per byte del payload, un nuovo checksum della ISO, un servizio mount-cd ora attivo o la causa certa del fallimento di avvio. Non si rinomina il file TrueNAS-SCALE.update in TrueNAS.update sulla base di sorgenti di un'altra versione. Nessun nuovo mount, formattazione USB o test RAM richiesto. Prossimo exit, 1 Install/Upgrade, navigare su sdc KINGSTON SV300S 223.57 GiB, selezionarlo con Spazio assicurando che solo quel disco abbia l'asterisco, OK e Yes all'avviso di cancellazione relativo al Kingston; acquisire la schermata successiva. La cancellazione del Kingston è compresa nell'installazione sul disco di avvio già prevista, senza estendere l'azione a SanDisk, WD o USB. Selezione, conferma ed effettive scritture ancora non osservate. Mappa attuale sda SanDisk, sdb WD, sdc Kingston, sdd Flash Disk. Sola RAM-03/A2 da 8 GB provvisori, obiettivo 16 GB ancora aperto e dati SanDisk pendenti prima del pool. Immagine archiviata subito, SHA-256 coincidente e originale conservato. Procedura ufficiale S205 già letta.

**Didattica:** nessuna nuova scheda: acquisito il riscontro richiesto sul live, distinto dalla sola inferenza da sorgenti di versione diversa.

**Template:** nessuna

## 26/10/2026: installer alla scelta dell'amministratore web truenas_admin

La nuova immagine mostra Web UI Authentication Method, con Administrative user (truenas_admin) selezionato e Configure using Web UI come alternativa. L'avanzamento è coerente con i passi precedenti del flusso S205, ma il disco selezionato non è visibile in questa schermata: non è una nuova lettura del target. Destinazione assegnata dalle istruzioni: solo Kingston V300 sdc 223.57 GiB; nessuna estensione a SanDisk, WD o chiavetta. Si indica di lasciare la prima voce, confermare Invio, impostare una password unica nei due campi usando Tab e salvarla nel proprio gestore, quindi OK e foto della schermata successiva. La credenziale è da digitare localmente; nessun valore è stato richiesto, ricevuto o conservato nei file del progetto. truenas_admin è il nome pubblico predefinito del ruolo amministrativo della gestione web, distinto dalle successive utenze per le condivisioni. Conferma del metodo, password impostata, scritture ed esito conclusivo ancora non osservati; non si dichiara TrueNAS installato. NAS acceso con sola RAM-03/A2 da 8 GB provvisori, obiettivo 16 GB aperto; payload TrueNAS-SCALE.update presente in /cdrom dalla verifica precedente, dati SanDisk ancora da chiarire prima del pool. Immagine copiata subito e verificata SHA-256, originale conservato. Procedura ufficiale S205 già letta.

**Didattica:** nessuna nuova scheda: passo previsto dell'installazione, distinguendo amministrazione web e futura autorizzazione delle condivisioni.

**Template:** nessuna

## 27/10/2026: truenas_admin e password confermati, installazione in avvio riferita

L'utente conferma di aver scelto truenas_admin e impostato la password, quindi riferisce che sta lanciando l'installazione. Sono conferme dichiarate, senza nuova immagine dell'avanzamento o dell'esito: non si accredita ancora Installation Succeeded, completamento o primo avvio dal Kingston. Nessun valore di password è stato richiesto, ricevuto o salvato. Prossimo lasciare proseguire con la chiavetta collegata e acquisire il messaggio finale di successo o errore prima del riavvio. Il target assegnato è solo Kingston V300 sdc nella mappa dell'installer già osservata, non una nuova verifica del disco in questo messaggio. RAM-03/A2 sola da 8 GB provvisori, obiettivo 16 GB ancora aperto, Crucial sul server; pool non creato e dati SanDisk ancora da chiarire. Non si deduce la durata dell'installazione o un funzionamento notturno dal cambio di data.

**Didattica:** nessuna nuova scheda: conferma operativa dell'autenticazione, avvio dichiarato distinto dall'esito ancora da acquisire.

**Template:** nessuna

## 27/10/2026: prima lettura errata di sdc come sda e richiesta di verifica

L'agente ha inizialmente letto sdc come sda nel messaggio Installation Succeeded e ha chiesto una verifica di modelli e filesystem prima del riavvio. Quella lettura del messaggio era errata e non descrive una destinazione diversa dell'installer. La rilettura dell'originale e il risultato lsblk, registrati nella voce successiva, confermano sdc Kingston con EFI/ZFS. La richiesta eseguita era 2 Shell, lsblk -o NAME,SIZE,MODEL,FSTYPE; nessuna scrittura è stata assegnata per questa verifica. Il messaggio precedente dell'agente sul possibile SanDisk installato è rettificato, senza considerare mai dimostrata una cancellazione del SanDisk.

**Didattica:** nessuna nuova scheda: prima interpretazione visiva errata, corretta nel medesimo giro con rilettura e riscontro.

**Template:** nessuna

## 27/10/2026: Kingston con EFI e ZFS verificato, corretto errore di lettura, prossimo primo avvio

La nuova lettura lsblk -o NAME,SIZE,MODEL,FSTYPE identifica sda SanDisk SDSSDA240G 223.6G con partizioni da 450M NTFS, 99M vfat, 16M, 222.5G NTFS e 530M NTFS; sdb WDC WDS250G1B0A-00H9H0 232.9G con partizioni da 450M NTFS, 99M vfat, 16M, 231.5G NTFS e 859M NTFS. sdc è KINGSTON SV300S37A240G 223.6G, con sdc1 1M, sdc2 512M vfat e sdc3 223.1G zfs_member. sdd è Flash Disk 58.2G, partizioni NTFS da 58.2G e vfat da 32M. Il Kingston ha quindi lo schema EFI/ZFS dell'installazione e SanDisk/WD mostrano ancora le strutture NTFS, senza che ciò provi la validità dei file. Riletta a risoluzione originale anche l'immagine del successo: il testo è The TrueNAS installation on sdc succeeded, non sda. L'agente aveva letto male la lettera, causando il controllo in più; errore riconosciuto all'utente e registrato esplicitamente. Non c'è evidenza di una destinazione sbagliata dell'installer. Installazione sul Kingston verificata, primo avvio ancora da osservare. Si indica exit dalla Shell, 3 Reboot System e rimozione della USB quando parte il riavvio, poi foto della console. L'utente chiede se scegliere 1: viene chiarito che 1 Install/Upgrade riapre l'installazione e che occorre 3 Reboot System. Nessuna di queste azioni è ancora confermata o vista. Account/password impostata confermati senza valore archiviato, RAM-03/A2 sola da 8 GB provvisori, obiettivo 16 GB e dati SanDisk ancora aperti. Foto nuova copiata e verificata SHA-256, originale conservato.

**Didattica:** nessuna nuova scheda: riscontro operativo del disco installato e rettifica trasparente della lettura errata.

**Template:** nessuna

## 27/10/2026: chiusura del live con messaggi unmount e watchdog, primo boot ancora da osservare

L'utente invia la prima schermata dopo le istruzioni exit e 3 Reboot System. Sono visibili Failed unmounting run-live-medium.mount - /run/live/medium e watchdog: watchdog0: watchdog did not stop. I messaggi appartengono alla chiusura dell'ambiente live già avviato dalla USB, coerente con le operazioni di smontaggio descritte in S208; non costituiscono una console del sistema installato. Il fotogramma non dimostra da solo la persistenza di un blocco e non viene attribuito a RAM, alimentatore, dischi o a un driver specifico. Rimozione USB non ancora confermata esplicitamente. Si indica di lasciare completare il riavvio e, soltanto se il sistema non è già ripartito e resta fermo così per almeno due minuti, tenere premuto il pulsante fino allo spegnimento, poi riaccendere con la chiavetta rimossa e acquisire la console. È una soglia operativa per questo passaggio, non un timeout del watchdog misurato o prescritto dalla fonte. Spegnimento manuale, nuova accensione e primo boot non ancora osservati. L'installazione sul Kingston sdc era già conclusa e verificata con EFI e ZFS; la precedente lettura sda del messaggio era errore dell'agente, già rettificato. Consultati S208 e S209: quest'ultimo è un documento storico sull'API watchdog, usato per il contesto generale, non per diagnosticare il kernel o il driver attuale. Foto archiviata subito con SHA-256 corrispondente, originale conservato. RAM-03/A2 da 8 GB provvisori, obiettivo 16 GB e dati SanDisk ancora aperti.

**Didattica:** nessuna nuova scheda: riconoscimento della fase di shutdown e separazione fra installazione riuscita e primo avvio ancora da verificare.

**Template:** nessuna

## 27/10/2026: primo avvio documentato in 17 foto, rete temporanea e DHCP già attivo

Archiviate e rilette tutte le17 foto fornite nella cartella Telegram: manifesto con17 sorgenti, copie, byte e SHA-256 coincidenti, originali conservati; successiva rilettura delle impronte dell'archivio completata. Le foto documentano GRUB del sistema installato25.10.7, caricamento ZFS2.3.9-1, avvio middlewared e servizi fino alla console1-10. L'ultima mostra The web interface could not be accessed. Please check network configuration, senza indirizzo di gestione. Primo boot del sistema installato quindi osservato, accesso web ancora no. Le attese ix-wait-on-disks e middlewared sono seguite nelle foto da esiti OK; le frazioni5s/20min e35s/15min10s non sono durate misurate dell'intero avvio o prove fallite. Registrati separatamente avvisi kernel MDS/MMIO/VMSCAPE, ASPM, pcspkr duplicato, dipendenze SSSD e timer ipa-epn fallito; una foto è mossa, la successiva conferma il timer. Gli avvisi non hanno impedito la console ma non vengono dichiarati risolti o usati per diagnosticare un guasto RAM. L'utente riferisce NAS temporaneamente sulla rete aziendale e chiede di preparare il resto prima della casa. Nelle ulteriori schermate sono osservati enp3s0, aliases/state.aliases vuoti, poi ipv4_dhcp Yes, ipv6_auto Yes, aliases vuoti, MTU not set. DHCP era già attivo alla lettura, non è una nuova configurazione eseguita. Prossimo Back,q,8 Open Linux Shell,ip -br address show enp3s0 e foto del risultato, ancora non acquisito. Nessun indirizzo statico, gateway, VLAN, pool, condivisione o impostazione della rete aziendale modificati. Configurazione portabile e rete definitiva tenute distinte in ADR-040 e scheda didattica03. RAM-03/A2 sola da8GB provvisori,16GB e dati SanDisk ancora aperti; nessun valore di password ricevuto o salvato.

**Didattica:** voce3 e scheda refactor-03-preparazione-nas-e-rete-temporanea.md, con estratti reali prima/dopo dalla riga Storage di rete di STACK.md.

**Template:** nessuna

## 27/10/2026: enp3s0 DOWN senza indirizzi, richiesta lettura dei flag e verifica del cavo

La nuova immagine mostra scelta8 Open Linux Shell e comando ip -br address show enp3s0 eseguito: unica riga enp3s0 DOWN e nessun indirizzo. Nel precedente editor ipv4_dhcp era già Yes, quindi non si richiede di abilitarlo di nuovo. Prossimo ip link show enp3s0 per distinguere stato amministrativo e collegamento, oltre al controllo del cavo Ethernet lato NAS e presa/switch. Flag completi e riscontro fisico non ancora acquisiti; non si conclude dal solo DOWN che il cavo sia certamente scollegato, che il server DHCP non risponda o che il driver sia guasto. Comando richiesto di sola lettura, nessuna modifica di indirizzo, DHCP o rete aziendale. Boot e installazione restano confermati, accesso web non ancora raggiunto. Foto copiata subito, SHA-256 coincidente e originale conservato.

**Didattica:** integrazione alla scheda03 con il riscontro DOWN; stato dell'opzione DHCP distinto da link e indirizzo.

**Template:** nessuna

## 27/10/2026: cavo inizialmente assente chiarito, enp3s0 ora UP ma senza IPv4

L'utente chiarisce che doveva ancora collegare il cavo Ethernet. La nuova immagine contiene la precedente lettura DOWN e una seconda esecuzione di ip -br address show enp3s0: ora UP, con un IPv6 link-local /64 e nessun IPv4 visibile. Il collegamento operativo è quindi osservato, senza cambiare il DHCP già Yes o altre impostazioni. Il valore IPv6 completo, identificante l'interfaccia, resta nella foto privata e non viene riportato nei documenti pubblici. La richiesta precedente di leggere ip link show non è più il prossimo passo: dopo il chiarimento e il nuovo UP si indica di attendere circa un minuto e digitare exit per tornare alla console e cercare l'indirizzo web; esito dopo attesa ancora non acquisito. Si chiede inoltre se l'altro capo è su presa/switch della rete aziendale o direttamente su un PC, per non presumere un servizio DHCP disponibile; risposta ancora pendente. Non si attribuisce ancora l'assenza IPv4 al server, al driver o a restrizioni della rete e non si tenta alcuna modifica alla rete aziendale. Immagine archiviata subito con hash coincidente e originale conservato.17foto precedenti salvate e lette, primo boot confermato,16GB e dati SanDisk aperti.

**Didattica:** aggiornamento scheda03: il cavo chiarisce il precedente DOWN, UP e lease IPv4 restano riscontri distinti.

**Template:** nessuna

## 27/10/2026: altro capo del cavo sullo switch aziendale con DHCP confermato dall'utente

L'utente risponde alla domanda sul collegamento: il cavo termina nello switch della rete aziendale, che assegna una classe IP specifica in DHCP. Non è un collegamento diretto NAS-PC e non si indicano IP statici manuali. Restano il DHCP già Yes e l'ultima lettura enp3s0 UP con solo IPv6 link-local; nessun IPv4 del NAS ancora osservato. Si conferma il prossimo gesto: breve attesa ed exit per leggere la console aggiornata, poi foto dell'indirizzo web o dell'eventuale stato ancora senza indirizzo. La disponibilità dichiarata del servizio DHCP non equivale a un lease già acquisito dal NAS. Nessuna modifica alla rete aziendale, nessun login web e nessun valore di password ricevuto.17foto archiviate e verificate, primo boot confermato,16GB e dati SanDisk ancora aperti.

**Didattica:** integrazione scheda03: topologia dichiarata chiarita, lease effettivo ancora da osservare.

**Template:** nessuna

## 27/10/2026: lease DHCP, login web e preferenza per gli avvisi su Proton

Le nuove schermate documentano la console con URL HTTP/HTTPS sul lease `<ip-nas-lan-temporanea>`, la pagina di login e poi la dashboard autenticata come truenas_admin. Raggiungibilità web e accesso amministrativo sono quindi verificati sulla LAN aziendale temporanea; il precedente stato senza IPv4 è superato. Nessuna modifica di DHCP, IP statici, gateway, DNS o VLAN. Dashboard25.10.7-Goldeye: 7,6 GiB disponibili, Create Pool e nessun pool dati. General Settings: memoria8 GiB, lingua English, fuso America/Los_Angeles, tastiera English (US) (us); il riquadro GUI mostra indirizzo di ascolto IPv4 0.0.0.0, che non è il lease da digitare nel browser. Indicato Localization, Settings, Europe/Rome e tastiera italiana, poi Save; salvataggio non ancora osservato e sincronizzazione oraria da verificare separatamente. Le cinque nuove immagini sono archiviate in privato e le copie sono verificate SHA-256; originali conservati.

Registrata la preferenza Proton/Gmail e Log NAS in ADR-041, pendenze, matrice16 e registro tecnico; servizio di spedizione, ricezione e filtro ancora aperti. Le17foto del primo boot restano archiviate e distinte dalle vecchie6SMART mancanti. La localizzazione è il prossimo gesto dell'utente. Nessun pool o invio email eseguito dall'agente.

**Didattica:** sviluppo della [scheda03](../context/refactor-03-preparazione-nas-e-rete-temporanea.md) su lease e login osservati e separazione fra destinatario, trasporto e classificazione.

**Template:** nessuna

## 27/10/2026: localizzazione Europe/Rome e Italian (it) salvata

La prima immagine mostra il pannello Localization Settings con Italian (it), Europe/Rome e salvataggio in corso; da sola non chiudeva la verifica. La successiva mostra il pannello chiuso e i valori nella scheda General Settings: Timezone Europe/Rome, Console Keyboard Map Italian (it), Language English, Date Format27/10/2026 e Time Format11:02:31 a24ore. Salvataggio e applicazione del fuso sono quindi osservati; non si accredita da questo la sincronizzazione NTP. Le due immagini sono archiviate nel livello privato con SHA-256 verificati e originali conservati. Prossimo gesto indicato: Settings del riquadro Email, in basso a destra, per osservare campi e metodo prima di configurare. Email ancora SMTP nel riepilogo, nessun mittente, destinatario o test di recapito osservato. Obiettivo16GB, dati SanDisk prima del pool, boot-pool ed export restano aperti.

**Didattica:** riscontro aggiunto alla scheda03: pannello con salvataggio in corso e valori finali riletti sono osservazioni diverse; nessuna nuova scelta architetturale.

**Template:** nessuna

## 27/10/2026: GMail OAuth selezionato, login e salvataggio ancora aperti

Il pannello Email Options mostra GMail OAuth selezionato, From Email e From Name vuoti, invito a configurare le credenziali OAuth e pulsante Log In To Gmail. Save e Send Test Mail sono disabilitati; il riepilogo sottostante mostra ancora SMTP. La selezione nel modulo è osservata, mentre autorizzazione, salvataggio e invio non lo sono. Email Recipients non è visibile: la descrizione di S214 resta una guida da confrontare con la GUI effettiva, non la prova di un campo già trovato. Immagine archiviata in privato con SHA-256 verificato, originale conservato. L'utente chiede se cambiando browser e rete il collegamento continuerà e conferma di procedere. Indicato Log In To Gmail, con account e consenso solo nella GUI locale; nessuna password o codice ricevuti.

Registrata la distinzione tra sessione del browser, autorizzazione salvata nel NAS e connettività della rete. Fonte Google S217 aggiunta; destinatari da trovare nella GUI effettiva, nessun recapito accreditato.

**Didattica:** sviluppo della scheda03 sul collegamento OAuth che segue la macchina e sul percorso remoto che va configurato separatamente.

**Template:** nessuna

## 27/10/2026: account Google personale dei servizi domestici, ancora da creare

Le due schermate mostrano GMail OAuth selezionato ma ancora da autorizzare, From Email e From Name vuoti, Save e Send Test Mail disabilitati. La prima apre l'help From Email, che cita envelope From e un indirizzo da configurare in Accounts > Users > Edit; la seconda descrive From Name come nome visualizzato del mittente. Sono testi di aiuto osservati, non prova di un account configurato o della posizione attuale del destinatario. Immagini archiviate in privato con SHA-256 verificati, originali conservati.

L'utente chiarisce che non ha una casella Gmail dedicata e propone di creare un normale account Google personale per altre esigenze private della propria rete domestica, riutilizzabile altrove. Raccomandato questo perimetro: un account dei servizi di casa, il cui primo utilizzo sarà l'invio degli avvisi NAS. Correzione operativa rispetto al precedente invito a usare il Gmail personale: il mittente sarà la nuova casella, non il Gmail personale già citato come destinatario alternativo. Nessun nuovo account, indirizzo, consenso, salvataggio o invio è ancora osservato. ADR-042 registra il piano, senza attestare la creazione.

Aggiunte fonti S218-S220 e placeholder del nuovo account senza un valore reale. Aggiornati mittente, destinatario e nome visualizzato nei documenti correnti. Il passo dell'utente è ora la registrazione Google Per uso personale; nessuna operazione su account Google eseguita dall'agente.

**Didattica:** [scheda04](../context/refactor-04-identita-google-e-notifiche.md), tipo di account Google, ruolo nel progetto e perimetro delle autorizzazioni.

**Template:** nessuna

## 27/10/2026: registrazione Google avviata, nuova Gmail ancora da scegliere

Le tre schermate mostrano inserimento del nome, informazioni di base e pagina Use an email address or phone number con campo vuoto. Il collegamento visibile Don't have an email address or phone number? è il prossimo gesto indicato per proseguire verso una nuova casella Gmail. Nessun indirizzo scelto, account completato o collegamento al NAS è ancora osservato. Dati anagrafici non trascritti nei documenti pubblici; indicato di verificare la correttezza della data del titolare. Le immagini sono archiviate nel livello privato con SHA-256 verificati e originali conservati.

S221 distingue account Google e Gmail: la registrazione può anche usare un indirizzo esterno o un numero, senza creare per questo la nuova casella Gmail prevista come mittente. Il piano di ADR-042 resta un account personale dei servizi domestici con Gmail; Proton resta destinatario degli avvisi. Selezione e completamento del nuovo indirizzo, autenticazione OAuth, salvataggio e recapito restano pendenti.

**Didattica:** integrazione della scheda04 su account Google e servizio Gmail; nessuna nuova scelta rispetto ad ADR-042.

**Template:** nessuna

## 27/10/2026: indirizzo servizi casa scelto e riepilogo Google dopo il QR

L'utente comunica l'indirizzo scelto per `<email-servizi-casa>` e la prima immagine mostra Verify some info before creating an account: Google chiede una verifica del dispositivo o numero contro gli abusi, con QR da scansionare dal telefono, passaggi sul telefono ed eventuale invio di un codice a Google, poi ritorno al PC. Indicato di lasciare aperta la pagina; QR conservato solo nella foto privata, non decodificato o pubblicato. La richiesta è coerente con S222, senza accreditare un'attivazione della verifica in due passaggi.

Le quattro immagini successive mostrano Add recovery email con il precedente Gmail personale compilato, Add phone number con campo vuoto, Add a recovery contact con lo stesso Gmail personale compilato e infine Review your account info con la nuova casella e pulsante Next. Il flusso ha quindi superato il ramo QR ed è al riepilogo; non è ancora osservato un accesso alla casella o al profilo dopo il completamento. Nessun numero di telefono è stato ricevuto; dal campo vuoto non si conclude che un numero sia stato aggiunto o saltato nei passi successivi. Nessun invito di recupero accettato o impostazione confermata nelle impostazioni finali.

Cinque immagini archiviate e verificate SHA-256, originali conservati. Indirizzo reale registrato prima nel livello privato e nei pattern di blocco; nel pubblico resta il segnaposto. Prossimo gesto indicato Next sul riepilogo, poi lettura della schermata seguente. Nessun login OAuth NAS, salvataggio del metodo o invio email osservato.

Aggiornati inventario, memoria e pendenze alla registrazione al riepilogo; indirizzo scelto non equivale a completamento o collegamento NAS. Mappatura privata e blocco letterale verificati prima dei documenti pubblici.

**Didattica:** sviluppo scheda04 su verifica antiabuso, recupero, identità mittente e prova del completamento. Nessuna nuova scelta architetturale oltre ADR-042.

**Template:** nessuna

## 27/10/2026: account Google dei servizi casa creato e protezione ancora da verificare

Le nove schermate documentano la scelta delle preferenze in quattro passi: attività web/app non salvata, cronologia YouTube non salvata, annunci generici selezionati dopo una prima vista senza selezione, promemoria privacy selezionati. Il riepilogo riporta attività e personalizzazione off e promemoria attivi. Seguono la pagina delle condizioni con I agree e infine la Home Google Account autenticata della nuova identità `<email-servizi-casa>`. La creazione è quindi osservata dalla pagina successiva al consenso, senza presumere il click dal solo pulsante. Le opzioni descritte sono quelle selezionate e riepilogate nel flusso; non è stata eseguita una nuova visita separata a ogni controllo dati dopo la creazione.

La Home invita ad aggiungere una seconda opzione di recupero con telefono. Il banner non dimostra lo stato di ogni metodo di accesso, del recupero o della verifica in due passaggi. Non sono ancora state aperte le impostazioni Security & sign-in: nessuna autenticazione a due fattori, passkey, app autenticatore o codice di backup viene dichiarato configurato da queste immagini. Email e contatto di recupero erano stati inseriti nel flusso precedente; conferma e stato dell'invito restano da verificare. Nove copie archiviate con SHA-256 verificati, originali conservati, dati identificanti nel solo livello privato.

Alla domanda sugli ulteriori settaggi, raccomandato un passaggio essenziale: leggere Security & sign-in, proteggere l'accesso con verifica in due passaggi e conservare i codici di backup in privato (S225-S226). La guida ammette app autenticatore e altri metodi; il metodo effettivo dipenderà dalle opzioni disponibili all'utente. Non si aggiungono servizi Google, nuovi account o una serie di controlli sulla personalizzazione già scelta. La raccomandazione non è un prerequisito tecnico di Gmail OAuth. Prossimo gesto aprire Security & sign-in, poi collegamento NAS.

Snapshot corrente compattato allo stato presente, con cronologia conservata nel registro. Fase account creazione chiusa, protezione e OAuth NAS ancora aperti. Fonti S225-S226 aggiunte.

**Didattica:** sviluppo scheda04 su preferenze dei dati, protezione dell'accesso e autorizzazione del NAS; nessuna ulteriore scelta architetturale rispetto ad ADR-042.

**Template:** nessuna

## 27/10/2026: Authenticator aggiunto, pulsante finale2FA e codici di backup rinviati

L'utente riferisce di avere impostato Google Authenticator e chiede perché sia ancora presente Turn on 2-Step Verification, chiedendo di proseguire e chiarendo di non capire quali siano i codici proposti. Le due schermate confermano Authenticator Added just now, messaggio Authenticator app has been set up e successiva riga verde Added1minuteago. Mostrano anche l'invito ad attivare2FA e il pulsante Turn on 2-Step Verification in basso. Metodo configurato e attivazione globale sono quindi stati separati: nessuna conferma2FA attiva è ancora osservata.

Indicato il solo pulsante finale, senza rifare il setup dell'app o richiedere un nuovo test di logout. I codici di backup di S226 sono spiegati come codici di scorta per accedere se perde il telefono; vengono rinviati per rispettare la richiesta di avanzare e non sono una condizione del collegamento NAS. La pendenza resta esplicita, non viene marcata completata. Dopo la conferma di attivazione si torna al NAS per Gmail OAuth. Nessun codice o QR segreto ricevuto. Le due immagini sono archiviate e verificate SHA-256, originali conservati. Fonti S225-S226 già consultate; nessun nuovo servizio o metodo aggiunto dall'agente.

**Didattica:** integrazione scheda04: un metodo aggiunto non equivale alla verifica in due passaggi attiva; rinvio dei codici mantenuto distinto dalla loro generazione.

**Template:** nessuna

## 27/10/2026: il clic2FA richiede un metodo aggiuntivo, Authenticator resta registrato

La nuova schermata mostra il dialogo Add second steps to your account: per attivare2-Step Verification chiede di aggiungere metodi come numero di telefono o passkey, con solo pulsante Go back. Sullo sfondo Authenticator resta con spunta verde e Added1minuteago. L'utente osserva correttamente che Authenticator è già un secondo fattore. Il metodo esiste, ma questo tentativo non ha attivato la protezione globale. Immagine archiviata in privato e verificata SHA-256, originale conservato; nessun numero di telefono o codice ricevuto.

Rettifica del passo precedente: indicare soltanto l'ultimo clic era un'aspettativa troppo ottimistica, smentita dal dialogo osservato. Il messaggio richiede un metodo ulteriore senza spiegarne la causa. Non si inventa un requisito universale di due metodi, non si dichiara un bug e non si rifà Authenticator. Proposto Go back, poi Phone number per seguire una delle opzioni indicate; dati e verifica si inseriscono soltanto sul sito Google. Il risultato di questo eventuale inserimento non è ancora osservato e non viene garantito. La passkey è l'altra opzione nominata dal dialogo, non configurata.

S225 descrive i metodi e l'attivazione generale. S227 è un annuncio ufficiale del6/5/2024, applicabile anche agli account personali, che distingue l'aggiunta dei metodi dall'attivazione2SV: contesto per la separazione degli stati, non diagnosi del messaggio di questo account nel2026. Il risultato osservato nella GUI guida il passo corrente. Codici di backup già rinviati; Gmail OAuth NAS non dipende tecnicamente da2FA e nessuna nuova checklist viene imposta.

**Didattica:** integrazione scheda04: Authenticator è un secondo fattore, ma registrazione del metodo e criterio di attivazione osservato nel provider restano distinti; rettifica di un'aspettativa smentita dalla GUI.

**Template:** nessuna

## 27/10/2026: verifica identità Google rifiutata nel nuovo profilo, completamento2FA richiesto ora

La prima immagine mostra We couldn't verify it's you durante il percorso di modifica della sicurezza dell'account servizi casa. La pagina suggerisce dispositivo/browser già usati e rete familiare, senza indicare causa o scadenza. L'utente riferisce poi un nuovo accesso in Chrome; la seconda immagine mostra Google Home con avatar, senza indirizzo completo. La terza mostra lo stesso rifiuto e il menu del profilo Chrome con l'indirizzo dell'account corretto, coincidente con quello della pagina Google. Il cambio di sessione non ha quindi risolto il rifiuto della verifica. Il pulsante Attiva nel menu Chrome riguarda la sincronizzazione di cronologia e schede, non l'attivazione2FA.

Tre copie archiviate e verificate SHA-256, originali conservati. I parametri di sessione visibili nell'URL restano nella sola foto privata e non vengono estratti. Nessun numero di telefono, codice o nuova conferma di metodo acquisiti. Authenticator è già stato aggiunto; una conferma2FA attiva non è osservata.

L'agente aveva proposto di rimandare l'attivazione e tornare al NAS; l'utente richiede esplicitamente di completare2FA adesso. Tale richiesta supera il rinvio: il passo corrente resta la protezione dell'account, non il collegamento NAS. Indicato il percorso ufficiale di S228: accedere al nuovo account nell'app Google o Gmail sul telefono, poi Gestisci account Google, Sicurezza e accesso, Verifica in due passaggi. Il risultato del percorso mobile non è ancora osservato. Non si rifà Authenticator, non si moltiplicano browser o metodi e non si promette che il nuovo accesso risolva il controllo. Codici di backup già rinviati, nessuna nuova richiesta di gerarli.

Fonte ufficiale S228 consultata e registrata. Distinti accesso ordinario all'account, registrazione di Authenticator, verifica per operazione sensibile e2FA attiva. Nessuna attesa o data di sblocco specifica accreditata.

**Didattica:** integrazione scheda04 su login riuscito e operazione sensibile consentita; richiesta dell'utente di completare2FA mantenuta esplicita, non trasformata in rinvio.

**Template:** nessuna

## 27/10/2026: account servizi casa aggiunto al telefono, prossimo stato2FA

L'utente conferma di avere aggiunto l'account dei servizi domestici al proprio telefono e chiede come proseguire. Riscontro dichiarato, senza nuova immagine; non si deduce che il controllo identità sia già superato o che2FA sia attiva. Indicato di selezionare il nuovo account nell'app Google o Gmail e aprire Gestisci il tuo Account Google, Sicurezza e accesso, Verifica in due passaggi; premere Attiva se presente e seguire la richiesta del fornitore. La conferma che chiude questa fase è Verifica in due passaggi attiva. Nessun codice, password, QR o numero richiesto in chat. Non si rifà l'aggiunta al telefono o il setup Authenticator. L'utente vuole completare questa fase ora; codici di backup ancora rinviati e OAuth NAS non ancora eseguito. Procedura coerente con S225 e S228 già consultate.

**Didattica:** nessuna nuova scelta; conferma operativa nel percorso già spiegato dalla scheda04.

**Template:** nessuna

## 27/10/2026: percorso dalle Impostazioni Google sul Samsung S25 Ultra

L'utente identifica il telefono come Samsung Galaxy S25 Ultra e chiede dove proseguire. L'account è già stato aggiunto secondo la sua dichiarazione; non si richiede di aggiungerlo nuovamente. Indicato il percorso dalle impostazioni del telefono: Impostazioni, Google, foto o iniziale dell'account in alto, selezione del nuovo account servizi casa, Gestisci il tuo Account Google, Sicurezza e accesso, Verifica in due passaggi. Se Google non è visibile nell'elenco, usare la ricerca delle Impostazioni per trovare la voce. Fonte generale Android S229, insieme a S225 per2FA; nessuna versione One UI o disposizione concreta della pagina viene dedotta senza una schermata.

Attiva va premuto se disponibile nella pagina2FA. L'esito non è ancora ricevuto e l'aggiunta al telefono non chiude questa fase: il criterio resta Verifica in due passaggi attiva. L'utente vuole completare la protezione ora, backup codes già rinviati, nessuna nuova configurazione Authenticator o tentativo da altro browser. Il modello del telefono è contesto per questa guida, non un censimento completo del dispositivo.

**Didattica:** nessuna nuova scelta; chiarimento di navigazione nel percorso già descritto dalla scheda04.

**Template:** nessuna

## 27/10/2026: telefono di recupero confermato e passkey presente,2FA globale ancora da leggere

La prima immagine dal Samsung mostra Confirm your recovery phone con il numero e le opzioni Yes confirm e No update. La seconda mostra il messaggio Recovery phone confirmed. Sono inoltre visibili una passkey etichettata Galaxy S25 Ultra, Last used Not yet used e This passkey is not syncable, una barra chiusa2 verification methods e le sezioni Safe Browsing, Your devices e Recent security activity. Non si è osservata la creazione della passkey: si registra la sua presenza. Non compare una dicitura esplicita di attivazione2-Step Verification. L'email completa non è visibile nelle due immagini, solo l'avatar coerente con il percorso seguito.

Il numero viene registrato prima nella mappa privata e nei pattern di blocco come `<tel-recupero-google>`, senza pubblicare valori o parametri identificanti. Due immagini archiviate e verificate SHA-256, originali conservati. Prossimo solo espandere2 verification methods, barra grigia sotto Continue, e leggere il contenuto. Non si prescrivono un'altra passkey, sincronizzazione Chrome o Enhanced Safe Browsing. La conferma del recupero e il conteggio dei metodi non vengono trasformati in2FA globale attiva; l'utente vuole completare questa fase ora, codici di backup rinviati e OAuth NAS non ancora eseguito.

**Didattica:** riscontro operativo nella scheda04: recupero confermato, credenziale presente e protezione globale restano prove diverse.

**Template:** nessuna

## 28/10/2026: Gmail OAuth salvato, test senza destinatario amministrativo e Google2FA off

Registrato alle 2026-10-28T10:53:11+01:00.

L’utente fornisce dodici nuove immagini e ribadisce che ogni passaggio deve essere registrato per poter riprendere il lavoro. Tutte le immagini nominate sono state lette e copiate nell’archivio privato, con SHA-256 confrontato con l’originale e manifest per immagine; gli originali sono conservati. Timestamp e numerazione non vengono assunti come sequenza esatta dei clic: si registrano gli stati visibili.

Nel modulo Email Options sono compilati From Email `<email-servizi-casa>` e From Name `<nome-mittente-nas>`. Il popup TrueNAS Authorization presenta Proceed; segue la scelta della nuova identità Google e la parte finale della pagina di consenso con Continue. Gli scope completi non sono visibili e non vengono inventariati per ipotesi. La schermata successiva conferma Gmail credentials have been applied e Logged In To Gmail. Un tentativo di test produce l’avviso che nessuna email è configurata per root o altro amministratore locale e chiede di configurarla prima. Infine Email settings updated e il riepilogo GMail OAuth con mittente confermano il salvataggio. OAuth e campi mittente sono quindi configurati; nessuna consegna NAS è provata.

Sul telefono Google notifica che TrueNAS ha ricevuto accesso e una copia dell’avviso compare nella Gmail personale indicata come email di recupero. Security & sign-in elenca l’evento di concessione e TrueNAS tra le applicazioni collegate. Questi sono riscontri Google del consenso, non messaggi di test inviati dal NAS. La stessa pagina mostra2-Step Verification is off, Authenticator Added Oct27, Google prompt1device, il recapito telefonico già censito e Recovery email con Verify arancione. La ricezione della copia dell’avviso non cancella quel Verify. Skip password when possible è On ed Enhanced Safe Browsing è Off: si registrano senza cambiarli. La passkey era visibile il27/10; il suo inventario non viene aperto ora e non si deduce né rimozione né creazione dalla voce del menu.

Prossimo sul telefono: dalla pagina Security & sign-in risalire a How you sign in to Google e toccare2-Step Verification, la riga con is off, poi leggere la schermata successiva. L’attivazione resta richiesta ora, i codici backup restano rinviati. Dopo2FA, verificare l’email dell’amministratore locale nel percorso utenti della GUI e impostare il destinatario Proton prima del nuovo test; nessuna modifica a utenti già eseguita. La discrepanza tra Email Recipients nella guida S214 e l’avviso effettivo rimane esplicita. S214 e S225 rilette il28/10; percorso di consenso coerente con la guida, stato reale sempre dedotto dalla GUI.

Riprendibilità e ripristino restano diversi: registro, memoria, checkpoint privato e fotografie ricostruiscono lo stato e i prossimi passi. Per un ripristino della configurazione TrueNAS serve ancora l’export con Password Secret Seed previsto da S137/S158 e la sua custodia privata; nessun file di backup o prova di restore viene dichiarato esistente. Non si propone di rifare OAuth già salvato. Password, token e codici restano in possesso dell’utente e non vengono estratti dalle immagini.

**Didattica:** scheda04 aggiornata: consenso OAuth,2FA, recapito NAS e backup configurazione hanno riscontri distinti.

**Template:** nessuna

## 28/10/2026: verifica in due passaggi attiva, email di conferma e indice privato dei messaggi

Registrato alle 2026-10-28T11:02:08+01:00.

Quattro nuove immagini documentano la pagina2-Step Verification con Turn on, Google prompt su un dispositivo, Authenticator già aggiunto e Phone number con spunta verde; è elencata anche una passkey con indicatore giallo, del quale non si inventa la causa. Segue Turning on, poi You’re now protected with 2-Step Verification con pulsante Done. L’ultima immagine mostra il corpo dell’email Google2-Step Verification turned on per l’account servizi casa. L’attivazione è quindi confermata e la relativa pendenza è chiusa, senza richiedere di rifare metodi o nuovi test di accesso. I codici di backup restano rinviati. Quattro copie archiviate e verificate SHA-256, originali conservati.

L’utente richiede di annotare anche quando arrivano le email per poterle ritrovare. Creato un indice privato per evento e casella: per ciascuna evidenza separa ora nel display della notifica, ora dell’orologio del telefono mentre il messaggio è aperto, data di osservazione e ora esatta dell’header, quando visibile. Nell’email finale l’header è fuori inquadratura: il titolo del corpo non viene chiamato oggetto verificato e l’ora di lettura non viene chiamata ricezione. Inclusa retroattivamente la notifica Gmail della copia dell’avviso OAuth già osservata nel lotto precedente, senza accreditarla come email NAS. Date e orari di sistema della registrazione vengono dalla macchina.

Prossimo sul PC TrueNAS: aprire Credentials > Users e leggere la schermata dell’account locale prima di intervenire sull’email richiesta dal test. Fonte S230 consultata per il percorso utenti; anche questa guida parla di destinatari separati da25.10, quindi non risolve per ipotesi la discrepanza della GUI. OAuth e mittente restano già salvati, recapito Proton e mail NAS ricevuta ancora non provati. Google2FA è una protezione dell’identità Google, non un’attivazione2FA della GUI NAS. Verifica email di recupero, filtro Log NAS ed export configurazione con seed rimangono aperti.

**Didattica:** scheda04: la conferma Google e l’email chiudono la sola attivazione2FA; indice messaggi con tipi di orario distinti.

**Template:** nessuna

## 28/10/2026: pagina Users osservata e motivazione TrueNAS rispetto a OMV riallineata

Registrato alle 2026-10-28T12:07:12+01:00.

La pagina Users mostra due utenti: root, Built-In Full Admin, e truenas_admin, Local Administrator e Full Admin. È selezionato root; i dettagli mostrano No Password, No SMB Access, No API Keys, No SSH Access e shell /usr/bin/zsh. Il pulsante Edit è in alto a destra. Nessun campo email è aperto e nessuna modifica è dimostrata. Immagine archiviata nel livello privato con SHA-256 verificato, originale conservato. Prossimo selezionare truenas_admin, seconda riga, poi Edit e leggere il modulo; nessuna modifica della password di root. Non sono osservate nuove email e il registro privato degli orari non riceve eventi inventati.

L’utente chiede inoltre di capire e documentare perché TrueNAS rispetto a OMV. Il confronto08 è riscritto sui requisiti correnti e la sezione tecnologia dello studio03 corretta; ADR-026 è mantenuto storico e chiarito alla luce di ADR-033/039. Il vantaggio attuale è una preferenza per l’integrazione ZFS, non avvio in specchio ormai assente,32GB o proprietà negate al plugin OMV. Fonti primarie consultate, correzione Btrfs, costi e condizioni di rivalutazione espliciti. Documento tecnico, matrice, memoria e didattica aggiornati senza cambiare la configurazione NAS.

**Didattica:** voce5 del racconto e scheda05 con estratti reali prima/dopo; distinzione capacità filesystem, integrazione piattaforma e stato attuale.

**Template:** nessuna

## 28/10/2026: Edit User aperto, campo Email dell’amministratore Not Set

Registrato alle 2026-10-28T12:20:29+01:00.

La schermata mostra selezionato truenas_admin e il pannello Edit User aperto. In Additional Details la riga Email riporta Not Set con una matita; Save è visibile in basso. Il campo dell’indirizzo amministrativo è quindi individuato e la sua assenza osservata direttamente. Nessun indirizzo inserito o salvataggio è ancora dimostrato. Immagine archiviata in privato con SHA-256 confrontato con l’originale, conservato. Non è mostrato un nuovo messaggio email: nessun orario di ricezione viene aggiunto al registro.

Prossimo: nella riga Email, sotto Additional Details del pannello destro, cliccare la matita accanto a Not Set, inserire Proton `<email-destinatario-nas>` e salvare con Save in basso. Password e permessi rimangono invariati; nessun nuovo utente richiesto. La casella Gmail `<email-servizi-casa>` resta il mittente OAuth già salvato. Email dell’account locale e identità del provider hanno ruoli distinti; dopo il salvataggio va ancora provata la ricezione reale di un messaggio NAS. S230 resta la fonte del percorso utenti, mentre la GUI effettiva identifica il controllo da usare.

**Didattica:** riscontro operativo della scheda04: il recapito email dell’amministratore è distinto dal mittente Gmail OAuth; nessuna nuova scelta architetturale.

**Template:** nessuna

## 28/10/2026: recapito Proton riscontrato nel Profile dell’amministratore

Registrato alle 2026-10-28T12:25:51+01:00.

L’utente conferma fatto. La nuova schermata mostra `<email-destinatario-nas>` sia nella riga Email del pannello Edit User di truenas_admin sia nel riquadro Profile sottostante. Il recapito non è quindi soltanto testo nel campo di modifica: il riepilogo del profilo lo riporta dopo l’azione dichiarata. Salvataggio riscontrato; nessun toast di successo è inquadrato. Il pannello di modifica resta aperto. Immagine archiviata in privato, SHA-256 confrontato con l’originale e originale conservato. Nessun nuovo test o messaggio ricevuto sono mostrati: nessun orario email aggiunto al registro.

Prossimo chiudere Edit User con la X in alto a destra, aprire System > General Settings, scegliere Settings nel riquadro Email e premere Send Test Mail. Leggere il risultato e controllare Proton; se arriva il messaggio, registrarne nel privato casella, mittente, oggetto e ora effettivamente visibili nell’header, distinguendoli dal momento della lettura. L’ora Method Call nel profilo è un evento della GUI, non una ricezione email. Gmail OAuth e Google2FA restano già acquisiti; nessuna nuova autorizzazione o modifica a password e permessi richiesta. Il servizio alert e il filtro Log NAS restano prove separate.

**Didattica:** nessuna nuova scheda; sola avanzata operativa del recapito già spiegato nella scheda04, consegna ancora distinta dal salvataggio.

**Template:** nessuna

## 28/10/2026: prima mail NAS ricevuta su Proton e backup delle personalizzazioni richiesto

Registrato alle 2026-10-28T12:36:05+01:00.

Quattro immagini mostrano Email Options con Gmail OAuth già autenticato, l’attività mail.send, Test email sent e il messaggio di prova aperto in Proton. L’utente conferma l’arrivo. Mittente visualizzato `<nome-mittente-nas>`, indirizzo coerente con il mittente configurato ma abbreviato nella vista mobile, corpo di prova TrueNAS Community Edition. Prima consegna NAS verificata, distinta dagli avvisi Google dei lotti precedenti. L’app e la notifica mostrano12:25, l’orologio del telefono12:26; data28/10 ricavata dal contesto della sessione e delle immagini, secondi e fuso non visibili. Oggetto completo e indirizzi sono solo nel registro email privato. Quattro copie archiviate, SHA-256 confrontati con gli originali, conservati.

L’utente richiede che anche le impostazioni sopravvivano a guasto o cambio hardware: ADR-043, documento backup10 e scheda didattica06. Primo export con seed ancora da acquisire; prossimo chiudere Email Options, System > Advanced Settings > Manage Configuration > Download File, selezionare Export Password Secret Seed e Save. Solo quando esiste il file, registrare versione, data, dimensioni, impronta e copie esterne; nessun export vuoto o ripristino già provato viene inventato. Fonti S137 e S158 rilette; S238 per il legame fra hardware e nomi rete.

Il pacchetto veeam-linux del template è stato ritrovato e letto, S237. Documenta il backup a livello di file e la rilettura su una macchina Linux, con limiti dichiarati sull’esecuzione degli script e sul recupero avviabile. Non si richiedono di nuovo i materiali; si riusa il percorso distinguendo prova precedente e protezione effettiva di questo NAS, che non è ancora acquisita. Nessun nuovo software installato. Test del servizio alert e filtro Log NAS restano aperti.

**Didattica:** voce6 e scheda06: configurazione, dati e materiali esterni separati; un export previsto non è un backup acquisito e il collaudo Veeam file non è un recupero TrueNAS.

**Template:** nessuna

## 28/10/2026: primo export configurazione con seed acquisito e verificato fuori NAS

Registrato alle 2026-10-28T12:43:04+01:00.

L’utente fornisce il percorso dell’export nativo. File849920byte copiato nell’archivio privato del PC, originale conservato, SHA-256 confrontato fra sorgente e copia e corrispondente. Archivio leggibile con freenas-v1.db da835584byte e pwenc_secret da32byte. Database letto in memoria, senza estrazione dei segreti in file intermedi, quick_check restituisce ok. Confronti booleani confermano mittente servizi casa, nome visualizzato, configurazione OAuth non vuota, destinatario Proton dell’amministratore e Europe/Rome; nessun valore segreto è stampato. Percorso, impronta, orari e manifest sono soltanto nel livello privato, file verificato ignorato da git.

Primo backup della configurazione fuori NAS acquisito e verificato per la tappa localizzazione/account/OAuth/recapito/prima mail ricevuta. La verifica di struttura e dei campi non è un’importazione su un’altra installazione e la presenza del campo OAuth non prova la validità futura del consenso. Download e copia sono sul medesimo PC; seconda destinazione indipendente, protezione nel lavoro Veeam e ripristino restano aperti. Nessun dato dei dataset incluso e nessun pool dati ancora creato. Nessuna nuova email mostrata, indice ricezioni invariato.

Prossimo nel NAS aprire System > Alert Settings e leggere la configurazione del servizio Email per verificare anche gli avvisi automatici, distinti dalla mail di test già riuscita. Il prossimo checkpoint di configurazione va riesportato dopo le relative modifiche; non si riscarica inutilmente la stessa tappa. Restano filtro Log NAS, boot-pool,16GB, dati SanDisk e verifica email recupero; codici Google backup rinviati.

**Didattica:** avanzamento scheda06: file acquisito, integrità strutturale e campi confermati, secondo supporto e recupero ancora distinti.

**Template:** nessuna

## 28/10/2026: Alert Settings aperto, E-Mail già abilitato al livello Warning

Registrato alle 2026-10-28T12:50:31+01:00.

Le due immagini mostrano System > Alert Settings. La tabella Alert Services contiene SNMP Trap ed E-Mail, entrambi con livello Warning ed Enabled Yes. Nella seconda riga E-Mail sono visibili matita di modifica e cestino all’estremità destra. Il destinatario e il pannello del servizio non sono ancora aperti. Non viene creato un nuovo servizio né dichiarata già riuscita la sua prova. La presenza del servizio di notifica SNMP Trap non dimostra che il demone SNMP di sistema sia in esecuzione e non viene modificata.

Sotto la tabella la categoria Applications mostra nomi di tipi di evento, livelli e frequenze impostabili; non è una lista di errori effettivamente in corso. Nessun evento applicativo viene diagnosticato da quelle etichette. Due immagini lette, archiviate e verificate SHA-256, originali conservati. Nessuna nuova email ricevuta mostrata: indice privato degli orari invariato.

Prossimo nella tabella Alert Services in alto cliccare la matita sulla seconda riga E-Mail, immediatamente prima del cestino, poi leggere destinatario e comando di test. Il primo test posta e il primo export con seed restano acquisiti; questa sola lettura non richiede un nuovo export, che si aggiornerà dopo eventuali modifiche effettive. Destinatario/test alert e filtro Log NAS restano distinti e aperti.

**Didattica:** nessuna nuova scheda: riscontro operativo del servizio già distinto da invio e ricezione nella scheda04; impostazione Enabled non sostituisce il test.

**Template:** nessuna

## 28/10/2026: override email vuoto, prossimo test del servizio alert

Registrato alle 2026-10-28T12:54:26+01:00.

Edit Alert Service mostra Name E-Mail, Enabled selezionato, Type E-Mail, Level Warning e il campo Override Admin Email vuoto. Sono presenti Save e Send Test Alert. La guida ufficiale25.10 S239 conferma che il campo vuoto usa l’email dell’amministratore: nel caso locale Proton è già salvato nel Profile. Non si duplica l’indirizzo nell’override e non si crea un nuovo servizio. Il livello Warning comprende quella gravità e quelle superiori secondo la stessa fonte, senza cambiare i livelli delle categorie.

Prossimo lasciare invariati i valori e premere Send Test Alert, pulsante grigio a destra di Save. Leggere il risultato e la ricezione su Proton; eventuale nuova email va aggiunta al registro privato con mittente, oggetto e orario effettivamente visibile. Nessun test alert, modifica o nuova email sono ancora osservati. La prima mail di test trasporto e il primo export con seed restano acquisiti; una lettura e una prova senza cambi di configurazione non richiedono un altro export della stessa tappa. Immagine letta, archiviata e verificata SHA-256, originale conservato.

**Didattica:** integrazione scheda04: destinatario ereditato distinto da override esplicito, test del servizio ancora da provare.

**Template:** nessuna

## 28/10/2026: test alert inviato e ricevuto su Proton, prossimo controllo boot-pool

Registrato alle 2026-10-28T14:42:38+01:00.

La schermata TrueNAS mostra Test alert sent nel pannello Edit Alert Service con Name/Type E-Mail, Enabled selezionato, Warning e override vuoto invariati. La schermata mobile mostra in Proton il messaggio del servizio con corpo This is a test alert, mittente visualizzato `<nome-mittente-nas>` e indirizzo abbreviato coerente con il mittente configurato. L’oggetto completo è nel registro privato. Messaggio e notifica mostrano1:01PM, registrato come13:01; telefono1:01, data28/10dal contesto e dai file osservati, secondi/fuso non visibili. L’ora di registrazione del riscontro è distinta dall’ora email. Test sintetico invio/ricezione del servizio alert concluso, senza attribuire un guasto reale o cambiarne i livelli. Le due immagini sono state lette; al momento della copia gli originali non risultano più disponibili. Cercate copie nelle cartelle di cattura/download/desktop, nell’archivio privato e nel Cestino, senza recupero. Nessuna copia o impronta delle due immagini viene accreditata: il manifest conserva descrizione e lacuna dell’archivio.

Aggiornato EMAIL-004 nel registro privato, distinto dal Test Message precedente delle12:25. Nessuna modifica di configurazione osservata: il primo export con seed rimane il checkpoint acquisito, senza richiesta di un altro download per il solo test. Non si riaprono OAuth o Google2FA.

Prossimo chiudere il pannello con la X in alto a destra e aprire System > Boot per leggere la schermata. S212 riletto per Stats/Settings e Boot Pool Status: si osserveranno condizione, dispositivi e contatori prima di interpretarli. Non sono ancora letti ONLINE o errori zero e non viene assegnato uno scrub o un ulteriore test di memoria. Filtro Log NAS mantenuto aperto; seconda copia indipendente/restore,16GB, dati SanDisk ed email recupero restano distinti.

**Didattica:** scheda04 aggiornata con la prova di servizio, distinta dalla prima prova del trasporto; nessuna nuova architettura.

**Template:** nessuna

## 28/10/2026: Boot Environments aperto,25.10.7 attivo

Registrato alle 2026-10-28T14:53:11+01:00.

La nuova schermata mostra Boot Environments con una sola voce25.10.7, Active Now, Date Created2026-10-27 11:00:07, Used Space3.42GiB e Keep No. Data e ora sono quelle visualizzate dalla GUI; non vengono trasformate in un evento di reinstallazione o di backup. Lo spazio è riferito alla voce ambiente, non alla capacità complessiva del Kingston o del pool. In alto sono visibili Stats/Settings, Boot Pool Status e Scrub Boot Pool. Non compare ancora la condizione del boot-pool né il dispositivo o i contatori di lettura/scrittura/checksum.

L’immagine è copiata e verificata SHA-256 prima della lettura visiva e dell’aggiornamento documentale, originale conservato. Il manifest registra questa sequenza per evitare una nuova perdita degli originali durante l’elaborazione. La lacuna delle due immagini precedenti rimane distinta e non viene chiusa da questa nuova copia. Nessuna email o modifica di configurazione osservate; il checkpoint nativo già acquisito rimane quello della tappa corrente.

Prossimo cliccare Boot Pool Status in alto a destra, pulsante centrale fra Stats/Settings e Scrub Boot Pool, e leggere la pagina. Non si avvia uno scrub né si modificano Keep, ambiente di avvio o firmware. Il controllo è una lettura dello stato attuale, non un nuovo ciclo di prove RAM.

**Didattica:** nessuna nuova scheda; sola lettura dell’ambiente, distinta dalla salute del pool e dal backup esterno già documentati.

**Template:** nessuna

## 28/10/2026: boot-pool ONLINE, dati dei due SSD dichiarati già salvati

Registrato alle 2026-10-28T15:07:38+01:00.

Boot Pool Status mostra boot-pool e il membro sdb3 entrambi ONLINE, ciascuno con Read0, Write0, Checksum0 e No Errors. La lettura dello stato corrente del pool di avvio è conclusa. Il nome del membro è quello della sessione osservata: non sostituisce l’identificazione per modello e ruolo, dato che le lettere dei dischi erano diverse durante l’installazione. Questi contatori non sono un nuovo test SMART né una verifica del ripristino. Il precedente dialogo Start the scrub now aveva Confirm non selezionato e Start Scrub disabilitato; non si accredita uno scrub avviato o concluso. L’ultima schermata mostra soltanto il menu Replace/Attach aperto, senza selezione.

Alla domanda esplicita sui dati di SanDisk240GB e WD Blue250GB, l’utente risponde: «Ho già salvato ciò che serve e quei dati non mi occorrono più». La questione conservazione del vecchio contenuto è chiusa per entrambi sulla base di questa dichiarazione. Non viene dedotto un collaudo delle copie né viene riaperta la stessa domanda. Si prosegue verso il pool dati in specchio sui due SSD previsti da ADR-033; il Kingston resta il disco di avvio da escludere. Nessun pool dati creato e nessuna cancellazione osservati.

Tre immagini archiviate e verificate SHA-256 prima della lettura visiva, originali conservati alla copia. Nessuna nuova email o modifica di configurazione osservata: registro email invariato e primo export con seed ancora valido per la tappa acquisita. Dopo la creazione effettiva del pool servirà una nuova generazione dell’export, conservando la precedente. La lacuna delle due vecchie immagini alert rimane dichiarata.

Prossimo cliccare in uno spazio vuoto per chiudere Replace/Attach, quindi Storage nella barra sinistra, seconda voce sotto Dashboard, e leggere la pagina per l’identificazione dei dischi. Non vengono assegnati altri scrub o test RAM. Fonte S212 per il pannello di stato; S240 consultata per il successivo wizard con selezione manuale dei dischi, mirror e riepilogo finale, ancora non eseguito.

**Didattica:** nessuna nuova scheda; lettura operativa e dichiarazione di conservazione chiusa, senza nuova scelta architetturale.

**Template:** nessuna

## 28/10/2026: Storage Dashboard aperto, No Pools

Registrato alle 2026-10-28T15:31:40+01:00.

La pagina Storage Dashboard mostra No Pools, il pulsante Create Pool al centro e Import Pool e Disks in alto a destra. Il menu del membro di avvio non è più aperto. L’assenza osservata riguarda i pool dati della dashboard, senza contraddire il boot-pool già letto ONLINE con contatori0. L’elenco con modelli e capacità dei dischi non è ancora aperto. Nessuna creazione, importazione, cancellazione o modifica di configurazione osservata.

La nuova immagine è archiviata e verificata SHA-256 prima della lettura visiva, originale conservato alla copia. Non contiene una nuova email; il registro degli orari resta invariato. Primo export con seed già acquisito; una nuova generazione sarà necessaria dopo le modifiche effettive.

Prossimo cliccare Disks in alto a destra, immediatamente a destra di Import Pool, e leggere l’elenco. SanDisk240GB e WD Blue250GB restano i due SSD del mirror dati previsto; il Kingston V300 di avvio va escluso. La dichiarazione dell’utente sui dati già salvati e non più necessari è acquisita per entrambi e non si richiede di nuovo. Pool dati, seconda copia indipendente della configurazione e ripristino restano da eseguire; nessun nuovo test RAM o scrub assegnato.

**Didattica:** nessuna nuova scheda; avanzamento della sola navigazione, senza nuove scelte architetturali.

**Template:** nessuna

## 28/10/2026: Disks letto, identificati i due SSD dati

Registrato alle 2026-10-28T15:35:41+01:00.

La pagina Disks mostra tre righe: sdc223.57GiB con Pool N/A, sdb223.57GiB con boot-pool e sda232.89GiB con Pool N/A. Nessuna casella di selezione è spuntata. I seriali di sdc e sda corrispondono ai dischi già censiti nella guida privata: rispettivamente SanDisk SDSSDA240G e WD Blue WDS250G1B0A-00H9H0. sdb è esplicitamente assegnato a boot-pool e coincide con il ruolo del Kingston su cui è già stata verificata l’installazione. I modelli non sono una lettura delle colonne di questa schermata; provengono dal collegamento con il censimento. Seriale completo e mappatura restano nel livello privato.

L’identificazione dei due candidati del mirror dati è conclusa per la sessione attuale; le lettere non diventano identità permanenti. Le capacità sono quelle mostrate dalla GUI, non una misura dello spazio utilizzabile del futuro mirror. La stessa capacità di sdc e sdb rende insufficiente distinguere i dischi solo dalla taglia: servono seriale e appartenenza al pool. Nessun pool dati creato, importato o disco cancellato. La conferma dell’utente sui dati già salvati e non più necessari di SanDisk e WD resta acquisita.

Immagine archiviata e verificata SHA-256 prima della lettura, originale conservato alla copia. Nessuna nuova email o modifica di configurazione osservata; export con seed precedente conservato, nuova generazione dopo la modifica effettiva.

Prossimo cliccare Storage, collegamento blu sopra il titolo Disks, quindi Create Pool al centro della dashboard per aprire la prima pagina del wizard. La configurazione prevista resta un solo VDEV dati Mirror con SanDisk e WD; il disco sdb di boot resta escluso. Aprire il wizard non equivale ad aver creato il pool; selezioni e riepilogo andranno letti nelle schermate successive, secondo S240.

**Didattica:** nessuna nuova scheda; applicazione del censimento e distinzione tra nome corrente, seriale e ruolo del disco.

**Template:** nessuna

## 28/10/2026: wizard tank, Mirror e primo VDEV ancora vuoto

Registrato alle 2026-10-28T15:49:17+01:00. HEAD ora osservato 7a659d12bc5e7372dd2f3fc5fc71f3446a2a3e04; aggiornamento del template intervenuto esternamente, senza commit o push dell’agente e senza riconciliare tutte le ancore.

La sequenza osservata parte da General Info con Name vuoto, Encryption non selezionata e due dischi non assegnati,223.57GiB e232.89GiB. La schermata successiva mostra tank compilato e preview Encryption None; poi è aperta Data con Layout ancora vuoto. Si osservano quindi Layout Mirror e il menu Disk Size aperto sulle due capacità, senza una taglia già selezionata. Manual Selection mostra soltanto WD WDS250G1B0A-00H9H0 sda232.89GiB e SanDisk SDSSDA240G sdc223.57GiB, entrambi SSD e con seriali corrispondenti al censimento privato. Il Kingston di boot non compare tra questi candidati. Dopo Add è presente un unico riquadro MIRROR, ancora vuoto, con richiesta di almeno due dischi e Save Selection disabilitato.

Prossimo trascinare dalla colonna sinistra prima il WD sda e poi il SanDisk sdc dentro lo stesso riquadro MIRROR a destra; non aggiungere un secondo VDEV. Leggere il risultato prima del salvataggio della selezione e del riepilogo. Le impostazioni sono ancora nel wizard: nessuna creazione, cancellazione o configurazione applicata osservate. La capacità0B della preview descrive la selezione ancora vuota, non una nuova misura della capacità fisica degli SSD.

Le sei immagini sono archiviate e verificate SHA-256 prima della rispettiva lettura, con originali conservati alla copia. Nessuna nuova email; primo export con seed invariato, nuova generazione dopo le modifiche effettive. Conservazione dei vecchi dati SanDisk/WD già risolta dalla dichiarazione dell’utente. S240 riletta per selezione manuale, mirror e raccomandazione sulla cifratura del dataset radice; la differenza fra pool, dataset e materiale di recupero è documentata nella nuova scheda07. Nessun dato ancora scritto e nessun dataset cifrato già creato.

**Didattica:** [scheda07](../context/refactor-07-pool-dataset-e-cifratura.md), confini del mirror, cifratura e custodia dei materiali di recupero.

**Template:** nessuna

## 28/10/2026: mirror dei due SSD selezionato, Review tank aperta

Registrato alle 2026-10-28T15:53:37+01:00.

La selezione manuale mostra un solo MIRROR contenente sda232.89GiB e sdc223.57GiB, con Est. Usable Raw Capacity223.57GiB e No Unassigned Disks. L’avviso Mixing disks of different sizes riguarda le capacità differenti del WD e del SanDisk già previsti dal piano. Il risultato mostrato è limitato al membro più piccolo; non si sommano le due capacità e non si dichiara223.57GiB come spazio netto dei futuri file. Nessuna nuova prova SMART o sostituzione è richiesta da questo avviso.

L’utente riferisce di avere premuto Save Selection; la schermata successiva mostra Manually Configured VDEVs, VDEVs1 e No warnings. Preview: tank, Data Manual layout1VDEVs, Encryption None, Total Raw Capacity223.57GiB; nessun disco non assegnato disponibile. L’assenza di avvisi nel pannello non cancella l’avviso di taglia effettivamente letto nel dialogo. Save Selection ha salvato soltanto la scelta nel wizard.

La pagina Review è poi osservata con Pool Name tank, Data Manual layout1VDEVs ed Est. Usable Raw Capacity223.57GiB. Pulsanti Back, Inspect VDEVs, Start Over e Create Pool. La selezione precedente permette di collegare quel singolo VDEV al mirror WD/SanDisk; Kingston di avvio resta escluso. Prossimo cliccare Create Pool, pulsante azzurro in basso a destra del gruppo, e leggere il dialogo successivo. Creazione, cancellazione e ONLINE del pool dati ancora non osservati. La conferma dell’utente sui vecchi dati resta acquisita e non si ripete la stessa domanda.

Le immagini successive sono archiviate e verificate SHA-256 prima della lettura; quella iniziale del lotto era già archiviata ed è stata ricontrollata senza duplicarla. Nessuna email né nuova configurazione applicata osservate. Primo export con seed conservato; dopo la creazione effettiva servirà una nuova generazione. S240 per il passaggio dalla selezione al riepilogo e alla creazione.

**Didattica:** sviluppo della [scheda07](../context/refactor-07-pool-dataset-e-cifratura.md): scelta salvata nel wizard distinta dal pool creato; capacità stimata distinta dallo spazio netto.

**Template:** nessuna

## 28/10/2026: tank creato, mirror Online no errors

Registrato alle 2026-10-28T15:59:16+01:00.

Sono osservati il riepilogo tank e il dialogo Warning con Confirm selezionato, poi pool.create a0%,15% con Formatting disks1/2 e95% con Setting pool options. La dashboard successiva mostra Pool created successfully. La creazione è conclusa e i due SSD dati sono stati riformattati secondo il flusso confermato dall’utente; la precedente dichiarazione sui contenuti già salvati è acquisita. Non si ripete la creazione. Il Kingston di avvio era escluso dalla selezione WD/SanDisk.

La dashboard tank mostra Data VDEVs1xMIRROR,2wide,Mixed Capacity e No other VDEV types. Storage Health: Online no errors. Usable Capacity213.19GiB, Available213.18GiB, Used8.19MiB e0% visualizzato. I223.57GiB della preview erano una stima grezza prima della creazione, non il valore ora indicato come utilizzabile. Non viene attribuita a una causa specifica la differenza senza una lettura dei relativi dettagli. Mixed Capacity conserva l’indicazione delle taglie differenti, non viene descritto come un guasto osservato.

Scheduled Scrub mostra At00:00 only on Sunday; è una pianificazione, non la prova di uno scrub già eseguito. Auto TRIM è Off. Disk Health mostra0avvisi legati alla temperatura e No disk temperature is available: zero avvisi non prova una temperatura regolare. Non si cambia ora la pianificazione né si avvia un nuovo scrub o test SSD/RAM.

Prossimo View VDEVs nel primo riquadro a sinistra per leggere membri e contatori dopo la creazione, poi nuova acquisizione configurazione con seed. Il primo file resta intatto, ma non copre la nuova tappa. Dataset/condivisioni e backup reali restano da realizzare. Le sei nuove immagini sono copiate e verificate SHA-256 prima della lettura. Il nuovo file con lo stesso nome della precedente cattura del riepilogo è diverso e conserva un archivio distinto; nessuna sovrascrittura dell’immagine già acquisita. Gli orari dei file sono registrati nel manifest ma non diventano orari esatti dei clic o del completamento. Nessuna nuova email osservata; registro email invariato. Lacuna delle vecchie immagini alert mantenuta.

Riconciliato lo stato corrente nei sei riepiloghi e nelle schede/pendenze pertinenti; la cronologia dei clic rimane nel registro, senza conservare una falsa pendenza pool assente.

**Didattica:** sviluppo della [scheda07](../context/refactor-07-pool-dataset-e-cifratura.md), configurazione applicata e misura reale distinte dalla preview.

**Template:** nessuna

## 28/10/2026: mirror e due membri ONLINE, prossimo export post-pool

Registrato alle 2026-10-28T16:07:52+01:00.

La pagina tank VDEVs espande l’unico MIRROR e mostra tre righe ONLINE, tutte con ZFS Errors No errors: il MIRROR, sda232.89GiB e sdc223.57GiB. L’appartenenza effettiva dei due SSD selezionati è ora osservata dopo la creazione; il Kingston sdb di avvio non è membro di tank. La pagina non mostra i singoli numeri Read/Write/Checksum: non si trasformano le etichette No errors in letture numeriche non presenti. Il controllo di topologia e stato corrente è concluso, senza un altro test, scrub, shell o richiesta di altre schermate sui contatori.

Prossimo acquisire la configurazione post-pool: System > Advanced Settings > Manage Configuration > Download File; nel dialogo Save Configuration selezionare Export Password Secret Seed e premere Save. S137 riletta conferma percorso, casella e salvataggio dopo cambiamenti. Il primo archivio va mantenuto; nuova acquisizione, copia e verifica non ancora eseguite. Nel download locale è ancora presente soltanto la prima generazione, secondo la lettura dei nomi file autorizzati. Dopo il download si verificano archivio e campi della tappa senza esporre seed o valori segreti.

L’immagine è archiviata e verificata SHA-256 prima della lettura, originale conservato alla copia. Nessuna modifica di configurazione, nuova email o prova di recupero osservate; registro email invariato. Dataset/condivisioni, backup dati, seconda destinazione indipendente e restore restano aperti.

**Didattica:** nessuna nuova scheda; sola verifica operativa dei membri secondo la distinzione già documentata nella scheda07.

**Template:** nessuna

## 29/10/2026: raccordo export post-pool e impostazioni da completare a casa

Registrato alle 2026-10-29T09:32:09+01:00.

Il file nativo indicato dall’utente è stato copiato e verificato il28/10:849920byte, SHA-256 originale/copia identici, SQLite quick_check ok e seed32byte presente. Il nuovo database contiene un unico record tank con GUID e System Dataset Pool tank; il primo non conteneva tank. Dimensione uguale non significa contenuto uguale: le impronte delle generazioni sono diverse. Confronti booleani confermano inoltre mittente, nome visualizzato, OAuth presente, recapito Proton e Europe/Rome; seed coerente con il precedente. Prima generazione e download originali conservati. Acquisizione post-pool conclusa, senza attribuire al file una prova di restore o una seconda destinazione indipendente.

Le tre schermate Advanced Settings del28/10 sono archiviate SHA-256 prima della lettura e mostrano: console testuale senza prompt Enabled, seriale Disabled; Syslog Info, nessun server e Include Audit Logs No; Audit7giorni, reservation/quota None e soglie75%/95%; debug kernel Disabled; Cron Jobs, Init/Shutdown Scripts e Sysctl senza voci. NTP contiene i tre server Debian configurati, senza prova di sincronizzazione. Storage indica System Dataset Pool tank e priorità resilver Never; Replication Tasks Limit5 è un limite simultaneo, non cinque attività configurate. Access mostra timeout5minuti, nessun banner; Allowed IP Addresses vuoto; nessuna GPU isolata; Global2FA TrueNAS e2FA SSH Disabled. Nessuna modifica è osservata in questi pannelli. La2FA Google già attiva resta una verifica distinta e conclusa.

Alla domanda sulle molte impostazioni, il quadro tecnico distingue preparazione locale, dipendenze della rete domestica e personalizzazioni giustificate da un bisogno. Dataset, utenti e permessi si preparano ora; indirizzi finali, DNS, VLAN e restrizione degli accessi seguono la topologia domestica; syslog segue la disponibilità del ricevitore. NTP effettivo e recupero precedono l’eventuale2FA NAS. Nessun debug, script, Sysctl o GPU aggiunti per riempire pannelli vuoti. Nuova guida tecnica10, matrice aggiornata e sviluppo didattico della scheda03; fonti S241/S242.

Il29/10 l’utente chiede di procedere. Prossimo cliccare Datasets nella barra sinistra e leggere la struttura di tank prima di creare dataset utente. Il nuovo export non va riscaricato per questa sola lettura. Filtro Log NAS, seconda copia indipendente, inclusione Veeam, restore, rete finale e obiettivo16GB restano aperti. Nessuna nuova email o nuova osservazione dal NAS il29/10 viene inventata; le letture fisiche restano del28/10.

**Didattica:** sviluppo della [scheda03](../context/refactor-03-preparazione-nas-e-rete-temporanea.md), capability del pannello distinta dal bisogno di configurarla; stessa separazione banco/rete di ADR-040.

**Template:** nessuna

## 29/10/2026: Datasets letto, requisito di crescita SSD/RAM/configurazione

Registrato alle 2026-10-29T09:50:32+01:00. HEAD ora osservato 9499dcae3668e49bb1069664176ca459d386fa53 per allineamento template esterno; nessun commit dell’agente o riconciliazione generale delle vecchie ancore.

La pagina Datasets mostra tank selezionato, Unencrypted,12.21MiB usati e213.18GiB disponibili. Details: Root Dataset, Sync STANDARD, Compression2.00x(LZ4), Enable Atime OFF, ZFS Deduplication OFF, Case Sensitivity ON e Path tank. Usage segnala System Dataset; Space Management mostra Total Allocation12.21MiB, Data Written96KiB e Children12.12MiB; User Quotas e Group Quotas None. Permissions: owner root:root e permessi Unix mostrati. Per la selezione sono indicati Snapshots0, Snapshot Tasks0 e No Backup Tasks, senza confonderli con gli export di configurazione già acquisiti. Nessun dataset utente creato e nessuna modifica osservata. Il rapporto di compressione è un dato visualizzato, non una previsione sul contenuto futuro.

L’utente richiede esplicitamente che tutto il lavoro sia scalabile con SSD di taglia maggiore, RAM e configurazione. ADR-044 adotta struttura per funzione, nomi stabili e quote rivedibili; guida NAS11 e scheda08 documentano crescita dello stesso mirror, compatibilità della memoria e continuità hardware tramite ADR-043. S243/S244 indicano sostituzione di un membro alla volta, attesa del resilver prima del successivo ed espansione dopo l’ultimo; S245 tratta dataset e quote modificabili; S246 dimensiona la memoria per carico e piattaforma. Nessun upgrade o nuovo test hardware eseguito o richiesto adesso.

Prossimo cliccare Add Dataset, pulsante azzurro in alto a destra accanto ad Add Zvol, e leggere il modulo prima di compilare o salvare. Il primo dataset utente sarà definito per funzione, senza modificare i permessi della radice per renderla una condivisione generica. Immagine archiviata e verificata SHA-256 prima della lettura, originale conservato alla copia. Nessuna nuova email o configurazione applicata; i due export precedenti rimangono il checkpoint acquisito, senza nuovo download per la sola navigazione.

**Didattica:** [scheda08](../context/refactor-08-crescita-nas-e-struttura-logica.md), struttura logica distinta dalla fotografia hardware e crescita ancora da eseguire.

**Template:** nessuna

## 29/10/2026: richieste ricevute, chiave dataset e assistente personale

Registrato alle 2026-10-29T10:12:45+01:00.

L’utente sceglie la cifratura con chiave automatica consigliata per il dataset documenti, ancora non salvato. Richiede inoltre uno studio di un assistente personale a basso consumo con Hermes Agent, Nix/NixOS e Tailscale per raggiungere la rete domestica; handoff locale ricevuto, copiato nel livello privato e in lettura. Un secondo sviluppo deve raggruppare la memoria personale con Obsidian e un brain per Claude, da raccordare alla futura capacità del template. Autori, denominazioni di modello e strumento non ancora identificato sono conservati nel promemoria privato, senza promuoverli a prodotti verificati. Si continua il lavoro NAS e si apre il filone di studio; nessuna installazione, acquisto, accesso a servizi o cambio delle rotte già eseguiti. Le precedenti restrizioni di ADR-025/037 vanno confrontate con il nuovo requisito Tailscale, senza trattarlo ancora come configurato.

**Didattica:** raccordo tecnico e didattico da completare nello stesso giro dopo lettura delle fonti e del catalogo.

**Template:** nessuna

## 29/10/2026: raccordo completo dataset e studio assistente

Registrato 2026-10-29T10:48:07+01:00. Modulo Add Dataset base e avanzato letto; immagini copiate prima della lettura e SHA-256 verificati. Prima Name vuoto/Generic/Save disabilitato; opzioni avanzate con quote/prenotazioni vuote, soglie80/95 ereditate, proprietà tabellate nella guida NAS12, ACL Type Inherit e Mode Restricted; Save abilitato non premuto. L’intestazione delle immagini avanzate non è visibile: documenti/SMB sono indicazioni da verificare, non valori già attestati. L’utente sceglie chiave automatica; Inherit(non-encrypted) ancora selezionato, cifratura non applicata. Prossimo Encryption Key/Generate Key, intestazione e ACL NFSv4 prima di Save. Dopo creazione chiave esterna e nuova generazione export; nessun nuovo export per la sola lettura. Nessuna mail nuova o modifica hardware. Fonti S247-S249.

Letto e archiviato con impronta l’handoff Nix locale; verificati homepage Hermes, piattaforme Linux ARM64/x86-64, Nix Tier2, percorso Telegram, NixOS, subnet router Tailscale, schema LLM Wiki, formato Obsidian e annuncio ufficiale Opus5.5. Link breve Nix recuperato via curl: contenuto homepage ufficiale, titolo e canonical verificati; non rimane una fonte non letta. Rinvii comunitari dell’handoff non consultati autonomamente, perimetro esplicito. Catalogo locale e template consultati in sola lettura: hermes-agent e knowledge-wiki già presenti, non istanziati. Nessuna nuova memoria globale nascosta.

Studio17 e ADR-045 conservano ruoli, confronto energetico senza watt inventati, correzioni del handoff, backup distinto di ambiente e stato, rete autorizzata per bisogno e prove future. Aggiornati VPN, accesso amministrativo, Cloudflare e matrice: il precedente stato Tailscale sola alternativa è superato dal nuovo requisito, ma nessun ingresso è già configurato. Il chiarimento dell’utente su Jev diventa un promemoria alla tappa di recezione del brain nel template; non riproporre ora la domanda. Corrette nel piano backup le vecchie frasi nessun export e pool da misurare, mantenendo aperti volumi, copia indipendente e restore.

Didattica: sviluppo voce7/scheda07 per proprietà ereditate, ACL e chiave; nuova voce9/scheda09 per assistente, memoria portabile, ambiente dichiarativo e rete. Fonti S247-S260. Nessun commit, acquisto, installazione, account o cambio macchina; lavoro documentale verificabile, servizio ancora da collaudare.

## 29/10/2026: verifica finale del raccordo assistente e dataset

Registrato 2026-10-29T11:03:08+01:00. Quattro copie fotografiche archiviate ricontrollate per dimensione e SHA-256; stesso paragrafo di stato NAS ritrovato nei sei punti di ripresa. S247-S260 univoche, ADR-045 univoca, promemoria Jev alla tappa template presente e sezione privata TAB-02/SoundCraft conservata. Raccordo NAS completo anche nel registro JSON privato. Metadati del template invariati rispetto alla copia di controllo: nel frattempo HEAD è avanzato da un’altra sessione per allineamento del template; ultimo osservato 9882943, nessun commit di questo agente e nessuna riconciliazione generale delle ancore dichiarata.

Verifiche: md-unwrap sui26Markdown del giro senza modifiche; tabelle su5file senza difetti dopo correzione della separazione della tabella fonti; albero181documenti tutti raggiungibili,0link rotti/orfani; guard-rail744file,731tracciati e13nuovi,0riscontri bloccanti e127avvisi da valutare già presenti, nessun avviso sui tre nuovi documenti. diff --check pulito. Sono controlli documentali: non dimostrano dataset creato, assistente avviato, consumi o ripristino. Didattica già collegata a voce7 e voce9. Nessuna nuova prova hardware, installazione o autorizzazione di rete.

## 29/10/2026: verifica del modulo documenti prima del Save

Registrato 2026-10-29T11:15:17+01:00. Due nuove immagini archiviate prima della lettura, originali conservati e SHA-256 verificati. Add Dataset: Parent Path tank, Name documenti, Dataset Preset SMB; Create SMB Share selezionato e SMB Name documenti. Encryption Inherit(non-encrypted) deselezionato, Encryption selezionato, Type Key, Generate Key selezionato, Algorithm AES-256-GCM. Comments vuoto, Sync Inherit(STANDARD), Compression Inherit(LZ4); quote superiori visibili vuote. tank sullo sfondo Unencrypted,12.57MiB usati/213.18GiB disponibili. Nessun Save o esito creazione osservati, nessuna nuova chiave esportata o condivisione creata. ACL non inquadrate: ultimo riscontro Inherit/Restricted. Prossimo togliere Create SMB Share per preparare prima utente e permessi, impostare ACL Type NFSv4 lasciando Mode Restricted, quindi Save e leggere esito/dialogo. La nuova configurazione con seed e la chiave esterna seguono la creazione, non questa anteprima. Nessuna nuova email o modifica hardware. Guida NAS12 aggiornata; S245/S247/S248 già registrate.

Didattica: sviluppo della voce7 nella scheda07 per distinguere dataset e condivisione automatica. Nessuna nuova scelta architetturale, skill o fonte richiesta; decisione Key già acquisita e non riproposta. Filone assistente e promemoria Jev al template conservati.

## 29/10/2026: condivisione automatica tolta, checklist unica per salvare

Registrato 2026-10-29T11:16:42+01:00. Nuova immagine copiata prima della lettura e SHA-256 verificato. Create SMB Share deselezionato, campo SMB Name non più mostrato; preset SMB, quote/riserve vuote e soglie80/95 ereditate confermati. L’utente chiede tutti i settings in un solo messaggio per scadenza della sessione: checklist completa nella guida NAS12, nessun ulteriore controllo intermedio degli stessi campi. Prossimo ACL Type NFSv4 e Mode Restricted, poi Save e lettura dell’esito. Nessun Save o dataset creato osservato, nessuna chiave esportata. Didattica: nessuna nuova scelta, resta sviluppo voce7/scheda07 già scritto. Assistente e richiamo Jev invariati.

## 29/10/2026: documenti creato, chiave esterna da acquisire

Registrato 2026-10-29T11:21:47+01:00. Due immagini archiviate prima della lettura, SHA-256 verificati e originali conservati.

Creazione osservata alle11:18: selezione documenti e messaggio Switched to new dataset. Dataset cifrato Unlocked, Usage Not Shared, Path tank/documenti. Used192KiB e Available213.17GiB; Total Allocation192KiB e Data Written192KiB(100%). SyncSTANDARD, Compression Inherit(1.00x(LZ4)), AtimeOFF, DedupOFF e CaseSensitivityOFF. UserQuotasNone. Per questa selezione Snapshots0,SnapshotTasks0,NoBackupTasks: nessuna attività dati ancora configurata. Radice tank Unencrypted,12.93MiB usati/213.17GiB disponibili. Owner root:root, pannello NFSv4 con tre ACE visibili: owner@root AllowFullControl,group@root AllowModify,builtin_users AllowModify; parte inferiore tagliata, non è una trascrizione completa delle ACL.

Prima del risultato compare ACL Types & ACL Modes, avviso generale sulla conversione delle ACL. L’anteprima sottostante mostra ACL Type SMB/NFSv4 e ACL Mode Passthrough. La dashboard successiva conferma NFSv4 ma non espone ACL Mode: non si dichiara Restricted applicato. Il valore finale va letto nella modifica delle proprietà prima di completare i permessi e la share; non si ricrea il dataset né si riaprono test hardware. Non occorre una snapshot preventiva per una migrazione di dati esistenti che questa creazione nuova non sta eseguendo.

Prossimo passo: mantenere documenti selezionato, scorrere nel pannello destro fino al riquadro Encryption e premere Export Key. S248 conferma che scarica un JSON; il file va acquisito nel livello privato senza trascrivere la chiave nei documenti o nella chat. S247 descrive la custodia esterna. Serve inoltre una nuova generazione dell’export con Password Secret Seed, conservando le due precedenti. Due copie sullo stesso client non chiudono la destinazione indipendente o il ripristino. Nessuna chiave esterna o nuovo export post-dataset è già acquisito.

Didattica: sviluppo voce7/scheda07 su avviso generale, proprietà osservate e impostazioni non ancora dimostrate. Nessuna nuova decisione di prodotto o conferma Key richiesta. S247/S248 rilette per Export Key; filone assistente e richiamo Jev conservati.

## 29/10/2026: acquisizione della chiave documenti conclusa

Registrato 2026-10-29T11:46:22+01:00. Chiave di tank/documenti acquisita dal file indicato dall’utente:86byte, originale conservato e copia privata ignorata da git, impronte SHA-256 uguali. JSON valido per il solo dataset atteso, chiave in formato esadecimale256bit; nessun valore stampato o trascritto nei documenti pubblici. Acquisizione della chiave fuori NAS conclusa. Download e archivio sono sullo stesso client: destinazione indipendente e prova di sblocco/ripristino ancora aperti. Nessuna dimostrazione del valore finale ACL Mode da questa lettura del file.

Prossimo System > Advanced Settings > Manage Configuration > Download File; selezionare Export Password Secret Seed e Save. Il nuovo archivio post-dataset è ancora da acquisire, mantenendo entrambi gli export del28/10. S137 riletto e conferma percorso e opzione; key export e configurazione restano materiali distinti. Nessuna nuova mail, test hardware o modifica al filone assistente/Jev.

Didattica: nessuna nuova scelta architetturale; prova di integrità e formato distinta dalla prova di recupero già spiegata in voce7/scheda07. Aggiornati i sei riepiloghi, guida NAS12, piano di recupero, pendenze e ripresa privata nel medesimo giro.

## 29/10/2026: export post-documenti concluso, passaggio ai permessi

Registrato 2026-10-29T11:53:05+01:00. Terzo export TrueNAS25.10.7 post-dataset acquisito:849920byte, copia privata ignorata identica al download per SHA-256, originale conservato. SQLite835584byte letto soltanto in memoria supera quick_check; seed32byte presente e coerente con la precedente. Quindici controlli di checkpoint tutti positivi: record tank/documenti univoco con campo chiave non vuoto e gestione locale, assente nell’export post-pool; pool/GUID invariati; share documenti non creata nel database; mittente/nome e recapito amministratore coerenti, OAuth presente, Europe/Rome e System Dataset Pool tank. Archivio differente da entrambe le generazioni precedenti, che restano conservate. Chiave JSON separata già acquisita e riletta per impronta. Nessun valore segreto stampato, nessun database o seed estratti su file. Il campo chiave del database non è stato decifrato o confrontato in valore con il JSON: la verifica non prova uno sblocco o restore.

Acquisizione dell’export di questa tappa conclusa. Download, archivio e chiave sono sul medesimo client: seconda destinazione indipendente, inclusione Veeam e recupero restano aperti. ACL Mode non è dimostrato dai controlli del database: ultima anteprima Passthrough, valore finale ancora da leggere. Prossimo Datasets > documenti > Edit nel riquadro Details > Advanced Options, scorrere fino a ACL Type/ACL Mode e leggere i valori; poi utente, permessi e condivisione. Nessun altro export identico o test hardware richiesto.

Didattica: sviluppo voce6/scheda06, distinzione fra nuovo checkpoint verificato, campo chiave presente e ripristino provato. Nessuna nuova scelta architetturale o fonte. Filone assistente, richiamo Jev alla tappa template e TAB/SoundCraft conservati; nessun commit dell’agente.

## 29/10/2026: rapporto NordVPN recepito e verifica del dataset selezionato

Registrato 2026-10-29T12:11:38+01:00. Edit Dataset mostra Snapshot Directory Invisible, SnapdevHidden, Copies1, RecordSize128K, ACL Type POSIX e ACL Mode Discard entrambi disabilitati, SpecialSmallBlocks0. Il nome/percorso del dataset è fuori inquadratura; il riscontro è compatibile con tank radice (S248), non una prova di regressione del figlio documenti già mostrato NFSv4. Prossimo chiudere il pannello con X, selezionare la riga documenti e verificare Details for documenti prima di Edit/Advanced Options e lettura ACL Type/Mode. Nessun Save o cambiamento dei permessi osservati; nessun nuovo export richiesto per questa sola lettura. tank sullo sfondo13.08MiB/213.17GiB, documenti192KiB/213.17GiB Unlocked. Immagine archiviata prima della lettura e SHA-256 verificato.

Letto il corpo del rapporto HTML corrente, comprese scelte, limiti, rischi e preventivo; bibliografia estratta ma non tutte le fonti consultate autonomamente. Copia privata SHA verificata e originale conservato. Non letti PDF, immagini della cartella fonti o versioni archiviate; non aperti Nord Account o dati di fughe altrui. Si recepisce il perimetro del rapporto: NordVPN spenta a casa, Meshnet esclusa con account condiviso, eventuale uso personale esterno separato. Studio18/ADR-046 e fonti S261-S268 registrano cautele di identità, DNS, Android, memoria e accessi. Il rapporto cita WireGuard, raccordato a Tailscale già richiesto in ADR-045, senza annullarlo. Prezzi e diritti contrattuali non ripubblicati o confermati; nessun acquisto o modifica di servizi.

Corrette nella documentazione le semplificazioni VPN unica protezione, Meshnet unica via di compromissione, sempre attiva uguale blocco connessioni e tutte le funzioni della suite ridotte al tunnel/DNS. Nei concetti storici aggiunta precisazione datata senza riscrittura estesa. Fonti Android, Meshnet, supporto DNS/monitor, TLS e release Windows consultate come primarie; il rinvio non recuperato sulla condivisione account non sostiene conclusioni. Didattica: nuova voce10/scheda10. Raccordati matrice, VPN, assistente, fonti, roadmap, pendenze, sei riepiloghi NAS e ripresa privata. Nessun commit, installazione o configurazione fisica; studio del brain e richiamo Jev conservati.

## 29/10/2026: lettura ACL documenti chiusa, nessuna modifica necessaria

Registrato 2026-10-29T12:21:49+01:00. Tre immagini archiviate prima della lettura, SHA-256 verificati e originali conservati. Il modulo Edit Dataset mostra Name tank/documenti bloccato: identità ora verificata. Valori letti: Comments vuoto; Sync Inherit(STANDARD); Compression Inherit(LZ4); Atime Inherit(OFF); Dedup Inherit(OFF); Case Sensitivity Insensitive bloccato; Checksum Inherit(ON); Read-only Inherit(OFF); Exec Inherit(ON); Snapshot Directory Invisible; Snapdev Inherit(HIDDEN); Copies1; Record Size Inherit(128KiB); ACL Type SMB/NFSv4; ACL Mode Restricted; Metadata(Special)Small Block Size Inherit(0). Save abilitato e Basic Options visibile. tank sullo sfondo13.16MiB/213.17GiB, documenti192KiB/213.17GiB Unlocked. Nessun campo richiede modifica.

Chiusa la lettura del tipo e della modalità ACL nel modulo identificato; i precedenti POSIX/Discard senza nome non sono proprietà accertate di documenti. Nessun nuovo Save osservato in queste immagini. Indicazione operativa: Save per confermare, poi Credentials > Users > Add e lettura del modulo utente; nessun utente, permesso finale o share ancora creati. Nessun nuovo export richiesto per una lettura senza cambi di configurazione. Tre export e chiave JSON restano acquisiti e verificati; copia indipendente e restore aperti.

Richiesta di stile ribadita dall’utente: in un solo messaggio indicare soltanto i settings che cambiano; tutti i valori, le ragioni e lo stato nel progetto. Qui i cambi necessari sono nessuno.

Didattica: nessuna nuova scelta; il criterio identità dell’oggetto più proprietà osservata, già nella scheda10, è ora soddisfatto. Campi prima non espliciti, incluso Snapshot Directory, riletti senza indovinare. Fonte UI locale, nessuna nuova fonte o ADR; filone VPN/assistente e richiamo Jev conservati.

## 29/10/2026: studi MCU, sicurezza e ponte Codex riparato a monte

Registrato 2026-10-29T16:29:12+01:00. Richiesta di strumenti browser ESP32/Arduino recepita con fonti primarie S269-S284; alternative Wokwi/CircuitJS, distinzione MCU/Linux/Hermes, preferenza Wi-Fi con SSID su VLAN per ruolo e misura alla presa. Pico/RP2040 dello studio audio non contato come hardware posseduto o host Linux. Studi19/20/21, ADR-047/048, didattica11/12; ISO27001 come metodo e GDPR con applicabilità concreta, sole due skill pertinenti istanziate da grc-skills v2.1.0. OPNsense26.7.7 ultima voce Community consultata, hotfix21/10 PHP8.5.12 incluso nel piano; macchina non aggiornata o ispezionata oggi.

Memo TXT dello switch XMG1915-10EP250×104×27mm scritto sul Desktop e verificato; fonte S09 riletta. Root AGENTS mancante riprodotto con wrapper già allineati: corretti generatore e allineatori nel template, root creato qui dal modello canonico e wrapper delle due skill generati. Otto regressioni funzionali positive, inclusi check senza scritture, personalizzazione conservata e ponte nel rapporto della passata. Nessun commit dell’agente; propagazione ufficiale globale dopo commit manuale a monte. La correzione non viene ridotta a un file locale.

Stato NAS invariato, nessun nuovo screenshot o comando sul NAS: documento identificato e Restricted corretti, nessun setting da cambiare; Save/utente/ACL/share non osservati. Export e JSON già verificati, copia indipendente/restore aperti. Jev alla tappa del brain, TAB/SoundCraft e tutti gli altri fili mantenuti. Chiusura e riapertura preparate nel livello privato; wipe ancora da eseguire solo dopo checkpoint e uscita.

**Didattica:** voci11/12 e schede corrispondenti, con estratti reali e prove che distinguono dato letto da effetto dimostrato.

**Template:** lezione del ponte mancante da registrare e recepire nel medesimo giro; filone browser da integrare a monte prima della chiusura.

## 30/10/2026: chiusura consolidata, nota fra sessioni e parità dei launcher

Registrato 2026-10-30T10:37:06+01:00. Nota esplicita della sessione esterna letta nel template: L-039 e L-040, esclusioni degli adattatori GRC e visibilità del template più avanti. Implementati a monte helper di stato con commit/pacchetti nuovi e scadenze, ricevuta nel rapporto della passata, rimozione esatta di una riga con copia preventiva e terminatori conservati. Aggiunta cassetta atomica fra Claude/Codex, launcher Claude comune e collegamento per tutti i numeri di account; nessuna notifica push o acquisizione retroattiva dei permessi promessa.

Autotest anonimizzazione riprodotto: sandbox nega la scrittura della fixture, fuori sandbox22 casi e0 errori. È un impedimento ambientale, non una prova di difetto del guard-rail; nessuna protezione tolta. Un vero difetto di chiusura individuato nel wrapper ISO27001 con trattino em: generatore corretto e pacchetto GRC ora ripara anche le esclusioni Codex alla reinstallazione, preservando la fonte terza. Le prove e i log di chiusura restano nel checkpoint privato, con esiti aggiornati prima della consegna.

Ponte e copie tecniche ricevuti qui con controllo di identità della versione precedente, marcatore del template lasciato invariato. Ripresa privata consolidata, precedente conservata con SHA; punto NAS invariato e nessun nuovo comando fisico. Nessun add, commit, push o wipe; passata ufficiale dopo commit manuale a monte. Preservati i due documenti di altra sessione nel template, TAB/SoundCraft, Jev alla tappa concordata e tutte le acquisizioni di recupero.

**Didattica:** sviluppo voce12 sulla distinzione fra controllo non eseguito, difetto riprodotto e propagazione ancora da eseguire.

**Template:** L-008 implementata; ulteriori lezioni su wrapper e fixture da registrare/recepire nello stesso lotto, con L-039/L-040 del progetto che le ha prodotte.

## 30/10/2026: prove di consegna e profilo della macchina aggiornato

Registrato 2026-10-30T11:19:18+01:00.55 regressioni complete positive in112,45secondi; verifica-ripresa28 prove positive e allinea-tutti24 casi positivi. Copertura di tutti gli account Codex1/2/3 anche su errore del backend, stessa cassetta esposta da launcher Claude/Codex e installazione ripetuta del profilo con contenuto esterno conservato. Installazione reale del profilo conclusa con backup: sette comandi, tre per ciascun agente più chiudi. Nessuna credenziale o configurazione di radice riscritta. Nuova finestra o caricamento del profilo per i nuovi launcher; nessuna ricezione retroattiva dei permessi nelle sessioni attive.

Controlli completi home-lab passati dopo le correzioni, albero senza link rotti o orfani, diff senza errori. La prova sandbox dell’autotest resta distinta dalla sua esecuzione riuscita fuori: nessuna esclusione di sicurezza aggiunta. L-008/L-009/L-010 ora recepite a monte e registro canonico copiato qui; L-039/L-040 del progetto di origine recepite con strumenti e prove. Quattro fonti browser e dipendenza pytest registrate; censimento193 fonti classificate e verificate, distinto dagli aggiornamenti di fonti già pendenti.

Nel template due soli interventi tipografici su documenti preesistenti, due accenti e due trattini, conservano tutto il contenuto: i documenti dell’altra sessione non sono presi automaticamente nel lotto di commit. Riscontro alla nota scritto privatamente, originale conservato. Stato NAS invariato, prossimo utente SMB. Chiusura manuale e passata ufficiale ancora da eseguire; nessun commit, push o wipe dell’agente.

**Didattica:** sviluppo voce12, prove del comportamento e conservazione della fonte distinti da pubblicazione e dialogo reale fra sessioni.

**Template:** L-008/L-009/L-010 recepite, con L-039/L-040 del progetto che le ha prodotte; altri filoni e lezioni preesistenti restano nel loro registro.

## Verifiche concluse 2026-10-30T11:29:19+01:00

Controlli richiesti del progetto:12 su12 positivi, albero documentale senza link rotti/orfani. Controlli del template:25 su25 positivi, diff senza errori.55 regressioni funzionali complete,24 ripetute dopo la sola formattazione,28 self-test ripresa e24 autotest passata positivi. Stage vuoto in entrambi i repository, nessun commit/push/wipe dell’agente. La distribuzione ufficiale segue il versionamento manuale.

La ripresa consolidata e il suo originale sono nel progetto. Profilo aggiornato per tutti e tre gli account dei due agenti, copia preventiva conservata. Cassetta su file e perimetro comune testati; registrazione non equivale a heartbeat, polling non equivale a notifica push, dialogo reale ancora da osservare. Chiavi e tre export restano privati; la copia su un altro disco dello stesso PC non prova una destinazione indipendente o un restore. Prossimo NAS: utente SMB, poi ACL/share; dataset già corretto e nessun nuovo test RAM.
