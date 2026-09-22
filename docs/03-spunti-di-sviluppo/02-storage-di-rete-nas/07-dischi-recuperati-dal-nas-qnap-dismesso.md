# Quattro dischi recuperati da un NAS QNAP dismesso, e che cosa se ne fa

Studio del 22/09/2026, basato sulle fonti U07-U08 e S50-S52 del [registro](../../../SOURCES.md). Chiude la decisione che [l'analisi del consolidamento](03-consolidamento-di-quattro-desktop-dismessi-in-un-nas.md) e la [guida all'assemblaggio](04-guida-assemblaggio-e-installazione-truenas.md) lasciavano aperta in tre punti identici, cioe' quali dischi meccanici comporranno il pool dei dati. I valori di stato riportati qui sono stati letti dall'interfaccia di gestione del NAS[^1] di provenienza e non da `smartctl` su una macchina di laboratorio: sono quindi da riverificare a dischi collegati alla base, e il protocollo di qualificazione descritto piu' avanti e' esattamente il modo in cui quella verifica si fa. Nessuno di questi dischi e' stato ancora spostato, nessun dato e' stato ancora migrato, e il NAS di provenienza e' in esercizio nel momento in cui questo documento viene scritto.

## Da dove vengono

Sono i quattro dischi da 2 TB di un QNAP TS-410U aziendale in dismissione, una macchina con processore Marvell 6281 a 800 MHz e 512 MB di memoria, dove lavorano in RAID[^2] 5 esponendo circa 5,4 TB. Non appartengono alla rete domestica documentata in questo albero, quindi seguono la convenzione delle macchine del consolidamento e compaiono con segnaposto propri.

| Baia | Modello | Firmware | Seriale | Ore di accensione | Settori riallocati | Errori di lettura grezzi | Temperatura |
|---|---|---|---|---|---|---|---|
| 1 | SAMSUNG HD204UI | `1AQ10001` | `<sn-hdd-samsung-A>` | 125.339 | 0 | 1 | 30 C |
| 2 | SAMSUNG HD204UI | `1AQ10001` | `<sn-hdd-samsung-B>` | 125.318 | 0 | 18 | 32 C |
| 3 | SAMSUNG HD204UI | `1AQ10001` | `<sn-hdd-samsung-C>` | 125.225 | 0 | 92 | 31 C |
| 4 | TOSHIBA DT01ACA200 | `MX4OABB0` | `<sn-hdd-toshiba>` | 104.496 | 0 | 0 | 35 C |

Il Samsung e' uno SpinPoint F4 EcoGreen del 2010, 5400 giri, interfaccia SATA a 3 Gb/s, 32 MB di cache. Il Toshiba e' della serie DT01ACA, 7200 giri, SATA a 6 Gb/s, 64 MB di cache, un terabyte per piatto, e dichiara 5,2 W a riposo attivo. Sono entrambi dischi da tavolo, non dischi destinati all'uso continuo: la differenza fra le due categorie, che qui determina quasi tutto, e' descritta nella scheda generale [Dischi e SSD per uso continuo contro uso generico](../../04-concetti-generali/10-hardware-soluzioni-tecnologie/03-dischi-e-ssd-per-uso-continuo-contro-uso-generico.md).

## Quattro riscontri, in ordine di peso

### Meccanicamente non mostrano degrado, ed e' il dato migliore

Tutti e quattro dichiarano zero settori riallocati, zero errori di ricerca, zero tentativi di riavvio del motore, e temperature fra i trenta e i trentacinque gradi. Il settore riallocato e' il primo sintomo osservabile del deterioramento della superficie magnetica, ed e' un contatore che non torna mai indietro: zero dopo quattordici anni significa che questi dischi hanno passato la loro vita in una finestra termica favorevole e senza sollecitazioni meccaniche. E' un riscontro a favore e va preso sul serio, perche' e' la stessa misura con cui si scarterebbe un disco nuovo.

Il conteggio di errori di lettura grezzi della terza unita', novantadue, non contraddice quel quadro: su queste famiglie e' un contatore cumulativo che il firmware normalizza a cento, cioe' il valore che il produttore considera sano, ed e' l'errore corretto dal codice di correzione prima che arrivi al sistema. Diventa significativo se cresce durante la qualificazione, non per il valore assoluto che porta oggi.

Un attributo della terza unita' resta pero' da guardare a mano e non si interpreta dall'interfaccia del NAS: `Program_Fail_Count` riporta un valore normalizzato di 25 con un peggiore storico di 1 contro una soglia di 0. Su questa famiglia Samsung quell'attributo e' notoriamente codificato in modo non standard e un peggiore storico di uno non equivale a un disco in procinto di cedere, ma e' un'affermazione che non si promuove a fatto senza rilettura diretta: e' uno dei riscontri che la qualificazione deve chiudere.

### L'eta' e' fuori dalle curve pubblicate

Centoventicinquemila ore sono quattordici anni e tre mesi di accensione, centoquattromila sono undici anni e undici mesi. L'analisi di Backblaze su circa trecentodiciassettemila unita', che e' il corpus statistico piu' ampio disponibile pubblicamente, colloca il picco del tasso di guasto a dieci anni e tre mesi con un valore del 4,25 per cento annuo, e osserva che la curva a vasca si e' spostata verso destra rispetto alle rilevazioni di dieci anni fa. Questi dischi stanno oltre l'estremo destro di quella curva.

La conseguenza va scritta per come e', senza addolcirla. Non esiste una base statistica pubblicata che descriva il comportamento di un disco meccanico a quattordici anni di accensione continua, quindi qualunque previsione sulla loro vita residua e' un'estrapolazione oltre i dati, non una stima. Cio' che si puo' dire e' che nessuno dei quattro mostra oggi il sintomo che precede il guasto per usura della superficie, e che questo non dice nulla sul guasto improvviso dell'elettronica o del motore, che non ha sintomi premonitori osservabili.

### Il lotto unico pesa piu' dell'eta'

I tre Samsung hanno seriali consecutivi e ore di accensione che differiscono di centoquattordici su centoventicinquemila, cioe' meno di un millesimo. Sono tre esemplari dello stesso lotto di produzione, montati insieme, accesi insieme e sottoposti allo stesso identico carico per quattordici anni dentro lo stesso RAID 5.

Questa e' la cosa che cambia le conclusioni, e la ragione e' che ogni calcolo di ridondanza assume che i guasti siano indipendenti. Due dischi in specchio proteggono perche' la probabilita' che cedano entrambi nella stessa finestra e' il prodotto di due probabilita' scorrelate. Se pero' i due dischi condividono lotto, difetto di fabbricazione, ore e sollecitazione, quel prodotto non si applica: si guastano per lo stesso meccanismo e nello stesso intorno di tempo, ed e' precisamente la ricostruzione del primo guasto a portare il secondo al punto di cedimento, perche' la ricostruzione e' il carico piu' pesante che un disco vede in tutta la sua vita.

Uno specchio composto da due di questi tre Samsung sarebbe quindi ridondanza sulla carta e non nei fatti. Il Toshiba, che e' di marca diversa, generazione diversa, velocita' di rotazione diversa e ha ventunomila ore in meno, e' l'unico disco del gruppo il cui guasto rispetto agli altri e' davvero indipendente.

### Il firmware porta un difetto noto, e non si puo' sapere se e' gia' corretto

La versione `1AQ10001` dell'HD204UI e' quella affetta dal difetto documentato che causa corruzione dei dati quando un comando `IDENTIFY DEVICE` o una lettura SMART[^3] raggiungono il disco mentre sta scrivendo con scritture accodate. Samsung ha pubblicato un correttivo, ma non ha incrementato il numero di versione: un disco corretto continua a dichiarare `1AQ10001`. Non esiste quindi un modo di stabilire per lettura se questi tre dischi sono gia' corretti, ed e' un'incertezza reale che va portata avanti invece di essere risolta per ipotesi.

Il punto e' rilevante perche' TrueNAS interroga lo SMART dei dischi con cadenza regolare e li sottopone a test periodici programmati, cioe' fa esattamente la cosa che innesca il difetto, mentre il pool scrive.

Ci sono due mitigazioni e una osservazione. La prima mitigazione e' applicare il correttivo, che si distribuiva come utility avviabile da DOS e la cui reperibilita' quindici anni dopo va verificata prima di contarci. La seconda, che non dipende da nessun file da ritrovare, e' disattivare le scritture accodate sui soli dischi interessati, cosa che sul kernel Linux si ottiene con un parametro di avvio applicato per porta, e il cui costo prestazionale su un carico prevalentemente sequenziale limitato da una rete a un gigabit e' trascurabile. La terza cosa non e' una mitigazione ma un'osservazione, e va dichiarata come inferenza e non come prova: questi dischi hanno lavorato quattordici anni dentro un NAS che interroga lo SMART, senza corruzione nota, il che suggerisce o che il correttivo sia stato applicato all'epoca o che la combinazione di eventi non si sia mai presentata. Nessuna delle due ipotesi e' verificata qui.

## Che cosa invece va bene senza riserve

Entrambi i modelli sono a registrazione convenzionale. E' un punto che la guida poneva come vincolo di acquisto, diffidando delle serie da tavolo economiche perche' spesso sono a registrazione sovrapposta senza dichiararlo, e che qui si risolve da solo per ragioni cronologiche: l'HD204UI e' del 2010 e la registrazione sovrapposta arriva sul mercato consumer soltanto anni dopo, mentre la serie DT01ACA e' dichiaratamente convenzionale. Il vincolo che avrebbe reso questi dischi inadatti a ZFS non si applica.

Le capacita' sono identiche al gigabyte dichiarato, 1863,02 GB su tutti e quattro, quindi si specchiano senza spreco a prescindere da quali due si accoppiano.

## Quel che manca e che questi dischi non hanno

Nessuno dei due modelli implementa il recupero d'errore a tempo limitato. Su un controller RAID tradizionale sarebbe squalificante, perche' un disco che impiega mezzo minuto a rileggere un settore difficile viene espulso dall'array come guasto; su ZFS il meccanismo e' diverso, perche' non c'e' un controller che espelle, ma il problema non sparisce: un disco che entra in un ciclo di recupero lungo blocca l'ingresso e uscita del suo gruppo finche' non ne esce, e il livello a blocchi del kernel, che di suo fallisce l'operazione dopo trenta secondi, la dichiara fallita mentre il disco sta ancora lavorando. La contromisura corretta e' controintuitiva e consiste nell'alzare quel timeout invece di abbassarlo, dando al disco il tempo di completare il recupero e tornare con il dato, che e' esattamente cio' che ZFS puo' usare.

Nessuno dei due ha sensori di vibrazione rotazionale. In una gabbia con tre dischi in rotazione la penalita' esiste ma e' contenuta, e diventa significativa nelle gabbie dense da otto alloggiamenti in su.

## Quanti ne entrano, fisicamente

La base ha sei porte SATA e tutte e sei restano disponibili, perche' un dispositivo M.2 in modalita' PCIe non sottrae porte a questa scheda. Due sono impegnate dall'insieme di avvio in mirror, quindi ne restano quattro, che i quattro dischi saturerebbero al pixel.

| Porta | Destinazione |
|---|---|
| `SATA6G_1` | SSD di avvio, prima meta' dello specchio |
| `SATA6G_2` | SSD di avvio, seconda meta' |
| `SATA6G_3` | pool dati, prima meta' di `mirror-0` |
| `SATA6G_4` | pool dati, seconda meta' di `mirror-0` |
| `SATA6G_5` | disco di riserva a caldo |
| `SATA6G_6` | libera, per la crescita |

L'alimentazione cambia rispetto a quanto la guida prevedeva. Il criterio di scelta dell'alimentatore chiedeva quattro connettori SATA, due per gli SSD e due per i meccanici: con la configurazione decisa qui ne servono cinque, e con tutti e quattro i dischi montati ne servirebbero sei. E' il primo dato che va riletto sulle etichette dei quattro alimentatori disponibili, insieme alla potenza nominale, perche' un adattatore da Molex a SATA e' una soluzione accettabile ma va prevista prima e non improvvisata a case aperto.

Il picco allo spunto sale di conseguenza. Con tre dischi meccanici che assorbono da venti a venticinque watt ciascuno mentre i motori raggiungono il regime, piu' i due SSD e il resto della macchina, il picco realistico si colloca fra i centocinquanta e i centottanta watt, che resta dentro l'obiettivo dei trecento-quattrocento watt gia' fissato e non lo invalida.

Restano due dati fisici ancora ignoti, ed e' onesto dire che sono la sola cosa che puo' far saltare questo piano. Il numero di alloggiamenti da tre pollici e mezzo del case della base non e' mai stato censito, e l'unica annotazione esistente dice che la gabbia e' predisposta per un disco solo. Se cosi' fosse, la soluzione non e' rinunciare ma prelevare una gabbia da uno dei tre case di scorta, che sono due ATX e uno micro-ATX e sono comunque destinati a restare vuoti: e' pero' un lavoro meccanico da prevedere, non un dettaglio. Il secondo dato ignoto e' l'etichetta dell'alimentatore, che non ha nessuna altra fonte oltre la lettura diretta.

## Prima di montarli: qualificare, non cancellare

L'intenzione iniziale era cancellare i dischi con tre passate di sovrascrittura su Linux, oppure con la pulizia integrale di `diskpart` su Windows. Entrambe le strade fanno una cosa sola, cancellare, e su dischi che si vogliono rimettere in servizio la cancellazione non e' lo scopo: ZFS riscrive comunque ogni settore che usa, e un disco che resta in casa non ha bisogno di essere sanificato contro un recupero forense. Lo scopo vero e' scoprire un disco marcio mentre e' ancora vuoto, ed e' un obiettivo che la cancellazione non serve, perche' scrive senza rileggere e quindi non verifica niente.

Le tre passate, poi, non aggiungono nulla. Su una registrazione magnetica moderna una sola sovrascrittura rende il dato non recuperabile con mezzi pratici, e ripeterla tre volte costa tre volte il tempo su dischi che hanno quattordici anni ed e' proprio il tipo di sollecitazione inutile che si vuole evitare.

Lo strumento corretto scrive e rilegge verificando, e cancella meglio di una passata di zeri perche' i pattern che usa sono quattro. La sequenza e' la seguente, e va eseguita su una macchina Linux con i dischi collegati direttamente, non attraverso un adattatore USB, che maschera i comandi SMART.

```bash
sudo badblocks -wsv -b 4096 -o /tmp/badblocks-sdX.log /dev/sdX
sudo smartctl -t long /dev/sdX
sudo smartctl -a /dev/sdX
```

Il primo comando percorre l'intera superficie quattro volte in scrittura e quattro in lettura. Su un disco da 2 TB a 5400 giri, la cui velocita' sequenziale media si colloca attorno ai settanta megabyte al secondo tenendo conto del calo verso le tracce interne, ogni coppia di passate richiede all'incirca sedici ore e il ciclo completo si avvicina ai tre giorni; sul Toshiba a 7200 giri e' sensibilmente meno. E' normale e non e' un guasto. I quattro dischi si possono qualificare in parallelo, uno per processo, purche' su ciascuno giri una sola prova per volta. Se il tempo e' un vincolo si riduce a un pattern solo, perdendo pero' la capacita' di intercettare i difetti che si manifestano solo con certe configurazioni di bit.

Il secondo comando avvia il test interno lungo del disco, che va lanciato dopo la sovrascrittura e non prima, cosi' che trovi la superficie nello stato in cui la userai. Il terzo rilegge gli attributi.

Il criterio di scarto e' netto e non ammette interpretazione. Si guardano il conteggio dei settori riallocati, il conteggio dei settori in attesa di riallocazione, il conteggio dei settori non correggibili offline e il conteggio degli errori di interfaccia, cioe' gli attributi 5, 197, 198 e 199. Tutti e quattro valgono zero oggi su tutti e quattro i dischi: qualunque valore diverso da zero al termine della qualificazione significa che quel disco e' cambiato sotto carico, e un disco che si degrada mentre lo si prova e' un disco che si scarta, non uno che si tiene d'occhio. L'unica eccezione ragionevole riguarda il conteggio degli errori di interfaccia, che se cresce accusa il cavo prima del disco e va rifatto sostituendo il cavo.

Il momento in cui fare tutto questo e' dopo la prova della memoria e prima della creazione del pool, cioe' dentro la finestra in cui la macchina e' gia' montata e TrueNAS e' gia' installato sull'insieme di avvio ma non ospita ancora nulla.

## La configurazione decisa

Nel pool dei dati entrano il Toshiba e il primo Samsung come unico gruppo in specchio. E' l'unica coppia possibile fra questi quattro dischi i cui due elementi non condividono lotto, marca, generazione, velocita' di rotazione e storia di carico, ed e' quindi l'unica in cui la ridondanza corrisponde a quello che promette. La disomogeneita' fra un disco a 5400 giri e uno a 7200 fa lavorare lo specchio alla velocita' del piu' lento in scrittura, il che significa circa centodieci megabyte al secondo, cioe' esattamente il tetto della rete a un gigabit: non si perde niente che sarebbe arrivato al client.

Il secondo Samsung resta nella macchina come disco di riserva a caldo. E' la risposta corretta al rischio del lotto unico, perche' trasforma il vantaggio residuo di avere tre esemplari identici, cioe' la disponibilita' immediata di un ricambio compatibile, in un automatismo che non richiede che qualcuno si accorga del guasto: alla perdita di un elemento dello specchio la ricostruzione parte da sola.

Il terzo Samsung esce dal NAS e va nella scorta a cui manca soltanto un disco, quella con la sola scheda di rete Intel del gruppo, che l'[inventario](06-inventario-delle-scorte-dopo-il-consolidamento.md) descrive come la macchina che si riaccende con la spesa minore. E' la parte meno ovvia di questa decisione e quella che produce il beneficio maggiore, perche' l'inventario dichiara oggi che dopo il consolidamento in magazzino non resta un solo disco, e definisce quel fatto il vincolo dominante che governa qualunque ricostruzione. Un disco solo lo rimuove, e trasforma una scorta inerte nel secondo nodo di laboratorio previsto dalla roadmap, quello su cui provare le macchine virtuali di monitoraggio senza toccare il NAS.

La sesta porta SATA resta libera, ed e' la forma piu' economica di espansione futura: un disco nuovo comprato fra un anno vi si aggiunge senza smontare niente.

## La decisione che questo documento non chiude

Quanto spazio serve davvero non e' noto. Il NAS di provenienza espone circa 5,4 TB in RAID 5 ma il dato che conta non e' la capacita' esposta, e' l'occupato reale da migrare piu' la crescita prevista, e quel numero non e' stato misurato. La configurazione decisa qui offre 2 TB utili.

Il cancello e' esplicito e si colloca prima della creazione del pool, non prima dell'assemblaggio, perche' nulla di quanto precede dipende da questa risposta. Si misura l'occupato sul NAS di provenienza mentre e' ancora acceso, e da li' si decide.

Se l'occupato sta sotto i due terabyte, la configurazione resta quella descritta e non si tocca nulla. Se lo supera, il terzo Samsung rientra come secondo gruppo in specchio portando il pool a 4 TB utili, la riserva a caldo scompare, la scorta resta senza disco, e quel secondo gruppo va dichiarato per quello che e': una coppia di gemelli con la stessa storia, cioe' una zona del pool la cui ridondanza e' piu' debole della prima. In quel caso l'unica regola sensata e' non usarlo per dati diversi da quelli ricreabili, e mettere in calendario la sostituzione del primo dei due che cede con un disco nuovo invece che con un altro esemplare dello stesso lotto.

## La regola d'ingaggio sui dati

Questi dischi diventano il pool dei dati e rimandano l'acquisto di dischi nuovi destinati all'uso continuo, ma non cambiano la natura di cio' che sono: supporti da tavolo a fine vita, tenuti in servizio perche' sono sani oggi e perche' costano zero.

Ne discende un confine che vale a prescindere dalla forma del pool. Nessun dato la cui unica copia sia su queste unita' puo' abitarci. Vanno bene l'archivio replicabile, la zona di transito, il bersaglio locale di una copia di sicurezza che esiste anche altrove, i file multimediali riscaricabili, le immagini di sistema ricostruibili. Non vanno bene le fotografie di famiglia, i documenti originali e qualunque cosa la cui perdita non si rimedi rifacendola. La regola delle tre copie su due supporti diversi con una fuori sede non e' sospesa dal fatto che il pool sia ridondante: la ridondanza protegge dal guasto di un disco, non dalla cancellazione per errore, non dal ransomware e non dall'incendio.

Gli automatismi di ZFS che rendono utile questa configurazione vanno attivati, perche' nessuno dei due e' acceso per impostazione predefinita. Lo scrub mensile percorre tutto il pool confrontando i dati con le loro somme di controllo e ripara dal gemello cio' che non torna, ed e' il solo meccanismo che su dischi di questa eta' intercetta il degrado silenzioso prima che diventi perdita. Le notifiche sugli errori del pool vanno configurate e poi provocate deliberatamente una volta, perche' una notifica non verificata e' una notifica presunta.

## Effetto sul consumo e sulla finestra di accensione

La [stima dei consumi](05-consumo-elettrico-e-finestra-di-accensione.md) sommava da undici a sedici watt per due dischi meccanici in rotazione. Con tre dischi accesi, perche' la riserva a caldo gira anch'essa salvo metterla in sospensione, il contributo sale a una cifra fra i diciassette e i ventiquattro watt alla presa, perdita di conversione compresa. La macchina passa cosi' da una stima centrale di quarantotto watt senza meccanici a una fra i sessantacinque e i settantadue.

Sulla finestra di accensione gia' decisa, centodiciotto ore alla settimana, e al costo marginale di 0,256 euro per kilowattora, la spesa annua passa da circa novantacinque euro a circa centodieci. Sono quindici euro l'anno in piu' a fronte di quattro terabyte grezzi che non si sono pagati, ed e' un confronto che va fatto con il prezzo di due dischi nuovi e non con lo zero.

C'e' un margine facile su cui tornare quando la macchina sara' in esercizio: mettere in sospensione il solo disco di riserva, che non serve finche' non c'e' un guasto, vale circa cinque watt continui, cioe' una trentina di kilowattora e otto euro l'anno. Non e' la sospensione aggressiva dei dischi del pool, che produrrebbe cicli di avvio e arresto frequenti ed e' una cosa diversa: qui si tratta di un disco che nel funzionamento normale non viene mai letto.

Tutte queste cifre restano stime per componenti con l'incertezza del trenta per cento gia' dichiarata. La misura alla presa, quando la macchina sara' accesa, le sostituisce.

## Che cosa succede al NAS di provenienza

Nulla di quanto sopra si esegue finche' i dati di quel NAS non sono stati migrati e la migrazione non e' stata verificata leggendo davvero i file ripristinati, non soltanto contando che l'operazione sia terminata. E' la stessa disciplina applicata ai salvataggi delle due macchine Linux del consolidamento, dove il ripristino e' stato eseguito per davvero prima di dichiarare le macchine formattabili, ed e' l'unico modo di sapere che una copia esiste.

Estrarre un disco da un RAID 5 in esercizio lo rende degradato e ogni disco estratto successivamente lo distrugge. I quattro dischi si prelevano insieme, a NAS spento, dopo la migrazione, e non uno alla volta.

Il telaio del QNAP, il suo alimentatore e i quattro cassetti non entrano in questa valutazione e vanno inventariati a parte quando la macchina sara' aperta: un cassetto da tre pollici e mezzo con la sua slitta e' esattamente il pezzo che potrebbe servire se la gabbia della base risultasse predisposta per un disco solo.

[^1]: *NAS*, Network Attached Storage - apparato dedicato che espone spazio disco in rete tramite protocolli standard di condivisione, invece di offrire dischi a un singolo computer.

[^2]: *RAID*, Redundant Array of Independent Disks - insieme di dischi presentati come un volume solo, con schemi che distribuiscono i dati e una quota di ridondanza per sopravvivere al guasto di una o piu' unita'.

[^3]: *SMART*, Self-Monitoring, Analysis and Reporting Technology - insieme di contatori che il firmware di un disco mantiene sul proprio stato, interrogabili dal sistema operativo e usati per stimare il degrado prima che diventi guasto.
