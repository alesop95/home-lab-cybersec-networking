# Veeam Agent for Windows

Il progetto conserva l'intenzione di salvare in modo incrementale dati privati e di studiare due percorsi distinti, T7 verso Google Drive e T7 Shield verso OneDrive. Al 19/10/2026 non sono verificati disponibilità dei supporti, contenuti, quote cloud, account, licenze o installazione dell'agente. Nessun dato personale è stato letto per sviluppare questo piano. La scelta del perimetro appartiene al proprietario.

## Ruolo nel laboratorio

Veeam è un candidato per l'immagine di un endpoint Windows quando serve recuperare anche il sistema. Per soli file selezionati si valuta invece il [percorso restic](06-salvataggio-dei-file-con-restic.md), con uno scopo e un budget propri. Un'immagine completa dell'endpoint non entra automaticamente nei circa 180 GB proposti per il piccolo NAS: vanno misurati prima copia, incrementi, manutenzione e recupero.

La documentazione di Veeam Agent for Windows 13 consultata il 19/10 elenca per l'edizione Free un solo job e destinazioni locali, share e repository Veeam; esclude backup diretto a object storage, Cloud Connect, sintetici e GFS. La Free è gratuita ma proprietaria. Non si progetta quindi una coppia di job indipendenti verso due destinazioni come se fosse già compresa nella licenza. [Edizioni e limiti](https://helpcenter.veeam.com/docs/agentforwindows/userguide/license_editions.html).

## Prima configurazione proposta

Si censiscono Windows e versione supportata, volumi di avvio e dati, cifratura, driver di rete e storage e tempo richiesto per tornare operativi. Si distingue il disco esterno usato come originale dal disco usato come destinazione. Il job selezionato scrive in una share dedicata dell'endpoint o su un supporto distinto, con quota e credenziale proprie; non usa l'account amministrativo NAS.

La prima copia è completa e le successive formano una catena di incrementi. Il recupero di un punto richiede la base e gli incrementi necessari: non si cancellano manualmente singoli file VBK o VIB per liberare spazio. La conservazione e le eventuali operazioni sulla base vanno dimensionate sul comportamento dell'agente, senza equipararlo automaticamente al modello restic del calcolatore. [Catena di backup](https://helpcenter.veeam.com/docs/agentforwindows/userguide/backup_chain.html).

Per gli SSD esterni si verifica il supporto VSS nella configurazione effettiva. Nella modalità intero computer, un disco esterno precedentemente salvato ma non collegato può essere saltato e il job può terminare con successo; con selezione esplicita del volume o dei file mancanti il comportamento documentato è invece un errore. Per T7 e T7 Shield si registrano quindi presenza e perimetro effettivo, oltre al colore dell'esito. Un disco configurato come supporto di destinazione a rotazione può essere escluso dagli originali. [Backup dei dischi esterni](https://helpcenter.veeam.com/docs/agentforwindows/userguide/backup_usb.html).

La pianificazione della Free consente orari giornalieri o giorni specifici ed eventi, ma disponibilità del NAS, endpoint e supporti devono coincidere. Il primo giro si sorveglia e si misura; gestione dei giri mancati e tentativi successivi si verifica nella versione scelta prima di abilitarli. Gli orari vanno raccordati alle [finestre del laboratorio](05-permessi-finestre-e-collaudo.md). [Pianificazione Free e Workstation](https://helpcenter.veeam.com/docs/agentforwindows/userguide/scheduled_backup_free_workstation.html).

## Preparare il recupero prima di affidarsi al job

Si prepara un'immagine ISO di recupero e la si conserva anche fuori dall'endpoint e dal solo NAS. La creazione diretta di un supporto rimovibile lo formatta: la scelta del supporto e la protezione dei suoi dati precedono l'operazione al banco. L'ISO evita di selezionare ora un dispositivo fisico, ma dovrà comunque essere resa avviabile o utilizzabile nell'ambiente di prova. [Prerequisiti del Recovery Media](https://helpcenter.veeam.com/docs/agentforwindows/userguide/image_create_before.html).

Si includono i driver necessari e si prova il riconoscimento di dischi e rete. L'opzione per includere una chiave di decrittazione nell'immagine semplifica il recupero ma rende l'immagine stessa materiale sensibile: il piano ne propone la custodia separata dalle copie e una scelta esplicita sull'inclusione. I driver aggiuntivi possono richiedere caricamento manuale nell'ambiente di emergenza. [Opzioni del supporto di recupero](https://helpcenter.veeam.com/docs/agentforwindows/userguide/image_create_options.html?ver=13).

## Recuperare prima un file, poi un sistema su disco di prova

Per il primo test si usa un file artificiale con versione e impronta note. Si avvia il ripristino file, si sceglie il punto identificato e nel browser si usa Copy To verso una cartella vuota distinta dall'originale. Si controllano contenuto, versione e permessi richiesti. La conservazione di ownership e ACL è una scelta esplicita; permessi ereditati dal parent possono non conservarsi recuperando il solo figlio. [Salvataggio in una nuova posizione](https://helpcenter.veeam.com/docs/agentforwindows/userguide/files_restore_new.html).

Il recupero completo richiede invece un disco di prova identificato e disponibile, con il disco originale protetto da scritture accidentali. Prima si prova soltanto l'avvio del Recovery Media e la lettura della destinazione, senza iniziare il ripristino. In caso di rete assente si controllano scheda, driver e parametri IPv4 dell'ambiente di recupero; la disponibilità della rete in Windows non prova quella in Windows RE. [Rete nell'ambiente di recupero](https://helpcenter.veeam.com/docs/agentforwindows/userguide/baremetal_network.html?ver=13).

Quando destinazione e mappatura sono confermate, la procedura documentata usa Bare Metal Recovery, Network storage, Shared folder, percorso e credenziale, backup e punto di recupero. Prima di avviare la scrittura si controllano dischi e volumi della destinazione di prova. Il collaudo si chiude dopo avvio del sistema ripristinato e controllo dei dati e delle applicazioni previste. Il semplice accesso al backup dalla chiavetta resta una prova preliminare. [Recupero da condivisione](https://helpcenter.veeam.com/docs/agentforwindows/userguide/howto_baremetal_share.html).

## Backup SSD T7 su Google Drive

L'intenzione originaria resta aperta. Prima si distinguono i dati originali del T7 dagli eventuali archivi Veeam, si censiscono dimensioni e requisiti di riservatezza e si verifica quota e tipo di account Drive. Google Drive non è Google Cloud Storage: il nome Google nel prodotto non prova la compatibilità con la destinazione desiderata.

La Free non offre il backup diretto a object storage e le fonti consultate qui non dimostrano un percorso diretto supportato verso Drive. Le alternative da valutare sono un repository file cifrato con un backend cloud supportato dallo strumento scelto oppure una copia coerente e verificata di archivi completi. Non si mette una catena Veeam in una cartella sincronizzata presumendo che tutti i file necessari siano caricati nello stesso istante. La soluzione cloud resta da progettare prima di qualsiasi collegamento o trasferimento.

## Backup SSD T7 Shield su Microsoft OneDrive

Anche questo percorso resta aperto e distinto dal primo. Si verificano prima supporto, perimetro, quota e tipo di account. OneDrive non è Azure Blob Storage; i limiti dell'edizione e la presenza di una destinazione Microsoft nell'interfaccia non dimostrano l'integrazione voluta.

Qualunque futura alternativa deve mantenere versioni recuperabili, cifratura e materiali di emergenza, controllare il trasferimento completo e consentire una prova da un'altra macchina. L'accesso ai due account e la scelta dei dati non sono attività eseguite durante questo lavoro autonomo. Stato comune dei due percorsi: intenzione preservata, implementazione e collaudo aperti.
