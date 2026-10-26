# Protezione degli endpoint e hardening oltre il firewall, a costo zero, 2026

Ritorno a [Further protection](README.md). Studio del 15/10/2026, nato da una richiesta dell'utente: quale antivirus gratuito usare sugli endpoint di casa, tenendo conto di Microsoft Defender nel piano Family che l'utente ha già, e quale sia la copertura massima ottenibile oltre al firewall con soli strumenti gratuiti, preferibilmente open source, scartando quelli che non mantengono ciò che promettono. Completa la scheda [Endpoint protection](02-endpoint-protection.md), che contiene soltanto collegamenti a video.

Stato al 15/10/2026: studio, nessuna decisione e nulla installato. La ricerca è stata condotta da un agente in sessione su fonti web e sul repository, ed è stata rivista prima di scriverla qui. Ogni affermazione porta la fonte del [registro](../../../SOURCES.md); dove manca la fonte, la frase lo dice ed è un'inferenza. Le versioni degli strumenti sono state lette dalle pagine delle release di GitHub il 15/10/2026 attraverso un riassunto automatico e non sul dato grezzo (S116): vanno ricontrollate prima di installare, e le licenze, scritte qui a memoria, vanno ricontrollate nei repository.

## La risposta breve

La copertura migliore a costo zero non viene da un antivirus da installare: viene da Microsoft Defender Antivirus, già presente in Windows, irrigidito con funzioni gratuite che sono spente o tenui per impostazione predefinita, più l'agente Wazuh già deciso in ADR-028 come occhio su tutti i PC, più un filtro DNS e gli aggiornamenti automatici. Gli strumenti che si aggiungono servono a coprire i sistemi su cui Defender non arriva, cioè Linux, il NAS e i telefoni, e a misurare l'hardening invece di presumerlo.

Questa non è la sicurezza migliore in assoluto, e scriverlo sarebbe falso: è la copertura più larga ottenibile senza pagare, con lacune dichiarate più sotto. Quello che la rende robusta è che ogni dominio ha almeno uno strumento, che i domini si coprono fra loro, e che le scelte poggiano su decisioni già prese invece di aggiungere servizi.

## Che cosa dà davvero il Defender che l'utente ha

Il nome Family indica con ogni probabilità l'app Microsoft Defender per privati, che richiede un abbonamento Microsoft 365 Personal o Family e gira su Windows, macOS, iOS e Android (S115). Su Windows l'app è un cruscotto sopra la Sicurezza di Windows e non la sostituisce; su Android aggiunge scansione delle app e protezione web; su iOS offre solo la protezione dal phishing, senza antivirus (S115). Non copre Linux, PS5, TV e firewall. La disponibilità e le funzioni in Italia nel 2026 non sono verificate: le pagine Microsoft non si sono aperte durante la ricerca.

La parte che protegge davvero su Windows è Microsoft Defender Antivirus, gratuito e già nel sistema. Nel test Real-World Protection di AV-Comparatives di febbraio e marzo 2026 risulta al 99,0 per cento, 396 casi su 400, senza falsi positivi, ma il numero viene da estratti e non dalla pagina dei risultati letta per intero (S111). Il commento di AV-Comparatives del 26/05/2026 lo giudica una base credibile e segnala il punto debole: senza rete il rilevamento scende all'89,2 per cento, perché si appoggia al cloud (S110).

Tre funzioni gratuite di Defender alzano molto il livello e sono il primo intervento da fare.

| Funzione | Che cosa fa | Stato di partenza | Fonte |
|---|---|---|---|
| Regole ASR[^1] | bloccano comportamenti tipici del malware, come documenti di Office che lanciano processi o il furto di credenziali dalla memoria; disponibili su ogni edizione di Windows, Home compresa, configurabili in locale | tre nella protezione standard, le altre da accendere, prima in audit | S112 |
| Accesso controllato alle cartelle | impedisce ai programmi non fidati di modificare Documenti, Immagini e le altre cartelle protette, cioè la difesa specifica contro il ransomware | spento; si accende prima in audit e poi in blocco | S113 |
| Protezione da manomissioni | impedisce che un programma spenga Defender o ne cambi le impostazioni | stato predefinito su Windows 11 Home non verificato | S114 |

Una cautela da sapere: a maggio 2026 due vulnerabilità di Defender sono entrate nel catalogo CISA delle vulnerabilità sfruttate, già corrette (S110). Defender va quindi tenuto aggiornato come ogni altro programma.

## Gli strumenti, con il verdetto

| Strumento | Dominio | Sistema | Ultima release letta | Verdetto e motivo |
|---|---|---|---|---|
| Microsoft Defender Antivirus con ASR, cartelle controllate, SmartScreen | antimalware, hardening | Windows | aggiornato di continuo | adottare: base solida nei test, funzioni gratuite (S110, S112, S113) |
| App Microsoft Defender | cruscotto, antimalware Android, anti-phishing mobile | Windows, macOS, Android, iOS | non verificata | opzionale: utile sugli Android, già pagata (S115) |
| Wazuh, agente e server | EDR[^2] leggero, FIM[^3], controlli di configurazione CIS[^4], vulnerabilità, log | Linux, Windows, macOS | v4.14.8 del 25/09/2026 | adottare, già deciso in ADR-028; non è un antivirus a firme (S116, S117) |
| Sysmon integrato in Windows 11 | telemetria dei processi per Wazuh | Windows 11 | anteprima di febbraio 2026; disponibilità generale non confermata | adottare sui PC Windows se la build lo offre (S118) |
| ClamAV | antimalware a firme | Linux, Windows, macOS | 1.5.4 del 07/08/2026 | adottare in forma limitata: scansione pianificata del NAS e delle cartelle di scambio, non protezione in tempo reale (S116, S124) |
| Lynis | verifica dell'hardening | Linux, macOS | 3.1.7 del 25/06/2026 | adottare: verifica periodica di Proxmox e dei PC Linux (S116) |
| HardeningKitty | verifica e hardening | Windows | 0.9.4 del 21/07/2026 | opzionale: confronta Windows con i profili CIS e Microsoft; prima in sola verifica (S116) |
| AppArmor | confinamento dei processi | Linux | parte del sistema | adottare: attivo di default su Ubuntu secondo conoscenza non riverificata; basta non spegnerlo |
| fail2ban | blocco dei tentativi su SSH | Linux | 1.1.1 del 15/08/2026 | adottare sulle macchine Linux con SSH (S116) |
| CrowdSec | reputazione degli indirizzi e blocco | Linux, Windows | v1.8.1 del 03/09/2026 | opzionale: serve se un servizio verrà esposto su Internet, oggi nessuno (S116) |
| AdGuard Home | filtro DNS | Linux, container | v0.107.79 del 18/08/2026 | adottare: è il solo filtro che arriva anche a TV e PS5 (S116) |
| Pi-hole | filtro DNS | Linux | v6.4.3 del 06/07/2026 | scartare come doppione di AdGuard Home (S116) |
| uBlock Origin | blocco di pubblicità e tracciatori nel browser | Firefox, Chromium | 1.75.0 del 16/09/2026 | adottare, meglio su Firefox (S116) |
| Vaultwarden | gestore di password ospitato in casa | Linux, container | 1.37.4 del 05/10/2026 | adottare sul server, con secondo fattore e backup (S116) |
| restic | backup cifrato e deduplicato | Linux, Windows, macOS | v0.19.1 del 05/07/2026 | adottare, con prove di ripristino (S116) |
| BorgBackup | backup cifrato | Linux, macOS | 1.4.5 del 18/07/2026 | scartare come doppione di restic (S116) |
| osquery | interrogare lo stato delle macchine | Linux, Windows, macOS | 5.23.1 del 24/06/2026 | opzionale: si integra con Wazuh, ma serve saper scrivere interrogazioni (S116) |
| Velociraptor | analisi forense e risposta | Linux, Windows, macOS | v0.77.3 del 05/10/2026 | opzionale: da tenere pronto per un incidente, non sempre acceso (S116) |
| VeraCrypt | volumi cifrati portabili | Windows, Linux, macOS | 1.26.29 del 12/06/2026 | opzionale: BitLocker, LUKS e FileVault coprono già i dischi di sistema (S116) |
| GrapheneOS | Android irrigidito | solo Pixel | 2026100600 | non applicabile: i telefoni di casa sono Samsung e Sony (S119) |
| Google Play Protect | antimalware | Android | integrato | tenere acceso; il suo risultato nel test mobile 2026 non è stato letto (S120) |
| Kaspersky | antimalware | Windows e altri | | scartare: vendita vietata negli Stati Uniti dal 2024 (S121) e avviso dell'agenzia italiana per la cybersicurezza nel 2022 sul software russo (S125) |
| Avast e AVG | antimalware gratuito | Windows e altri | | scartare: la FTC ha vietato ad Avast nel 2024 di vendere i dati di navigazione dei suoi utenti (S122) |

Si scartano in blocco anche gli ottimizzatori e gli antivirus gratuiti sconosciuti che arrivano con pubblicità o installazioni abbinate: è un'inferenza di prudenza, non un test.

## La combinazione per dominio, nella rete già decisa

Antimalware su Windows, cioè PC-01, PC-04 e LAP-01: Defender Antivirus con protezione dal cloud e protezione da manomissioni attive, cartelle controllate prima in audit e poi in blocco, regole ASR della protezione standard attive e le altre in audit per qualche settimana. Resta scoperto il rilevamento senza rete, più debole (S110).

Rilevazione e integrità: l'agente Wazuh su tutti i PC, come vuole ADR-028, con Sysmon dove la build lo offre. Resta scoperto il blocco automatico di un EDR commerciale: la risposta attiva di Wazuh è spenta per scelta all'inizio, e Wazuh non sostituisce il motore antimalware.

Linux e NAS: ClamAV pianificato, FIM di Wazuh e AppArmor. Resta scoperta la scansione in tempo reale paragonabile a Defender.

Hardening: Lynis e i controlli di configurazione di Wazuh su Proxmox e sui PC Linux; HardeningKitty e gli stessi controlli di Wazuh su Windows. Si cambia qualcosa solo dopo una verifica in sola lettura, e Proxmox per ultimo.

Accessi: SSH con sole chiavi, già in ADR-025, più fail2ban; CrowdSec solo se un servizio verrà esposto. Resta il punto debole già dichiarato in ADR-025, cioè la postazione di amministrazione riconosciuta dal suo indirizzo.

Navigazione e DNS: AdGuard Home sul server, uBlock Origin nel browser. Resta scoperto il DNS cifrato dentro le applicazioni, che aggira il filtro; il blocco su OPNsense è possibile secondo conoscenza non verificata qui.

Credenziali, backup e cifratura: Vaultwarden con secondo fattore; restic verso il NAS più una copia fuori casa; BitLocker, LUKS e FileVault sui dischi. Restano da fare le prove di ripristino e da decidere dove tenere le chiavi di recupero.

Aggiornamenti: Windows Update e aggiornamenti automatici su Linux. LAP-03 con macOS Monterey non riceve più correzioni di sicurezza dalla fine del 2024 secondo una fonte secondaria (S123): va tenuto fuori dalla zona fidata o ritirato. La stessa verifica va fatta su Xperia III, su TAB-01 e TAB-02, i due Galaxy Tab S6 Lite, e su PC-01, il cui Windows 11 l'inventario dichiara installato forzando i requisiti, con il supporto agli aggiornamenti non verificato.

Telefoni e console: Play Protect, aggiornamenti del produttore e l'app Defender sugli Android; per PS5 e TV nessun agente è possibile, restano il filtro DNS e la zona di rete, già decisi.

Non coperto da nessuno strumento gratuito: il phishing nella posta fuori da Edge e Outlook, i dispositivi senza aggiornamenti, e il tempo di chi deve leggere gli allarmi, che è la risorsa più scarsa di un laboratorio domestico.

## Che cosa resta da verificare prima di decidere

La disponibilità in Italia e le funzioni attuali dell'app Defender nel piano Family; lo stato predefinito della protezione da manomissioni su Windows 11 Home; il risultato di Defender sulla pagina primaria di AV-Comparatives; la disponibilità di Sysmon integrato sulla build dei PC di casa; le licenze di tutti gli strumenti in tabella; le versioni lette con un riassunto, da ricontrollare sul dato grezzo; e se in casa esista un iPhone o un iPad, che l'inventario non elenca.

## Da dove si riparte

Il primo passo non costa nulla e non richiede il laboratorio acceso: irrigidire Defender su un PC Windows, con le regole ASR e le cartelle controllate in audit, e leggere dopo una settimana che cosa avrebbero bloccato. Il resto segue la roadmap: Wazuh, AdGuard Home e Vaultwarden arrivano con il server Proxmox, ClamAV con il NAS. La scelta finale, strumento per strumento, spetta all'utente.

[^1]: *ASR*, Attack Surface Reduction - regole di Defender che bloccano comportamenti tipici del malware invece di riconoscerne la firma.

[^2]: *EDR*, Endpoint Detection and Response - sorveglianza continua di un computer che registra processi, file e connessioni per scoprire e fermare un attacco in corso.

[^3]: *FIM*, File Integrity Monitoring - controllo che segnala quando un file importante cambia.

[^4]: *CIS*, Center for Internet Security - organizzazione che pubblica profili di configurazione sicura per sistemi operativi e programmi, i CIS Benchmark.
