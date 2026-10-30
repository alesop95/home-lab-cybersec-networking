---
covers-paths: ["docs/03-spunti-di-sviluppo/05-strategia-di-backup/10-configurazione-truenas-e-cambio-hardware.md", "docs/03-spunti-di-sviluppo/05-strategia-di-backup/04-procedure-di-backup-e-ripristino.md", ".claude/memory/decisions.md"]
last-verified-commit: c5678424466e07e6c2e9e8611fe408d09fde43db
---

# Refactor06 - Le impostazioni devono sopravvivere alla macchina

Scheda del28/10/2026 sull’evoluzione della documentazione nell’albero di lavoro. Ritorno al [racconto](studio-didattico-master.md), piano operativo in [configurazione e cambio hardware](../../docs/03-spunti-di-sviluppo/05-strategia-di-backup/10-configurazione-truenas-e-cambio-hardware.md).

## Dal riepilogo dei clic al recupero del servizio

La prima mail NAS arriva su Proton e dimostra l’intero percorso di invio. L’utente chiede subito che anche le impostazioni siano salvate: se muore il computer, devono restare il mittente, il destinatario, gli account e le successive personalizzazioni. Le fotografie permettono di rileggere i campi ma non ricreano da sole i valori cifrati o il database della piattaforma.

La procedura NAS-01 conteneva già questa istruzione reale:

```text
Dopo la prima configurazione e dopo ogni modifica significativa si esporta la configurazione dalla GUI TrueNAS con Export Password Secret Seed selezionato.
```

Il nuovo documento tecnico rende esplicito il criterio di chiusura:

```text
La tappa è protetta solo quando esiste il relativo file esterno verificato.
```

La differenza è operativa: il primo export viene collegato alla tappa mail riuscita, con versione e copia fuori dal NAS da acquisire ora. Non basta spostare la stessa pendenza più avanti ogni volta che cambia una schermata. Finché il file non è scaricato, quel backup non è dichiarato disponibile.

## Tre perdite possibili, tre materiali diversi

Se si guasta soltanto l’avvio, servono configurazione e nuovo supporto di sistema; i dischi dei dati possono essere ancora validi. Se si perdono anche i dischi dati, il database delle impostazioni non contiene i documenti: occorre la loro copia. Se manca un materiale esterno di recupero, non lo si ricava automaticamente né dalle foto né dall’export del NAS. La protezione dell’account Google resta distinta dalla configurazione TrueNAS e i codici backup restano rinviati come richiesto.

La sostituzione dell’hardware non promette nomi di rete identici: l’impianto logico viene ripristinato e gli abbinamenti fisici vengono verificati. Anche un consenso Google conservato va verificato nel servizio ripristinato. Il criterio è recuperare il comportamento atteso, non ottenere soltanto un login riuscito.

## Riutilizzare Veeam senza attribuirgli prove diverse

Il materiale veeam-linux è già nel template: descrive il backup file e la rilettura eseguiti su un’altra macchina. Lo riusiamo senza chiedere di rifare quelle acquisizioni e senza chiamarlo un recupero TrueNAS già provato. Il file export dovrà essere incluso nel percorso di copia scelto, con destinazione indipendente dal NAS e verifica della sua presenza e recuperabilità.

ADR-043 fissa il requisito dell’utente; il registro distingue esito della mail, file esportato, copia fuori macchina e prova di recupero. Lo stesso schema si estende alle future personalizzazioni: ogni tappa deve indicare quali impostazioni ha aggiunto e quale versione del backup le contiene. Fonti S137,S158,S237,S238 e limiti dichiarati nel documento tecnico.

Avanzamento osservato del28/10/2026: il primo export esiste ora fuori dal NAS. La copia è identica al download, contiene database e seed e supera i controlli di struttura; alcuni campi della tappa sono confrontati in memoria con esiti booleani. Questo chiude l’acquisizione della prima copia, non l’importazione su altro hardware o la seconda destinazione indipendente. La presenza di OAuth nel database non rende il consenso irrevocabile. Il prossimo cambiamento della configurazione richiederà una nuova generazione, mantenendo il file attuale.

Avanzamento del28/10 raccordato il29/10/2026: acquisita e verificata anche la generazione post-pool con seed. Un record tank con GUID è presente soltanto nel nuovo export; mittente, OAuth, recapito, fuso e System Dataset Pool tank sono riscontrati tramite esiti booleani. Le due generazioni hanno stessa dimensione ma impronte differenti, e la prima resta conservata. Questo chiude il checkpoint della creazione del pool; copia indipendente e restore rimangono aperti.

## Terza generazione: il checkpoint distingue davvero una tappa

L’export del29/10 ha la stessa dimensione dei due precedenti ma un’impronta differente. Il record tank/documenti con campo chiave non vuoto compare ora nel database e manca nel post-pool: questo misura la nuova tappa. La chiave JSON separata è già conservata; il campo nel database non è stato decifrato o confrontato in valore con quel JSON. La presenza del seed e dei record e il quick_check dimostrano acquisizione e coerenza dell’archivio, senza provare importazione o sblocco. Lo stesso controllo non rivela ACL Mode, che resta una lettura della GUI. Registro e riepiloghi chiudono la nuova acquisizione e tengono aperti solo i recuperi e i permessi effettivamente non osservati.
