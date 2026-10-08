---
generated-from-commit: 86b5c8a61a55a48997d7757592aa4d91da9e8581
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - docs/02-ftth-fastweb/**
  - docs/03-spunti-di-sviluppo/**
  - docs/04-concetti-generali/**
  - .claude/rules/anonymization.md
  - tools/Test-Anonymization.py
last-verified-commit: 1256ba7
---

# Paradigmi di progettazione e di sicurezza

> Scheda tecnica. Raccoglie i principi che governano le scelte del lab e quelli che governano la sicurezza del repository, che sono due materie distinte e vanno tenute separate: la prima riguarda una rete da costruire, la seconda un archivio pubblico da non far diventare una mappa d'ingaggio di una casa reale.

## Il principio architetturale che regge tutto

Esiste un unico punto di decisione di livello 3, ed è il firewall. Lo switch trasporta e segmenta ma non instrada; gli access point sono ponti di livello 2 e non fanno né routing né traduzione di indirizzi; il modem dell'operatore, per quanto sia costretto a restare l'apparato di frontiera, viene ridotto a fornitore di connettività e non partecipa alla politica di sicurezza interna. Ogni volta che una funzione di sicurezza viene tentata altrove, per esempio la separazione fra rete di casa e rete ospiti fatta sul modem, il risultato è un secondo punto di decisione che nessuno controlla insieme al primo, ed è esattamente ciò che questa architettura evita.

Il corollario operativo è che il firewall resta un apparato deterministico e noioso: nessun servizio estraneo alla sicurezza di rete gira su quella macchina. Il monitoraggio, il DNS interno, la gestione endpoint e qualunque altro servizio vivono su macchine separate, tipicamente virtualizzate, e parlano con il firewall come qualunque altro host.

## Le zone e il loro contratto

Le zone sono la WAN, la DMZ su una porta fisica separata e, dietro il trunk verso lo switch, sei segmenti VLAN: 10 client fidati, 30 servizi e storage, 40 IoT, 50 ospiti, 60 laboratorio, 99 gestione. Il piano e il contratto fra zone, in forma di tabella, sono nello studio del 22/09/2026, `docs/03-spunti-di-sviluppo/23-studio-home-lab/01-architettura.md`: si nega di default e si apre porta per porta. La sicurezza non deriva dal nome della zona ma dalle regole scritte, e questo va ripetuto perché chiamare DMZ un'interfaccia non la rende isolata.

La zona non fidata è la WAN del firewall, che in questa topologia non è Internet ma la rete privata del modem. Da lì arriva traffico già tradotto una volta, e il firewall applica il proprio filtro come se fosse traffico di frontiera, perché rispetto alle reti interne lo è.

La zona fidata è la VLAN 10 dei client, con politica permissiva in uscita e chiusa in ingresso. Lo storage sta nella VLAN 30, raggiunta dalla 10 sui soli protocolli di condivisione e amministrata dalla 99 (ADR-018); gli access point hanno la gestione nella 99 e portano gli SSID CASA, IOT e OSPITI sulle VLAN 10, 40 e 50.

La zona esposta è la DMZ, che ospita il servizio raggiungibile da fuori. Il contratto è asimmetrico e va scritto in quest'ordine: dalla WAN verso la DMZ passa solo ciò che è esplicitamente inoltrato, sulle sole porte necessarie; dalla DMZ verso Internet passa il traffico in uscita necessario agli aggiornamenti e alle chiamate verso servizi esterni; dalla DMZ verso la LAN non passa nulla, e questa è la regola che rende la DMZ una DMZ. Se il servizio esposto viene compromesso, l'attaccante resta confinato in quel segmento.

## Amministrazione e monitoraggio

Dall'8/10/2026 l'amministrazione di firewall, switch, AP e NAS passa da tre soli ingressi, la workstation ADMIN, la porta di recupero della VLAN 99 e il tunnel WireGuard, verso interfacce di gestione che ascoltano solo nella VLAN 99, con TOTP e chiavi SSH (ADR-025, `docs/03-spunti-di-sviluppo/23-studio-home-lab/09-accesso-amministrativo.md`). Il monitoraggio è Wazuh su Proxmox con Suricata integrato in OPNsense e il plugin `os-wazuh-agent`, con risposta attiva spenta all'inizio (ADR-028, `11-monitoraggio-wazuh-suricata.md` nella stessa cartella). Le regole per interfaccia sono in `08-regole-fra-le-zone.md`, con le aperture a tempo del laboratorio.

## Il doppio NAT e cosa comporta davvero

La topologia impone due traduzioni di indirizzo in cascata: il modem traduce fra l'indirizzo pubblico e la propria rete privata, il firewall traduce fra quella rete e le proprie reti interne. La scelta di progetto è un solo inoltro sul modem, la porta UDP di WireGuard verso la WAN del firewall, che termina il tunnel. La funzione di host esposto, che inoltrerebbe tutte le porte e sposterebbe sul firewall ogni decisione sul traffico entrante, resta l'alternativa per quando la DMZ ospiterà un servizio pubblico. Nessuna delle due elimina la prima traduzione. La spiegazione didattica completa è in `docs/03-spunti-di-sviluppo/23-studio-home-lab/07-doppio-nat-dietro-modem-in-comodato.md`.

Le conseguenze concrete sono tre e vanno tenute a mente quando si pubblicherà un servizio. Il firewall non vede mai l'indirizzo pubblico sulla propria interfaccia, quindi ogni regola che lo assumesse sarebbe sbagliata. Il tracciamento delle connessioni attraversa due tabelle di stato invece di una, e un problema di raggiungibilità va diagnosticato su entrambe. I protocolli sensibili alla traduzione, in primo luogo la segnalazione della fonia, vanno lasciati passare senza manipolazioni applicative, disabilitando gli aiuti automatici del firewall. Una quarta conseguenza è favorevole: l'inoltro del modem riscrive la destinazione e non la sorgente, quindi i log del firewall vedono l'indirizzo vero di chi si collega.

## L'indirizzo pubblico statico come abilitatore

L'indirizzo pubblico statico, richiesto e ottenuto senza costi su una linea residenziale, è ciò che rende praticabile l'esposizione di un servizio. La documentazione contiene un'analisi estesa di che cosa accade con un indirizzo dinamico, e la conclusione è netta: un nome DNS aggiornato dinamicamente rende stabile l'identificatore ma non l'indirizzo, quindi le sessioni attive cadono a ogni cambio, la propagazione del record introduce una finestra di irraggiungibilità legata al tempo di vita della cache, e qualunque controparte che filtri per indirizzo sorgente va aggiornata a mano. Con l'indirizzo statico questi tre problemi non si pongono, ed è per questo che l'implementazione della gestione endpoint con indirizzo dinamico è stata abbandonata.

## Il segmento scoperto

Nella configurazione attuale la rete wireless generata dal modem non attraversa il firewall. Questo è il rischio principale della fase intermedia in cui il progetto si trova, ed è bene chiamarlo per nome: la segmentazione progettata copre il cablato, mentre il wireless, che è il segmento con la superficie d'attacco più ampia e i client meno controllabili, resta su una rete piatta gestita dal firewall del modem, che offre soltanto traduzione di indirizzi, filtro fra rete principale e rete ospiti e blocco delle porte non richieste.

Le due sole architetture che chiudono il buco sono mettere il modem in bridge, cosa che il suo firmware non consente, oppure spostare tutto il wireless su access point collegati allo switch a valle del firewall. Poiché la prima è preclusa, la seconda non è un miglioramento facoltativo ma il completamento necessario del progetto. Nel frattempo l'unica mitigazione disponibile è l'igiene delle impostazioni radio del modem, cioè cifratura moderna, rete ospiti separata con spegnimento temporizzato, e nessun dispositivo sensibile su quella rete.

Dal 07/10/2026 il completamento è deciso: due access point cablati ai piani centrali (ADR-017, ADR-018), con la rete ospiti nella VLAN 50 isolata sull'AP e sul firewall. Restano fuori dal perimetro per scelta dichiarata la PS5, collegata al modem per avere un NAT solo, e la Wi-Fi del modem se l'utente decide di tenerla come rete esterna: in quel caso la WAN del firewall non deve esporre l'interfaccia di gestione né altri servizi verso la rete del modem.

## Il DNS come punto di controllo

Il progetto tratta il DNS non come servizio accessorio ma come punto di controllo infrastrutturale. L'architettura scelta mette un motore di policy davanti a un resolver ricorsivo: il primo risponde ai client, applica liste di blocco e liste di permesso, e inoltra soltanto ciò che passa la policy; il secondo risolve per conto proprio interrogando i server radice, i server di dominio di primo livello e infine quelli autoritativi, validando le risposte con DNSSEC e senza mai delegare a un resolver pubblico di terzi.

La regola che rende reale questo controllo è una sola e sta sul firewall: il traffico DNS in uscita è consentito soltanto dall'indirizzo del resolver, e bloccato da qualunque altro host. Senza quella regola qualunque client può interrogare un resolver pubblico e aggirare la policy, e la configurazione diventa decorativa. Va aggiunto che distribuire ai client un secondo server DNS esterno come ripiego distrugge il modello, perché molti stack ricadono sul secondo alla prima risposta negativa: la resilienza si ottiene con ridondanza interna, non con un resolver pubblico affiancato.

## Sicurezza del repository

Il repository è destinato a un remoto pubblico, e questo cambia la natura di ogni informazione che vi si scrive. La materia è governata dalla regola `anonymization.md`, che qui si riassume nel suo principio: un progetto di home lab, se pubblicato integralmente, descrive dove si trova una casa, come raggiungerla da Internet, che cosa c'è dentro e con quale sistema operativo. Ognuno di questi dati preso da solo è innocuo, l'insieme no.

Il presidio non è la buona volontà ma un controllo eseguibile, `tools/Test-Anonymization.py`, che passa tutti i file tracciati e quelli nuovi e fallisce se trova indirizzi reali, identificativi macchina, numeri di serie, nomi propri, frammenti di ubicazione o contatti personali. Dall'8/10/2026 riconosce anche IBAN di ogni paese e carte di pagamento, validati con le loro cifre di controllo, e porta un autotest che `chiudi` esegue a ogni commit. Lo script è versionato e non contiene alcun valore reale: ciò che deve cercare vive in un file privato accanto alla mappa dei segnaposto, e se quel file manca lo script si ferma invece di restituire un verde non calcolato.

Due proprietà di questo impianto meritano di essere capite. La prima è che, dal 25/08/2026, l'anonimizzazione non è più una regola di generazione ma un gesto di scrittura: l'albero si scrive a mano, nessuna sostituzione automatica rimedia a un valore reale digitato per distrazione, e per questo la voce va aggiunta alla mappa e ai pattern privati prima di scrivere il segnaposto. Il guard-rail cerca le organizzazioni a parola intera, come i nomi propri, e ammette per costruzione le caselle su domini riservati dagli RFC 2606 e 6761, che compaiono negli esempi e nei test del template. La seconda è che la redazione si applica anche ai titoli, non solo al corpo, perché dal titolo discendono lo slug del file e il nome della cartella: un nome proprio lasciato in un titolo finisce nel percorso di un file tracciato, dove nessuna redazione del corpo lo raggiungerebbe.

## Un'esposizione nella storia pubblicata, bonificata il 07/10/2026

Va detto perché cambia il quadro rispetto a quanto la documentazione precedente lasciava intendere. Il remoto non è da collegare: esiste ed è già pushato fino al commit di riferimento. Nella regola sull'identità git, prima dell'allineamento al template del 24/08/2026, comparivano in chiaro la casella di posta di lavoro e il nome dell'organizzazione di lavoro dell'autore. L'allineamento li ha sostituiti con segnaposto, quindi da questo commit in avanti l'albero è pulito, ma la storia li conserva.

La casella personale e l'utente GitHub, che comparivano nello stesso file, non costituiscono un'esposizione aggiuntiva perché coincidono con i metadati di autore di ogni commit: anonimizzarli nel testo non avrebbe alcun effetto protettivo. La casella di lavoro e il nome dell'organizzazione sono invece un'esposizione reale e non necessaria, ed è esattamente il caso previsto dalla regola: si segnala, si corregge nel file corrente, si registrano i valori nel file privato dei pattern perché il guard-rail li intercetti se rientrassero, e si annota la bonifica della storia come lavoro a parte, da pianificare con backup e non da improvvisare a valle di una sessione.

La bonifica è stata decisa dall'autore ed eseguita il 07/10/2026. Una scansione di ogni oggetto della storia con i pattern privati ha trovato i valori di lavoro in quattro versioni storiche di due file e in nessun metadato; la storia è stata riscritta in un clone separato, sostituendo i valori con segnaposto, con l'albero dell'ultimo commit identico all'originale, e pubblicata con un push forzato dopo un backup completo. La casella personale resta negli autori dei commit per scelta dell'autore. I commit precedenti restano raggiungibili per hash sulla piattaforma finché questa non li elimina, e una rimozione garantita passa da una richiesta al suo supporto. Gli hash citati nei documenti scritti prima di quella data si riferiscono alla storia originale.

La visibilità del repository è verificata il 07/10/2026 dall'interfaccia pubblica della piattaforma: è pubblico, senza fork. L'impostazione del progetto lo assumeva già per prudenza, e non cambierebbe se diventasse privato, perché un repository privato oggi può tornare pubblico domani con tutta la sua storia.

## Perimetro delle operazioni git

Le operazioni di aggiunta, commit e push restano manuali dell'utente, e le regole di negazione in `.claude/settings.json` le bloccano anche in modalità permissiva. L'identità git è impostata a livello locale del repository secondo `identita-git/RIFERIMENTO.md`, così che un progetto personale non finisca firmato con l'identità di lavoro su una macchina condivisa. Il controllo di anonimizzazione va eseguito prima di ogni commit che tocchi documentazione, e sull'intero albero tracciato, non sui soli file modificati: un residuo non si introduce, si eredita.
