# Snapshot di sincronizzazione

> Da leggere per primo a inizio sessione. Fotografa lo stato del progetto al commit di riferimento e mappa ogni scheda al suo stato di verifica. E' la fonte di verita' su cosa e' fatto, non la lettura affrettata dei documenti tecnici, che descrivono in larga parte cio' che si intende costruire.

## Stato

```
Branch attivo:         main
Commit di riferimento: e91a133
Data snapshot:         2026-09-22
Remoto:                origin, allineato
```

## Avvertenza sul remoto, da leggere prima di scrivere qualunque cosa

Il remoto non e' da collegare: esiste gia', e la storia fino a `e897797` e' gia' pubblicata. La finestra in cui bastava correggere un file prima del primo push si e' chiusa in un commit precedente a questa riorganizzazione, e la conseguenza va conosciuta invece che scoperta.

Nel commit `2d3dc2c` la regola sull'identita' git conteneva, in chiaro, la casella di posta di lavoro e il nome dell'organizzazione di lavoro dell'autore, oltre alla casella personale e all'utente GitHub. L'allineamento al template del 24/08/2026 li ha sostituiti con segnaposto nell'albero di lavoro, quindi da questo commit in avanti il tree e' pulito, ma la storia li conserva e resta consultabile. La casella personale e l'utente GitHub coincidono con i metadati di ogni commit e non sono quindi un'esposizione aggiuntiva; la casella di lavoro e il nome dell'organizzazione lo sono.

Non si riscrive la storia di propria iniziativa: e' un'operazione pianificata, con backup, e va decisa dall'autore. Nel frattempo i due valori sono registrati nel file privato dei pattern, cosi' che il guard-rail li intercetti se dovessero rientrare.

## La cosa da sapere prima di ogni altra

La documentazione di questo progetto e' quasi tutta progettazione. Di realizzato c'e' l'installazione del sistema operativo del firewall del 16/01/2026, senza configurazione di rete, e l'ottenimento dell'indirizzo pubblico statico dall'operatore. Lo switch non e' acquistato, gli access point non esistono, nessun servizio interno e' in esercizio. Chi legge le schede tecniche senza questo avvertimento le scambia per descrizione di uno stato di fatto, e sbaglia.

Il vincolo operativo della linea concreta e' che l'assistenza ha escluso il collegamento diretto dell'OPNsense all'ONT e il modem non si puo' mettere in bridge. La documentazione pubblica non prova un vincolo MAC generale dell'ONT, quindi il progetto registra l'evidenza come locale e non la generalizza. Da li' discendono la baseline ONT -> Seven -> OPNsense, il doppio NAT e il wireless Seven inizialmente fuori dal perimetro del firewall.

## Stato di verifica delle schede

| Scheda | last-verified | Stato |
|---|---|---|
| `context/STACK.md` | 494b45e | aggiornata |
| `context/design-and-security.md` | 494b45e | aggiornata |
| `context/deployment.md` | 494b45e | aggiornata |
| `context/dev-testing.md` | 494b45e | aggiornata |
| `context/current-work.md` | e91a133 | aggiornata |
| `context/roadmap.md` | 494b45e | aggiornata |
| `context/diagrams/topologia-di-rete.md` | 494b45e | aggiornata |
| `context/diagrams/monitoraggio-open-source.md` | 494b45e | aggiornata |

Le schede sono state scritte il 24/08/2026 e rilette il 25/08/2026 contro il commit indicato, che e' quello in cui la documentazione ha assunto la forma attuale. Da qui in avanti la skill di sincronizzazione le segnalera' come da riverificare appena HEAD si muove, ed e' il comportamento voluto: una scheda vale finche' qualcuno l'ha confrontata con lo stato reale.

## Documentazione generata

L'albero `docs/` e' scritto e manutenuto a mano dal 25/08/2026 (ADR-010). Nasce da una conversione del documento Word, oggi archiviato in `_notes/sorgenti/`, ma non si rigenera piu': il convertitore si rifiuta di sovrascriverlo. Consistenza attuale: 146 documenti, tutti raggiungibili dalla home, zero collegamenti rotti. Il conteggio era 132 nello snapshot del 14/09/2026; la differenza sono i documenti dello studio home lab e delle note fonti aggiunti il 22/09 in una sessione parallela, piu' le tre schede nuove del 22/09, cioe' lo studio dei dischi recuperati dal QNAP, la scheda didattica su dischi e SSD per uso continuo e la scheda METATRON.

La completezza dell'ingestione iniziale non e' affidata al conteggio dei titoli: un confronto paragrafo per paragrafo ha ritrovato 1591 paragrafi su 1591, zero mancanti. Il metodo e le due insidie che lo rendevano inaffidabile alla prima corsa sono in `progress.md`; i conteggi restano in `docs/_CONVERSION-REPORT.md` come documento storico.

## Materiale privato, non versionato

Il progetto si legge e si modifica senza, ma non si verifica: il guard-rail di anonimizzazione ha bisogno del file dei pattern e si ferma se manca, invece di dare un verde non calcolato.

```
_notes/sorgenti/                        materiale grezzo archiviato, con il suo LEGGIMI.md
_notes/sorgenti/PROGETTO ... .docx      prima stesura, archivio e non fonte
_notes/.anonymization-map.md            traduzione segnaposto -> valore reale
_notes/.anonymization-patterns.json     cosa deve cercare il guard-rail
_notes/verbale-installazione-opnsense/  fotografie leggibili della sessione
tools/redactions.json                   sostituzioni della prima stesura, oggi registro
```

## Il consolidamento NAS, e cosa ha insegnato sul guard-rail

Dal 01/09/2026 il repository contiene la scheda del consolidamento di quattro desktop dismessi in un NAS, sotto `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/`, che e' l'hardware candidato allo storage di rete della fase 4. Le quattro macchine non appartengono alla rete domestica e hanno segnaposto propri, registrati nella mappa privata.

Il materiale di lavoro con i valori reali vive in `_notes/nas-consolidation/HANDOFF.md`, escluso da git per nome. L'esclusione e' per nome e non per cartella, perche' i cinque script di censimento nella stessa cartella sono puliti e versionati: se quel file viene rinominato o spostato, l'esclusione non lo segue.

La lezione che vale oltre questo caso riguarda il guard-rail. Su un file con sei password in chiaro e quattro nomi propri dichiarava zero riscontri bloccanti, perche' la categoria dei segreti letterali aveva la lista vuota e i nomi non erano registrati. Il controllo verifica cio' che gli e' stato insegnato: un esito verde su materiale nuovo non e' una garanzia finche' i valori di quel materiale non sono entrati nel file dei pattern. E' il motivo per cui la regola prescrive di aggiornare mappa e pattern prima di scrivere, non dopo.

## Il consolidamento NAS e' in esecuzione, non piu' in progetto

Dal 03/09/2026 questo e' il lavoro attivo, ed e' la prima cosa del progetto che tocca hardware invece di documentazione. Chi apre una sessione riprende da qui.

La guida operativa e' `_notes/nas-consolidation/GUIDA-PASSO-A-PASSO.md`, non versionata perche' porta i valori reali delle quattro macchine, ed e' il documento da leggere per sapere dove si e' arrivati: ogni passo concluso porta un timbro con la data. Le sue controparti pubblicabili sono le tre schede sotto `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/`, che portano l'analisi, la sequenza di assemblaggio e il calcolo dei consumi con i segnaposto al posto dei nomi macchina.

Lo stato fisico in questo momento e' che le quattro macchine sono **spente, con l'interruttore dell'alimentatore su aperto** ed etichettate; il **primo case e' aperto** e i suoi tre pezzi sono usciti, cioe' i due moduli di memoria e l'SSD SATA, etichettati sul tavolo. Gli altri due case di scorta non sono stati toccati.

Accanto alla guida vivono altri due documenti privati, scritti il 04/09. `SMONTAGGIO-CRONOLOGICO.md` e' la condensazione da banco dei passi da 1.2 a 1.7, riordinata nell'ordine dei gesti, e non porta timbri di proposito, cosi' che non esistano due registri in disaccordo. `INVENTARIO-SCORTE.md` fotografa che cosa resta disponibile dopo il consolidamento, e la sua controparte pubblicabile e' la scheda 06 della cartella NAS sotto `docs/`.

Esiste inoltre una quinta macchina, censita il 04/09, in esercizio e fuori dal consolidamento. Al NAS non porta niente, ma la sua scheda madre e' la gemella di quella della base, stesso modello e stesso lotto: cambia la gerarchia dei ricambi anche se non e' disponibile, ed e' un'informazione da ricordare il giorno di un guasto.

Due cose da non rifare, perche' sono gia' state fatte e in sessione si e' perso tempo a scoprirlo. Il censimento hardware delle quattro macchine esiste dal 31/08 e dall'01/09 in `nas-consolidation/scripts/`, e i suoi valori sono gia' trascritti nelle tabelle di identificazione della guida. La cartella `_censimento-hardware` sul NAS di backup e' una copia parziale e ridondante di quei file, non una fonte: le mancano i due report delle macchine Linux.

Una cosa che il censimento software non puo' dare, e che quindi resta da fare a mano a case aperti: i dati degli alimentatori. Un alimentatore ATX non ha interfaccia dati verso la scheda madre, quindi l'etichetta e' la sola fonte.

## Che cosa ha aggiunto la sessione del 14/09/2026, e perche' non tocca l'avanzamento fisico

Sessione interamente documentale: il filo del NAS e' rimasto fermo dov'era, e il punto di ripresa fisico descritto piu' sotto e' quello del 08/09 senza modifiche.

Sono entrate due testimonianze esterne, lette da immagine e trasformate in schede. La prima e' in coda a `docs/03-spunti-di-sviluppo/21-idee-setup-da-profili-linkedin-interessanti/02-home-lab-cybersecurity-infrastructure-autore-linkedin-b.md` e riguarda il confronto fra cio' che si puo' fare dentro una LAN di casa e cio' che sta facendo questo progetto. Il suo riscontro principale e' che la strozzatura sulla WAN si presenta identica su una linea di un altro operatore, quindi il doppio NAT non e' una peculiarita' di questa linea ma la forma normale di un firewall personale dietro un ONT in comodato. Resta una testimonianza di terzi non verificata qui, ed e' dichiarata come tale.

La seconda e' la scheda nuova `docs/03-spunti-di-sviluppo/03-server/03-stack-linux-domestico-con-soli-strumenti-open-source.md`, che descrive lo stack a cinque strati di una macchina Linux domestica con soli strumenti open source e lo lega al doppio NAT: con un proxy inverso davanti, ai due apparati in serie serve una regola di inoltro sola invece di una per servizio.

La cosa da ricordare per le sessioni future sta nella differenza fra le due architetture. Il modello del laboratorio isolato, cioe' casa sul modem e dietro il firewall solo il segmento cablato, e' senza modifiche la configurazione in cui questo progetto si trovera' il giorno dopo la fase 2: e' uno stato utilizzabile e non uno stato incompleto, e non va attraversato in fretta solo perche' gli access point non sono ancora arrivati.

## Che cosa ha aggiunto la sessione del 22/09/2026, e perche' il filo fisico resta fermo

Sessione documentale che chiude una decisione, ma non muove l'assemblaggio: nessun disco e' stato spostato, il punto di ripresa fisico resta quello dell'08/09. Sono diventati disponibili quattro dischi da 2 TB gratuiti da un QNAP TS-410U aziendale in dismissione, e la sessione li ha analizzati e destinati. La decisione, registrata come ADR-013, e' che il pool dati nasce da questi dischi invece che da un acquisto: uno specchio Toshiba piu' un Samsung, un secondo Samsung come riserva a caldo, il terzo Samsung verso la scorta con la sola rete Intel. Il motivo per cui non si fanno due specchi con tutti e quattro e' che i tre Samsung hanno seriali consecutivi e ore identiche, cioe' sono dello stesso lotto e il loro guasto non e' indipendente: uno specchio di due di loro sarebbe ridondanza solo sulla carta.

Cade cosi' il vincolo dominante del magazzino, i zero dischi dichiarati dall'inventario, ma senza lasciare una scorta di dischi: il disco disponibile e' speso per riaccendere la scorta a cui mancava solo quello. Resta aperto un solo nodo, il dimensionamento, che si chiude misurando l'occupato del QNAP prima di creare il pool.

Due schede nuove oltre allo studio applicato: la scheda didattica generale su dischi e SSD per uso continuo contro uso generico sotto `docs/04-concetti-generali/10-hardware-soluzioni-tecnologie/`, che il caso applicato richiama invece di ripetere la teoria, e la scheda METATRON sotto `docs/03-spunti-di-sviluppo/16-va-e-pentesting/`, aggiunta al filo del pentesting in home lab. Aggiornati i quattro documenti pubblici della cartella NAS e i due privati, con il nuovo Passo 4.4 di qualificazione dei dischi nella guida passo a passo.

Sul piano dell'anonimizzazione la sessione ha applicato la lezione gia' registrata due volte: i quattro seriali dei dischi sono entrati nei pattern come primo gesto, prima della scrittura, non dopo. E' la terza volta che il punto si presenta, e la prima in cui e' stato rispettato senza doverlo scoprire a posteriori.

## Punto di ripresa

I controlli sono verdi al 22/09/2026: 146 documenti su 146 raggiungibili, zero collegamenti rotti, nessun comando spezzato, nessun riscontro bloccante di anonimizzazione sui file tracciati e nuovi, e nessun riferimento di fonte non registrato. I quattro seriali dei dischi recuperati dal QNAP sono stati inseriti nei pattern del guard-rail prima di scrivere la scheda che li riguarda, ed e' verificato che i seriali reali non compaiono su nessun file tracciato mentre i segnaposto compaiono. Il verde del guard-rail vale piu' di quelli precedenti su questo materiale, perche' fino al 08/09 non conosceva nessuno dei seriali hardware ne' due dei cinque nomi host delle macchine del consolidamento: ora li conosce, e la voce di quella data nel work-log dice quali e perche' gli altri tre erano intercettati solo di rimbalzo. Il secondo controllo ha una riserva nota, descritta nella voce del 01/09/2026 del work-log: il comando documentato percorre tutto l'albero di lavoro invece dei soli file tracciati, quindi resta rosso per materiale grezzo non versionato sotto `_notes/`, mentre sui 238 documenti tracciati e' pulito.

C'e' un lavoro aperto, ed e' fisico: l'assemblaggio del NAS. Lo stato di avanzamento vive nella guida operativa sotto `_notes/nas-consolidation/`, dove ogni passo concluso porta un timbro con la data, e la feature e' descritta in `.claude/context/current-work.md`.

**Punto esatto in cui la sessione del 08/09/2026 si e' chiusa.** Giorno zero chiuso, Passo 1.1 chiuso. Passi 1.2 e 1.3 chiusi: da `PC-DESKTOP-B` sono usciti i due moduli di memoria da 8 GB e l'SSD SATA, etichettati, e il suo case e' ancora aperto. **Restano da recuperare su quel case, prima di richiuderlo, tre letture saltate al momento del prelievo**: il codice data dei due moduli, l'etichetta dell'alimentatore, e i due accessori del disco, cioe' il cavo dati uscito con esso e la slitta da 2,5 a 3,5 pollici. Il cavo cambia il piano, perche' prelevarlo qui rende superfluo prelevarne uno da `linux-desktop-B`, che quindi non va toccata oltre il suo NVMe.

Il case si richiude **dopo** quelle letture, e sul fianco si scrive che cosa gli manca: quella macchina resta un ricambio pronto e non un donatore di pezzi, perche' e' la sola che puo' sostituire la base con un trapianto invece che con una ricostruzione. **Il passo successivo e' il 1.4 della guida: si apre `linux-desktop-A` e si preleva soltanto il suo NVMe**, mentre la memoria resta dentro perche' e' l'unico kit DDR4 libero del magazzino. La confusione piu' probabile dell'intero lavoro sta li': i due NVMe da prelevare sono modelli Crucial diversi che si distinguono per un carattere nel codice prodotto, e vanno in due posizioni diverse della base.

Resta aperto in parallelo, e non blocca nulla, il Passo 0.3: l'ordine dell'adattatore da PCIe a M.2 e della scheda di rete Intel. Servono al montaggio, ai passi 2.5 e 2.6, non ai prelievi.

Da decidere a parte, e non in una sessione di lavoro ordinaria: se bonificare la storia gia' pubblicata dai due valori descritti sopra, e se il repository su GitHub debba essere pubblico o privato, cosa che al momento non risulta verificata da nessuna parte del progetto.

Il lavoro successivo alla pubblicazione e' la fase 2 della roadmap, cioe' l'identificazione fisica delle tre interfacce del firewall dalla console e la loro assegnazione ai tre ruoli, che e' il primo passo che cambia lo stato della rete e non solo della sua descrizione. La catena da predisporre e' Seven LAN 2,5 GbE -> WAN OPNsense; la guida operativa di casa e' `docs/03-spunti-di-sviluppo/23-studio-home-lab/05-guida-configurazione-opnsense-in-casa.md`.
