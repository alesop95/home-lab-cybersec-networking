---
generated-from-commit: 86b5c8a61a55a48997d7757592aa4d91da9e8581
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - tools/**
  - scripts/**
  - docs/**
  - .claude/rules/**
last-verified-commit: 6769dc4
---

# Stack del progetto

> Documento di recupero più importante: tracciato, perché chi clona deve vedere di che cosa è fatto questo repository e come lo si rimette in moto. Attenzione a una distinzione che qui conta più che altrove: lo stack del repository e lo stack del lab sono due cose diverse, e questa scheda le tiene separate.

## Che tipo di progetto è

Questo repository non contiene il software del lab: contiene la sua documentazione e gli strumenti che la producono e la verificano. Il codice presente è interamente strumentale, cioè serve a convertire, formattare e controllare documenti, non a far funzionare una rete. Il lab vero, quando esisterà, sarà fatto di apparati fisici e di sistemi installati su di essi, e questo repository ne sarà la descrizione.

## Stack del repository

Python 3 per tutti gli strumenti, senza gestore di pacchetti dedicato e senza ambiente virtuale: le dipendenze sono minime e si installano a livello di interprete. I quattro controlli in esercizio usano soltanto la libreria standard, quindi per lavorare sulla documentazione basta un interprete. Le due dipendenze esterne servono a strumenti ormai occasionali: `python-docx` al convertitore archiviato, `Pillow` al ridimensionamento delle fotografie. L'interprete verificato su questa macchina è Python 3.13.

Non esistono test automatici propri del progetto, con l'eccezione della suite che accompagna lo strumento di normalizzazione Markdown nel pacchetto di origine sotto `.claude/templates/md-unwrap/tests/`. La verifica del progetto è fatta da quattro controlli deterministici, descritti nella scheda `dev-testing.md`.

## Gli strumenti e il loro ruolo architetturale

Gli strumenti in esercizio sono quattro, e sono tutti controlli: nessuno genera più documentazione, perché dal 25/08/2026 la documentazione si scrive a mano.

| File | Ruolo |
|---|---|
| `tools/check-docs-tree.py` | verifica che l'albero regga come struttura navigabile: nessun documento scollegato dagli indici, nessun collegamento relativo che punti nel vuoto |
| `tools/md-unwrap.py` | riunisce le righe di continuazione nei file Markdown, attuando la convenzione di un paragrafo per riga sorgente; rifiuta di scrivere se il rendering cambierebbe |
| `tools/lint-md-commands.py` | percorre i blocchi di shell nei file Markdown e segnala comandi spezzati su più righe, che `md-unwrap` per contratto non tocca |
| `tools/Test-Anonymization.py` | guard-rail: passa i file tracciati e segnala valori reali residui; è l'ultimo controllo prima di un commit di documentazione |
| `tools/source-register.py` | aggiorna e con `--check` verifica il blocco derivato di `SOURCES.md` che censisce i riferimenti pubblici citati nei documenti; non tocca le voci curate e non accede alla rete |

Accanto a questi vivono lo strumento archiviato e i file privati che alimentano il guard-rail.

| File | Ruolo |
|---|---|
| `tools/docx-to-md.py` | ha convertito il documento Word nell'albero; resta come strumento e come storia, ma si rifiuta di scrivere in una cartella priva del timbro `.generato-da-docx`, quindi non può sovrascrivere `docs/` |
| `tools/redactions.json` | privato, non versionato: le sostituzioni applicate nella prima stesura; oggi registro, non più meccanismo attivo |
| `tools/annotations.json` | storico: i banner iniettati durante la generazione, che ora sono testo dentro i file |
| `_notes/.anonymization-map.md` | privato: traduzione da segnaposto a valore reale |
| `_notes/.anonymization-patterns.json` | privato: alimenta il guard-rail, che senza di esso si ferma invece di dare verde |

Il flusso che li lega è lineare e va ricordato in quest'ordine: si modifica un file, si verifica la coerenza dell'albero, si normalizza la formattazione, si controllano i blocchi di comando, si esegue il guard-rail di anonimizzazione, e solo allora si committa.

## Stack del lab, come progettato

Nessuno di questi componenti è in esercizio, tranne dove indicato. La colonna dello stato dice esattamente a che punto è ciascuno.

| Componente | Scelta | Stato |
|---|---|---|
| Terminazione ottica | ONT dell'operatore, Zyxel PM5100-T1 | in esercizio, fornito e gestito dall'operatore |
| Apparato di frontiera | modem dell'operatore, con Wi-Fi 7 e fonia VoIP | in esercizio, non sostituibile |
| Firewall e router interno | OPNsense 25.7 su x86 dedicato | sistema installato il 16/01/2026, non configurato |
| Hardware del firewall | i3 di settima generazione, 8 GB RAM, SSD SATA 120 GB, NIC integrata 1 GbE più due TP-Link TX201 a 2,5 Gbps su chipset Realtek RTL8125B | assemblato |
| Switch | Zyxel XMG1915, managed, 8 porte 2,5 GbE più 2 SFP+ a 10 Gbps: variante 10EP con PoE per due o tre AP come candidato principale, variante 10E senza PoE con un iniettore se l'AP resta uno | scelta fra le due varianti aperta dal 22/09/2026, non acquistato |
| Access point | due o tre AP Zyxel Wi-Fi 7, NWA50BE Pro o NWA130BE, alimentati dallo switch | ipotizzato |
| Virtualizzazione | Proxmox VE, edizione gratuita | pianificato |
| Gestione endpoint | MeshCentral self-hosted, in container | pianificato |
| DNS interno | Pi-hole come motore di policy davanti a Unbound come resolver ricorsivo con DNSSEC | pianificato |
| Monitoraggio | Wazuh al centro, Snort per il traffico, stack ELK per l'indicizzazione | pianificato |
| Storage di rete | TrueNAS SCALE su hardware proprio ricavato da quattro desktop dismessi; unico pool sui due NVMe da 1 TB in specchio, senza dischi meccanici (ADR-014, ADR-015); alimentatore della base tenuto con condizioni di accettazione (ADR-016) | in assemblaggio: prelievi chiusi il 07/10/2026, montaggio fermo in attesa dell'adattatore da PCIe a M.2 per il secondo NVMe |
| VPN | Tailscale per la semplicità, oppure Pritunl per il controllo | in valutazione, nessuna delle due adottata |
| Backup | agente di backup incrementale su disco esterno, con copia su due servizi cloud diversi | parzialmente in uso |

## Alternative deliberatamente escluse

Sono decisioni già prese, e riaprirle senza un fatto nuovo è spreco di tempo. Il razionale esteso di ciascuna sta nel registro delle decisioni.

Un mini-PC generico di importazione come piattaforma firewall è stato scartato per assenza di garanzie su firmware, aggiornamenti e componentistica, che in un apparato di sicurezza sono il punto di rottura. pfSense è stato scartato a favore di OPNsense per la governance e il ritmo di rilascio. IPFire è stato confrontato in dettaglio e scartato per prestazioni meno prevedibili in NAT intensivo e integrazione dei servizi meno ricca. NethSecurity è stato citato e non valutato. Lo switch MikroTik CRS310 è stato scartato perché il suo routing di livello 3 non serve in una topologia dove il firewall è l'unico punto di decisione, e costa di più. Lo switch Ubiquiti USW-Flex-2.5G-5 è stato scartato perché la sua gestione dipende da un controller esterno, cioè introduce una dipendenza infrastrutturale che una rete domestica non ha motivo di assumere. L'uso di una live Linux per mappare le schede di rete è stato abbandonato a favore della console del firewall, per non introdurre un secondo stack di driver diverso da quello che governerà il traffico reale. L'esposizione di servizi con IP pubblico dinamico e DNS dinamico è decaduta con l'assegnazione dell'indirizzo statico.

## Vincoli che nessuna scelta tecnica può aggirare

Il modem non espone bridge né passthrough, e per questa linea l'assistenza ha escluso il collegamento diretto del firewall all'ONT; la documentazione pubblica dell'operatore non prova un vincolo MAC generale dell'ONT, quindi l'evidenza resta locale e non si generalizza. Ne discende che il doppio NAT è strutturale e che la Wi-Fi del modem resta fuori dal firewall finché non la si sostituisce con access point a valle. L'indirizzo pubblico statico, ottenuto senza costi su una linea residenziale, è ciò che rende sensato esporre un servizio dalla DMZ; è un dato di contratto, non una proprietà dell'apparato, e va trattato come tale.
