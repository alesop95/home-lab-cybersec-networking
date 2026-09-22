# Registro unico delle fonti dell'home lab

Dal 22/09/2026 questo e' il punto di ingresso canonico per le fonti di rete, servizi, dispositivi e NAS. Il metodo riprende il progetto retrogame: registro unico, note di lettura collegate, distinzione fra fonte individuata e fonte letta, contenuto grezzo privato e sintesi versionata. Le schede storiche conservano le citazioni e il contesto; nessun riferimento viene cancellato durante il censimento.

La [mappa delle fonti](docs/fonti/index-fonti.md) collega le note allo [studio dell'home lab](docs/03-spunti-di-sviluppo/23-studio-home-lab/README.md). Il [registro storico](docs/fonti-web-consultate.md) conserva le motivazioni del lavoro NAS: la sessione parallela ne resta responsabile. Il [catalogo dei materiali](docs/fonti-e-materiali.md) descrive gli originali locali. Non si importano credenziali, nomi macchina, seriali o indirizzi reali da materiale privato.

## Metodo e confini

Una specifica si verifica sul produttore o sul progetto software; un resoconto di community documenta l'esperienza di chi lo scrive, non una garanzia generale; un rivenditore documenta un prezzo datato, non prevale sul manuale. Anche una risposta nel forum ufficiale va distinta fra personale del produttore, utente e assistente virtuale. Le affermazioni promozionali restano dichiarazioni del progetto finche' non collaudate. Un modello disponibile oggi non prova che lo sia nella regione italiana o che abbia ancora una durata di supporto adeguata.

Ogni voce curata dichiara URL, tipo, stato della lettura, data e uso. Le note spiegano applicazione, limiti e relazioni. Gli screenshot restano locali, ma nome, contenuto utile e derivazione delle fonti sono registrati. Le copie integrali di terzi, se necessarie, stanno in `_notes/fonti/`; nel repository entrano sintesi e attribuzioni. Una lettura riuscita non significa software installato o apparato acquistato.

`python tools/source-register.py` censisce gli URL esatti nei Markdown pubblici di progetto e nel diario di scoperta, conserva la provenienza e mantiene anche le voci non piu' citate. `python tools/source-register.py --check` segnala riferimenti non registrati, senza modificare file. Il controllo non certifica che una pagina sia stata letta, non percorre Internet, non legge `_notes/` e non sostituisce la verifica dei contenuti. Le fonti nei binari, nelle immagini e nei segnalibri privati richiedono una scheda esplicita. Le righe curate si modificano a mano, il solo blocco di censimento e' derivato. Nessun ID viene rinumerato.

## Fonti consegnate dall'utente il 22/09/2026

| ID | Fonte e URL | Tipo e lettura | Uso e destinazione |
|---|---|---|---|
| U01 | `screenshot_149.png`; https://www.cloudflare.com/vi-vn/application-services/products/waf/ | immagine letta il 22/09; URL trascritto, pagina commerciale da confrontare con documentazione | Cloudflare WAF; [nota](docs/fonti/strumenti-da-screenshot.md). Lo screenshot non identifica con certezza il sito aggregatore circostante |
| U02 | `screenshot_150.png`; https://cheat.sh/ | immagine letta il 22/09; repository consultato | consultazione comandi; [nota](docs/fonti/strumenti-da-screenshot.md) |
| U03 | `screenshot_151.png`; https://canyouseeme.org/ | immagine e pagina lette il 22/09 | controllo esterno porte; [nota](docs/fonti/strumenti-da-screenshot.md) |
| U04 | https://www.raffaelechiatto.com/installazione-e-configurazione-base-di-adguard-home-su-ubuntu-server-26-04-con-docker-compose/ | articolo del 17/09/2026, corpo letto il 22/09 tramite API pubblica WordPress dopo mancato recupero web | AdGuard in Docker; [nota](docs/fonti/adguard-home.md); lettura conclusa, procedura non eseguita |
| U05 | https://github.com/usestrix/strix | repository ufficiale, README letto il 22/09 | pentest applicativo autonomo; [nota](docs/fonti/strix.md) |
| U06 | https://novascm.polariscore.it/ | involucro con iframe, letto il 22/09 | rimanda alla pagina effettiva NovaSCM; [nota](docs/fonti/novascm.md) |
| U07 | `screenshot_180.png`, `screenshot_184.png`..`screenshot_195.png` (in `_notes/fonti/2026-09-22-dischi-qnap/`) | immagini lette il 22/09 dall'interfaccia QNAP Storage Manager, scheda Disk SMART | stato SMART dei quattro dischi da 2 TB recuperati; studio dischi QNAP. Valori letti dall'interfaccia, non da `smartctl`, da riverificare a dischi collegati |
| U08 | `screenshot_183.png` (in `_notes/fonti/2026-09-22-dischi-qnap/`) | immagine letta il 22/09 | riepilogo del QNAP TS-410U: Marvell 6281 800 MHz, 512 MB RAM, 4x2 TB in RAID 5 = 5,40 TB; studio dischi QNAP |

## Fonti tecniche curate

Le voci seguenti sono consultate il 22/09/2026 salvo indicazione diversa. La lettura riguarda il contenuto pertinente alla decisione, non un audit dell'intero codice o sito.

<!-- CURATED SOURCES -->

| ID | Fonte | Tipo / stato | Cosa sostiene e dove serve |
|---|---|---|---|
| S01 | https://github.com/AdguardTeam/AdGuardHome/wiki/Docker | ufficiale, lettura parziale; consultata anche versione raw | installazione container, persistenza e rete; nota AdGuard |
| S02 | https://raw.githubusercontent.com/wiki/AdguardTeam/AdGuardHome/Docker.md | ufficiale, letta | testo della guida Docker; nota AdGuard |
| S03 | https://docs.opnsense.org/manual/unbound.html | ufficiale, consultata | resolver, override e blocklist; studio DNS |
| S04 | https://github.com/chubin/cheat.sh | progetto ufficiale, README consultato | riferimento comandi; screenshot U02 |
| S05 | https://developers.cloudflare.com/waf/ | ufficiale, consultata | WAF applicativo e differenze per piano; screenshot U01 |
| S06 | https://www.polariscore.it/novascm/ | autore del progetto, pagina letta via HTTP | funzioni dichiarate e collegamento al codice; nota NovaSCM |
| S07 | https://github.com/ClaudioBecchis/NovaSCM | progetto ufficiale, README consultato | console, server, workflow, inventario e deploy; nota NovaSCM |
| S08 | https://github.com/ClaudioBecchis/NovaSCM/blob/main/LICENSE | repository ufficiale, pagina individuata; testo da riverificare | verifica licenza prima di adozione; il sito dichiara MIT |
| S09 | https://www.zyxel.com/global/en/products/switch/xmg1915-series/specifications | produttore, tabella letta | porte, PoE, assenza ventola sui 10E/10EP e routing statico; studio acquisti |
| S10 | https://www.zyxel.com/global/en/products/switch/xmg1915-series/features | produttore, consultata | VLAN e funzioni gestionali; studio acquisti |
| S11 | https://www.zyxel.com/global/en/products/wireless/nwa50be-pro/specifications | produttore, tabella letta | uplink 2,5 GbE e PoE+ 16 W; studio acquisti |
| S12 | https://www.zyxel.com/global/en/products/wireless/nwa50be-pro | produttore, consultata | doppia radio BandFlex e gestione standalone; studio acquisti |
| S13 | https://www.zyxel.com/global/en/products/wireless/nwa130be/specifications | produttore, tabella letta | tre radio, due porte 2,5 GbE, PoE+ 24 W e RADIUS; studio acquisti |
| S14 | https://www.zyxel.com/global/en/products/wireless/nwa50ax-pro/specifications | produttore, tabella letta | alternativa Wi-Fi 6, 2,5 GbE, 20,5 W; studio acquisti |
| S15 | https://www.zyxel.com/global/en/products/wireless/nwa90be-pro/specifications | produttore, consultata | candidato con funzioni enterprise; verifica per EAP-TLS |
| S16 | https://www.zyxel.com/global/en/products/switch/gs1915-series | produttore, consultata | alternativa Gigabit e budget 60 W del modello 8EP |
| S17 | https://www.zyxel.com/global/en/products/nebula-cloud-center/nebula-control-center/plans-and-pricing | produttore, estratto di ricerca | Base gratuito e piani aggiuntivi; verificare funzioni richieste sul piano corrente |
| S18 | https://community.zyxel.com/en/discussion/14731/nwa50ax-managment-vlan | community, discussione letta; intervento dipendente Zyxel | errore di tagging e risoluzione DHCP; nota Zyxel |
| S19 | https://community.zyxel.com/en/discussion/30875/help-with-nwa50be-pro | community, letta; risposta dipendente Zyxel | 5 e 6 GHz non simultanei sul 50BE Pro; nota Zyxel |
| S20 | https://community.zyxel.com/en/discussion/28852/heads-up-latest-wi-fi-7-enforces-new-mlo-change-zyxel-implement-in-7-20 | comunicazione sul forum del produttore, consultata | MLO/WPA3 e compatibilita' client da collaudare |
| S21 | https://community.zyxel.com/en/discussion/1150/gs1900-8hp-poe-budget | community del 2018, testo recuperato nei risultati | potenza riservata per classe rispetto al consumo; pista di collaudo, non bug attribuito a XMG1915 |
| S22 | https://www.reddit.com/r/homelab/comments/1cpeo16/looking_to_upgrade_to_25g_any_opinions_on_the/ | testimonianze dirette, lettura porzione pertinente | esperienza 10EP/18EP, rumore e routing; corroborazione tecnica su S09 |
| S23 | https://www.idealo.it/confronta-prezzi/203921679/zyxel-xmg1915-10ep.html | commerciale, pagina consultata; indice della settimana precedente | prezzo indicativo 288,17 euro, non preventivo |
| S24 | https://www.idealo.it/confronta-prezzi/207723303/zyxel-nwa50be-pro.html | commerciale, pagina consultata; indice del mese precedente | prezzo indicativo 102,70 euro, non preventivo |
| S25 | https://www.idealo.it/confronta-prezzi/204014075/zyxel-nwa130be.html | commerciale, pagina aperta con cache del giorno precedente | 188,62 euro nella pagina aperta; il vecchio estratto dava 169,14: usata la pagina, sempre da riconfermare |
| S26 | https://www.idealo.it/confronta-prezzi/203921684/zyxel-xmg1915-10e.html | commerciale, estratto indicizzato di quattro settimane prima | prezzo indicativo 195,22 euro, da riconfermare |
| S27 | https://github.com/louislam/uptime-kuma | progetto ufficiale, consultato | monitor disponibilita'; studio servizi |
| S28 | https://github.com/henrygd/beszel | progetto ufficiale, consultato | metriche host leggere; studio servizi |
| S29 | https://docs.librenms.org/ | ufficiale, consultata | monitoraggio rete; studio servizi |
| S30 | https://documentation.wazuh.com/current/quickstart.html | ufficiale, requisiti letti | 1-25 agenti: 4 vCPU, 8 GiB RAM, 50 GB per 90 giorni; dimensionamento |
| S31 | https://docs.opnsense.org/manual/ips.html | ufficiale, consultata | Suricata IDS/IPS e vincoli di interfaccia; studio sicurezza |
| S32 | https://restic.readthedocs.io/en/stable/ | ufficiale, consultata | backup e ripristino; studio servizi |
| S33 | https://docs.opnsense.org/manual/how-tos/wireguard-client.html | ufficiale, consultata | VPN road warrior; topologia e accesso remoto |
| S34 | https://docs.netbird.io/selfhosted/selfhosted-quickstart | ufficiale, consultata | alternativa overlay self-hosted; non necessaria alla prima fase |
| S35 | https://netboxlabs.com/docs/netbox/ | ufficiale, consultata tramite redirect di docs.netbox.dev | documentazione infrastrutturale e IPAM; confronto inventario |
| S36 | https://www.glpi-project.org/en/features/ | ufficiale, consultata | asset, inventario e gestione IT; confronto inventario |
| S37 | https://github.com/Ylianst/MeshCentral | progetto ufficiale, consultato | accesso remoto tramite agenti; confronto con NovaSCM |
| S38 | https://www.zaproxy.org/docs/docker/baseline-scan/ | ufficiale, letta | spider e analisi passiva, distinti dagli attacchi attivi; piano pentest |
| S39 | https://trivy.dev/docs/latest/guide/ | ufficiale, consultata | vulnerabilita' e configurazioni di immagini/progetti; piano pentest |
| S40 | https://www.proxmox.com/en/products/proxmox-virtual-environment/pricing | ufficiale, consultata | software e sottoscrizione di supporto; host di calcolo separato |
| S41 | https://github.com/pi-hole/pi-hole | progetto ufficiale, consultato | alternativa DNS filtrante; studio servizi |
| S42 | https://github.com/immich-app/immich | progetto ufficiale, consultato | foto e video self-hosted; servizio successivo al backup |
| S43 | https://github.com/paperless-ngx/paperless-ngx | progetto ufficiale, consultato | gestione documenti; servizio successivo al backup |
| S44 | https://github.com/dani-garcia/vaultwarden | progetto ufficiale, consultato | server compatibile Bitwarden non ufficiale; continuita' e backup da progettare |
| S45 | https://github.com/nextcloud/server | progetto ufficiale, consultato | sincronizzazione e condivisione; adottare solo se necessarie |
| S46 | https://github.com/awesome-selfhosted/awesome-selfhosted | catalogo mantenuto dalla community, consultato | scoperta di alternative; presenza nel catalogo non equivale a verifica |
| S47 | https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-command-injection-and-improper-authentication-vulnerabilities-in-certain-aps-fwa7-and-security-routers-08-04-2026 | produttore, avviso e tabella letti | firmware correttivi per AP candidati; studio acquisti |
| S48 | https://www.zyxel.com/global/en/support/end-of-life | produttore, pagina consultata | controllo ciclo di vita prima dell'ordine; nessuna data garantita dei candidati stabilita in questo studio |
| S49 | https://pve.proxmox.com/wiki/Migrate_to_Proxmox_VE?trk=public_post_comment-text | documentazione ufficiale, estratto di ricerca | funzionalita' disponibili senza canone; distinzione dal supporto |
| S50 | https://www.backblaze.com/blog/are-hard-drives-getting-better-lets-revisit-the-bathtub-curve/ | resoconto statistico del fornitore, risultati di ricerca letti; pagina da aprire per conferma | picco di guasto a 10 anni e 3 mesi su ~317k unita' e curva a vasca spostata a destra; studio dischi QNAP, usato per dire che i dischi stanno fuori dalle curve pubblicate |
| S51 | https://sourceforge.net/p/smartmontools/mailman/message/27378703/ | lista di supporto smartmontools, risultati di ricerca letti | difetto del firmware 1AQ10001 dell'HD204UI su IDENTIFY/SMART durante NCQ e correttivo che non cambia versione; studio dischi QNAP |
| S52 | https://www.truenas.com/community/resources/hard-drive-burn-in-testing.92/ | risorsa di community TrueNAS, risultati di ricerca letti | protocollo di collaudo dischi con badblocks -wsv e smartctl -t long, e attributi 5/197/198/199 come criterio di scarto; studio dischi QNAP |
| S53 | https://github.com/sooryathejas/METATRON | repository del progetto, presentazione consegnata dall'utente; codice non eseguito | assistente di pentesting con modello linguistico locale su Parrot OS; scheda VA e pentesting. Descrizione degli autori, non provata in laboratorio |

## Materiali locali che non devono sparire dal quadro

Gli originali gia' censiti in [Fonti e materiali](docs/fonti-e-materiali.md) restano registrati: Word iniziale, whitepaper OPNsense, `quickprint.docx`, 31 fotografie di installazione, DxDiag del portatile, diagramma del monitoraggio, appunti draw.io, privacy pack e due segnalibri. Il Word e' archivio storico dal 25/08/2026, non un sorgente da rigenerare. I report hardware e i documenti privati del consolidamento NAS restano sotto il controllo della sessione NAS: si citano le controparti pubbliche, senza duplicare valori reali o stato del banco.

I tre screenshot U01-U03 sono stati letti nella cartella locale Screenpresso; i loro originali non sono pubblicati. Tutto il contenuto tecnico identificabile e' riportato nella nota collegata. Non si deducono nome del video, autore, sito aggregatore o strumenti fuori inquadratura.

## Censimento conservativo degli altri riferimenti

Il censimento include le citazioni storiche e i risultati individuati durante la ricerca, anche quando non selezionati per lo studio. Il testo a cui ciascuna fonte serviva resta nel file di provenienza. Non si promuove una vecchia citazione a verifica corrente; URL diversi, versioni, query e frammenti restano distinti. Eventuali URL di esempio presenti nei documenti vengono conservati e non vanno scambiati per fonti tecniche.

<!-- BEGIN SOURCE COVERAGE -->

| ID stabile | URL esatto | Provenienza conservata | Stato |
|---|---|---|---|
| H-210x8dbx1a1x41c | http://www.example.com | `docs/03-spunti-di-sviluppo/11-server-dns-secondario-privato/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-00cxd89x8cfxe62 | http://www.ripe.net/whois | `docs/02-ftth-fastweb/05-prima-del-design-della-rete-privata/02-ticket-a-fastweb-26022026-2802026.md` | censita; lettura e contenuto da verificare |
| H-8bbx866x38ex7f1 | https://203.0.113.41 | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/05-uscire-con-la-lan-fuori.md` | censita; lettura e contenuto da verificare |
| H-a01x928x3e7xd3a | https://adminboxpro.com/program/meshcentral/ | `docs/03-spunti-di-sviluppo/04-rmm-management-meshcentral-self-hosted-open-source/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-c2dxb7bx108xa91 | https://adminhub.dev/program/meshcentral/ | `docs/03-spunti-di-sviluppo/04-rmm-management-meshcentral-self-hosted-open-source/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-8a6x1b3xb8ex18e | https://apps.db.ripe.net/db-web-ui/query | `docs/02-ftth-fastweb/05-prima-del-design-della-rete-privata/02-ticket-a-fastweb-26022026-2802026.md` | censita; lettura e contenuto da verificare |
| H-817x975x02cxb88 | https://blog.octabyte.io/posts/development/pritunl/pritunl-the-open-source-vpn-solution-for-secure-and-scalable-remote-access/ | `docs/03-spunti-di-sviluppo/12-vpn/05-comparazione-pritunl-e-tailscale.md` | censita; lettura e contenuto da verificare |
| H-e88xee0xf1cx6ef | https://corpsystools.com/program/meshcentral/ | `docs/03-spunti-di-sviluppo/04-rmm-management-meshcentral-self-hosted-open-source/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-47bx60dxc44x603 | https://cybersecsentinel.com/short-lived-certs-long-term-security-lets-encrypt-secures-ips/ | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/05-uscire-con-la-lan-fuori.md` | censita; lettura e contenuto da verificare |
| H-a12xfaax686xac9 | https://deno.com/deploy | `docs/03-spunti-di-sviluppo/22-sviluppi-interni-aggiuntivi/01-hosting-di-un-bot-python-telegram.md` | censita; lettura e contenuto da verificare |
| H-089x283x425x8e7 | https://deno.com/deploy/pricing | `docs/03-spunti-di-sviluppo/22-sviluppi-interni-aggiuntivi/01-hosting-di-un-bot-python-telegram.md` | censita; lettura e contenuto da verificare |
| H-009x32fxd46xb6a | https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/H170-PRO/E12046_H170-PRO_UM_V2_WEB.pdf | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-528x6f6xb0cx68e | https://docs.nethsecurity.org/en/latest/download.html | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/04-tbc-l-alternativa-ulteriore-nethsecurity8.md` | censita; lettura e contenuto da verificare |
| H-8d2x3f0xcccxa0f | https://docs.opnsense.org/firewall.html | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md` | censita; lettura e contenuto da verificare |
| H-7f2x0ddx515x6e2 | https://docs.opnsense.org/manual/gui.html | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md` | censita; lettura e contenuto da verificare |
| H-0a3xad7x68dx413 | https://docs.opnsense.org/manual/install.html | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md` | censita; lettura e contenuto da verificare |
| H-d02x2ddx683xb57 | https://docs.opnsense.org/manual/install.html#download-and-verification | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md` | censita; lettura e contenuto da verificare |
| H-222xbd6xbdax509 | https://docs.opnsense.org/third_party_plugins.html | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md` | censita; lettura e contenuto da verificare |
| H-dc2x235x3d6x9cc | https://docs.opnsense.org/vendor/sunnyvalley/zenarmor.html | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md` | censita; lettura e contenuto da verificare |
| H-b06x65bxd68x97e | https://download.truenas.com/TrueNAS-SCALE-Goldeye/25.10.4/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-c5fxf97x10fx952 | https://download.truenas.com/TrueNAS-SCALE-Goldeye/25.10.4/TrueNAS-SCALE-25.10.4.iso.sha256 | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-08dx28dxf6dx9cb | https://e-catalog.com/KINGSTON-INDUSTRIAL-MICROSDHC-32GB.htm | `docs/03-spunti-di-sviluppo/01-storage-non-di-rete/01-micro-sd-robuste.md` | censita; lettura e contenuto da verificare |
| H-b59x6bbxc21x4e9 | https://en.wikipedia.org/wiki/X86-64 | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md` | censita; lettura e contenuto da verificare |
| H-e7ex94dxe8bx2a5 | https://gigazine.net/gsc_news/en/20251109-tailscale-technical-overview | `docs/03-spunti-di-sviluppo/12-vpn/05-comparazione-pritunl-e-tailscale.md` | censita; lettura e contenuto da verificare |
| H-230x69fx7caxb06 | https://github.com/Gowtham-Darkseid/AutoPentestX | `docs/03-spunti-di-sviluppo/16-va-e-pentesting/02-autopentestx-linux-automated-pentesting-vulnerability-report.md` | censita; lettura e contenuto da verificare |
| H-c8dx034x8c4xa3b | https://github.com/NakedTrashPanda/OneCommander-Catppuccin-Theme | `docs/03-spunti-di-sviluppo/06-file-storage-e-handling/01-onecommander-for-windows.md` | censita; lettura e contenuto da verificare |
| H-5f4x943xc82x7c6 | https://github.com/memtest86plus/memtest86plus/releases | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-09bx313x984x599 | https://github.com/sooryathejas/METATRON/tree/main | `docs/03-spunti-di-sviluppo/16-va-e-pentesting/03-metatron-pentesting-assistito-da-llm-locale.md` | censita; lettura e contenuto da verificare |
| H-fdcx094x68axa7c | https://github.com/tailscale/tailscale | `docs/03-spunti-di-sviluppo/12-vpn/05-comparazione-pritunl-e-tailscale.md` | censita; lettura e contenuto da verificare |
| H-b75xb46x0bfx416 | https://help.sapphireims.com/Remote_Control_using_MeshCentral.htm | `docs/03-spunti-di-sviluppo/04-rmm-management-meshcentral-self-hosted-open-source/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-7caxea7xa0exd4b | https://hossted.com/knowledge-base/osspedia/infrastructure-and-network/networking/empowering-secure-remote-device-management-with-meshcentral-self-hosted-scalable-and-privacy-first-control/ | `docs/03-spunti-di-sviluppo/04-rmm-management-meshcentral-self-hosted-open-source/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-f12xe84x933x520 | https://it.infobyip.com/ | `docs/02-ftth-fastweb/05-prima-del-design-della-rete-privata/02-ticket-a-fastweb-26022026-2802026.md` | censita; lettura e contenuto da verificare |
| H-c41xfc6xd53x4ab | https://it.scribd.com/document/543055536/MeshCentral2UserGuide-0-2-9 | `docs/03-spunti-di-sviluppo/04-rmm-management-meshcentral-self-hosted-open-source/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-77fx70dx632x559 | https://it.wikipedia.org/wiki/Pi-hole | `docs/03-spunti-di-sviluppo/11-server-dns-secondario-privato/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-43exf47xaebx2c7 | https://letsencrypt.org/2025/01/16/6-day-and-ip-certs | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/05-uscire-con-la-lan-fuori.md` | censita; lettura e contenuto da verificare |
| H-9b1x7f3x6cexa90 | https://lkml.iu.edu/1801.1/05775.html | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-864x604xe88x3e9 | https://offerta-internet.it/fastweb-nexxt-box-one | `docs/02-ftth-fastweb/02-modem/01-vecchi-modem-che-venivano-dati-in-comodato-d-uso.md` | censita; lettura e contenuto da verificare |
| H-2cax7e8x00ex803 | https://openvas.org/ | `docs/03-spunti-di-sviluppo/16-va-e-pentesting/01-openvas.md` | censita; lettura e contenuto da verificare |
| H-f86x4afx79fxa64 | https://opnsense.org/ | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md` | censita; lettura e contenuto da verificare |
| H-081xde9x65cxac4 | https://ostechnix.com/truenas-26-beta-released/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-51ex53fx8f6xb5f | https://pi-hole.net/ | `docs/03-spunti-di-sviluppo/11-server-dns-secondario-privato/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-031xceax51axaf1 | https://pritunl.com/ | `docs/03-spunti-di-sviluppo/12-vpn/04-pritunl-with-web-interface-open-source-per-gestione-centrali.md`; `docs/03-spunti-di-sviluppo/12-vpn/05-comparazione-pritunl-e-tailscale.md` | censita; lettura e contenuto da verificare |
| H-cf8xfd1x75ax91b | https://rdap.arin.net/registry/entity/ABUSE3850-ARIN | `docs/02-ftth-fastweb/05-prima-del-design-della-rete-privata/02-ticket-a-fastweb-26022026-2802026.md` | censita; lettura e contenuto da verificare |
| H-412xb7dx970x1a1 | https://rdap.arin.net/registry/entity/RIPE | `docs/02-ftth-fastweb/05-prima-del-design-della-rete-privata/02-ticket-a-fastweb-26022026-2802026.md` | censita; lettura e contenuto da verificare |
| H-a33xa94xdd5x3e9 | https://rdap.arin.net/registry/entity/RNO29-ARIN | `docs/02-ftth-fastweb/05-prima-del-design-della-rete-privata/02-ticket-a-fastweb-26022026-2802026.md` | censita; lettura e contenuto da verificare |
| H-8d6xc2fxe38x087 | https://rdap.arin.net/registry/ip/203.0.113.0 | `docs/02-ftth-fastweb/05-prima-del-design-della-rete-privata/02-ticket-a-fastweb-26022026-2802026.md` | censita; lettura e contenuto da verificare |
| H-a00xbabxd44x080 | https://support.zyxel.eu/hc/en-us/articles/4416989548178-Access-Point-NWA50-55AXEE-90AX-110AX-210AX-Differences-in-Hardware-and-Features | `docs/fonti/ricerca-2026-09-22.json` | censita; lettura e contenuto da verificare |
| H-c26x4b5xd33x96d | https://syslinuxos.com/ | `docs/03-spunti-di-sviluppo/09-monitoraggio/01-nodo-di-analisi-e-diagnostica-rete.md` | censita; lettura e contenuto da verificare |
| H-428x1f6x761x931 | https://tailscale.com/compare/pritunl | `docs/03-spunti-di-sviluppo/12-vpn/05-comparazione-pritunl-e-tailscale.md` | censita; lettura e contenuto da verificare |
| H-a01x990xf16x444 | https://wazuh.com/ | `docs/03-spunti-di-sviluppo/21-idee-setup-da-profili-linkedin-interessanti/02-home-lab-cybersecurity-infrastructure-autore-linkedin-b.md` | censita; lettura e contenuto da verificare |
| H-273xd0bxeedxb41 | https://www.7-zip.org/download.html | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md` | censita; lettura e contenuto da verificare |
| H-b77xae1x9b5xb08 | https://www.alldatasheet.com/datasheet-pdf/pdf/1480326/KINGSTON/SDCIT2/32GB.html | `docs/03-spunti-di-sviluppo/01-storage-non-di-rete/01-micro-sd-robuste.md` | censita; lettura e contenuto da verificare |
| H-631x8f2x0f4x5df | https://www.amazon.it/10Gtek%C2%AE-I210-T1-Gigabit-Ethernet-singola/dp/B01H6O7TMO | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-fabxc0dx577x90d | https://www.amazon.it/503-incasso/s?k=503+incasso | `docs/02-ftth-fastweb/04-come-avviene-la-posatura-e-il-passaggio-fibra.md` | censita; lettura e contenuto da verificare |
| H-892x883xa6cx30c | https://www.amazon.it/AMPCOM-Adattatore-SSD-Express-PCIe/dp/B0876MLNY6 | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-d89x653x910x3b6 | https://www.amazon.it/Gigabit-Intel-Converged-Network-Adapter-Ethernet/dp/B073F51FHT | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-168xe74xeb2xb83 | https://www.amazon.it/HB-DIGITAL-Cat-6a-connettore-resistente-impermeabile/dp/B08P5S42ZL/ref=sr_1_4?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1C6YY14AY9J0P&dib=eyJ2IjoiMSJ9.-WySkLGXEXcFQcW51MvTpHRB6lv3XzoxYePrCHrbLz9m2A7bbIBoUNJX8FWFPJCkaboHYKlc7fgln5SC8LpvO6li2mubaVXmPJkGXxrLhnwZXvX5SFRAKaBPDLelWoqo2RD1iiwOzDYMBFiIh_6r4NAqf_rIlFSL_LkwyjCBoyKuahysaOtFwrCTuoi1GECqyCayCGtCma7MSiW8_ea1xO5lqGKnb0pBDXXSEGB5BC1XItBqvoSxaSUzSauqz5ApL-6Fe1XXM4h98Zsvnjp7V1OPxQMGFfjVILAQ0aUDtJw.8z4Tp8E5IL1v6JxQOQIB4Yy_krWHPBfqHzMmbXofbQI&dib_tag=se&keywords=Cavo+Ethernet+Cat6A+30m+Solid+%28Outdoor%2FInterno%29&qid=1765970076&s=electronics&sprefix=cavo+ethernet+cat6a+30m+solid+outdoor%2Finterno+%2Celectronics%2C232&sr=1-4 | `docs/04-concetti-generali/03-passaggi-cavi-fisici/02-studio-soluzioni-pratiche-per-passaggi-cavi-fisici.md` | censita; lettura e contenuto da verificare |
| H-72fx955x05cx7cf | https://www.amazon.it/Intel-%C2%AE-I210T1-Scheda-rete/dp/B00C3S791U | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-cb4xfa1xc75x3ad | https://www.amazon.it/Lotvic-Passacavi-Elettricista-Poliestere-LInstallazione/dp/B0B8SPBVZB | `docs/04-concetti-generali/03-passaggi-cavi-fisici/02-studio-soluzioni-pratiche-per-passaggi-cavi-fisici.md` | censita; lettura e contenuto da verificare |
| H-c22xf68xea5xe95 | https://www.amazon.it/Passacavi-Professionale-Elettricista-LInstallazione-terminali/dp/B0DKP9N6J2/ | `docs/04-concetti-generali/03-passaggi-cavi-fisici/02-studio-soluzioni-pratiche-per-passaggi-cavi-fisici.md` | censita; lettura e contenuto da verificare |
| H-cfcx279xdaexf40 | https://www.amazon.it/TP-Link-Adattatore-Express-supporta-TX201/dp/B0BKTHJDHX/?th=1 | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md` | censita; lettura e contenuto da verificare |
| H-c6dx2afxffex7aa | https://www.amazon.it/gp/product/B0F1LLNDMH/ref=ewc_pr_img_1?smid=AXJYC9MH9K5LP&psc=1 | `docs/04-concetti-generali/03-passaggi-cavi-fisici/02-studio-soluzioni-pratiche-per-passaggi-cavi-fisici.md` | censita; lettura e contenuto da verificare |
| H-496xe43xca8xb67 | https://www.angeloantona.it/progetti/Consulenza/00099-Piccola_infrastruttura_enterprise_EN.html | `docs/fonti-e-materiali.md` | censita; lettura e contenuto da verificare |
| H-ea6x91bx57ax162 | https://www.arin.net/resources/registry/whois/inaccuracy_reporting/ | `docs/02-ftth-fastweb/05-prima-del-design-della-rete-privata/02-ticket-a-fastweb-26022026-2802026.md` | censita; lettura e contenuto da verificare |
| H-0b7x612xc61xf4f | https://www.arin.net/resources/registry/whois/tou/ | `docs/02-ftth-fastweb/05-prima-del-design-della-rete-privata/02-ticket-a-fastweb-26022026-2802026.md` | censita; lettura e contenuto da verificare |
| H-92exa52x92fx476 | https://www.bhphotovideo.com/c/product/1661916-REG/kingston_sdcit2_32gb_32gb_microsdhc_industrial_c10.html | `docs/03-spunti-di-sviluppo/01-storage-non-di-rete/01-micro-sd-robuste.md` | censita; lettura e contenuto da verificare |
| H-b01xc78x697xb75 | https://www.deciso.com/opnsense-25-7-visionary-viper-launches-with-smarter-security-and-faster-setup/ | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md` | censita; lettura e contenuto da verificare |
| H-5d5x635xbfbx3ea | https://www.drawio.com/ | `docs/fonti-e-materiali.md` | censita; lettura e contenuto da verificare |
| H-462xb56x06ex9e4 | https://www.fastweb.it/adsl-fibra-ottica/connessione-fastweb/ | `docs/02-ftth-fastweb/01-introduzione.md`; `docs/fonti/fastweb-ont-modem.md` | censita; lettura e contenuto da verificare |
| H-ecax98fxe9dx11e | https://www.fastweb.it/adsl-fibra-ottica/dettagli/altri-modem/ | `docs/fonti/fastweb-ont-modem.md` | censita; lettura e contenuto da verificare |
| H-121x839x812xc35 | https://www.fastweb.it/modem/ | `docs/02-ftth-fastweb/02-modem/README.md` | censita; lettura e contenuto da verificare |
| H-847x1bbx422x359 | https://www.fastweb.it/myfastweb/assistenza/guide/compatibilita-tecniche-del-modem-di-tua-proprieta/ | `docs/fonti/fastweb-ont-modem.md` | censita; lettura e contenuto da verificare |
| H-531x44bx2edxa49 | https://www.fastweb.it/myfastweb/assistenza/guide/seven-installazione-bs-gpon | `docs/fonti/fastweb-ont-modem.md` | censita; lettura e contenuto da verificare |
| H-29fxb2cxdbbx00b | https://www.fastweb.it/myfastweb/seven/ | `docs/02-ftth-fastweb/02-modem/02-fastweb-seven-modello-fibra.md`; `docs/05-analisi-del-caso/01-tbc-studio-dispositivi-domestici.md` | censita; lettura e contenuto da verificare |
| H-daax927x775x9e6 | https://www.glotrends-store.com/products/pa05 | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-f37x474x459x958 | https://www.ictsecuritymagazine.com/articoli/tailscale-vpn-open-source/ | `docs/03-spunti-di-sviluppo/12-vpn/02-tailscale.md`; `docs/03-spunti-di-sviluppo/12-vpn/05-comparazione-pritunl-e-tailscale.md` | censita; lettura e contenuto da verificare |
| H-e7ax2aax174x14a | https://www.ilsoftware.it/lets-encrypt-https-anche-su-indirizzi-ip-pubblici-senza-dominio/ | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/05-uscire-con-la-lan-fuori.md` | censita; lettura e contenuto da verificare |
| H-5b4x5d0xe4fx1c4 | https://www.ilsoftware.it/tailscale-cambio-profilo-gratuito/ | `docs/03-spunti-di-sviluppo/12-vpn/03-tbc-cambio-profilo-gratuito.md` | censita; lettura e contenuto da verificare |
| H-4fexa0bxab8xc76 | https://www.intel.com/content/www/us/en/products/sku/184676/intel-ethernet-controller-i225v/specifications.html | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md` | censita; lettura e contenuto da verificare |
| H-673x396x488x462 | https://www.ipfire.org/blog/ipfire-2-29-core-update-200-released | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/03-l-alternativa-linux-ip-fire-e-confronto.md` | censita; lettura e contenuto da verificare |
| H-ef6xcedx333xcd8 | https://www.itu.int/rec/T-REC-G.657 | `docs/02-ftth-fastweb/04-come-avviene-la-posatura-e-il-passaggio-fibra.md` | censita; lettura e contenuto da verificare |
| H-543xb13x252x93f | https://www.itu.int/rec/T-REC-G.9807.1 | `docs/02-ftth-fastweb/04-come-avviene-la-posatura-e-il-passaggio-fibra.md` | censita; lettura e contenuto da verificare |
| H-2c1x85cx813x30a | https://www.itu.int/rec/T-REC-G.984 | `docs/02-ftth-fastweb/04-come-avviene-la-posatura-e-il-passaggio-fibra.md` | censita; lettura e contenuto da verificare |
| H-020xe70x733x4eb | https://www.kingston.com/datasheets/sdcit2_us.pdf | `docs/03-spunti-di-sviluppo/01-storage-non-di-rete/01-micro-sd-robuste.md` | censita; lettura e contenuto da verificare |
| H-c50x8a3x67bxaca | https://www.linkedin.com/in/ACoAABSc9aABi8vyWB72YzZwoXloPfaest2-sm0 | `docs/03-spunti-di-sviluppo/09-monitoraggio/02-siem-analysis.md`; `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/02-soluzione-professionale-con-opnsense-25-7.md` | censita; lettura e contenuto da verificare |
| H-b1fxaa2x737x97e | https://www.linkedin.com/in/Autore-LinkedIn-B-Autore-LinkedIn-B-4738771a9/ | `docs/03-spunti-di-sviluppo/21-idee-setup-da-profili-linkedin-interessanti/02-home-lab-cybersecurity-infrastructure-autore-linkedin-b.md` | censita; lettura e contenuto da verificare |
| H-5f2x95cx957xdbe | https://www.memtest.org/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-937xe9exe55x8b5 | https://www.mondomobileweb.it/307166-fastweb-seven-e-vodafone-seven-nuovi-modem-con-wi-fi-7-caratteristiche-e-cosa-cambia/ | `docs/02-ftth-fastweb/02-modem/02-fastweb-seven-modello-fibra.md` | censita; lettura e contenuto da verificare |
| H-386xe99xfe2xb25 | https://www.navigaresenzapubblicita.org/unbound-e-pi-hole-una-soluzione-dns-completa/ | `docs/03-spunti-di-sviluppo/11-server-dns-secondario-privato/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-ea2x253xffex88b | https://www.neowin.net/reviews/terramaster-f2-425-review-a-low-cost-local-cloud-backup-and-streaming-nas/ | `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/01-gestire-dati-su-disco-e-renderli-disponibili-in-modo-ordinat.md` | censita; lettura e contenuto da verificare |
| H-01fxd1axa83x97d | https://www.onecommander.com/ | `docs/03-spunti-di-sviluppo/06-file-storage-e-handling/01-onecommander-for-windows.md` | censita; lettura e contenuto da verificare |
| H-b5fxe45xed4x03f | https://www.openmediavault.org/ | `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/01-gestire-dati-su-disco-e-renderli-disponibili-in-modo-ordinat.md` | censita; lettura e contenuto da verificare |
| H-75fx864x752x800 | https://www.phoronix.com/news/TrueNAS-26-Beta | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-2bcx826x018x239 | https://www.qnap.com/en-in/performance/model/ts-464 | `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/01-gestire-dati-su-disco-e-renderli-disponibili-in-modo-ordinat.md` | censita; lettura e contenuto da verificare |
| H-c33xd5ex9d9x23e | https://www.qnap.com/en/product/ts-464 | `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/01-gestire-dati-su-disco-e-renderli-disponibili-in-modo-ordinat.md` | censita; lettura e contenuto da verificare |
| H-ba3x5ecxdd2xefc | https://www.raffaelechiatto.com/installazione-e-configurazione-base-di-mailcow-su-ubuntu-server-24-04/ | `docs/03-spunti-di-sviluppo/07-further-protection/01-browser-and-navigation-protection.md` | censita; lettura e contenuto da verificare |
| H-61ax68cxf98x571 | https://www.reddit.com/r/HomeNetworking/comments/16oxkl1 | `docs/fonti/ricerca-2026-09-22.json` | censita; lettura e contenuto da verificare |
| H-4cbxfd9xc4axa6b | https://www.reddit.com/r/HomeNetworking/comments/1g9e16m | `docs/fonti/ricerca-2026-09-22.json` | censita; lettura e contenuto da verificare |
| H-e48x659x62fxc2a | https://www.reddit.com/r/HomeNetworking/comments/1g9ej0j | `docs/fonti/ricerca-2026-09-22.json` | censita; lettura e contenuto da verificare |
| H-1e3xd60x332xadb | https://www.reddit.com/r/ItalyHardware/comments/1mtdqwv/parere_su_acquisto_di_dispositivi_hardware_per/ | `docs/03-spunti-di-sviluppo/15-vlan-segmentation.md` | censita; lettura e contenuto da verificare |
| H-7c2xd71x30fx957 | https://www.reddit.com/r/ItalyHardware/comments/1mtdqwv/parere_su_acquisto_di_dispositivi_hardware_per/?utm_source=chatgpt.com | `docs/03-spunti-di-sviluppo/10-firewall-before-the-switch/01-mini-pc-firewall.md` | censita; lettura e contenuto da verificare |
| H-003xd0fxda2xea8 | https://www.reddit.com/r/MeshCentral/comments/vvi1bt/meshcentral_agent_behind_reverse_proxy | `docs/03-spunti-di-sviluppo/04-rmm-management-meshcentral-self-hosted-open-source/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-d4dx4cfxd97x630 | https://www.reddit.com/r/Ubiquiti/comments/1au5zm2/how_bad_did_i_mess_up/ | `docs/04-concetti-generali/03-passaggi-cavi-fisici/02-studio-soluzioni-pratiche-per-passaggi-cavi-fisici.md` | censita; lettura e contenuto da verificare |
| H-2fcx6b6x8b3x171 | https://www.synology.com/en-af/products/DS925%2B | `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/01-gestire-dati-su-disco-e-renderli-disponibili-in-modo-ordinat.md` | censita; lettura e contenuto da verificare |
| H-5ecx1a1x8d1x170 | https://www.techradar.com/computing/terramaster-f2-425-nas-review | `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/01-gestire-dati-su-disco-e-renderli-disponibili-in-modo-ordinat.md` | censita; lettura e contenuto da verificare |
| H-b4ex5d4xa04xb1b | https://www.theregister.com/2025/01/23/openzfs_23_raid_expansion/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-f5axcecx5bbx900 | https://www.tp-link.com/it/home-networking/soho-switch/tl-sg108-m2/ | `docs/03-spunti-di-sviluppo/13-switch/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-86cx019x784x598 | https://www.tp-link.com/us/business-networking/unmanaged-switch/tl-sg108-m2/ | `docs/03-spunti-di-sviluppo/13-switch/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-35dxd26xc85x083 | https://www.trovaprezzi.it/prezzo_altro-informatica_adattatore_m.2_pcie_nvme.aspx | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-46ax403x716x5bf | https://www.trovaprezzi.it/prezzo_schede-rete_intel_i210.aspx | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-876x8b2x49cxcd6 | https://www.truenas.com/blog/blog-truenas-26-beta1-release/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-f65x974x0bax127 | https://www.truenas.com/blog/truenas-25-10-2-goldeye/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-88ax25fx856xa0b | https://www.truenas.com/blog/truenas-25-10-rc1-features/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-5ffx8c4xdcaxe67 | https://www.truenas.com/blog/truenas-plans-for-2026/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-f7cx0e8xf83x48e | https://www.truenas.com/community/threads/fixed-realtek-rtl8111-8168-8411-flapping-on-high-transfer-rates.107797/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-32ax8e3x558x9aa | https://www.truenas.com/community/threads/realtek-8111h-on-truenas-scale.107268/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-d25xef9x92fxe54 | https://www.truenas.com/community/threads/truenas-12-and-realtek-updating-your-driver-to-1-96-to-prevent-re0-watchdog-timeout.88806/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-43exa83x3b5xdf5 | https://www.truenas.com/docs/core/13.0/coretutorials/systemconfiguration/mirroringthebootpool/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-3a1xd7bx258x46d | https://www.truenas.com/docs/scale/25.10/gettingstarted/install/installingscale/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-46bx273xe93x220 | https://www.truenas.com/docs/scale/25.10/gettingstarted/versionnotes/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-795x579x45dx702 | https://www.truenas.com/docs/scale/25.10/scaletutorials/storage/managepoolsscale/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-598xa54x1ccxf03 | https://www.truenas.com/docs/scale/scaletutorials/dataprotection/scrubtasksscale/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-1e3xb1fx612x968 | https://www.truenas.com/docs/softwarestatus/ | `docs/fonti-web-consultate.md` | censita; lettura e contenuto da verificare |
| H-d65x349xc5bxe65 | https://www.udemy.com/course/proxmox-per-comuni-mortali/?couponCode=KEEPLEARNING | `docs/03-spunti-di-sviluppo/21-idee-setup-da-profili-linkedin-interessanti/02-home-lab-cybersecurity-infrastructure-autore-linkedin-b.md` | censita; lettura e contenuto da verificare |
| H-3c3x68bx936xb5f | https://www.zyxel.com/it/it/products/switch/8-16-port-2-5gbe-smart-managed-switch-with-2-sfp-uplink-xmg1915-series/overview | `docs/03-spunti-di-sviluppo/13-switch/02-switch-2-5gbps-managed.md` | censita; lettura e contenuto da verificare |
| H-80cx730x841x210 | https://www.zyxel.com/uk/en-gb/products/switch/8-16-port-2-5gbe-smart-managed-switch-with-2-sfp-uplink-xmg1915-series/specifications | `docs/03-spunti-di-sviluppo/13-switch/02-switch-2-5gbps-managed.md` | censita; lettura e contenuto da verificare |
| H-64fx39cx71axc33 | https://www.zyxel.com/us/en-us/products/wireless/nwa50ax | `docs/fonti/ricerca-2026-09-22.json` | censita; lettura e contenuto da verificare |
| H-b73x187x3c0xfb0 | https://ylianst.github.io/MeshCentral/meshcentral/ | `docs/03-spunti-di-sviluppo/04-rmm-management-meshcentral-self-hosted-open-source/01-introduzione.md` | censita; lettura e contenuto da verificare |
| H-b9ax747x2d8x57c | https://youtu.be/2WReUqnN0zg?si=nibTgnXttw1fgSpD | `docs/03-spunti-di-sviluppo/12-vpn/01-migliori-vpn-2026-da-cybernews.md` | censita; lettura e contenuto da verificare |
| H-6b5x752xbb7xb5e | https://youtu.be/lzSWh25uwEw?si=cFaH2Gnc7WjHaoA2 | `docs/03-spunti-di-sviluppo/07-further-protection/02-endpoint-protection.md` | censita; lettura e contenuto da verificare |
| H-39axbd7x9aax580 | https://youtube.com/playlist?list=PL2FZs7vQjTinerbS4CN6YaaKsspZodA1v&si=QoFiThsLKockuwKJ | `docs/03-spunti-di-sviluppo/07-further-protection/01-browser-and-navigation-protection.md` | censita; lettura e contenuto da verificare |

<!-- END SOURCE COVERAGE -->
