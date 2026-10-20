# Backup e ripristino del laboratorio

Documento avviato il 19/10/2026 durante il collaudo della memoria del NAS. La preparazione documentale è pronta per la revisione al 20/10/2026; non certifica un backup eseguito, un ripristino riuscito o una configurazione già applicata. Le scelte di hardware restano quelle di [Allocazione dell'hardware](../23-studio-home-lab/12-allocazione-dell-hardware.md); il [registro del montaggio](../02-storage-di-rete-nas/09-registro-del-montaggio.md) conserva lo stato fisico.

## Il vincolo da risolvere

Il NAS previsto ha il Kingston V300 per il solo avvio e uno specchio dati fra SanDisk 240 GB e WD Blue 250 GB. L'allocazione canonica ora distingue il limite nominale di 240 GB, circa 223,517 GiB prima del costo del filesystem, dal tetto iniziale proposto di 180 GB decimali. Lo spazio effettivamente disponibile dopo la creazione del pool resta da misurare. Il server Proxmox è previsto sui due NVMe da 1 TB in specchio; il montaggio e la capacità occupata dalle macchine virtuali non sono ancora verificati. Non si può promettere che il NAS contenga tutte le copie del server senza misurare il contenuto da salvare.

Al 20/10 entrambi i moduli del NAS hanno prodotto errori nelle prove individuali nello stesso slot A1; il secondo mostra due errori a Time 3:03:15, Pass 3. La qualificazione della memoria resta condizione di avvio. Il piano qui descritto si prepara senza intervenire sulle macchine.

## Il perimetro della consegna

Il lavoro deve separare i dati originali dalle copie e dalle configurazioni, stabilire quali ripristini siano possibili dopo un guasto, rendere visibili i casi senza una seconda copia indipendente e proporre una finestra di salvataggio compatibile con l'accensione del NAS. Capacità, durata e numero di versioni devono essere calcolati con assunzioni dichiarate, senza contare in anticipo su compressione o deduplicazione.

La consegna comprende il piano di protezione, le procedure di backup e ripristino per macchina e servizio, i controlli di accesso proposti, un calcolo riproducibile dello spazio e una sequenza di collaudo. I documenti distinguono fonti lette, prove locali e ripristini reali ancora da eseguire.

## Stato della ricerca

Vincoli, dimensionamento, procedure e criteri di ammissione sono scritti. Le fonti ufficiali lette distinguono backend PVE, recupero host, TrueNAS stabile 25.10, Veeam Agent 13, restic 0.19.1 e alternativa PBS. Sono ricostruite le dipendenze di rete e di emergenza, con le correzioni dell'allocazione canonica applicate il 20/10 durante la preparazione del versionamento, dopo il controllo dei delta. Le prove sulle macchine restano da eseguire. Conservazione, orari aggiuntivi, quote e obiettivi di perdita massima restano proposte esplicite, senza trasformarsi in decisioni accettate dall'utente.

## Verifiche aperte

Non sono ancora noti il volume dei dati da proteggere, la dimensione reale dei backup delle macchine virtuali, la velocità sostenuta sulla rete, la disponibilità di una copia fuori macchina e l'effetto delle istantanee sullo spazio. Il piano non chiude queste misure con dati costruiti.

## Primo risultato: capacità e confini delle copie

Il [dimensionamento riproducibile](03-dimensionamento-e-scenari-di-backup.md) chiarisce le unità del piccolo specchio SATA e fornisce uno strumento con scenari costruiti, compresi i casi che superano spazio e durata. Il tetto iniziale proposto è 180 GB decimali; il pool reale e le dimensioni degli archivi restano da misurare.

La documentazione del progetto Proxmox distingue archivi completi su storage a file e repository a blocchi deduplicati su Proxmox Backup Server. Per partire senza un altro servizio, questo piano studia gli archivi completi su una condivisione dedicata del NAS. Il loro spazio di picco comprende anche una nuova generazione. Il [confronto con PBS](09-confronto-archivi-proxmox-e-pbs.md) esplicita risorse aggiuntive, spazio prima della raccolta dei blocchi, permessi e dipendenze di recupero; resta un'alternativa da collaudare, senza assegnazione di hardware o installazione. [Backup e ripristino Proxmox](https://raw.githubusercontent.com/proxmox/pve-docs/master/vzdump.adoc).

| Contenuto | Originale previsto | Copia distinta da progettare | Stato |
|---|---|---|---|
| dischi e configurazioni delle VM | specchio NVMe del server | archivi sullo specchio SATA del NAS | contenuto e dimensioni da raccogliere |
| configurazione dell'host Proxmox | server | fascicolo privato fuori host, oltre ai backup guest | HOST-01 preparata; metodo coerente per il database e prova reale aperti |
| documenti conservati sul NAS | specchio SATA del NAS | destinazione su altra macchina o supporto da assegnare | il mirror e le istantanee locali non chiudono la copia |
| configurazione e chiavi NAS | avvio e configurazione TrueNAS | esportazione custodita fuori dal NAS, con materiali di recupero separati | nessun export ancora eseguito |
| file degli endpoint | rispettivi computer | repository o immagine solo per contenuti selezionati e dimensionati | censimento e scelta degli oggetti da proteggere aperti |
| dati di laboratorio sacrificabili | nodo di laboratorio | ricostruzione da procedura, salvo dati selezionati | nessuna promessa di conservare tutti gli esperimenti |
| configurazioni di rete e accesso di emergenza | firewall e futuri switch/AP | fascicolo privato leggibile anche senza NAS e server | RETE-01/02 preparate, export e supporto da qualificare |

Il file di configurazione TrueNAS contiene impostazioni e dati sensibili del servizio, mentre il campo Export Password Secret Seed consente il recupero dei valori cifrati della configurazione. Per dataset cifrati vanno comunque conservati fuori macchina anche i materiali di sblocco; una passphrase ZFS non è inclusa nel file. Questa parte si basa sulla documentazione stabile 25.10, non sulla pagina generale che seguiva lo sviluppo di TrueNAS 28. [Esportazione della configurazione](https://www.truenas.com/docs/scale/25.10/scaletutorials/systemsettings/advanced/managesysconfig/).

## Le ipotesi che non diventano decisioni da sole

Non si assegna un'ulteriore macchina fisica, non si compra un disco e non si presume disponibile un abbonamento cloud o un supporto esterno. Il piano può proporre una copia su hardware già previsto, ma deve esplicitare spazio sottratto agli altri usi, dipendenze di recupero e contenuto delle credenziali. La scelta finale degli oggetti irrinunciabili appartiene all'utente; intanto la progettazione prosegue sulle alternative e sui vincoli verificabili.

I salvataggi devono terminare prima dell'arresto programmato del NAS. La finestra accettata resta 07:30-23:30 per le notti da domenica a giovedì e si estende fino alle 02:30 successive per venerdì e sabato. Qui non si cambia la decisione: si deve collocare il lavoro al suo interno, con controllo dei ritardi e senza spegnere una destinazione ancora in scrittura. Il [documento sui consumi](../02-storage-di-rete-nas/05-consumo-elettrico-e-finestra-di-accensione.md) distingue la scelta di accensione dalle stime elettriche sul vecchio hardware, ancora da misurare alla presa.

## Come si usa il piano

Si parte dal [dimensionamento](03-dimensionamento-e-scenari-di-backup.md), si sceglie un perimetro sostenibile e si prepara la [procedura della macchina interessata](04-procedure-di-backup-e-ripristino.md). [Permessi, finestre e collaudo](05-permessi-finestre-e-collaudo.md) definisce chi può leggere e scrivere, i flussi ancora mancanti e come misurare il recupero. Gli endpoint hanno percorsi distinti per [immagine Windows](01-veeam-agent-for-windows.md) e [file selezionati con restic](06-salvataggio-dei-file-con-restic.md). Il [modello di verbale](07-modello-di-verbale-di-collaudo.md) raccoglie atteso, osservato, esclusioni e tempi.

Il piano distingue fonte primaria letta, proposta specifica del laboratorio, verifica locale del modello e collaudo sulle macchine. Al 20/10 i primi livelli hanno risultati tracciati; il collaudo è aperto. La prima attivazione procede con dati artificiali e poi con il perimetro reale autorizzato, senza compromettere gli originali per provare un recupero.

Il [fascicolo di emergenza della rete](08-fascicolo-di-emergenza-della-rete.md) copre la dipendenza dai percorsi di gestione e dalla configurazione di firewall, switch e access point. Il dimensionamento comprende ora anche uno scenario per lo spazio sottratto ai guest dalla copia dei documenti NAS sul server: la capacità di quella destinazione non si presume illimitata perché il suo mirror è più grande.
