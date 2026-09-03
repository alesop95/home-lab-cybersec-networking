# Registro delle decisioni

> Registro ADR-lite, append-only. Ogni voce fissa una decisione architetturale con il suo contesto, le alternative considerate e le conseguenze accettate. Una decisione non si cancella e non si riscrive: se cambia, si aggiunge una voce nuova che la supera e si annota la sostituzione nella voce vecchia. Le decisioni qui registrate sono ricostruite dal documento sorgente e dalle evidenze del progetto, non inventate; dove la fonte non permette di stabilire una data, il campo lo dichiara.

## ADR-001, il firewall sta a valle del modem dell'operatore

Data: fine febbraio 2026, consolidata con il ticket del 26/02 e la conferma del 28/02. Stato: accettata, non reversibile senza cambiare contratto o apparato.

Contesto. L'obiettivo iniziale era rendere il firewall l'apparato di frontiera, collegandolo direttamente all'ONT e riducendo il modem dell'operatore a punto di accesso wireless. Due evidenze indipendenti lo escludono: una prova condotta da un fornitore, che ha collegato il firewall direttamente all'ONT senza ottenere traffico, e la conferma esplicita dell'assistenza tecnica. La causa piu' probabile e' che l'ONT sia vincolato all'indirizzo hardware del modem fornito in comodato, comportamento non standard ma adottato da alcuni operatori. Si aggiunge che l'interfaccia del modem non espone alcuna modalita' bridge, ne' passthrough del protocollo di autenticazione, ne' passthrough di VLAN.

Alternative considerate. Collegare il firewall direttamente all'ONT, scartata perche' non funziona. Attivare un modem di proprieta' con la procedura dedicata dell'operatore, tenuta aperta come possibilita' futura ma non perseguita perche' comporta l'acquisto di un apparato e la riapertura del tema dei parametri di accesso.

Decisione. La catena e' ONT, modem dell'operatore, firewall, switch, access point. Il modem termina la sessione con l'operatore e detiene l'indirizzo pubblico; il firewall e' il router e il punto di sicurezza di tutte le reti interne.

Conseguenze accettate. Doppio NAT strutturale. La rete wireless del modem resta fuori dal perimetro del firewall finche' non viene sostituita da access point a valle. I parametri di accesso alla rete dell'operatore, cioe' protocollo e VLAN, diventano irrilevanti per la configurazione del firewall, perche' restano interni al modem: e' l'unica conseguenza positiva del vincolo.

## ADR-002, OPNsense come piattaforma firewall

Data: non databile con precisione dal sorgente, precedente all'installazione del 16/01/2026. Stato: accettata, attuata parzialmente.

Contesto. Serve una piattaforma firewall in grado di gestire 2,5 Gbps reali con traduzione di indirizzi con stato, VLAN e VPN, su hardware x86 riutilizzato.

Alternative considerate. Un mini-PC generico di importazione con firewall preinstallato, scartato per assenza di garanzie su firmware documentato, aggiornamenti di sicurezza e qualita' della componentistica, che in un apparato di sicurezza sono il punto di rottura. pfSense, scartato per decisioni di licenza e una tabella di marcia meno aperta, pur restando tecnicamente valido. Una distribuzione Linux generica con filtro di pacchetti configurato a mano, scartata perche' richiederebbe messa a punto profonda di tabelle, tracciamento connessioni, affinita' degli interrupt e gestione manuale degli aggiornamenti, aumentando il rischio operativo. IPFire, confrontato voce per voce e scartato per prestazioni meno prevedibili in traduzione intensiva e per un'integrazione dei servizi meno ricca. NethSecurity, citata e non valutata.

Decisione. OPNsense 25.7, installazione bare-metal su macchina dedicata, con WAN e LAN su schede fisicamente separate e nessun servizio estraneo alla sicurezza in esecuzione su quella macchina.

Conseguenze accettate. Lo stack e' FreeBSD, quindi la nomenclatura delle interfacce segue il driver e non la convenzione prevedibile di Linux, e la compatibilita' delle schede va valutata sul supporto FreeBSD e non su quello Linux.

## ADR-003, tre interfacce fisiche per tre zone

Data: non databile con precisione, contestuale alla scelta dell'hardware. Stato: accettata, non ancora attuata.

Contesto. La macchina scelta ha una scheda gigabit integrata e due slot liberi, riempiti con due schede a 2,5 Gbps basate su chipset Realtek RTL8125B, per una spesa complessiva contenuta.

Decisione. Una scheda a 2,5 Gbps come WAN verso il modem, l'altra come LAN verso lo switch, la gigabit integrata come zona esposta. Le velocita' non sono vincolate dal ruolo logico: la zona esposta sta sulla porta piu' lenta perche' il servizio che ospitera' non ha bisogno di banda multigigabit.

Alternative considerate. Schede Intel della serie i225 o i226, riconosciute come piu' affidabili sotto lo stack FreeBSD, non acquistate per costo; le Realtek sono documentate come pienamente supportate dal driver nelle versioni recenti. Adattatori da USB a 2,5 Gbps, esclusi per latenza, instabilita' sotto carico e comportamento imprevedibile.

Conseguenze accettate. Se in futuro emergesse instabilita' sotto carico, la sostituzione delle due schede con equivalenti Intel e' un intervento circoscritto che non tocca l'architettura.

## ADR-004, richiesta e adozione dell'indirizzo pubblico statico

Data: richiesta il 26/02/2026, sollecitata e confermata il 05/03/2026. Stato: accettata, attuata.

Contesto. Il progetto prevede di esporre almeno un servizio dalla zona esposta. Su linea residenziale l'indirizzo pubblico e' tipicamente dinamico, e la sua variazione, pur non periodica, invalida sessioni attive, richiede aggiornamento del nome DNS con una finestra di incoerenza legata al tempo di vita della cache, e rompe qualunque autorizzazione basata su indirizzo presso terzi.

Decisione. Richiesta dell'indirizzo statico all'operatore, ottenuta senza costi aggiuntivi trattandosi di un profilo residenziale.

Conseguenze. Decade l'intera linea di implementazione della gestione endpoint basata su DNS dinamico, che resta nella documentazione come analisi dei limiti di un indirizzo dinamico e non come piano. Diventa praticabile la pubblicazione di servizi con inoltro di porte dalla zona esposta.

Nota di verifica. Al momento della lettura dell'interfaccia del modem in febbraio, la connessione attiva risultava essere quella mobile di riserva e non la fibra, quindi i parametri letti in quella occasione non sono quelli della linea in fibra. La rilettura a fibra attiva e' fra le pendenze.

## ADR-005, switch gestito di livello 2 senza alimentazione via cavo

Data: non databile con precisione, successiva alla scelta del firewall. Stato: accettata, non ancora acquistato.

Contesto. Serve distribuzione a 2,5 Gbps con segmentazione, a valle di un firewall che e' gia' l'unico punto di decisione di livello 3.

Alternative considerate. Uno switch non gestito, scartato perche' non riconosce le etichette di VLAN e quindi rende impossibile la segmentazione. Un modello con routing di livello 3, scartato perche' quella capacita' non serve in una topologia dove nessun traffico fra VLAN deve evitare il firewall, e costa di piu'. Un modello di un vendor la cui gestione dipende da un controller esterno, scartato perche' introduce una dipendenza infrastrutturale che una rete domestica non ha motivo di assumere, e senza il controller si comporta di fatto come un non gestito.

Decisione. Zyxel XMG1915-10E, otto porte a 2,5 Gbps piu' due porte ottiche a 10 Gbps per collegamenti futuri, gestione locale via interfaccia web senza software esterno, senza alimentazione via cavo.

Conseguenze accettate. L'access point al piano inferiore va alimentato con un iniettore separato, il cui modello e' gia' individuato, perche' lo switch non fornisce alimentazione sulle porte.

## ADR-006, il wireless passa dal firewall tramite access point a valle

Data: non databile con precisione, discende da ADR-001. Stato: accettata, non attuata.

Contesto. Con il firewall a valle del modem, la rete wireless generata dal modem e' interna alla LAN del modem stesso e non attraversa il firewall.

Alternative considerate. Mettere il modem in bridge, preclusa dal firmware. Accettare il wireless scoperto, scartata perche' e' il segmento con la superficie d'attacco piu' ampia e i client meno controllabili.

Decisione. Tutto il wireless viene rifatto con access point collegati allo switch a valle del firewall, che agiscono come ponti di livello 2 e non fanno routing; la radio del modem viene spenta o ridotta a sola rete ospiti.

Conseguenze accettate. Serve portare un cavo al piano inferiore, che e' la parte materialmente piu' difficile del progetto, e serve un iniettore per l'alimentazione.

## ADR-007, DNS interno come punto di controllo, non come servizio accessorio

Data: non databile con precisione. Stato: accettata, non attuata.

Contesto. Il traffico DNS precede qualunque connessione e ne rivela la destinazione. Lasciarlo a un resolver di terzi significa cedere visibilita' e controllo su tutto cio' che la rete raggiunge.

Alternative considerate. Un solo motore di blocco pubblicitario che inoltra a un resolver pubblico, scartato perche' e' un filtro davanti a una dipendenza esterna, non un'infrastruttura DNS: mantiene l'esposizione delle interrogazioni e il punto singolo di guasto altrove. Un resolver ricorsivo nudo, scartato perche' non offre policy.

Decisione. Motore di policy davanti a resolver ricorsivo completo con validazione crittografica delle risposte, su una macchina dedicata con indirizzo interno fisso. Il firewall consente traffico DNS in uscita soltanto da quell'indirizzo.

Conseguenze accettate. La regola di uscita sul firewall e' parte integrante della decisione, non un'aggiunta: senza di essa qualunque client puo' aggirare la policy e la configurazione diventa decorativa. Non si distribuisce ai client alcun resolver esterno come secondario, perche' molti stack ricadono sul secondario alla prima risposta negativa.

## ADR-008, la documentazione si genera, non si scrive due volte

Data: 24/08/2026. Stato: superata da ADR-010 il 25/08/2026. Resta valida la parte sull'ingestione iniziale, cioe' che il contenuto e' entrato nel repository per conversione deterministica e non per riscrittura; non vale piu' la parte sulla rigenerazione continua.

Contesto. La base documentale e' un unico documento Word molto grande, che l'autore continua a modificare. Riscrivere a mano il suo contenuto nel repository creerebbe due verita' destinate a divergere.

Alternative considerate. Riscrittura curata in una ventina di documenti tematici, scartata perche' la completezza dipenderebbe dalla riscrittura invece che da un controllo meccanico, e perche' ogni modifica al sorgente andrebbe riportata a mano. Solo albero generato senza layer curato, scartata perche' un dump navigabile non dice quale sia lo stato del progetto ne' perche' le scelte sono quelle.

Decisione. Conversione deterministica e ripetibile del sorgente in un albero versionato, con verifica automatica di completezza, piu' un layer curato scritto a mano che vive accanto all'albero e non dentro di esso. I file generati non si modificano mai a mano: si corregge il sorgente, oppure si aggiunge un banner nel sidecar delle annotazioni.

Conseguenze accettate. Chi clona il repository non puo' rigenerare l'albero, perche' il sorgente non e' versionato. La documentazione resta leggibile ma la sua rigenerazione dipende dal materiale locale dell'autore.

## ADR-009, anonimizzazione come regola di generazione, applicata anche ai titoli

Data: 24/08/2026. Stato: accettata, attuata.

Contesto. Il repository e' destinato a un remoto pubblico e il materiale contiene l'indirizzo dell'abitazione, l'indirizzo pubblico statico della linea, identificativi di apparato, nomi macchina, numeri di serie, nomi di persona e riferimenti contrattuali. Presi insieme descrivono dove si trova una casa, come raggiungerla e che cosa c'e' dentro.

Alternative considerate. Revisione manuale del testo generato, scartata perche' verrebbe annullata alla rigenerazione successiva. Pubblicare solo il layer curato tenendo l'albero generato in locale, scartata perche' il dettaglio fine non sarebbe piu' recuperabile da un clone.

Decisione. Le sostituzioni vivono in un sidecar privato applicato dal convertitore, i valori reali in una mappa privata, e un guard-rail eseguibile controlla tutti i file tracciati prima di ogni commit. La redazione si applica anche ai titoli, perche' dal titolo discendono lo slug del file e il nome della cartella: senza questa estensione due nomi propri sarebbero finiti nei percorsi di file tracciati, dove nessuna redazione del corpo li avrebbe raggiunti. Il convertitore e' stato modificato di conseguenza rispetto alla versione del pacchetto di origine.

Conseguenze accettate. Restano reali per decisione motivata i nomi di operatore e vendor, i modelli di apparato, il piano di indirizzamento privato, gli indirizzi di gestione di fabbrica, gli indirizzi pubblici di transito di un traceroute, i contatti istituzionali di un registro regionale e i prezzi di listino pubblici. Il razionale di ciascuna eccezione e' scritto nella regola, perche' un'eccezione non motivata diventa una crepa.

Aggiornamento del 25/08/2026. Con ADR-010 l'albero non si rigenera piu', quindi il sidecar di redazione non viene piu' applicato a ogni corsa: il contenuto nuovo si scrive gia' anonimizzato. Il presidio resta il guard-rail eseguibile, che e' sempre stato la parte che conta, perche' il sidecar sostituiva i valori noti mentre il guard-rail verifica il risultato. Il sidecar si conserva come registro di cio' che e' stato sostituito nella prima stesura, e va comunque tenuto allineato alla mappa insieme al file dei pattern.

## ADR-010, la fonte diventa il repository, non piu' il documento Word

Data: 25/08/2026. Stato: accettata, attuata. Supera ADR-008.

Contesto. Con la conversione completata e verificata, tenere il documento Word come fonte viva ha smesso di avere senso e ha cominciato ad avere costi. E' un binario da ventun megabyte, non diffabile, modificabile solo dentro un elaboratore di testi fuori dalla portata dell'agente, che per essere letto richiede la disciplina della disclosure progressiva e che per essere aggiornato impone un ciclo di rigenerazione dell'intero albero. Il modo in cui il lavoro procede davvero, invece, e' aprire una sessione nuova sul repository e continuare da dove si era rimasti.

Il punto non e' l'eleganza del formato ma dove vive la continuita'. Se la fonte e' il Word, una sessione nuova deve prima ricostruirsi il contesto da un binario; se la fonte e' il repository, la continuita' e' gia' scritta nei file che la sessione legge comunque all'avvio, cioe' l'indice di memoria, le schede di contesto e l'albero.

Alternative considerate. Tenere entrambe le fonti vive, scartata subito perche' produrrebbe due verita' destinate a divergere, che e' esattamente il problema che ADR-008 voleva evitare. Continuare con il Word come fonte e usare il repository come sola vetrina, scartata perche' e' lo stato che si sta abbandonando. Reimportare occasionalmente da un Word aggiornato, scartata perche' incompatibile con la manutenzione a mano: una reimportazione sovrascriverebbe il lavoro fatto nel frattempo.

Decisione. L'albero `docs/` passa a manutenzione manuale. Il documento Word resta in `_notes/sorgenti/` come archivio della prima stesura e prova di provenienza, non come fonte. Il convertitore resta nel repository perche' e' lo strumento che ha prodotto l'albero e la sua storia va conservata, ma non va piu' eseguito su `docs/`.

Attuazione. Il lucchetto non e' una raccomandazione scritta ma un controllo nel codice: il convertitore scrive nella cartella di destinazione un timbro `.generato-da-docx`, e si rifiuta di scrivere in una cartella che contiene gia' documenti senza quel timbro. Congelare l'albero e' consistito nel rimuovere il timbro. Chi dovesse insistere ha l'opzione esplicita `--forza`, che il messaggio di errore nomina insieme alla conseguenza. La ragione per cui serve un controllo e non una nota e' che la procedura di rigenerazione era scritta in quattro file diversi, e una sessione futura che ne legge uno la eseguirebbe in buona fede.

Conseguenze. I marcatori che escludevano l'albero dalla normalizzazione Markdown sono stati rimossi e l'albero e' stato normalizzato: non e' piu' testo verbatim di una fonte esterna, e' documentazione del progetto come tutto il resto. Il sidecar delle annotazioni non viene piu' applicato e i suoi banner sono ormai testo dentro i file. La coerenza dell'albero, che prima era garantita per costruzione dalla struttura dei titoli del sorgente, ora va verificata, e per questo esiste `tools/check-docs-tree.py`. I prefissi numerici di cartelle e file restano come nomi stabili e non si rinumerano piu': per inserire qualcosa si usa il primo numero libero.

## ADR-011, il NAS non resta accesso sempre: finestra di accensione notturna

Data: 02/09/2026. Stato: accettata, non ancora attuata perche' la macchina non e' assemblata.

Contesto. L'analisi delle sei bollette mensili del 2026 ha prodotto un numero che ha cambiato la valutazione del progetto. Il costo marginale di un kilowattora su questa fornitura e' di 0,256 euro, comprensivo di accisa e imposta, e va distinto dal prezzo medio apparente di 0,558 euro che si ottiene dividendo la spesa totale per i consumi: quel secondo numero e' gonfiato dai costi fissi mensili divisi su un consumo domestico basso, scenderebbe da solo se il consumo aumentasse, e non serve a decidere niente. Con il costo marginale, un archivio di rete stimato a sessanta watt alla presa e acceso in continuo costa circa centotrentacinque euro all'anno.

Il dato che ha determinato la decisione non e' pero' il valore assoluto ma il rapporto. L'abitazione consuma circa ottantasette kilowattora al mese, una frazione della media domestica nazionale, e la macchina ne consumerebbe quarantaquattro: un incremento di circa la meta' del consumo elettrico di casa, che nei mesi estivi rilevati a sessanta e sessantadue kilowattora renderebbe l'archivio di rete il singolo apparato che consuma piu' di ogni altro. La ragione non e' che sessanta watt siano molti, ma che il funzionamento e' continuo mentre tutto il resto della casa consuma poco: e' il tempo di accensione a determinare il costo, non la potenza.

Alternative considerate. Il funzionamento continuo, che e' il default implicito di ogni progetto di archivio di rete e che si sarebbe adottato senza porsi la domanda. La sospensione dei dischi durante il funzionamento, scartata come misura principale perche' produce cicli di avvio molto frequenti sui dischi meccanici e perche' le verifiche periodiche li risvegliano comunque, quindi il risparmio e' minore di quanto sembra e l'usura maggiore. La riduzione della memoria o la rinuncia a un disco a stato solido, scartate perche' valgono pochi watt e costano funzioni che servono. L'acquisto di un alimentatore nuovo ed efficiente, che rientrerebbe in tre o quattro anni e resta marginale rispetto alla scelta fra quelli gia' disponibili.

Decisione. La macchina resta spenta nelle ore notturne, con due orari distinti fra i giorni lavorativi e il fine settimana, per un totale di cinquanta ore spente su centosessantotto, cioe' il settanta per cento di tempo acceso. Il risparmio e' di quaranta euro all'anno, cioe' il trenta per cento del costo di esercizio, e riduce l'incremento sul consumo di casa dal cinquanta al trentacinque per cento.

Va detto che una valutazione preliminare, fatta ipotizzando quattro ore di accensione al giorno, indicava un fattore sei di risparmio. Con una finestra di sedici o diciassette ore quel fattore non si realizza e il risparmio reale e' di un terzo: la differenza fra le due cifre e' significativa e la registrazione della decisione la conserva, perche' una decisione presa su un numero sbagliato va rivalutata quando il numero si corregge, e in questo caso la decisione regge comunque.

Attuazione. Servono due meccanismi distinti e non uno, ed e' il punto in cui un piano approssimativo si rompe. Lo spegnimento si programma dal sistema operativo con un'attivita' pianificata, perche' e' l'unico meccanismo che distingue i giorni della settimana, e deve essere un arresto ordinato: il file system e' transazionale e non si corromperebbe nemmeno con un taglio di corrente, ma le scritture in volo si perderebbero, e una macchina il cui scopo e' custodire dati non si spegne strappando la spina. La riaccensione non puo' venire dal sistema, che a macchina spenta non gira, e viene dall'allarme dell'orologio in tempo reale del firmware, che il manuale documenta come capace di programmare giorni e ore. E' preferibile al risveglio da rete, che la scheda pure supporta, perche' non dipende da nessun apparato esterno.

L'allarme del firmware ammette un solo orario giornaliero mentre la decisione ne prevede due: si imposta sull'orario piu' precoce e si accetta che nel fine settimana la macchina si accenda un'ora e mezza prima del necessario, per un costo di meno di trenta centesimi al mese. Complicare la configurazione per recuperarli sarebbe un cattivo scambio.

Conseguenze. Le attivita' pianificate non girano a macchina spenta e non lo segnalano: ogni orario va ricollocato dentro la finestra di accensione, e deve avere il tempo di completarsi prima dello spegnimento. Il caso concreto e' la verifica periodica dell'integrita' del pool, che il sistema crea da se' a mezzanotte del sabato e che con questa finestra partirebbe due ore e mezza prima di uno spegnimento, venendo interrotta: va spostata alla mattina del sabato, subito dopo la riaccensione. I salvataggi automatici notturni da altri apparati non troverebbero la destinazione, ed e' il conflitto piu' sostanziale perche' essere destinazione dei backup della rete e' uno degli usi principali di un archivio di rete: se quell'uso si concretizza, gli orari vanno portati dentro la finestra oppure la finestra va ripensata. L'impostazione di riaccensione dopo un'interruzione di corrente resta incondizionata, perche' l'alternativa che ripristina lo stato precedente introduce un modo di fallire peggiore, cioe' una macchina che resta spenta quando la si vuole accesa.

Un timore che non si realizza riguarda l'usura dei dischi: uno spegnimento al giorno significa circa trecentosessantacinque cicli all'anno contro tolleranze dichiarate di decine di migliaia, e non e' una sollecitazione significativa.

## ADR-012, l'alimentatore si sceglie fra quelli disponibili, e piu' piccolo e' meglio

Data: 03/09/2026. Stato: accettata, da attuare durante l'assemblaggio.

Contesto. Il progetto dispone degli alimentatori di tutte le macchine dismesse, e la scelta fra loro non e' indifferente. Un alimentatore rende al meglio attorno al cinquanta per cento del carico nominale e perde rapidamente scendendo; la macchina assorbira' fra trenta e quarantacinque watt in continua, che su un alimentatore da cinquecento watt e' il nove per cento del carico, cioe' la zona peggiore della curva. La differenza di rendimento fra un alimentatore mal dimensionato e uno adatto, in quella zona, vale cinque a dieci watt continui, cioe' da undici a ventidue euro all'anno su una macchina il cui costo di esercizio complessivo e' di circa novantacinque.

Il fatto controintuitivo, e la ragione per cui questa decisione merita di essere registrata, e' che un alimentatore piu' piccolo e' migliore e non peggiore, purche' copra il picco. La certificazione di efficienza piu' diffusa misura il rendimento al venti, al cinquanta e al cento per cento del carico e non dice nulla su cosa accade al dieci per cento, che e' invece la condizione in cui questa macchina lavorera' per tutta la sua vita: soltanto il livello piu' alto della scala specifica anche quel punto. Un alimentatore da settecentocinquanta watt certificato, a quaranta watt di carico, puo' rendere peggio di uno da trecento non certificato.

Il picco da coprire non e' il consumo a riposo. All'accensione i dischi meccanici assorbono da venti a venticinque watt ciascuno per qualche secondo mentre i motori raggiungono la velocita' di regime, quindi il picco realistico dell'intera macchina sta fra centocinquanta e duecento watt.

Alternative considerate. L'acquisto di un alimentatore nuovo ed efficiente, che costerebbe fra cinquanta e settanta euro e rientrerebbe in tre o quattro anni: scartato come primo passo perche' marginale, e riproponibile se la scelta fra quelli disponibili non desse un candidato adatto. Il confronto misurato alla presa fra i migliori candidati, che sarebbe il metodo piu' rigoroso perche' la differenza fra due letture nella stessa condizione e' direttamente la differenza di rendimento sul carico reale: scartato per proporzionalita', perche' richiede di montare e smontare la macchina piu' volte per un guadagno che la lettura delle etichette approssima abbastanza bene.

Decisione. Si scelgono per lettura delle etichette, con criteri in ordine di importanza: la potenza nominale piu' bassa che copra duecento watt di picco, quindi un obiettivo fra trecento e quattrocento watt; poi la certificazione piu' alta a pari potenza; poi la data di fabbricazione piu' recente, perche' i condensatori elettrolitici degradano con il tempo e con il calore e un alimentatore di dodici anni puo' avere capacita' residua molto inferiore alla nominale; e infine la disponibilita' dei connettori necessari, cioe' ventiquattro pin per la scheda, otto pin per il processore e almeno quattro connettori per dischi.

Va verificata anche la corrente disponibile sulla linea a dodici volt, che e' quella da cui si alimenta praticamente tutto in una macchina moderna e che su alimentatori vecchi o economici e' molto inferiore a quanto il totale dichiarato suggerisce.

Conseguenze. La lettura delle etichette non si puo' fare con il censimento software, e non e' una lacuna degli strumenti: un alimentatore ATX non ha nessuna interfaccia dati verso la scheda madre, quindi non esiste una classe da interrogare e l'etichetta e' la sola fonte. Ne discende che questa attivita' appartiene alla fase di smontaggio, quando i case sono comunque aperti, e non alla preparazione: l'etichetta e' spesso girata verso l'interno del case e puo' richiedere di sfilare l'alimentatore per leggerla.
