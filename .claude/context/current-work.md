---
generated-from-commit: 494b45e
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - docs/**
  - .claude/**
last-verified-commit: 494b45e
---

# Lavoro corrente

> Scheda tecnica della feature attiva. Va riletta a inizio sessione e riscritta quando la feature cambia, non accresciuta all'infinito: il registro storico e' `.claude/memory/progress.md`, questa scheda descrive solo cio' che e' aperto adesso.

## Nessuna feature documentale aperta

Il lavoro sulla documentazione e' chiuso e committato. Il repository contiene la documentazione completa del progetto, anonimizzata, coerente e verificata, e il modello di manutenzione e' quello definitivo: si scrive a mano qui dentro, non si genera piu' da nulla.

Chi apre una sessione ora non ha una feature documentale da riprendere. Ha due possibilita': lavorare sulla rete, che e' la fase 2 della roadmap, oppure aggiungere materiale di studio alla documentazione, che non e' una feature ma l'uso normale del progetto.

## Il prossimo lavoro, quando si decide di farlo

Fase 2 della roadmap: identificare fisicamente le tre schede di rete del firewall dalla console e assegnarle ai tre ruoli. E' la prima azione che cambia lo stato della rete invece che la sua descrizione, e sblocca sette delle pendenze aperte.

Si fa alla macchina, non al repository. L'agente puo' assistere sulla sequenza dei comandi e sull'interpretazione dell'output, ma l'esecuzione e' manuale. A valle si scrive un documento trasversale nuovo sotto `docs/`, sul modello di `verbale-installazione-opnsense.md`, e lo si collega da `docs/README.md`.

Attenzione a un punto che puo' costare l'accesso alla macchina: dopo l'assegnazione, OPNsense crea una regola permissiva sulla sola LAN, mentre WAN e la zona esposta partono chiuse in ingresso. Un abbinamento sbagliato chiude fuori dall'interfaccia di gestione oppure espone l'interfaccia sbagliata. La mappatura fisica con la verifica a LED e' un prerequisito, non una raffinatezza.

## Due decisioni sospese, non tecniche

Se bonificare la storia gia' pubblicata dai due valori descritti in `.claude/memory/index.md`. Se il repository su GitHub debba essere pubblico o privato, cosa che non risulta verificata da nessuna parte del progetto e che oggi si assume pubblica per prudenza.

Nessuna delle due si decide in una sessione di lavoro ordinaria e nessuna delle due blocca la fase 2.

## Confine da non superare

L'agente non esegue operazioni git e non tocca lo stato della rete. Prepara file e propone comandi.
