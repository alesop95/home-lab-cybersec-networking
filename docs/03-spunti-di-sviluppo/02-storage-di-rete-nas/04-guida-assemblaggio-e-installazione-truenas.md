# Guida all'assemblaggio e all'installazione di TrueNAS

> Guida operativa da eseguire al banco. Presuppone le decisioni prese nella scheda di analisi, [Consolidamento di quattro desktop dismessi in un NAS](03-consolidamento-di-quattro-desktop-dismessi-in-un-nas.md), a cui rimanda per il perché di ogni scelta: qui c'è la sequenza, là il ragionamento. Le macchine hanno i segnaposto di quella scheda, `PC-DESKTOP-A` è la base e `PC-DESKTOP-B`, `linux-desktop-A` e `linux-desktop-B` sono quelle da cui si prelevano i componenti.

## Stato di questo documento

Progetto, non verbale. Nulla di quanto segue è stato eseguito. Le affermazioni sull'hardware sono verificate sul manuale del costruttore e quelle sul software sulla documentazione di TrueNAS alla data del 01/09/2026; le versioni vanno riverificate al momento dell'installazione, perché un ciclo di rilascio annuale le muove.

A valle dell'esecuzione va scritto un verbale separato, sul modello di [verbale-installazione-opnsense.md](../../verbale-installazione-opnsense.md), che racconti cosa è realmente accaduto. Questa guida non va corretta a posteriori per farla combaciare con l'esito: le due cose hanno funzioni diverse, e un progetto riscritto per assomigliare al risultato perde il valore di documento di previsione.

## Quale TrueNAS, e una precisazione sul nome

La scelta di TrueNAS resta quella giusta per questo caso, e la ragione è una sola: ZFS[^1], con le somme di controllo su dati e metadati, le istantanee non costose e la verifica periodica dell'integrità dell'intero pool. È la differenza fra accorgersi di un bit corrotto e scoprirlo tre anni dopo aprendo un file. Le alternative restano valide per obiettivi diversi, e la scheda di analisi le confronta.

Va però corretta la denominazione, perché è cambiata. Il suffisso *SCALE*, che distingueva la variante Linux da *CORE* su FreeBSD, è stato dismesso: il prodotto si chiama TrueNAS, nelle edizioni Community ed Enterprise, e cercare "TrueNAS SCALE" oggi porta a documentazione di versioni precedenti.

| Versione | Stato al 01/09/2026 | Uso |
|---|---|---|
| TrueNAS 25.10 *Goldeye* | stabile, raccomandata per nuove installazioni | ✅ questa |
| TrueNAS 26 *Halfmoon* | beta da aprile 2026, apre la cadenza annuale e la numerazione semplificata | non su una macchina che deve custodire dati |

La 25.10 porta OpenZFS 2.3.4, e questo risolve una riserva che la scheda di analisi lasciava aperta. L'espansione di un vdev[^2] raidz un disco alla volta è disponibile, e insieme c'è *ZFS File Rewrite*, un'estensione sviluppata da TrueNAS che riscrive i dati già presenti per allinearli al nuovo assetto del vdev. La seconda risolve il limite storico della prima: dopo un'espansione i dati vecchi conservavano il rapporto di parità precedente finché non venivano riscritti, e ora esiste un comando che li ribilancia. La conseguenza pratica è che non serve più acquistare tutti i dischi in una volta.

## Che cosa avere in mano prima di cominciare

| Cosa | Nota |
|---|---|
| Adattatore PCIe verso M.2 NVMe | la scheda base ha un solo alloggiamento M.2 e vanno montati due NVMe |
| Scheda di rete Intel gigabit PCIe | la Realtek integrata resta come seconda interfaccia |
| Chiavetta USB da almeno 8 GB | per l'immagine di installazione, il cui contenuto viene distrutto |
| Immagine di TrueNAS 25.10 e la sua somma di controllo | la somma va confrontata, non solo scaricata |
| Immagine di `memtest86+` avviabile | serve per il test che precede l'installazione |
| Un cacciavite a croce e una superficie non conduttiva | |
| Etichette e un pennarello | per i componenti che finiscono in scorta |

Un elemento che la scheda di analisi non nomina e che va valutato adesso, perché condiziona il montaggio: un gruppo di continuità. Questa macchina è stata scelta al posto di un'altra proprio per la capacità di riaccendersi da sola dopo un'interruzione di corrente, il che ammette implicitamente che le interruzioni accadano. ZFS regge bene una perdita di alimentazione, perché le scritture sono transazionali e non lascia un file system in stato incoerente, ma reggere non è la stessa cosa che non subire: una scrittura in volo si perde comunque, e su una macchina senza memoria a correzione d'errore ogni evento elettrico anomalo è un'occasione in più di corruzione silenziosa. TrueNAS parla con i gruppi di continuità e sa spegnersi in modo ordinato quando la batteria scende. Non è un prerequisito dell'assemblaggio e non blocca nulla, ma è la spesa con il miglior rapporto fra costo e rischio evitato dopo i dischi.

## Fase 1, prima di aprire i case

Le due macchine Linux si possono spegnere e formattare soltanto se il loro salvataggio è stato *ripristinato*, non soltanto prodotto. Un archivio mai riletto non è un backup ma una speranza, e la differenza si scopre nel momento peggiore. Sulle due macchine Windows va confermato che non ci sia nulla da conservare.

Le licenze Windows delle due macchine sono di tipo OEM e legate alla scheda madre: non si spostano con i componenti. È irrilevante, perché sulla base andrà TrueNAS, ma va saputo prima di sperare di recuperarle.

Si etichettano i quattro case prima di spegnerli, mentre è ancora ovvio quale è quale, e si scollega l'alimentazione di tutti e quattro. Scollegare, non solo spegnere: su un alimentatore ATX moderno la scheda resta alimentata anche a macchina spenta, e lavorare su una scheda sotto tensione di standby è il modo più comune di uccidere un componente.

## Fase 2, i prelievi

Da `PC-DESKTOP-B` si prelevano i due moduli di memoria da 8 GB e l'SSD SATA. Da `linux-desktop-A` e da `linux-desktop-B` si preleva un NVMe da 1 TB ciascuna, dall'alloggiamento M.2. Facoltativamente si recupera un masterizzatore, che su un NAS serve raramente ma non costa niente.

Prima di estrarre i moduli di memoria conviene fotografare la loro posizione. Sulle schede a quattro alloggiamenti il doppio canale richiede le coppie in posizioni alterne, e montarle affiancate dimezza la banda senza dare nessun errore: la macchina parte, funziona, ed è lenta per una ragione che nessuno vede.

Un NVMe si estrae svitando la vite di fermo e sollevandolo: la scheda si alza da sola per effetto della molla del connettore, e non va tirata. Se scalda ancora, conviene attendere.

## Fase 3, il montaggio sulla base

I quattro moduli da 8 GB vanno nei quattro alloggiamenti. Sono dello stesso codice prodotto, quindi la questione delle coppie non si pone come compatibilità ma solo come posizione, e con tutti e quattro occupati non c'è scelta da fare. Al primo avvio il firmware deve dichiarare trentadue gigabyte in doppio canale.

I due SSD SATA vanno su due porte SATA qualsiasi. Il manuale della scheda conferma che un dispositivo M.2 in modalità PCIe, cioè un NVMe, non sottrae nessuna porta SATA: la contesa riguarda i soli M.2 in modalità SATA. Tutte e sei restano quindi disponibili, e questo è ciò che rende possibile tenere due dischi per l'avvio e lasciare posto ai meccanici.

Il primo NVMe va nell'alloggiamento M.2 della scheda. Il secondo va sull'adattatore, e l'adattatore nel secondo slot x16, quello nero, che opera a x4: sono esattamente le quattro corsie che un NVMe utilizza, quindi nulla è sprecato e lo slot a x16 pieno resta libero. La scheda di rete Intel va su uno slot x1, perché un collegamento gigabit non chiede di più.

| Slot | Larghezza reale | Destinazione |
|---|---|---|
| `PCIEX16_1` | x16 | libero |
| `PCIEX16_2` | max x4 | adattatore PCIe verso M.2 |
| `PCIEX1_1` | x1 | scheda di rete Intel |
| `PCIEX1_2` | x1 | libero |

Prima di chiudere il case conviene contare gli slot fisicamente utilizzabili invece di fidarsi del conteggio del firmware. Il firmware elenca gli slot che esistono elettricamente, non quelli che un dissipatore, un fascio di cavi o una gabbia dischi rendono raggiungibili.

## Fase 4, il firmware

Si entra nel firmware al primo avvio e si verifica quanto segue prima di installare qualsiasi cosa.

| Voce | Valore | Perché |
|---|---|---|
| Memoria rilevata | 32 GB, doppio canale | se dichiara 16 o canale singolo, i moduli sono nella posizione sbagliata |
| Dischi rilevati | 2 SSD SATA e 2 NVMe | un NVMe assente indica l'adattatore non inserito a fondo |
| `Intel Virtualization Technology` | Enabled | serve se un domani si vorranno container o macchine virtuali sulla stessa macchina |
| `Secure Boot` | Disabled | TrueNAS non è firmato dalla catena che il firmware verifica per default |
| Boot mode | UEFI | la base ha firmware UEFI, e usarlo evita la classe di difetti che ha squalificato `linux-desktop-B` |
| `Restore on AC Power Loss` | Power On | ✅ **è il requisito per cui questa macchina è stata scelta** |
| Ordine di avvio | il futuro dispositivo di avvio per primo | dopo l'installazione, uno dei due SSD SATA |

La frequenza della memoria non va cercata. Il manuale dichiara DDR4 a 2133 MHz e precisa che per limitazione del chipset i moduli certificati per frequenze superiori girano comunque al massimo a 2133, anche nel profilo di overclock. I moduli disponibili sono certificati 2400 e gireranno a 2133: è il comportamento corretto, non un difetto da correggere, e non esiste un'impostazione che lo cambi.

Nella stessa schermata si trova la conferma di un limite di piattaforma che vale conoscere: la scheda supporta memoria non-ECC senza buffer, quindi l'assenza di memoria a correzione d'errore non dipende dal processore scelto ma dalla scheda, e nessuna sostituzione di CPU la introdurrebbe. È la ragione per cui la fase successiva non è opzionale.

## Fase 5, i test, che precedono l'installazione

Questa è la fase che si salta più volentieri e che costa di più saltare. Su ZFS senza memoria a correzione d'errore un modulo difettoso corrompe i dati in silenzio: le somme di controllo di ZFS certificano fedelmente ciò che la memoria ha consegnato loro, quindi un dato già corrotto in memoria viene scritto su disco con una somma di controllo perfettamente valida e nessun allarme scatta mai. La verifica periodica dell'integrità non lo troverà, perché dal punto di vista del disco quel dato è corretto.

Si avvia `memtest86+` da chiavetta e si lascia girare almeno un ciclo completo, meglio una notte intera. I quattro moduli sono usati e provengono da due macchine diverse, il che li rende il componente statisticamente più sospetto di tutto l'assemblaggio. Se emerge un errore si isola il modulo responsabile escludendone uno per volta, e si scarta: ventiquattro gigabyte sani valgono più di trentadue con un modulo marcio, e su questa piattaforma non c'è nessun meccanismo che compensi.

Sui dischi si lancia il test SMART[^3] lungo, che percorre l'intera superficie e richiede alcune ore, e si rilegge l'esito a test concluso.

```bash
sudo smartctl -t long /dev/sdX
sudo smartctl -a /dev/sdX
```

I valori attesi sono noti dal censimento e servono come riferimento: i due SSD SATA hanno usura dichiarata nulla e circa diciannovemila ore di accensione, i due NVMe risultavano superare l'autodiagnosi. Un valore peggiorato rispetto al censimento è più informativo del valore assoluto.

## Fase 6, l'installazione

Si scrive l'immagine sulla chiavetta e si confronta la somma di controllo pubblicata con quella del file scaricato. È un gesto di trenta secondi che protegge dalla classe di problemi più difficile da diagnosticare, cioè un'installazione che riesce e si comporta in modo inspiegabile.

Nella schermata di scelta del dispositivo di installazione si selezionano **entrambi** gli SSD SATA, non uno. L'installatore accetta più dispositivi di avvio e ne costruisce un mirror, che usa la capacità del minore dei due, e la configurazione supportata è esattamente un disco solo oppure due in mirror.

L'ordine conta, e sbagliarlo costa una reinstallazione. L'operazione di aggancio di un secondo disco all'insieme di avvio, eseguita dopo l'installazione, pretende che il disco nuovo sia almeno grande quanto quello esistente. I due SSD disponibili hanno capacità diverse, circa 224 e circa 233 gigabyte: installare sul maggiore e poi tentare di agganciare il minore **non funziona**. Selezionare entrambi dall'inizio evita del tutto il problema; se per qualche ragione si installa su un disco solo, si installa sul più piccolo, così che il maggiore resti agganciabile.

L'insieme di avvio non va usato per i dati. Tenere l'avvio separato dai dati è la configurazione corretta e non una precauzione superflua: permette di reinstallare il sistema senza toccare il pool e di importarlo dopo, che è la procedura di ripristino normale di TrueNAS.

A installazione conclusa la macchina espone l'interfaccia di amministrazione via browser sul proprio indirizzo, che la console mostra all'avvio.

## Fase 7, il pool dei dati

È il primo passo che dipende da una decisione ancora aperta, quella sull'acquisto dei dischi, e per questo è collocato qui e non prima: tutto ciò che precede si esegue senza averla presa.

L'architettura corretta mette i dati di massa su dischi meccanici in mirror e riserva i due NVMe, a loro volta in mirror, a un pool separato per le applicazioni in container e le eventuali macchine virtuali. Che siano due e non uno con l'altro di scorta dipende da un dato di fatto verificato: hanno la stessa capacità al byte pur essendo modelli diversi, quindi si specchiano senza spreco, e il guasto di uno non porta via i servizi. Il motivo è che il tetto di questa macchina è un collegamento gigabit, circa centodieci megabyte al secondo, e un singolo disco meccanico moderno lo satura già in sequenziale: la velocità degli NVMe non arriverebbe mai al client, mentre la loro scarsa capacità si sentirebbe subito. Sui carichi a I/O casuale, che sono le applicazioni e le macchine virtuali e non la condivisione di file, gli NVMe fanno invece una differenza reale.

Le tre cose che sui forum vengono raccomandate più spesso e che qui non servono meritano una riga ciascuna, perché evitarle è un risparmio. Una cache di lettura di secondo livello su NVMe serve le letture casuali che la cache in memoria non ha trattenuto, e su un carico in larga parte sequenziale limitato dalla rete non produce nessun guadagno misurabile. Un dispositivo di log delle scritture accelera le sole scritture sincrone, e la condivisione SMB[^4] scrive in asincrono; inoltre un NVMe di fascia consumer, privo di protezione dalla perdita di alimentazione, è il dispositivo sbagliato per quel ruolo proprio perché il suo scopo sarebbe sopravvivere a una perdita di alimentazione. Un vdev speciale per i metadati accelera davvero un pool meccanico, ma diventa parte del pool e la sua perdita è la perdita del pool, quindi va tenuto in mirror, e un terabyte è sovradimensionato di un ordine di grandezza per i metadati di un pool di pochi terabyte.

Sull'acquisto dei dischi resta la trappola che su ZFS è più severa che altrove. I dischi a registrazione sovrapposta, gli SMR[^5], allungano in modo patologico la ricostruzione di un mirror degradato, che è precisamente il momento in cui il pool è vulnerabile e in cui la lentezza si traduce in rischio. Servono dischi a registrazione convenzionale dichiarati tali: le famiglie destinate all'uso continuo li garantiscono, mentre le serie desktop economiche sono spesso a registrazione sovrapposta e non sempre lo dichiarano in evidenza.

Con due dischi la scelta è il mirror, perché raidz1 richiede tre dischi. Grazie all'espansione un disco alla volta e alla riscrittura di ribilanciamento disponibili nella versione corrente, la crescita successiva non richiede di rifare il pool, che era il vincolo su cui la scheda di analisi si esprimeva con cautela.

Un ultimo numero da tenere presente: un pool ZFS degrada sensibilmente oltre l'ottanta per cento di riempimento. La capacità utile da pianificare non è quella nominale, ma l'ottanta per cento di essa.

## Fase 8, dopo il pool

Qui conviene sapere che cosa il sistema fa da sé e che cosa no, perché la ripartizione non è intuitiva.

Alla creazione di un pool viene generato automaticamente un compito di verifica dell'integrità, con cadenza e soglia di trentacinque giorni. Non va creato di nuovo, e crearne un secondo è un errore comune: va guardato, ed eventualmente portato a una cadenza mensile.

Le istantanee periodiche invece non esistono finché qualcuno non le definisce, e sono la metà del valore per cui si è scelto ZFS. Sono anche l'unica difesa pratica contro la cancellazione accidentale e contro un crittolocker che raggiunga una condivisione, perché un'istantanea non è modificabile dal client che la vede.

Le notifiche sono la vera lacuna delle configurazioni predefinite, e vanno configurate per prime fra le cose facoltative. Una verifica che gira regolarmente, trova un errore e non avvisa nessuno equivale a una verifica che non è mai girata: la differenza fra ZFS e un file system ordinario non è che ZFS non perde dati, è che ZFS *sa* di averli persi, e quel sapere ha valore solo se raggiunge una persona.

Le condivisioni si creano su dataset dedicati e non sulla radice del pool, così che le proprietà, le istantanee e le quote si possano definire per condivisione invece che per tutta la macchina.

## Fase 9, quando si può dire che è finito

Non quando la macchina risponde, ma quando ha superato le prove che simulano ciò per cui esiste.

Si stacca l'alimentazione e si verifica che la macchina si riaccenda da sola e che il pool torni disponibile senza intervento: è il requisito che ha determinato la scelta della base, e va verificato invece che assunto. Si stacca uno dei due dischi di avvio e si verifica che la macchina parta comunque, degradata, e che lo dichiari: un mirror non verificato è un mirror presunto. Si legge una condivisione da un client e si misura il transito, aspettandosi di trovare il limite della rete e non quello dei dischi. Si provoca deliberatamente una notifica, per esempio con una soglia abbassata, e si verifica che arrivi a destinazione.

Solo allora si scrive il verbale, e si annota che cosa è andato diversamente da questa guida, perché è quella la parte che vale rileggere.

## Errori che costano un rifacimento

| Errore | Conseguenza |
|---|---|
| Installare sul disco maggiore e agganciare il minore dopo | l'aggancio è rifiutato, serve reinstallare |
| Saltare il test della memoria | corruzione silenziosa che nessuna verifica di ZFS può rilevare |
| Acquistare dischi a registrazione sovrapposta | ricostruzione patologicamente lenta proprio quando il pool è vulnerabile |
| Creare le condivisioni sulla radice del pool | proprietà, istantanee e quote non più separabili per condivisione |
| Creare un secondo compito di verifica dell'integrità | verifiche sovrapposte, perché uno esiste già |
| Non configurare le notifiche | ZFS rileva l'errore e nessuno lo sa |
| Usare l'insieme di avvio anche per i dati | una reinstallazione diventa una perdita di dati |
| Montare i moduli di memoria in posizioni affiancate | metà della banda, senza nessun errore che lo segnali |

[^1]: *ZFS*, Zettabyte File System - file system che unisce in un solo strato la gestione dei volumi e il file system, con somme di controllo su dati e metadati, istantanee non costose e verifica periodica dell'integrità dell'intero pool.

[^2]: *vdev*, virtual device - l'unità di redundanza di ZFS. Un pool è composto da uno o più vdev, e la perdita di un vdev non ridondato comporta la perdita dell'intero pool, non della sola porzione di dati che conteneva.

[^3]: *SMART*, Self-Monitoring, Analysis and Reporting Technology - insieme di contatori e autodiagnosi che un disco espone sul proprio stato di salute; il test lungo percorre l'intera superficie, quello breve solo un campione.

[^4]: *SMB*, Server Message Block - protocollo di condivisione di file usato nativamente da Windows e supportato da Linux e macOS, che scrive in modo asincrono se non gli si chiede diversamente.

[^5]: *SMR*, Shingled Magnetic Recording - tecnica di registrazione che sovrappone parzialmente le tracce per aumentare la densità, a costo di riscritture amplificate che rendono molto lenta la ricostruzione di un array degradato.
