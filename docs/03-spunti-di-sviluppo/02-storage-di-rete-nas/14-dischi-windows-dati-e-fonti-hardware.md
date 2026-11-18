# Dischi del Windows quotidiano: dati, riuso e fonti hardware

Ritorno al [NAS](README.md). Dettaglio della [ricognizione hardware](13-ricognizione-hardware-novembre-2026.md), aggiornato il 18/11/2026 su richiesta del proprietario. Il quadro distingue specifiche del modello, misure datate del singolo esemplare e proposte di riallocazione. Le copie integrali delle fonti restano nell’archivio privato; [registro di provenienza, revisione e impronte](../../fonti/hardware-windows-2026-11-18.json) pubblicabile, fonti S289-S294 nel [registro unico](../../../SOURCES.md). Nessun trasferimento o cancellazione eseguiti.

## Ruolo chiarito dal proprietario: corsi di cybersecurity

Il 18/11/2026 il proprietario precisa che l’HDD conserva materiale di corsi di cybersecurity da aprire soltanto in un ambiente Windows 11 sandboxato. Propone quindi di lasciarlo nel PC Windows quotidiano. Questo requisito supera la precedente proposta dell’agente di scollegarlo dopo un trasferimento generico: il volume locale ha un uso preciso e si conserva per quel ruolo. Il proprietario conferma successivamente presenza e avvio della Windows Sandbox nativa. Il riscontro base è chiuso su sua dichiarazione; configurazione di file/rete e isolamento dei corsi rimangono da collaudare.

| Componente | Destinazione nel piano aggiornato | Condizione |
|---|---|---|
| Samsung 850 EVO M.2 SATA 250 GB | Windows 11 e programmi, dopo migrazione del sistema | adattatore, salute, partizioni e avvio indipendente ancora da verificare |
| Samsung HD502HJ 500 GB di PC-07 | resta nel PC per il materiale dei corsi | apertura soltanto nell’ambiente Windows 11 isolato richiesto; salute e copie di protezione da verificare |
| Crucial BX500 1 TB | candidato al NAS dopo la migrazione del solo sistema Windows | rilascio soltanto dopo avvio e dati verificati; crescita mirror ancora legata al secondo SSD |

Non serve spostare i 275,28 GiB di G: per liberare il BX500, se il volume dei corsi rimane sull’HDD. Il limite dei 213,19 GiB del NAS conserva valore per un’eventuale copia integrale di G:, ma quel trasferimento non è più un prerequisito della migrazione del solo C:. Il supporto fisico e l’ambiente di apertura hanno funzioni distinte: lasciare il disco nel PC non realizza da sé l’isolamento. Nessun file dei corsi è stato aperto o eseguito in questa sessione e non se ne deduce la natura dal solo argomento dei corsi.

## Che cosa entra davvero nell’SSD da 250 GB

Il report Windows del 15/11/2026 misura C: 929,89 GiB totali e 789,40 GiB liberi sul BX500; G: 465,22 GiB totali e 189,94 GiB liberi sul Samsung meccanico. Le capacità riportate come GB dal report vengono qui interpretate in base binaria, coerentemente con i tagli commerciali. Non è una nuova lettura dei dischi.

| Dato | Calcolo o fonte | Risultato | Conseguenza |
|---|---|---|---|
| Windows e contenuto attuale di C: |929,89-789,40|140,49 GiB occupati|ordine di grandezza compatibile con l’850 EVO, da verificare su partizioni e dati attuali|
| Contenuto attuale di G: |465,22-189,94|275,28 GiB occupati|supera da solo la capacità nominale dell’850 EVO|
| Somma dei due volumi |140,49+275,28|415,77 GiB occupati|non entra interamente in un SSD commerciale 250 GB|
| Capacità commerciale 250 GB in base binaria |250000000000/1073741824|circa 232,83 GiB prima di partizioni e filesystem|circa 92,34 GiB di margine grezzo rispetto al solo C:, non tutto spazio finale libero garantito|
| Mirror NAS esistente |capacità utilizzabile letta alla creazione di tank,28/10|213,19 GiB|mancano almeno 62,09 GiB per il solo G:, anche supponendo pool vuoto e senza margine operativo|

La sufficienza dei 250 GB riguarda quindi il contenuto di C: osservato, non tutto il contenuto del PC. Prima della migrazione vanno riletti occupazione, partizioni, dati da conservare e salute dell’850 EVO. L’HDD contiene dati: non diventa una scorta vuota quando Windows cambia disco. Il NAS nello stato attuale non può riceverli tutti; il BX500 liberato è un candidato alla crescita, che richiede ancora il secondo SSD adeguato per il mirror. I calcoli sono riproducibili dai valori sopra; il progetto conserva anche il risultato JSON nel livello privato.

## I fatti documentati sul Samsung meccanico

Il Samsung del Windows è un HD502HJ,500 GB commerciali, formato 3,5 pollici, SATA 3 Gb/s,7200 giri/min e 16 MB di cache: caratteristiche del modello confermate dalle schede Samsung S292/S293. La scheda di famiglia lo classifica Desktop Class. La copia S292 è conservata da Dustin; S293 è una stampa del sito Samsung del 29/09/2009 conservata da Kabelfreak. Sono documenti attribuiti al produttore ospitati altrove, senza far passare il distributore per autore o la stampa storica per pagina ufficiale corrente.

Il report del 15/11 riporta per l’esemplare Windows 27°C,43616 ore di accensione e 7571 cicli. Sono circa cinque anni equivalenti di accensione, non l’età di calendario né una previsione della vita residua. La voce Healthy e i pochi contatori presenti non sostituiscono SMART completo, registro dei test ed eventuali verifiche di lettura. La data di fabbricazione agosto 2011 letta sull’altro HD502HJ di PC-02 non si trasferisce a questo esemplare. Il progetto distingue sempre HDD-PC07 in uso e HDD-PC02 recuperato, anche se il modello è uguale.

S292 dichiara 5 W tipici in idle e 1 W in standby per la famiglia 320/500 GB: il disco acceso aggiunge assorbimento, rumore e vibrazioni, senza che qui ne sia misurato il valore effettivo. Le due pubblicazioni storiche riportano valori diversi in lettura/scrittura; non si fissa un consumo operativo univoco del singolo esemplare scegliendo una revisione a piacere.

## Che cosa farne dopo la migrazione

| Opzione | Utilità | Condizioni | Valutazione proposta |
|---|---|---|---|
| Lasciarlo nel Windows durante la migrazione |mantiene accessibili i dati di G: mentre si verifica l’850 EVO|conservare copie dei dati importanti; nessuna pulizia automatica|è il passaggio temporaneo consigliato|
| Tenerlo come disco dati interno |materiale locale dei corsi di cybersecurity|apertura nell’ambiente Windows 11 isolato; salute e copie indipendenti da verificare|orientamento attuale del proprietario|
| Usarlo come copia aggiuntiva scollegata |ulteriore copia di dati selezionati entro la capacità disponibile|dati originali prima trasferiti e verificati; collaudo e controllo delle copie; altra copia affidabile esistente|utile come copia supplementare, non come unica destinazione di protezione|
| Riserva per prove al banco |test di installazione o recupero su dati sacrificabili|liberarlo solo dopo la conservazione verificata dei dati attuali|ruolo ragionevole per un disco anziano|
| Toglierlo dal servizio |riduce componenti sempre accesi se non ha più un bisogno da soddisfare|destinazione dei dati e copie verificate prima di qualunque cancellazione o conferimento|alternativa futura, superata oggi dal ruolo locale dei corsi|

La precedente raccomandazione dell’agente di valutare lo scollegamento è superata dal chiarimento sul materiale dei corsi: l’orientamento attuale è mantenere l’HDD nel Windows per quel ruolo, con apertura nell’ambiente Windows 11 isolato richiesto. Non lo assegnerei al pool NAS principale in questo piano: capacità 500 GB, ore elevate documentate e salute ancora da qualificare non portano il mirror SSD verso l’obiettivo 1 TB. Non è un’affermazione che ogni HD502HJ sia guasto o inutilizzabile; è una scelta di ruolo proposta per questo esemplare e questi bisogni. Le alternative della tabella restano un confronto, mentre il chiarimento attuale orienta il piano verso l’uso locale dell’HDD per i corsi.

Una copia nello stesso PC rimane esposta agli eventi comuni al PC; scollegare il supporto quando non serve cambia il perimetro di esposizione, senza renderlo infallibile. Per un eventuale uso USB del disco 3,5 pollici occorre un collegamento che fornisca anche l’alimentazione richiesta; non si presume sufficiente il cavetto alimentato dalla sola USB usato per molti dischi 2,5 pollici. Non si propone di acquistare un box appositamente prima di sapere se quel ruolo serva.

## Specifiche dei componenti e fonti da riusare

| Componente | Fatti del modello riscontrati | Fonte e limite |
|---|---|---|
| ASRock H97 Anniversary |sei porte SATA3 6 Gb/s; quattro DDR3 fino 32 GB; layout senza M.2 integrato|S285 pagina produttore e S289 manuale 1.0; specifiche e schema, non cablaggio del PC reale|
| Samsung 850 EVO M.2 da 250 GB, MZ-N5E250 |M.2 2280, SATA 6 Gb/s; cache 512 MB LPDDR3 per 250 GB;75 TBW dichiarati per il taglio|S288 supporto e S290 datasheet Rev.2.0; TBW di specifica non misura scritture o salute dell’esemplare|
| Crucial BX500 CT1000BX500SSD1 |1000 GB, SATA III 6 Gb/s,2,5 pollici e 7 mm;540/500 MB/s dichiarati in lettura/scrittura;360 TBW per 1000 GB|S294 documento Micron/Crucial del 24/09/2019 presso Simms; prestazioni dichiarate e revisione datata, non misure del disco usato|
| Samsung HD502HJ |500 GB,3,5 pollici, SATA 3 Gb/s,7200 giri/min,16 MB; alimentazioni5 V e 12 V nella scheda di famiglia|S292/S293, copie storiche Samsung; non certificano la salute di HDD-PC07|
| StarTech SAT32M225, esempio di adattatore |M.2 SATA B/B+M, supporto2280; uscita SATA dati7 pin e alimentazione15 pin|S291; esempio compatibile di categoria, non acquisto deciso|
| Corsair CMV16GX3M2A1600C11 recuperati |kit ValueSelect 2 × 8 GB DDR3,1,5 V, SPD 1333 e prova1600|S286 pagina Corsair letta16/11; riferimento già registrato, nessun nuovo collaudo dei moduli|

Le fonti S289-S294 hanno copie PDF private con SHA-256 e metadati versionati. Le estrazioni e la vista di S292 sono prodotte con PdfCraft0.21.1 locale. Le pagine Micron consultate dal servizio web hanno restituito un rifiuto; il tentativo locale ha confermato un corpo HTML invece del PDF. L’endpoint content.crucial.com non è stato acquisito per errore TLS. Queste vie restano non lette; le caratteristiche BX500 qui usate sono state lette nella copia primariaS294, senza sostituire il contenuto con il risultato del motore di ricerca. Il supporto Seagate del vecchio Spinpoint ha dato un ciclo di redirect e non è una fonte consultata per le specifiche.

Specifiche e revisioni sono una base documentale stabile e vanno riusate senza ricercarle a ogni ripresa. Un nuovo esemplare o una revisione diversa richiedono confronto. Occupazione, SMART, salute, disponibilità dei pezzi, prezzi e stato dei trasferimenti sono invece dati che cambiano: mantengono data e fonte, e si rileggono quando da essi dipende un’azione.

## Windows Sandbox nativa: indicazione e verifica ancora aperta

Il proprietario conferma presenza e avvio della funzione nativa Windows Sandbox; l’indicazione inizialmente probabile è stata confermata nel giro successivo. Il report del 15/11 attesta Windows 11 Pro e Hypervisor present True, ma non contiene l’elenco delle funzionalità opzionali né lo stato di Containers-DisposableClientVM. La sola presenza dell’hypervisor non identifica la funzione che lo usa. La macchina di questa sessione è diversa dal PC-07 del report: un controllo locale qui non confermerebbe lo stato del PC quotidiano. L’agente non ha eseguito un controllo diretto della Sandbox sul PC-07; la conferma di avvio proviene dal proprietario. Nessun corso è stato aperto dall’agente.

Microsoft conferma Windows Sandbox nelle edizioni supportate, inclusa Pro, e descrive un ambiente temporaneo con kernel separato tramite hypervisor, ricreato dopo la chiusura. La guida richiede virtualizzazione abilitata, almeno 4 GB di RAM e 8 GB consigliati; questi sono requisiti della funzione, non un dimensionamento del carico complessivo di questo utente. Fonti ufficiali lette 18/11/2026: [S295, panoramica](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/) e [S296, installazione e avvio](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-install). La configurazione effettiva di accesso ai corsi, condivisioni e rete resta non verificata; nessuna impostazione viene dedotta dalla sola conferma di avvio.

Il riscontro base di presenza e avvio è chiuso sulla conferma del proprietario. La prossima verifica riguarda accesso ai file dei corsi, configurazione e confini di rete; non si richiede nuovamente un semplice avvio vuoto. Il piano dischi resta 850 EVO per Windows/programmi, HDD 500 GB per corsi locali e BX500 1 TB candidato NAS dopo migrazione verificata.

## Conferma dell’avvio Windows Sandbox,18/11/2026

Il proprietario conferma presenza e avvio della funzione nativa. Non si richiede di nuovo quel riscontro. La conferma è dell’utente, non una schermata o un controllo diretto dell’agente; non riguarda ancora file condivisi, rete o isolamento dei corsi. Piano dischi invariato. Il [punto complessivo](../23-studio-home-lab/04-piano-di-lavoro.md) riunisce ora le dipendenze hardware e rete.
