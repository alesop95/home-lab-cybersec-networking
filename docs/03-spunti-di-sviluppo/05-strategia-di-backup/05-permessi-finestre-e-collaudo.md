# Permessi, finestre e collaudo dei backup

Questo documento accompagna le [procedure di recupero](04-procedure-di-backup-e-ripristino.md). Le regole e gli orari aggiuntivi sono proposte del 19/10/2026, non configurazioni applicate. Il [contratto fra le zone](../23-studio-home-lab/08-regole-fra-le-zone.md) e l'[accesso amministrativo](../23-studio-home-lab/09-accesso-amministrativo.md) rimangono il riferimento di rete; gli scarti rilevati qui vanno riconciliati prima dell'attivazione.

## Una destinazione per ogni autorizzazione

La condivisione degli archivi PVE usa un dataset figlio dedicato, separato dai documenti originali e dai backup endpoint. Ogni writer ha un'identità propria e accesso al solo contenitore di sua competenza. Per il job PVE servono creazione, lettura, scrittura e rimozione degli archivi secondo il ciclo di conservazione; chiamarlo utente di backup non impedisce di cancellare ciò su cui può scrivere. Un'identità distinta di recupero può avere sola lettura quando lo strumento lo consente. Per restic va verificata anche la gestione dei lock: il riferimento offre --no-lock soltanto per alcune operazioni su repository di sola lettura. Non lo si aggiunge indiscriminatamente ai job; si prova un percorso di recupero da copia ferma e senza manutenzioni concorrenti, lasciando separate le credenziali dei writer. [Opzioni restic](https://restic.readthedocs.io/en/stable/manual_rest.html).

Il preset iniziale non basta a dimostrare l'isolamento: TrueNAS distingue ACL della share e ACL del filesystem. Le prime non proteggono lo stesso percorso da altri protocolli o altre share; le seconde vanno controllate anche per accessi ereditati e gruppi ampi. Si usa un gruppo dedicato e si verifica che gli account di backup non ottengano accesso ai documenti tramite gruppi predefiniti. [SMB e permessi nella versione stabile 25.10](https://www.truenas.com/docs/scale/25.10/scaletutorials/shares/smb/).

| Identità logica proposta | Destinazione | Permesso necessario | Permesso da non attribuire per comodità |
|---|---|---|---|
| writer PVE | dataset archivi PVE sul NAS | gestione dei soli archivi ammessi dal job | amministrazione NAS, accesso ai documenti e ai repository endpoint |
| writer endpoint singolo | proprio repository NAS | operazioni richieste dallo strumento e dalla manutenzione | lettura o modifica dei backup degli altri endpoint |
| lettore documenti NAS dal server | soli documenti selezionati sul NAS | sola lettura, più eventuale attraversamento dei parent necessari | scrittura sugli originali, lettura degli archivi guest |
| operatore recupero | sola copia da recuperare | lettura del contenuto e accesso separato al segreto di cifratura | amministrazione permanente di tutte le copie |
| amministratore NAS | configurazione e gestione dei dataset | privilegi amministrativi per operazioni esplicite | utilizzo della stessa identità nei job ordinari |

Le password SMB, la password del repository restic e le passphrase dei dataset sono materiali diversi. Non si inseriscono nella riga di comando, nei verbali pubblici o in una cronologia di shell. L'automazione usa un archivio di segreti o un file privato leggibile soltanto dall'identità del job, con copia di emergenza fuori dalle macchine protette. La documentazione restic offre `--password-file` e `--password-command`; la scelta della custodia resta da attuare, non si presume un gestore già disponibile. [Preparazione del repository](https://restic.readthedocs.io/en/stable/030_preparing_a_new_repo.html).

Il flag Protected di PVE e un'istantanea locale non equivalgono a una copia inattaccabile. Nel modello di rischio si distinguono compromissione del guest, dell'endpoint, dell'host PVE e dell'amministratore NAS. Un guest senza credenziali SMB della destinazione ha meno accesso; il root dell'host PVE può leggere la credenziale del proprio storage. Un amministratore NAS può intervenire sul pool e sulle istantanee. La copia scollegata o con amministrazione indipendente resta necessaria per coprire quei guasti comuni e non è stata ancora assegnata.

## I flussi che mancano al contratto corrente

Il piano server colloca la gestione del nodo PVE soltanto in VLAN 99; la destinazione dati del NAS è proposta in VLAN 30. La regola 3 della VLAN 99 blocca le connessioni verso le reti interne. Dal confronto documentale segue che il job PVE verso SMB necessita una nuova eccezione circoscritta prima di quel blocco. Non è un esito di prova sul firewall attivo.

Si propone l'alias `PVE_HOST` per il solo indirizzo di gestione del nodo, ancora da riservare. Non si riutilizza `HOST_SERVIZI`, che descrive una destinazione della VLAN 30, e non si sposta il nodo di gestione nella VLAN dei guest per evitare la regola.

| Origine | Destinazione | Protocollo/porta | Posizione proposta | Uso |
|---|---|---|---|---|
| PVE_HOST in VLAN 99 | NAS dati, alias NAS in VLAN 30 | TCP 445 | prima del blocco verso RETI_INTERNE della VLAN 99 | archivi guest e prelievo documenti con credenziali separate |
| ADMIN dalla VLAN 10 | solo PVE_HOST | TCP 8006 | prima del blocco verso RETI_INTERNE della VLAN 10 | GUI/API PVE |
| WG_RETE | solo PVE_HOST | TCP 8006 | prima del blocco finale WireGuard | amministrazione PVE dal tunnel |

Il riferimento ufficiale conferma che pveproxy usa HTTPS sulla porta TCP 8006. L'alias generale PORTE_GESTIONE contiene oggi 22 e 443 e l'elenco GESTIONE non comprende il nodo PVE. La proposta aggiunge una destinazione e una porta specifiche, da verificare anche per eventuale accesso SSH amministrativo; non apre 8006 verso tutti gli apparati. [pveproxy, descrizione e ascolto](https://raw.githubusercontent.com/proxmox/pve-docs/master/pveproxy.adoc).

La porta fisica di recupero in VLAN 99 condivide invece il segmento del nodo: il traffico nello stesso dominio di livello 2 non viene filtrato dalle sole regole instradate di OPNsense. Per SMB si propone il bind al solo indirizzo dati del NAS, lasciando quello di gestione fuori dall'ascolto: il campo Bind IP Addresses della versione 25.10, se vuoto, ascolta su tutte le interfacce attive. Si collauda questo vincolo con accesso locale disponibile e un client per ciascun percorso. Eventuali filtri sull'host e restrizioni del servizio completano il controllo; il firewall non isola da solo due peer della stessa VLAN. [Ascolto del servizio SMB](https://www.truenas.com/docs/scale/25.10/scaleuireference/systemsettings/services/smbservicesscreen/).

L'endpoint fidato usa il percorso VLAN 10 verso NAS già previsto; la share dedicata è protetta dalle ACL. Gli esperimenti in VLAN 60 non ricevono per default credenziali o un'apertura SMB. Il backup del loro disco può essere prelevato dall'host secondo la selezione PVE senza aprire il laboratorio verso la casa. La registrazione dei flussi non contiene password e deve consentire di riconoscere sia un accesso ammesso sia un accesso negato.

L'alternativa PBS ha [identità, flussi e manutenzioni propri](09-confronto-archivi-proxmox-e-pbs.md), da approvare soltanto se scelta e qualificata. La matrice SMB sopra descrive il percorso iniziale degli archivi; non autorizza automaticamente un servizio PBS o una nuova destinazione di rete.

## Quote e spazio trattenuto dalle istantanee

I dataset proposti distinguono archivi PVE, repository per endpoint e documenti originali; gli export di configurazione sono un insieme sensibile da custodire fuori dal NAS. Le quote di ciascun insieme derivano dal suo picco misurato e la loro somma non deve far scomparire il margine del pool. Una quota non crea una seconda copia e non rende indipendenti dataset che condividono gli stessi dischi.

TrueNAS espone limiti per il dataset e per dataset con figli, riserve e soglie di allarme. Prima di inserire un valore si controllano unità effettive e perimetro, includendo lo spazio delle istantanee nella contabilità appropriata. Il tetto proposto di 180 GB decimali non va trascritto come 180 GiB per somiglianza del numero. Il test di quota usa dati artificiali e verifica che il rifiuto riguardi il writer corretto senza saturare il pool. [Gestione delle quote](https://www.truenas.com/docs/scale/25.10/scaletutorials/datasets/datasetsscale/), [campi Capacity Settings](https://www.truenas.com/docs/scale/25.10/scaleuireference/datasets/capacitysettingsscale/).

Per gli archivi guest completi si propone inizialmente di evitare istantanee periodiche ricorsive che trattengano generazioni già rimosse dal pruning; la conservazione si affida ai punti espliciti e alla futura copia indipendente. Se si scelgono istantanee di quel dataset per un diverso rischio, si assegna loro un budget separato e si ripete il calcolo. I documenti originali possono avere una politica diversa. Nomi, ricorsione ed esclusioni devono risultare nel verbale: un'istantanea del parent può includere figli che si pensava di avere escluso.

## Finestre e obiettivi proposti

La finestra decisa per il NAS resta quella del [piano di accensione](../02-storage-di-rete-nas/05-consumo-elettrico-e-finestra-di-accensione.md): 07:30-23:30 nelle giornate con arresto ordinario, con estensione fino alle 02:30 successive per venerdì e sabato. Ogni scheduler dovrà usare un fuso esplicito e registrare l'ora effettiva con offset; il cambio d'ora non si risolve con un generico conteggio settimanale.

La proposta di prima qualificazione riserva 09:00-12:00 ai job ordinari selezionati, eseguiti senza sovrapposizione. L'ora di avvio non è ancora applicata: prima si misura che NAS e server siano raggiungibili, che gli endpoint interessati siano accesi e che il primo backup completo termini nel tempo ammesso. Se il NAS o un endpoint mancano, il giro è saltato o fallito e il registro della copia riuscita non avanza. Un recupero automatico dei job persi va configurato esplicitamente nella versione scelta e mantenuto entro la finestra.

La verifica dei repository, il pruning, le istantanee, lo scrub e un ripristino completo possono costare più della scrittura ordinaria. Si riservano turni separati misurati e si evita di avviarli contemporaneamente per poi usare una velocità ottenuta a macchina scarica. Il calcolatore stima prima corsa e corsa ordinaria; non comprende da sé il costo di ogni prova o manutenzione.

Prima di rendere operativo lo spegnimento programmato serve un coordinamento verificato che rilevi scritture e manutenzioni attive, impedisca nuovi avvii tardivi e segnali un superamento della finestra. Un semplice orario di cron non dimostra questo coordinamento. La proposta è rinviare l'arresto automatico in caso di lavoro ancora attivo e registrare il motivo, con una politica amministrativa esplicita; non spegnere il NAS nel mezzo del job per mantenere il risparmio stimato.

| Oggetto | Obiettivo di progetto proposto | Quando diventa un risultato misurato |
|---|---|---|
| file irrinunciabili NAS/endpoint | perdita massima auspicata di 24 ore quando sorgente e destinazione sono disponibili ogni giorno | età dell'ultimo punto riuscito e recuperabile confrontata col dato che si vuole recuperare |
| VM di servizio selezionate | un punto riuscito al giorno, inizialmente due punti conservati se ammessi dallo spazio | più giri reali, recupero del guest e misura della dimensione delle generazioni |
| configurazione host/NAS | salvataggio dopo ogni modifica significativa e prima di aggiornamenti | export leggibile da un'altra macchina e prova di recupero pertinente |
| tempo di recupero | da misurare per file, guest, host e pool; nessun valore garantito | cronometro dall'inizio dell'incidente fino a dati e servizio verificati, inclusi attesa NAS, credenziali e preparazione |

Due punti conservati limitano la profondità del recupero e possono entrambi essere successivi a una corruzione scoperta tardi. Non si promette uno storico lungo finché spazio e frequenza delle modifiche non sono noti. Se il dimensionamento fallisce, si riduce esplicitamente il perimetro o si sceglie una destinazione più capiente: non si cancella l'ultima copia valida per far diventare verde l'ammissione.

## Collaudo che distingue un recupero da un file presente

Ogni prova ha originale identificato, destinazione distinta, risultato atteso scritto prima e un passaggio discriminante. Prima si usano contenuti artificiali riconoscibili, senza documenti personali. I dati reali entrano soltanto nel censimento e nella protezione scelti dall'utente; l'agente non li apre per progettare questa procedura.

| Prova futura | Preparazione | Passaggio discriminante | Evidenza da conservare |
|---|---|---|---|
| file cancellato o versione precedente | due versioni artificiali diverse, backup identificati, poi modifica del solo originale di prova | recuperare l'ID previsto in cartella vuota e ottenere l'impronta della versione attesa, diversa da quella corrente | ID e ora del punto, hash atteso/ottenuto, byte e percorso logico |
| VM recuperata | guest di prova con dato e servizio attesi, backup, target isolato e ID libero | avviare la copia e leggere il dato salvato attraverso il servizio previsto | log backup/restore, verifica del contenuto, prova funzionale, isolamento e tempo |
| contenitore con dato esterno | file artificiale nel rootfs e nel bind mount, perimetro dichiarato | verificare quale dato è recuperato e coprire separatamente il mount escluso | esito esplicito sul contenuto esterno, senza chiusura parziale travestita da completa |
| separazione delle ACL | identità autorizzata e identità priva di accesso, file artificiali dedicati | primo account crea/legge secondo i diritti; secondo account non legge né modifica quel dataset | esito per account anonimizzato, share, permesso, data e log pertinente |
| NAS non disponibile | repository distinto del NAS pronto e materiale di apertura indipendente | recuperare dal server o supporto senza montare l'originale NAS | elenco logico, hash e materiali di avvio realmente usati |
| avvio di emergenza endpoint | ISO/supporto di recupero e backup identificati | rilevare rete, dischi e backup senza usare il sistema Windows installato | modalità di boot, driver, raggiungibilità e assenza di scritture sugli originali |
| recupero integrale endpoint | disco di prova sostitutivo identificato e originale protetto | ripristinare e avviare il sistema con applicazioni e dati verificati | destinazione, capacità, mappatura, versione e durata completa |

Una prova preliminare di avvio non equivale a un recupero integrale. Una verifica degli hash di pochi file non prova la completezza dell'intero insieme. Il verbale riporta il perimetro effettivo e le esclusioni, insieme agli eventuali errori che impediscono la chiusura. Per i metadati si provano almeno permessi e attributi dichiarati necessari, non solo il contenuto dei file.

Si ripete il recupero dopo la prima installazione, dopo cambi sostanziali di versione, layout, cifratura o permessi e, come proposta iniziale, con un campione mensile e una prova più ampia trimestrale. Queste frequenze restano da confermare con dimensioni e costi reali. Non esiste al 19/10 un verbale di queste prove né un allarme di mancato backup già installato.
