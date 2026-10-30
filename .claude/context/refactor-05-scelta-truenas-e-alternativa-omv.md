---
covers-paths: ["docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/08-valutazione-openmediavault.md", "docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/03-consolidamento-di-quattro-desktop-dismessi-in-un-nas.md", ".claude/memory/decisions.md"]
last-verified-commit: c5678424466e07e6c2e9e8611fe408d09fde43db
---

# Refactor05 - Capire perché manteniamo TrueNAS

Scheda del28/10/2026 sulla documentazione nell’albero di lavoro, non sul collaudo delle funzioni del NAS. Ritorno al [racconto evolutivo](studio-didattico-master.md). Il [confronto tecnico](../../docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/08-valutazione-openmediavault.md) contiene requisiti, fonti e stato; il [registro NAS](../../docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/09-registro-del-montaggio.md) conserva i passi effettivi.

## Il problema era nella motivazione leggibile

L’utente aveva già scelto TrueNAS ma non aveva capito che cosa ottenesse rispetto a OpenMediaVault. Rileggendo la valutazione si trovava una risposta costruita su una macchina diversa:32GB di RAM, dischi di avvio in specchio e due NVMe per i dati. Il piano corrente ha un solo Kingston per il sistema,8GB attivi e un futuro specchio dati SATA. Ripetere la conclusione vecchia avrebbe dato una ragione non più applicabile al NAS davanti all’utente.

Il testo precedente del confronto, conservato nella storia, diceva:

```text
Per una macchina con 32 GB di memoria, due SSD destinati proprio a un avvio in specchio e un pool ZFS come unico deposito dei dati, TrueNAS SCALE resta la scelta più coerente: fa nativamente le due cose che OpenMediaVault fa con componenti aggiunti o non fa.
```

La nuova frase nello stesso file descrive la scelta che esiste oggi:

```text
Il progetto vuole un archivio per documenti e copie del server, con controllo dell’integrità e una storia recuperabile dei file. Manteniamo TrueNAS perché organizza intorno a ZFS la gestione dello storage, delle istantanee e della replica.
```

L’estratto omette soltanto il marcatore della nota a piè di pagina. ADR-026 conserva la decisione storica; ADR-033 documenta perché il vantaggio dell’avvio in specchio non è più un criterio attuale. Non stiamo riscrivendo retroattivamente la motivazione dell’8/10: spieghiamo perché continuiamo oggi con il piano cambiato.

## Seguire un file fa capire le differenze

Pensiamo a un documento sul futuro NAS. Se un disco smette di funzionare, la seconda copia dello specchio serve a mantenere disponibile il contenuto. Se un disco restituisce un blocco alterato, il controllo d’integrità serve a riconoscerlo e la copia valida può consentire la correzione. Se l’utente cancella il file, lo specchio registra normalmente la cancellazione: serve una versione conservata prima. Se scompare tutto il NAS, serve una copia esterna con una procedura di recupero. Questi scenari spiegano perché nel progetto parliamo di ridondanza, controlli, snapshot e backup come passi diversi.

TrueNAS riunisce amministrazione di ZFS e attività di protezione nel proprio percorso. OMV con il plugin ZFS conserva le proprietà del medesimo filesystem e documenta anche le attività di snapshot, scrub e replica. La preferenza è per il percorso integrato che vogliamo mantenere, non per una presunta esclusiva di integrità del prodotto. Le fonti S74,S231,S233,S235,S236 sono consultabili dal confronto tecnico. La destinazione e il collaudo di una replica restano attività future; il solo uso di ZFS anche sul server non li realizza.

## Il costo della scelta deve essere esplicito

OMV dichiara un requisito base di memoria inferiore. TrueNAS25.10 parte da8GB per le operazioni base, che coincidono con il modulo attualmente montato. Nessuno dei due numeri misura già il futuro carico con snapshot, client e altri servizi: non li usiamo come benchmark comparabile. Il progetto conserva l’obiettivo16GB e la separazione delle applicazioni su Proxmox. Cambiare sistema operativo non rende affidabili i moduli con errori e non produce un risparmio elettrico misurato.

OMV rimane un’alternativa ragionevole per cartelle condivise con una base più leggera, oppure per ZFS amministrato attraverso il suo percorso di plugin e kernel. Manteniamo TrueNAS come preferenza consapevole, non per l’idea che la decisione iniziale fosse irreversibile. La vecchia generalizzazione su Btrfs viene corretta con la documentazione del filesystem, S234: le somme di controllo non appartengono soltanto a ZFS.

## Come useremo questa spiegazione mentre configuriamo

Il confronto tecnico chiude con lo stato osservato: sistema installato, pool dati ancora assente, funzioni di protezione da configurare e provare. Ogni passo successivo dovrà dire quale dei problemi del file risolve e mostrare il relativo risultato. Una mail ricevuta proverà la notifica, una versione recuperata proverà quel recupero, un export custodito salverà la configurazione. Il motivo della scelta resta comprensibile anche se l’ordine del montaggio cambia.
