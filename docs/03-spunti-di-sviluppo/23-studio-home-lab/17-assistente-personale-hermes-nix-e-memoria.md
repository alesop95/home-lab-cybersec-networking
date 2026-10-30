# Assistente personale: Hermes, Nix, Tailscale e memoria consultabile

Studio aperto il29/10/2026 su richiesta esplicita dell’utente. Raggruppa materiali già presenti e nuove direzioni; non certifica un assistente installato. Il file handoff consegnato è letto e archiviato integralmente nel livello privato con impronta SHA-256, originale conservato. Il futuro sviluppo del template è una dipendenza da recepire, non una modifica da eseguire ora in quel repository.

## Risultato desiderato e stato

Un assistente personale raggiungibile anche fuori casa, residente su un computer sempre acceso dal consumo minimo misurabile. Lo studio prende Hermes come agente, Nix/NixOS come percorso dichiarativo da valutare, Tailscale per l’accesso domestico e un archivio personale consultabile con Obsidian. Il modello inizialmente remoto è l’ipotesi dell’handoff; il precedente [studio del modello locale su CPU](13-modello-linguistico-locale-su-cpu.md) resta un esperimento distinto e può fornire in futuro un altro backend.

ADR-045 registra queste direzioni e aggiorna il precedente ruolo di Tailscale come sola alternativa. Non sono ancora scelti hardware, provider, credenziali, budget, host, subnet pubblicizzate o policy. Nessun account, bot, servizio o acquisto è stato creato da questo studio. «Jev» è la denominazione riportata dall’utente ma non ancora identificata: su sua indicazione del29/10, chiederne nome/link quando il template avrà recepito l’impianto del brain, senza riaprire ora la domanda.

## I materiali già esistenti convergono qui

| Materiale | Cosa riutilizziamo | Limite da conservare |
|---|---|---|
| [Accesso remoto](06-accesso-remoto-vpn.md) e [accesso amministrativo](09-accesso-amministrativo.md) | confronto WireGuard/Tailscale, host sempre acceso, confini della gestione | vecchia esclusione Tailscale aggiornata da ADR-045; nessuna nuova rotta applicata |
| [Cloudflare e alternative](15-cloudflare-zero-trust-e-alternative.md), [matrice dei bisogni](16-bisogni-controlli-e-flussi.md) | accesso a servizi, amministrazione, DNS e uscita Internet come bisogni distinti | Cloudflare non viene adottato per effetto di questo filone |
| [Allocazione hardware](12-allocazione-dell-hardware.md), [energia NAS](../02-storage-di-rete-nas/05-consumo-elettrico-e-finestra-di-accensione.md) | inventario e finestra NAS | nessun Raspberry assegnato; NAS a orario inadatto come unica sede dell’assistente residente |
| [Piano di backup](../05-strategia-di-backup/02-piano-di-backup-e-ripristino-del-lab.md) | inventario dei dati, copie e verbale di recupero | esportare una configurazione non salva automaticamente conversazioni e archivio personale |
| Pacchetto template hermes-agent | agente residente, gateway e attività programmate | presente nel catalogo, non installato o collaudato qui; costi del provider e manutenzione separati |
| Pacchetto template knowledge-wiki | schema, fonti conservate, pagine collegate, indice e registro | il lab ha già la propria memoria nativa: evitare una seconda knowledge base concorrente nel repository |
| Handoff Nix locale | percorso proposto per NixOS, Telegram, backend terminale e Tailscale | proposta di agosto2026, da correggere e verificare prima dell’esecuzione |

Il catalogo del template è stato consultato in sola lettura, anche nella sede indicata dall’utente. Nessun pacchetto aggiuntivo è stato istanziato. Il raccordo futuro deve importare una capacità mantenuta dal template, conservando qui solo configurazione e decisioni specifiche del lab.

## Componenti e confini

| Componente | Funzione nel disegno | Cosa richiede separatamente |
|---|---|---|
| Hermes | riceve richieste, usa strumenti, conserva stato operativo | identità di servizio, ambito file/rete, aggiornamenti, backup del suo stato |
| Modello, incluso Claude Opus5.5 da studiare | genera risposte e decide i passi consentiti attraverso l’agente | provider compatibile, autenticazione ammessa, costo e verifica delle risposte |
| Archivio Markdown e Obsidian | contenuti personali leggibili e navigabili | schema, fonti, revisione, versione privata, backup e sincronizzazione |
| Nix / NixOS | descrive pacchetti e, con NixOS, servizi e sistema | lock delle versioni, configurazione hardware, segreti e dati persistenti |
| Tailscale | collega i dispositivi autorizzati e, se necessario, reti domestiche selezionate | identità, policy e routing collaudati |
| Telegram | interfaccia proposta dall’handoff per dialogare con l’assistente | bot e mittenti autorizzati; il canale non è una VPN per l’intera casa |

Hermes dichiara integrazioni di messaggistica, memoria persistente, strumenti e pianificazione, S250. Queste capacità non provano né qualità delle risposte né autorizzazione a modificare il lab. La memoria operativa dell’assistente è un dato applicativo privato; la memoria versionata di questo progetto resta la fonte dello stato del lab. Non si abilita memoria nascosta globale di Codex o Claude per effetto di questa proposta.

## Hardware a basso consumo: prima il ruolo, poi la scheda

Con inferenza remota il computer di casa esegue soprattutto gateway, strumenti e archivio. La documentazione Hermes include Linux e container su x86-64 e aarch64, S251: è una base per valutare un SBC ARM64, non una certificazione di ogni modello Raspberry o accessorio. Un microcontrollore generico non è la piattaforma Linux prevista per questo stack; può avere altri ruoli periferici nel lab.

| Candidato | Perché valutarlo | Dato che decide |
|---|---|---|
| VM su host già acceso tutto il giorno | riuso senza nuova macchina | incremento reale dei watt e disponibilità continua dell’host; se si accende il server solo per l’agente va conteggiato tutto il consumo aggiunto |
| SBC ARM64, incluso Raspberry compatibile | nodo piccolo e indipendente | supporto distribuzione/Nix, RAM sotto carico, affidabilità del supporto dati, alimentazione, rete e potenza totale |
| Mini PC x86 efficiente | compatibilità e SSD ordinario | confronto alla presa con SBC e VM sul medesimo carico, inclusi alimentatore e periferiche |

Nessun valore in watt, modello da comprare o vincitore è ancora misurato. Per un servizio24/7, ogni watt medio corrisponde a8,76kWh/anno: la potenza totale media, non il solo TDP della CPU, alimenta il calcolo. La misura deve coprire attesa, messaggi con chiamata al modello e attività con strumenti. Un’esperienza più lenta può tenere la macchina occupata più a lungo; confronto energetico e qualità del servizio vanno letti insieme. I4GB citati nell’handoff sono un’ipotesi iniziale, da verificare sul carico selezionato.

Non si riutilizzano nel NAS i moduli RAM esclusi dai test per finanziare questa idea. Non si cambia l’inventario fisico finché una macchina non è realmente destinata al ruolo.

## Nix e NixOS: che cosa adottare dello handoff

Nix è il gestore e sistema di costruzione; NixOS è una distribuzione che usa configurazione dichiarativa per il sistema, S253. Hermes fornisce flake e moduli NixOS/Home Manager, ma li classifica Tier2, best effort; il ramo main può romperli, S252. Quindi NixOS è una direzione di studio autorizzata, non una piattaforma già validata. Confrontare un modulo ufficiale fissato a una revisione funzionante con una distribuzione Linux supportata e container; il modulo comunitario dell’handoff non diventa preferito soltanto perché contiene più esempio.

Prima di eseguire il piano vanno separati configurazione dichiarativa, lock delle dipendenze, segreti e stato modificabile. Un rollback di generazione ripristina l’ambiente selezionato, non riporta automaticamente indietro database, conversazioni o documenti scritti dopo. La persistenza dei dati richiede un inventario e una copia coerente, S254. Non mettere chiavi in file Nix pubblici o nello store come testo leggibile; il meccanismo privato di consegna dei segreti va definito al collaudo.

Il progetto deve conservare una revisione provata di configurazione e dipendenze, identificare che cosa viene scaricato, poi dimostrare riavvio e recupero. La dichiaratività riduce differenze accidentali fra installazioni; non promette ogni build identica né aggiornamenti privi di regressioni.

## Tailscale e Telegram rispondono a due bisogni diversi

La richiesta dell’utente promuove Tailscale a direzione di progetto per l’accesso remoto a casa, ADR-045. Primo caso da studiare: peer diretto sul nodo dell’assistente. Un subnet router serve per apparati domestici senza client, con sole destinazioni motivate. Approvare una rotta e autorizzare il relativo traffico sono meccanismi distinti, S255; le regole OPNsense e l’eventuale source NAT vanno verificati sul percorso concreto. Nessuna pubblicizzazione indistinta di VLAN, gestione, ospiti, IoT o laboratorio e nessun exit node automatico.

ADR-025 continua a descrivere i percorsi amministrativi già progettati, incluso WireGuard su OPNsense. La sua esclusione assoluta di Tailscale come futura opzione è superata dal nuovo requisito; il dettaglio di un eventuale ingresso di gestione deve ancora aggiornare la tabella09 e superare la prova dei flussi. L’assistente non riceve diritti di amministrazione soltanto perché il suo host è raggiungibile via Tailscale. Se il nodo ospitasse anche routing, distinguere i privilegi del router da quelli del processo Hermes; preferire ruoli isolati quando il disegno concreto lo permette.

Per Telegram, Hermes documenta polling in uscita come default e webhook come alternativa, S256. Il polling evita di esporre per quel bot un server HTTPS in ingresso; richiede comunque uscita consentita da firewall e provider. L’accesso ai servizi domestici via Tailscale è un altro percorso. Telegram non dimostra il funzionamento della VPN e un tunnel Tailscale attivo non dimostra che i mittenti del bot siano limitati.

## Un brain leggibile: Obsidian, fonti e modello

La proposta LLM Wiki dell’Autore-Wiki-A, S257, separa fonti conservate, pagine Markdown sintetizzate e schema operativo. La conoscenza accumula collegamenti e contraddizioni invece di lasciare ogni conclusione soltanto nella chat. Il catalogo knowledge-wiki già presente traduce questo schema in una capacità del template. Qui si studia come usarlo per un archivio personale privato, evitando di duplicare lo stato canonico del lab.

Obsidian legge un vault di normali file Markdown e registra preferenze nella cartella `.obsidian`, S258. È quindi una vista utile sui contenuti, indipendente dal modello usato per aggiornarli. La sincronizzazione fra PC e nodo residente va scelta: due scrittori simultanei possono produrre conflitti, e sincronizzare non equivale a conservare versioni recuperabili. In prima prova proporre un solo scrittore dell’archivio compilato e accesso limitato alle fonti selezionate; lo schema deve conservare provenienza, data, stato di verifica e registro delle modifiche.

Claude Opus5.5 esiste nell’annuncio ufficiale Anthropic del22/09/2026, S259. Si registra come modello da studiare, separato dal formato della memoria. Non è dimostrato qui che un abbonamento esistente lo autorizzi in Hermes, né che il relativo metodo di accesso sia compatibile: autenticazione, costi e trattamento dei contenuti vanno verificati nel canale scelto. La base di conoscenza deve sopravvivere al cambio di modello o applicazione.

Il lavoro futuro nel template aggiungerà l’impianto del brain. Quando quella capacità sarà disponibile, la ripresa deve chiedere all’utente l’identificazione di «Jev», rileggere il pacchetto aggiornato e decidere il raccordo. Il promemoria è legato a questa tappa, non a una data inventata. Nessun vault personale viene importato nel repository pubblico e nessuna cartella personale viene letta senza la richiesta specifica prevista dalle regole di progetto.

## Correzioni dello handoff prima del collaudo

Il documento consegnato resta una fonte locale di intenzioni, non un runbook da lanciare automaticamente. Le sue frasi assolute su uscita attraverso NAT, hash e rollback devono essere sostituite da verifiche concrete. Uscita Internet dipende dalle regole; la riproducibilità dipende anche da input e lock; il rollback non salva lo stato applicativo.

Il backend terminale in container richiede limiti su montaggi, rete e privilegi. Non vale la promessa che qualunque danno resti automaticamente nel container; Docker documenta privilegi equivalenti a root per l’accesso al suo gruppo, S260. Non si consegna il socket del motore all’agente senza un bisogno e un isolamento specifici. Restano da verificare i requisiti del backend della revisione Hermes scelta.

Provider, canone, soglie del piano Tailscale e comandi d’installazione dell’handoff non sono assunti attuali. Il link breve Nix è stato recuperato via curl dopo il fallimento del lettore web: il corpo è la homepage ufficiale nixos.org, titolo e canonical verificati. I rinvii Reddit/Discord presenti nell’handoff non sono stati letti autonomamente e non sostengono conclusioni di questa scheda. Le fonti ufficiali S250-S260 sostengono il primo studio; non si dichiara una revisione esaustiva di tutti i link dell’handoff.

## Sequenza proposta e prove che chiudono il filone

1. Recezione della futura capacità nel template; identificazione di «Jev» a quella tappa. Definire un primo compito concreto e un piccolo corpus personale autorizzato.
2. Prototipo su host disponibile, prima di acquistare hardware. Verificare revisione Hermes, percorso Nix o container, provider e costo; fissare la configurazione funzionante.
3. Telegram privato con mittenti limitati e accesso Tailscale al solo servizio necessario. Dimostrare da rete mobile una richiesta ammessa e il rifiuto di mittente/destinazione non autorizzati.
4. Compito ripetibile su fonti conservate: risposta con provenienza controllabile, aggiornamento della wiki, ripresa dopo riavvio senza perdita dello stato atteso. Misurare tempo, RAM, energia alla presa e costo del modello sullo stesso compito.
5. Copia separata di configurazione, lock, vault, stato Hermes e materiali segreti con custodia privata. Ripristinare su ambiente sostitutivo, verificando una conversazione e una nota già presenti prima del guasto simulato.
6. Solo con misure confrontabili scegliere VM, SBC o mini PC; estendere poi gli accessi domestici per bisogno. NAS spento nella sua finestra non deve fermare dialogo e accesso remoto di base.

Le prove sono future: non si etichetta «funzionante» un insieme di pacchetti installabili. La [scheda didattica09](../../../.claude/context/refactor-09-assistente-e-memoria-personale.md) spiega il passaggio dai nomi degli strumenti ai confini del sistema; il punto operativo NAS resta distinto e conservato nella memoria di progetto.

## Raccordo con il rapporto sull’account NordVPN

ADR-046 e [studio18](18-nordvpn-account-condiviso-e-confini-domestici.md),29/10/2026: NordVPN resta spenta a casa e Meshnet esclusa con l’identità condivisa. Il futuro assistente non riceve quell’account né un accesso remoto da quel gruppo. Tailscale di ADR-045 rimane la direzione richiesta per il filone; nessuna rotta, exit node o nuova identità configurati. Su Android il passaggio fra applicazioni VPN va verificato sul profilo, senza presumere tunnel simultanei. Promemoria Jev ancora alla tappa del template.

## Raccordo del29/10: nodi piccoli e host dell’agente

Lo [studio19](19-microcontrollori-microserver-e-laboratorio-browser.md) distingue firmware MCU, Linux per Hermes e inferenza remota; apre laboratorio browser e misura energetica. La preferenza Wi-Fi si attua con SSID associati a VLAN40 per IoT e VLAN30 per servizi, senza accesso generale a NAS/gestione. Lo [studio20](20-governo-sicurezza-e-privacy-domestiche.md) raccoglie rischi e flussi personali. Nessuna macchina già assegnata, nessun Pico audio contato come disponibile. Jev resta da identificare alla recezione del brain nel template.
