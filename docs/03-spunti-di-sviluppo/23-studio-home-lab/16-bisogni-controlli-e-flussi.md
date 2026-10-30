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
| navigare a casa rispettando i controlli e le identità del lab | NordVPN spenta; Meshnet esclusa con account condiviso, ADR-046 | endpoint, resolver effettivo e permessi degli overlay | il firewall vede il tunnel esterno ma non automaticamente i flussi interni; account condiviso fuori dalla gestione | scelta recepita dal rapporto, attuazione da verificare, studio18 |
| collegarsi da fuori casa a servizi e assistente | Tailscale come direzione richiesta dal29/10, ADR-045; peer diretto o subnet router secondo bisogno | identità, policy overlay, rotte e regole verso destinazioni selezionate | raggiungere il nodo non autorizza Hermes ad amministrare la rete; nessun exit node implicito | studio17 avviato, nulla installato; supera Tailscale come sola alternativa, NetBird non adottato |
| raccogliere e correlare eventi di sicurezza | Wazuh con eventi di Suricata e apparati | log, eventi degli endpoint e osservazioni della rete | un allarme non è una regola di accesso; la risposta attiva non è implicitamente abilitata | deciso, ADR-028; da implementare e collaudare |
| capire carico, capacità e anomalie operative | Netdata sul server Linux previsto | metriche di host e apparati, soglie e storico effettivamente raccolto | un grafico regolare non dimostra assenza di compromissioni o correttezza delle autorizzazioni | deciso, ADR-036; da mettere in opera nel lab |
| conservare i file e tollerare il guasto di un disco | TrueNAS e specchio dati tank creato | dischi, pool e condivisioni | lo specchio replica anche cancellazioni o modifiche indesiderate; non è un backup indipendente | TrueNAS25.10.7 installato; primo boot, lease DHCP e login web verificati su LAN temporanea, tank creato28/10,1xMIRROR2wide, Online no errors,213.19GiB utilizzabili; MIRROR e membri sda/sdc letti ONLINE con ZFS Errors No errors; export post-pool con seed ora acquisito e verificato; dataset/condivisioni e recuperi ancora aperti |
| conservare documenti e copie con integrità e versioni recuperabili | TrueNAS25.10.7 e pool tank SanDisk/WD in specchio; OMV con ZFS resta alternativa tecnica | pool, copie valide per correzione, snapshot conservate e backup su destinazione distinta | mirror e snapshot locali non sostituiscono backup; proprietà ZFS disponibili anche in OMV, preferenza TrueNAS per integrazione | ADR-026 riletto con ADR-033/039; installato e tank creato Online no errors; snapshot, backup e recuperi non ancora realizzati; [confronto](../02-storage-di-rete-nas/08-valutazione-openmediavault.md), S74,S204,S231-S236 |
| proteggere i contenuti senza legare tutti i dati a un unico materiale di sblocco | eventuali dataset ZFS cifrati con custodia esterna dei materiali di recupero | singolo dataset e verifica del recupero dopo sblocco | specchio e backup della configurazione non sostituiscono custodia delle passphrase e copie dei file | raccomandazione S240; pool tank creato dopo wizard con Encryption None, nessun dataset cifrato ancora creato; scelta dei dataset prima dei primi dati reali; [procedura](../05-strategia-di-backup/10-configurazione-truenas-e-cambio-hardware.md) |
| conservare le personalizzazioni cambiando hardware NAS | export nativo con Password Secret Seed e copie versionate esterne | acquisizione della configurazione dopo le tappe e verifica del file copiato, poi ripristino su installazione compatibile | impostazioni distinte dai contenuti dataset e dai materiali esterni; riscontri Veeam Linux non qualificano automaticamente TrueNAS | ADR-043, primo export con seed acquisito e verificato fuori NAS; export post-tank con seed ora acquisito e verificato; prima generazione conservata, seconda copia indipendente e restore aperti; [procedura](../05-strategia-di-backup/10-configurazione-truenas-e-cambio-hardware.md), S137/S158/S237/S238 |
| ricevere avvisi e rapporti di salute del NAS | Gmail OAuth salvato, mittente `<email-servizi-casa>` e nome `<nome-mittente-nas>`; Proton `<email-destinatario-nas>` nel profilo amministratore; Google2FA attiva | generazione NAS, invio provider e ricezione Proton ora osservati sulla mail di test | messaggio di test distinto da servizio alert e filtro Log NAS; recapito distinto dal backup configurazione | prima consegna NAS verificata; E-Mail Enabled/Warning e override vuoto, Send Test Alert inviato e ricevuto su Proton, S239; filtro ancora aperto; primo export con seed acquisito ADR-043, successivi checkpoint da aggiornare; S214-S216 |
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

## Applicazione alle impostazioni avanzate del NAS

La [guida al banco e nella rete domestica](../02-storage-di-rete-nas/10-configurazione-al-banco-e-in-rete-domestica.md) collega i pannelli TrueNAS ai bisogni e al momento della loro configurazione. IP, VLAN, DNS e restrizione degli accessi richiedono il piano finale; syslog richiede un ricevitore disponibile; dataset e permessi si preparano sul NAS; debug, script e parametri kernel restano senza personalizzazioni finché manca un bisogno concreto. Le impostazioni lette non sono modifiche già eseguite. La2FA TrueNAS Disabled e quella Google attiva appartengono a due accessi diversi. Fonti S241/S242, riscontri del28/10, raccordo29/10.

## Crescita dello storage e della macchina

ADR-044,29/10/2026: il bisogno è conservare servizi e dati mentre crescono SSD e RAM. I nomi e i permessi seguono ruoli logici; quote, conservazione e risorse si ridimensionano con il carico reale. La [guida NAS11](../02-storage-di-rete-nas/11-crescita-del-nas-e-indipendenza-dall-hardware.md) distingue aumento dello stesso mirror, memoria compatibile e cambio completo della macchina con ADR-043. Nessuna espansione o sostituzione è ancora eseguita. Fonti S243-S246, lettura Datasets e requisito esplicito registrati; ogni futuro upgrade richiede i suoi riscontri di capacità, accesso e recupero.

## Assistente personale e memoria consultabile

ADR-045 e [studio17](17-assistente-personale-hermes-nix-e-memoria.md),29/10/2026: raggruppati Hermes, Nix/NixOS, Tailscale, hardware a consumo misurato e brain personale Markdown/Obsidian da recepire dal template. Richiesta dell’utente acquisita; modello Opus5.5 verificato come esistente, compatibilità e provider non collaudati. Nessuna installazione, rotta o hardware assegnato. La precedente frase sulle sole alternative conserva il significato storico del23/10, ma non esclude il nuovo percorso Tailscale. Jev va identificato chiedendolo all’utente quando il template avrà recepito la capacità; non adesso. Il dataset tank/documenti è creato, cifrato e Unlocked; chiave JSON e tre export con seed acquisiti e verificati. Il modulo identificato conferma SMB/NFSv4 e Restricted; Save finale, utente e share non osservati, guida NAS12.

## Rapporto VPN condivisa,29/10/2026

ADR-046 e [studio18](18-nordvpn-account-condiviso-e-confini-domestici.md) distinguono uscita NordVPN, rete Meshnet condivisa e accesso privato a casa. La scelta Tailscale di ADR-045 è conservata; niente modifiche a DNS o ingressi di gestione dal solo rapporto. Android, permessi Meshnet e rischio dei dati nel monitor sono raccordati alle fonti primarie S262-S268. Nessun accesso a account o dati di fughe altrui eseguito. Il pannello senza nome con POSIX/Discard non è stato attribuito al figlio. La successiva lettura identificata di tank/documenti conferma SMB/NFSv4 e Restricted: verifica di identità e modalità conclusa, nessun setting da cambiare.

## MCU, host Linux e governo dei rischi

ADR-047/048 e studi19/20/21: preferenza Wi-Fi sui nodi piccoli, SSID associati alle VLAN per ruolo, MCU IoT distinta dall’host Linux Hermes e inferenza remota. Consumo alla presa e disponibilità da misurare, nessun Pico audio contato come disponibile. ISO27001 come metodo proporzionato e applicabilità GDPR per trattamento reale; OPNsense alla Production mantenuta prima dell’attivazione, con hotfix verificato sulla macchina. Documentazione e fonti presenti, nessuna installazione o prova fisica attribuite allo studio.
