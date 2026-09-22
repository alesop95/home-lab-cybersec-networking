# Dischi e SSD per uso continuo contro uso generico

Scheda di concetto generale, scritta il 22/09/2026. Spiega che cosa distingue davvero un disco meccanico o un'unita' a stato solido destinati a stare accesi sempre dentro un apparato di archiviazione in rete da uno generico venduto per un computer da tavolo, e perche' la differenza non sta quasi mai dove la si cerca, cioe' nella velocita'. Serve come riferimento per le scelte di acquisto e come chiave di lettura dei componenti gia' presenti nel progetto; il caso applicato ai quattro dischi recuperati sta in [Quattro dischi recuperati da un NAS QNAP dismesso](../../03-spunti-di-sviluppo/02-storage-di-rete-nas/07-dischi-recuperati-dal-nas-qnap-dismesso.md).

## L'equivoco di partenza

La domanda che si pone quasi sempre e' quale disco sia piu' veloce, e quasi sempre e' la domanda sbagliata. In un archivio di rete domestico il limite non e' il disco: un solo disco meccanico moderno satura gia' in sequenziale una rete a un gigabit, che si ferma attorno ai centodieci megabyte al secondo, e anche una rete a due gigabit e mezzo viene servita da una coppia di dischi qualunque. Comprare velocita' che la rete non trasporta e' spesa che non arriva mai al client.

Cio' che un uso continuo chiede davvero e' una cosa diversa, ed e' comportamento prevedibile. Prevedibile quando il supporto incontra un errore, perche' la differenza fra un apparato che continua a servire e uno che si ferma sta in come il supporto reagisce al primo settore difficile. Prevedibile sotto carico prolungato, perche' il profilo di scrittura di un archivio non e' una raffica di dieci minuti seguita da ore di inattivita' ma un flusso che dura quanto dura la copia. Prevedibile in presenza di altri supporti, perche' quattro dischi che girano nella stessa gabbia non sono quattro dischi isolati. Ed e' su queste tre cose, non sulla velocita' di punta, che le famiglie destinate all'uso continuo si distinguono.

## Dischi meccanici

### Il recupero d'errore a tempo limitato, che e' la differenza piu' importante

Quando un disco incontra un settore che non riesce a leggere al primo tentativo, entra in una procedura di recupero: riposiziona la testina, rilegge, applica correzioni progressivamente piu' aggressive. Un disco da tavolo insiste finche' ci riesce, e puo' impiegare trenta secondi o piu', perche' nel computer di casa quel comportamento e' corretto: meglio un'attesa lunga che un file perso, dato che non esiste una seconda copia da cui attingere.

Dentro un insieme ridondante quella logica si capovolge, perche' una seconda copia esiste. Il recupero d'errore a tempo limitato, che i produttori chiamano con nomi diversi a seconda della marca, impone al disco di arrendersi entro sette secondi e di dichiarare il fallimento, cosi' che il livello superiore vada a prendere il dato dalla copia e riscriva il settore. Il disco da tavolo, che invece non si arrende, produce un effetto che sorprende chi lo osserva la prima volta: un controller RAID[^1] classico lo considera non rispondente e lo espelle dall'insieme come guasto, pur essendo un disco perfettamente sano che stava soltanto lavorando. Da qui viene la fama dei dischi da tavolo che cadono fuori dagli array, che non e' un difetto di affidabilita' ma di protocollo.

Su un filesystem a somme di controllo come ZFS[^2] il meccanismo e' diverso, perche' non c'e' un controller che decide di espellere, e questo e' il motivo per cui un disco privo di recupero a tempo limitato vi resta utilizzabile. Il problema pero' si sposta invece di sparire: il disco che insiste blocca l'ingresso e uscita del proprio gruppo per tutta la durata del tentativo, e il livello a blocchi del sistema operativo, che di suo dichiara fallita un'operazione dopo trenta secondi, la interrompe mentre il disco sta ancora lavorando. La contromisura corretta e' controintuitiva e consiste nell'alzare quel timeout invece di abbassarlo, perche' un disco lasciato finire spesso torna con il dato buono, ed e' esattamente il dato che serve.

### Il carico annuo dichiarato

I produttori dichiarano per ogni famiglia un volume di dati letti e scritti all'anno entro il quale la garanzia e le stime di affidabilita' valgono. Le serie da tavolo si collocano attorno ai cinquantacinque terabyte all'anno, che descrivono bene un computer usato di giorno e spento di notte. Le serie destinate all'uso continuo dichiarano centottanta terabyte all'anno, e quelle professionali trecento.

Il numero da solo dice poco finche' non lo si confronta con il proprio uso, ed e' un confronto che quasi sempre rassicura in un contesto domestico: un archivio di famiglia con qualche centinaio di gigabyte di movimento al mese sta comodamente dentro il limite anche di una serie da tavolo. Il conto cambia se si aggiungono le letture degli scrub periodici e delle ricostruzioni, perche' uno scrub mensile su un pool da due terabyte legge due terabyte, cioe' ventiquattro terabyte all'anno di solo controllo, e una ricostruzione ne legge altrettanti in una volta sola. Il dato utile non e' quindi il limite in se' ma la consapevolezza che gli automatismi che proteggono i dati consumano anch'essi carico dichiarato.

### I sensori di vibrazione rotazionale

Un piatto che gira a settemiladuecento giri produce vibrazione, e piu' dischi nella stessa gabbia se la trasmettono attraverso il telaio. Le testine, che devono restare allineate su tracce larghe frazioni di micron, reagiscono riposizionandosi, e ogni riposizionamento e' una lettura mancata da ripetere. Le famiglie destinate all'uso continuo integrano sensori che misurano quella vibrazione e correggono il servomeccanismo in tempo reale.

La cosa da sapere e' che il beneficio non e' lineare con il numero di dischi: e' trascurabile con uno o due, diventa misurabile da quattro in su e significativo nelle gabbie dense da otto alloggiamenti, dove i produttori indicano cali prestazionali importanti sui dischi che ne sono privi. In una macchina domestica con due o tre dischi e' quindi la differenza meno rilevante fra le quattro, ed e' utile saperlo per non pagarla quando non serve.

### Registrazione convenzionale contro sovrapposta

La registrazione convenzionale scrive tracce affiancate e indipendenti. La registrazione sovrapposta le fa parzialmente accavallare come le tegole di un tetto, guadagnando densita' a un prezzo preciso: riscrivere una traccia obbliga a riscrivere anche quelle che le stanno sopra, quindi ogni scrittura casuale su una zona gia' piena innesca una catena di riscritture. Il disco la nasconde con un'area cuscinetto gestita come cache, e finche' il carico e' a raffiche il trucco funziona; quando il carico e' sostenuto la cuscinetto si esaurisce e la velocita' crolla di un ordine di grandezza.

E' la trappola d'acquisto piu' insidiosa perche' non si vede nella scheda tecnica, dove compaiono capacita' e velocita' di punta identiche, e perche' diversi produttori hanno immesso dischi sovrapposti in serie da tavolo senza dichiararlo in evidenza. Su un insieme ridondante la penalita' colpisce nel momento peggiore: la ricostruzione dopo un guasto e' precisamente un flusso di scritture sostenute su un disco intero, quindi una ricostruzione che dovrebbe durare ore ne dura giorni, e il pool resta senza ridondanza per tutto quel tempo. La regola operativa e' semplice e non ammette scorciatoie: si verifica la tecnologia sul modello esatto prima di comprare, e in assenza di dichiarazione si assume il peggio.

## Unita' a stato solido

Nell'elettronica a stato solido i quattro parametri sopra non hanno senso, perche' non ci sono testine ne' piatti. La divisione fra generico e destinato all'uso continuo esiste comunque, e passa altrove.

### Resistenza alla scrittura

Ogni cella di memoria sopporta un numero finito di cicli di cancellazione e riscrittura. I produttori esprimono il limite in due modi equivalenti: i terabyte scritti complessivi che la garanzia copre, oppure le riscritture complete al giorno sostenibili per tutta la durata della garanzia. Un'unita' di fascia consumer si colloca tipicamente attorno a un decimo o due decimi di riscrittura completa al giorno; una di fascia professionale dichiara una riscrittura al giorno o piu', cioe' da cinque a dieci volte tanto.

Come per il carico annuo dei dischi meccanici, il numero conta solo confrontato con il proprio uso, e in un contesto domestico la soglia e' quasi sempre lontana. Diventa vicina in un solo caso, quello in cui l'unita' assorbe scritture che non le appartengono, come accade a un dispositivo di log delle scritture sincrone.

### La protezione dalla perdita di alimentazione

E' la differenza che conta di piu' ed e' quella che quasi nessuno guarda. Un'unita' a stato solido non scrive subito nella memoria permanente: accumula in un buffer interno e scrive a blocchi, perche' e' cosi' che la memoria funziona. Se l'alimentazione manca in quell'istante, cio' che sta nel buffer sparisce, e il sistema operativo aveva gia' ricevuto conferma che il dato era al sicuro.

Le unita' destinate all'uso continuo montano condensatori che conservano energia sufficiente a svuotare il buffer nella memoria permanente mentre tutto il resto si spegne. E' una differenza fisica, verificabile a occhio sul circuito, e non un'impostazione del firmware. Va distinta con attenzione da cio' che diverse unita' consumer chiamano con nomi simili, che protegge i dati gia' scritti nella memoria dal danneggiamento durante una caduta di tensione ma non salva il contenuto del buffer: sono due garanzie diverse e solo una delle due e' quella che serve.

La conseguenza pratica riguarda un ruolo preciso. Un dispositivo che raccoglie il log delle scritture sincrone esiste per una ragione sola, garantire che una scrittura confermata sopravviva a una perdita di alimentazione: affidarlo a un'unita' che in quella circostanza perde il proprio buffer significa costruire la garanzia sopra la cosa che non la offre. E' la ragione tecnica, e non una preferenza, per cui [la guida all'assemblaggio](../../03-spunti-di-sviluppo/02-storage-di-rete-nas/04-guida-assemblaggio-e-installazione-truenas.md) ha gia' escluso quel ruolo dai due NVMe di fascia consumer di questo progetto.

### La cache veloce dinamica, e il crollo che nasconde

Le unita' consumer moderne usano una porzione della propria memoria in una modalita' piu' veloce e meno densa, come area di transito per le scritture in arrivo. Finche' quell'area basta, l'unita' mostra la velocita' pubblicizzata; quando si esaurisce, perche' la scrittura e' piu' lunga di quanto l'area contenga, la velocita' scende alla velocita' vera della memoria sottostante, che puo' essere cinque o dieci volte inferiore e in alcuni casi peggiore di un disco meccanico.

Non e' un difetto: e' una scelta di progetto ragionevole per il profilo d'uso domestico, fatto di scritture brevi. Diventa un problema quando il profilo e' un altro, cioe' quando si copiano decine di gigabyte di fila, ed e' precisamente il motivo per cui le prove di velocita' brevi non descrivono il comportamento di un archivio. Le unita' destinate all'uso continuo tengono una velocita' piu' bassa sulla carta ma costante fino alla fine, ed e' una proprieta' che si chiama coerenza e vale piu' del picco.

Vi si accompagna la latenza di coda, cioe' il tempo oltre il quale cade solo una richiesta su mille. Un'unita' consumer che in media risponde benissimo puo' avere code sporadiche molto lunghe, prodotte dalla manutenzione interna della memoria che decide da sola quando girare; un'unita' professionale dichiara e rispetta un tetto. In un archivio domestico e' la meno pressante delle differenze, ma e' quella che spiega le pause inattese durante una copia lunga.

### Lo spazio di riserva

Le unita' destinate all'uso continuo riservano una quota di memoria non visibile al sistema, dal sette al ventotto per cento, che il controller usa per la manutenzione interna e per rimpiazzare le celle esauste. E' la ragione per cui la stessa memoria fisica viene venduta come cinquecentododici gigabyte in una serie e come quattrocentottanta in un'altra piu' cara: i trentadue gigabyte di differenza non mancano, sono di riserva.

Una cosa utile da sapere e' che quella riserva si puo' creare a mano su un'unita' consumer, semplicemente lasciando una porzione del supporto mai partizionata. Non e' equivalente a comprare l'unita' giusta, perche' non aggiunge i condensatori ne' cambia la qualita' della memoria, ma allunga la vita e stabilizza le prestazioni a costo zero.

## Come si legge questo progetto alla luce di quanto sopra

I due dischi a stato solido dell'insieme di avvio e i due NVMe da un terabyte destinati al pool delle applicazioni sono tutti di fascia consumer, e va bene cosi'. Per l'avvio la scelta corretta e' lo specchio, che rende irrilevante la resistenza alla scrittura del singolo, e il carico e' comunque minimo. Per le applicazioni in contenitore il profilo e' fatto di accessi casuali brevi, cioe' esattamente cio' in cui anche un'unita' consumer eccelle, e lo specchio copre il guasto del singolo.

I dischi meccanici recuperati dal NAS dismesso sono invece da tavolo su tutti e quattro i fronti descritti: senza recupero a tempo limitato, senza sensori di vibrazione, con carico annuo dichiarato basso. Sono a registrazione convenzionale, che e' l'unica delle quattro proprieta' che conta davvero in questo contesto, e sono privi delle altre tre in modo tollerabile perche' i dischi sono pochi, il filesystem non li espelle e il carico e' domestico.

Il principio che lega le due meta' di questa scheda e' quindi uno solo. La distinzione fra generico e destinato all'uso continuo non e' una gerarchia di qualita' in cui il piu' caro e' sempre meglio, e' una differenza di profilo: sono supporti progettati per stare accesi sempre, per fallire in fretta invece che a lungo, e per comportarsi allo stesso modo al decimo minuto di una copia e al primo. Dove il profilo d'uso non esercita quelle proprieta', pagarle e' spesa che non produce nulla; dove invece le esercita, risparmiarle si paga nel momento peggiore, cioe' durante una ricostruzione.

[^1]: *RAID*, Redundant Array of Independent Disks - insieme di dischi presentati come un volume solo, con schemi che distribuiscono i dati e una quota di ridondanza per sopravvivere al guasto di una o piu' unita'.

[^2]: *ZFS*, Zettabyte File System - filesystem che unisce gestione dei volumi e somme di controllo end-to-end, capace di accorgersi che un dato letto e' diverso da quello scritto e di ripararlo dalla copia ridondante.
