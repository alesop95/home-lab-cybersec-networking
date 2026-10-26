# Pendenze aperte

> Documento curato, non generato. Vista consolidata di ciò che nel progetto risulta dichiarato incompleto: sezioni marcate dall'autore come da chiarire, percorsi esplicitamente abbandonati, titoli rimasti segnaposto e verifiche sospese. Non è una fonte: ogni voce punta al file generato che la contiene, e la verità su ciascuna sta lì. Va riletto quando si riprende il progetto, perché è l'unico posto da cui si vede quanto della documentazione è progetto e quanto è stato di fatto.

Rilevazione automatica alla data del 24/08/2026, sull'albero generato dal documento sorgente: cinquanta intestazioni fra sezioni aperte e segnaposto, su un totale di 338 titoli. Il conteggio si riproduce percorrendo le intestazioni dei file sotto `docs/` alla ricerca dei marcatori dell'autore.

## Le tre categorie di marcatore

L'autore ha usato tre convenzioni, che hanno significato diverso e vanno lette diversamente.

Il marcatore `[TBC]`, da chiarire, indica una sezione dove l'analisi è iniziata ma manca una verifica o una decisione. È il marcatore più frequente ed è quello che porta il lavoro residuo vero.

Il marcatore `aborted` indica un percorso valutato e chiuso. Non è lavoro residuo: è una decisione presa, e la sezione resta come traccia del motivo per cui quella strada è stata scartata. Cancellarla farebbe perdere l'informazione più utile, cioè l'alternativa già esclusa.

Il marcatore `not-of-interest-here` indica una parte dell'interfaccia del modem che è stata censita per completezza ma non rileva per il progetto. Non è lavoro residuo neppure questo, ed è segnalato solo perché un lettore che cerca contenuto in quelle sezioni non ne troverà.

A queste si aggiungono i titoli rimasti segnaposto, cioè composti da una lettera ripetuta o da soli punti, che sono strutture predisposte e mai riempite.

## Il vuoto più significativo

La macrosezione `06-progetto-rete-domestica-effettivamente-implementato/` esiste nel sorgente come intestazione con tre sottotitoli segnaposto e nessun contenuto. È la sezione destinata alla rete realizzata, e il fatto che sia vuota è la sintesi più onesta dello stato del progetto: tutto il resto della documentazione è progettazione, confronto fra alternative e censimento, mentre di realizzato c'è l'installazione del sistema operativo del firewall documentata in `verbale-installazione-opnsense.md` e nient'altro.

## Lavoro residuo sul firewall

Sono le pendenze che bloccano il progetto, nel senso che finché non si chiudono la rete non cambia forma. Stanno tutte sotto `03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md`, tranne dove indicato.

| Sezione | Che cosa manca |
|---|---|
| Scan porte ethernet e NIC | identificare quale nome di interfaccia corrisponde a quale connettore fisico, con `pciconf -lv`, `ifconfig` e la verifica a LED, distinguendo la gigabit integrata dalle due schede a 2,5 Gbps |
| L'assignation (segmentazione logica) | assegnare le tre interfacce ai ruoli WAN, LAN e OPT1 poi rinominata DMZ; nella sessione del 16/01/2026 è stata assegnata la sola LAN |
| Scenario con l'operatore che espone IPoE via DHCP | resta ipotesi non confermata; nella topologia adottata il firewall parla con il modem e non con l'ONT, quindi lo scenario diventa rilevante solo se un giorno il modem venisse superato |
| Configurare i parametri delle interfacce | indirizzi delle tre reti, server DHCP interno, verifica che LAN e DMZ non si sovrappongano |
| Due sottosezioni con titolo segnaposto | strutture predisposte e mai riempite, dentro lo stesso file |
| Con una live Ubuntu | percorso abbandonato: la mappatura delle schede si fa dalla console di OPNsense, non da una live esterna, per non introdurre un secondo stack di driver |
| Punti salienti della documentazione per il firewalling | la sezione contiene solo il collegamento alla documentazione ufficiale, senza estrazione |

Si aggiunge una pendenza che non viene dal documento sorgente ma dal verbale fotografico: durante il boot dell'ambiente live è comparso `Generating configuration: templates...failed`, e va riverificato sul sistema installato.

## Lavoro residuo sul lato operatore

Sotto `02-ftth-fastweb/`.

| Sezione | Che cosa manca |
|---|---|
| Topologia della rete teorica | il disegno definitivo, che oggi esiste come descrizione a parole e come diagramma testuale, non come schema |
| Questione fonia VoIP | verificare se le credenziali SIP sono ottenibili; se non lo sono, il modem resta necessario per la fonia e va tenuto come client SIP dentro la LAN |
| Alternativa modem libero | l'ipotesi di attivare un modem di proprietà con procedura dedicata resta aperta, e cambierebbe l'intera topologia eliminando il doppio NAT |
| Seconda lettura dei parametri di interesse | rileggere lo stato WAN quando l'interfaccia in fibra risulta attiva; nella lettura di febbraio 2026 la connessione attiva era quella mobile di backup, quindi i parametri letti non erano quelli della fibra |
| Differenza fra port forwarding ed Exposed Host | domanda posta e non risolta nel sorgente |
| Differenza fra le due DMZ in atto | quella del modem verso il firewall e quella del firewall verso il server; la distinzione è abbozzata ma non chiusa |
| Parametri di interfaccia del modem | la sezione contenitore è marcata da chiarire nel suo insieme |

## Lavoro residuo sui componenti del lab

| Sezione | Che cosa manca |
|---|---|
| `03-spunti-di-sviluppo/13-switch/` | la configurazione dello switch nella rete, cioè quali VLAN, quali porte access e quale trunk verso il firewall |
| `03-spunti-di-sviluppo/12-vpn/` | contestualizzare Tailscale alla rete domestica, e la questione del cambio di profilo sul piano gratuito |
| `03-spunti-di-sviluppo/04-rmm-management-.../` | l'implementazione con IP statico, che è lo scenario diventato attuale dopo l'assegnazione dell'indirizzo fisso; e una verifica su una distribuzione candidata come host |
| `03-spunti-di-sviluppo/02-storage-di-rete-nas/` | compatibilità con un lettore audio via USB, verifica non fatta |
| `03-spunti-di-sviluppo/02-storage-di-rete-nas/` | eventuale acquisto futuro di due dischi CMR da uso continuo in specchio, come secondo pool accanto ai due NVMe: dal 07/10/2026 il NAS parte senza dischi meccanici (ADR-014, ADR-015) e le schede della cartella sono riallineate; resta da fare solo se la capacità di circa 1 TB non basta |
| `03-spunti-di-sviluppo/10-firewall-.../04-...nethsecurity8.md` | alternativa citata e non valutata |

## Lavoro residuo sul censimento dei dispositivi

Sotto `05-analisi-del-caso/01-tbc-studio-dispositivi-domestici.md`, che è marcato da chiarire nel suo insieme. Delle voci presenti, sei postazioni fisse e quattro portatili più console, televisore, telefoni e tablet, molte hanno la sola intestazione e la sottosezione sulle schede di rete lasciata a segnaposto. Le voci con contenuto reale sono la postazione fissa numero quattro, i portatili due e tre, e la console; le altre sono da compilare. Due voci di dispositivo hanno il titolo composto da soli punti, quindi non è possibile sapere a che cosa si riferiscano senza chiederlo all'autore.

Dal 07/10/2026 il censimento ha un obiettivo in più, chiesto dall'utente: per ogni client dire se sarà cablato o resterà in Wi-Fi, e su quale porta o SSID finirà. Si fa per categoria e con i segnaposto nei file tracciati. È anche la misura che dirà se le otto porte dello switch bastano.

Dall'8/10/2026 il metodo è deciso (ADR-021) ed è descritto in `05-analisi-del-caso/02-scheda-dispositivo.md`, con gli strumenti di raccolta. Restano da fare le raccolte, PC per PC, e la prima corsa vera dello script Linux, controllata a campione. Il PC su cui è stato provato lo script Windows è una macchina di sviluppo esterna alla rete domestica, quindi non entra nel censimento.

Il censimento è meno accessorio di quanto sembri: è la fonte che dice quale endpoint può realmente saturare una porta a 2,5 Gbps e quale no, e senza di esso il dimensionamento dello switch e la scelta di dove portare le porte veloci restano decisioni prese a intuito.

Dal 26/10/2026 TAB-02 è identificato come Galaxy Tab S6 Lite (2024) SM-P620. Restano due schermate, da chiedere alla ripresa quando l'utente è a casa, perché i tablet stanno lì. La prima si fa sul tablet della schermata del 26/10, quello intestato a Persona-B: Impostazioni, Informazioni sul tablet, Informazioni software. Dà la versione di Android e il livello delle patch di sicurezza, da cui dipende la scelta fra VLAN 10 e VLAN 40. La seconda si fa sull'altro tablet, TAB-01: Impostazioni, Informazioni sul tablet, cioè la stessa schermata del 26/10. Serve perché la sua edizione 2022 LTE è dichiarata e non letta, ed è anche la sola fonte del rapporto di età fra i due tablet.

## SoundCraft sulla postazione Ubuntu Studio: valutazione e personalizzazione

Aperta il 26/10/2026 su richiesta dell'utente, in attesa di riallineamento. Riguarda `linux-desktop-C`, ma la sede canonica del lavoro sono i progetti gemelli della produzione audio, cioè la documentazione d'ambiente del progetto dei monitor, che la propaga al progetto di home recording. Questo repository riceve soltanto una riga nella scheda della postazione, se il programma ci verrà installato. Prima della personalizzazione restano da decidere che cosa serva davvero ai due progetti e se il fork sia necessario oppure basti un rilascio ufficiale. I dati raccolti il 26/10 sono nel work-log di quel giorno e le fonti sono S194-S197. La stessa voce, con le stesse fonti, è PA-034 nel progetto dei monitor e PA-003 in quello di home recording, così che la ripresa la mostri in tutti e tre i progetti.

## Chiusa il 09/10/2026: foto dell'interno di altri due PC

Aperta l'8/10/2026 e chiusa il giorno dopo. I due PC sono PC-02, con Xubuntu, e PC-03, con anduinOS; le ventidue foto sono nel materiale privato con il loro indice. Da lì discendono ADR-030, ADR-031 e le sezioni del 09/10/2026 del [piano unificato](03-spunti-di-sviluppo/23-studio-home-lab/10-piano-unificato-hardware-e-stack.md).

## PC-02 dismesso e preparazione di PC-03

Aggiornamento del 17/10/2026 su dichiarazione dell'utente e due nuove foto. PC-02 è dismesso e la GeForce 210 è recuperata: resta scorta video non collaudata. Non si chiede più di intervenire sulla macchina dismessa; il lettore DVD non entra nelle scorte certe perché il suo recupero non è confermato. I prelievi principali di dischi, memoria, alimentatore, cavi e minuteria erano già registrati.

PC-03 è attualmente senza SSD secondo l'utente. Il Samsung 850 EVO M.2 SATA da 250 GB era nelle foto del 09/10 e resta destinato al laboratorio, ma non si trova una conferma registrata del prelievo o del rimontaggio: il piano del 09/10 ne prevedeva l'estrazione per il server, cambiata con ADR-033 il 12/10. Localizzare il disco, anche fra i pezzi in un'altra stanza, prima del montaggio. La targa dell'Atlantis è ora letta: P016-MPW-6000-W, 600 W massimi dichiarati, due +12 V da 22 A ciascuno; la voce della lettura della targa è chiusa, la salute elettrica non è misurata. Restano processore, vano da 3,5 pollici, montaggio del disco da 500 GB e dei 16 GB DDR3 di `linux-desktop-B`, poi collaudi. Il Tecnoware resta di scorta (ADR-035). Stato e ragioni in [Allocazione dell'hardware](03-spunti-di-sviluppo/23-studio-home-lab/12-allocazione-dell-hardware.md) e nel [registro del montaggio](03-spunti-di-sviluppo/02-storage-di-rete-nas/09-registro-del-montaggio.md).

## Supporti di montaggio dei dischi da due pollici e mezzo

Dal 09/10/2026: l'utente dichiara di avere probabilmente rotto le slitte e gli adattatori da due pollici e mezzo a tre e mezzo di PC-02, che la sequenza del da farsi prevedeva di riutilizzare. La conseguenza è circoscritta a un disco solo, il Kingston V300, perché il Samsung 850 EVO va nell'alloggiamento M.2 senza supporto e il disco meccanico da 500 GB è da tre pollici e mezzo e usa il montaggio del case che lo ospita. Resta da verificare, aprendo il case di `linux-desktop-A`, se abbia un montaggio proprio per i dischi da due pollici e mezzo, come molti case del 2017; se non ce l'ha serve un adattatore da pochi euro. Un disco non si lascia appoggiato dentro il case: anche senza parti in movimento, può cortocircuitare contro il telaio e sollecita il connettore SATA. Aggiornamento del 14/10/2026: le foto di PC-02 aperto mostrano il Kingston V300 avvitato su un adattatore Corsair da due pollici e mezzo a tre e mezzo che appare integro, quindi il V300 ha già il suo supporto e va in un alloggiamento da tre pollici e mezzo del NAS con le viti laterali, senza fascetta e senza acquisto. Resta da confermare a mano che l'adattatore non abbia alette spezzate e che il case del NAS abbia un alloggiamento da tre pollici e mezzo libero. Aggiornamento del 15/10/2026: una foto del V300 fuori dalla macchina mostra il telaio dell'adattatore integro sui due lati visibili; lo stesso giorno l'utente l'ha scosso a mano: il disco non si muove e la cornice non ha parti rotte. Resta il vano libero nel NAS.

## Memoria e dischi ridistribuiti fra NAS e server: le verifiche al banco

Dal 12/10/2026, conseguenza di ADR-032 e ADR-033, con l'allocazione canonica in [Allocazione dell'hardware](03-spunti-di-sviluppo/23-studio-home-lab/12-allocazione-dell-hardware.md). Le decisioni sono prese, le verifiche no. Sul NAS l'alimentatore deve avere tre connettori SATA, e il Kingston V300 va fissato nel case, dal 14/10/2026 con l'adattatore Corsair su cui è già avvitato; il pool dei dati parte da circa 180 GB pianificabili, e la prima copia reale di una macchina virtuale del server dirà quanto spazio occupano le copie. Sul server la scheda deve vedere i due NVMe insieme nei due alloggiamenti M.2, come dichiara il produttore (S103). Sul NAS il firmware deve dichiarare 16 GB in doppio canale e il test della memoria di una notte deve chiudere senza errori, che è anche la quarta condizione di ADR-016 sull'alimentatore. Aggiornamento del 16/10/2026: al primo avvio il firmware dichiara 16 GB in doppio canale, +12 V a 12,192 V, ventola in funzione e tre dischi visti, quindi di ADR-016 restava il solo test della memoria, che il 16/10/2026 ha trovato un errore singolo dopo quattro passaggi puliti e quasi quattro ore: la condizione non è soddisfatta e i moduli vanno isolati uno per volta prima di installare TrueNAS; prima di creare il pool va confermato che il contenuto del SanDisk, disco di sistema della base, non serve più, e va verificato che Intel Rapid Storage Technology lasci i dischi in AHCI. Il dettaglio è nel [registro del montaggio](03-spunti-di-sviluppo/02-storage-di-rete-nas/09-registro-del-montaggio.md). Sul server Proxmox lo scambio dei moduli si fa al passo 8 della sequenza del banco del [piano unificato](03-spunti-di-sviluppo/23-studio-home-lab/10-piano-unificato-hardware-e-stack.md), e richiede che il firmware dichiari 24 GB in doppio canale e una notte di test pulita, perché i moduli arrivano da due macchine diverse. Collegato, ma di nessuna conseguenza sul NAS: i moduli DDR3 di PC-02 sono quattro e non due; il 15/10/2026 le foto li mostrano tutti fuori dalla macchina, due da 2 GB e due da 4 GB, 12 GB in tutto, e la voce della taglia è chiusa.

Aggiornamento del 26/10/2026 sul collaudo NAS: Stato NAS del 26/10/2026: RAM-03 da sola in A2, 8192 MB a 2133 MHz, AHCI e tre SSD sulle porte 1/2/6 verificati. SystemRescue 8.07 e GSmartControl avviati. Mappa della sessione: /dev/sda SanDisk, /dev/sdb Kingston V300, /dev/sdc WD Blue; /dev/sdd USB. Tutti e tre gli SSD hanno controllo SMART generale PASSED e un autotest esteso documentato: Extended offline, Completed without error, 100%, una voce ciascuno. Test estesi dei tre SSD conclusi positivamente, senza ripetizioni richieste. Restano le schede General dei tre SSD e Attributes di Kingston/WD per firmware e usura; Attributes del SanDisk già acquisita. Dati SanDisk da chiarire prima del pool: domanda inviata il 26/10 e risposta attesa. Accettazione ADR-016 e riallocazione NAS/server ADR-032 ancora aperte. TrueNAS non installato, nessun pool creato. PC-DESKTOP-B conservato come scorta; Crucial non prelevati e RAM-03 da non contare anche sul server. Dettaglio nel [registro del montaggio](03-spunti-di-sviluppo/02-storage-di-rete-nas/09-registro-del-montaggio.md).

## Strategia di backup e ripristino del laboratorio

Aperta il 19/10/2026 nel lavoro autonomo autorizzato durante Memtest. Il [piano operativo](03-spunti-di-sviluppo/05-strategia-di-backup/02-piano-di-backup-e-ripristino-del-lab.md) comprende ora dimensionamento delle due destinazioni con cinque scenari, procedure guest/host/NAS, percorsi restic e Veeam, permessi, finestra proposta, verbale e fascicolo di emergenza della rete. Il NAS ha un piccolo specchio SATA 240/250 GB contro lo specchio NVMe da 1 TB previsto per il server: dati reali, dimensioni e ripristini non sono verificati. Le etichette GB/GiB del budget canonico sono state riconciliate il 20/10; il calcolo usa la proposta esplicita di 180 GB decimali e lo spazio del pool resta da misurare. Da assegnare quota sul server per copia distinta dei documenti NAS, supporto e custodia del fascicolo di emergenza, copia scollegata/fuori sede, perimetro endpoint e percorsi cloud T7/T7 Shield. Il contratto di rete richiede un alias PVE_HOST con indirizzo da riservare, TCP 445 da PVE in VLAN 99 al NAS dati e accessi amministrativi specifici TCP 8006; nessuna regola è applicata. Metodo coerente di salvataggio host, recupero in sola lettura e coordinamento con lo spegnimento richiedono verifica prima dell'attivazione. Il confronto documentale con PBS è pronto: eventuale adozione, risorse, datastore, manutenzioni e prova di recupero senza il vecchio nodo restano da valutare su misure reali. Nessuna pendenza operativa è chiusa dalla sola progettazione.

## Modello linguistico locale su CPU: la misura sul nodo di laboratorio

Dal 13/10/2026, studio in [Modello linguistico locale su CPU](03-spunti-di-sviluppo/23-studio-home-lab/13-modello-linguistico-locale-su-cpu.md). La collocazione è decisa dall'utente (ADR-034): colibri sul nodo di laboratorio a 32 GB, VLAN 60, alternato all'analisi dei campioni. La procedura con i comandi è nella sezione «La misura, passo per passo» dello studio. Aperta finché non si misurano, a nodo assemblato, i token al secondo di Qwen3.6-35B-A3B a cache calda, l'attesa su un prompt di 512 token, la memoria residente e il consumo alla presa durante l'inferenza, contro la soglia fissata nello studio: almeno 2 token al secondo e meno di tre minuti di attesa. Le velocità scritte oggi sono stime. Dipende dal processore di PC-03, che deve avere AVX2, e da un'apertura a tempo della VLAN 60 per lo scaricamento se la misura si fa a rete nuova già attiva.

## Studio futuro: espansione del modello linguistico locale con una GPU

Dal 13/10/2026, deciso dall'utente senza data. Va scritto in un documento a sé quando lo si vorrà affrontare. Le domande sono già elencate nella sezione «Lo studio futuro» dello [studio sul modello locale](03-spunti-di-sviluppo/23-studio-home-lab/13-modello-linguistico-locale-su-cpu.md): dove montare la scheda, se l'alimentatore del nodo la regge, quanta memoria video serve, quanto costa all'acquisto e in corrente, e se basti a superare la soglia nel caso in cui la misura sul solo processore vada sotto. Non blocca nulla.

## Raccoglitore di metriche: Netdata accettato, verifiche a cose accese

Dal 15/10/2026, su segnalazione dell'utente, studio in [Metriche in tempo reale con Netdata](03-spunti-di-sviluppo/23-studio-home-lab/14-metriche-con-netdata.md). La riga delle metriche di switch, access point e host è pendente nel piano unificato dall'8/10/2026 ed è l'unica voce di monitoraggio non decisa; ora ha un candidato studiato, con la forma proposta, i percorsi dei dati, i costi dichiarati dal produttore e le alternative già censite messe a confronto. Il 15/10/2026 l'utente ha detto sì (ADR-036), con il parent su una macchina Linux: la scelta è chiusa e la voce resta aperta solo per le verifiche. Non blocca la configurazione della rete. Quattro verifiche restano fuori dalla documentazione, e si fanno solo a cose accese: se il plugin `netdata` di OPNsense esista nella versione installata e funzioni, oppure se il firewall si legga via SNMP; se i profili SNMP riconoscano lo XMG1915 e i NWA130BE; quanta memoria e quanto disco occupi davvero il parent sul server dopo una settimana; se i suoi allarmi si sovrappongano a quelli di Wazuh al punto da doverne spegnere una parte.

## Preventivo per switch e access point

Dall'8/10/2026: l'utente invia al proprio fornitore la richiesta di preventivo per uno XMG1915-10EP e due NWA130BE (ADR-023, ADR-024). Il sorgente è privato in `_notes/preventivo/`. Quando arriva la risposta si confronta con i prezzi di mercato registrati (S59, S68) e, se il fornitore propone alternative, si verificano sui requisiti della richiesta prima di accettarle.

## Seven Booster: disattivazione del servizio e restituzione

Dall'8/10/2026, su richiesta dell'utente, che paga il canone del servizio di estensione del segnale Wi-Fi e con i due AP non avrà più bisogno del Booster. Quanto risulta dalle fonti (S57, S58): l'opzione si può dismettere chiamando il servizio clienti al 192 193 o dall'area MyFastweb; il canone indicato è di 3 euro al mese; a cessazione del contratto gli apparati in comodato vanno restituiti entro 45 giorni con un'etichetta di spedizione gratuita, pena 60 euro per un Booster non restituito; ma in un caso del 2023 Fastweb ha risposto che la restituzione del Booster non era prevista, perché in quel caso era compreso in un pacchetto. Lo scopo dell'utente è smettere di pagare il canone, non ottenere un rimborso. Secondo le fonti il canone è il prezzo dell'opzione, non del possesso dell'apparato: cessa con la disattivazione dell'opzione, mentre la restituzione del Booster è una questione separata che non lo influenza. Le condizioni del contratto dell'utente non sono note, quindi va chiesto nella stessa richiesta. La sequenza proposta: si aspetta il collaudo dei due AP, perché fino ad allora il Booster dà copertura; si chiede la disattivazione dell'opzione, chiedendo nella stessa richiesta se il Booster è in comodato e, se sì, come restituirlo; si conserva la risposta scritta e il Booster integro finché non arriva; si controlla nella fattura successiva che la voce del canone sia sparita.

## Rilevazioni del Seven da ripetere

Dall'8/10/2026 si aggiungono due verifiche emerse dalla riscrittura di `02-ftth-fastweb/05-prima-del-design-della-rete-privata/`: se il firewall del Seven permette di non rispondere al ping sulla WAN, che alla data del test rispondeva; e la trascrizione, già anonimizzata, delle cinque immagini della pagina sul modem libero, oggi senza descrizione.

Dal 07/10/2026, con la lettura tecnica che dall'8/10/2026 sta dentro le pagine di `02-ftth-fastweb/06-tbc-i-parametri-di-interfaccia-modem-su-192-168-1-254-rotte/`. Le schermate dello stato WAN sono state catturate con la GPON giù e la connessione mobile su, quindi vanno rifatte con la fibra attiva, verificando che l'indirizzo pubblico statico sia lo stesso sui due collegamenti. Vanno fotografate per la prima volta lo stato LAN, la sezione LAN switch, il Port Triggering, il Filtro MAC, Easy Mesh, l'Analizzatore e la modalità ECO, che nel censimento hanno il solo titolo.

Dal 12/10/2026 l'occasione è arrivata, e porta con sé un rischio opposto. Dal 9/10/2026 la linea è giù per un guasto in cabina, con l'ONT che segnala assenza di segnale ottico, e il 12/10 è previsto l'intervento di riparazione con collaudo e riavvio del modem, senza il proprietario in casa. Quando la fibra torna su, le schermate si possono finalmente catturare con la GPON attiva; nello stesso giro va verificato che l'intervento non abbia cambiato l'indirizzo pubblico statico, la configurazione del modem e le impostazioni Wi-Fi, perché un ripristino alle impostazioni di fabbrica le azzererebbe tutte. La checklist operativa, che incrocia i valori reali della linea, vive fuori da git in `_notes/collaudo-fastweb-2026-10-12.md`. Una nota di lettura per le schermate nuove: la porta LAN 4 risulterà alla velocità della scheda di rete della macchina collegata in quel momento, cioè 1 Gbps con la macchina Windows di prova, e non è un degrado rispetto ai 2,5 Gbps letti a febbraio 2026.

Dal 12/10/2026, a intervento avvenuto, il guasto è chiuso e la pendenza resta. Il tecnico ha riparato in cabina, dove un armadio era staccato e il percorso di rete era sbagliato, senza toccare nulla in casa: la configurazione del modem e le impostazioni Wi-Fi sono intatte, quindi il rischio del ripristino di fabbrica non si è realizzato e non va più verificato. Resta da fare il giro di schermate con la GPON attiva e il confronto dell'indirizzo pubblico statico fra fibra e collegamento di riserva, che ora è solo un'azione dell'utente davanti all'interfaccia del Seven. Il racconto dell'evento, con la lettura del valore ottico dichiarato dal tecnico e il bilancio di tratta che lo inquadra, è in [Guasto in cabina, ottobre 2026](02-ftth-fastweb/08-guasto-in-cabina-ottobre-2026.md).

Dal 14/10/2026 la pratica con l'operatore è chiusa, e una prova di velocità dal telefono in Wi-Fi a VPN spenta, 903,57 Mbit/s in scarico, mostra l'indirizzo statico sulla fibra: del confronto resta solo il lato del collegamento di riserva, insieme al giro di schermate del Seven con la GPON attiva, che dirà anche la potenza ottica ricevuta se il modem la espone. Il dettaglio delle misure è nella sezione del 14/10/2026 dello stesso documento.

## Protezione degli endpoint oltre il firewall, gratuita e affidabile

Dal 15/10/2026, su richiesta dell'utente; lo stesso giorno è stato scritto lo studio [Protezione degli endpoint e hardening oltre il firewall, a costo zero, 2026](03-spunti-di-sviluppo/07-further-protection/03-studio-protezione-endpoint-2026.md), con le verifiche ancora aperte elencate in fondo, e la scelta strumento per strumento spetta all'utente. La domanda è doppia: quale antivirus gratuito usare sugli endpoint della rete di casa, considerando che l'utente ha già Microsoft Defender nel piano Family, come lo chiama lui; e quale sia la copertura massima ottenibile oltre al firewall con soli strumenti gratuiti e open source, scartando quelli che non mantengono ciò che promettono. Il punto di partenza è la scheda esistente [Endpoint protection](03-spunti-di-sviluppo/07-further-protection/02-endpoint-protection.md), da rileggere contro questa domanda, insieme a ciò che è già deciso: Wazuh con Suricata sul firewall (ADR-028) e Netdata per le metriche (ADR-036). Lo studio deve distinguere i sistemi operativi presenti in casa e dire, per ciascuno strumento, che cosa copre e che cosa no.

## Metodo del censimento dei dispositivi

Richiesta dell'utente del 07/10/2026: decidere un modo per caratterizzare in maniera completa e omogenea tutti i dispositivi della rete. La proposta è una scheda a campi fissi per dispositivo e una raccolta in sola lettura per sistema operativo, da approvare prima di compilare il censimento.

## Strumenti del template non attivi in questo progetto

Dal 07/10/2026: regole e skill del progetto citano sedici volte strumenti `tools/...` che vivono solo in `.claude/templates/tools/`, fra cui la verifica di ripresa, i controlli di tabelle, tipografia e prosa e la verifica delle schede. Finché non sono istanziati, quei presidi non girano, e due di loro lanciati dalla cartella del template danno un verde non calcolato. Deciso con ADR-022: si istanziano dai pacchetti, e da lì li aggiorna l'allineamento. Il guard-rail di anonimizzazione è riconciliato l'8/10/2026 in `tools/Test-Anonymization.py`, e lo stesso giorno sono istanziati gli altri strumenti. Restano tre lavori che gli strumenti hanno misurato e non chiuso: sette schede di contesto superate rispetto all'ancora, da riconciliare per contenuto con la skill `sync-context`; 77 segnalazioni di `lint-prosa` in 57 file, da rileggere; 16.769 occorrenze di forme di accento ambigue, da decidere leggendo la frase, che conviene affrontare documento per documento durante la riscrittura di ADR-020.

Verifica del 19/10/2026: riconciliato il censimento derivato con `python tools/source-register.py`; i tredici URL già contenuti in `docs/anti-slop/FONTI.md` al commit HEAD sono ora registrati con stato «censita; lettura e contenuto da verificare», senza presentarli come consultati. Il controllo successivo rileva 211 URL e zero riferimenti non registrati nel perimetro dei Markdown pubblici e del censimento storico JSON percorso dallo strumento. Questa pendenza di copertura è chiusa; la lettura delle fonti storiche non è dichiarata completa.

## Sezioni censite ma dichiarate non rilevanti

Undici sottosezioni dell'interfaccia del modem sono marcate `not-of-interest-here`: panoramica dei dispositivi connessi, telefono, l'intero ramo Wi-Fi, USB, condivisione contenuti, condivisione stampante, LAN switch, modalità a risparmio energetico, stato della fonia, e le tre sezioni di dettaglio e statistica su IPv6 e IPv4 della WAN. Una sezione, lo stato LAN, è marcata come mancante, cioè l'autore ha annotato che avrebbe dovuto catturarla e non l'ha fatta.

Vale la pena una nota critica: il ramo Wi-Fi del modem è marcato come non rilevante, ma nella topologia adottata la Wi-Fi del modem è esattamente il pezzo di rete che resta fuori dal firewall, quindi le sue impostazioni di sicurezza, cioè cifratura, canale e rete ospite, sono l'unico controllo disponibile su quel segmento finché gli access point a valle non saranno installati. La marcatura andava rivista, ed è stata rivista l'8/10/2026 nella riscrittura della cartella del Seven (ADR-020): la pagina Wi-Fi spiega perché la sezione conta e come si imposta, e lo stesso vale per panoramica e telefono. I nomi dei file conservano la marcatura, perché i nomi sono stabili.

## Come si aggiorna questo file

L'elenco si ricalcola percorrendo le intestazioni dei file generati alla ricerca dei tre marcatori e dei titoli segnaposto. Va rifatto dopo ogni rigenerazione dell'albero, perché i marcatori vivono nel documento sorgente e cambiano quando l'autore lo modifica. Le voci che non vengono dal sorgente, come la pendenza sull'avviso dei template, si aggiungono a mano e si riconoscono perché non hanno un marcatore corrispondente nell'albero.

## Controlli del template dopo l'allineamento del 20/10/2026

Durante la preparazione del versionamento il 20/10/2026, la suite completa di chiusura passa tutti i dodici controlli nel contesto esterno al sandbox, con esito Controlli verdi. I fine riga del metadato sono stati corretti senza cambiare i valori JSON; il riferimento opzionale craft-apps è già corretto dall'allineamento. Nel runner isolato resta riproducibile il difetto delle fixture temporanee Windows, registrato come L-004: non è stato nascosto saltando casi o indebolendo il guard-rail. L'allineamento successivo ha corretto il richiamo PowerShell L-005 e il registro riconosce tutte e cinque le lezioni come recepite, con zero aperte e zero avvisi. L-004 è recepita come norma di verifica delle fixture: non implica che il guard-rail locale sia stato modificato o che il runner isolato abbia acquisito nuovi permessi. La documentazione è controllata per il versionamento; nessun commit o push è stato eseguito dall'agente.
