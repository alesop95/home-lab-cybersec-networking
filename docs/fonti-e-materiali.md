# Fonti e materiali del progetto

> Documento curato, non generato. Inventario di tutto il materiale su cui si regge la documentazione, distinguendo cio' che chi clona il repository puo' raggiungere da solo da cio' che resta sul disco di chi lavora al progetto. Serve a rendere esplicito che una parte della base documentale non e' versionata, e a dire dov'e' e perche'.

## Il documento sorgente

`_notes/sorgenti/PROGETTO rete e networking domestica.docx` e' la fonte primaria: 1906 paragrafi, 338 titoli fino al nono livello di annidamento, 74 immagini incorporate, circa 250 mila caratteri di testo al netto degli spazi. Non e' versionato, perche' il `.gitignore` esclude sia i documenti Word sia l'intera cartella `_notes/`, e perche' contiene in chiaro i valori reali che l'albero `docs/` porta invece anonimizzati. E' la fonte di rigenerazione: senza di esso l'albero `docs/` resta leggibile ma non piu' aggiornabile, quindi il file va conservato e incluso nei backup personali con la stessa cura del repository.

Il 25/08/2026 e' stata verificata la completezza della conversione con un confronto paragrafo per paragrafo fra sorgente e albero generato, su testo normalizzato e con le stesse redazioni applicate al sorgente: 1591 paragrafi su 1591 ritrovati, zero mancanti. Le uniche righe volutamente non riportate sono i segnaposto di corpo composti da una lettera ripetuta, rimossi dall'opzione di pulizia.

## Materiali locali non versionati

Vivevano alla radice del progetto e dal 25/08/2026 sono raccolti sotto `_notes/sorgenti/`, che ha un proprio indice. Sono esclusi dal versionamento sia per tipo di file sia perche' `_notes/` e' ignorata per intero.

| Materiale | Che cos'e' | Perche' non e' versionato |
|---|---|---|
| `OPNsense/OPNsense-Whitepaper-features-NIEUW.pdf` | whitepaper ufficiale sulle funzionalita' di OPNsense, scaricato dal sito del progetto | documento di terzi, ridistribuibile solo alle condizioni dell'editore; si riscarica dalla fonte |
| `OPNsense/quickprint.docx` | esaminato il 24/08/2026: contiene soltanto due loghi OPNsense e l'illustrazione della release 25.7, nessun contenuto tecnico | privo di informazione, non c'e' nulla da trascrivere |
| `QuickShare_2601161748-originali/` | trentuno fotografie della sessione di installazione del 16/01/2026, 187 MB | immagini di schermate reali con seriali e identificativi; trascritte e anonimizzate in `verbale-installazione-opnsense.md` |
| `DxDiag asus X513EAN (sysinfo).txt` | output completo di `dxdiag` sul portatile Windows del censimento, circa 96 KB | contiene nome macchina e identificativo di sistema; la porzione utile e' gia' nel censimento sotto `05-analisi-del-caso/`, anonimizzata |
| `Open-Source Security Monitoring Workflow.png` | schema del flusso di monitoraggio open source | immagine; ridisegnata come diagramma testuale in `../.claude/context/diagrams/monitoraggio-open-source.md` |
| `Diagram/Notes.txt` | appunti sulla scelta dello strumento di disegno della rete | riportato per intero qui sotto |
| `privacy pack.txt` | confronto fra servizi mainstream e alternative | riportato per intero in `alternative-privacy-oriented.md` |

Accanto a `_notes/sorgenti/` vivono, sempre sotto `_notes/` e sempre ignorate, la copia leggibile delle fotografie in `verbale-installazione-opnsense/`, ridotta da 187 a 7,5 MB senza perdere leggibilita', gli estratti temporanei del documento sorgente, e i due file dell'anonimizzazione, che sono il materiale piu' sensibile del progetto perche' rendono reversibile ogni segnaposto.

Il documento `quickprint.docx` merita una nota, perche' il suo nome promette piu' di quello che contiene. E' composto da cinque paragrafi vuoti e tre immagini, quindi non ha testo estraibile, e le tre immagini, esaminate il 24/08/2026, sono due varianti del logo OPNsense e l'illustrazione promozionale della release 25.7. Non contiene alcuna informazione tecnica: e' la stampa dell'intestazione grafica di una pagina web, non una guida rapida. Puo' essere eliminato senza perdita.

## Appunti sullo strumento di disegno della rete

Il file `Diagram/Notes.txt` contiene la motivazione della scelta dello strumento, che si riporta qui perche' e' l'unica traccia di una decisione presa e altrimenti andrebbe persa con un file non versionato.

Per un progetto di rete domestica composto da modem, switch, PC, subnetting degli indirizzi e mappa fisica e logica, la scelta ricade su draw.io: e' gratuito, funziona sia in locale come applicazione desktop sia via browser, ha librerie di simboli di rete standard e consente di annotare indirizzi IP, subnet, nomi di dispositivo e collegamenti. Non fa simulazione di traffico e non calcola le subnet automaticamente, quindi gli indirizzi vanno calcolati a parte con uno strumento esterno e poi inseriti a mano. Operativamente si sceglie la libreria Device, si trascinano le icone di modem o router, switch e PC, si creano collegamenti con linee etichettate, per esempio con il nome dell'interfaccia, e dentro ogni dispositivo si creano campi di testo per indirizzo e maschera, nella forma di un indirizzo con prefisso per il router e di un altro indirizzo della stessa subnet per un PC. La versione desktop e' un'applicazione Electron leggera e indipendente dalla connessione.

Lo schema finale non e' stato ancora disegnato in quello strumento. Nel frattempo la topologia bersaglio e' descritta come diagramma testuale in `../.claude/context/diagrams/topologia-di-rete.md`, che ha il vantaggio di essere versionabile e diffabile, cosa che un file di disegno binario non e'.

## Riferimenti esterni raccolti come segnalibri

Sotto `_notes/sorgenti/` ci sono due collegamenti Internet salvati come file `.url`, anch'essi non versionati. Se ne riportano qui gli indirizzi, che sono l'unica informazione che contengono.

Lo strumento di disegno, https://www.drawio.com/, dal file `Diagram/drawio (per editare schema finale).url`.

Un caso studio di terze parti su una piccola infrastruttura in stile enterprise, https://www.angeloantona.it/progetti/Consulenza/00099-Piccola_infrastruttura_enterprise_EN.html, dal file `infrastruttura enterprise example.url`, tenuto come riferimento di progettazione.

## Le fonti citate dentro il documento sorgente

Il `.docx` cita oltre cinquanta indirizzi web fra documentazione ufficiale, schede prodotto, articoli e discussioni. Restano tutti intatti nell'albero generato, in linea nel testo che li usa, e non si duplicano qui: cercarli nella sezione pertinente e' piu' utile che avere un elenco piatto scollegato dal contesto in cui la fonte serve. Le categorie principali sono la documentazione ufficiale di OPNsense, comprese le pagine su installazione, firewall e plugin di terze parti, le pagine tecniche dell'operatore sulla linea e sul modem, le schede prodotto dei vendor per switch, NAS e schede di rete, gli articoli su Tailscale e sui certificati per indirizzo IP, e alcune discussioni su Reddit usate come riscontro di esperienza altrui e non come fonte autorevole.

Le persone terze citate come autori di post, articoli o corsi compaiono con un segnaposto invece del nome, secondo `../.claude/rules/anonymization.md`; l'indirizzo della fonte resta accanto al segnaposto, quindi la citazione resta verificabile e il nome resta comunque leggibile a chi apre il collegamento.

## Onesta' sulle fonti

Buona parte del testo del documento sorgente e' materiale prodotto in dialogo con assistenti conversazionali, poi riletto e integrato con documentazione ufficiale e con esperienza diretta. Questo va detto perche' cambia il peso di cio' che si legge: le affermazioni ancorate a un indirizzo di documentazione ufficiale o a una schermata fotografata sono verificate, quelle che non hanno ancoraggio sono ragionamenti plausibili che nessuno ha ancora messo alla prova. Le sezioni marcate come da chiarire, elencate in `pendenze-aperte.md`, sono in larga parte proprio i punti in cui l'autore ha riconosciuto che mancava la verifica.
