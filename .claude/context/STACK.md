---
generated-from-commit: e89779723cb1ed715b781763011255a81a82700e
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - tools/**
  - scripts/**
  - docs/**
  - .claude/rules/**
last-verified-commit: e89779723cb1ed715b781763011255a81a82700e
---

# Stack del progetto

> Documento di recupero piu' importante: tracciato, perche' chi clona deve vedere di che cosa e' fatto questo repository e come lo si rimette in moto. Attenzione a una distinzione che qui conta piu' che altrove: lo stack del repository e lo stack del lab sono due cose diverse, e questa scheda le tiene separate.

## Che tipo di progetto e'

Questo repository non contiene il software del lab: contiene la sua documentazione e gli strumenti che la producono e la verificano. Il codice presente e' interamente strumentale, cioe' serve a convertire, formattare e controllare documenti, non a far funzionare una rete. Il lab vero, quando esistera', sara' fatto di apparati fisici e di sistemi installati su di essi, e questo repository ne sara' la descrizione.

## Stack del repository

Python 3 per tutti gli strumenti, senza gestore di pacchetti dedicato e senza ambiente virtuale: le dipendenze sono minime e si installano a livello di interprete. L'unica dipendenza esterna e' `python-docx`, usata dal convertitore per leggere il documento Word; tutto il resto usa la libreria standard. L'interprete verificato su questa macchina e' Python 3.13 con `python-docx` 1.2.0.

Non esistono test automatici propri del progetto, con l'eccezione della suite che accompagna lo strumento di normalizzazione Markdown nel pacchetto di origine sotto `.claude/templates/md-unwrap/tests/`. La verifica del progetto e' fatta da tre controlli deterministici, descritti nella scheda `dev-testing.md`.

## Gli strumenti e il loro ruolo architetturale

| File | Ruolo |
|---|---|
| `tools/docx-to-md.py` | converte il documento sorgente nell'albero `docs/`, applica le redazioni e produce il report di conversione; e' il generatore di quasi tutta la documentazione |
| `tools/redactions.json` | sidecar privato, non versionato: le sostituzioni che anonimizzano il testo e i titoli in fase di generazione |
| `tools/annotations.json` | banner curati iniettati nei file generati; e' l'unico modo lecito di aggiungere testo dentro l'albero generato |
| `tools/md-unwrap.py` | riunisce le righe di continuazione nei file Markdown, attuando la convenzione di un paragrafo per riga sorgente; rifiuta di scrivere se il rendering cambierebbe |
| `tools/lint-md-commands.py` | percorre i blocchi di shell nei file Markdown e segnala comandi spezzati su piu' righe, che `md-unwrap` per contratto non tocca |
| `scripts/Test-Anonymization.py` | guard-rail: passa i file tracciati e segnala valori reali residui; e' l'ultimo controllo prima di un commit di documentazione |
| `_notes/.anonymization-map.md` | privato: traduzione da segnaposto a valore reale |
| `_notes/.anonymization-patterns.json` | privato: alimenta il guard-rail, che senza di esso si ferma invece di dare verde |

Il flusso che li lega e' lineare e va ricordato in quest'ordine: si modifica il documento sorgente, si rigenera l'albero con il convertitore, si normalizzano i Markdown scritti a mano con `md-unwrap`, si controllano i blocchi di comando con il linter, si esegue il guard-rail di anonimizzazione, e solo allora si committa.

## Stack del lab, come progettato

Nessuno di questi componenti e' in esercizio, tranne dove indicato. La colonna dello stato dice esattamente a che punto e' ciascuno.

| Componente | Scelta | Stato |
|---|---|---|
| Terminazione ottica | ONT dell'operatore, Zyxel PM5100-T1 | in esercizio, fornito e gestito dall'operatore |
| Apparato di frontiera | modem dell'operatore, con Wi-Fi 7 e fonia VoIP | in esercizio, non sostituibile |
| Firewall e router interno | OPNsense 25.7 su x86 dedicato | sistema installato il 16/01/2026, non configurato |
| Hardware del firewall | i3 di settima generazione, 8 GB RAM, SSD SATA 120 GB, NIC integrata 1 GbE piu' due TP-Link TX201 a 2,5 Gbps su chipset Realtek RTL8125B | assemblato |
| Switch | Zyxel XMG1915-10E, managed L2, 8 porte 2,5 GbE piu' 2 SFP+ a 10 Gbps, senza PoE | scelto, non acquistato |
| Access point | modello Wi-Fi 7 alimentato via iniettore PoE Cudy PoE200H | ipotizzato |
| Virtualizzazione | Proxmox VE, edizione gratuita | pianificato |
| Gestione endpoint | MeshCentral self-hosted, in container | pianificato |
| DNS interno | Pi-hole come motore di policy davanti a Unbound come resolver ricorsivo con DNSSEC | pianificato |
| Monitoraggio | Wazuh al centro, Snort per il traffico, stack ELK per l'indicizzazione | pianificato |
| Storage di rete | NAS commerciale con doppia porta 2,5 GbE, oppure OpenMediaVault su hardware proprio | in valutazione |
| VPN | Tailscale per la semplicita', oppure Pritunl per il controllo | in valutazione, nessuna delle due adottata |
| Backup | agente di backup incrementale su disco esterno, con copia su due servizi cloud diversi | parzialmente in uso |

## Alternative deliberatamente escluse

Sono decisioni gia' prese, e riaprirle senza un fatto nuovo e' spreco di tempo. Il razionale esteso di ciascuna sta nel registro delle decisioni.

Un mini-PC generico di importazione come piattaforma firewall e' stato scartato per assenza di garanzie su firmware, aggiornamenti e componentistica, che in un apparato di sicurezza sono il punto di rottura. pfSense e' stato scartato a favore di OPNsense per la governance e il ritmo di rilascio. IPFire e' stato confrontato in dettaglio e scartato per prestazioni meno prevedibili in NAT intensivo e integrazione dei servizi meno ricca. NethSecurity e' stato citato e non valutato. Lo switch MikroTik CRS310 e' stato scartato perche' il suo routing di livello 3 non serve in una topologia dove il firewall e' l'unico punto di decisione, e costa di piu'. Lo switch Ubiquiti USW-Flex-2.5G-5 e' stato scartato perche' la sua gestione dipende da un controller esterno, cioe' introduce una dipendenza infrastrutturale che una rete domestica non ha motivo di assumere. L'uso di una live Linux per mappare le schede di rete e' stato abbandonato a favore della console del firewall, per non introdurre un secondo stack di driver diverso da quello che governera' il traffico reale. L'esposizione di servizi con IP pubblico dinamico e DNS dinamico e' decaduta con l'assegnazione dell'indirizzo statico.

## Vincoli che nessuna scelta tecnica puo' aggirare

L'ONT accetta traffico solo dal MAC del modem dell'operatore, e il modem non espone bridge ne' passthrough. Ne discende che il doppio NAT e' strutturale e che la Wi-Fi del modem resta fuori dal firewall finche' non la si sostituisce con access point a valle. L'indirizzo pubblico statico, ottenuto senza costi su una linea residenziale, e' cio' che rende sensato esporre un servizio dalla DMZ; e' un dato di contratto, non una proprieta' dell'apparato, e va trattato come tale.
