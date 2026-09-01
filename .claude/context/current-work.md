---
generated-from-commit: 494b45e
generated-from-branch: main
generated-date: 2026-09-01
covers-paths:
  - docs/**
  - .claude/**
last-verified-commit: eb2f6c3
---

# Lavoro corrente

> Scheda tecnica della feature attiva. Va riletta a inizio sessione e riscritta quando la feature cambia, non accresciuta all'infinito: il registro storico e' `.claude/memory/progress.md`, questa scheda descrive solo cio' che e' aperto adesso.

## Feature attiva: assemblaggio del NAS per lo storage di rete

Dal 01/09/2026 c'e' un lavoro aperto, e non e' documentale: l'assemblaggio della macchina che coprira' lo storage di rete della fase 4, ricavata da quattro postazioni desktop dismesse. La progettazione e' chiusa e sta in `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/03-consolidamento-di-quattro-desktop-dismessi-in-un-nas.md`; il materiale operativo con i valori reali, escluso da git per nome, e' in `nas-consolidation/HANDOFF.md`.

La definizione di fatto per questa feature e' una macchina montata, con trentadue gigabyte verificati da un ciclo completo di test della memoria, i dischi passati al test SMART lungo, e TrueNAS installato e raggiungibile su un mirror di avvio composto dai due SSD SATA. Non comprende la creazione del pool dei dati, che dipende da un acquisto non ancora deciso ed e' l'unico passo che quella decisione blocca.

Il punto che conta per non perdere tempo: la scelta fra dischi meccanici e NVMe in mirror non e' un prerequisito dell'assemblaggio. Una versione precedente del piano la metteva al primo posto come se lo fosse. Montaggio, firmware, test di stabilita' e installazione si eseguono tutti prima, con una spesa di circa venticinque euro per un adattatore PCIe verso M.2 e una scheda di rete Intel.

A valle dell'assemblaggio si scrive un verbale sul modello di `docs/verbale-installazione-opnsense.md`, che descriva cio' che e' realmente accaduto invece della progettazione, e lo si collega dalla home dell'albero.

## Il lavoro sulla rete, quando si decide di farlo

Fase 2 della roadmap: identificare fisicamente le tre schede di rete del firewall dalla console e assegnarle ai tre ruoli. E' la prima azione che cambia lo stato della rete invece che la sua descrizione, e sblocca sette delle pendenze aperte.

Si fa alla macchina, non al repository. L'agente puo' assistere sulla sequenza dei comandi e sull'interpretazione dell'output, ma l'esecuzione e' manuale. A valle si scrive un documento trasversale nuovo sotto `docs/`, sul modello di `verbale-installazione-opnsense.md`, e lo si collega da `docs/README.md`.

Attenzione a un punto che puo' costare l'accesso alla macchina: dopo l'assegnazione, OPNsense crea una regola permissiva sulla sola LAN, mentre WAN e la zona esposta partono chiuse in ingresso. Un abbinamento sbagliato chiude fuori dall'interfaccia di gestione oppure espone l'interfaccia sbagliata. La mappatura fisica con la verifica a LED e' un prerequisito, non una raffinatezza.

## Due decisioni sospese, non tecniche

Se bonificare la storia gia' pubblicata dai due valori descritti in `.claude/memory/index.md`. Se il repository su GitHub debba essere pubblico o privato, cosa che non risulta verificata da nessuna parte del progetto e che oggi si assume pubblica per prudenza.

Nessuna delle due si decide in una sessione di lavoro ordinaria e nessuna delle due blocca la fase 2.

## Confine da non superare

L'agente non esegue operazioni git e non tocca lo stato della rete. Prepara file e propone comandi.

Sull'assemblaggio il confine e' lo stesso: l'agente ragiona sulle compatibilita', verifica le affermazioni contro i manuali dei costruttori invece di dedurle, e interpreta l'esito dei test, ma il montaggio e i test li esegue una persona. Se serve un riscontro visivo che l'agente non puo' ottenere da se', per esempio la schermata del firmware o l'esito del test di memoria, si applica la regola sugli screenshot manuali.
