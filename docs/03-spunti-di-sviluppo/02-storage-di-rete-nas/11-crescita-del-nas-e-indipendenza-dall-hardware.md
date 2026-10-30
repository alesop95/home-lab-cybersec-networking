# Far crescere il NAS mantenendo dati e configurazione

Ritorno allo [NAS](README.md). Requisito esplicito dell’utente del29/10/2026, ADR-044: la configurazione deve accompagnare SSD più capienti, aumenti di RAM ed eventuali sostituzioni della macchina. La [continuità della configurazione](../05-strategia-di-backup/10-configurazione-truenas-e-cambio-hardware.md) conserva le impostazioni; questa scheda definisce quali elementi rimangono stabili durante la crescita. Nessun ampliamento hardware è eseguito da questo documento.

## Struttura logica e componenti fisici

Il pool attuale si chiama tank e contiene un solo mirror SanDisk240GB/WD250GB. Il Kingston ospita il sistema, RAM-03/A2 offre8GB e l’obiettivo16GB rimane aperto. La capacità utilizzabile osservata è213.19GiB; sulla pagina Datasets del29/10 risultano213.18GiB disponibili e12.21MiB usati. La radice tank è Unencrypted e usata anche dal sistema; i dataset utente non sono ancora creati.

I dataset si organizzano per funzione, con nomi stabili, anziché per marca, taglia del disco o quantità di RAM. Per esempio, documenti e copie del server richiedono ambiti distinti di accesso, conservazione e recupero: i nomi di esempio non attestano dataset già creati. I limiti di spazio si dimensionano sul contenuto e si possono rivedere; non si preparano partizioni rigide legate ai240GB attuali.

| Elemento | Che cosa deve rimanere stabile | Che cosa si rivede dopo la crescita |
|---|---|---|
| pool e dataset | identità logica e percorsi conservati nell’espansione dello stesso pool | spazio disponibile e impostazioni di capacità |
| utenti, gruppi e condivisioni | identità, nomi e regole di accesso mantenute dalla configurazione | collaudo dai client previsti, senza dipendere dai nomi correnti sda/sdc |
| quote e conservazione | obiettivo di separare i consumi e proteggere versioni utili | valori delle quote, picco dei backup e durata delle copie sulla nuova capacità |
| RAM | dataset e condivisioni non sono ricreati per il solo aumento di memoria | compatibilità di scheda, CPU e moduli, stabilità e carico servito |
| macchina e disco di sistema | configurazione con seed, dati e materiali di recupero custoditi separatamente | versione compatibile, riconoscimento dei dischi, rete e servizi ripristinati |

## SSD più grandi nello stesso mirror

La procedura prevista da S243/S244 sostituisce un membro per volta con il disco nuovo identificato. Si attende il completamento del resilver e il ritorno ONLINE prima del membro successivo. Finché rimane il disco piccolo, quello limita lo spazio. Dopo l’ultimo membro si esegue Expand e si verifica la nuova capacità. Dataset e condivisioni rimangono sul medesimo pool; non si ricrea tank per ottenere spazio.

Prima di un futuro intervento si verificheranno copia dei dati, export con seed e compatibilità dei nuovi dischi. La procedura concreta dipenderà anche da porte, alimentazione e vani disponibili; non si prescrive oggi di scollegare un disco funzionante. Nomi Linux e ordine delle porte non sostituiscono modello, seriale privato e appartenenza al pool.

Questa crescita non trasforma automaticamente il mirror in qualunque altra topologia. Aggiungere altri VDEV o migrare verso un altro pool richiede un piano distinto, con effetti su capacità, ridondanza e percorsi da verificare. Non sono acquisti o modifiche già decisi.

## RAM e sostituzione della macchina

La quantità di RAM segue carico, servizi e compatibilità della piattaforma. S246 distingue dimensioni della memoria e casi d’uso: non impone un rapporto universale fra ogni terabyte e memoria. Dal disegno del progetto discende che il solo aumento di RAM compatibile non richiede di ricreare filesystem, utenti o condivisioni. Non si imposta qui alcun limite di memoria legato agli8GB attuali e non si modifica il ruolo del NAS in server di applicazioni.

Il cambio completo di macchina passa invece dal percorso ADR-043: installazione TrueNAS compatibile, recupero dell’export con seed e riconoscimento/importazione del pool esistente, poi rete, accessi e servizi da provare. Se cambiano interfacce o collocazione, gli abbinamenti fisici vanno aggiornati. Un cambio hardware non è un’istruzione a cancellare o ricreare il pool. Prima e dopo le tappe si conservano versioni della configurazione.

## Dataset e capacità che restano modificabili

La schermata attuale mostra Sync STANDARD, LZ4 con rapporto visualizzato2.00x, atime e deduplicazione Off. Il rapporto2.00x è un valore letto, non una promessa di dimezzare ogni file futuro. Snapshots0, Snapshot Tasks0 e No Backup Tasks sono riscontri per il dataset selezionato, distinti dai due export di configurazione già acquisiti fuori NAS.

S245 consente quote modificabili sui dataset. Se si imposta una quota numerica, l’espansione fisica non rende quel limite automaticamente una nuova politica di spazio: lo si rivede con i consumi e i picchi dei lavori. Il [dimensionamento dei backup](../05-strategia-di-backup/03-dimensionamento-e-scenari-di-backup.md) va aggiornato usando capacità e copie reali, non un valore iniziale trattato come definitivo.

Il prossimo passo operativo è aprire Add Dataset sulla radice tank per leggere il modulo. Nome, preset, eventuale cifratura e permessi si definiranno per la funzione del contenuto prima del salvataggio. Nessun dataset utente, condivisione o quota viene dichiarato configurato da questa scheda.

Fonti primarie lette il29/10/2026: S243, [espansione dei pool25.10](https://www.truenas.com/docs/scale/25.10/scaletutorials/storage/managepoolsscale/); S244, [sostituzione dei dischi](https://www.truenas.com/docs/scale/25.10/scaletutorials/storage/disks/replacingdisks/); S245, [dataset e quote](https://www.truenas.com/docs/scale/25.10/scaletutorials/datasets/datasetsscale/); S246, [hardware e memoria](https://www.truenas.com/docs/scale/25.10/gettingstarted/scalehardwareguide/). Il disegno logico è una scelta di progetto, non una prova di upgrade già riuscito.
