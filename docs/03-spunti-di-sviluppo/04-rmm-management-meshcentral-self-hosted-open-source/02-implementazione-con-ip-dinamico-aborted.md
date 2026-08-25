# Implementazione con IP dinamico (aborted)

> PERCORSO ABBANDONATO, conservato come riferimento. L'ipotesi di esporre MeshCentral con IP pubblico dinamico e Dynamic DNS e' decaduta con l'assegnazione dell'IP statico da parte dell'operatore, confermata il 05/03/2026. L'analisi resta valida come descrizione dei limiti di un IP dinamico. Vedi ADR-004 in `.claude/memory/decisions.md`.

## Come funziona con l’IP dinamico

Se installo MeshCentral su un server nella LAN, lo connetto alla DMZ del firewall e uso quella connessione da fuori per me stesso con un opportuno dominio (magari comprato gratuito) è settabile? La soluzione è tecnicamente coerente e realizzabile: si può installare MeshCentral in DMZ o su VM interna, esporre le porte necessarie tramite NAT del firewall, e si punta un dominio verso l’IP pubblico tramite Dynamic DNS e connettersi da remoto. Tutto funziona per un uso personale e la perdita temporanea di sessioni dovuta a IP dinamico è accettabile.

Installando MeshCentral su un server interno alla LAN, si può posizionare nella DMZ virtuale del firewall OPNsense o comunque aprire solo le porte necessarie verso quel server, tipicamente HTTPS (443) per la gestione web e la comunicazione degli agenti. La DMZ in questo contesto serve a isolare il server dagli altri dispositivi della LAN, riducendo il rischio di compromissione se la porta esposta dovesse essere attaccata dall’esterno.

Dal punto di vista tecnico, la connessione da remoto verso MeshCentral avviene tramite il nome DNS del dominio che possiedi o che ottieni con un servizio Dynamic DNS (DNS dinamico). Il client esterno risolve sempre il nome in un indirizzo IP pubblico che il firewall NATta verso il server MeshCentral in DMZ. Se la WAN ha IP dinamico, il firewall aggiorna automaticamente il DNS tramite un client Dynamic DNS integrato in OPNsense. L’IP fisico della WAN cambia, ma il nome DNS rimane costante come punto di accesso. Le connessioni attive in corso perderanno temporaneamente la sessione quando cambia l’IP, ma questo non è un problema operativo per un utilizzo personale: basta riconnettersi semplicemente al nuovo IP tramite lo stesso dominio.

Lato sicurezza, si può limitare l’accesso al server MeshCentral esponendo solo le porte necessarie, abilitando HTTPS con certificato valido, usando autenticazione forte a due fattori per l’account amministrativo, e eventualmente limitando l’accesso in ingresso agli indirizzi IP dai quali prevedi di connetterti. Non c’è conflitto con avere più VM interne o un hypervisor; le VM restano isolate internamente e MeshCentral le gestisce come agent registrati; quindi, la natura dinamica dell’IP WAN resta l’unico limite per sessioni attive esterne.

## [TBC] Strutturare rete Docker e mapping porte in relazione alla DMZ di OPNsense

### Esempio case study con docker

Nel tuo case study concreto. Hai un host fisico con Proxmox. Sopra crei una VM Debian minimale. In quella VM installi Docker e docker-compose. Ora definisci uno stack chiamato ad esempio “meshcentral”. Nel file compose dichiari:

un servizio meshcentral basato su una specifica immagine con tag di versione preciso, ad esempio meshcentral:1.x.y, così eviti aggiornamenti impliciti; un volume persistente montato, ad esempio /opt/meshcentral-data, dove risiedono database, certificati TLS e configurazione; una rete docker bridge dedicata, isolata dagli altri container; le porte esposte verso la VM, tipicamente 443.

Quando fai “docker compose up -d”, l’intero stack viene creato in modo coerente. Se domani aggiorni versione, modifichi solo il tag dell’immagine nel file, rilanci il deploy, e Docker ricrea il container mantenendo intatti i volumi. Se qualcosa non funziona, ripristini il tag precedente e fai nuovamente deploy. Il rollback è deterministico perché il dato applicativo è separato dal codice dell’immagine.

Nel tuo contesto LAN domestico questo ha tre implicazioni operative concrete.

Primo, portabilità reale. Se cambi host fisico o VM, copi la directory contenente il file docker-compose.yml e i volumi persistenti su un nuovo server, installi Docker e rilanci lo stack. Non reinstalli MeshCentral manualmente, non ricrei utenti o certificati: riparti identico.

Secondo, coesistenza con altri servizi senza conflitti. Supponiamo che nella stessa VM tu voglia eseguire anche un reverse proxy Nginx o un servizio di monitoraggio come Zabbix. Con docker-compose puoi definire più servizi nello stesso file o in file separati, ciascuno con la propria rete e mappatura porte. Eviti conflitti di librerie Node.js, dipendenze di sistema o versioni OpenSSL perché ogni container è isolato a livello di filesystem e runtime.

Terzo, backup coerente. Il backup non è “backup dell’intera VM alla cieca”. Puoi fare snapshot Proxmox a livello VM, ma puoi anche fare backup applicativo mirato dei soli volumi persistenti. Questo riduce RPO e semplifica ripristini granulari.

Nel tuo scenario specifico, dove vuoi controllo remoto personale della LAN tramite MeshCentral, l’uso di docker-compose ti dà controllo di versione, ripetibilità e migrazione rapida senza cambiare architettura firewall o DNS. È una scelta tecnica coerente con l’idea di laboratorio evolutivo ma stabile.

### [TBC] aaaaaaaaaaaa

