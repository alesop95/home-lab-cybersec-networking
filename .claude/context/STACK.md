---
generated-from-commit: 86b5c8a61a55a48997d7757592aa4d91da9e8581
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - tools/**
  - docs/**
  - .claude/rules/**
last-verified-commit: ee63b19
---

# Stack del progetto

> Documento di recupero più importante: tracciato, perché chi clona deve vedere di che cosa è fatto questo repository e come lo si rimette in moto. Attenzione a una distinzione che qui conta più che altrove: lo stack del repository e lo stack del lab sono due cose diverse, e questa scheda le tiene separate.

## Che tipo di progetto è

Questo repository non contiene il software del lab: contiene la sua documentazione e gli strumenti che la producono e la verificano. Il codice presente è interamente strumentale, cioè serve a convertire, formattare e controllare documenti, non a far funzionare una rete. Il lab vero, quando esisterà, sarà fatto di apparati fisici e di sistemi installati su di essi, e questo repository ne sarà la descrizione.

## Stack del repository

Python 3 per tutti gli strumenti, senza gestore di pacchetti dedicato e senza ambiente virtuale: le dipendenze sono minime e si installano a livello di interprete. Gli strumenti in esercizio usano soltanto la libreria standard, quindi per lavorare sulla documentazione basta un interprete. Le due dipendenze esterne servono a strumenti ormai occasionali: `python-docx` al convertitore archiviato, `Pillow` al ridimensionamento delle fotografie. L'interprete verificato su questa macchina è Python 3.13.

Non esistono test automatici propri del progetto, con l'eccezione della suite che accompagna lo strumento di normalizzazione Markdown nel pacchetto di origine sotto `.claude/templates/md-unwrap/tests/`. La verifica del progetto è fatta dai controlli deterministici che `chiudi` esegue, più quello dell'albero, descritti nella scheda `dev-testing.md`. Alcuni strumenti portano un proprio autotest: il guard-rail, i tre correttori tipografici e la prova della loro catena.

## Gli strumenti e il loro ruolo architetturale

Gli strumenti in esercizio sono controlli o correttori: nessuno genera documentazione, perché dal 25/08/2026 la documentazione si scrive a mano. Dall'8/10/2026 quelli copiati dai pacchetti del template (ADR-022) li aggiorna `allinea-dal-template.py`. L'elenco completo, una riga per strumento, è nell'indice di `CLAUDE.md`; qui si descrivono quelli che reggono il flusso.

| File | Ruolo |
|---|---|
| `tools/check-docs-tree.py` | verifica che l'albero regga come struttura navigabile: nessun documento scollegato dagli indici, nessun collegamento relativo che punti nel vuoto |
| `tools/md-unwrap.py` | riunisce le righe di continuazione nei file Markdown, attuando la convenzione di un paragrafo per riga sorgente; rifiuta di scrivere se il rendering cambierebbe |
| `tools/lint-md-commands.py` | percorre i blocchi di shell nei file Markdown e segnala comandi spezzati su più righe, che `md-unwrap` per contratto non tocca |
| `tools/Test-Anonymization.py` | guard-rail: passa i file tracciati e quelli nuovi e segnala valori reali residui; è la versione del pacchetto del template con sei estensioni del progetto, registrata come adattata in `.claude/allineamento-risolti.json` |
| `tools/chiudi-sessione.ps1` | chiusura: esegue i controlli istanziati, committa, pubblica e registra l'impronta di ripresa; si lancia con `chiudi` |
| `tools/fix-accents.py` | con `fix-missing-accents.py` e `fix-dashes.py` attua le convenzioni tipografiche; in `chiudi` gira in sola verifica |
| `tools/verifica-schede.py` | segnala le schede di contesto superate rispetto alla loro ancora, e i `covers-paths` che non puntano a niente |
| `tools/source-register.py` | aggiorna e con `--check` verifica il blocco derivato di `SOURCES.md` che censisce i riferimenti pubblici citati nei documenti; non tocca le voci curate e non accede alla rete |

Accanto a questi vivono lo strumento archiviato e i file privati che alimentano il guard-rail.

| File | Ruolo |
|---|---|
| `tools/docx-to-md.py` | ha convertito il documento Word nell'albero; resta come strumento e come storia, ma si rifiuta di scrivere in una cartella priva del timbro `.generato-da-docx`, quindi non può sovrascrivere `docs/` |
| `tools/redactions.json` | privato, non versionato: le sostituzioni applicate nella prima stesura; oggi registro, non più meccanismo attivo |
| `tools/annotations.json` | storico: i banner iniettati durante la generazione, che ora sono testo dentro i file |
| `_notes/.anonymization-map.md` | privato: traduzione da segnaposto a valore reale |
| `_notes/.anonymization-patterns.json` | privato: alimenta il guard-rail, che senza di esso si ferma invece di dare verde |

Il flusso che li lega è lineare e va ricordato in quest'ordine: si modifica un file, si verifica la coerenza dell'albero, si normalizza la formattazione, si controllano i blocchi di comando, si lanciano i controlli di `chiudi`, fra cui il guard-rail e i correttori tipografici in verifica, e solo allora si committa con `chiudi`.

## Stack del lab, come progettato

Nessuno di questi componenti è in esercizio, tranne dove indicato. La colonna dello stato dice esattamente a che punto è ciascuno.

| Componente | Scelta | Stato |
|---|---|---|
| Terminazione ottica | ONT dell'operatore, Zyxel PM5100-T1 | in esercizio, fornito e gestito dall'operatore |
| Apparato di frontiera | modem dell'operatore, con Wi-Fi 7 e fonia VoIP | in esercizio, non sostituibile |
| Firewall e router interno | OPNsense 25.7 su x86 dedicato | sistema installato il 16/01/2026, non configurato |
| Hardware del firewall | i3 di settima generazione, 8 GB RAM, SSD SATA 120 GB, NIC integrata 1 GbE più due TP-Link TX201 a 2,5 Gbps su chipset Realtek RTL8125B | assemblato |
| Switch | Zyxel XMG1915-10EP, managed, 8 porte 2,5 GbE PoE++ con budget di 130 W più 2 SFP+ a 10 Gbps (ADR-017) | deciso il 07/10/2026, non acquistato |
| Access point | due AP Zyxel NWA130BE Wi-Fi 7, tre bande, 802.1X/RADIUS e SNMP, cablati e alimentati dallo switch al terzo e al secondo piano, con roaming fra i due (ADR-018, ADR-024) | decisi, cavi posati, non acquistati |
| Console di gioco | PS5 su una porta LAN da 1 GbE del modem, fuori dal perimetro, con un NAT solo (ADR-018) | collocazione decisa |
| Virtualizzazione | Proxmox previsto su linux-desktop-A,i7-7700,16GB DDR4 censiti,due NVMe1TB in specchio; precedente24GB sospeso | montaggio/installazione non confermati; riferimento allocazione12 eADR-039 |
| Gestione endpoint | MeshCentral self-hosted, in container | pianificato |
| DNS interno | Unbound su OPNsense nella fase iniziale, poi AdGuard Home su un host sempre acceso come motore di policy davanti a Unbound, secondo lo studio del 22/09/2026; il documento sorgente proponeva Pi-hole nello stesso ruolo | pianificato |
| Monitoraggio | Wazuh con il proprio indicizzatore, su Proxmox; Suricata integrato in OPNsense; plugin os-wazuh-agent; syslog per gli apparati | deciso l'8/10/2026 (ADR-028), non installato |
| Storage di rete | TrueNAS25.10.7 su H170-PRO/i7-6700, RAM-03/A2 da8GB e obiettivo16GB aperto; Kingston avvio, tank su mirror SanDisk/WD | tank Online no errors e213.19GiB utilizzabili alla creazione; documenti cifrato creato29/10, Unlocked e Not Shared; chiave JSON e terzo export con seed post-dataset acquisiti e verificati, due precedenti conservati; ACL Type SMB/NFSv4 e Mode Restricted letti su documenti, prossimo utente/ACL/share; rete definitiva, copia indipendente e recuperi aperti, ADR-033/039/043/044 |
| VPN | WireGuard per gestione secondo ADR-025; Tailscale richiesto per accesso domestico e assistente, ADR-045; NordVPN spenta a casa e Meshnet condivisa esclusa, ADR-046 | nessun tunnel domestico o subnet router collaudato; studio18 recepisce i vincoli dell’account commerciale senza modificare telefono o rete |
| Backup | agente di backup incrementale su disco esterno, con copia su due servizi cloud diversi | parzialmente in uso |

## Alternative deliberatamente escluse

Sono decisioni già prese, e riaprirle senza un fatto nuovo è spreco di tempo. Il razionale esteso di ciascuna sta nel registro delle decisioni.

Un mini-PC generico di importazione come piattaforma firewall è stato scartato per assenza di garanzie su firmware, aggiornamenti e componentistica, che in un apparato di sicurezza sono il punto di rottura. pfSense è stato scartato a favore di OPNsense per la governance e il ritmo di rilascio. IPFire è stato confrontato in dettaglio e scartato per prestazioni meno prevedibili in NAT intensivo e integrazione dei servizi meno ricca. NethSecurity è stato citato e non valutato. Lo switch MikroTik CRS310 è stato scartato perché il suo routing di livello 3 non serve in una topologia dove il firewall è l'unico punto di decisione, e costa di più. Lo switch Ubiquiti USW-Flex-2.5G-5 è stato scartato perché la sua gestione dipende da un controller esterno, cioè introduce una dipendenza infrastrutturale che una rete domestica non ha motivo di assumere. L'uso di una live Linux per mappare le schede di rete è stato abbandonato a favore della console del firewall, per non introdurre un secondo stack di driver diverso da quello che governerà il traffico reale. L'esposizione di servizi con IP pubblico dinamico e DNS dinamico è decaduta con l'assegnazione dell'indirizzo statico. Un router di terze parti come un FRITZ!Box è stato scartato il 07/10/2026 (ADR-018): dietro il modem aggiungerebbe una terza traduzione, al suo posto richiederebbe una configurazione libera della linea che qui non è validata.

## Vincoli che nessuna scelta tecnica può aggirare

Il modem non espone bridge né passthrough, e per questa linea l'assistenza ha escluso il collegamento diretto del firewall all'ONT; la documentazione pubblica dell'operatore non prova un vincolo MAC generale dell'ONT, quindi l'evidenza resta locale e non si generalizza. Ne discende che il doppio NAT è strutturale e che la Wi-Fi del modem resta fuori dal firewall finché non la si sostituisce con access point a valle. L'indirizzo pubblico statico, ottenuto senza costi su una linea residenziale, è ciò che rende sensato esporre un servizio dalla DMZ; è un dato di contratto, non una proprietà dell'apparato, e va trattato come tale.

La scelta dello storage è motivata nel [confronto TrueNAS/OMV](../../docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/08-valutazione-openmediavault.md), aggiornato il28/10/2026: preferenza per la gestione integrata ZFS, OMV con ZFS come alternativa valida. I precedenti32GB e lo specchio di avvio non descrivono la configurazione attuale e non ne motivano più la scelta. Nessun confronto di consumi o prestazioni eseguito.

## Assistente personale, direzione del29/10/2026

Hermes, Nix/NixOS, Tailscale e archivio personale Markdown/Obsidian sono raggruppati nello [studio17](../../docs/03-spunti-di-sviluppo/23-studio-home-lab/17-assistente-personale-hermes-nix-e-memoria.md), ADR-045. Modello inizialmente remoto come ipotesi dell’handoff; Opus5.5 verificato come prodotto, compatibilità/provider non provati. Hardware a basso consumo da misurare, nessun SBC assegnato. Pacchetti hermes-agent e knowledge-wiki già nel catalogo, non istanziati qui. Capacità brain futura nel template; chiedere Jev quando sarà recepita. Nessun bot, vault personale, account, installazione o percorso di rete configurati.

## Estensione in studio del29/10/2026

Studi19/20/21 nell’area home-lab: firmware MCU distinto da host Linux Hermes, browser didattici, Wi-Fi con SSID per zona, governo sicurezza e piano di aggiornamento OPNsense. Sono candidati e requisiti, senza nuovi servizi in esercizio. Istanziate le skill testuali iso27001/gdpr-compliance dal pacchetto grc-skills v2.1.0; ponte AGENTS e wrapper Codex verificati. Nessun server MCP o agente remoto aggiunto.
