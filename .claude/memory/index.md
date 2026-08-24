# Snapshot di sincronizzazione

> Da leggere per primo a inizio sessione. Fotografa lo stato del progetto al commit di riferimento e mappa ogni scheda al suo stato di verifica. E' la fonte di verita' su cosa e' fatto, non la lettura affrettata dei documenti tecnici, che descrivono in larga parte cio' che si intende costruire.

## Stato

```
Branch attivo:         main
Commit di riferimento: e897797
Data snapshot:         2026-08-24
Remoto:                origin, gia' collegato e gia' pushato fino a e897797
```

## Avvertenza sul remoto, da leggere prima di scrivere qualunque cosa

Il remoto non e' da collegare: esiste gia', e la storia fino a `e897797` e' gia' pubblicata. La finestra in cui bastava correggere un file prima del primo push si e' chiusa in un commit precedente a questa riorganizzazione, e la conseguenza va conosciuta invece che scoperta.

Nel commit `2d3dc2c` la regola sull'identita' git conteneva, in chiaro, la casella di posta di lavoro e il nome dell'organizzazione di lavoro dell'autore, oltre alla casella personale e all'utente GitHub. L'allineamento al template del 24/08/2026 li ha sostituiti con segnaposto nell'albero di lavoro, quindi da questo commit in avanti il tree e' pulito, ma la storia li conserva e resta consultabile. La casella personale e l'utente GitHub coincidono con i metadati di ogni commit e non sono quindi un'esposizione aggiuntiva; la casella di lavoro e il nome dell'organizzazione lo sono.

Non si riscrive la storia di propria iniziativa: e' un'operazione pianificata, con backup, e va decisa dall'autore. Nel frattempo i due valori sono registrati nel file privato dei pattern, cosi' che il guard-rail li intercetti se dovessero rientrare.

## La cosa da sapere prima di ogni altra

La documentazione di questo progetto e' quasi tutta progettazione. Di realizzato c'e' l'installazione del sistema operativo del firewall del 16/01/2026, senza configurazione di rete, e l'ottenimento dell'indirizzo pubblico statico dall'operatore. Lo switch non e' acquistato, gli access point non esistono, nessun servizio interno e' in esercizio. Chi legge le schede tecniche senza questo avvertimento le scambia per descrizione di uno stato di fatto, e sbaglia.

Il vincolo che determina l'intera architettura e' che l'ONT dell'operatore accetta traffico solo dal modem in comodato, e il modem non si puo' mettere in bridge. Da li' discendono il doppio NAT e il wireless inizialmente fuori dal perimetro del firewall.

## Stato di verifica delle schede

| Scheda | last-verified | Stato |
|---|---|---|
| `context/STACK.md` | e897797 | aggiornata |
| `context/design-and-security.md` | e897797 | aggiornata |
| `context/deployment.md` | e897797 | aggiornata |
| `context/dev-testing.md` | e897797 | aggiornata |
| `context/current-work.md` | e897797 | aggiornata |
| `context/roadmap.md` | e897797 | aggiornata |
| `context/diagrams/topologia-di-rete.md` | e897797 | aggiornata |
| `context/diagrams/monitoraggio-open-source.md` | e897797 | aggiornata |

Tutte le schede sono state scritte nella sessione del 24/08/2026 contro il commit indicato, che e' l'ultimo commit del repository prima della riorganizzazione. Il commit che introdurra' la riorganizzazione stessa non esiste ancora al momento della scrittura: alla prima esecuzione della skill di sincronizzazione dopo quel commit, le schede risulteranno da riverificare, ed e' corretto che sia cosi'.

## Documentazione generata

L'albero `docs/` e' prodotto da `tools/docx-to-md.py` a partire dal documento sorgente non versionato. Ultima generazione: 24/08/2026, 120 file, 338 titoli su 338, 74 immagini estratte e non versionate, 54 sostituzioni di anonimizzazione. Il report di ogni corsa e' in `docs/_CONVERSION-REPORT.md`.

I file curati dentro `docs/`, cioe' `DEVELOPMENT.md`, `verbale-installazione-opnsense.md`, `alternative-privacy-oriented.md`, `fonti-e-materiali.md` e `pendenze-aperte.md`, sono scritti a mano e non vanno cancellati quando si rigenera l'albero.

## Materiale privato necessario e non versionato

Senza questi file il progetto si legge ma non si rigenera in modo sicuro.

```
PROGETTO rete e networking domestica.docx   fonte della conversione
tools/redactions.json                       sostituzioni di anonimizzazione
_notes/.anonymization-map.md                traduzione segnaposto -> valore reale
_notes/.anonymization-patterns.json         cosa deve cercare il guard-rail
QuickShare_2601161748/                      fotografie della sessione di installazione
```

## Punto di ripresa

I tre controlli sono stati eseguiti il 24/08/2026 e sono verdi: formattazione conforme su 124 file curati, nessun comando di shell spezzato, nessun riscontro bloccante di anonimizzazione su 355 file fra tracciati e nuovi. Resta da fare il commit e il push, che sono operazioni manuali dell'utente e che l'agente non esegue.

Da decidere a parte, e non in una sessione di lavoro ordinaria: se bonificare la storia gia' pubblicata dai due valori descritti sopra, e se il repository su GitHub debba essere pubblico o privato, cosa che al momento non risulta verificata da nessuna parte del progetto.

Il lavoro successivo alla pubblicazione e' la fase 2 della roadmap, cioe' l'identificazione fisica delle tre interfacce del firewall dalla console e la loro assegnazione ai tre ruoli, che e' il primo passo che cambia lo stato della rete e non solo della sua descrizione.
