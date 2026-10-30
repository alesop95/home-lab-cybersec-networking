---
covers-paths: ["docs/03-spunti-di-sviluppo/23-studio-home-lab/12-allocazione-dell-hardware.md", "docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/09-registro-del-montaggio.md", ".claude/memory/decisions.md", ".claude/context/current-work.md"]
last-verified-commit: 76ec0d2bedcb32371b193e72290d3ef0dbf85123
---

# Refactor 02 - Inventario reale, obiettivi e RAM con errori

Scheda del26/10/2026. Ritorno al [racconto](studio-didattico-master.md) e all'[allocazione tecnica](../../docs/03-spunti-di-sviluppo/23-studio-home-lab/12-allocazione-dell-hardware.md). Gli estratti sono stati letti dai file reali prima e dopo questa revisione nell'albero di lavoro; HEAD non contiene ancora le modifiche da committare manualmente.

## Perché non bastava il totale dei gigabyte

Il piano precedente assegnava NAS16 GB e server24 GB, prima degli errori emersi nei moduli. Durante il montaggio sono emersi errori in tre moduli TEAMGROUP da8 GB. Il NAS è rimasto con RAM-03 da8 GB e i Crucial non sono stati prelevati dal server. Questa informazione era nel registro, ma la tabella generale continuava a presentare gli obiettivi come disponibilità.

Il problema non era una differenza di stile: la tabella autorizzava implicitamente gesti non più sostenuti dai pezzi. Una sessione successiva avrebbe potuto chiedere di montare sul server due moduli da8 GB già impegnati o esclusi, oppure di cercare due Crucial in magazzino mentre risultavano ancora sulla scheda madre.

## Prima e dopo, nel sorgente effettivo

La riga NAS di `12-allocazione-dell-hardware.md` prima della revisione era:

```markdown
| `PC-DESKTOP-A` | NAS TrueNAS SCALE | ASUS H170-PRO, i7-6700 | 16 GB DDR4 | avvio sul Kingston V300; dati in specchio sui due SSD SATA SanDisk e WD Blue | ripristino automatico dell'accensione, sei porte SATA; serve file su rete a 1 Gbit, che un SSD SATA già satura (ADR-016, ADR-026, ADR-033) |
```

La stessa riga dopo la revisione è:

```markdown
| `PC-DESKTOP-A` | NAS di file TrueNAS | ASUS H170-PRO, i7-6700, sei porte SATA | 8 GB montati, RAM-03 in A2; obiettivo 16 GB con un secondo modulo da 8 GB | Kingston V300 240 GB per avvio; SanDisk 240 GB e WD 250 GB per futuro specchio dati; tutti test estesi superati, sistema non installato |
```

Anche la riga server cambiava significato se la si leggeva come stato attuale. Prima:

```markdown
| `linux-desktop-A` | server Proxmox SRV-01, sempre acceso | ASRock H270M Pro4, i7-7700 | 24 GB DDR4 | i due NVMe da 1 TB, Crucial P2 e P3, in specchio ZFS, sistema e macchine virtuali | il processore più recente, la sola rete Intel, due alloggiamenti M.2 NVMe; è la macchina che scrive di continuo (ADR-030, ADR-033) |
```

Dopo:

```markdown
| `linux-desktop-A` | server Proxmox SRV-01, sempre acceso | ASRock H270M Pro4, i7-7700, rete Intel | ultimo censimento 16 GB DDR4, quattro Crucial da 4 GB; vecchio obiettivo 24 GB sospeso | Crucial P2 e P3 NVMe da 1 TB previsti in specchio; montaggio e Proxmox non confermati |
```

Sono estratti di documentazione operativa, non codice di un gestore della memoria. Il loro effetto è sul gesto che il proprietario compie: una destinazione futura non deve apparire come un prelievo già avvenuto.

## Censito, provato, assegnato e proposto

Una capacità censita dice quanto era stato osservato in una macchina. Una prova dice come si è comportata una configurazione specifica. Un'assegnazione dice dove si trova o rimane un pezzo. Una proposta descrive un possibile gesto e attende una scelta. Nessuna delle quattro cose implica automaticamente le altre.

RAM-03 ha una prova individuale prolungata senza fail riferita dall'utente. I Crucial risultano dal censimento, con assenza di errori segnalati, ma non viene inventato un loro nuovo Memtest. RAM-01/02 hanno fallito da sole in due slot e RAM-04 da sola in A2. Per i servizi restano escluse: un errore che altera un dato può danneggiare anche una VM o il monitoraggio, non soltanto un filesystem. Non si certifica però da questo una diagnosi elettronica definitiva su un'altra piattaforma.

Un eventuale banco di recupero sulla B150-PRO avrebbe un senso diverso dal ripetere indefinitamente la stessa combinazione: confronterebbe un'altra scheda, controller e alimentazione. È una possibilità di studio separata, senza una nuova prova imposta per finire il NAS e senza contare in anticipo il modulo come recuperato.

## Il motivo concreto degli 8 GB

S204 conferma il minimo base di8 GB per TrueNAS25.10. L'adeguatezza per questo progetto è un'inferenza sul ruolo scelto: condivisioni di file e ricezione di copie su due SSD, mentre applicazioni e VM sono altrove. La RAM serve al sistema, alle strutture di gestione e alla cache; i file persistono sui dischi. Aumentarla può aiutare cache e concorrenza, ma non sostituisce backup o memoria che conservi correttamente i bit.

Il compromesso viene dichiarato:8 GB hanno meno margine di16 e le prestazioni reali con il carico del progetto non sono ancora misurate. Non si deduce una necessità di ripetere tutti i test hardware prima di avviare il sistema. Non si adotta un carico diverso, come VM o deduplicazione, senza rifare il conto.

## La redistribuzione è una somma con vincoli fisici

RAM-03 più quattro Crucial fanno24 GB DDR4 senza errori segnalati.8 al NAS e16 al server è il punto corrente. Un Crucial aggiunto al NAS produce12/12, non12/16. Tutti i Crucial al NAS e RAM-03 al server producono16/8, con meno margine alla macchina che ospita Proxmox e Wazuh. Per16/16 mancano8 GB utilizzabili. La DDR3 del laboratorio non riempie questo vuoto perché appartiene a un'altra piattaforma.

Le tre alternative sono proposte nella tabella tecnica, senza spacciarle per montaggi eseguiti. Se cambia la scelta, si aggiornano allocazione e decisione prima di chiedere il gesto; si identifica il modulo fisico e poi si verifica la combinazione finale. La lezione estendibile è mantenere insieme disponibilità, stato e costo per l'altro ruolo, non scegliere una cifra isolata perché sembra più rassicurante.

## La scelta finale dell'utente non modifica retroattivamente i test

Dopo il confronto delle quantità, l'utente chiede un secondo modulo da8 GB nel NAS e gli altri due come scorta. Si registra l'obiettivo16 GB con chiarezza. Non si registra però un inesistente secondo modulo già passato: ancheRAM-01/02/04 avevano mostrato errori. La destinazione candidata non è una qualifica tecnica. Il NAS attuale resta8 GB, i Crucial rimangono nel server e le due scorte RAM-02/04 conservano lo stato con errori.

Se un modulo viene recuperato su altra piattaforma o sostituito, sarà quel nuovo riscontro a chiudere il punto. Questa distinzione permette di rispettare il risultato richiesto senza cambiare i fatti precedenti o imporre un'intera matrice di prove come premessa a ogni passo.

L'ultima autorizzazione dell'utente permette di rendere concreta la verifica: RAM-03 rimaneA2, RAM-01 viene propostaB2, BIOS16 GB a2133 MHz e XMP disabilitato, poi quattro passaggi senza errori o stop al primo errore. La coppia non risulta già provata. È un esperimento sulla configurazione richiesta, non una dichiarazione che il modulo precedentemente fallito sia ora buono. Nessun montaggio o esito è ancora stato osservato.

## Perché la RAM volatile può lasciare un errore su disco

Sviluppo successivo del 26/10/2026: la coppia RAM-03/A2 + RAM-01/B2 è stata montata, il BIOS ha riconosciuto 16384 MB e Memtest è partito. La prova è poi fallita prima del primo passaggio, con un errore. Le descrizioni precedenti della proposta restano la sequenza storica, non lo stato corrente.

Volatile descrive ciò che accade togliendo corrente: il contenuto della RAM si perde. Durante il funzionamento, invece, la RAM contiene dati dei file, cache e strutture del sistema operativo. Un dato alterato in RAM può essere scritto su SSD e diventare un errore persistente; un blocco già letto può anche essere inviato alterato al PC che lo sta copiando. Sono possibili crash e blocchi, oppure corruzione senza un crash evidente. Il mirror protegge da alcuni guasti dei dischi, ma due dischi possono ricevere lo stesso dato già errato. Un checksum calcolato dopo l'alterazione può essere coerente con il dato sbagliato: è un esempio del limite di un controllo posto a valle, non un guasto ZFS già osservato. Non è possibile tradurre un errore Memtest in una percentuale di file corrotti o in un intervallo di tempo al guasto. Il rischio dipende da quale contenuto occupa la zona interessata e da quando viene usato. La guida TrueNAS 25.10, S204, descrive esplicitamente crash e perdita o corruzione di dati causati da errori RAM, pur riconoscendo che molti sistemi funzionano senza ECC. Non avere ECC e avere errori riprodotti sono condizioni diverse; non viene imposto un cambio di piattaforma o un acquisto ECC.

Il confronto osservato sul banco è reale e proviene dalla riga di errore documentata nel registro NAS:

```text
Configurazione: RAM-03/A2 + RAM-01/B2
Pass: 0   Errors: 1   Test della riga: 9
Failing Address: 0x000100d49410
Expected:        0x3d12e399ff15f5d8
Found:           0x3d12e399ff15fdd8
XOR calcolato:   0x0000000000000800
```

Qui il confronto prima/dopo è fra il valore atteso dal test e quello riletto dalla memoria: cambia il bit 11. Non è il contenuto di un file utente e non prova una corruzione già avvenuta sui tre SSD. Dimostra però il difetto che il controllo cercava, nella configurazione desiderata da 16 GB. Un successivo passaggio pulito non rende inesistente questo errore. Il criterio di stop evita di pagare altre ore per una configurazione che ha già fallito. Restano aperti la causa esatta e il secondo modulo utilizzabile; non si dichiara guasto irreversibile un DIMM dall'indirizzo o necessaria una matrice infinita di prove. Fonti: S126 e S129 per lettura e limiti di Memtest, S204 per i rischi RAM su TrueNAS.
