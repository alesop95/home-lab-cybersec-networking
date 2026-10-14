# Guasto in cabina, ottobre 2026

Documento di fatto e non di progettazione: registra un evento reale della linea, la sua diagnosi dichiarata dall'operatore e la lettura tecnica del solo numero che ne è uscito. Vale la pena scriverlo perché è la prima interruzione documentata della fibra da quando il progetto esiste, e perché il modo in cui si legge un valore ottico dettato al telefono è esattamente il genere di cosa che alla prossima occasione nessuno si ricorderebbe.

## Che cosa è successo

Dal 9/10/2026 la linea è rimasta giù. L'ONT Zyxel PM5100-T1 mostrava LOS[^1] rosso fisso, PON spento e la porta LAN 2,5G spenta, cioè assenza di segnale ottico, e l'applicazione dell'operatore dichiarava il modem non raggiungibile; la casa ha continuato a navigare sul collegamento mobile di riserva del Seven, che è il motivo per cui l'interruzione non si è vista come un blackout.

L'intervento è avvenuto il 12/10/2026 e si è svolto interamente fuori dall'abitazione. Il tecnico ha riferito per telefono che in cabina un armadio era staccato e il percorso di rete era sbagliato. In casa non è stato toccato nulla: nessun apparato è stato riavviato o riconfigurato dall'esterno, la rete senza fili è tornata da sé quando il collegamento ottico si è ristabilito, e di conseguenza non si applica il rischio che la checklist di collaudo teneva in conto, cioè un ripristino alle impostazioni di fabbrica che avrebbe azzerato configurazione del modem e impostazioni Wi-Fi.

## Perché la causa dichiarata è coerente con i sintomi

Il ragionamento si registra perché è la parte che resta utile il giorno di un guasto successivo, quando di nuovo si dovrà decidere se cercare la causa in casa o fuori. Un LOS rosso fisso con PON spento non descrive un collegamento degradato ma un collegamento assente: l'ONT non aggancia perché non vede luce, o ne vede troppo poca per sincronizzarsi. Un eccesso di attenuazione, per esempio una bretella piegata oltre il raggio di curvatura o un connettore sporco, si manifesta in modo diverso, con un collegamento che sale e ricade, con errori in salita o con una sincronizzazione instabile, e quasi mai con un'assenza netta e continua per giorni. Una tratta interrotta a monte produce invece esattamente questo quadro. La diagnosi dichiarata, un armadio staccato e un percorso errato, appartiene a questa seconda famiglia, ed è compatibile con il fatto che nulla in casa sia stato toccato e che il ritorno del servizio sia stato immediato e stabile.

## Il valore ottico dichiarato, e come si legge

Il tecnico ha dichiarato per telefono un valore di 20,93 e ha indicato come soglia operativa il 25, sotto il quale la linea non è considerata problematica. Il dato è riportato come è stato ricevuto: non è stato misurato con uno strumento né letto su un'interfaccia, quindi resta una dichiarazione verbale di seconda mano, da confermare con una lettura diretta il giorno in cui servisse come riferimento.

L'unità pronunciata, dBm, non può valere per entrambe le letture possibili del numero, e la distinzione non è pedanteria perché cambia quale grandezza si sta confrontando con quale limite. Se il numero è l'attenuazione della tratta ottica, l'unità corretta è il dB e non il dBm, perché un rapporto fra due potenze non è una potenza: si tratterebbe di 20,93 dB di perdita fra OLT[^2] e ONT, comprensivi di fibra, splitter e connettori. Se invece è la potenza ottica ricevuta dall'ONT, l'unità è davvero il dBm, ma il segno è negativo, cioè -20,93 dBm, perché un terminale domestico riceve sempre una frazione di milliwatt.

Entrambe le letture si valutano contro il bilancio di tratta della classe ottica. In GPON la classe B+ prevede un trasmettitore OLT fra +1,5 e +5 dBm, una sensibilità dell'ONT di -27 dBm, una soglia di sovraccarico di -8 dBm e un'attenuazione ammessa fra 13 e 28 dB; la classe C+ sposta i tre numeri a +3 fino a +7 dBm, -32 dBm e 17 fino a 32 dB.

Nella prima lettura, con un OLT a +3 dBm, 20,93 dB di perdita lasciano all'ONT circa -17,9 dBm, cioè circa nove decibel sopra la sensibilità di classe B+ e molto lontano dal sovraccarico. La soglia operativa di 25 dB lascia tre decibel di margine rispetto ai 28 ammessi dalla classe, ed è il tipo di numero che un operatore si tiene per invecchiamento della tratta, giunzioni aggiunte e riparazioni future.

Nella seconda lettura, -20,93 dBm di potenza ricevuta stanno circa sei decibel sopra la sensibilità di classe B+ e undici sopra quella di classe C+, dentro la finestra in cui si trova normalmente un ONT domestico sano. In questa lettura però la soglia di 25 significherebbe non scendere sotto -25 dBm, cioè fermarsi a due decibel dalla sensibilità, che è un margine stretto per una regola pratica da dettare al telefono. È la ragione per cui la prima lettura, attenuazione in decibel, resta la più probabile, e resta comunque un'inferenza.

La conclusione pratica non dipende da quale delle due sia: il collegamento ottico ristabilito sta dentro il bilancio di tratta con margine abbondante, e il numero conferma la riparazione invece di spiegare il guasto. Un guasto da bilancio ottico si sarebbe presentato con un valore vicino o oltre il limite della classe, non con nove decibel di margine.

L'ambiguità si risolve con un dato che il progetto deve raccogliere comunque: se la pagina di stato dell'ONT o la sezione GPON dello stato WAN del Seven espone la potenza ottica ricevuta, segno e unità si leggono lì e il valore dettato al telefono trova o perde conferma. È un'inferenza da verificare, aggiunta al giro di schermate già pendente.

## La verifica del 14/10/2026, e la chiusura della pratica

Il 14/10/2026 l'utente dichiara chiusa la pratica aperta con l'operatore per il guasto, e porta tre schermate di una prova di velocità fatta con speedtest.net nel browser di un telefono Android, collegato al Wi-Fi del Seven, con il server scelto in automatico dal servizio. Le schermate mostrano lo scarico e la latenza, non il carico, che quindi non è misurato.

| Ora | VPN sul telefono | Scarico | Latenza a riposo | Latenza durante lo scarico |
|---|---|---|---|---|
| 08:02 | attiva, dall'icona nella barra di stato | 746,38 Mbit/s | 46 ms | 119 ms |
| 08:03 | spenta | 903,57 Mbit/s | 45 ms | 117 ms |

Nella terza schermata, a VPN spenta, il servizio indica come fornitore Fastweb e un indirizzo pubblico che coincide con l'indirizzo statico della linea, `203.0.113.10` nei segnaposto del progetto; il confronto è stato fatto in locale, e la schermata originale resta fuori da git. L'intervento in cabina non ha quindi toccato l'assegnazione dell'indirizzo statico, che era la domanda della checklist di collaudo a cui il tecnico non poteva rispondere con certezza per telefono. È coerente con quanto il tecnico aveva dichiarato, cioè di non aver toccato nulla in casa: lo stesso indirizzo, e il telefono che si ricollega da solo alle stesse reti senza fili.

Come si leggono i numeri. Novecento megabit al secondo in Wi-Fi su un telefono dicono che la linea non è il collo di bottiglia: il valore sta vicino a ciò che una porta da 1 Gbit/s dà via cavo, e il profilo da 2,5 Gbit/s resta misurabile solo lato modem, come la checklist di collaudo già prevedeva. La prova con la VPN attiva misura il percorso fino al server della VPN e non la linea; lo scarto di circa 160 Mbit/s è con ogni probabilità il costo della VPN, ed è un'inferenza. La latenza a riposo di 45 ms è più alta di quella che ci si aspetta da una fibra verso un server vicino, ma senza la distanza del server e senza una ripetizione via cavo non si può attribuire alla linea, al Wi-Fi o al server: resta un dato da guardare alla prossima misura, non un difetto. Il quadro conferma la lettura del valore ottico data sopra: collegamento dentro il bilancio di tratta, linea sana.

## Che cosa resta aperto

Il guasto è chiuso e non lascia lavoro residuo, e dal 14/10/2026 è chiusa anche la pratica con l'operatore: la linea è tornata, la configurazione di casa è intatta e nessun intervento è rimasto a metà. Restano aperte le verifiche che l'evento ha reso finalmente possibili, che riguardano la documentazione e non la riparazione: le schermate dello stato WAN del Seven con la GPON attiva, dato che il censimento di febbraio 2026 le aveva prese sul collegamento mobile di riserva, e il confronto dell'indirizzo pubblico statico fra la fibra e il collegamento di riserva, di cui dal 14/10/2026 il lato della fibra è verificato e resta solo quello del collegamento di riserva. Entrambe stanno nel [registro delle pendenze](../pendenze-aperte.md), sotto le rilevazioni del Seven da ripetere, e la loro guida di lettura è la [seconda lettura dei parametri di interesse](07-tbc-new-i-parametri-di-accesso-wan-su-ont/03-tbc-seconda-lettura-parametri-di-interesse.md).

[^1]: *LOS*, Loss of Signal: l'indicazione con cui un terminale ottico segnala di non ricevere potenza sufficiente a riconoscere il segnale della rete PON. Acceso fisso descrive un collegamento assente, non degradato.

[^2]: *OLT*, Optical Line Terminal: l'apparato dell'operatore in centrale che termina il ramo ottico dal lato di rete, cioè la controparte dell'ONT installato presso il cliente.
