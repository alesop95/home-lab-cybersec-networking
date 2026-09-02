# Consolidamento di quattro desktop dismessi in un NAS

> Studio di fattibilità e progetto di assemblaggio. Quattro postazioni desktop dismesse vengono consolidate in una sola macchina destinata a servire come NAS[^1] domestico su rete gigabit; dalle altre tre si recupera il meglio e il resto resta come scorta funzionante. Il materiale di lavoro con i valori reali, cioè indirizzi, utenze e credenziali delle quattro macchine, vive fuori dall'albero versionato e non è riferito qui: in questa scheda le macchine hanno segnaposto.

## Stato di questo documento

L'analisi è chiusa, le due decisioni di progetto sono prese, l'assemblaggio non è stato eseguito. Il censimento hardware delle quattro macchine è stato raccolto sul campo con due script di sola lettura, uno per Windows e uno per Linux, e le affermazioni sulla scheda base sono state verificate contro il manuale del costruttore invece di essere dedotte. Tutto ciò che riguarda il montaggio, i test di stabilità e l'installazione del sistema è progetto e non stato di fatto.

Il rapporto con il resto del progetto è quello della fase 4 della roadmap, cioè lo storage di rete: questa macchina è l'hardware candidato a coprire quel ruolo. Le quattro postazioni non appartengono alla rete domestica documentata altrove in questo albero, ma provengono da un contesto diverso e dismesso.

## Il parco macchine

Le quattro macchine differiscono in modo che conta, e la differenza decisiva non è la velocità della CPU ma il socket, l'età del firmware e la disponibilità di slot.

| | `PC-DESKTOP-A` | `PC-DESKTOP-B` | `linux-desktop-A` | `linux-desktop-B` |
|---|---|---|---|---|
| Motherboard | ASUS H170-PRO, ATX | ASUS B150-PRO, ATX | ASRock H270M Pro4, mATX | ASUS Z97-P, ATX |
| Chipset | H170, serie 100 | B150, serie 100 | H270, serie 200 | Z97 |
| Firmware | UEFI, AMI 2018 | UEFI con Secure Boot, AMI 2015 | UEFI, AMI 2017 | BIOS legacy, AMI 2015 |
| CPU | i7-6700 Skylake | i7-6700 Skylake | i7-7700 Kaby Lake | i7-4790 Haswell |
| Socket | LGA1151 | LGA1151 | LGA1151 | LGA1150 |
| Virtualizzazione | attiva | disattivata nel firmware | attiva | assente |
| RAM | 16 GB DDR4, 2 moduli | 16 GB DDR4, 2 moduli | 16 GB DDR4, 4 moduli | 16 GB DDR3, 2 moduli |
| Alloggiamenti RAM liberi | 2 | 2 | 0 | 2 |
| Disco | SSD SATA 240 GB | SSD SATA 250 GB | NVMe 1 TB | NVMe 1 TB |
| Rete | Realtek gigabit | Realtek gigabit | Intel gigabit | Realtek gigabit |
| Slot di espansione | 6 | 7, di cui 3 PCI legacy | pochi, formato mATX | non rilevato |
| Porte SATA | 6 | 6 | 6 | 6 |
| Alloggiamenti M.2 | 1 | 1 | 1 | 1 |

Sommando le risorse, il parco offre tre CPU intercambiabili fra loro e una quarta di generazione diversa, quattro moduli DDR4 da 8 GB in due coppie dello stesso codice prodotto più quattro da 4 GB, due NVMe da 1 TB, due SSD SATA con usura dichiarata nulla e circa diciannovemila ore di accensione, e infine due masterizzatori, quattro alimentatori e quattro case.

## Il vincolo che comanda: il socket, non la CPU

La trappola più facile su questo parco è credere che LGA1151 sia una famiglia unica. Non lo è. Le schede di serie 100 e 200, quindi B150, H170 e H270, accettano Skylake e Kaby Lake; le schede di serie 300 accettano solo Coffee Lake e non sono retrocompatibili pur avendo lo stesso numero di pin. Tre delle quattro macchine sono di serie 100 o 200, quindi fra loro CPU e memoria si scambiano; la quarta è LGA1150 con memoria DDR3 e non condivide nulla con le altre.

La conseguenza pratica sui sedici gigabyte della macchina Haswell è che sono irrecuperabili: sono DDR3, e le altre tre schede sono tutte DDR4. Restano scorta per un'eventuale altra macchina della stessa generazione, non per questo progetto.

## Perché la base è `PC-DESKTOP-A`

Due macchine si escludono prima del confronto. `linux-desktop-B` ha un firmware BIOS legacy del 2015 e un difetto di avvio dimostrato: la partizione di avvio si trovava a circa settecentotrenta gigabyte dall'inizio di un NVMe, e ne è derivato in modo intermittente l'errore del boot loader che dichiara di leggere fuori dai limiti del disco. Si manifesta prima che il sistema operativo esista, quindi nessuno script può rimediare. In più la tastiera non risponde né al firmware né al boot loader, pur funzionando dentro il sistema avviato, con cause probabili nell'uso di una porta USB 3.0 invece di una 2.0, nel supporto USB legacy disabilitato o nell'avvio rapido attivo. Per una macchina il cui requisito è ripartire da sola dopo un'interruzione di corrente è squalificante.

`linux-desktop-A` si esclude per una ragione meno drammatica ma decisiva: è in formato mATX con pochi slot, e ha tutti e quattro gli alloggiamenti di memoria occupati da moduli da 4 GB, quindi per salire a trentadue gigabyte andrebbero scartati tutti.

Fra le due ATX di serie 100 la scelta cade sulla H170-PRO per tre ragioni cumulative. Il firmware è del 2018 contro il 2015, cioè tre anni di correzioni e il supporto Kaby Lake già incluso. Il chipset H170 porta più corsie PCIe dal chipset e la tecnologia di storage Intel, che il B150 entry level non ha. E dei sette slot della B150-PRO tre sono PCI legacy, quindi inutilizzabili in pratica, mentre i sei della H170-PRO comprendono quattro PCIe.

Va detto con onestà che la differenza non è drammatica e che la B150-PRO farebbe benissimo da NAS. La scelta della migliore ha senso perché non costa niente, e lascia la seconda come scorta completa e funzionante.

## Che cosa dice il manuale della scheda base

Tre affermazioni sono state verificate sul manuale del costruttore, e due di esse cambiano il piano di montaggio.

La prima riguarda l'alloggiamento M.2 e la sua contesa con le porte SATA, che su molte schede di quella generazione fa sparire una porta. Il manuale dichiara che quando sull'M.2 si installa un dispositivo in modalità PCIe il connettore SATA Express continua a supportare dispositivi sia in modalità PCIe sia SATA, e che la limitazione a una sola porta utilizzabile si presenta soltanto con un dispositivo M.2 in modalità SATA. I due dischi da montare sono NVMe, quindi PCIe: tutte e sei le porte SATA restano disponibili, e questo apre spazio a una configurazione di avvio ridondata che altrimenti non avrebbe avuto posto.

La seconda riguarda gli slot. Il manuale elenca uno slot PCIe 3.0 x16 che opera a x16, un secondo slot di lunghezza x16 che opera al massimo a x4 ed è compatibile con schede x1 e x4, due slot PCIe x1 e due PCI legacy. Il censimento raccolto dal firmware ne enumera quattro, perché salta i PCI, e li segnala tutti disponibili. Ne discende l'allocazione: l'adattatore che porta il secondo NVMe va nel secondo slot x16, che offre esattamente le quattro corsie che un NVMe utilizza e nulla di sprecato, mentre la scheda di rete aggiuntiva va in uno dei due x1, perché un collegamento gigabit non ha bisogno di più.

La terza chiude una porta, e vale saperla chiusa. Il manuale dichiara quattro alloggiamenti di memoria, un tetto di sessantaquattro gigabyte, DDR4 a 2133 MHz e memoria non-ECC senza buffer, e aggiunge che per limitazione del chipset i moduli da 2133 MHz e superiori girano al massimo a 2133 anche nel profilo di overclock. I moduli disponibili sono certificati 2400 e gireranno a 2133, come il censimento delle due macchine di provenienza già conferma leggendo la frequenza effettivamente configurata: non esiste un'impostazione da cercare nel firmware, e cercarla è tempo perso. Soprattutto, la memoria ECC[^2] non è preclusa soltanto dalla CPU, come si potrebbe concludere guardando il listino del produttore del processore: non la supporta la scheda. Su questa piattaforma non esiste percorso verso l'ECC, il che rende definitiva e non provvisoria la scelta descritta più sotto.

## La configurazione bersaglio

| Componente | Provenienza | Nota |
|---|---|---|
| Motherboard H170-PRO | `PC-DESKTOP-A`, resta nel suo case | |
| CPU i7-6700 | già montata, non si sostituisce | vedi il paragrafo seguente |
| 32 GB DDR4 | 16 GB presenti più 16 GB da `PC-DESKTOP-B` | quattro moduli da 8 GB dello stesso codice prodotto |
| SSD SATA di avvio | entrambi gli SSD SATA del parco | in mirror, vedi la sezione dedicata |
| Primo NVMe 1 TB | `linux-desktop-A` | nell'alloggiamento M.2 della scheda |
| Secondo NVMe 1 TB | `linux-desktop-B` | su adattatore PCIe verso M.2, secondo slot x16 |
| Scheda di rete Intel gigabit | acquisto di fascia bassa | su slot PCIe x1; la Realtek integrata resta come seconda |
| Adattatore PCIe verso M.2 | acquisto di fascia bassa | la scheda ha un solo alloggiamento M.2 |

Verrebbe naturale spostare sulla base l'i7-7700, che è la CPU più veloce del parco, e sarebbe uno sbaglio. Il guadagno reale è di due decimi di gigahertz sulla frequenza base e altrettanti sul turbo, cioè nulla per una macchina il cui collo di bottiglia è un collegamento gigabit e non il calcolo. In cambio si introdurrebbe un rischio: il supporto Kaby Lake sulle schede di serie 100 è arrivato con aggiornamenti di firmware, e anche se quello del 2018 quasi certamente lo comprende, verificarlo richiede montare e provare, con la prospettiva di aver smontato tutto per niente. La CPU già installata è compatibile senza verifiche e per servire file è sovradimensionata.

## La tecnologia: TrueNAS SCALE, e ZFS senza ECC

Il confronto è fra tre candidati. TrueNAS SCALE e OpenMediaVault sono gratuiti e aperti, Unraid è a pagamento con abbonamento annuale. La differenza sostanziale non è il prezzo ma il file system: TrueNAS porta ZFS[^3], con somme di controllo da un capo all'altro della catena, istantanee e verifiche periodiche dell'integrità; OpenMediaVault porta ext4 o btrfs sopra il RAID software del kernel; Unraid usa un array proprietario. Il valore di ZFS in un archivio domestico è esattamente la differenza fra accorgersi di un bit corrotto e scoprirlo tre anni dopo aprendo il file.

Il costo è la memoria, e trentadue gigabyte collocano questa macchina nella fascia consigliata invece che al minimo. La curva di apprendimento è più ripida di quella di OpenMediaVault, che è in sostanza un Debian con un'interfaccia di amministrazione: chi preferisce consumi minimi e semplicità sceglie quello, perdendo ZFS e le sue garanzie.

Resta il limite dell'ECC, ed è un limite di piattaforma e non di configurazione. ZFS senza memoria a correzione d'errore funziona, perché l'ECC è una raccomandazione e non un requisito, ma un modulo difettoso corrompe i dati in silenzio e le somme di controllo di ZFS registrano fedelmente ciò che la memoria ha consegnato loro. Da qui l'importanza, in questa configurazione più che in un'altra, del test di memoria descritto nella sequenza di verifica: è l'unica difesa che questa piattaforma consente.

## L'architettura dello storage, e l'errore da non fare

La decisione sulla forma del pool va presa prima di crearlo, perché un vdev in mirror non diventa raidz e da un pool che contiene vdev raidz non si rimuove un vdev.

La tentazione è usare i due NVMe da 1 TB in mirror come archivio principale, ottenendo un terabyte utile. È uno spreco: un singolo disco meccanico moderno satura già un collegamento gigabit, che si ferma attorno ai centodieci megabyte al secondo, quindi le prestazioni dei due NVMe non arriverebbero mai al client. L'architettura corretta mette i dati di massa su due dischi meccanici in mirror, che a pari spesa danno da quattro a dodici terabyte, e riserva gli NVMe a ciò che ne trae davvero vantaggio.

Qui va corretto un luogo comune diffuso. L'NVMe non va usato come cache di lettura di secondo livello, la L2ARC[^4]: quella cache serve le letture casuali che la cache in memoria non ha trattenuto, e su un carico di condivisione file, archivio e contenuti multimediali, in larga parte sequenziale, il tetto resta il collegamento di rete e il guadagno è nullo. Nemmeno come dispositivo di log delle scritture sincrone ha senso, perché la condivisione SMB scrive in asincrono e un NVMe di fascia consumer, privo di protezione dalla perdita di alimentazione, è comunque il dispositivo sbagliato per quel ruolo. L'uso che rende davvero è un pool separato dedicato alle applicazioni in container e alle eventuali macchine virtuali, che sono i carichi a I/O casuale che sui dischi rotanti vanno male, e i due NVMe vi entrano in mirror invece che uno solo con l'altro di scorta. Hanno la stessa capacità esatta al byte pur essendo modelli diversi, quindi si specchiano senza spreco, cosa a cui ZFS non oppone nulla; il mirror non costa niente oltre l'adattatore già previsto, non lascia un disco fermo in un cassetto, e fa sì che il guasto di uno dei due non porti via i servizi. Esiste una terza possibilità, il vdev speciale per i metadati, che accelera realmente un pool meccanico ma ne diventa parte: se muore, muore il pool, quindi va tenuto in mirror, e un terabyte è sovradimensionato di un ordine di grandezza per i metadati di un pool di pochi terabyte.

Va infine ammorbidita l'idea che la scelta iniziale sia irreversibile. I dati si spostano fra pool diversi con gli strumenti nativi di invio e ricezione di ZFS, conservando istantanee e proprietà: partire dagli NVMe non è un vicolo cieco, costa una migrazione da eseguire con entrambi i gruppi di dischi collegati insieme. E l'espansione di un raidz un disco alla volta esiste nelle versioni recenti di OpenZFS, il che cambia il calcolo di quanti dischi acquistare subito; quale versione porti la release di TrueNAS che si installerà è da verificare al momento, e non si assume qui.

Sull'acquisto dei dischi meccanici resta una trappola che su ZFS è severa. I dischi a registrazione sovrapposta, gli SMR[^5], allungano in modo patologico la ricostruzione di un mirror degradato. Servono dischi a registrazione convenzionale dichiarati tali: le famiglie destinate all'uso continuo li garantiscono, le serie desktop economiche spesso no e non sempre lo dichiarano in evidenza.

## Il mirror di avvio, che non costa niente

Il parco contiene due SSD SATA, uno da circa 224 e uno da circa 233 gigabyte, entrambi con stato di salute buono e usura dichiarata nulla. L'installatore di TrueNAS accetta più dispositivi di avvio e ne costruisce un mirror, che utilizza la capacità del minore dei due. Poiché il manuale ha confermato che tutte e sei le porte SATA restano disponibili con gli NVMe montati in modalità PCIe, c'è posto per due dischi di avvio più i meccanici dei dati.

Metterli entrambi costa zero, perché sono già disponibili, e rimuove un punto singolo di guasto da una macchina il cui requisito dichiarato è ripartire da sola dopo un'interruzione di corrente. Tenere il secondo in un cassetto come scorta è l'alternativa peggiore: un disco di scorta richiede che qualcuno si accorga del guasto e intervenga, un mirror no.

## Sequenza di assemblaggio e verifica

L'ordine dei passi non è indifferente, e va notato che la decisione sull'architettura dello storage non blocca nulla di quanto segue tranne l'ultimo punto. Assemblaggio, configurazione del firmware, test di stabilità e installazione del sistema sul mirror di avvio si eseguono tutti prima di aver acquistato i dischi dei dati.

Prima di aprire i case si verifica che le due macchine Linux siano state salvate e che il salvataggio sia stato ripristinato per davvero, non soltanto prodotto, perché un backup non collaudato non è un backup; e si conferma che sulle due macchine Windows non ci sia nulla da conservare. Le licenze Windows delle due sono di tipo OEM e legate alla scheda madre, quindi non si spostano con i componenti: è irrilevante, perché sulla base andrà un sistema Linux. Si etichettano i quattro case prima di spegnerli, e si scollega l'alimentazione.

I prelievi sono due moduli di memoria e l'SSD SATA da `PC-DESKTOP-B`, l'NVMe da ciascuna delle due macchine Linux, e facoltativamente un masterizzatore. Conviene fotografare la posizione dei moduli prima di estrarli, perché sulle schede a quattro alloggiamenti il doppio canale richiede le coppie in posizioni alterne e sbagliarle costa metà della banda di memoria.

Il montaggio sulla base dispone i quattro moduli da 8 GB nei quattro alloggiamenti, i due SSD SATA sulle porte SATA, il primo NVMe nell'alloggiamento M.2, il secondo sull'adattatore nel secondo slot x16 e la scheda di rete Intel su uno slot x1.

Nel firmware si verifica che siano riconosciuti trentadue gigabyte in doppio canale e tutti i dischi, si abilita la virtualizzazione perché è utile se un domani si vorranno container o macchine virtuali sulla stessa macchina, si disabilita il Secure Boot perché il sistema da installare non è firmato dal produttore del sistema operativo desktop, si impone la modalità di avvio UEFI, e soprattutto si imposta il ripristino automatico dell'accensione al ritorno della corrente, che è la ragione per cui questa macchina è stata scelta invece di quella con il firmware legacy.

Il test di stabilità precede l'installazione e non è opzionale, per il motivo detto sopra sull'assenza di ECC. Si esegue almeno un ciclo completo di test della memoria, e meglio una notte intera, perché i moduli sono usati e provengono da due macchine diverse; se emerge un errore si isola il modulo escludendone uno per volta e si scarta, perché ventiquattro gigabyte sani valgono più di trentadue con un modulo guasto. In parallelo si lancia il test SMART lungo su ogni disco e si rilegge l'esito dopo alcune ore.

L'installazione mette il sistema sul mirror dei due SSD SATA, tenendo l'avvio separato dai dati. I due dischi vanno selezionati entrambi già nella schermata di scelta del dispositivo di installazione, e non uno solo con l'intenzione di aggiungere il secondo dopo: l'operazione di aggancio successivo pretende che il disco nuovo sia almeno grande quanto quello esistente, quindi partire dal maggiore dei due renderebbe impossibile agganciare il minore. Se per qualche ragione si installa su un disco solo, si installa sul minore.

Dopo l'installazione si creano le condivisioni e si verifica lo stato dei compiti periodici, ed è qui che conviene sapere cosa il sistema fa da sé e cosa no. Alla creazione di un pool viene generato automaticamente un compito di verifica dell'integrità, con cadenza e soglia di trentacinque giorni: non va creato di nuovo, va guardato, ed eventualmente portato a una cadenza mensile. Le istantanee periodiche invece non esistono fino a quando qualcuno non le definisce, ed è la parte che si dimentica. Restano infine le notifiche sugli errori del pool, che sono la vera lacuna delle configurazioni predefinite: una verifica che gira regolarmente, trova un errore e non avvisa nessuno equivale a una verifica che non è mai girata.

La creazione del pool dei dati è l'unico passo che attende la decisione sull'acquisto dei dischi.

## Che cosa resta come scorta

Dopo l'assemblaggio restano tre sistemi completi. Il primo è una piattaforma Skylake con la B150-PRO e la seconda CPU i7-6700. Il secondo è una piattaforma Kaby Lake con la H270M Pro4, l'i7-7700 e quattro moduli da 4 GB. Il terzo è una piattaforma Haswell con la Z97-P, l'i7-4790 e due moduli DDR3, con il difetto di avvio e la tastiera non funzionante nel firmware documentati sopra. Si aggiungono due masterizzatori, quattro alimentatori, quattro case e le ventole.

Ogni pezzo messo da parte va etichettato con tipo, socket e provenienza. A distanza di mesi nessuno ricorda quale memoria sia DDR3 e quale CPU appartenga a quale socket, e un'etichetta costa meno di una prova di montaggio.

## Pendenze

Restano aperte la decisione sull'acquisto dei dischi meccanici, che condiziona la sola creazione del pool dei dati; il conteggio a case aperto degli slot fisicamente liberi, per escludere un ingombro meccanico che il firmware non vede; e la verifica di quale versione di OpenZFS accompagni la release di TrueNAS al momento dell'installazione, da cui dipende la disponibilità dell'espansione di un raidz un disco alla volta.

[^1]: *NAS*, Network Attached Storage - apparato dedicato che espone spazio disco in rete tramite protocolli standard di condivisione, invece di offrire dischi a un singolo computer.

[^2]: *ECC*, Error Correcting Code - memoria capace di rilevare e correggere la corruzione di un singolo bit, disponibile sulle piattaforme server e su alcune di fascia professionale, non su questa.

[^3]: *ZFS*, Zettabyte File System - file system che unisce la gestione dei volumi e il file system in un solo strato, con somme di controllo su dati e metadati, istantanee non costose e verifica periodica dell'integrità dell'intero pool.

[^4]: *L2ARC*, Level 2 Adaptive Replacement Cache - secondo livello della cache di lettura di ZFS, ospitato su un dispositivo a blocchi, che estende la cache residente in memoria e serve le letture casuali che questa non ha trattenuto.

[^5]: *SMR*, Shingled Magnetic Recording - tecnica di registrazione che sovrappone parzialmente le tracce per aumentare la densità, a costo di riscritture amplificate che rendono molto lenta la ricostruzione di un array degradato.
