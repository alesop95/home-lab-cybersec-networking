# Bisogni della rete, strumenti e punti di controllo

Ritorno allo [studio](README.md). Documento tecnico del 23/10/2026, approvato dall'utente insieme alle raccomandazioni di ADR-037. È il riferimento per distinguere i bisogni della rete e il controllo che risponde a ciascuno. Il racconto di come questa distinzione è stata adottata sta nel [livello tecnico-didattico](../../../.claude/context/studio-didattico-master.md).

Le righe che seguono descrivono il progetto, non certificano che i servizi siano già in esercizio. In questa sessione sono stati osservati hardware e firmware del NAS; non sono state configurate VLAN, VPN, policy Cloudflare o DNS della casa. La separazione fra decisione ed esecuzione rimane visibile anche quando una raccomandazione è approvata.

## La matrice dei bisogni

| Bisogno concreto | Strumento scelto o candidato | Dove si applica il controllo | Che cosa resta fuori | Stato |
|---|---|---|---|---|
| amministrare firewall, switch, AP e NAS da fuori casa | WireGuard su OPNsense, poi credenziali delle interfacce | chiave del dispositivo al tunnel; regole verso la VLAN 99; autenticazione del servizio | il tunnel non autorizza ogni porta e non filtra automaticamente la navigazione Internet | deciso, ADR-025 e ADR-037; collaudo da eseguire |
| leggere i file del NAS da fuori casa | WireGuard e condivisione SMB | regola dalla rete del tunnel al NAS sulle porte previste; permessi della condivisione | entrare nella VPN non rende amministratore del NAS; una condivisione non è una copia di sicurezza | previsto nelle regole fra zone, non ancora provato |
| separare client, IoT, ospiti, servizi e laboratorio | OPNsense, switch e access point con VLAN | porte e reti sullo switch/AP; regole di instradamento sul firewall | due host nella stessa VLAN possono comunicare senza attraversare OPNsense | architettura decisa, messa in opera e prove pendenti |
| filtrare le richieste di nomi della casa | AdGuard Home davanti a Unbound ricorsivo | richiesta DNS e regole che obbligano i client a usare il percorso previsto | il DNS vede il nome richiesto, non il contenuto completo di ogni URL o di ogni connessione | deciso, ADR-007; non sostituito con Gateway |
| consentire a un familiare una sola applicazione web con login | Cloudflare Access e Tunnel | identità e sessione davanti all'applicazione; accesso del connettore alla sola destinazione | non autorizza una rete intera, non configura la separazione fra VLAN e non crea un ingresso di gestione approvato | esperimento facoltativo approvato come indirizzo, servizio non adottato |
| filtrare DNS o web su un portatile fuori casa | possibile Cloudflare Gateway con client e policy dedicate | traffico effettivamente instradato a Gateway; certificato radice se si vuole decifrare HTTPS | il tunnel WireGuard amministrativo, configurato come parziale, non implica questo instradamento generale | esigenza distinta da valutare, nessuna attivazione approvata qui |
| semplificare il collegamento di dispositivi dietro NAT | Tailscale o NetBird come alternative a una VPN gestita direttamente | identità dei nodi, policy dell'overlay e regole sulle destinazioni raggiungibili | la comodità del collegamento non giustifica accesso indiscriminato alle VLAN | alternative studiate, non adottate in aggiunta a WireGuard |
| raccogliere e correlare eventi di sicurezza | Wazuh con eventi di Suricata e apparati | log, eventi degli endpoint e osservazioni della rete | un allarme non è una regola di accesso; la risposta attiva non è implicitamente abilitata | deciso, ADR-028; da implementare e collaudare |
| capire carico, capacità e anomalie operative | Netdata sul server Linux previsto | metriche di host e apparati, soglie e storico effettivamente raccolto | un grafico regolare non dimostra assenza di compromissioni o correttezza delle autorizzazioni | deciso, ADR-036; da mettere in opera nel lab |
| conservare i file e tollerare il guasto di un disco | TrueNAS e specchio dei dati previsto | dischi, pool e condivisioni | lo specchio replica anche cancellazioni o modifiche indesiderate; non è un backup indipendente | NAS in verifica hardware, sistema e pool non installati |
| recuperare dati o configurazioni dopo un incidente | piano di backup con copie distinte e prove di ripristino | archivi conservati, credenziali e percorso di recupero | la presenza di un archivio non dimostra che il ripristino riesca | procedure documentate, prove reali pendenti |

Il criterio è partire dalla domanda e seguire il percorso fino al punto che prende la decisione. Prodotti diversi possono coprire una parte dello stesso bisogno, e un prodotto può offrire più funzioni. Non ne segue che quelle funzioni siano equivalenti o che siano state tutte attivate.

## Tre percorsi concreti

### Un file del NAS attraverso la rete privata

Il dispositivo remoto presenta la propria chiave a WireGuard. Il tunnel rende raggiungibile un percorso; OPNsense applica poi le regole previste per la rete dei peer. La condivisione del NAS applica infine i propri permessi. Sono tre decisioni distinte: ammettere il dispositivo nel tunnel, consentire la connessione alla porta e autorizzare l'operazione sul file.

Il progetto contiene già una regola proposta da WG_RETE verso NAS su PORTE_CONDIVISIONE. Nella rilettura del 23/10 l'alias viene limitato a TCP 445: comprendeva anche 443 per applicazioni NAS che ADR-032 non prevede più. La gestione HTTPS rimane nel perimetro amministrativo separato. Questo non è un risultato di collaudo. La prova futura deve mostrare che il file autorizzato si raggiunge e che destinazioni, porte o operazioni non ammesse restano negate. La gestione amministrativa usa invece il perimetro della VLAN 99 e le credenziali stabilite da ADR-025. I dettagli sono in [Regole fra le zone](08-regole-fra-le-zone.md) e [Accesso amministrativo](09-accesso-amministrativo.md).

### Una piccola applicazione web attraverso Cloudflare

Il familiare apre il nome pubblico dell'applicazione nel browser. Access verifica l'identità e la policy, quindi la richiesta può arrivare attraverso Tunnel al connettore e all'applicazione scelta. L'uscita del connettore deve rimanere limitata alle risorse necessarie: la sua presenza non autorizza ad amministrare firewall, hypervisor o NAS.

Questo caso può evitare un client VPN per l'applicazione web scelta. È un motivo per studiarlo, non un motivo per instradare attraverso Cloudflare tutta la rete domestica. Il percorso approvato come raccomandazione è un eventuale esperimento isolato con un'applicazione non critica. Le interfacce amministrative restano nel disegno WireGuard. Fonti: [applicazioni Access](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/choose-application-type/) e [connettività Cloudflare](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/).

### Una richiesta DNS e la visita a una pagina

Il filtro DNS decide sul nome richiesto. Dopo la risoluzione avviene la connessione al servizio, con protocollo e contenuti propri. Permettere o bloccare un nome non significa avere ispezionato ogni pagina o file di quel dominio. Per controllare contenuti HTTPS servirebbe un altro percorso di ispezione, con il relativo modello di fiducia.

Nel progetto la risposta a questo primo bisogno rimane AdGuard Home con Unbound ricorsivo locale. Gateway è tecnicamente un'alternativa, ma inoltrargli le richieste cambierebbe ADR-007. Per l'ispezione HTTP/HTTPS Cloudflare documenta client, proxy e certificato radice quando si vuole decifrare il traffico: non viene abilitata come conseguenza automatica di Access o di Tunnel. Fonti: [filtro DNS](https://developers.cloudflare.com/cloudflare-one/traffic-controls/get-started/dns/) e [filtro HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-controls/get-started/http/).

## Una misura non sostituisce un'altra

La stessa distinzione vale per il NAS che si sta assemblando. Il 23/10/2026 il BIOS ha mostrato 8192 MB nel solo A2, tre SSD sulle porte previste e SATA Mode Selection su AHCI. Queste letture verificano rilevamento e modalità del controller. Non dimostrano la salute dei dischi o l'esistenza di una copia recuperabile.

Il commutatore SMART Self Test su On è un'impostazione. Una lettura degli attributi SMART e l'esito di un test lungo sono altri riscontri. Anche il confronto della RAM appartiene a un livello diverso: RAM-03/A2 ha circa 22 ore senza fail riferite dall'utente, mentre RAM-04 nello stesso A2 ha mostrato un errore. Il [registro NAS](../02-storage-di-rete-nas/09-registro-del-montaggio.md) conserva valori, origine delle osservazioni e limiti, senza trasformare un singolo esito positivo in una certificazione di ogni componente.

Per il monitoraggio valgono distinzioni analoghe. Wazuh e Suricata rispondono al bisogno di osservare eventi di sicurezza secondo il [piano di monitoraggio](11-monitoraggio-wazuh-suricata.md); Netdata risponde alle domande di capacità e prestazioni del [proprio studio](14-metriche-con-netdata.md). Il [piano di backup e ripristino](../05-strategia-di-backup/02-piano-di-backup-e-ripristino-del-lab.md) risponde alla recuperabilità, che richiede una prova effettiva.

## Come documenteremo gli sviluppi

Ogni fase aggiorna il documento tecnico del componente e il registro di stato pertinente con ciò che è stato deciso, configurato e verificato. Il riscontro indica da dove viene: documento del produttore con data, osservazione di una schermata, dichiarazione dell'utente o prova eseguita. Un valore non letto non viene dedotto dalla sola aspettativa.

Quando emerge una distinzione o una scelta significativa, il [racconto tecnico-didattico](../../../.claude/context/studio-didattico-master.md) aggiunge una voce con il caso iniziale, il motivo della difficoltà, il principio adottato e il rimando al dettaglio. Gli sviluppi successivi aggiungono storia; il documento tecnico conserva lo stato corrente. Non si riscrive il passato per far sembrare già installato ciò che allora era soltanto una proposta.

Per ogni controllo di accesso la prova comprende un caso ammesso e uno negato. Per i servizi di recupero comprende un ripristino. Per le misure riporta il contatore effettivamente acquisito e il suo perimetro. Un eventuale test non eseguito rimane dichiarato come tale.

## Fonti e confini della decisione

Le fonti esterne del confronto sono registrate in SOURCES.md, voci S178-S185, insieme alle fonti OPNsense S33 e S82. La [valutazione Cloudflare](15-cloudflare-zero-trust-e-alternative.md) conserva prezzi, limiti gratuiti e data della verifica senza duplicarli in ogni documento. I vincoli locali provengono da ADR-007, ADR-025, ADR-028, ADR-036 e dalle approvazioni ADR-037 e ADR-038 del 23/10/2026.

L'approvazione riguarda questa separazione dei bisogni e le raccomandazioni: WireGuard per gestione e NAS, DNS locale, fondamenti di rete prioritari e Cloudflare come esperimento applicativo facoltativo. Non autorizza implicitamente un account Cloudflare, un nuovo ingresso amministrativo, un cambio del resolver o l'installazione contemporanea delle alternative.
