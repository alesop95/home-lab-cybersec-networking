# Dimensionamento dei backup: spazio di picco e finestra

Questa pagina documenta [dimensiona-backup.py](../../../tools/dimensiona-backup.py), il calcolatore locale del [piano di backup](02-piano-di-backup-e-ripristino-del-lab.md). Legge soltanto lo scenario JSON indicato; non raccoglie dati dai computer, non accede al NAS e non esegue copie o cancellazioni. Il risultato riguarda il modello, mentre l'esito di un ripristino resta una misura distinta.

## Le unità e il budget iniziale

GB significa un miliardo di byte; GiB significa 1.073.741.824 byte. I due SSD dati nominali da 240 e 250 GB in specchio mettono a disposizione al massimo i 240 GB del membro minore, equivalenti a circa 223,517 GiB prima del costo del filesystem. All'ottanta per cento sono 192 GB, circa 178,814 GiB. Queste conversioni vengono dai numeri nominali, non da un pool già creato.

Il riferimento precedente a «223 GB utili, circa 180 GB pianificabili» mescola le due etichette. Per il calcolo iniziale si adotta come proposta prudente un tetto esplicito di 180 GB decimali, cioè circa 167,638 GiB: è più basso dell'ottanta per cento della capacità nominale. Non si modifica l'allocazione dei dischi e non si dichiara misurato lo spazio disponibile. Dopo la creazione del pool il limite va ricalcolato dai dati reali.

Il campo filesystem_reserve dello scenario sottrae prima una riserva esplicita; max_fraction applica poi il margine percentuale. Il programma prende il minore fra questo limite e planning_limit. Nell'esempio la riserva di 5 GB è un'ipotesi del modello, non un costo ZFS misurato o una specifica del produttore.

## Che cosa occupa spazio

Il picco è la somma di dati fissi, copie complete conservate, repository incrementali conservati, blocchi trattenuti dalle istantanee, intera nuova generazione di archivi e spazio di lavoro. Gli archivi protetti sono aggiuntivi rispetto ai posti della conservazione ordinaria. La dimensione di ciascun archivio deve essere un limite superiore ragionevole ricavato dalle copie osservate e dalla crescita prevista; il programma non indovina il rapporto di compressione.

Per gli archivi completi, il modello conta tutte le copie conservate e una nuova generazione intera, anche se i lavori partono in sequenza. Contare solo il maggiore dei nuovi file presupporrebbe che ogni archivio precedente venga liberato prima del successivo: la prima versione del modello faceva questa assunzione, ora rimossa. Il risultato resta prudente senza dipendere dall'ordine di pruning di una specifica versione del software.

Per un repository incrementale si dichiara una base e un limite di dati unici aggiunti per ogni punto conservato. Il modello usa base più variazione unica moltiplicata per i punti successivi al primo e riserva anche l'incremento seguente. È una stima sotto assunzioni costanti: non riproduce il comportamento interno di restic o Veeam, non calcola la deduplicazione futura e non rileva dati dimenticati nell'elenco.

I blocchi trattenuti dalle istantanee hanno un campo separato, snapshot_hold. Cancellare un vecchio archivio non garantisce che il pool ne recuperi subito lo spazio se un'istantanea lo conserva. Una durata di conservazione non si traduce in gigabyte senza conoscere le scritture e le cancellazioni. Lo zero è appropriato solo se tale consumo è stato escluso dal disegno o misurato compatibilmente; non significa «non lo so».

## Lo scenario piccolo, dichiaratamente costruito

Lo [scenario iniziale](esempi/budget-nas-iniziale.json) serve a verificare il metodo e a preparare i campi della raccolta. Non descrive macchine virtuali già installate.

| Componente | Spazio nel modello |
|---|---|
| documenti e configurazioni | 22 GB |
| due copie ordinarie di archivi VM da 18 e 12 GB | 60 GB |
| repository file con base 12 GB e sei variazioni da 500 MB | 15 GB |
| blocchi trattenuti dalle istantanee | 15 GB |
| nuova generazione dei due archivi VM | 30 GB |
| prossimo incremento del repository | 0,5 GB |
| spazio di lavoro generale e del repository | 8 GB |
| picco complessivo | 150,5 GB |
| tetto pianificato e margine residuo | 180 GB e 29,5 GB |

A 20 MiB/s dichiarati come velocità completa della catena, più quindici minuti di lavoro aggiuntivo, la prima corsa da 42 GB richiede nel modello 2.903 secondi; una corsa ordinaria da 30,5 GB richiede 2.355 secondi. Non sono prestazioni misurate del NAS. Il programma arrotonda la durata per eccesso e confronta separatamente la prima copia e quelle ordinarie con la finestra dichiarata.

Una VM il cui archivio pesi 60 GB rende subito visibile il limite: due copie conservate più la nuova consumano da sole 180 GB; tre copie più la nuova consumano 240 GB. Nel primo caso mancherebbe già lo spazio per gli altri dati e per il lavoro temporaneo. Lo specchio da 1 TB del server non implica che i suoi archivi stiano in quello del NAS: contano i dati inclusi e le dimensioni delle copie, ancora da osservare.

## Come eseguire il calcolo

I comandi sono gli stessi in PowerShell e nelle shell Linux, eseguiti dalla radice del repository. Non richiedono librerie aggiuntive.

```text
python tools/dimensiona-backup.py docs/03-spunti-di-sviluppo/05-strategia-di-backup/esempi/budget-nas-iniziale.json
python tools/dimensiona-backup.py docs/03-spunti-di-sviluppo/05-strategia-di-backup/esempi/budget-nas-iniziale.json --json
```

Lo [scenario con troppe copie](esempi/budget-nas-saturo.json) aumenta a cinque le copie ordinarie per ogni VM. Il picco diventa 240,5 GB e il margine meno 60,5 GB. Lo [scenario con finestra insufficiente](esempi/budget-finestra-stretta.json) conserva lo stesso spazio ma riduce la velocità a 2 MiB/s: la finestra di tre ore non contiene né la prima corsa né quella ordinaria.

```text
python tools/dimensiona-backup.py docs/03-spunti-di-sviluppo/05-strategia-di-backup/esempi/budget-nas-saturo.json --json
python tools/dimensiona-backup.py docs/03-spunti-di-sviluppo/05-strategia-di-backup/esempi/budget-finestra-stretta.json --json
```

Il codice di uscita è zero se spazio e due durate rientrano nei limiti pianificati, uno se lo scenario valido li supera, due per file o schema non validi. La chiave operationally_validated resta sempre false, anche con input etichettati measured: il calcolo non dimostra né l'esistenza né il recupero di un backup. Unità mancanti o ambigue, chiavi duplicate o sconosciute e campi obbligatori assenti sono errori, invece di diventare consumi silenziosamente ignorati.

## Dimensionare anche la copia NAS proposta sul server

Il mirror NVMe del server non è spazio illimitato per NAS-03. Lo [scenario server con copia NAS](esempi/budget-server-con-copia-nas.json), aggiunto il 20/10/2026, usa gli stessi controlli del calcolatore con due dispositivi nominali da 1 TB. Riserva di 50 GB, frazione 0,8 e tetto esplicito di 700 GB sono valori costruiti, da sostituire con il budget del pool reale. Il limite percentuale del modello è 760 GB, quindi prevale il tetto più basso di 700 GB.

| Componente del caso server | Spazio costruito |
|---|---|
| dati originali dei guest | 500 GB |
| sistema, installer e altri file locali | 50 GB |
| repository dei documenti NAS, base 22 GB e sei variazioni da 1 GB | 28 GB |
| blocchi trattenuti dalle istantanee | 10 GB |
| prossimo incremento del repository | 1 GB |
| spazio generale e manutenzione | 10 GB |
| picco complessivo | 599 GB |
| tetto e margine | 700 GB e 101 GB |

La quota dei guest riguarda byte occupati da originali o il loro limite superiore pianificato, non la sola somma delle dimensioni virtuali sparse. La copia dei documenti NAS esclude gli archivi PVE conservati sul NAS, evitando una copia ricorsiva dei backup del server. Questo conto non dimostra che tutti i 500 GB dei guest siano protetti dal piccolo NAS: la selezione degli archivi deve essere riconciliata separatamente nella matrice di copertura.

A 20 MiB/s e quindici minuti aggiuntivi, la prima copia dei 22 GB richiede nel modello 1.950 secondi, la successiva variazione da 1 GB 948 secondi. Il primo valore include l'arrotondamento per eccesso prima di aggiungere il tempo fisso. Nel [caso server saturo](esempi/budget-server-saturo.json) cambia soltanto il limite dei dati guest, da 500 a 700 GB: picco 799 GB e margine meno 99 GB, anche se le durate del solo backup NAS sono identiche. Entrambi i casi sono costruiti e non misurano una macchina già montata.

```text
python tools/dimensiona-backup.py docs/03-spunti-di-sviluppo/05-strategia-di-backup/esempi/budget-server-con-copia-nas.json --json
python tools/dimensiona-backup.py docs/03-spunti-di-sviluppo/05-strategia-di-backup/esempi/budget-server-saturo.json --json
```

I due comandi sono stati eseguiti il 20/10/2026: exit 0 e 1 rispettivamente, con risultati e impronte degli input conservati nella parte privata. Non richiedono di leggere gli originali del NAS e non configurano una quota sul server.

## Le prove e il loro limite

La [suite](../../../tools/test_dimensiona_backup.py) verifica conversioni, membro minore dello specchio, vecchie copie che rientrano mentre il nuovo archivio non rientra, nuova generazione intera, archivi protetti, istantanee, spazio di manutenzione, frontiera di un byte, prima copia e incrementi, arrotondamento del tempo, errori dello schema e codici CLI.

```text
python tools/test_dimensiona_backup.py
```

Il 19/10/2026 passano 27 prove. Sette copie mutate del programma sono state sottoposte alla stessa suite: sommare i dischi, omettere il nuovo full, contare soltanto il nuovo maggiore, omettere istantanee o copie protette, certificare operatività dalla stima, trattare la prima copia come un incremento. Tutte provocano asserzioni fallite e nessun errore di esecuzione; l'impronta del programma originale rimane invariata. Questa verifica prova che la suite distingue quei difetti del modello. Non misura la dimensione dei dati di casa, il funzionamento di Proxmox o il ripristino di un servizio.

## Ricalcolo dopo la crescita del NAS

ADR-044 del29/10/2026 rende il dimensionamento rivedibile con SSD più capienti. Gli esempi su240GB e il tetto proposto di180GB descrivono il punto di partenza, non una quota permanente già applicata al NAS. Dopo l’espansione si leggono capacità reale, quote eventualmente configurate e picchi dei lavori e si aggiornano gli input; non si presume che una quota numerica cresca insieme ai dischi. Si mantengono nomi dei dataset e destinazioni logiche; dettagli nella [guida NAS11](../02-storage-di-rete-nas/11-crescita-del-nas-e-indipendenza-dall-hardware.md). Nessuna prova di espansione è già eseguita.
