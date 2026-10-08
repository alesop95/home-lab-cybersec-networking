# Dischi e SSD per uso continuo contro uso generico

Scheda di concetto generale, scritta il 22/09/2026. Spiega che cosa distingue davvero un disco meccanico o un'unità a stato solido destinati a stare accesi sempre dentro un apparato di archiviazione in rete da uno generico venduto per un computer da tavolo, e perché la differenza non sta quasi mai dove la si cerca, cioè nella velocità. Serve come riferimento per le scelte di acquisto e come chiave di lettura dei componenti già presenti nel progetto; il caso applicato ai quattro dischi recuperati sta in [Quattro dischi recuperati da un NAS QNAP dismesso](../../03-spunti-di-sviluppo/02-storage-di-rete-nas/07-dischi-recuperati-dal-nas-qnap-dismesso.md).

## L'equivoco di partenza

La domanda che si pone quasi sempre è quale disco sia più veloce, e quasi sempre è la domanda sbagliata. In un archivio di rete domestico il limite non è il disco: un solo disco meccanico moderno satura già in sequenziale una rete a un gigabit, che si ferma attorno ai centodieci megabyte al secondo, e anche una rete a due gigabit e mezzo viene servita da una coppia di dischi qualunque. Comprare velocità che la rete non trasporta è spesa che non arriva mai al client.

Ciò che un uso continuo chiede davvero è una cosa diversa, ed è comportamento prevedibile. Prevedibile quando il supporto incontra un errore, perché la differenza fra un apparato che continua a servire e uno che si ferma sta in come il supporto reagisce al primo settore difficile. Prevedibile sotto carico prolungato, perché il profilo di scrittura di un archivio non è una raffica di dieci minuti seguita da ore di inattività ma un flusso che dura quanto dura la copia. Prevedibile in presenza di altri supporti, perché quattro dischi che girano nella stessa gabbia non sono quattro dischi isolati. Ed è su queste tre cose, non sulla velocità di punta, che le famiglie destinate all'uso continuo si distinguono.

## Dischi meccanici

### Il recupero d'errore a tempo limitato, che è la differenza più importante

Quando un disco incontra un settore che non riesce a leggere al primo tentativo, entra in una procedura di recupero: riposiziona la testina, rilegge, applica correzioni progressivamente più aggressive. Un disco da tavolo insiste finché ci riesce, e può impiegare trenta secondi o più, perché nel computer di casa quel comportamento è corretto: meglio un'attesa lunga che un file perso, dato che non esiste una seconda copia da cui attingere.

Dentro un insieme ridondante quella logica si capovolge, perché una seconda copia esiste. Il recupero d'errore a tempo limitato, che i produttori chiamano con nomi diversi a seconda della marca, impone al disco di arrendersi entro sette secondi e di dichiarare il fallimento, così che il livello superiore vada a prendere il dato dalla copia e riscriva il settore. Il disco da tavolo, che invece non si arrende, produce un effetto che sorprende chi lo osserva la prima volta: un controller RAID[^1] classico lo considera non rispondente e lo espelle dall'insieme come guasto, pur essendo un disco perfettamente sano che stava soltanto lavorando. Da qui viene la fama dei dischi da tavolo che cadono fuori dagli array, che non è un difetto di affidabilità ma di protocollo.

Su un filesystem a somme di controllo come ZFS[^2] il meccanismo è diverso, perché non c'è un controller che decide di espellere, e questo è il motivo per cui un disco privo di recupero a tempo limitato vi resta utilizzabile. Il problema però si sposta invece di sparire: il disco che insiste blocca l'ingresso e uscita del proprio gruppo per tutta la durata del tentativo, e il livello a blocchi del sistema operativo, che di suo dichiara fallita un'operazione dopo trenta secondi, la interrompe mentre il disco sta ancora lavorando. La contromisura corretta è controintuitiva e consiste nell'alzare quel timeout invece di abbassarlo, perché un disco lasciato finire spesso torna con il dato buono, ed è esattamente il dato che serve.

### Il carico annuo dichiarato

I produttori dichiarano per ogni famiglia un volume di dati letti e scritti all'anno entro il quale la garanzia e le stime di affidabilità valgono. Le serie da tavolo si collocano attorno ai cinquantacinque terabyte all'anno, che descrivono bene un computer usato di giorno e spento di notte. Le serie destinate all'uso continuo dichiarano centottanta terabyte all'anno, e quelle professionali trecento.

Il numero da solo dice poco finché non lo si confronta con il proprio uso, ed è un confronto che quasi sempre rassicura in un contesto domestico: un archivio di famiglia con qualche centinaio di gigabyte di movimento al mese sta comodamente dentro il limite anche di una serie da tavolo. Il conto cambia se si aggiungono le letture degli scrub periodici e delle ricostruzioni, perché uno scrub mensile su un pool da due terabyte legge due terabyte, cioè ventiquattro terabyte all'anno di solo controllo, e una ricostruzione ne legge altrettanti in una volta sola. Il dato utile non è quindi il limite in sé ma la consapevolezza che gli automatismi che proteggono i dati consumano anch'essi carico dichiarato.

### I sensori di vibrazione rotazionale

Un piatto che gira a settemiladuecento giri produce vibrazione, e più dischi nella stessa gabbia se la trasmettono attraverso il telaio. Le testine, che devono restare allineate su tracce larghe frazioni di micron, reagiscono riposizionandosi, e ogni riposizionamento è una lettura mancata da ripetere. Le famiglie destinate all'uso continuo integrano sensori che misurano quella vibrazione e correggono il servomeccanismo in tempo reale.

La cosa da sapere è che il beneficio non è lineare con il numero di dischi: è trascurabile con uno o due, diventa misurabile da quattro in su e significativo nelle gabbie dense da otto alloggiamenti, dove i produttori indicano cali prestazionali importanti sui dischi che ne sono privi. In una macchina domestica con due o tre dischi è quindi la differenza meno rilevante fra le quattro, ed è utile saperlo per non pagarla quando non serve.

### Registrazione convenzionale contro sovrapposta

La registrazione convenzionale scrive tracce affiancate e indipendenti. La registrazione sovrapposta le fa parzialmente accavallare come le tegole di un tetto, guadagnando densità a un prezzo preciso: riscrivere una traccia obbliga a riscrivere anche quelle che le stanno sopra, quindi ogni scrittura casuale su una zona già piena innesca una catena di riscritture. Il disco la nasconde con un'area cuscinetto gestita come cache, e finché il carico è a raffiche il trucco funziona; quando il carico è sostenuto la cuscinetto si esaurisce e la velocità crolla di un ordine di grandezza.

È la trappola d'acquisto più insidiosa perché non si vede nella scheda tecnica, dove compaiono capacità e velocità di punta identiche, e perché diversi produttori hanno immesso dischi sovrapposti in serie da tavolo senza dichiararlo in evidenza. Su un insieme ridondante la penalità colpisce nel momento peggiore: la ricostruzione dopo un guasto è precisamente un flusso di scritture sostenute su un disco intero, quindi una ricostruzione che dovrebbe durare ore ne dura giorni, e il pool resta senza ridondanza per tutto quel tempo. La regola operativa è semplice e non ammette scorciatoie: si verifica la tecnologia sul modello esatto prima di comprare, e in assenza di dichiarazione si assume il peggio.

## Unità a stato solido

Nell'elettronica a stato solido i quattro parametri sopra non hanno senso, perché non ci sono testine né piatti. La divisione fra generico e destinato all'uso continuo esiste comunque, e passa altrove.

### Resistenza alla scrittura

Ogni cella di memoria sopporta un numero finito di cicli di cancellazione e riscrittura. I produttori esprimono il limite in due modi equivalenti: i terabyte scritti complessivi che la garanzia copre, oppure le riscritture complete al giorno sostenibili per tutta la durata della garanzia. Un'unità di fascia consumer si colloca tipicamente attorno a un decimo o due decimi di riscrittura completa al giorno; una di fascia professionale dichiara una riscrittura al giorno o più, cioè da cinque a dieci volte tanto.

Come per il carico annuo dei dischi meccanici, il numero conta solo confrontato con il proprio uso, e in un contesto domestico la soglia è quasi sempre lontana. Diventa vicina in un solo caso, quello in cui l'unità assorbe scritture che non le appartengono, come accade a un dispositivo di log delle scritture sincrone.

### La protezione dalla perdita di alimentazione

È la differenza che conta di più ed è quella che quasi nessuno guarda. Un'unità a stato solido non scrive subito nella memoria permanente: accumula in un buffer interno e scrive a blocchi, perché è così che la memoria funziona. Se l'alimentazione manca in quell'istante, ciò che sta nel buffer sparisce, e il sistema operativo aveva già ricevuto conferma che il dato era al sicuro.

Le unità destinate all'uso continuo montano condensatori che conservano energia sufficiente a svuotare il buffer nella memoria permanente mentre tutto il resto si spegne. È una differenza fisica, verificabile a occhio sul circuito, e non un'impostazione del firmware. Va distinta con attenzione da ciò che diverse unità consumer chiamano con nomi simili, che protegge i dati già scritti nella memoria dal danneggiamento durante una caduta di tensione ma non salva il contenuto del buffer: sono due garanzie diverse e solo una delle due è quella che serve.

La conseguenza pratica riguarda un ruolo preciso. Un dispositivo che raccoglie il log delle scritture sincrone esiste per una ragione sola, garantire che una scrittura confermata sopravviva a una perdita di alimentazione: affidarlo a un'unità che in quella circostanza perde il proprio buffer significa costruire la garanzia sopra la cosa che non la offre. È la ragione tecnica, e non una preferenza, per cui [la guida all'assemblaggio](../../03-spunti-di-sviluppo/02-storage-di-rete-nas/04-guida-assemblaggio-e-installazione-truenas.md) ha già escluso quel ruolo dai due NVMe di fascia consumer di questo progetto.

### La cache veloce dinamica, e il crollo che nasconde

Le unità consumer moderne usano una porzione della propria memoria in una modalità più veloce e meno densa, come area di transito per le scritture in arrivo. Finché quell'area basta, l'unità mostra la velocità pubblicizzata; quando si esaurisce, perché la scrittura è più lunga di quanto l'area contenga, la velocità scende alla velocità vera della memoria sottostante, che può essere cinque o dieci volte inferiore e in alcuni casi peggiore di un disco meccanico.

Non è un difetto: è una scelta di progetto ragionevole per il profilo d'uso domestico, fatto di scritture brevi. Diventa un problema quando il profilo è un altro, cioè quando si copiano decine di gigabyte di fila, ed è precisamente il motivo per cui le prove di velocità brevi non descrivono il comportamento di un archivio. Le unità destinate all'uso continuo tengono una velocità più bassa sulla carta ma costante fino alla fine, ed è una proprietà che si chiama coerenza e vale più del picco.

Vi si accompagna la latenza di coda, cioè il tempo oltre il quale cade solo una richiesta su mille. Un'unità consumer che in media risponde benissimo può avere code sporadiche molto lunghe, prodotte dalla manutenzione interna della memoria che decide da sola quando girare; un'unità professionale dichiara e rispetta un tetto. In un archivio domestico è la meno pressante delle differenze, ma è quella che spiega le pause inattese durante una copia lunga.

### Lo spazio di riserva

Le unità destinate all'uso continuo riservano una quota di memoria non visibile al sistema, dal sette al ventotto per cento, che il controller usa per la manutenzione interna e per rimpiazzare le celle esauste. È la ragione per cui la stessa memoria fisica viene venduta come cinquecentododici gigabyte in una serie e come quattrocentottanta in un'altra più cara: i trentadue gigabyte di differenza non mancano, sono di riserva.

Una cosa utile da sapere è che quella riserva si può creare a mano su un'unità consumer, semplicemente lasciando una porzione del supporto mai partizionata. Non è equivalente a comprare l'unità giusta, perché non aggiunge i condensatori né cambia la qualità della memoria, ma allunga la vita e stabilizza le prestazioni a costo zero.

## Come si legge questo progetto alla luce di quanto sopra

I due dischi a stato solido dell'insieme di avvio e i due NVMe da un terabyte, che dal 07/10/2026 formano l'unico pool e portano applicazioni e dati insieme perché il NAS parte senza dischi meccanici, sono tutti di fascia consumer, e va bene così. Per l'avvio la scelta corretta è lo specchio, che rende irrilevante la resistenza alla scrittura del singolo, e il carico è comunque minimo. Per le applicazioni in contenitore il profilo è fatto di accessi casuali brevi, cioè esattamente ciò in cui anche un'unità consumer eccelle, e lo specchio copre il guasto del singolo. Per i dati, su un carico domestico di condivisione file, la resistenza alla scrittura di un NVMe consumer da un terabyte è lontana dall'essere il limite, che resta la capacità.

I dischi meccanici che si attendevano da un NAS dismesso, e che non si sono resi disponibili, erano invece da tavolo su tutti e quattro i fronti descritti, e il ragionamento resta come esempio di come si valuta un disco usato: senza recupero a tempo limitato, senza sensori di vibrazione, con carico annuo dichiarato basso. Erano a registrazione convenzionale, che è l'unica delle quattro proprietà che conta davvero in questo contesto, e privi delle altre tre in modo tollerabile perché i dischi sono pochi, il filesystem non li espelle e il carico è domestico.

Il principio che lega le due metà di questa scheda è quindi uno solo. La distinzione fra generico e destinato all'uso continuo non è una gerarchia di qualità in cui il più caro è sempre meglio, è una differenza di profilo: sono supporti progettati per stare accesi sempre, per fallire in fretta invece che a lungo, e per comportarsi allo stesso modo al decimo minuto di una copia e al primo. Dove il profilo d'uso non esercita quelle proprietà, pagarle è spesa che non produce nulla; dove invece le esercita, risparmiarle si paga nel momento peggiore, cioè durante una ricostruzione.

[^1]: *RAID*, Redundant Array of Independent Disks - insieme di dischi presentati come un volume solo, con schemi che distribuiscono i dati e una quota di ridondanza per sopravvivere al guasto di una o più unità.

[^2]: *ZFS*, Zettabyte File System - filesystem che unisce gestione dei volumi e somme di controllo end-to-end, capace di accorgersi che un dato letto è diverso da quello scritto e di ripararlo dalla copia ridondante.
