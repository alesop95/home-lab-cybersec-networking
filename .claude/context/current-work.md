---
generated-from-commit: 494b45e
generated-from-branch: main
generated-date: 2026-09-03
covers-paths:
  - docs/**
  - .claude/**
last-verified-commit: 05cc896
---

# Lavoro corrente

> Scheda tecnica della feature attiva. Va riletta a inizio sessione e riscritta quando la feature cambia, non accresciuta all'infinito: il registro storico e' `.claude/memory/progress.md`, questa scheda descrive solo cio' che e' aperto adesso.

## Feature attiva: assemblaggio del NAS per lo storage di rete

Dal 01/09/2026 c'e' un lavoro aperto, e dal 03/09 e' passato dalla progettazione all'esecuzione: e' la prima attivita' del progetto che tocca hardware invece di documentazione. Copre lo storage di rete della fase 4 della roadmap, ricavato da quattro postazioni desktop dismesse.

La progettazione, anonimizzata e pubblicabile, sta in tre schede sotto `docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/`: l'analisi con le decisioni, la guida all'assemblaggio, e il calcolo dei consumi con la finestra di accensione. Il materiale operativo con i valori reali delle quattro macchine sta fuori dall'albero versionato, sotto `_notes/nas-consolidation/`, e comprende la guida passo a passo che porta lo stato di avanzamento, l'analisi dei consumi con i dati di bolletta, le credenziali e l'handoff originale.

## Dove si e' arrivati

La fonte di verita' sull'avanzamento e' la guida operativa, dove ogni passo concluso porta un timbro con la data. Al 03/09/2026 lo stato e' il seguente.

E' chiusa la fase preparatoria. I salvataggi delle due macchine Linux sono stati verificati per ripristino effettivo e non soltanto prodotti, l'assenza di dati da conservare e' confermata su tutte e quattro, le immagini di installazione sono scaricate e verificate per somma di controllo contro il valore pubblicato dalla fonte, la finestra di accensione e' decisa e registrata come ADR-011, e le etichette sono stampate e attaccate ai quattro case dopo riverifica degli indirizzi.

E' chiuso il primo passo dello smontaggio. Le quattro macchine sono spente, con l'interruttore dell'alimentatore in posizione aperta e il cavo lasciato inserito: e' una scelta migliore dello scollegare, perche' il conduttore di terra non passa dall'interruttore e quindi il telaio resta il riferimento su cui scaricare la statica mentre le linee di alimentazione sono morte. Nessun case e' ancora stato aperto.

## Il passo successivo, esattamente

Si apre soltanto `PC-DESKTOP-B` e si prelevano i due moduli di memoria da otto gigabyte dagli alloggiamenti A1 e B1, che sono in posizioni non adiacenti. Da quella macchina escono tre dei cinque pezzi da recuperare, ed e' la ragione per cui e' la prima ad aprirsi; la macchina base si apre per ultima, perche' una volta aperta ci si lavora dentro fino alla fine.

Resta aperto in parallelo, e non blocca nulla, l'ordine dell'adattatore da PCIe verso M.2 e della scheda di rete Intel: servono al montaggio e non ai prelievi, quindi l'intera fase di smontaggio si esegue senza di essi.

## Definizione di fatto

Una macchina montata, con trentadue gigabyte verificati da un ciclo completo di test della memoria, i dischi passati al test SMART lungo, e il sistema installato e raggiungibile su un insieme di avvio in mirror composto dai due dischi a stato solido SATA. Non comprende la creazione del pool dei dati, che dipende da un acquisto non ancora deciso ed e' l'unico passo che quella decisione blocca.

A valle si scrive un verbale sotto `docs/`, sul modello di `docs/verbale-installazione-opnsense.md`, che descriva cio' che e' realmente accaduto invece della progettazione, e lo si collega dalla home dell'albero.

## Due cose che sono gia' state fatte e non vanno rifatte

Il censimento hardware delle quattro macchine esiste dal 31/08 e dall'01/09 in `nas-consolidation/scripts/`, e i suoi valori sono gia' trascritti nelle tabelle di identificazione della guida. In sessione si e' perso tempo a riproporne la raccolta, ed e' un errore da non ripetere.

La cartella `_censimento-hardware` sul NAS di backup non e' una fonte ma una copia parziale e ridondante degli stessi file, priva dei due report delle macchine Linux. L'handoff originale la citava in un modo che la faceva sembrare una fonte.

Resta invece da fare a mano, a case aperti, la sola cosa che il censimento software non puo' dare: i dati degli alimentatori. Un alimentatore ATX non ha interfaccia dati verso la scheda madre, quindi non esiste una classe da interrogare e l'etichetta e' la sola fonte.

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
