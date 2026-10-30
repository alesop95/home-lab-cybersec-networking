---
covers-paths: ["docs/03-spunti-di-sviluppo/23-studio-home-lab/16-bisogni-controlli-e-flussi.md", "docs/03-spunti-di-sviluppo/05-strategia-di-backup/10-configurazione-truenas-e-cambio-hardware.md"]
last-verified-commit: 7a659d12bc5e7372dd2f3fc5fc71f3446a2a3e04
---

# Refactor07 - Pool, dataset e cifratura hanno confini diversi

Scheda del28/10/2026. Ritorno al [racconto](studio-didattico-master.md); procedura in [configurazione e cambio hardware](../../docs/03-spunti-di-sviluppo/05-strategia-di-backup/10-configurazione-truenas-e-cambio-hardware.md).

## La casella Encryption apre una scelta di recupero

Il wizard mostra tank, Encryption None e un mirror ancora da popolare. Non significa che esistano già un pool o dati protetti. La guida di recupero conteneva questa frase reale:

```text
Le passphrase ZFS e i segreti conservati da servizi esterni hanno una custodia propria.
```

Era corretta ma non collegava quella custodia alla prima casella del wizard. Se si legge ogni opzione di sicurezza come un miglioramento automatico, si può creare una dipendenza di recupero senza averne predisposto il materiale esterno.

Il documento tecnico ora aggiunge:

```text
Prima dei primi dati reali va definito quali dataset cifrare.
```

S240 raccomanda un dataset radice non cifrato e cifratura separata dei dataset quando necessaria. Questo permette di scegliere ambiti e materiali di sblocco distinti. L’indicazione operativa lascia quindi Encryption vuota nel wizard; non decide che tutti i futuri contenuti saranno sempre in chiaro. La scelta dei dataset e la custodia dei relativi materiali restano esplicite prima dell’uso reale.

## Il mirror risponde a un altro bisogno

I due SSD devono entrare nello stesso VDEV Mirror, non in due gruppi separati. L’integrità e la tolleranza al guasto di un membro appartengono al percorso di conservazione; la cifratura riguarda la leggibilità senza il materiale di sblocco. La matrice dei bisogni ora tiene visibili questi confini, senza attribuire al mirror un backup indipendente o all’export delle impostazioni i file dei dataset.

Nel primo riscontro il VDEV è vuoto e Save Selection è disabilitato. La verifica successiva deve mostrare entrambi i dischi nel medesimo riquadro, poi il riepilogo corretto, la creazione e lo stato del pool. Una preview valida resta diversa da una configurazione applicata. Il nuovo export si acquisirà dopo la modifica effettiva.

## Come estendere il percorso

Quando si aggiunge un dataset si documentano bisogno, eventuale cifratura, custodia esterna, copia dei contenuti e prova di recupero. Password Secret Seed dell’export e passphrase ZFS restano materiali con funzioni distinte. Al28/10 nessuna chiave di dataset è ancora configurata; non si dichiara recuperabilità soltanto dalla presenza di una casella o di un archivio.

Fonte primaria S240, [Create Pool25.10](https://www.truenas.com/docs/scale/25.10/scaletutorials/storage/createpoolwizard/); S137 per il contenuto dell’export e i limiti sulle passphrase. Il registro NAS conserva i riscontri della GUI e gli esiti ancora aperti.

## Avanzamento: selezione salvata e riepilogo ancora senza pool

Le schermate successive mostrano entrambi gli SSD nello stesso Mirror e223.57GiB di capacità grezza utile stimata. L’avviso sulle taglie diverse è coerente con SanDisk240GB e WD250GB: la GUI usa la capacità del membro minore. Questo non misura lo spazio netto per i file e non diagnostica un guasto. Save Selection riporta alla sezione Data con un VDEV manuale; Review conferma tank e la stessa stima. La selezione è ora verificata, mentre Create Pool non è ancora eseguito. Il cambiamento di stato va attribuito al comando che lo applica e al suo esito, non al nome generico Save.

## Dal riepilogo alla configurazione applicata

Ora Pool created successfully e la dashboard tank chiudono la creazione: un mirror a due dischi, Online no errors e213.19GiB utilizzabili. La stima223.57GiB prima della creazione e il valore utilizzabile successivo sono campi diversi, non due misure intercambiabili. Anche i0avvisi temperatura non equivalgono a una lettura normale: la stessa dashboard dichiara temperature non disponibili. Il prossimo controllo legge membri e contatori, senza provocare un guasto.

La modifica rende necessario un nuovo export con seed. Il file precedente resta recuperabile per la tappa precedente, ma la sua integrità non può certificare impostazioni aggiunte dopo. Memoria, registro e piano di backup chiudono la voce creazione del pool e mantengono aperta la nuova acquisizione, insieme ai servizi e ai recuperi ancora da costruire.

## Il dataset avanzato: la scelta non è ancora applicata

Il29/10 l’utente sceglie la chiave automatica. Le immagini mostrano ancora Inherit(non-encrypted) e nessun esito Save: la scelta acquisita e il filesystem creato sono eventi distinti. La [guida NAS12](../../docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/12-dataset-documenti-parametri-e-motivazioni.md) registra ogni campo e distingue eredità, quote e prenotazioni. La stringa reale `ACL Type Inherit` rende visibile una dipendenza: il tipo di permessi deve essere verificato rispetto alla radice e al bisogno SMB, scegliendo NFSv4; Mode Restricted non assegna da solo l’accesso all’utente.

Cifrare il dataset protegge la leggibilità senza chiave; il mirror mantiene due membri e il backup indipendente conserva una via di recupero diversa. Copies1 non annulla il mirror, e SnapdevHIDDEN non prova il valore della directory snapshot mostrata come `--`. Le chiavi esportate e la nuova configurazione si acquisiscono dopo la creazione, senza attribuire ai due export precedenti impostazioni ancora non salvate. La radice rimane non cifrata e il dataset figlio può esserlo; aggiungere cifratura a un dataset già non cifrato richiederebbe migrazione, S247. Fonti dei campi S248/S249; del recupero S137.

## Dataset e condivisione sono due eventi

Il successivo modulo conferma documenti, SMB e la cifratura Key automatica AES-256-GCM. Mostra anche `Create SMB Share` selezionato: il preset prepara quindi più del solo filesystem se si lascia quella casella. La sequenza toglie la creazione automatica per definire prima utente e ACL, poi la condivisione nei passi dedicati. Il tipo NFSv4 si imposta nel dataset; gli accessi finali saranno verificati con il client. Il nome corretto e la chiave selezionata chiudono la lettura di quei campi, senza provare un dataset creato prima del Save.

## La creazione chiude un evento, senza provare tutti i campi

Ora documenti esiste, Unlocked e Not Shared: la cifratura e la separazione dalla condivisione sono osservate. La selezione nel modulo non è più l’unica prova. La schermata precedente mostra però ACL Mode Passthrough mentre l’istruzione era Restricted; la dashboard finale conferma ACL NFSv4 senza mostrare quel campo. Si registra la differenza come valore finale da leggere, evitando sia di dichiararlo corretto senza prova sia di ricreare il filesystem. La chiave esterna e la nuova configurazione sono ora una tappa di recupero concreta, distinta dai due export acquisiti prima della creazione.
