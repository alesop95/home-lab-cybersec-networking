# Servizi gratuiti: scelta e collocazione

Ritorno allo [studio](README.md). Per gratuito si intende utilizzabile nel lab senza un canone software obbligatorio per la funzione selezionata. Restano energia, dischi, backup esterno, eventuale dominio e manutenzione. Il [registro](../../../SOURCES.md) distingue documentazione ufficiale, community e offerte commerciali. Questa e' una selezione ragionata per il caso documentato, non una graduatoria universale.

## Criteri

Prima vengono continuita' della rete, ripristino e utilita' quotidiana; poi apprendimento e sperimentazione. Si privilegiano formati esportabili, configurazioni documentabili, progetto mantenuto e assenza di dipendenza necessaria da un piano a pagamento. Ogni nuovo servizio deve avere proprietario operativo, finestra di aggiornamento, backup e una prova di ripristino. I nomi del software non implicano che siano gia' installati.

| Bisogno | Proposta | Alternativa e motivo | Collocazione / priorita' |
|---|---|---|---|
| Firewall, DHCP, DNS | OPNsense gia' installato e [Unbound](https://docs.opnsense.org/manual/unbound.html) | sostituire piattaforma ora disperderebbe lavoro gia' fatto | firewall fisico, P0 |
| DNS filtrante con statistiche | [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome/wiki/Docker) | [Pi-hole](https://github.com/pi-hole/pi-hole) e' un'alternativa libera; scegliere uno solo. Le blocklist Unbound bastano per partire | host sempre acceso da individuare, P1 |
| Disponibilita' dei servizi | [Uptime Kuma](https://github.com/louislam/uptime-kuma) | non serve un'intera piattaforma di metriche per sapere se DNS/HTTPS rispondono | host servizi, P1 |
| CPU, memoria, dischi, container | [Beszel](https://github.com/henrygd/beszel) | utile prima di un sistema di metriche piu' articolato; non sostituisce i test applicativi | host servizi con agenti, P1 |
| Stato e traffico apparati | [LibreNMS](https://docs.librenms.org/) | aggiungerlo se SNMP e storico porte producono valore; non tutti gli AP economici espongono SNMP | host servizi, P2 |
| Backup di file e configurazioni | [restic](https://restic.readthedocs.io/en/stable/) | snapshot NAS utili ma insufficienti come unica copia | client/host verso destinazione separata, P0/P1 |
| Accesso remoto | [WireGuard OPNsense](https://docs.opnsense.org/manual/how-tos/wireguard-client.html) | [NetBird self-hosted](https://docs.netbird.io/selfhosted/selfhosted-quickstart) se servono overlay e gestione peer; aggiunge componenti | firewall, P1 |
| Inventario iniziale | tabella versionata e dettagli privati | [GLPI](https://www.glpi-project.org/en/features/) se servono agenti, asset e gestione IT; [NetBox](https://netboxlabs.com/docs/netbox/) se serve modello rete/IPAM | repository ora, applicazione solo quando utile |
| Assistenza remota | [MeshCentral](https://github.com/Ylianst/MeshCentral) | NovaSCM va valutato per workflow/deploy; non sono sostituti perfetti | VLAN servizi, accesso via VPN, P2 |
| Provisioning e apprendimento | [NovaSCM](https://github.com/ClaudioBecchis/NovaSCM) in pilota | mantenere procedure manuali riproducibili finche' il pilota non passa | VM LAB, P2 |
| SIEM / sicurezza endpoint | [Wazuh](https://documentation.wazuh.com/current/quickstart.html) | partire da log firewall e pochi endpoint, prima di ampliare raccolta | VM dedicata su host adeguato, P3 |
| Rilevamento sulla rete | [Suricata in OPNsense](https://docs.opnsense.org/manual/ips.html) | modalita' di rilevamento prima del blocco, dopo test prestazionali | firewall, P2/P3 |
| Verifica applicazioni | [Trivy](https://trivy.dev/docs/latest/guide/) e [ZAP Baseline](https://www.zaproxy.org/docs/docker/baseline-scan/) | [Strix](https://github.com/usestrix/strix) aggiunge test autonomi e dipendenza da modello | runner LAB, P2 poi P3 |
| Documenti | [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | iniziare da una raccolta piccola, conservando originali ed esportazione | dopo backup, P2 |
| Foto e video | [Immich](https://github.com/immich-app/immich) | non usare la libreria applicativa come unica copia | dopo scelta storage e backup, P2 |
| File fra dispositivi | [Nextcloud](https://github.com/nextcloud/server) se servono davvero sincronizzazione e condivisione | per soli file in LAN valutare le condivisioni del NAS gia' previsto | successivo al NAS, P2 |
| Password | [Vaultwarden](https://github.com/dani-garcia/vaultwarden) come candidato | e' un'implementazione non ufficiale compatibile Bitwarden; adozione solo con recupero e backup collaudati | host sempre disponibile, P3 |

Il catalogo [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) e' utile per trovare alternative e licenze dichiarate. Non e' una verifica di sicurezza o sostenibilita' del singolo progetto. La tabella seleziona funzioni con un bisogno riconoscibile; altri servizi del catalogo non entrano automaticamente nella roadmap.

## Dove farli girare

Il firewall mantiene il proprio compito di rete. Il NAS mantiene il progetto TrueNAS e la finestra di accensione della sessione dedicata: ospitarvi servizi opzionali e' una scelta successiva, ma DNS, autenticazione necessaria alla rete e monitoraggio di continuita' non possono dipendere dal suo spegnimento programmato. Non viene proposto di reinstallare il NAS con un hypervisor differente.

Serve identificare un host di calcolo sempre acceso fra l'hardware disponibile, misurandone il consumo; al momento non e' assegnato. Per pochi container una macchina Linux con Compose e' sufficiente come proposta. [Proxmox VE](https://www.proxmox.com/en/products/proxmox-virtual-environment/pricing) diventa sensato se occorrono VM isolate, snapshot e sistemi diversi; il piano di supporto si distingue dall'uso del software. Il suo impiego resta separato dall'assemblaggio NAS e dal firewall.

| Profilo proposto | Risorse iniziali da riservare | Significato |
|---|---|---|
| DNS + Kuma + metriche leggere | 2 vCPU, 2-4 GiB RAM, 20-40 GB SSD | stima ingegneristica iniziale, da misurare con log e retention |
| Wazuh, 1-25 agenti | 4 vCPU, 8 GiB RAM, 50 GB | raccomandazione ufficiale per 90 giorni di alert indicizzati, S30 |
| Applicazioni documenti/foto | da dimensionare su corpus e indicizzazione | niente stima unica prima di conoscere volume, OCR e foto |
| LAB con VM Windows e runner pentest | da dimensionare sulla VM e sul modello scelto | non sommare implicitamente queste risorse agli 8 GB del firewall |

Per confronto energetico, 10 W continuativi valgono 87,6 kWh/anno, 20 W valgono 175,2 kWh/anno e 40 W valgono 350,4 kWh/anno. Sono calcoli `W / 1000 * 24 * 365`, non misure di un candidato. Il costo si ottiene moltiplicando per la propria tariffa, conservata nel livello privato. Alimentare un vecchio desktop per un solo piccolo servizio puo' costare piu' del software gratuito che ospita.

## Backup e verificabilita'

La prima consegna operativa sara' una copia ripristinabile delle configurazioni OPNsense, switch/AP e dei dati applicativi, piu' un documento che dica come ricreare il servizio. Il mirror protegge da alcuni guasti disco, non da cancellazione, compromissione o perdita dell'intero apparato. La proposta e' una copia separata e almeno una offline o fuori sede; non si presume gratuito lo spazio cloud. Per database si usano dump o procedure applicative coerenti, non si presume valido copiare file aperti.

Uptime Kuma sullo stesso host delle applicazioni aiuta a diagnosticare ma non puo' notificare la morte del proprio host. Si aggiunge una verifica da un secondo dispositivo quando disponibile. Il backup e' riuscito solo dopo un ripristino su destinazione di prova e una verifica di contenuto; un log di upload non chiude quel requisito.

## Tre separazioni necessarie

Il DNS filtrante non e' un firewall applicativo web. [Cloudflare WAF](https://developers.cloudflare.com/waf/) e' un servizio esterno per eventuali siti pubblici; il piano gratuito non equivale a uno stack libero self-hosted. [cheat.sh e CanYouSeeMe](../../fonti/strumenti-da-screenshot.md) sono strumenti di consultazione e diagnostica, non VM da predisporre. Infine [Strix](../../fonti/strix.md) non e' gratis in ogni configurazione: il costo del modello va rilevato nel pilota.
