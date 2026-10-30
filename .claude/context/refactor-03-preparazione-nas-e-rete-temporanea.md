---
covers-paths: [".claude/context/STACK.md", ".claude/context/current-work.md", "docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/09-registro-del-montaggio.md", ".claude/memory/decisions.md"]
last-verified-commit: 76ec0d2bedcb32371b193e72290d3ef0dbf85123
---

# Refactor03 - Preparazione del NAS e rete temporanea

Scheda del27/10/2026. Ritorno al [racconto](studio-didattico-master.md). Il [registro NAS](../../docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/09-registro-del-montaggio.md) conserva fatti e piano tecnico. Gli estratti seguenti sono stati letti dal file reale prima e dopo l'aggiornamento nell'albero di lavoro; non sono codice di configurazione eseguito sul NAS.

## Da un unico stato a più riscontri

Il NAS ha raggiunto la console del sistema installato. Questo chiude il primo avvio, ma non il collegamento al browser: l'ultima foto non mostra l'indirizzo di gestione. L'utente segnala inoltre una rete temporanea diversa da quella domestica prevista. La domanda utile diventa quale proprietà serva per il passo successivo, senza aspettare che ogni dipendenza futura sia pronta.

In `.claude/context/STACK.md`, prima:

```markdown
| Storage di rete | TrueNAS25.10.7 previsto su H170-PRO/i7-6700,8GB attuali e obiettivo16GB da provare; KingstonV300 avvio,SanDisk/WD dati,nessuna app NAS | tre SSD testati,ISO suVentoy; non installato,datiSanDisk da chiarire,ADR-033/039 |
```

Dopo:

```markdown
| Storage di rete | TrueNAS25.10.7 installato su H170-PRO/i7-6700, RAM-03/A2 da8GB provvisori e obiettivo16GB aperto; Kingston avvio, SanDisk/WD dati previsti | primo boot fino alla console osservato; web senza indirizzo, enp3s0 già DHCP Yes su rete temporanea; pool e dati SanDisk ancora da chiarire, ADR-033/039/040 |
```

Il prima continuava a descrivere il progetto quando il sistema era già stato installato. Il dopo conserva il progresso e rende esplicito il limite: esiste il primo boot, manca ancora l'accesso web. Il numero di gigabyte resta8, con16 come obiettivo aperto; il collegamento non promuove la RAM esclusa e non autorizza la cancellazione dei dischi dati.

## Che cosa segue la macchina e che cosa segue il luogo

Lingua, tastiera, fuso orario, account e stato del disco di avvio appartengono alla preparazione della macchina. L'indirizzo usato per raggiungerla dipende dalla rete; regole fra zone e instradamento devono essere provati nella topologia effettiva. DHCP[^1] è la scelta operativa temporanea, ma la schermata osservata lo mostra già Yes: cambiare un valore già corretto non dimostrerebbe che è arrivato un indirizzo. Il passo informativo è leggere stato e indirizzi di enp3s0, quindi provare il login web quando compare un indirizzo.

I17 fotogrammi vanno letti come una sequenza: alcune righe rosse sono attese di job poi seguite da esiti OK; il timer IPA ha invece un errore esplicito, registrato senza una causa inventata. Il sistema arriva comunque alla console. Da qui non si deducono una rete operativa o l'irrilevanza permanente di ogni messaggio.

## La preparazione si conserva, il trasferimento si verifica

Dopo l'accesso, il piano tecnico prepara localizzazione, lettura della salute del boot-pool ed export della configurazione. I contenuti dei file SanDisk restano una decisione distinta, prima di creare il mirror. Al trasferimento a casa si applica l'indirizzamento previsto, si prova di nuovo l'accesso e si rinnova l'export. Il file con secret seed resta nel livello privato, non nella memoria pubblica.

Il principio si estende chiedendo per ogni attività quale dipendenza debba essere vera e dove sia osservabile. La presenza di DHCP, un indirizzo e un login riuscito sono tre riscontri distinti. Conservare queste differenze permette di avanzare senza inventare una rete già realizzata e senza ripetere ogni impostazione a ogni spostamento. Fonti S210-S212 e S158 per i passi di TrueNAS; separazione delle fasi adottata in ADR-040.

[^1]: DHCP, Dynamic Host Configuration Protocol, assegna parametri di rete al client nella rete disponibile. Qui l'opzione è osservata attiva, ma un indirizzo non è ancora stato mostrato.

Sviluppo seguente del27/10. La lettura richiesta restituisce enp3s0 DOWN e nessun indirizzo, mentre DHCP era già Yes. Il prossimo controllo legge i flag con ip link show enp3s0 e verifica il cavo: il valore configurato, lo stato amministrativo, il collegamento e il lease restano proprietà distinte, secondo il modello operativo del kernel documentato in S213. Non è ancora stata acquisita la causa della mancata operatività e non si introduce un IP statico per aggirare un collegamento non verificato.

Chiarimento successivo. L'utente riferisce il cavo non ancora collegato e la nuova lettura mostra UP con solo IPv6 locale. La verifica dei flag richiesta per il DOWN viene superata dal nuovo riscontro: non si continua un ramo diagnostico già risolto. Manca ancora il lease IPv4, quindi si attende l'aggiornamento della console e si chiarisce dove termina il cavo prima di assumere che un server DHCP sia presente. Nessun nuovo indirizzo o servizio di rete è stato configurato.

La risposta chiarisce che il NAS è sullo switch aziendale con una classe IP assegnata in DHCP. Il servizio è atteso nella rete disponibile, mentre il lease del NAS non è ancora visibile. Si mantiene la configurazione DHCP e si verifica la console aggiornata, senza inventare un indirizzo o trattare il collegamento come NAS-PC diretto.

## Dal lease al login e alle notifiche

Le schermate successive mostrano prima il lease IPv4 e poi la dashboard autenticata. Il limite documentato nella riga dopo diventa storia, mentre lo stato corrente di `.claude/context/STACK.md` ora è:

```markdown
| Storage di rete | TrueNAS25.10.7 installato su H170-PRO/i7-6700, RAM-03/A2 da8GB provvisori e obiettivo16GB aperto; Kingston avvio, SanDisk/WD dati previsti | primo boot, lease DHCP e login web verificati sulla LAN temporanea; localizzazione e notifiche da configurare, pool e dati SanDisk ancora aperti, ADR-033/039/040/041 |
```

Il collegamento ha quindi prodotto un indirizzo utilizzabile e il login è riuscito. Sono osservazioni distinte dal salvataggio della localizzazione: General Settings mostra ancora America/Los_Angeles e tastiera americana. Il valore 0.0.0.0 nella sezione GUI descrive invece dove il servizio ascolta; non sostituisce l'indirizzo assegnato alla scheda per raggiungere la pagina. Nessuna impostazione di rete è stata cambiata per ottenere questi riscontri.

La richiesta di email aggiunge tre passaggi: il NAS genera l'avviso, un provider autenticato lo spedisce e la casella destinataria lo riceve e classifica. Proton è la destinazione preferita dell'utente; Gmail OAuth è una proposta di trasporto separata. Salvare il metodo in GUI misura la configurazione, Send Test Mail e la ricezione misurano il recapito, il test del servizio alert misura quel percorso, e vedere il messaggio in Log NAS misura il filtro. Ognuno ha un esito proprio, ancora aperto.

La cartella raccoglie notifiche e rapporti utili a reagire; i log completi hanno contenuto e conservazione da progettare nel loro percorso. Lo studio generale della posta dai server domestici è rinviato esplicitamente. La preparazione attuale segue ADR-041, con dettaglio tecnico nel registro NAS e fonti S214-S216. Il modello si estende agli altri servizi chiedendo chi produce, chi trasporta, chi riceve e quale osservazione dimostri ciascun passaggio.

Riscontro seguente del27/10/2026: il pannello di modifica mostra Italian (it) e Europe/Rome durante il salvataggio; la schermata successiva li riporta nel riepilogo, con lingua inglese e data giorno/mese/anno. La localizzazione è quindi applicata e verificata. Il passaggio dalla selezione al valore riletto chiude questa verifica; l'orario coerente con il fuso non dimostra da solo una sincronizzazione NTP. Il prossimo passo riguarda i campi Email, ancora da configurare e provare.

## Il consenso nel browser e il lavoro del NAS

La nuova schermata mostra GMail OAuth selezionato ma Save ancora disabilitato e richiesta di login. È un altro stato intermedio: selezione, autorizzazione salvata e consegna osservata restano separati. La domanda dell'utente sul cambio di browser chiarisce dove risiede il lavoro. Il browser raccoglie il consenso; dopo il salvataggio il NAS usa il collegamento per spedire (S214). Il rinnovo OAuth consente l'uso senza utente presente finché l'autorizzazione resta valida (S217).

La parte che segue la macchina è il collegamento salvato. La connettività in uscita va verificata nella nuova rete. La possibilità di aprire la GUI da fuori richiede invece il percorso di accesso previsto dal progetto: scegliere OAuth non configura la VPN. Questa distinzione estende ADR-040 e la separazione fra destinatario, trasporto e classificazione di ADR-041; non dichiara ancora riuscito alcun login o test email.

## I riquadri avanzati non sono un elenco di lavori mancanti

Il28/10 l’utente osserva Console, Syslog, Audit, NTP, Storage, Access, restrizioni IP e2FA e chiede quante cose dipendano dalla rete di casa. La distinzione iniziale banco/rete torna utile a un livello più fine: una funzione disponibile non impone di attivarla. Syslog richiede un ricevitore; la restrizione IP richiede i client definitivi; debug e script richiedono un problema reale. Il system dataset su tank è invece già osservato e non deve essere spostato per il solo fatto che esista Configure.

Prima, la procedura di continuità si limitava al principio reale:

```text
Non si presume che vecchi nomi di interfaccia e collegamenti fisici coincidano: si verifica la rete dalla console e si recupera l’accesso amministrativo.
```

Il nuovo documento tecnico10 rende esplicito il criterio operativo:

```text
Le impostazioni avanzate si cambiano quando esistono un bisogno, una dipendenza disponibile e una verifica dell’esito.
```

La [guida al banco e a casa](../../docs/03-spunti-di-sviluppo/02-storage-di-rete-nas/10-configurazione-al-banco-e-in-rete-domestica.md) registra il valore letto e il momento della configurazione per ogni pannello. S241 chiarisce default, NTP, accessi, dataset di sistema e limite delle repliche; S242 collega la2FA del NAS all’ora e al recupero. La2FA Google attiva protegge un’altra identità e non viene annullata dal Disabled di TrueNAS. Questo permette di avanzare con dataset e permessi mentre restano espliciti i controlli da applicare nella rete finale.

Il secondo export con seed contiene ora tank e preserva le impostazioni precedenti; la prima generazione è conservata. Il raccordo documentale del29/10 chiude questa acquisizione, senza promuovere una copia sul PC a ripristino già provato. Il passo successivo legge Datasets e non ripete l’esportazione appena verificata per una semplice navigazione.
