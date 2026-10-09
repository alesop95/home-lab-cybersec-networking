# Snapshot di sincronizzazione

> Da leggere per primo a inizio sessione. Fotografa lo stato del progetto al commit di riferimento e mappa ogni scheda al suo stato di verifica. È la fonte di verità su cosa è fatto, non la lettura affrettata dei documenti tecnici, che descrivono in larga parte ciò che si intende costruire.

## Stato

```
Branch attivo:         main
Commit di riferimento: ee63b19, template 04b60ad
Data snapshot:         2026-10-09
Remoto:                origin, allineato
```

## Avvertenza sul remoto, da leggere prima di scrivere qualunque cosa

Il remoto non è da collegare: esiste già, e la storia fino a `e897797` è già pubblicata. La finestra in cui bastava correggere un file prima del primo push si è chiusa in un commit precedente a questa riorganizzazione, e la conseguenza va conosciuta invece che scoperta.

Nel commit `2d3dc2c` la regola sull'identità git conteneva, in chiaro, la casella di posta di lavoro e il nome dell'organizzazione di lavoro dell'autore, oltre alla casella personale e all'utente GitHub. L'allineamento al template del 24/08/2026 li ha sostituiti con segnaposto nell'albero di lavoro, quindi da questo commit in avanti il tree è pulito, ma la storia li conserva e resta consultabile. La casella personale e l'utente GitHub coincidono con i metadati di ogni commit e non sono quindi un'esposizione aggiuntiva; la casella di lavoro e il nome dell'organizzazione lo sono.

Il 07/10/2026 la storia è stata bonificata e pubblicata con push forzato: i valori sono sostituiti da segnaposto e l'albero di HEAD è rimasto identico. Il backup mirror dell'originale è in `E:/_backup-git/`. I vecchi commit restano raggiungibili per hash su GitHub finché la piattaforma non li elimina. Il repository risulta pubblico all'API di GitHub, con zero fork. Il dettaglio è nel work-log del 07/10/2026.

## La cosa da sapere prima di ogni altra

La documentazione di questo progetto è quasi tutta progettazione. Di realizzato c'è l'installazione del sistema operativo del firewall del 16/01/2026, senza configurazione di rete, e l'ottenimento dell'indirizzo pubblico statico dall'operatore. Lo switch non è acquistato, gli access point non esistono, nessun servizio interno è in esercizio. Chi legge le schede tecniche senza questo avvertimento le scambia per descrizione di uno stato di fatto, e sbaglia.

Il vincolo operativo della linea concreta è che l'assistenza ha escluso il collegamento diretto dell'OPNsense all'ONT e il modem non si può mettere in bridge. La documentazione pubblica non prova un vincolo MAC generale dell'ONT, quindi il progetto registra l'evidenza come locale e non la generalizza. Da lì discendono la baseline ONT -> Seven -> OPNsense, il doppio NAT e il wireless Seven inizialmente fuori dal perimetro del firewall.

## Stato di verifica delle schede

| Scheda | last-verified | Stato |
|---|---|---|
| `context/STACK.md` | ee63b19 | aggiornata il 9/10/2026 con foto, matrice e decisioni |
| `context/design-and-security.md` | ee63b19 | aggiornata il 9/10/2026 con foto, matrice e decisioni |
| `context/deployment.md` | ee63b19 | aggiornata il 9/10/2026 con foto, matrice e decisioni |
| `context/dev-testing.md` | ee63b19 | aggiornata il 9/10/2026 con foto, matrice e decisioni |
| `context/current-work.md` | ee63b19 | aggiornata il 9/10/2026 con foto, matrice e decisioni |
| `context/roadmap.md` | ee63b19 | aggiornata il 9/10/2026 con foto, matrice e decisioni |
| `context/diagrams/topologia-di-rete.md` | ee63b19 | aggiornata il 9/10/2026 con foto, matrice e decisioni |
| `context/diagrams/monitoraggio-open-source.md` | ee63b19 | aggiornata il 9/10/2026 con foto, matrice e decisioni |

Le schede sono state scritte il 24/08/2026 e rilette il 25/08/2026 contro il commit indicato, che è quello in cui la documentazione ha assunto la forma attuale. Da qui in avanti la skill di sincronizzazione le segnalerà come da riverificare appena HEAD si muove, ed è il comportamento voluto: una scheda vale finché qualcuno l'ha confrontata con lo stato reale.

## Documentazione generata

L'albero `docs/` è scritto e manutenuto a mano dal 25/08/2026 (ADR-010). Nasce da una conversione del documento Word, eliminato il 07/10/2026 dopo la verifica di ADR-019: `docs/` è l'unica fonte. Consistenza all'8/10/2026: 160 documenti, tutti raggiungibili dalla home, zero collegamenti rotti, misurati con `tools/check-docs-tree.py`. Il conteggio era 132 nello snapshot del 14/09/2026; la differenza sono i documenti dello studio home lab e delle note fonti aggiunti il 22/09 in una sessione parallela, più le tre schede nuove del 22/09, cioè lo studio dei dischi recuperati dal QNAP, la scheda didattica su dischi e SSD per uso continuo e la scheda METATRON.

La completezza dell'ingestione iniziale non è affidata al conteggio dei titoli: un confronto paragrafo per paragrafo ha ritrovato 1591 paragrafi su 1591, ma con un perimetro di soli paragrafi; il 07/10/2026 una verifica più larga ha trovato e recuperato 53 note a piè di pagina che quel confronto non vedeva (ADR-019). Il metodo e le due insidie che lo rendevano inaffidabile alla prima corsa sono in `progress.md`; i conteggi restano in `docs/_CONVERSION-REPORT.md` come documento storico.

## Materiale privato, non versionato

Il progetto si legge e si modifica senza, ma non si verifica: il guard-rail di anonimizzazione ha bisogno del file dei pattern e si ferma se manca, invece di dare un verde non calcolato.

```
_notes/sorgenti/                        materiale grezzo archiviato, con il suo LEGGIMI.md
_notes/.anonymization-map.md            traduzione segnaposto -> valore reale
_notes/.anonymization-patterns.json     cosa deve cercare il guard-rail
_notes/verbale-installazione-opnsense/  fotografie leggibili della sessione
tools/redactions.json                   sostituzioni della prima stesura, oggi registro
```

## Il consolidamento NAS, e cosa ha insegnato sul guard-rail

Dal 01/09/2026 il repository contiene la scheda del consolidamento di quattro desktop dismessi in un NAS, sotto `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/`, che è l'hardware candidato allo storage di rete della fase 4. Le quattro macchine non appartengono alla rete domestica e hanno segnaposto propri, registrati nella mappa privata.

Il materiale di lavoro con i valori reali vive in `_notes/nas-consolidation/HANDOFF.md`, escluso da git per nome. L'esclusione è per nome e non per cartella, perché i cinque script di censimento nella stessa cartella sono puliti e versionati: se quel file viene rinominato o spostato, l'esclusione non lo segue.

La lezione che vale oltre questo caso riguarda il guard-rail. Su un file con sei password in chiaro e quattro nomi propri dichiarava zero riscontri bloccanti, perché la categoria dei segreti letterali aveva la lista vuota e i nomi non erano registrati. Il controllo verifica ciò che gli è stato insegnato: un esito verde su materiale nuovo non è una garanzia finché i valori di quel materiale non sono entrati nel file dei pattern. È il motivo per cui la regola prescrive di aggiornare mappa e pattern prima di scrivere, non dopo.

## Il consolidamento NAS è in esecuzione, non più in progetto

Dal 03/09/2026 questo è il lavoro attivo, ed è la prima cosa del progetto che tocca hardware invece di documentazione. Chi apre una sessione riprende da qui.

La guida operativa è `_notes/nas-consolidation/GUIDA-PASSO-A-PASSO.md`, non versionata perché porta i valori reali delle quattro macchine, ed è il documento da leggere per sapere dove si è arrivati: ogni passo concluso porta un timbro con la data. Le sue controparti pubblicabili sono le tre schede sotto `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/`, che portano l'analisi, la sequenza di assemblaggio e il calcolo dei consumi con i segnaposto al posto dei nomi macchina.

Lo stato fisico al 07/10/2026 è che tutti i prelievi sono chiusi, dal Passo 1.1 al 1.7: i pezzi sono sul tavolo, etichettati e verificati contro il censimento, e le tre macchine donatrici sono richiuse ed etichettate come scorte intere. Il montaggio sulla base non è cominciato, in attesa dell'adattatore da PCIe a M.2. Il paragrafo che qui descriveva il primo case aperto dell'08/09 è superato.

Accanto alla guida vivono altri due documenti privati, scritti il 04/09. `SMONTAGGIO-CRONOLOGICO.md` è la condensazione da banco dei passi da 1.2 a 1.7, riordinata nell'ordine dei gesti, e non porta timbri di proposito, così che non esistano due registri in disaccordo. `INVENTARIO-SCORTE.md` fotografa che cosa resta disponibile dopo il consolidamento, e la sua controparte pubblicabile è la scheda 06 della cartella NAS sotto `docs/`.

Esiste inoltre una quinta macchina, censita il 04/09, in esercizio e fuori dal consolidamento. Al NAS non porta niente, ma la sua scheda madre è la gemella di quella della base, stesso modello e stesso lotto: cambia la gerarchia dei ricambi anche se non è disponibile, ed è un'informazione da ricordare il giorno di un guasto.

Due cose da non rifare, perché sono già state fatte e in sessione si è perso tempo a scoprirlo. Il censimento hardware delle quattro macchine esiste dal 31/08 e dall'01/09 in `nas-consolidation/scripts/`, e i suoi valori sono già trascritti nelle tabelle di identificazione della guida. La cartella `_censimento-hardware` sul NAS di backup è una copia parziale e ridondante di quei file, non una fonte: le mancano i due report delle macchine Linux.

Una cosa che il censimento software non può dare, e che quindi resta da fare a mano a case aperti: i dati degli alimentatori. Un alimentatore ATX non ha interfaccia dati verso la scheda madre, quindi l'etichetta è la sola fonte.

## Che cosa ha aggiunto la sessione del 14/09/2026, e perché non tocca l'avanzamento fisico

Sessione interamente documentale: il filo del NAS è rimasto fermo dov'era, e il punto di ripresa fisico descritto più sotto è quello del 08/09 senza modifiche.

Sono entrate due testimonianze esterne, lette da immagine e trasformate in schede. La prima è in coda a `docs/03-spunti-di-sviluppo/21-idee-setup-da-profili-linkedin-interessanti/02-home-lab-cybersecurity-infrastructure-autore-linkedin-b.md` e riguarda il confronto fra ciò che si può fare dentro una LAN di casa e ciò che sta facendo questo progetto. Il suo riscontro principale è che la strozzatura sulla WAN si presenta identica su una linea di un altro operatore, quindi il doppio NAT non è una peculiarità di questa linea ma la forma normale di un firewall personale dietro un ONT in comodato. Resta una testimonianza di terzi non verificata qui, ed è dichiarata come tale.

La seconda è la scheda nuova `docs/03-spunti-di-sviluppo/03-server/03-stack-linux-domestico-con-soli-strumenti-open-source.md`, che descrive lo stack a cinque strati di una macchina Linux domestica con soli strumenti open source e lo lega al doppio NAT: con un proxy inverso davanti, ai due apparati in serie serve una regola di inoltro sola invece di una per servizio.

La cosa da ricordare per le sessioni future sta nella differenza fra le due architetture. Il modello del laboratorio isolato, cioè casa sul modem e dietro il firewall solo il segmento cablato, è senza modifiche la configurazione in cui questo progetto si troverà il giorno dopo la fase 2: è uno stato utilizzabile e non uno stato incompleto, e non va attraversato in fretta solo perché gli access point non sono ancora arrivati.

## Che cosa ha aggiunto la sessione del 22/09/2026, e perché il filo fisico resta fermo

Superata il 07/10/2026: i dischi del QNAP non si sono resi disponibili, e la decisione che questa sezione descrive è stata sostituita da ADR-014 e ADR-015, con il NAS che parte senza dischi meccanici. La sezione resta come storia.

Sessione documentale che chiude una decisione, ma non muove l'assemblaggio: nessun disco è stato spostato, il punto di ripresa fisico resta quello dell'08/09. Sono diventati disponibili quattro dischi da 2 TB gratuiti da un QNAP TS-410U aziendale in dismissione, e la sessione li ha analizzati e destinati. La decisione, registrata come ADR-013, è che il pool dati nasce da questi dischi invece che da un acquisto: uno specchio Toshiba più un Samsung, un secondo Samsung come riserva a caldo, il terzo Samsung verso la scorta con la sola rete Intel. Il motivo per cui non si fanno due specchi con tutti e quattro è che i tre Samsung hanno seriali consecutivi e ore identiche, cioè sono dello stesso lotto e il loro guasto non è indipendente: uno specchio di due di loro sarebbe ridondanza solo sulla carta.

Cade così il vincolo dominante del magazzino, i zero dischi dichiarati dall'inventario, ma senza lasciare una scorta di dischi: il disco disponibile è speso per riaccendere la scorta a cui mancava solo quello. Resta aperto un solo nodo, il dimensionamento, che si chiude misurando l'occupato del QNAP prima di creare il pool.

Due schede nuove oltre allo studio applicato: la scheda didattica generale su dischi e SSD per uso continuo contro uso generico sotto `docs/04-concetti-generali/10-hardware-soluzioni-tecnologie/`, che il caso applicato richiama invece di ripetere la teoria, e la scheda METATRON sotto `docs/03-spunti-di-sviluppo/16-va-e-pentesting/`, aggiunta al filo del pentesting in home lab. Aggiornati i quattro documenti pubblici della cartella NAS e i due privati, con il nuovo Passo 4.4 di qualificazione dei dischi nella guida passo a passo.

Sul piano dell'anonimizzazione la sessione ha applicato la lezione già registrata due volte: i quattro seriali dei dischi sono entrati nei pattern come primo gesto, prima della scrittura, non dopo. È la terza volta che il punto si presenta, e la prima in cui è stato rispettato senza doverlo scoprire a posteriori.

## Che cosa ha aggiunto la sessione del 07/10/2026

Allineamento al template `4f4f9d0`, senza conflitti, e guard-rail riportato al verde: i nove riscontri bloccanti erano falsi positivi ereditati dagli allineamenti di fine settembre, cioè un nome di organizzazione corto che combaciava dentro parole comuni e caselle d'esempio su domini riservati. Lo script ora cerca le organizzazioni a parola intera e ammette i domini riservati; il dettaglio e la prova sono nel work-log. Il filo fisico del NAS è fermo dove l'aveva lasciato l'08/09. Nella stessa giornata: storia bonificata e pubblicata, allineamento al template fino a `c668b85`, NAS senza dischi meccanici, costo d'esercizio ricalcolato con il motore delle bollette, prelievi chiusi al banco e alimentatore della base confermato.

## Punto di ripresa

Al 07/10/2026, commit `6769dc4` più le scritture di chiusura di questa sessione. Storia bonificata e pubblicata; repository pubblico; progetto allineato al template `c668b85`, con `chiudi` utilizzabile e il guard-rail di anonimizzazione fra i suoi controlli. Le ancore delle schede, che puntavano a commit di prima della riscrittura, sono state riportate sugli equivalenti della storia attuale con la tabella di corrispondenza privata `_notes/bonifica-2026-10-07-commit-map.txt`; gli hash citati in prosa nel work-log prima del 07/10 sono quelli vecchi, e si traducono con la stessa tabella.

Al 09/10/2026 il server Proxmox è deciso: `linux-desktop-A` (ADR-030), con la Z97-P di PC-03 a 32 GB come nodo di laboratorio e banco di analisi dei campioni. Lo switch resta il 10EP con moduli SFP in rame se servono (ADR-029). PC-02 si svuota e si smaltisce (ADR-031). Il lavoro fisico è fermo al passo 1 della sequenza del da farsi al banco, scritta nel piano unificato in dodici passi: l'utente è al banco e non ha ancora aperto le macchine. Le slitte dei dischi di PC-02 risultano rotte, con una conseguenza circoscritta al solo Kingston V300.

Il filo attivo è la progettazione della rete e dei servizi, descritto in `.claude/context/current-work.md`, che contiene il quadro sempre aggiornato delle decisioni prese, proposte e pendenti. Decisi: switch XMG1915-10EP e due NWA130BE (ADR-017, ADR-023, ADR-024), PS5 sul Seven e niente FRITZ!Box (ADR-018), NAS su TrueNAS SCALE (ADR-026), amministrazione da tre ingressi verso la VLAN 99 (ADR-025), regole fra le zone con aperture a tempo del laboratorio, monitoraggio Wazuh con Suricata in OPNsense (ADR-028). Il piano unificato propone `linux-desktop-A` come server Proxmox. Le foto di PC-02 e PC-03 del 09/10/2026 mostrano solo DDR3, quindi l'idea della DDR4 cade; portano due SSD SATA da circa 250 GB, candidati allo specchio di Proxmox dopo la lettura SMART e la raccolta che legge i processori. La riscrittura al posto della documentazione dell'autore (ADR-020) ha completato `02-ftth-fastweb` e il censimento; restano `04-concetti-generali` e `03-spunti-di-sviluppo`, oltre ai documenti di dettaglio di ogni area del piano. Il progetto è allineato al template `04b60ad` con gli strumenti in `tools/` (ADR-022).

Il filo del NAS è in pausa in attesa dell'adattatore da PCIe a M.2. Tutti i prelievi sono chiusi, dal Passo 1.1 al 1.7, e il montaggio non è cominciato; la ripresa è il Passo 1.6 della guida privata. Decisioni del giorno: ADR-014 e ADR-015 sul pool senza dischi meccanici, ADR-016 sull'alimentatore della base.

Il lavoro che cambia lo stato della rete resta la fase 2 della roadmap, cioè l'identificazione fisica delle tre schede di rete del firewall dalla console. Si fa alla macchina, non al repository.
