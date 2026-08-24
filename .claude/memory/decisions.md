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

Data: 24/08/2026. Stato: accettata, attuata.

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
