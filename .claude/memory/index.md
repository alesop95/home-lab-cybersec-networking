# Snapshot di sincronizzazione

> Da leggere per primo a inizio sessione. Fotografa lo stato del progetto al commit di riferimento e mappa ogni scheda al suo stato di verifica. E' la fonte di verita' su cosa e' fatto, non la lettura affrettata dei documenti tecnici, che descrivono in larga parte cio' che si intende costruire.

## Stato

```
Branch attivo:         main
Commit di riferimento: eb2f6c3
Data snapshot:         2026-09-01
Remoto:                origin, allineato
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
| `context/STACK.md` | 494b45e | aggiornata |
| `context/design-and-security.md` | 494b45e | aggiornata |
| `context/deployment.md` | 494b45e | aggiornata |
| `context/dev-testing.md` | 494b45e | aggiornata |
| `context/current-work.md` | 494b45e | aggiornata |
| `context/roadmap.md` | 494b45e | aggiornata |
| `context/diagrams/topologia-di-rete.md` | 494b45e | aggiornata |
| `context/diagrams/monitoraggio-open-source.md` | 494b45e | aggiornata |

Le schede sono state scritte il 24/08/2026 e rilette il 25/08/2026 contro il commit indicato, che e' quello in cui la documentazione ha assunto la forma attuale. Da qui in avanti la skill di sincronizzazione le segnalera' come da riverificare appena HEAD si muove, ed e' il comportamento voluto: una scheda vale finche' qualcuno l'ha confrontata con lo stato reale.

## Documentazione generata

L'albero `docs/` e' scritto e manutenuto a mano dal 25/08/2026 (ADR-010). Nasce da una conversione del documento Word, oggi archiviato in `_notes/sorgenti/`, ma non si rigenera piu': il convertitore si rifiuta di sovrascriverlo. Consistenza attuale: 127 documenti, tutti raggiungibili dalla home, zero collegamenti rotti.

La completezza dell'ingestione iniziale non e' affidata al conteggio dei titoli: un confronto paragrafo per paragrafo ha ritrovato 1591 paragrafi su 1591, zero mancanti. Il metodo e le due insidie che lo rendevano inaffidabile alla prima corsa sono in `progress.md`; i conteggi restano in `docs/_CONVERSION-REPORT.md` come documento storico.

## Materiale privato, non versionato

Il progetto si legge e si modifica senza, ma non si verifica: il guard-rail di anonimizzazione ha bisogno del file dei pattern e si ferma se manca, invece di dare un verde non calcolato.

```
_notes/sorgenti/                        materiale grezzo archiviato, con il suo LEGGIMI.md
_notes/sorgenti/PROGETTO ... .docx      prima stesura, archivio e non fonte
_notes/.anonymization-map.md            traduzione segnaposto -> valore reale
_notes/.anonymization-patterns.json     cosa deve cercare il guard-rail
_notes/verbale-installazione-opnsense/  fotografie leggibili della sessione
tools/redactions.json                   sostituzioni della prima stesura, oggi registro
```

## Il consolidamento NAS, e cosa ha insegnato sul guard-rail

Dal 01/09/2026 il repository contiene la scheda del consolidamento di quattro desktop dismessi in un NAS, sotto `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/`, che e' l'hardware candidato allo storage di rete della fase 4. Le quattro macchine non appartengono alla rete domestica e hanno segnaposto propri, registrati nella mappa privata.

Il materiale di lavoro con i valori reali vive in `_notes/nas-consolidation/HANDOFF.md`, escluso da git per nome. L'esclusione e' per nome e non per cartella, perche' i cinque script di censimento nella stessa cartella sono puliti e versionati: se quel file viene rinominato o spostato, l'esclusione non lo segue.

La lezione che vale oltre questo caso riguarda il guard-rail. Su un file con sei password in chiaro e quattro nomi propri dichiarava zero riscontri bloccanti, perche' la categoria dei segreti letterali aveva la lista vuota e i nomi non erano registrati. Il controllo verifica cio' che gli e' stato insegnato: un esito verde su materiale nuovo non e' una garanzia finche' i valori di quel materiale non sono entrati nel file dei pattern. E' il motivo per cui la regola prescrive di aggiornare mappa e pattern prima di scrivere, non dopo.

## Punto di ripresa

L'albero e' allineato al remoto e i controlli sono verdi: 127 documenti su 127 raggiungibili, zero collegamenti rotti, nessun comando spezzato, nessun riscontro bloccante di anonimizzazione. Il secondo controllo ha una riserva nota, descritta nella voce del 01/09/2026 del work-log: il comando documentato percorre tutto l'albero di lavoro invece dei soli file tracciati, quindi resta rosso per materiale grezzo non versionato sotto `_notes/`, mentre sui 238 documenti tracciati e' pulito.

C'e' un lavoro aperto, ed e' fisico: l'assemblaggio del NAS descritto in `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/03-consolidamento-di-quattro-desktop-dismessi-in-un-nas.md`. Vedi `.claude/context/current-work.md`.

Da decidere a parte, e non in una sessione di lavoro ordinaria: se bonificare la storia gia' pubblicata dai due valori descritti sopra, e se il repository su GitHub debba essere pubblico o privato, cosa che al momento non risulta verificata da nessuna parte del progetto.

Il lavoro successivo alla pubblicazione e' la fase 2 della roadmap, cioe' l'identificazione fisica delle tre interfacce del firewall dalla console e la loro assegnazione ai tre ruoli, che e' il primo passo che cambia lo stato della rete e non solo della sua descrizione.
