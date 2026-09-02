# Consumo elettrico del NAS e finestra di accensione

> Analisi del costo di esercizio della macchina descritta in [Consolidamento di quattro desktop dismessi in un NAS](03-consolidamento-di-quattro-desktop-dismessi-in-un-nas.md), e progetto della finestra oraria di accensione che ne discende. Le tariffe sono reali e prese dalle bollette dell'abitazione, secondo la regola che tiene reali le cifre di un'offerta commerciale e anonimizza il fornitore e i codici di contratto. Il nome del fornitore, il codice dell'offerta, il codice di prelievo e l'intestazione del contratto non compaiono qui e vivono nel materiale non versionato.

## Stato di questo documento

Le tariffe sono misurate su sei bollette mensili consecutive del 2026. Il consumo della macchina è **stimato per componenti** e non misurato, perché la macchina non è ancora stata assemblata: l'incertezza dichiarata è di circa il trenta per cento, e la sezione sulla misura dice come chiuderla. La finestra di accensione è una decisione presa, non ancora attuata.

## Il numero da cui dipende tutto: il costo marginale

C'è una distinzione che va vista prima di qualunque stima, perché sbagliarla porta a conclusioni sbagliate di un fattore due.

Dividendo la spesa totale del semestre per i kilowattora consumati si ottiene un prezzo apparente di circa **0,558 euro per kilowattora**. Non è la tariffa: è la conseguenza di dividere anche i costi fissi mensili, che su questa fornitura ammontano a circa ventiquattro euro fra quota fissa, quota potenza e gestione amministrativa, su un consumo domestico basso. Quel numero **scenderebbe da solo** se il consumo aumentasse, senza che nessuna tariffa cambi, e per questo non serve a decidere niente.

Il numero che serve è il **costo marginale**, cioè quanto costa un kilowattora in più, perché i costi fissi si pagano comunque, che il NAS[^1] ci sia o no. Si ottiene sommando la quota per consumi, l'accisa domestica e l'imposta sul valore aggiunto.

| Componente | Valore |
|---|---|
| Quota per consumi, media su quattro mesi rilevati | 0,210311 €/kWh |
| di cui spesa per la vendita di energia | 0,165301 €/kWh |
| di cui spesa per la rete e gli oneri generali | 0,045011 €/kWh |
| Accisa domestica | 0,022700 €/kWh |
| Imposta sul valore aggiunto | 10% |
| **Costo marginale** | **0,256 €/kWh** |

L'offerta è a prezzo variabile indicizzato al prezzo unico nazionale per fasce orarie, con aggiornamento mensile, quindi la quota per consumi oscilla: nei quattro mesi con il dettaglio disponibile va da 0,1957 a 0,2200 euro per kilowattora, cioè il costo marginale varia fra 0,240 e 0,267. La variabilità è più piccola dell'incertezza sulla stima del consumo, quindi si usa il valore medio senza perdere significato.

Va notato che la componente di rete e oneri generali è **stabile a 0,045 euro per kilowattora** mentre tutta l'oscillazione sta nella vendita di energia. È una distinzione utile perché dice che l'esposizione al mercato riguarda meno di quattro quinti del costo variabile, non tutto.

## Quanto consuma la macchina

### Perché conta il consumo a riposo

Un archivio di rete domestico è a riposo oltre il novantacinque per cento del tempo: serve file quando qualcuno li chiede, e nessuno li chiede continuamente. La bolletta la determina il consumo a riposo moltiplicato per le ore di accensione, non il picco.

C'è inoltre una circostanza che aiuta e che è specifica di questa architettura: il carico di servizio dei file **non fa lavorare il processore**. Il tetto è il collegamento gigabit, e il processore installato lo satura senza accorgersene. Il consumo sotto carico è quindi poco più alto di quello a riposo, esattamente il contrario di quanto accade su una macchina da calcolo, dove il picco è multiplo del riposo.

### La somma per componenti

| Componente | A riposo | Nota |
|---|---|---|
| Processore | 4-8 W | i 65 W di targa sono il massimo sotto carico, non il riposo |
| Scheda madre, chipset, regolatori di tensione | 15-20 W | la voce più grossa e la meno comprimibile |
| 32 GB di memoria su quattro moduli | 4-6 W | circa 1-1,5 W per modulo |
| Due SSD SATA | 0,5-1 W | trascurabili |
| Due NVMe | 2-4 W | dipende dagli stati di risparmio attivi |
| Scheda di rete aggiuntiva | 1-1,5 W | |
| Ventole | 2-5 W | |
| **Somma in continua** | **29-46 W** | |
| Perdita di conversione dell'alimentatore | +20-30% | vedi la sezione dedicata |
| **Alla presa, senza dischi meccanici** | **40-55 W** | stima centrale 48 W |
| Due dischi meccanici da 3,5 pollici in rotazione | +11-16 W | 4-6 W ciascuno, più la perdita di conversione |
| **Alla presa, configurazione completa** | **52-70 W** | stima centrale 60 W |

## L'alimentatore, e un fatto controintuitivo sull'efficienza

Questa è la parte dell'analisi con il maggior valore trasferibile ad altri progetti, perché il ragionamento vale ogni volta che si costruisce una macchina a basso consumo e funzionamento continuo.

Un alimentatore raggiunge la sua efficienza migliore attorno al cinquanta per cento del carico nominale, e la perde rapidamente scendendo. Una macchina che assorbe trenta o quaranta watt in continua da un alimentatore da quattrocento o cinquecento watt lavora attorno al **dieci per cento** del carico, che è la zona peggiore della curva.

Ne discende una conseguenza che sorprende: **un alimentatore più piccolo è migliore, non peggiore**, purché copra il picco. La certificazione di efficienza più diffusa misura il rendimento al venti, al cinquanta e al cento per cento del carico, e non dice nulla su cosa accade al dieci per cento; soltanto il livello più alto della scala specifica anche il rendimento al dieci per cento. Un alimentatore da settecentocinquanta watt certificato, a quaranta watt di carico, può quindi rendere peggio di uno da trecento non certificato.

La differenza fra un alimentatore mal dimensionato e uno adatto, in quella zona di carico, è di **cinque a dieci watt continui**. Su un anno di funzionamento sono da quarantaquattro a ottantotto kilowattora, cioè da undici a ventidue euro: una cifra piccola in assoluto ma pari a un decimo del costo di esercizio, ottenuta senza comprare niente.

### Come si scegliono, quando se ne hanno molti

Il progetto dispone degli alimentatori di tutte le macchine dismesse, e la scelta si fa in due fasi.

La prima fase è documentale e si fa leggendo le etichette. Serve la potenza nominale totale, il livello di certificazione di efficienza se presente, la corrente disponibile sulla linea a dodici volt, che è quella da cui si alimenta praticamente tutto in una macchina moderna, il numero di connettori di alimentazione per dischi SATA, e la data di fabbricazione. Quest'ultima conta più di quanto si pensi: i condensatori elettrolitici degradano con il tempo e con il calore, e un alimentatore di dodici anni, anche di buona marca, può avere una capacità residua molto inferiore alla nominale.

Il criterio di selezione, in ordine di importanza, è dunque la **potenza nominale più bassa** che copra il picco con margine, poi la **certificazione più alta**, poi la **data più recente**, e infine la disponibilità dei connettori necessari.

Il picco da coprire non è il consumo a riposo. All'accensione i dischi meccanici assorbono da venti a venticinque watt ciascuno per qualche secondo, mentre i motori raggiungono la velocità di regime. Con due dischi meccanici, i due SSD e il resto della macchina, il picco realistico sta fra centocinquanta e duecento watt: un alimentatore da trecento watt è già abbondante, uno da cinquecento è sovradimensionato di un fattore due e mezzo, e ogni watt di sovradimensionamento peggiora il rendimento nella zona in cui la macchina lavora per il resto del tempo.

La seconda fase è la misura, ed è quella che decide. Con un misuratore di consumo da presa si legge l'assorbimento alla presa della macchina a riposo, si spegne, si sostituisce l'alimentatore con un altro candidato, e si rilegge nella stessa condizione. **La differenza fra le due letture è direttamente la differenza di rendimento fra i due alimentatori**, misurata sul carico reale invece che dedotta da una certificazione ottenuta a un carico diverso. È un confronto che nessuna scheda tecnica può darti, e si fa con dieci euro di strumento.

## Il rapporto che cambia la prospettiva

Il costo assoluto di esercizio, con la stima centrale della configurazione completa a funzionamento continuo, è di circa **undici euro al mese** e **centotrentacinque euro all'anno**, con un intervallo onesto fra sette e tredici euro al mese.

Il dato interessante non è però il valore assoluto ma il rapporto con il consumo esistente. L'abitazione consuma circa **ottantasette kilowattora al mese**, cioè intorno a mille kilowattora all'anno, che è una frazione della media domestica nazionale. Il NAS a funzionamento continuo ne consumerebbe **quarantaquattro al mese**.

**Il NAS aumenterebbe il consumo elettrico dell'abitazione di circa la metà.** Nei mesi estivi, in cui il consumo rilevato è sceso a sessanta e sessantadue kilowattora, l'archivio di rete da solo sarebbe oltre il quaranta per cento del totale e diventerebbe con ogni probabilità il singolo apparato che consuma più di ogni altro nella casa.

La ragione non è che sessanta watt siano molti: sono meno di una vecchia lampadina a incandescenza. È che il funzionamento è continuo, e che l'abitazione consuma poco. **Un apparato acceso ventiquattro ore su ventiquattro pesa in proporzione a quanto è basso tutto il resto**, ed è il tempo di accensione e non la potenza a determinare il costo.

Da qui la decisione della sezione seguente, che senza questo rapporto sarebbe sembrata una raffinatezza inutile.

## La finestra di accensione

### La decisione

La macchina non resta accesa ventiquattro ore su ventiquattro. Resta spenta nelle ore notturne, con due orari diversi fra i giorni lavorativi e il fine settimana.

| Notte | Spegnimento | Riaccensione | Ore spenta |
|---|---|---|---|
| Da domenica a giovedì, cinque notti | 23:30 | 07:30 | 8 |
| Venerdì e sabato, due notti | 02:30 | 07:30 | 5 |
| **Totale settimanale** | | | **50 su 168** |

Ne risultano centodiciotto ore di accensione a settimana, cioè circa il **settanta per cento** del tempo, e circa cinquecentotredici ore al mese.

### Che cosa si risparmia, senza esagerare

| | Continuo | Con la finestra | Differenza |
|---|---|---|---|
| Ore accese al mese | 730 | 513 | -217 |
| Consumo a 60 W | 43,8 kWh | 30,8 kWh | -13,0 kWh |
| Spesa mensile | 11,22 € | 7,88 € | **-3,34 €** |
| Spesa annua | 134,60 € | 94,60 € | **-40,00 €** |
| Incremento sul consumo di casa | +50% | **+35%** | |

Il risparmio è di **quaranta euro all'anno**, cioè il **trenta per cento** del costo di esercizio. Va detto con precisione perché una valutazione preliminare, fatta ipotizzando quattro ore di accensione al giorno, aveva indicato un fattore sei: con una finestra di sedici o diciassette ore quel fattore non si realizza, e il risparmio reale è di un terzo. Resta un risparmio vero, ma di un ordine di grandezza diverso da quello ipotizzato prima di avere gli orari.

Ci sono inoltre due benefici non monetari che non compaiono in tabella. Duemilaseicento ore all'anno in meno di funzionamento su ogni componente, dischi meccanici compresi, e nessun rumore di ventole e di dischi durante la notte, che su una macchina collocata in un ambiente abitato non è irrilevante.

### Come si attua: due meccanismi, non uno

Lo spegnimento e la riaccensione hanno bisogno di meccanismi diversi, e questa è la parte in cui un progetto approssimativo si rompe.

Lo **spegnimento** si programma dal sistema operativo, con un'attività pianificata che invochi un arresto ordinato. Deve essere un arresto e non un'interruzione di alimentazione: il file system è transazionale e non si corromperebbe nemmeno con un taglio brusco, ma le scritture in volo si perderebbero comunque, e una macchina il cui scopo è custodire dati non si spegne strappando la spina. Il vantaggio di programmare lo spegnimento dal sistema è che l'attività pianificata distingue i giorni della settimana, che è esattamente ciò che serve avendo due orari diversi.

La **riaccensione** non può venire dal sistema operativo, perché a macchina spenta il sistema non gira. Viene dal firmware, e il manuale della scheda documenta la voce che serve nella sezione di gestione dell'alimentazione: un allarme dell'orologio in tempo reale, per cui si impostano giorni, ore, minuti e secondi, che genera un evento di accensione. È la soluzione corretta perché non dipende da nessun apparato esterno, a differenza del risveglio da rete, che pure la scheda supporta ma che richiederebbe qualcosa che invii il pacchetto di risveglio nel momento giusto.

L'allarme del firmware ammette però **un solo orario giornaliero**, mentre la decisione ne prevede due. La soluzione è impostarlo sull'orario **più precoce**, cioè quello dei giorni lavorativi, accettando che nel fine settimana la macchina si accenda un'ora e mezza prima del necessario. Il costo di quella semplificazione è di circa tre ore di accensione in più a settimana, cioè meno di trenta centesimi al mese: una cifra che non giustifica di complicare la configurazione.

### Che cosa si rompe, e come si sistema

Una finestra di accensione rompe tre cose, e vanno affrontate esplicitamente perché il guasto non si manifesta subito.

Le **attività pianificate non girano a macchina spenta**. Le istantanee periodiche e la verifica periodica dell'integrità del pool sono programmate a orari fissi, e se quegli orari cadono nella finestra di spegnimento semplicemente non si eseguono, senza che nessuno lo segnali. Vanno ricollocate dentro la finestra di accensione, e va verificato che ci stiano per intero.

Questa seconda condizione merita attenzione, perché la verifica dell'integrità di un pool di alcuni terabyte richiede diverse ore. Il compito che il sistema crea da sé alla creazione del pool è programmato a mezzanotte del sabato, che con questa finestra cade nelle due ore e mezza che precedono lo spegnimento del venerdì notte: la verifica partirebbe e verrebbe interrotta. Va spostata a un orario che disponga di tutta la durata necessaria, per esempio la mattina del sabato subito dopo la riaccensione, che precede lo spegnimento successivo di diciannove ore.

I **salvataggi automatici notturni da altri apparati non trovano la destinazione**. È il conflitto più sostanziale, perché essere la destinazione dei backup della rete è uno degli usi principali di un archivio di rete, e la notte è la finestra in cui quei backup si programmano naturalmente. Se questo uso è previsto, gli orari dei backup vanno portati dentro la finestra di accensione, oppure la finestra va ripensata.

L'**impostazione di riaccensione dopo un'interruzione di corrente interagisce con la finestra**. Quella impostazione, che vale il requisito per cui la macchina è stata scelta, riaccende incondizionatamente: se un'interruzione avviene durante la finestra di spegnimento, la macchina si accende fuori orario e resta accesa fino allo spegnimento programmato successivo. La conseguenza economica è di pochi centesimi e la si può ignorare. Esiste un'alternativa che ripristina lo stato precedente invece di accendere, e sarebbe più coerente con la finestra, ma introduce un modo di fallire peggiore, cioè una macchina che resta spenta quando la si vuole accesa. Poiché l'allarme del firmware la riaccende comunque all'orario previsto, la scelta incondizionata resta preferibile per semplicità.

Un timore che invece **non** si realizza riguarda l'usura dei dischi. Uno spegnimento al giorno significa circa trecentosessantacinque cicli di avvio e arresto all'anno sui dischi meccanici, mentre le specifiche dei dischi destinati all'uso continuo dichiarano tolleranze di decine di migliaia di cicli. Non è una sollecitazione significativa, ed è una cosa diversa dalla sospensione aggressiva dei dischi durante il funzionamento, che invece produce cicli molto più frequenti e va valutata a parte.

## Misurare invece di stimare

Tutta la stima del consumo ha un'incertezza di circa il trenta per cento, perché somma intervalli invece di valori. Un misuratore di consumo da presa costa dieci o quindici euro e la trasforma in una misura.

Le letture che servono sono quattro, e vanno prese in condizioni dichiarate. A macchina spenta ma collegata, per conoscere il consumo di attesa e decidere se convenga un interruttore a monte. A riposo con il sistema avviato e nessun accesso, lasciando stabilizzare qualche minuto: **è la lettura che determina la bolletta**, perché descrive la condizione in cui la macchina passa quasi tutto il tempo. Durante un trasferimento a piena velocità da un client, per il picco realistico d'uso. E durante una verifica dell'integrità del pool, che è il carico più alto che la macchina produce per conto proprio, con tutti i dischi letti insieme.

Con la seconda lettura il calcolo diventa esatto: i watt misurati, moltiplicati per le ore di accensione mensili e divisi per mille, moltiplicati per il costo marginale, danno la spesa in euro.

Il momento giusto per misurare è durante il collaudo dell'assemblaggio, quando la macchina è installata e non contiene ancora dati, quindi può stare a riposo per qualche minuto senza che nessuno la interroghi.

[^1]: *NAS*, Network Attached Storage - apparato dedicato che espone spazio disco in rete tramite protocolli standard di condivisione, invece di offrire dischi a un singolo computer.
