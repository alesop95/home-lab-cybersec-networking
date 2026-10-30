# NordVPN condivisa: uso escluso dal lab e cautele

Aggiornamento del29/10/2026, ADR-046. La richiesta dell’utente è recepire il rapporto locale sul mancato utilizzo della VPN nel contesto domestico e sui rischi dell’account condiviso. Il rapporto distingue NordVPN spenta a casa da eventuale uso personale fuori casa; esclude Meshnet con quell’account. Questa scheda mantiene tale perimetro, senza trasformarlo in un divieto generale di qualunque VPN o ritirare Tailscale già richiesto in ADR-045.

Il rapporto HTML corrente è letto e copiato nel livello privato con SHA-256 verificato, originale conservato. PDF, schermate delle fonti e versioni d’archivio non sono stati letti: l’HTML indica il PDF come export e gli altri documenti come prove o stesure superate. La bibliografia è censita, ma non tutti i collegamenti sono verificati autonomamente. Fonte locale S261; fonti ufficiali selezionate S262-S268. Non sono stati aperti Nord Account, dati di fughe altrui o configurazioni del telefono.

## Decisione per la rete di casa

| Bisogno | Regola recepita | Stato |
|---|---|---|
| Navigare dalla rete domestica con le policy locali | tunnel NordVPN spento; nessuna VPN commerciale sul router per tutta la casa | scelta, non controllo del telefono già eseguito |
| Raggiungere NAS, server o assistente da fuori | percorsi privati WireGuard del disegno amministrativo e Tailscale del filone assistente, con destinazioni autorizzate | progettazione; nessun tunnel domestico collaudato |
| Collegare dispositivi con l’account Nord condiviso | Meshnet non si usa; disattivata sui dispositivi di questo progetto che avessero quell’account | vincolo da verificare sugli endpoint, nessuna modifica remota eseguita |
| VPN personale su rete estranea | eventuale uso NordVPN separato dal lab, secondo bisogno e regole della rete | il rapporto lo contempla; nessun obbligo generalizzato o collaudo qui |
| Password, file e monitoraggio di dati personali | identità e custodia personali, separati dall’account condiviso | nessun import di dati o adesione ai servizi accessori effettuati |

Il firewall OPNsense è installato ma non configurato nella topologia definitiva, switch/AP e DNS filtrante restano da mettere in esercizio. La Wi-Fi del modem a monte è fuori da quel futuro perimetro. Quindi la regola NordVPN spenta a casa non dimostra che oggi tutti i dispositivi siano già protetti dai controlli del progetto.

## Perché il tunnel cambia ciò che il lab può controllare

Deduzione progettuale: un tunnel completo può portare risoluzione DNS e traffico applicativo a un servizio esterno, togliendoli alla policy DNS e alla visibilità interna della rete domestica. Il firewall continua a vedere e governare la connessione esterna del tunnel; non scompare dal percorso. Non ne consegue però che possa leggere i flussi cifrati interni. La separazione riguarda punti di controllo diversi, come nella [matrice dei bisogni](16-bisogni-controlli-e-flussi.md).

Lo split tunneling non garantisce da solo l’uso del DNS di casa: NordVPN documenta casi in cui l’applicazione esclusa esce con l’IP dell’operatore mentre il DNS rimane NordVPN, S265. Per un’eventuale eccezione futura servono osservazioni delle rotte e della risoluzione effettiva, non il solo interruttore di un’app. Anche DNS privato del sistema e DNS del browser hanno impostazioni proprie da verificare al collaudo.

SmartDNS e VPN sul router non sono introdotti nel disegno. Un cambiamento di resolver ricadrebbe su ADR-007; una nuova uscita o un ingresso remoto richiederebbero il relativo aggiornamento di rete. Nessuna configurazione commerciale viene aggiunta per il solo fatto che un abbonamento esista.

## Account condiviso: cosa tenere fuori

Meshnet distingue permessi di collegamento, file, instradamento e rete locale, S263. Non basta confondere la disconnessione del server VPN con la disattivazione di queste funzioni. S264 documenta che l’accesso LAN si combina con traffic routing e può raggiungere gli apparati locali: è un percorso che il progetto non vuole concedere attraverso l’account condiviso. Qui la scelta resta non usare Meshnet, senza tentare di renderla equivalente alla policy Tailscale di un’identità privata.

Dark Web Monitor rende consultabili gli avvisi da Nord Account e può mostrare dati esposti nelle fughe, S266. Con credenziali condivise manca la separazione personale degli accessi a quel pannello: è una deduzione del modello di autenticazione, coerente con il riscontro riportato nel documento locale. Non inserire in quel profilo email, telefono, carte o documenti personali; non aprire dati di fughe di altri partecipanti. I dettagli della fuga citata nel rapporto non sono stati esaminati o ripubblicati qui.

Il vault personale di password e i file riservati non devono dipendere dall’identità o dal recupero account del titolare del gruppo. Non riusare la password condivisa in altri servizi; diffidare delle richieste di codici ricevute da contatti non verificati. Quote, recupero account, dispositivi e rinnovo sono responsabilità da coordinare con il titolare: nessun prezzo, scadenza contrattuale o diritto di utilizzo viene confermato da questa scheda tecnica. Nessuna credenziale è stata richiesta o usata dall’agente.

## Android: distinguere gli interruttori

Android permette un solo VpnService attivo per utente o profilo, S262. Sullo stesso profilo del telefono, passare fra NordVPN, WireGuard e Tailscale può sostituire il tunnel precedente; il percorso va scelto per il bisogno del momento, senza promettere una concatenazione automatica.

Auto-connect dell’app, VPN sempre attiva di Android e Blocca connessioni senza VPN sono controlli distinti. L’ultimo impone il blocco del traffico fuori tunnel; non è una conseguenza inevitabile della sola opzione sempre attiva. Per il percorso domestico con NordVPN intenzionalmente spenta, il rapporto propone auto-connect disattivato e nessun blocco che impedisca quell’uso. Sono indicazioni da verificare nel profilo NordVPN del telefono, non modifiche da applicare indiscriminatamente a futuri profili gestiti o aziendali.

Il rapporto segnala funzioni separate di protezione chiamate/SMS e controllo di contenuti. Stato e permessi di quei componenti vanno trattati a parte: non provano che il tunnel sia attivo né sostituiscono la policy del lab. Non sono stati riletti sul telefono in questo giro.

## Precisazioni rispetto alle frasi assolute del rapporto e dei vecchi appunti

Una VPN non è l’unica protezione su un Wi-Fi estraneo. TLS/HTTPS fornisce cifratura, integrità e autenticazione del server anche su una rete non fidata, S267; restano aggiornamenti, identità della rete e controllo dei certificati. Una VPN aggiunge un altro confine di fiducia e non elimina phishing o compromissione dell’endpoint. Non si rende la VPN obbligatoria per ogni uso fuori casa soltanto per quella frase del rapporto.

Meshnet non è l’unico possibile accesso illecito a un telefono: applicazioni compromesse, credenziali riusate e altri strumenti remoti hanno percorsi distinti. Tenerla spenta chiude il percorso Meshnet previsto da questa scelta, senza promettere immunità generale. Nemmeno il furto dell’account condiviso va ridotto automaticamente alla sola perdita del servizio: contano dati consultabili e autorizzazioni concesse.

Il tunnel e i prodotti accessori di una suite commerciale vanno valutati separatamente. La documentazione NordVPN per Windows descrive anche protezioni web e file oltre al tunnel, S268: i vecchi appunti che riducono ogni funzione a semplice cifratura o solo DNS sono troppo assoluti. Questo non trasforma la suite nel firewall o nell’EDR del progetto, né ne autorizza installazione o sostituzione dei controlli già scelti.

## Collaudo futuro e raccordo con Tailscale

Alla messa in esercizio si devono osservare, sui dispositivi interessati, tunnel commerciale disconnesso a casa, Meshnet disattivata, resolver effettivo e raggiungibilità dei soli servizi autorizzati. Dal telefono su rete mobile, il test dell’accesso domestico riguarda il tunnel WireGuard o Tailscale scelto e deve includere una destinazione ammessa e una negata. Si verifica anche il passaggio fra i profili Android, senza assumere che restino entrambi attivi.

Il rapporto locale cita WireGuard come unico accesso futuro; ADR-045 ha nel frattempo aggiunto Tailscale per casa e assistente. Questo raccordo conserva la decisione più recente, descritta nello [studio17](17-assistente-personale-hermes-nix-e-memoria.md), e non introduce Meshnet o un exit node. Il [racconto didattico10](../../../.claude/context/refactor-10-vpn-commerciale-e-accesso-domestico.md) spiega il confine fra privacy dell’uscita, identità condivisa e accesso alla LAN. Nessuna prova su telefono, modem o account è dichiarata eseguita.
