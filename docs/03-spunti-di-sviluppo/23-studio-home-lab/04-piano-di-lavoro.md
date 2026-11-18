# Piano di lavoro e punto complessivo del progetto

Ritorno allo [studio](README.md). Quadro aggiornato il 18/11/2026: prima si completa la riallocazione hardware, poi si riprende il NAS e si porta in esercizio la rete segmentata. Gli studi successivi restano visibili senza diventare installazioni già eseguite. Il [registro delle pendenze](../../pendenze-aperte.md) mantiene lo stato corrente, mentre il [registro delle decisioni](../../../.claude/memory/decisions.md) conserva il perché.

## Stato realmente documentato

Il Windows quotidiano e Ubuntu Studio sono postazioni in uso. Il proprietario conferma presenza e avvio della Windows Sandbox nativa sul Windows quotidiano: quel riscontro è chiuso su sua dichiarazione; rete, cartelle esposte e modalità d’apertura dei corsi restano da verificare. L’SSD 850 EVO di AnduinOS è ritrovato. La migrazione Windows, il rilascio del BX500, l’aumento RAM e l’assemblaggio del server non risultano eseguiti.

TrueNAS 25.10.7 è installato al banco; tank è un mirror SanDisk 240 GB/WD 250 GB, con 213,19 GiB utilizzabili alla creazione, e tank/documenti è creato, cifrato e non ancora condiviso nell’ultima evidenza. Tre export con seed e la chiave sono conservati e verificati sul client; seconda destinazione indipendente e ripristino restano aperti. Il punto utenti/ACL/share è sospeso per la riallocazione hardware. Il firewall ha un’installazione storica, la rete domestica segmentata e switch/AP non sono attestati in esercizio.

## Allocazione hardware corrente e proposta

| Macchina | Ultimo stato documentato | Destinazione e lavoro residuo |
|---|---|---|
| Windows PC-07 | H97 Anniversary/i7-4790,16 GB DDR3, BX500 1 TB e HDD 500 GB; Windows Sandbox confermata dal proprietario |850 EVO M.2 SATA 250 GB candidato a sistema/programmi con adattatore SATA; HDD resta per corsi; BX500 verso NAS dopo migrazione e avvio verificati; scelta RAM 16/24/32 GB aperta|
| NAS | H170-PRO/i7-6700,8 GB DDR4, Corsair HX520W, V300 240 GB avvio, SanDisk 240/WD 250 mirror |conserva piattaforma; obiettivo 16 GB con altri 8 GB affidabili, BX500 candidato dati con secondo SSD da definire; poi utenti/ACL/share e recupero|
| Server futuro | H270M Pro4/i7-7700,16 GB DDR4 Crucial; P2/P3 NVMe 1 TB assegnati |confermare montaggio e collaudi, installare Proxmox e dimensionare VM/container; non contare 24 GB già disponibili|
| Ubuntu Studio | H170-PRO/i7-6700 dal censimento; fonte audio:16 GB DDR4 e Crucial P2 500 GB | conserva RAM e dischi; ambiente canonico in `diy-2way-monitors-home`, propagato a `home-recording-training-mixing-setup` |
| Scorta NAS | B150-PRO/i7-6700 |ultima descrizione senza RAM/SSD; non una seconda macchina già pronta|
| Seconda Z97-P | i7-4790 e due Corsair 8 GB nel censimento storico |presenza attuale di macchina/moduli da riconfermare; non contarli già trasferiti|
| AnduinOS PC-03 | smembrato; Corsair ValueSelect 2 × 8 GB, Atlantis e850 EVO recuperati |donatore di componenti; laboratorio 32 GB da rivalutare, non ricostruito automaticamente|
| Xubuntu PC-02 | dismesso/smembrato; DDR3 2 × 4 GB+2 × 2 GB, Tecnoware e GeForce 210 recuperati; V300 già NAS |HDD 500 GB distinto da quello Windows; DVD non confermato; scorte non collaudate dove dichiarato|
| Firewall dedicato | i3 settima generazione,8 GB RAM, SSD 120 GB, integrata1 GbE e due TX201 2,5 GbE |resta dedicato a OPNsense; versione, configurazione e corrispondenza porte da leggere alla console|

I 24 GB DDR4 utili censiti sono 8 GB NAS+16 GB server: l’obiettivo 16+16 ne richiede altri 8. Le DDR3 recuperate non risolvono quel fabbisogno. Per Windows 24 GB bastano Corsair 2 × 8 GB e Kingston 2 × 4 GB, liberando due 4 GB;32 GB dipende da altri due 8 GB da riconfermare. Sono alternative da collaudare e scegliere, non trasferimenti effettuati. Gli alimentatori recuperati rimangono scorte senza prova elettrica; HX520W non viene sostituito per questa ricognizione.

Il report15/11 misura 140,49 GiB su C: e275,28 GiB su G:. Il sistema può essere candidato all’850 EVO 250 GB, mentre G: resta sull’HDD dei corsi. Per liberare il BX500 non serve trasferire G: sul NAS. La capacità 213,19 GiB del NAS attuale resta invece insufficiente per una copia integrale di G:. Specifiche, revisioni e copie delle fonti sono nella [scheda dischi](../02-storage-di-rete-nas/14-dischi-windows-dati-e-fonti-hardware.md); stato fisico nella [ricognizione](../02-storage-di-rete-nas/13-ricognizione-hardware-novembre-2026.md) e nell’[allocazione canonica](12-allocazione-dell-hardware.md).

### Raccordo con i progetti audio,18/11/2026

Il proprietario conferma che questa è la postazione condivisa dai progetti `diy-2way-monitors-home` e `home-recording-training-mixing-setup`. La fonte canonica dell'ambiente è `docs/10-ambiente/` nel primo progetto; il secondo riceve quel blocco attraverso `python tools/sync-ambiente.py`, eseguito dal primo. Non si corregge separatamente la copia a valle. Il controllo `--check` del18/11 ha trovato20 file allineati, zero da propagare e zero orfani.

La fonte audio descrive16 GB DDR4 e un Crucial P2 da500 GB. Quel disco resta alla postazione musicale ed è distinto dal P2 da1 TB previsto per Proxmox. Salute SMART e versioni software riportate dalla fonte hanno le proprie date: la lettura del documento non è una nuova misura della macchina. Ogni proposta di prelievo di RAM, dischi, interfacce o cambio di rete va coordinata con il progetto canonico. SoundCraft rimane PA-034 nel progetto DIY e PA-003 nel progetto home recording; ruolo e necessità del fork sono ancora da decidere.

Al momento della consegna la memoria audio documenta preparazione Ubuntu, backup locale e collaudo DSP su file. Sono lavori di quella sessione, non avanzamenti hardware del lab. Richiesta di coordinamento consegnata alla sua cassetta; risposta non ancora acquisita. I file audio in lavorazione restano nella loro sede.

## Topologia prevista della rete

```text
Fibra -> ONT -> Fastweb Seven -> WAN OPNsense
                  |                  |
                  |              LAN trunk 2,5 GbE
                  |                  |
                  |          Zyxel XMG1915-10EP
                  |             |           |
                  |          AP piano 3   AP piano 2
                  |             +-- SSID CASA / IOT / OSPITI
                  |             +-- client, NAS e server sulle VLAN previste
                  |
                  +-- PS5 su LAN1 GbE, fuori dal perimetro per scelta
                  +-- Wi-Fi Seven, upstream e da decidere dopo collaudo AP

OPNsense, terza interfaccia -> DMZ fisica separata, da usare quando servirà un servizio
```

Questa è la destinazione di progetto, non il cablaggio domestico già collaudato. La baseline mantiene Seven e doppio NAT, senza riaprire il collegamento diretto OPNsense-ONT. Routing, DHCP e regole fra zone restano su OPNsense; lo switch trasporta VLAN. Due AP NWA130BE e switch10EP sono scelti; i cavi ai piani 3 e 2 sono già posati. Restano acquisto, configurazione e collaudi. Non riproporre10E più iniettori come scelta corrente.

| Rete prevista | Ruolo | Verifica ancora necessaria |
|---|---|---|
| VLAN 10,192.168.10.0/24 |client fidati, SSID CASA|censimento e flussi autorizzati|
| DMZ fisica,192.168.20.0/24 |eventuali servizi esposti|servizio concreto prima di assegnare host o aprire porte|
| VLAN 30,192.168.30.0/24 |servizi e NAS|separazione accesso dati e amministrazione|
| VLAN 40,192.168.40.0/24 |IoT e supporto incerto, SSID IOT|rifiuto verso NAS/gestione e soli endpoint necessari|
| VLAN 50,192.168.50.0/24 |ospiti, SSID OSPITI|solo Internet e nessun accesso interno|
| VLAN 60,192.168.60.0/24 |laboratorio e bersagli autorizzati|host da riallocare e isolamento da provare|
| VLAN 99,192.168.99.0/24 |gestione|accesso limitato e recupero locale|

La Windows Sandbox del PC quotidiano e la futura VLAN 60 rispondono a confini diversi; l’avvio della funzione non prova l’intero disegno del laboratorio. Fonti di progetto: [architettura](01-architettura.md), [regole](08-regole-fra-le-zone.md), [accesso amministrativo](09-accesso-amministrativo.md) e [topologia tecnica](../../../.claude/context/diagrams/topologia-di-rete.md).

## Ordine di lavoro raccomandato

| Ordine | Blocco | Risultato che permette di avanzare |
|---|---|---|
|1|chiudere l’allocazione hardware|collegamento850 EVO pronto, dati conservati, migrazione con avvio indipendente, scelta RAM e pezzi realmente disponibili|
|2|completare NAS e recuperabilità|stato reale riletto, utente/ACL/share verificati; copia separata e almeno un recupero; crescita dischi come intervento distinto|
|3|preparare firewall e dati della linea|configurazione salvata, software mantenuto verificato, NIC mappate, una postazione di prova funzionante e ritorno al cablaggio iniziale|
|4|acquistare/configurare switch e AP|VLAN, SSID, gestione, copertura e prove positive/negative; poi migrazione client e richiesta disattivazione Booster|
|5|mettere in servizio il calcolo e i servizi essenziali|Proxmox collaudato, DNS indipendente dal NAS a orario, backup e risorse misurate|
|6|osservabilità e accesso remoto|Wazuh/Suricata, Netdata, WireGuard/Tailscale secondo perimetro, con prove funzionali e di rifiuto|
|7|prototipi e servizi aggiuntivi|app familiari, inventario/RMM, LAB/LLM, Hermes/brain e MCU solo con bisogno, risorse e recupero definiti|

È un ordine di dipendenze, senza date inventate. Sopralluogo rete, preventivo, censimento e studio possono procedere mentre si lavora al banco. Le macchine non vengono spente o smontate per effetto del piano; commit, push e deploy restano manuali.

## Registro operativo consolidato

Ogni riga mantiene qui lo stato; i documenti collegati dal piano e dal registro pendenze conservano i dettagli. Le righe raggruppano le voci storiche, senza trattare come aperti l’SSD ritrovato, l’avvio Sandbox confermato, il dataset creato o gli export già acquisiti.

| ID | Filone | Stato corrente | Lavoro che resta |
|---|---|---|---|
| P01 | Windows: SSD e continuità | aperta, prima priorità | riscontrare adattatore M.2 SATA 2280 verso SATA, salute e contenuto 850 EVO; conservare sistema e dati; preparare riduzione/copia partizioni e avvio con BX500 scollegato |
| P02 | Windows: RAM | scelta aperta | 16 GB attuali;24 GB con Corsair 2 × 8 GB recuperati e Kingston 2 × 4 GB;32 GB solo con altri due 8 GB riconfermati e collaudo; nessuno spostamento già eseguito |
| P03 | NAS: memoria affidabile | aperta | 8 GB DDR4 attuali, obiettivo 16 GB; mancano 8 GB utilizzabili senza prelevare implicitamente i16 GB del server; tre moduli con errori esclusi |
| P04 | NAS: crescita storage | aperta, dopo P01 | BX500 1 TB candidato dopo rilascio da Windows; secondo SSD adeguato ancora da definire; un solo1 TB non espande a1 TB il mirror240/250 GB |
| P05 | Server Proxmox | da assemblare/confermare | H270M Pro4/i7-7700,16 GB DDR4 e P2/P3 NVMe 1 TB assegnati; verificare montaggio, entrambi i dischi, collaudo, consumi e installazione |
| P06 | NAS: utente, ACL e share | sospesa per hardware | tank/documenti già creato, cifrato, Unlocked; SMB/NFSv4 e Restricted già letti; ultimo Save, utente e share non attestati; rileggere il punto reale prima di proseguire |
| P07 | Backup e recupero | aperta, trasversale | copia indipendente di chiave e tre export con seed; recupero/sblocco da provare; copie dati NAS/server/endpoint e corsi; restic/Veeam e confronto PBS da collaudare, non solo archiviare file |
| P08 | NAS: integrazione domestica | aperta | indirizzo finale, DNS/gateway, NTP osservato, gestione, eventuali restrizioni GUI e2FA NAS con recupero; log e allarmi dopo esistenza del ricevitore |
| P09 | Identità e notifiche NAS | parzialmente chiusa | Google2FA e invii test ricevuti già confermati; restano filtro Log NAS, recupero account/codici rinviati, controlli periodici e copie delle configurazioni aggiornate |
| P10 | Firewall OPNsense | da eseguire alla console | leggere versione e configurazione, esportare, preparare release mantenuta e patch correnti, mappare3NIC, assegnare WAN/LAN/DMZ, DHCP/DNS/regole e recupero; non fissare la release letta a ottobre |
| P11 | Seven e linea | verifiche locali aperte | schermate con GPON attiva, IP sul collegamento di riserva, pagine LAN e altre mancanti, risposta pingWAN; fibra riparata e IP statico su fibra già confermati |
| P12 | Switch e due AP | scelti, acquisto non attestato | XMG1915-10EP e2 NWA130BE: ricevere/confrontare preventivo, budget porte e PoE, supporti e firmware; eventuali moduli SFP rame da verificare solo se necessari |
| P13 | VLAN, regole e gestione | progetto da applicare | 10/30/40/50/60/99, DMZ fisica separata; trunk/access e SSID; DHCP/DNS, autorizzazioni e rifiuti, IPv6 se attivo, percorso di recupero locale |
| P14 | Wi-Fi e Booster | dopo P12/P13 | AP ai piani 3 e 2, cavi già posati; misurare copertura/roaming e piano terra; decidere radio Seven; disattivare opzione Booster solo dopo collaudo e chiarire restituzione con operatore |
| P15 | Censimento client e tablet | aperta | connettività, porta/SSID/VLAN, aggiornamenti e capacità; TAB-02 Android/patch e TAB-01 modello/edizione da leggere; piani 4 e due cavi AP già noti, non richiederli ancora |
| P16 | DNS domestico | decisione adottata, implementazione aperta | AdGuard Home con Unbound ricorsivo; host disponibile quando serve e ripiego provato; NAS spento non deve fermare la risoluzione della casa |
| P17 | Accessi remoti | progetto da applicare | WireGuard per gestione/file secondo policy; Tailscale richiesto per assistente/servizi selezionati; identità e rotte da collaudare; NordVPN/Meshnet condivisa fuori dalla gestione domestica |
| P18 | Wazuh e Suricata | adottati, da mettere in opera | VM Wazuh sul server, sorgenti e agenti, Suricata inizialmente in rilevazione su OPNsense; alert di prova, risorse e impatto sul traffico misurati prima del blocco |
| P19 | Netdata | adozione chiusa, verifiche aperte | parent Linux; plugin OPNsense o SNMP, profili Zyxel, RAM/disco dopo raccolta e sovrapposizione allarmi con Wazuh |
| P20 | Protezione endpoint | studio e scelte aperti | perimetro Windows/Linux/Android; Defender in audit come primo confronto, configurazioni e recupero da verificare; non dedurre copertura da licenze o nomi dei prodotti |
| P21 | LAB, pentest e modello locale | da rivalutare con hardware | VLAN 60 e bersagli autorizzati; PC-03 smembrato, quindi nodo32 GB non già disponibile; AVX2, prestazioni CPU/token e consumo da misurare; GPU studio futuro, nessun acquisto |
| P22 | Inventario e gestione software | piloti, non servizi attivi | NovaSCM/MeshCentral e possibili GLPI/NetBox secondo bisogno; enrollment, permessi, distribuzione e recupero in ambiente di prova; Strix/Trivy/ZAP solo nel perimetro autorizzato |
| P23 | Applicazioni self-hosted | candidati da scegliere | Paperless-ngx, Immich, Nextcloud, Vaultwarden e servizi analoghi dopo bisogni, capacità e backup; Kuma opzionale per disponibilità, senza duplicare Netdata/Wazuh |
| P24 | Assistente personale e brain | direzione adottata, prototipo aperto | Hermes, Nix/NixOS, archivio Markdown/Obsidian, Telegram e Tailscale; compito/corpus/provider/costi e recupero; prototipo prima di scegliere hardware; Jev solo alla tappa brain concordata |
| P25 | Microcontrollori e piccoli nodi | studio aperto | ESP32/Arduino/PicoW, esercizi browser e primo flusso sensore-servizio; Wi-Fi verso VLAN 40 o30 secondo ruolo; consumi alla presa e isolamento reali da misurare, nessuna schedina assegnata |
| P26 | Governo sicurezza e privacy | pratica richiesta, attuazione aperta | skill ISO27001/GDPR presenti; registro beni/rischi/accessi/dati e prove di recupero; verifiche normative al caso concreto, nessuna certificazione o conformità dedotta dalle skill |
| P27 | Energia, disponibilità e UPS | dimensionamento aperto | misurare NAS/server/nodi, fissare finestre e dipendenze; scegliere UPS su carichi e autonomia; NIC NAS 2,5 GbE eventuale, non prerequisito per iniziare |
| P28 | Ubuntu Studio, SoundCraft e audio | sedi e cascata riscontrate; riscontro della sessione audio atteso | ambiente canonico in `diy-2way-monitors-home`, poi `home-recording-training-mixing-setup`; SoundCraft PA-034 e PA-003; qui registrare dipendenze hardware/rete e installazioni confermate |
| P29 | Documentazione e schede | manutenzione aperta | 19 schede superate rispetto alle ancore su 20,0 difetti strutturali; revisione per contenuto, prosa/typografia e segnaposto storici; documentare rete realizzata a ogni tappa |
| P30 | Template, pacchetti e fonti | parzialmente verificato | 18 skill presenti, wrapper allineati; ultima ricevuta senza conflitti; registro adozioni incompleto; Hermes/knowledge-wiki catalogati ma non istanziati qui; report sicurezza assente, letture/fonti storiche da distinguere dalle consultate |
| P31 | Residui di studio non bloccanti | rinviati o condizionali | modem libero/SIP e alternative firewall solo se si riapre il vincolo di linea; compatibilità audioUSB NAS, DVDPC-02 non confermato, ruoli residui seconda Z97-P; nessuna assegnazione dedotta |

## Skill e capacità già recepite

Ricognizione locale:18 file canonici SKILL.md sotto .claude/skills e controllo degli adattatori Codex positivo. La tabella descrive capacità disponibili agli agenti, non software installato nei dispositivi del lab.

| Gruppo | Skill canoniche presenti | Stato e uso |
|---|---|---|
| Ripresa e stato | riprendi, repo-status, sync-context, git-sync | presenti; verifica wrapper positiva |
| Avvio progetto | onboard, init-project-system | presenti; nessun nuovo bootstrap richiesto |
| Pacchetti del template | cerca-pacchetto, gate-pacchetti | presenti; non attivano da soli tutto il catalogo |
| Prove e memoria didattica | prove-che-misurano, retrospettiva, studio-didattico | presenti; pratica didattica adottata con ADR-038 |
| Identità e alberi Git | identita-git, alberi-di-lavoro | presenti; un solo worktree osservato |
| Fonti e documenti | fonti-non-recuperabili, craft-apps | presenti; applicazioni Craft da distinguere per macchina |
| Sicurezza e privacy | iso27001, gdpr-compliance | adottate con ADR-048; attuazione dei controlli ancora progressiva |
| Ambienti di prova | separazione-ambienti | presente; nessuna nuova infrastruttura attivata da questo riepilogo |

Le due skill di dominio sono state recepite per lo studio20 e ADR-048. Consentono lavoro di audit, documentazione e valutazione quando pertinente; non attestano controlli già realizzati o conformità. Il [registro pacchetti](../../../.claude/pacchetti.json) contiene una sola adozione formale, anonymization: non è un inventario completo di tutto ciò che è già istanziato. Va riconciliato sulle evidenze, non riempito deducendo installazioni dalla presenza dei modelli.

Hermes-agent e knowledge-wiki esistono nel catalogo del template e non risultano istanziati qui. L’assistente e il brain sono uno studio richiesto, con compito, provider, permessi, costi, hardware e recupero ancora da provare. La presenza della voce nel catalogo non chiude la tappa del futuro brain: l’identificazione di Jev rimane legata alla consegna concordata, non è da richiedere automaticamente oggi. I plugin dell’account e il design system sono capacità della sessione; non vanno sommati alle installazioni dei server. Nessun nuovo pacchetto è stato installato per questo punto.

## Studi da tenere visibili

La [matrice bisogni/controlli](16-bisogni-controlli-e-flussi.md) rimane il criterio per scegliere strumenti. Wazuh/Suricata e Netdata sono decisioni adottate da implementare; Cloudflare Access/Tunnel/Gateway, applicazioni familiari e inventario avanzato conservano lo stato di esperimenti o candidati. L’accesso amministrativo WireGuard e Tailscale per assistente/servizi hanno perimetri distinti. Non si attivano tutti i prodotti del [catalogo servizi](02-servizi-gratuiti.md).

Il [modello locale su CPU](13-modello-linguistico-locale-su-cpu.md) aspetta un host reale dopo lo smembramento del vecchio laboratorio; GPU rinviata. L’[assistente personale](17-assistente-personale-hermes-nix-e-memoria.md) e i [piccoli nodi](19-microcontrollori-microserver-e-laboratorio-browser.md) richiedono prototipi e misure prima degli acquisti. [Sicurezza e privacy](20-governo-sicurezza-e-privacy-domestiche.md), [aggiornamento firewall](21-aggiornamento-e-vulnerabilita-opnsense.md) e [protezione endpoint](../07-further-protection/03-studio-protezione-endpoint-2026.md) accompagnano la messa in esercizio; versioni, avvisi e prezzi vanno ricontrollati al momento dell’intervento, senza trattare i numeri di ottobre come attuali.

## Che cosa è chiuso e che cosa non si ripete

SSD 850 EVO ritrovato; materiale dei corsi identificato e mantenuto sull’HDD Windows; Windows Sandbox presente e avviabile confermata dal proprietario. Foto e fonti hardware sono conservate con impronte e revisioni. PC-02/PC-03 sono smembrati, non laboratori già pronti. Tre moduli RAM con errori restano fuori dalle assegnazioni affidabili. Non si riaprono le esclusioni definitive del magazzino.

TrueNAS, tank e documenti sono già creati; chiave e tre export sono acquisiti. Non si ricrea pool/dataset, non si riscaricano archivi identici per una ripresa e non si ripetono OAuth o Memtest senza un motivo nuovo. Questo non chiude utenti/share, copia indipendente, sblocco o ripristino. Il nuovo riepilogo non avvia il precedente mandato autonomo documentato come blocked.

---

## Piano storico del22/09/2026

La stesura seguente conserva la sequenza originaria. Dove diverge da scelte e osservazioni successive vale il quadro corrente sopra; il registro decisioni e le schede tecniche mantengono la storia.

Ritorno allo [studio](README.md). Questo piano riguarda la rete e i servizi; la guida NAS nella sessione parallela resta autorità sull'assemblaggio. Nessun passo fisico è marcato eseguito perché ne è stata scritta la procedura.

| Fase | Attività | Prerequisito | Evidenza per chiuderla |
|---|---|---|---|
| 0 | consolidare fonti e inventario documentale | documenti locali e fonti dell'utente | registro con tutti i sei riferimenti iniziali e censimento controllato; tabella dispositivi con lacune esplicite |
| 1 | sopralluogo rete e conteggio porte | disponibilità locale | elenco prese, piani, stanze, client cablati simultanei, posizione AP e budget |
| 2 | identificare NIC firewall, backup e aggiornamento | console e accesso locale | corrispondenza porte fisiche, versione e config salvata; una postazione di prova naviga senza spostare tutta la casa |
| 3 | scegliere e acquistare switch/AP | fase 1 e confronto modelli | preventivo EU completo, PoE e porte sufficienti, firmware/supporto verificati |
| 4 | configurare switch e primo AP | firewall e apparati | VLAN di gestione accessibile, SSID su subnet corretta, blocchi inter-VLAN provati, recupero locale possibile |
| 5 | estendere Wi-Fi e migrare client | fase 4 | misure copertura e roaming, scelta motivata del terzo AP, stato del Wi-Fi modem dichiarato |
| 6 | host sempre acceso, DNS opzionale e monitor | hardware e consumi misurati | rete funzionante con NAS spento; backup e ritorno a Unbound provati |
| 7 | integrare NAS e backup | collaudo NAS concluso dall'altra sessione | NIC/servizi/finestra di accensione confermati, un ripristino completato |
| 8 | pilota inventario e NovaSCM | VM LAB isolata | enrollment, raccolta, workflow controllato e ripristino documentati |
| 9 | Wazuh/Suricata e pentest | risorse, log e LAB disponibili | alert atteso riprodotto, prestazioni misurate, finding confermati e ritestati |

La fase 0 è documentale. L'inventario fisico e la scelta definitiva di quanti AP acquistare restano aperti finché non si dispone dei dati della fase 1. Questo non impedisce lo studio degli scenari di spesa e della configurazione.

## Informazioni da rilevare senza duplicare il lavoro NAS

Per la casa servono numero di piani e aree, materiali dei muri/solai, punti Ethernet e prese di alimentazione, eventuali aree esterne, client che devono lavorare cablati insieme e budget apparati/posa. La mappa dell'abitazione e gli identificativi reali restano nel livello privato. Per ogni dispositivo già citato si confermano presenza, uso, connettività, supporto aggiornamenti e dipendenza da discovery locale.

Dalla sessione NAS basta ricevere un riepilogo anonimizzato del sistema finale: modello/NIC e velocità, servizi previsti, finestre di disponibilità, interfaccia di gestione, backup e collaudi conclusi. Non si ricensisce il lotto donatore e non si cambia la configurazione di storage per rendere più comodo questo piano.

## Decisioni proposte, non ancora eseguite

Il firewall resta fisico, con routing fra zone su OPNsense. Lo switch principale è candidato 10EP; gli AP sono due cablati con possibile terzo dopo misure. La variante 130BE favorisce funzioni di laboratorio, la 50BE Pro riduce il costo. Il DNS iniziale resta Unbound; AdGuard entra dopo individuazione dell'host sempre acceso. Il primo inventario è documentale, NovaSCM e Strix sono piloti isolati. Le scelte potranno essere promosse a decisioni adottate nel registro ADR dopo riscontro dell'utente e collaudo pertinente, senza dichiarare già acquistato o funzionante ciò che è proposto.

## Collaudo minimo prima della migrazione completa

Si documentano almeno una prova positiva e una negativa per ogni zona: client autorizzato raggiunge il servizio, ospite non raggiunge NAS o gestione. Si include IPv6 se attivo. Si prova la perdita di DNS, riavvio AP/switch, accesso console firewall e ripristino di una configurazione. Si misura trasferimento locale verso un host cablato per separare prestazioni Wi-Fi da velocità Internet. Per WireGuard si usa una rete esterna e si verifica accesso solo ai servizi autorizzati.

Ogni prova registra atteso, osservato, data, versione e riferimento alle evidenze private, con una sintesi anonimizzata nel repository. Un test non svolto resta `da eseguire`; il documento di architettura non può essere usato come verbale.

## Continuità fra sessioni

Il punto di ingresso di questo filone è questo indice di studio, collegato dalla home. Il registro delle fonti è [SOURCES.md](../../../SOURCES.md); dopo nuovi link si esegue `python tools/source-register.py` e poi `python tools/source-register.py --check`. I file di avanzamento NAS non vengono riscritti per rappresentare questo filone parallelo. Commit, push e deploy restano manuali dell'utente.
