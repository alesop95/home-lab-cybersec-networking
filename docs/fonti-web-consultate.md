# Fonti web consultate, per sessione

> Registro delle fonti esterne consultate durante il lavoro, con la data e l'affermazione che ciascuna sostiene. Nasce dal principio già enunciato in [Fonti e materiali del progetto](fonti-e-materiali.md): le affermazioni ancorate a un indirizzo di documentazione ufficiale sono verificate, quelle senza ancoraggio sono ragionamenti plausibili che nessuno ha messo alla prova. Questo file rende quell'ancoraggio consultabile invece che implicito, così che chi rilegge una scheda tecnica possa risalire a che cosa la sostiene e con quale grado di affidabilità.

## Come si legge, e i tre gradi di affidabilità

Non tutte le fonti valgono lo stesso, e mescolarle sarebbe il modo più rapido di svuotare di senso questo registro. Le fonti sono quindi classificate in tre gradi, e il grado va tenuto presente quando si cita l'affermazione a valle.

Il grado *ufficiale* è la documentazione del produttore dell'apparato o del software: un manuale di scheda madre, la documentazione di una release, un file di somme di controllo pubblicato accanto al proprio artefatto. È l'unico grado su cui si può fondare un'affermazione presentata come fatto.

Il grado *comunità* è una segnalazione riportata su un forum o una lista di sviluppo. Vale come indizio di un problema reale, e vale di più quando più segnalazioni indipendenti convergono sullo stesso componente, ma non è una specifica: descrive che a qualcuno è accaduto, non che accadrà.

Il grado *commerciale* è un listino, una scheda prodotto di un rivenditore o un comparatore di prezzi. Documenta un prezzo e una disponibilità a una data, ed è la classe di informazione che decade più rapidamente: si cita per orientare una spesa, mai per fondare un'affermazione tecnica.

## Sessione del 01-02/09/2026, consolidamento di quattro desktop in un NAS

Le fonti seguenti sostengono la scheda [Consolidamento di quattro desktop dismessi in un NAS](03-spunti-di-sviluppo/02-storage-di-rete-nas/03-consolidamento-di-quattro-desktop-dismessi-in-un-nas.md) e la [Guida all'assemblaggio e all'installazione di TrueNAS](03-spunti-di-sviluppo/02-storage-di-rete-nas/04-guida-assemblaggio-e-installazione-truenas.md).

### Manuale della scheda madre — grado ufficiale

| Fonte | Che cosa sostiene |
|---|---|
| [Manuale ASUS H170-PRO, E12046 V2](https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/H170-PRO/E12046_H170-PRO_UM_V2_WEB.pdf) | Un dispositivo M.2 in modalità PCIe non sottrae porte SATA, mentre uno in modalità SATA lascia utilizzabile la sola `SATA_2`. Configurazione degli slot: un x16 a x16, un x16 a massimo x4, due x1, due PCI legacy. Memoria dichiarata DDR4 2133 MHz, non-ECC senza buffer, tetto 64 GB, e limitazione del chipset che riporta a 2133 anche i moduli certificati per frequenze superiori in profilo XMP. Raccomandazione di raffreddamento più efficiente a pieno carico di quattro moduli. Raccomandazione di moduli con la stessa latenza CAS e dello stesso codice data. Mappatura in doppio canale della dimensione del canale minore, con l'eccedenza del canale maggiore in canale singolo. |

È la fonte che ha smentito un sospetto invece di confermarlo, e per questo vale citarla per prima: si temeva che l'alloggiamento M.2 sottraesse la porta SATA destinata al disco di avvio, e il manuale ha escluso il problema per i dispositivi NVMe.

### Versioni e stato del software — grado ufficiale

| Fonte | Che cosa sostiene |
|---|---|
| [Note di versione TrueNAS 25.10 Goldeye](https://www.truenas.com/docs/scale/25.10/gettingstarted/versionnotes/) | La serie 25.10 e le sue caratteristiche |
| [Stato del software TrueNAS](https://www.truenas.com/docs/softwarestatus/) | Quale release è raccomandata per una installazione nuova |
| [TrueNAS 25.10.2 Goldeye](https://www.truenas.com/blog/truenas-25-10-2-goldeye/) | La 25.10 porta OpenZFS 2.3.4 |
| [TrueNAS 25.10-RC1](https://www.truenas.com/blog/truenas-25-10-rc1-features/) | OpenZFS 2.3.4 e l'estensione *ZFS File Rewrite*, sviluppata da TrueNAS sopra OpenZFS 2.3.3, che riscrive dataset e file per allinearli a un assetto di vdev cambiato, utilizzabile per ribilanciare dopo l'aggiunta di un vdev o un'espansione raidz |
| [Installazione di TrueNAS](https://www.truenas.com/docs/scale/25.10/gettingstarted/install/installingscale/) | Procedura di installazione |
| [Gestione dei pool](https://www.truenas.com/docs/scale/25.10/scaletutorials/storage/managepoolsscale/) | Per estendere un pool aggiungendo un vdev, il vdev nuovo deve essere dello stesso tipo di quelli esistenti |
| [Compiti di verifica dell'integrità](https://www.truenas.com/docs/scale/scaletutorials/dataprotection/scrubtasksscale/) | La soglia predefinita è di trentacinque giorni e la verifica gira solo se dall'ultima è passato più tempo della soglia |
| [Mirroring dell'insieme di avvio](https://www.truenas.com/docs/core/13.0/coretutorials/systemconfiguration/mirroringthebootpool/) | Le sole configurazioni supportate sono un dispositivo singolo oppure due in mirror, e un dispositivo aggiunto a posteriori deve avere capacità almeno pari a quella dell'esistente |
| [Piani TrueNAS per il 2026](https://www.truenas.com/blog/truenas-plans-for-2026/) | Cadenza annuale e numerazione semplificata a partire dalla 26 |
| [TrueNAS 26 beta 1](https://www.truenas.com/blog/blog-truenas-26-beta1-release/) | La 26 *Halfmoon* è in beta da aprile 2026 |

La fonte sulla soglia di trentacinque giorni ha corretto un'affermazione già scritta e committata, che dava le verifiche periodiche come non attive per impostazione predefinita. La correzione non è cosmetica: chi crede che manchino ne crea una seconda, sovrapposta alla prima.

La fonte sull'insieme di avvio è quella con la conseguenza operativa più immediata di tutto il registro, perché i due dischi disponibili hanno capacità diverse e l'ordine di installazione determina se il mirror sarà possibile o richiederà di reinstallare.

### Versioni e stato del software — grado comunità e stampa tecnica

| Fonte | Che cosa sostiene |
|---|---|
| [OSTechNix, TrueNAS 26 beta](https://ostechnix.com/truenas-26-beta-released/) | La 26 porta OpenZFS 2.4 |
| [Phoronix, TrueNAS 26 beta](https://www.phoronix.com/news/TrueNAS-26-Beta) | Linux 6.18 LTS e OpenZFS 2.4 nella 26 |
| [The Register, espansione raidz in OpenZFS 2.3](https://www.theregister.com/2025/01/23/openzfs_23_raid_expansion/) | L'espansione di un vdev raidz un disco alla volta è arrivata con OpenZFS 2.3 |

### Affidabilità del controller di rete integrato — grado comunità

Questa è la parte del registro dove il grado conta di più, perché l'affermazione a valle è una raccomandazione di spesa e non un fatto di specifica. Nessuna documentazione ufficiale dichiara inadatto il controller integrato: le fonti sono segnalazioni, e il loro peso viene dalla convergenza su uno stesso componente sotto uno stesso carico.

| Fonte | Che cosa sostiene |
|---|---|
| [Realtek 8111H su TrueNAS SCALE](https://www.truenas.com/community/threads/realtek-8111h-on-truenas-scale.107268/) | Segnalazioni sul chip RTL8111H specificamente sulla base Linux, non su quella FreeBSD |
| [RTL8111/8168/8411 instabile ad alte velocità di trasferimento](https://www.truenas.com/community/threads/fixed-realtek-rtl8111-8168-8411-flapping-on-high-transfer-rates.107797/) | Il collegamento cade e risale sotto trasferimenti prolungati a piena velocità |
| [Aggiornamento del driver Realtek su TrueNAS 12 per prevenire il watchdog timeout](https://www.truenas.com/community/threads/truenas-12-and-realtek-updating-your-driver-to-1-96-to-prevent-re0-watchdog-timeout.88806/) | Il problema storico sulla base FreeBSD, con il driver `re` |
| [Segnalazione di instabilità del driver r8169 sulla lista del kernel Linux](https://lkml.iu.edu/1801.1/05775.html) | Il driver Linux `r8169` è stato oggetto di segnalazioni di instabilità |

Il valore di queste fonti prese insieme è di avere smentito un'ipotesi comoda: si potrebbe pensare che l'avversione per questi controller appartenga all'epoca FreeBSD e sia superata dal driver Linux mainline. Le segnalazioni sulla base Linux, e in particolare quella su un passaggio da FreeBSD a Linux fatto proprio per risolvere crash sotto carico e rimasto senza esito, indicano che l'ipotesi non regge. Resta una raccomandazione fondata su indizi convergenti, non su una specifica, e per questo la scheda la accompagna con una prova di collaudo che la mette alla prova sul posto invece di darla per assodata.

### Origine dei binari e loro verifica — grado ufficiale

| Fonte | Che cosa sostiene |
|---|---|
| [memtest.org](https://www.memtest.org/) | Sito ufficiale di Memtest86+, libero sotto GPL v2, distinto da MemTest86 di PassMark che dal 2013 è software chiuso freemium. Versione 8.10 del 16/05/2026, e i nomi dei file distribuiti |
| [Release v8.10 di memtest86plus su GitHub](https://github.com/memtest86plus/memtest86plus/releases) | Corrobora versione e data della release, ma non pubblica binari né somme di controllo |
| [Cartella di download di TrueNAS 25.10.4](https://download.truenas.com/TrueNAS-SCALE-Goldeye/25.10.4/) | Nomi e dimensioni esatti dei file: `TrueNAS-SCALE-25.10.4.iso` di 2,26 GB e `TrueNAS-SCALE-25.10.4.iso.sha256` di 64 byte |
| [Somma di controllo pubblicata dell'ISO 25.10.4](https://download.truenas.com/TrueNAS-SCALE-Goldeye/25.10.4/TrueNAS-SCALE-25.10.4.iso.sha256) | La somma attesa, usata come riscontro indipendente dal file scaricato insieme all'immagine |

La distinzione fra le ultime due voci è il motivo per cui esistono entrambe. Confrontare l'immagine scaricata con il file di somme scaricato accanto ad essa prova soltanto che i due sono coerenti fra loro: se entrambi fossero stati alterati o troncati nello stesso trasferimento, il confronto passerebbe comunque. Il riscontro che chiude il cerchio è rileggere la somma dalla fonte in una richiesta separata, ed è quello che rende la verifica indipendente invece che circolare.

Su Memtest86+ questo riscontro **non è disponibile**: il sito ufficiale non pubblica somme di controllo accanto ai file, la release su GitHub non pubblica artefatti, e l'installer per Windows **non è firmato digitalmente**. L'assicurazione disponibile si riduce quindi al trasporto cifrato dal dominio ufficiale e alla corrispondenza fra la versione dichiarata dal sito e quella della release pubblica. È una lacuna che va dichiarata e non aggirata; la circostanza che la attenua è che quel programma gira prima di qualunque sistema operativo, non monta e non scrive dischi, e opera sulla sola memoria.

### Prezzi e disponibilità dei componenti da acquistare — grado commerciale

Queste voci documentano un prezzo a una data e decadono rapidamente. Servono a orientare una spesa, e vanno ricontrollate al momento dell'acquisto invece di essere citate come se fossero stabili.

| Fonte | Che cosa sostiene, al 02/09/2026 |
|---|---|
| [GLOTRENDS PA05, pagina del produttore](https://www.glotrends-store.com/products/pa05) | Il modello è dichiarato *without bracket*, cioè senza staffa, pensato per case compatti e rack di due unità |
| [Adattatore AMPCOM su Amazon.it](https://www.amazon.it/AMPCOM-Adattatore-SSD-Express-PCIe/dp/B0876MLNY6) | Candidato per l'adattatore da M.2 NVMe a PCIe |
| [Comparatore, adattatori M.2 PCIe NVMe](https://www.trovaprezzi.it/prezzo_altro-informatica_adattatore_m.2_pcie_nvme.aspx) | Fascia di prezzo degli adattatori, circa 12-18 euro |
| [Comparatore, schede di rete Intel I210](https://www.trovaprezzi.it/prezzo_schede-rete_intel_i210.aspx) | Fascia di prezzo delle schede con chip Intel I210, circa 44-72 euro |
| [Intel I210T1 su Amazon.it](https://www.amazon.it/Intel-%C2%AE-I210T1-Scheda-rete/dp/B00C3S791U) | Candidato per la scheda di rete |
| [Scheda con chip Intel i210, Amazon.it](https://www.amazon.it/Gigabit-Intel-Converged-Network-Adapter-Ethernet/dp/B073F51FHT) | Candidato alternativo |
| [10Gtek I210-T1 su Amazon.it](https://www.amazon.it/10Gtek%C2%AE-I210-T1-Gigabit-Ethernet-singola/dp/B01H6O7TMO) | Candidato alternativo |

Il comparatore sulle schede di rete ha corretto una stima sbagliata scritta in una versione precedente della guida, che indicava circa quindici euro per una scheda con chip Intel. La fascia reale è tre volte tanto, e la conseguenza non è soltanto di budget: a quindici euro si acquista un prodotto che dichiara Intel senza esserlo, il che vanifica la ragione stessa dell'acquisto.

## Manutenzione di questo registro

Una fonte si aggiunge quando viene consultata, non a posteriori quando serve giustificare un'affermazione: la ricostruzione tardiva è il modo con cui un registro di fonti diventa una bibliografia decorativa. Si annota l'indirizzo, il grado e che cosa quella fonte sostiene concretamente, non l'argomento generico di cui tratta.

Le voci di grado commerciale portano una data e vanno considerate scadute dopo poche settimane. Non si cancellano, perché documentano su che base è stata presa una decisione di spesa in quel momento, ma non si citano come attuali.

Quando una fonte smentisce un'affermazione già scritta nel repository, la smentita si annota qui accanto alla fonte e la correzione si applica al documento. Le tre occasioni in cui è accaduto in questa sessione sono segnalate nel testo sopra, e sono la ragione principale per cui questo registro vale il suo costo: senza di esso, un'affermazione corretta e una mai verificata hanno lo stesso aspetto.
