# Registro delle decisioni

> Registro ADR-lite, append-only. Ogni voce fissa una decisione architetturale con il suo contesto, le alternative considerate e le conseguenze accettate. Una decisione non si cancella e non si riscrive: se cambia, si aggiunge una voce nuova che la supera e si annota la sostituzione nella voce vecchia. Le decisioni qui registrate sono ricostruite dal documento sorgente e dalle evidenze del progetto, non inventate; dove la fonte non permette di stabilire una data, il campo lo dichiara.

## ADR-001, il firewall sta a valle del modem dell'operatore

Data: fine febbraio 2026, consolidata con il ticket del 26/02 e la conferma del 28/02. Stato: accettata, non reversibile senza cambiare contratto o apparato.

Contesto. L'obiettivo iniziale era rendere il firewall l'apparato di frontiera, collegandolo direttamente all'ONT e riducendo il modem dell'operatore a punto di accesso wireless. Due evidenze indipendenti lo escludono: una prova condotta da un fornitore, che ha collegato il firewall direttamente all'ONT senza ottenere traffico, e la conferma esplicita dell'assistenza tecnica. La causa più probabile è che l'ONT sia vincolato all'indirizzo hardware del modem fornito in comodato, comportamento non standard ma adottato da alcuni operatori. Si aggiunge che l'interfaccia del modem non espone alcuna modalità bridge, né passthrough del protocollo di autenticazione, né passthrough di VLAN.

Alternative considerate. Collegare il firewall direttamente all'ONT, scartata perché non funziona. Attivare un modem di proprietà con la procedura dedicata dell'operatore, tenuta aperta come possibilità futura ma non perseguita perché comporta l'acquisto di un apparato e la riapertura del tema dei parametri di accesso.

Decisione. La catena è ONT, modem dell'operatore, firewall, switch, access point. Il modem termina la sessione con l'operatore e detiene l'indirizzo pubblico; il firewall è il router e il punto di sicurezza di tutte le reti interne.

Conseguenze accettate. Doppio NAT strutturale. La rete wireless del modem resta fuori dal perimetro del firewall finché non viene sostituita da access point a valle. I parametri di accesso alla rete dell'operatore, cioè protocollo e VLAN, diventano irrilevanti per la configurazione del firewall, perché restano interni al modem: è l'unica conseguenza positiva del vincolo.

## ADR-002, OPNsense come piattaforma firewall

Data: non databile con precisione dal sorgente, precedente all'installazione del 16/01/2026. Stato: accettata, attuata parzialmente.

Contesto. Serve una piattaforma firewall in grado di gestire 2,5 Gbps reali con traduzione di indirizzi con stato, VLAN e VPN, su hardware x86 riutilizzato.

Alternative considerate. Un mini-PC generico di importazione con firewall preinstallato, scartato per assenza di garanzie su firmware documentato, aggiornamenti di sicurezza e qualità della componentistica, che in un apparato di sicurezza sono il punto di rottura. pfSense, scartato per decisioni di licenza e una tabella di marcia meno aperta, pur restando tecnicamente valido. Una distribuzione Linux generica con filtro di pacchetti configurato a mano, scartata perché richiederebbe messa a punto profonda di tabelle, tracciamento connessioni, affinità degli interrupt e gestione manuale degli aggiornamenti, aumentando il rischio operativo. IPFire, confrontato voce per voce e scartato per prestazioni meno prevedibili in traduzione intensiva e per un'integrazione dei servizi meno ricca. NethSecurity, citata e non valutata.

Decisione. OPNsense 25.7, installazione bare-metal su macchina dedicata, con WAN e LAN su schede fisicamente separate e nessun servizio estraneo alla sicurezza in esecuzione su quella macchina.

Conseguenze accettate. Lo stack è FreeBSD, quindi la nomenclatura delle interfacce segue il driver e non la convenzione prevedibile di Linux, e la compatibilità delle schede va valutata sul supporto FreeBSD e non su quello Linux.

## ADR-003, tre interfacce fisiche per tre zone

Data: non databile con precisione, contestuale alla scelta dell'hardware. Stato: accettata, non ancora attuata.

Contesto. La macchina scelta ha una scheda gigabit integrata e due slot liberi, riempiti con due schede a 2,5 Gbps basate su chipset Realtek RTL8125B, per una spesa complessiva contenuta.

Decisione. Una scheda a 2,5 Gbps come WAN verso il modem, l'altra come LAN verso lo switch, la gigabit integrata come zona esposta. Le velocità non sono vincolate dal ruolo logico: la zona esposta sta sulla porta più lenta perché il servizio che ospiterà non ha bisogno di banda multigigabit.

Alternative considerate. Schede Intel della serie i225 o i226, riconosciute come più affidabili sotto lo stack FreeBSD, non acquistate per costo; le Realtek sono documentate come pienamente supportate dal driver nelle versioni recenti. Adattatori da USB a 2,5 Gbps, esclusi per latenza, instabilità sotto carico e comportamento imprevedibile.

Conseguenze accettate. Se in futuro emergesse instabilità sotto carico, la sostituzione delle due schede con equivalenti Intel è un intervento circoscritto che non tocca l'architettura.

## ADR-004, richiesta e adozione dell'indirizzo pubblico statico

Data: richiesta il 26/02/2026, sollecitata e confermata il 05/03/2026. Stato: accettata, attuata.

Contesto. Il progetto prevede di esporre almeno un servizio dalla zona esposta. Su linea residenziale l'indirizzo pubblico è tipicamente dinamico, e la sua variazione, pur non periodica, invalida sessioni attive, richiede aggiornamento del nome DNS con una finestra di incoerenza legata al tempo di vita della cache, e rompe qualunque autorizzazione basata su indirizzo presso terzi.

Decisione. Richiesta dell'indirizzo statico all'operatore, ottenuta senza costi aggiuntivi trattandosi di un profilo residenziale.

Conseguenze. Decade l'intera linea di implementazione della gestione endpoint basata su DNS dinamico, che resta nella documentazione come analisi dei limiti di un indirizzo dinamico e non come piano. Diventa praticabile la pubblicazione di servizi con inoltro di porte dalla zona esposta.

Nota di verifica. Al momento della lettura dell'interfaccia del modem in febbraio, la connessione attiva risultava essere quella mobile di riserva e non la fibra, quindi i parametri letti in quella occasione non sono quelli della linea in fibra. La rilettura a fibra attiva è fra le pendenze.

## ADR-005, switch gestito di livello 2 senza alimentazione via cavo

Data: non databile con precisione, successiva alla scelta del firewall. Stato: accettata, non ancora acquistato.

Contesto. Serve distribuzione a 2,5 Gbps con segmentazione, a valle di un firewall che è già l'unico punto di decisione di livello 3.

Alternative considerate. Uno switch non gestito, scartato perché non riconosce le etichette di VLAN e quindi rende impossibile la segmentazione. Un modello con routing di livello 3, scartato perché quella capacità non serve in una topologia dove nessun traffico fra VLAN deve evitare il firewall, e costa di più. Un modello di un vendor la cui gestione dipende da un controller esterno, scartato perché introduce una dipendenza infrastrutturale che una rete domestica non ha motivo di assumere, e senza il controller si comporta di fatto come un non gestito.

Decisione. Zyxel XMG1915-10E, otto porte a 2,5 Gbps più due porte ottiche a 10 Gbps per collegamenti futuri, gestione locale via interfaccia web senza software esterno, senza alimentazione via cavo.

Conseguenze accettate. L'access point al piano inferiore va alimentato con un iniettore separato, il cui modello è già individuato, perché lo switch non fornisce alimentazione sulle porte.

## ADR-006, il wireless passa dal firewall tramite access point a valle

Data: non databile con precisione, discende da ADR-001. Stato: accettata, non attuata.

Contesto. Con il firewall a valle del modem, la rete wireless generata dal modem è interna alla LAN del modem stesso e non attraversa il firewall.

Alternative considerate. Mettere il modem in bridge, preclusa dal firmware. Accettare il wireless scoperto, scartata perché è il segmento con la superficie d'attacco più ampia e i client meno controllabili.

Decisione. Tutto il wireless viene rifatto con access point collegati allo switch a valle del firewall, che agiscono come ponti di livello 2 e non fanno routing; la radio del modem viene spenta o ridotta a sola rete ospiti.

Conseguenze accettate. Serve portare un cavo al piano inferiore, che è la parte materialmente più difficile del progetto, e serve un iniettore per l'alimentazione.

## ADR-007, DNS interno come punto di controllo, non come servizio accessorio

Data: non databile con precisione. Stato: accettata, non attuata.

Contesto. Il traffico DNS precede qualunque connessione e ne rivela la destinazione. Lasciarlo a un resolver di terzi significa cedere visibilità e controllo su tutto ciò che la rete raggiunge.

Alternative considerate. Un solo motore di blocco pubblicitario che inoltra a un resolver pubblico, scartato perché è un filtro davanti a una dipendenza esterna, non un'infrastruttura DNS: mantiene l'esposizione delle interrogazioni e il punto singolo di guasto altrove. Un resolver ricorsivo nudo, scartato perché non offre policy.

Decisione. Motore di policy davanti a resolver ricorsivo completo con validazione crittografica delle risposte, su una macchina dedicata con indirizzo interno fisso. Il firewall consente traffico DNS in uscita soltanto da quell'indirizzo.

Conseguenze accettate. La regola di uscita sul firewall è parte integrante della decisione, non un'aggiunta: senza di essa qualunque client può aggirare la policy e la configurazione diventa decorativa. Non si distribuisce ai client alcun resolver esterno come secondario, perché molti stack ricadono sul secondario alla prima risposta negativa.

## ADR-008, la documentazione si genera, non si scrive due volte

Data: 24/08/2026. Stato: superata da ADR-010 il 25/08/2026. Resta valida la parte sull'ingestione iniziale, cioè che il contenuto è entrato nel repository per conversione deterministica e non per riscrittura; non vale più la parte sulla rigenerazione continua.

Contesto. La base documentale è un unico documento Word molto grande, che l'autore continua a modificare. Riscrivere a mano il suo contenuto nel repository creerebbe due verità destinate a divergere.

Alternative considerate. Riscrittura curata in una ventina di documenti tematici, scartata perché la completezza dipenderebbe dalla riscrittura invece che da un controllo meccanico, e perché ogni modifica al sorgente andrebbe riportata a mano. Solo albero generato senza layer curato, scartata perché un dump navigabile non dice quale sia lo stato del progetto né perché le scelte sono quelle.

Decisione. Conversione deterministica e ripetibile del sorgente in un albero versionato, con verifica automatica di completezza, più un layer curato scritto a mano che vive accanto all'albero e non dentro di esso. I file generati non si modificano mai a mano: si corregge il sorgente, oppure si aggiunge un banner nel sidecar delle annotazioni.

Conseguenze accettate. Chi clona il repository non può rigenerare l'albero, perché il sorgente non è versionato. La documentazione resta leggibile ma la sua rigenerazione dipende dal materiale locale dell'autore.

## ADR-009, anonimizzazione come regola di generazione, applicata anche ai titoli

Data: 24/08/2026. Stato: accettata, attuata.

Contesto. Il repository è destinato a un remoto pubblico e il materiale contiene l'indirizzo dell'abitazione, l'indirizzo pubblico statico della linea, identificativi di apparato, nomi macchina, numeri di serie, nomi di persona e riferimenti contrattuali. Presi insieme descrivono dove si trova una casa, come raggiungerla e che cosa c'è dentro.

Alternative considerate. Revisione manuale del testo generato, scartata perché verrebbe annullata alla rigenerazione successiva. Pubblicare solo il layer curato tenendo l'albero generato in locale, scartata perché il dettaglio fine non sarebbe più recuperabile da un clone.

Decisione. Le sostituzioni vivono in un sidecar privato applicato dal convertitore, i valori reali in una mappa privata, e un guard-rail eseguibile controlla tutti i file tracciati prima di ogni commit. La redazione si applica anche ai titoli, perché dal titolo discendono lo slug del file e il nome della cartella: senza questa estensione due nomi propri sarebbero finiti nei percorsi di file tracciati, dove nessuna redazione del corpo li avrebbe raggiunti. Il convertitore è stato modificato di conseguenza rispetto alla versione del pacchetto di origine.

Conseguenze accettate. Restano reali per decisione motivata i nomi di operatore e vendor, i modelli di apparato, il piano di indirizzamento privato, gli indirizzi di gestione di fabbrica, gli indirizzi pubblici di transito di un traceroute, i contatti istituzionali di un registro regionale e i prezzi di listino pubblici. Il razionale di ciascuna eccezione è scritto nella regola, perché un'eccezione non motivata diventa una crepa.

Aggiornamento del 25/08/2026. Con ADR-010 l'albero non si rigenera più, quindi il sidecar di redazione non viene più applicato a ogni corsa: il contenuto nuovo si scrive già anonimizzato. Il presidio resta il guard-rail eseguibile, che è sempre stato la parte che conta, perché il sidecar sostituiva i valori noti mentre il guard-rail verifica il risultato. Il sidecar si conserva come registro di ciò che è stato sostituito nella prima stesura, e va comunque tenuto allineato alla mappa insieme al file dei pattern.

## ADR-010, la fonte diventa il repository, non più il documento Word

Data: 25/08/2026. Stato: accettata, attuata. Supera ADR-008.

Contesto. Con la conversione completata e verificata, tenere il documento Word come fonte viva ha smesso di avere senso e ha cominciato ad avere costi. È un binario da ventun megabyte, non diffabile, modificabile solo dentro un elaboratore di testi fuori dalla portata dell'agente, che per essere letto richiede la disciplina della disclosure progressiva e che per essere aggiornato impone un ciclo di rigenerazione dell'intero albero. Il modo in cui il lavoro procede davvero, invece, è aprire una sessione nuova sul repository e continuare da dove si era rimasti.

Il punto non è l'eleganza del formato ma dove vive la continuità. Se la fonte è il Word, una sessione nuova deve prima ricostruirsi il contesto da un binario; se la fonte è il repository, la continuità è già scritta nei file che la sessione legge comunque all'avvio, cioè l'indice di memoria, le schede di contesto e l'albero.

Alternative considerate. Tenere entrambe le fonti vive, scartata subito perché produrrebbe due verità destinate a divergere, che è esattamente il problema che ADR-008 voleva evitare. Continuare con il Word come fonte e usare il repository come sola vetrina, scartata perché è lo stato che si sta abbandonando. Reimportare occasionalmente da un Word aggiornato, scartata perché incompatibile con la manutenzione a mano: una reimportazione sovrascriverebbe il lavoro fatto nel frattempo.

Decisione. L'albero `docs/` passa a manutenzione manuale. Il documento Word resta in `_notes/sorgenti/` come archivio della prima stesura e prova di provenienza, non come fonte. Il convertitore resta nel repository perché è lo strumento che ha prodotto l'albero e la sua storia va conservata, ma non va più eseguito su `docs/`.

Attuazione. Il lucchetto non è una raccomandazione scritta ma un controllo nel codice: il convertitore scrive nella cartella di destinazione un timbro `.generato-da-docx`, e si rifiuta di scrivere in una cartella che contiene già documenti senza quel timbro. Congelare l'albero è consistito nel rimuovere il timbro. Chi dovesse insistere ha l'opzione esplicita `--forza`, che il messaggio di errore nomina insieme alla conseguenza. La ragione per cui serve un controllo e non una nota è che la procedura di rigenerazione era scritta in quattro file diversi, e una sessione futura che ne legge uno la eseguirebbe in buona fede.

Conseguenze. I marcatori che escludevano l'albero dalla normalizzazione Markdown sono stati rimossi e l'albero è stato normalizzato: non è più testo verbatim di una fonte esterna, è documentazione del progetto come tutto il resto. Il sidecar delle annotazioni non viene più applicato e i suoi banner sono ormai testo dentro i file. La coerenza dell'albero, che prima era garantita per costruzione dalla struttura dei titoli del sorgente, ora va verificata, e per questo esiste `tools/check-docs-tree.py`. I prefissi numerici di cartelle e file restano come nomi stabili e non si rinumerano più: per inserire qualcosa si usa il primo numero libero.

## ADR-011, il NAS non resta accesso sempre: finestra di accensione notturna

Data: 02/09/2026. Stato: accettata, non ancora attuata perché la macchina non è assemblata.

Contesto. L'analisi delle sei bollette mensili del 2026 ha prodotto un numero che ha cambiato la valutazione del progetto. Il costo marginale di un kilowattora su questa fornitura è di 0,256 euro, comprensivo di accisa e imposta, e va distinto dal prezzo medio apparente di 0,558 euro che si ottiene dividendo la spesa totale per i consumi: quel secondo numero è gonfiato dai costi fissi mensili divisi su un consumo domestico basso, scenderebbe da solo se il consumo aumentasse, e non serve a decidere niente. Con il costo marginale, un archivio di rete stimato a sessanta watt alla presa e acceso in continuo costa circa centotrentacinque euro all'anno.

Il dato che ha determinato la decisione non è però il valore assoluto ma il rapporto. L'abitazione consuma circa ottantasette kilowattora al mese, una frazione della media domestica nazionale, e la macchina ne consumerebbe quarantaquattro: un incremento di circa la metà del consumo elettrico di casa, che nei mesi estivi rilevati a sessanta e sessantadue kilowattora renderebbe l'archivio di rete il singolo apparato che consuma più di ogni altro. La ragione non è che sessanta watt siano molti, ma che il funzionamento è continuo mentre tutto il resto della casa consuma poco: è il tempo di accensione a determinare il costo, non la potenza.

Alternative considerate. Il funzionamento continuo, che è il default implicito di ogni progetto di archivio di rete e che si sarebbe adottato senza porsi la domanda. La sospensione dei dischi durante il funzionamento, scartata come misura principale perché produce cicli di avvio molto frequenti sui dischi meccanici e perché le verifiche periodiche li risvegliano comunque, quindi il risparmio è minore di quanto sembra e l'usura maggiore. La riduzione della memoria o la rinuncia a un disco a stato solido, scartate perché valgono pochi watt e costano funzioni che servono. L'acquisto di un alimentatore nuovo ed efficiente, che rientrerebbe in tre o quattro anni e resta marginale rispetto alla scelta fra quelli già disponibili.

Decisione. La macchina resta spenta nelle ore notturne, con due orari distinti fra i giorni lavorativi e il fine settimana, per un totale di cinquanta ore spente su centosessantotto, cioè il settanta per cento di tempo acceso. Il risparmio è di quaranta euro all'anno, cioè il trenta per cento del costo di esercizio, e riduce l'incremento sul consumo di casa dal cinquanta al trentacinque per cento.

Va detto che una valutazione preliminare, fatta ipotizzando quattro ore di accensione al giorno, indicava un fattore sei di risparmio. Con una finestra di sedici o diciassette ore quel fattore non si realizza e il risparmio reale è di un terzo: la differenza fra le due cifre è significativa e la registrazione della decisione la conserva, perché una decisione presa su un numero sbagliato va rivalutata quando il numero si corregge, e in questo caso la decisione regge comunque.

Attuazione. Servono due meccanismi distinti e non uno, ed è il punto in cui un piano approssimativo si rompe. Lo spegnimento si programma dal sistema operativo con un'attività pianificata, perché è l'unico meccanismo che distingue i giorni della settimana, e deve essere un arresto ordinato: il file system è transazionale e non si corromperebbe nemmeno con un taglio di corrente, ma le scritture in volo si perderebbero, e una macchina il cui scopo è custodire dati non si spegne strappando la spina. La riaccensione non può venire dal sistema, che a macchina spenta non gira, e viene dall'allarme dell'orologio in tempo reale del firmware, che il manuale documenta come capace di programmare giorni e ore. È preferibile al risveglio da rete, che la scheda pure supporta, perché non dipende da nessun apparato esterno.

L'allarme del firmware ammette un solo orario giornaliero mentre la decisione ne prevede due: si imposta sull'orario più precoce e si accetta che nel fine settimana la macchina si accenda un'ora e mezza prima del necessario, per un costo di meno di trenta centesimi al mese. Complicare la configurazione per recuperarli sarebbe un cattivo scambio.

Conseguenze. Le attività pianificate non girano a macchina spenta e non lo segnalano: ogni orario va ricollocato dentro la finestra di accensione, e deve avere il tempo di completarsi prima dello spegnimento. Il caso concreto è la verifica periodica dell'integrità del pool, che il sistema crea da sé a mezzanotte del sabato e che con questa finestra partirebbe due ore e mezza prima di uno spegnimento, venendo interrotta: va spostata alla mattina del sabato, subito dopo la riaccensione. I salvataggi automatici notturni da altri apparati non troverebbero la destinazione, ed è il conflitto più sostanziale perché essere destinazione dei backup della rete è uno degli usi principali di un archivio di rete: se quell'uso si concretizza, gli orari vanno portati dentro la finestra oppure la finestra va ripensata. L'impostazione di riaccensione dopo un'interruzione di corrente resta incondizionata, perché l'alternativa che ripristina lo stato precedente introduce un modo di fallire peggiore, cioè una macchina che resta spenta quando la si vuole accesa.

Un timore che non si realizza riguarda l'usura dei dischi: uno spegnimento al giorno significa circa trecentosessantacinque cicli all'anno contro tolleranze dichiarate di decine di migliaia, e non è una sollecitazione significativa.

## ADR-012, l'alimentatore si sceglie fra quelli disponibili, e più piccolo è meglio

Data: 03/09/2026. Stato: accettata, da attuare durante l'assemblaggio.

Contesto. Il progetto dispone degli alimentatori di tutte le macchine dismesse, e la scelta fra loro non è indifferente. Un alimentatore rende al meglio attorno al cinquanta per cento del carico nominale e perde rapidamente scendendo; la macchina assorbirà fra trenta e quarantacinque watt in continua, che su un alimentatore da cinquecento watt è il nove per cento del carico, cioè la zona peggiore della curva. La differenza di rendimento fra un alimentatore mal dimensionato e uno adatto, in quella zona, vale cinque a dieci watt continui, cioè da undici a ventidue euro all'anno su una macchina il cui costo di esercizio complessivo è di circa novantacinque.

Il fatto controintuitivo, e la ragione per cui questa decisione merita di essere registrata, è che un alimentatore più piccolo è migliore e non peggiore, purché copra il picco. La certificazione di efficienza più diffusa misura il rendimento al venti, al cinquanta e al cento per cento del carico e non dice nulla su cosa accade al dieci per cento, che è invece la condizione in cui questa macchina lavorerà per tutta la sua vita: soltanto il livello più alto della scala specifica anche quel punto. Un alimentatore da settecentocinquanta watt certificato, a quaranta watt di carico, può rendere peggio di uno da trecento non certificato.

Il picco da coprire non è il consumo a riposo. All'accensione i dischi meccanici assorbono da venti a venticinque watt ciascuno per qualche secondo mentre i motori raggiungono la velocità di regime, quindi il picco realistico dell'intera macchina sta fra centocinquanta e duecento watt.

Alternative considerate. L'acquisto di un alimentatore nuovo ed efficiente, che costerebbe fra cinquanta e settanta euro e rientrerebbe in tre o quattro anni: scartato come primo passo perché marginale, e riproponibile se la scelta fra quelli disponibili non desse un candidato adatto. Il confronto misurato alla presa fra i migliori candidati, che sarebbe il metodo più rigoroso perché la differenza fra due letture nella stessa condizione è direttamente la differenza di rendimento sul carico reale: scartato per proporzionalità, perché richiede di montare e smontare la macchina più volte per un guadagno che la lettura delle etichette approssima abbastanza bene.

Decisione. Si scelgono per lettura delle etichette, con criteri in ordine di importanza: la potenza nominale più bassa che copra duecento watt di picco, quindi un obiettivo fra trecento e quattrocento watt; poi la certificazione più alta a pari potenza; poi la data di fabbricazione più recente, perché i condensatori elettrolitici degradano con il tempo e con il calore e un alimentatore di dodici anni può avere capacità residua molto inferiore alla nominale; e infine la disponibilità dei connettori necessari, cioè ventiquattro pin per la scheda, otto pin per il processore e almeno quattro connettori per dischi.

Va verificata anche la corrente disponibile sulla linea a dodici volt, che è quella da cui si alimenta praticamente tutto in una macchina moderna e che su alimentatori vecchi o economici è molto inferiore a quanto il totale dichiarato suggerisce.

Conseguenze. La lettura delle etichette non si può fare con il censimento software, e non è una lacuna degli strumenti: un alimentatore ATX non ha nessuna interfaccia dati verso la scheda madre, quindi non esiste una classe da interrogare e l'etichetta è la sola fonte. Ne discende che questa attività appartiene alla fase di smontaggio, quando i case sono comunque aperti, e non alla preparazione: l'etichetta è spesso girata verso l'interno del case e può richiedere di sfilare l'alimentatore per leggerla.

## ADR-013, il pool dati nasce da quattro dischi recuperati da un QNAP dismesso, non da un acquisto

Data: 22/09/2026. Stato: superata il 07/10/2026 da ADR-014, perché i dischi non si libereranno. Il ragionamento sul lotto unico e sulla qualificazione resta valido come metodo per qualunque disco usato.

Contesto. La creazione del pool dei dati era l'unico passo del sottoscopo NAS che attendeva una decisione, dichiarata identica in tre documenti come acquisto di dischi meccanici a registrazione convenzionale. Diventano invece disponibili quattro dischi da 2 TB gratuiti provenienti da un QNAP TS-410U aziendale in dismissione, dove lavorano in RAID 5 da quattordici anni: tre Samsung HD204UI e un Toshiba DT01ACA200. Coprono esattamente le quattro porte SATA libere della base, il che invita a montarli tutti, ma lo SMART letto dall'interfaccia del QNAP dice una cosa che cambia la conclusione.

I riscontri che contano. Tutti e quattro hanno zero settori riallocati e temperature fra trenta e trentacinque gradi: meccanicamente non mostrano degrado. L'età è però fuori dalle curve pubblicate, perché i Samsung stanno a 125.339, 125.318 e 125.225 ore e il Toshiba a 104.496, mentre l'analisi Backblaze più ampia colloca il picco di guasto a dieci anni e tre mesi: qualunque stima di vita residua è un'estrapolazione oltre i dati e va dichiarata tale. Soprattutto, i tre Samsung hanno seriali consecutivi e ore identiche a meno di un millesimo, cioè sono dello stesso lotto con la stessa storia di carico: fra loro il guasto non è indipendente, e uno specchio composto da due di loro sarebbe ridondanza sulla carta e non nei fatti, perché il calcolo di ridondanza assume guasti scorrelati. Infine il firmware dei Samsung è 1AQ10001, la versione col difetto di corruzione su IDENTIFY/SMART durante NCQ, il cui correttivo non cambia il numero di versione: non si può stabilire per lettura se sono già corretti.

Alternative considerate. Due specchi con tutti e quattro i dischi, cioè 4 TB utili: scartata come forma predefinita perché il secondo specchio sarebbe di Samsung gemelli, e resta ammessa solo come esito condizionato al dimensionamento, con la dichiarazione esplicita che quella zona del pool ha ridondanza più debole. raidz2 su quattro dischi, che tollera due guasti qualsiasi: scartata perché la ricostruzione legge tutti i superstiti e dura molto più a lungo, stressando proprio i gemelli anziani nel momento peggiore. raidz1, 6 TB utili: scartata perché un solo guasto tollerato e nessuna parità residua a fronte di un errore di lettura durante la ricostruzione sono la combinazione peggiore su dischi di questa età. L'acquisto di dischi nuovi destinati all'uso continuo: rimandato, perché questi coprono il fabbisogno a costo zero, con una regola d'ingaggio severa.

Decisione. Nel pool dati entra un solo specchio, che accoppia il Toshiba con un Samsung: è l'unica coppia del gruppo i cui elementi non condividono lotto, marca, generazione, velocità e storia di carico, quindi l'unica con ridondanza reale. Un secondo Samsung resta nella macchina come riserva a caldo sulla porta SATA libera. Il terzo Samsung esce dal NAS e va alla scorta con la sola rete Intel, che l'inventario descrive come l'unica a cui manca soltanto un disco, sciogliendo il vincolo dichiarato dei zero dischi in magazzino e sbloccando il secondo nodo di laboratorio. Prima di montarli i dischi si qualificano con badblocks -wsv seguito da smartctl -t long, con scarto su qualunque valore diverso da zero negli attributi 5, 197, 198 e 199: la cancellazione con shred o con la pulizia integrale non si fa, perché cancella senza verificare e lo scopo qui è scoprire un disco marcio mentre è ancora vuoto. Il dimensionamento resta l'unico nodo aperto e si chiude misurando l'occupato del QNAP prima di creare il pool: sotto i 2 TB la forma descritta basta, sopra rientra il terzo Samsung come secondo specchio.

Conseguenze. La decisione sull'acquisto dei dischi, prima pendenza del sottoscopo NAS, si chiude. L'inventario delle scorte perde il suo vincolo dominante dichiarato, cioè i zero dischi in magazzino. Il conteggio dei connettori SATA dell'alimentatore sale da quattro a cinque, e il picco allo spunto va ricalcolato con tre dischi in rotazione, restando dentro l'obiettivo dei trecento-quattrocento watt. Il consumo stimato passa da una spesa annua di circa novantacinque euro a circa centodieci sulla finestra di ADR-011, recuperabili in parte mettendo in sospensione la sola riserva a caldo. Restano due dati fisici da rilevare a case aperto, il numero di alloggiamenti da 3,5 pollici della gabbia e l'etichetta dell'alimentatore, e nessun dato la cui unica copia sia su questi dischi può abitarli, perché restano supporti da tavolo a fine vita.

## ADR-014, i dischi del QNAP non arriveranno: il pool dati torna senza dischi

Data: 07/10/2026. Stato: accettata. Decisione dell'utente. La strada fra le tre elencate nelle conseguenze è stata scelta lo stesso giorno in ADR-015: partenza senza dischi meccanici.

Contesto. ADR-013 aveva costruito il pool dati sui quattro dischi da 2 TB del QNAP aziendale in dismissione, presupponendo che si liberassero. L'utente ha comunicato il 07/10/2026 che nessuno di quei dischi è libero e che non lo sarà.

Decisione. ADR-013 decade per intero nella sua parte attuativa: niente specchio Toshiba più Samsung, niente riserva a caldo, niente Samsung alla scorta, niente Passo 4.4 di qualificazione su quei dischi. Il magazzino torna a zero dischi meccanici, che è il vincolo dominante dichiarato dall'inventario prima del 22/09.

Conseguenze. La provenienza dei dischi del pool dati torna una decisione aperta, con tre strade che non si escludono nel tempo: acquisto di due dischi CMR da uso continuo in specchio; avvio del NAS senza pool dati, con il solo pool applicazioni sui due NVMe da 1 TB in specchio a ospitare anche i dati finché bastano; oppure un singolo NVMe per le applicazioni e l'altro per i dati, senza ridondanza, che si sconsiglia. La scorta con la sola rete Intel torna senza disco. Le stime che ADR-013 aveva alzato, cioè cinque connettori SATA invece di quattro, il picco con tre dischi in rotazione e la spesa annua di circa centodieci euro, tornano ai valori con due dischi o con nessuno, secondo la strada scelta. I documenti pubblici della cartella NAS e la guida privata vanno riallineati: finché non lo sono, descrivono un pool che non verrà costruito.

## ADR-015, il NAS parte senza dischi meccanici: i due NVMe in specchio sono il pool dati e applicazioni

Data: 07/10/2026. Stato: accettata. Decisione dell'utente.

Contesto. Con ADR-014 il pool dati è rimasto senza dischi, e nel magazzino non ce ne sono altri: le quattro macchine del consolidamento portano al NAS due SSD SATA e due NVMe da 1 TB, nessun disco meccanico. ADR-014 lasciava tre strade: acquistare due dischi CMR in specchio, partire con i soli NVMe, oppure dividere i due NVMe fra applicazioni e dati senza ridondanza.

Alternative considerate. L'acquisto di due dischi CMR da uso continuo in specchio, che resta la forma bersaglio descritta nell'analisi: rimandato, non scartato, perché l'utente non ha dischi da mettere e la macchina può partire senza. La divisione dei due NVMe in due pool da un disco ciascuno: scartata, perché toglie la ridondanza a entrambi per separare due carichi che sugli stessi due dischi i dataset separano già.

Decisione. Il NAS parte con l'insieme di avvio in specchio sui due SSD SATA e con un solo pool in specchio sui due NVMe, il P2 nell'alloggiamento M.2 della scheda e il P3 sull'adattatore da PCIe a M.2, che ospita dati e applicazioni separati per dataset. Se l'adattatore non è arrivato al momento della creazione del pool, il pool nasce sul solo P2 senza ridondanza dei dati, lo si dichiara a chi ci scrive sopra, e il P3 si aggancia come seconda metà dello specchio a pool vivo quando l'adattatore arriva. Due dischi CMR in specchio restano un'aggiunta futura come secondo pool, senza reinstallare: i dataset di massa vi si spostano con invio e ricezione ZFS e gli NVMe restano alle applicazioni.

Conseguenze. La capacità utile è di circa 1 TB, da pianificare attorno agli 800 GB per la regola dell'ottanta per cento. I connettori SATA di alimentazione necessari scendono a due, quelli dei due SSD, e il picco all'accensione non ha più motori da avviare: stimato sotto i 120 W, non misurato. Il consumo di riferimento torna alla riga senza dischi meccanici della scheda 05, stima centrale 48 W alla presa, e con la finestra di ADR-011 la spesa annua stimata scende da circa 95 euro (60 W) a circa 76, con lo stesso costo marginale di 0,256 euro per kilowattora; il perimetro del calcolo è dichiarato nella scheda. Il Passo 4.4 di qualificazione dei dischi del QNAP decade, la sezione del pool e i Passi 7.x della guida privata sono riscritti, la scheda 07 diventa storica. La scorta con la sola rete Intel torna senza disco. L'uso degli NVMe per i dati resta lo spreco di velocità che l'analisi descrive quando lo si sceglie: qui è accettato perché è l'unica forma possibile con i pezzi disponibili, ed è reversibile.

## ADR-016, l'alimentatore del NAS resta quello della base, con quattro controlli di accettazione

Data: 07/10/2026. Stato: accettata. Decisione dell'utente.

Contesto. ADR-012 chiedeva di scegliere fra gli alimentatori disponibili, preferendo il più piccolo. Le etichette lette il 07/10/2026 danno quattro unità fra 500 e 600 W, nessuna con certificazione stampata: tutte circa dieci volte sopra il fabbisogno del NAS senza dischi meccanici, quindi la potenza non le distingue in modo utile. Le distinguono qualità ed età: la base monta un'unità modulare di marca di fascia alta, prodotta con buona probabilità nel 2006 secondo il seriale; la prima macchina di scorta ne monta una economica di circa il 2022.

Alternative considerate. Spostare nella base l'unità più recente e mettere l'altra nella macchina di scorta: scartata dall'utente per il lavoro che richiede, a fronte di un rischio che si può verificare invece di supporre. L'unità da 500 W, la più piccola: scartata perché di marca generica economica, cioè il componente che più probabilmente cede in una macchina che custodisce dati.

Decisione. Resta l'alimentatore già montato nella base, a quattro condizioni di accettazione: ispezione visiva senza condensatori gonfi, macchie o odore, eseguita dall'utente il 07/10/2026 con esito positivo; ventola senza rumori al primo avvio; tensione a +12 V fra 11,4 e 12,6 V letta dal firmware; test della memoria di una notte senza errori né riavvii. Se una condizione fallisce si passa all'unità più recente, che resta montata nella macchina di scorta e si scambia in mezz'ora.

Conseguenze. Nessuno spostamento di alimentatori. L'età resta un rischio dichiarato e non nascosto: l'invecchiamento dei condensatori dipende dalle ore di funzionamento e dal calore, che per questa unità non sono noti. Un guasto, su questa architettura, spegne la macchina senza perdita di dati, grazie al file system transazionale e ai dischi in specchio.


## ADR-017, switch con PoE integrato e due access point

Data: 07/10/2026. Stato: accettata. Decisione dell'utente.

Contesto. La scelta dello switch dipendeva dal numero di access point: uno solo rendeva sensato lo XMG1915-10E con un iniettore PoE a 2,5 GbE, due o tre rendevano più ordinato lo XMG1915-10EP. Il rilievo fisico della casa non è ancora stato fatto, ma l'utente ha fissato il fabbisogno: uno switch PoE e due access point.

Decisione. Lo switch è lo Zyxel XMG1915-10EP, otto porte 2,5 GbE PoE++ con budget di 130 W e due SFP+. Gli access point sono due, entrambi alimentati dallo switch e collegati in trunk; il terzo AP non è previsto e la porta 4 che gli era riservata passa a un client cablato. Il modello degli AP resta aperto fra NWA130BE, che porta 802.1X/RADIUS e SNMP, e NWA50BE Pro, più economico. Con due NWA130BE l'assorbimento di targa è 48 W, ampiamente dentro il budget.

Conseguenze. L'iniettore PoE esce dalla lista degli acquisti. La posizione dei due AP, e quindi la lunghezza e il percorso dei cavi, resta legata al rilievo della casa. Spenta la radio del Seven dopo il collaudo dei due AP, tutto il wireless di casa passa da OPNsense: è la differenza dichiarata rispetto al modello di Autore-LinkedIn-B, che tiene la casa sul modem.

## ADR-018, AP cablati ai piani centrali, PS5 sul Seven, niente FRITZ!Box

Data: 07/10/2026. Stato: accettata. Decisioni dell'utente.

Contesto. Dopo ADR-017 restavano da fissare la collocazione fisica degli AP, il posto dei dispositivi che non hanno bisogno del perimetro e l'eventuale acquisto di un router di terze parti. La casa si sviluppa su quattro piani, con Seven e switch al piano più alto.

Decisione. I due AP stanno al terzo e al secondo piano, collegati ciascuno con un cavo già posato a una porta dello switch, da cui prendono l'alimentazione PoE; il requisito di mesh si realizza come roaming fra due AP cablati, non come collegamento radio fra AP. La PS5 si collega a una porta LAN da 1 GbE del Seven, fuori dal perimetro, con un NAT solo. Non si acquista un FRITZ!Box. Il NAS resta nella VLAN 30 a 1 GbE, con una scheda da 2,5 GbE come aggiunta facoltativa futura. La Wi-Fi del Seven può restare accesa come rete esterna dichiarata; la decisione definitiva è rimandata.

Alternative considerate. Mesh radio con un solo AP cablato: inutile, i cavi ci sono. PS5 sullo switch nella VLAN IoT con UPnP o NAT statico su OPNsense: scartata dall'utente, perché la console non naviga, non le serve il perimetro e occuperebbe una porta dello switch. FRITZ!Box dietro o al posto del Seven: terza traduzione nel primo caso, configurazione libera della linea non validata nel secondo.

Conseguenze. La porta 4 dello switch va a un client cablato. La copertura del piano terra dall'AP del secondo piano va misurata. Sul Seven, per la PS5, si preferiscono inoltri statici verso l'indirizzo della console a UPnP, che aprirebbe porte a ogni dispositivo del Seven. Il ragionamento didattico è in `docs/03-spunti-di-sviluppo/23-studio-home-lab/07-doppio-nat-dietro-modem-in-comodato.md`.

## ADR-019, `docs/` unica fonte: eliminati i testi dell'autore già ingeriti

Data: 07/10/2026. Stato: accettata. Decisione dell'utente, eseguita dopo verifica.

Contesto. ADR-010 aveva tolto al documento Word il ruolo di fonte di rigenerazione ma lo aveva tenuto come archivio in `_notes/sorgenti/`, insieme agli appunti e ai collegamenti da cui erano nati alcuni documenti. L'utente ha chiesto una sola fonte di verità: ingerire tutto nel punto giusto e poi cancellare i testi scritti da lui, conservando immagini e materiale di contesto.

Decisione. Verificato il contenuto del Word contro `docs/` per paragrafi, note a piè di pagina, immagini e collegamenti, e corretta la lacuna trovata, cioè le 53 note mai convertite, sono stati spostati nel Cestino di Windows il documento Word, `privacy pack.txt`, `Diagram/Notes.txt`, i due file `.url` e `quickprint.docx`. Restano in `_notes/sorgenti/` le 31 fotografie originali, lo schema PNG del monitoraggio e il whitepaper OPNsense. L'output DxDiag, tenuto in un primo momento perché non era testo dell'utente, è stato spostato nel Cestino lo stesso giorno su sua indicazione; la parte utile era già nel censimento.

Conseguenze. `docs/` è l'unica fonte di quel contenuto, e un errore lì non si corregge più risalendo al Word. La ricostruzione della mappa di anonimizzazione resta possibile da `tools/redactions.json`, che non dipendeva dal Word. Il Cestino è l'ultima via di recupero finché non viene svuotato. Il metodo e i numeri della verifica sono in `docs/fonti-e-materiali.md`.

## ADR-020, i documenti dell'autore si riscrivono al loro posto, con verifica di copertura

Data: 07/10/2026. Stato: accettata. Decisione dell'utente.

Contesto. La trasformazione della documentazione dell'autore in documentazione tecnica di progetto poteva produrre un documento nuovo accanto all'originale, come è stato fatto per il Seven, oppure riscrivere l'originale. Con ADR-019 l'utente ha chiesto una sola fonte di verità.

Decisione. Ogni documento dell'autore si riscrive al suo posto come documento tecnico. Dopo ogni riscrittura si verifica con il confronto paragrafo per paragrafo che ogni contenuto dell'autore sia ancora presente, oppure tolto con una ragione scritta nel work-log. Il documento sul Seven scritto come file separato si riassorbe nel censimento delle voci di menu. L'utente chiede che tutto sia tracciato: ogni riscrittura passa da work-log, pendenze, fonti e snapshot nello stesso giro.

Conseguenze. Nessun documento tecnico duplica un originale. La copertura diventa una misura dichiarata per ogni area, con il suo perimetro.

## ADR-021, scheda dispositivo a campi fissi e raccolta in sola lettura

Data: 07/10/2026. Stato: accettata. Decisione dell'utente.

Decisione. Ogni dispositivo della rete ha una scheda con gli stessi campi: identità (codice segnaposto, categoria, proprietario per ruolo), sistema (sistema operativo, versione, supporto), rete cablata (chip, velocità massima), Wi-Fi (standard, bande, WPA3, 802.1X), collocazione (cablato o Wi-Fi, piano, porta o SSID, VLAN) ed esposizione (servizi offerti, inoltri, sensibilità dei dati). I dati si raccolgono con uno script PowerShell di sola lettura su Windows, con `ip`, `ethtool` e `lshw` su Linux, e a mano dalle schermate di impostazione per telefoni, televisori e console. I dati grezzi stanno in `_notes/`; nel repository va la sola scheda anonimizzata. Si parte dal censimento esistente in `docs/05-analisi-del-caso/`.

## ADR-022, il template è l'autorità: adozione dei pacchetti con il gate, aggiornamento con l'allineamento

Data: 07/10/2026. Stato: accettata. Decisione dell'utente.

Contesto. Sedici riferimenti di regole e skill puntavano a strumenti `tools/...` che il progetto non aveva istanziato, quindi i presidi di prosa, tipografia, tabelle, ripresa e schede non giravano.

Decisione. Il template è l'autorità e il progetto ne eredita le funzionalità; non si propongono modifiche al template per adattarlo al progetto. Si adottano tutti gli strumenti del template utili a questo progetto, compresi quelli di prosa e tipografia, istanziandoli dai pacchetti secondo i loro README; da lì in poi li aggiorna `allinea-dal-template.py`. Restano fuori gli strumenti che servono solo al template o a funzioni che il progetto non usa.

Conseguenze. Il 07/10/2026 l'allineamento ha aggiornato nove file e ne ha aggiunto uno, senza conflitti. Il guard-rail di anonimizzazione del progetto, in `scripts/`, non è sostituibile alla cieca: legge chiavi del file dei pattern (seriali, ubicazione, organizzazioni private, importi ammessi, telefoni reali) che la versione del template non conosce, mentre gli manca `--autotest`, che `chiudi` ora richiede. Il 08/10/2026, su scelta dell'utente, la riconciliazione è fatta: `tools/Test-Anonymization.py` è la versione del template con sei estensioni del progetto marcate nel codice, registrata come risolta in `.claude/allineamento-risolti.json`, e la copia in `scripts/` è tolta.

## ADR-023, lo switch è lo XMG1915-10EP anche al confronto dei prezzi

Data: 08/10/2026. Stato: accettata. Decisione dell'utente.

Contesto. ADR-017 aveva scelto lo XMG1915-10EP. L'utente ha chiesto di riaprire la scelta con un solo criterio: spendere il meno possibile lasciando invariato il progetto, cioè otto porte 2,5 GbE gestite con VLAN, alimentazione PoE per due AP e uplink verso il firewall.

Alternative considerate, con i prezzi raccolti l'8/10/2026 (S59-S63), indicativi e non preventivi. XMG1915-10E senza PoE con due iniettori 2,5 GbE: circa 251-307 euro più 2 x 28-31 euro, quindi circa 310-370 euro, con due alimentatori in più. TP-Link SG2210XMP-M2: circa 303-353 euro. Switch di marca generica 8 x 2,5 GbE PoE+ gestito, tipo Sodola: circa 170-200 euro, cioè l'unico risparmio reale, scartato perché firmware e aggiornamenti hanno provenienza poco documentata su un apparato che trasporta tutte le VLAN di un laboratorio di sicurezza.

Decisione. Zyxel XMG1915-10EP, da comprare al prezzo più basso disponibile, circa 291 euro alla ricerca dell'8/10/2026.

Conseguenze. Il risparmio sugli acquisti di rete, se serve, si cerca nel modello degli access point, che è ancora aperto.

## ADR-024, due NWA130BE: la soluzione più completa al costo minore

Data: 08/10/2026. Stato: accettata. Criterio dell'utente, scelta conseguente.

Contesto. Il modello degli AP era aperto fra NWA50BE Pro, NWA90BE Pro, NWA130BE e una combinazione. L'utente ha dato il criterio: la soluzione più completa possibile al costo minore. Completa, per questo progetto, significa tre bande in contemporanea, autenticazione 802.1X/RADIUS e SNMP su entrambi gli AP, perché una rete aziendale di prova che esistesse su un solo piano non avrebbe roaming e non sarebbe completa.

Alternative considerate, con i prezzi raccolti il 22/09 e l'8/10/2026 (S24, S25, S64, S68-S70), indicativi. Due NWA50BE Pro, circa 205 euro: non hanno 802.1X né SNMP, e trasmettono su 2,4 GHz più una sola fra 5 e 6 GHz. Due NWA90BE Pro, circa 270-390 euro: 802.1X sì, SNMP no, due radio. Un NWA130BE e un NWA50BE Pro, circa 300 euro: completo su un piano solo. Ubiquiti U7 Pro, circa 220 euro IVA inclusa: richiede il controller UniFi, la stessa dipendenza per cui lo switch Ubiquiti era stato escluso. TP-Link EAP772: prezzo italiano non trovato e SNMP in modalità autonoma non verificato.

Decisione. Due Zyxel NWA130BE, da comprare al prezzo più basso disponibile: 188,62 euro il 22/09 e 213,99 euro l'8/10/2026 presso un rivenditore italiano, cioè circa 380-430 euro in tutto.

Conseguenze. Spesa di rete indicativa con lo switch (ADR-023): circa 670-720 euro, esclusi cavi e posa, già fatta. L'assorbimento di targa dei due AP è 48 W, dentro i 130 W dello switch. Lo stesso costruttore per switch e AP permette la gestione unificata Nebula, che resta facoltativa. Il prezzo del NWA130BE oscilla di decine di euro fra settimane: conviene controllarlo al momento dell'ordine.

## ADR-025, amministrazione solo da tre ingressi, verso indirizzi della VLAN 99

Data: 08/10/2026. Stato: accettata. Decisione dell'utente.

Decisione. Firewall, switch, access point e NAS si amministrano soltanto dalla workstation designata della VLAN 10 (alias ADMIN), dalla porta di recupero della VLAN 99 e dal tunnel WireGuard, la cui rete è `192.168.98.0/24`. Le interfacce di amministrazione ascoltano solo su indirizzi della VLAN 99; il NAS ha a questo scopo un secondo indirizzo nella VLAN 99. Si aggiungono utente amministratore personale, TOTP sull'interfaccia web del firewall, SSH solo con chiavi, HSTS, credenziali di fabbrica cambiate, registro dei blocchi. Il dettaglio, con l'ordine di attivazione per non chiudersi fuori e il collaudo, è in `docs/03-spunti-di-sviluppo/23-studio-home-lab/09-accesso-amministrativo.md`.

Conseguenze. Il punto debole dichiarato è l'identità della workstation, riconosciuta dall'indirizzo: è coperta dalla seconda barriera e, se servisse, da 802.1X sulla porta dello switch. Il laboratorio non ha uscita predefinita verso Internet e si apre con due regole preparate e disattivate, attivate a tempo con una pianificazione, come descritto in `08-regole-fra-le-zone.md`; anche questo è approvato dall'utente.

## ADR-026, il NAS resta su TrueNAS SCALE

Data: 08/10/2026. Stato: accettata. Decisione dell'utente.

Contesto. L'utente ha chiesto di valutare OpenMediaVault. La valutazione, in `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/08-valutazione-openmediavault.md`, ha mostrato che OpenMediaVault porta ZFS solo con un plugin legato al kernel e non prevede l'avvio in specchio dall'installatore.

Decisione. Resta TrueNAS SCALE, con l'avvio in specchio sui due SSD SATA e il pool ZFS in specchio sui due NVMe (ADR-015). L'analisi dell'hardware vecchio continua con le foto dell'interno di altri due PC, per riallocare le risorse se serve.

## ADR-027, eliminati i contenuti sugli strumenti di monitoraggio scartati

Data: 08/10/2026. Stato: accettata. Decisione dell'utente.

Contesto. Il piano unificato ha verificato che dello schema di monitoraggio della prima stesura MozDef è archiviato, OSSIM e Apache Metron sono ritirati, Sagan è fermo, Snort non è integrato in OPNsense ed ELK separato duplica l'indicizzatore di Wazuh. L'utente ha chiesto di cancellare dal progetto ciò che riguarda questi componenti.

Decisione. Tolte le sezioni dello studio SIEM su OSSIM, ELK con Elasticsearch, Apache Metron, MozDef, Sagan e Snort; tolta l'immagine dello schema dall'albero e lo schema PNG dal materiale privato, nel Cestino; tolta dalla scheda del monitoraggio la trascrizione dello schema. Restano, perché sono il registro della scelta e non contenuto sugli strumenti, le righe del piano unificato e delle decisioni che dicono perché ciascun componente è scartato, con le fonti. Resta la sezione su Splunk Free, non valutata come scarto e marcata come non open source.

Conseguenze. È un'eccezione dichiarata ad ADR-020: contenuto dell'autore tolto per decisione dell'autore, con la ragione scritta. La storia git conserva il testo eliminato.

## ADR-028, il flusso di monitoraggio adottato: Wazuh con Suricata in OPNsense

Data: 08/10/2026. Stato: accettata. Decisione dell'utente.

Decisione. Wazuh, con server, indicizzatore e dashboard sulla stessa macchina virtuale del server Proxmox, è il centro del monitoraggio. Suricata, integrato in OPNsense, rileva sul traffico, prima in sola rilevazione. Il plugin os-wazuh-agent porta a Wazuh i log del firewall e gli allarmi di Suricata; switch, AP e NAS mandano syslog; i PC hanno l'agente. La dashboard ascolta nella VLAN 99. La risposta attiva resta spenta all'inizio. Il dettaglio tecnico, con porte, regole, ripiego e ordine di messa in opera, è in `docs/03-spunti-di-sviluppo/23-studio-home-lab/11-monitoraggio-wazuh-suricata.md`.

Conseguenze. Snort è sostituito da Suricata. La pendenza sull'integrazione fra Suricata e Wazuh è chiusa dal plugin, il cui supporto limitato è il punto fragile, con un ripiego via syslog.
