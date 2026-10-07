# NAS network storage

Un NAS Synology[^1] 2-bay rappresenta solo una delle possibili architetture hardware per realizzare uno storage di rete domestico o professionale a basso consumo, e le alternative spaziano da sistemi analoghi multi-bay a dispositivi completamente personalizzabili, ciascuno con caratteristiche precise legate a prestazioni, espandibilità, silenziosità e assorbimento energetico.

La prima alternativa naturale è costituita dai NAS con un solo bay, che riducono ulteriormente consumi e rumore ma sacrificano ridondanza e capacità aggregate, risultando adatti a scenari dove il backup è delegato ad altri sistemi o a cloud esterni.

Una seconda opzione consiste nei NAS 4-bay, 6-bay o superiori, che permettono array RAID più flessibili, caching SSD dedicato[^2], volumi espandibili nel tempo e prestazioni superiori, pur richiedendo un assorbimento elettrico più elevato e una dissipazione termica maggiore, motivo per cui vengono scelti solo quando serve scalabilità reale.

Esistono poi soluzioni all-in-one come i micro-server compatti (ad esempio HP MicroServer o Lenovo Tiny personalizzati[^3]) che integrano hardware x86 standard in chassis molto piccoli, permettono di installare sistemi operativi come TrueNAS o Unraid e offrono un buon equilibrio tra potenza di calcolo, possibilità di espansione, consumo tipico fra 20 e 40 watt in idle e *massima libertà software*, risultando spesso la scelta preferita da chi vuole controllare ogni parametro del proprio storage ma potrebbe avere il limite di non essere multi-bay.

Un’alternativa ancora più efficiente in termini energetici è rappresentata dai single board computer avanzati come Raspberry Pi 5 o RockPro64, ai quali si collegano uno o più dischi tramite USB o HAT dedicati, ottenendo un NAS estremamente parsimonioso (talvolta sotto i 10 watt) e sorprendentemente stabile per backup, media server o storage leggero, benché limitato nelle prestazioni I/O e nella gestione dei file system avanzati.

Si possono considerare anche soluzioni basate su mini PC NUC-like con chassis predisposti per più dischi, che uniscono consumi contenuti e potenza sufficiente per compiti complessi come snapshot, deduplica o Docker, rimanendo comunque più configurabili di un NAS commerciale.

Infine, per chi cerca consumi ridottissimi e un approccio totalmente modulare, è possibile realizzare un NAS con enclosure USB multipli collegati a un computer molto efficiente dal punto di vista energetico, delegando al software la gestione dei volumi e accettando i limiti strutturali del bus USB, una soluzione interessante quando l’obiettivo primario è minimizzare il wattaggio e mantenere un’architettura semplice e facilmente sostituibile.

## NAS Synology (2-bay)

Un NAS Synology 2-bay è un’unità di archiviazione di rete progettata con due alloggiamenti fisici per inserire due hard disk o SSD, permettendo di configurare lo storage in modalità indipendente o in RAID per ottenere maggiore sicurezza dei dati o maggiore capacità, e di usarlo come sistema centralizzato per backup, condivisione file e servizi di rete all’interno di un’infrastruttura domestica o aziendale.

[^1]: In questo contesto “Synology” indica un NAS commerciale proprietario, cioè hardware dedicato e sistema operativo DiskStation Manager (DSM) ed ecosistema software integrato, non un’architettura tecnica generica. Pertanto, è una soluzione chiusa, preconfigurata e ottimizzata dal produttore, in cui prestazioni, consumi, funzionalità e limiti sono definiti dal design Synology e non liberamente modificabili come in un sistema custom.

[^2]: Nel contesto dei NAS multi‑bay, il caching SSD dedicato è una funzionalità che utilizza uno o più SSD installati separatamente dai dischi principali per memorizzare temporaneamente i dati più richiesti, riducendo la latenza e accelerando letture e scritture senza coinvolgere direttamente gli HDD, così da migliorare drasticamente le prestazioni del volume mantenendo inalterata la capacità di archiviazione.

[^3]: Ad esempio, il Lenovo ThinkCentre M700 Tiny è un mini-PC della linea Lenovo Tiny utilizzabile come base hardware per un NAS fai‑da‑te, perché offre un processore x86 standard, consumi ridotti, dimensioni molto compatte e la possibilità di gestire storage esterno tramite USB o adattatori dedicati, pur non essendo progettato nativamente per ospitare più dischi interni come un NAS multi‑bay.
