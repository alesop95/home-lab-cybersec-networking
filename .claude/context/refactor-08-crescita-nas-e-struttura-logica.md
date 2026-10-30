---
covers-paths: ["docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/11-crescita-del-nas-e-indipendenza-dall-hardware.md", "docs/03-spunti-di-sviluppo/23-studio-home-lab/12-allocazione-dell-hardware.md", ".claude/memory/decisions.md"]
last-verified-commit: 9499dcae3668e49bb1069664176ca459d386fa53
---

# Refactor08 - Far crescere l’hardware mantenendo la struttura logica

Scheda del29/10/2026. Ritorno al [racconto](studio-didattico-master.md); piano tecnico in [crescita del NAS](../../docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/11-crescita-del-nas-e-indipendenza-dall-hardware.md), requisito in ADR-044.

## Una fotografia dell’hardware non deve diventare un vincolo permanente

L’utente chiede esplicitamente che il lavoro rimanga valido con SSD più grandi, altra RAM e modifiche della macchina. La documentazione aveva già separato recupero della configurazione e copie dei dati; mancava il percorso di crescita dello stesso pool. Le misure attuali potevano sembrare il perimetro definitivo del sistema.

La scheda di allocazione contiene questa frase reale, corretta come misura:

```text
Il mirror dati è limitato al membro nominale da 240 GB, circa 223,517 GiB prima del costo del filesystem.
```

Questa descrive la coppia presente e non impedisce di sostituirla. Il nuovo documento tecnico esplicita invece la regola di progettazione:

```text
I dataset si organizzano per funzione, con nomi stabili, anziché per marca, taglia del disco o quantità di RAM.
```

L’elemento che i client e i backup devono riconoscere è la funzione del dato. Una sostituzione dei supporti non dovrebbe costringerli a inseguire un nome che codificava il modello precedente. Il requisito riguarda percorsi, identità e regole; non promette che ogni futuro cambiamento hardware sia automatico.

## Conservare il pool e far crescere i suoi membri

S243/S244 documentano la crescita mediante sostituzione dei membri del mirror. Il pool e i dataset rimangono gli stessi mentre cambiano i supporti. Ogni resilver deve finire prima del disco successivo; lo spazio resta vincolato al membro minore finché i supporti piccoli rimangono. La verifica finale riguarda capacità nuova, salute e accessi, non il semplice riconoscimento dei dischi nel firmware.

Il processo cambia se si aggiungono VDEV o si migra verso un altro pool: allora si pianificano topologia e percorsi. Non si presenta Expand come trasformazione libera del mirror né si esegue ora un’operazione distruttiva per dimostrarne la possibilità.

## Quote, memoria e continuità delle impostazioni

S245 permette di modificare quote già impostate. Una quota protegge uno scopo, ma il suo valore numerico può diventare piccolo dopo l’espansione e va rivisto con il budget dei backup. La conservazione delle copie segue lo stesso ragionamento: avere più spazio non sceglie da solo quali dati proteggere o quante versioni mantenere.

S246 dimensiona la memoria in base al carico e alla piattaforma. L’aumento di RAM compatibile rimane un cambio della macchina, separato dalla struttura persistente dei dataset. Non si introducono parametri manuali dipendenti dagli8GB presenti e non si assegnano nuovi test alla configurazione attuale. Compatibilità e stabilità del futuro assetto andranno verificate quando si interverrà.

ADR-043 continua a coprire la sostituzione completa della macchina con export con seed e recupero del pool esistente. Le due generazioni già acquisite restano evidenze di copia, non prove di upgrade o restore eseguiti. La nuova guida e ADR-044 rendono la crescita un requisito durevole prima della creazione dei dataset utente.

## Il primo passo verificabile resta piccolo

La schermata Datasets mostra tank, dati di sistema e nessun dataset utente visibile, con0snapshot e0attività snapshot per la selezione. Si apre Add Dataset per leggere il modulo; nome, profilo, cifratura e permessi si definiscono prima di salvare. Lo sviluppo resta osservabile passo per passo e le impostazioni vengono esportate dopo le tappe effettive.
