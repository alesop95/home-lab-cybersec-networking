# Fascicolo di emergenza della rete

Il [piano dei backup](02-piano-di-backup-e-ripristino-del-lab.md) deve consentire di raggiungere le copie anche dopo la perdita della configurazione di rete. OPNsense è installato ma la rete segmentata non è configurata; switch e access point non risultano ancora installati. Questo è il procedimento da predisporre, non il verbale di un export già eseguito.

## Il contenuto che deve sopravvivere ai servizi

Un fascicolo privato raccoglie configurazioni esportate, versioni, mappatura fisica delle porte, indirizzi effettivi di gestione e materiali per autenticarsi. Il repository pubblico conserva il disegno con i segnaposto; non può sostituire il fascicolo con i valori necessari al recupero. Il livello privato ignorato da git non riceve una copia di sicurezza perché esiste il remoto pubblico: anche la sua custodia va assegnata.

La proposta prevede un archivio cifrato leggibile da una macchina di recupero e una copia fuori da NAS e server. Il supporto non è ancora assegnato e non si presume disponibile un altro SSD o un abbonamento cloud. La chiave per aprire l'archivio deve essere recuperabile separatamente: non basta conservarla dentro l'archivio stesso o nel solo servizio che si sta tentando di riavviare. Il supporto attualmente usato per Memtest non viene modificato da questa progettazione.

| Oggetto | Materiale da conservare in privato | Quando aggiornarlo |
|---|---|---|
| firewall OPNsense | export completo protetto, versione installata, nome logico delle interfacce e mappatura delle prese WAN/LAN/trunk | dopo la prima configurazione, dopo modifiche significative e prima degli aggiornamenti |
| switch futuro | configurazione salvata/esportata secondo modello e firmware, VLAN, PVID, tagging, porta di gestione e porta di recupero | dopo il collaudo del cablaggio e dopo ogni variazione |
| access point futuri | export se supportato, oppure manifest di SSID, VLAN, rete di gestione e parametri radio necessari | dopo adozione e variazioni; credenziali in custodia separata |
| NAS e nodo PVE | export e inventario previsti dalle procedure NAS-01 e HOST-01 | a ogni variazione di rete, storage o accesso |
| accesso di emergenza | account e chiavi amministrative, recupero del secondo fattore ove previsto, password degli export e sblocco dei repository | quando cambiano i materiali, verificando la copia di emergenza |
| istruzioni e installer | sequenza di recupero, manuali pertinenti, versioni e supporti necessari | dopo modifiche di procedura o di versione |

Gli export possono contenere chiavi VPN, certificati, password e identificativi: restano fuori da git e dai verbali pubblici. Si prova la lettura dalla macchina di recupero senza copiare i valori nella documentazione versionata. Il contenuto del fascicolo va inventariato senza riutilizzare una password amministrativa come password comune di tutti gli archivi.

## RETE-01: esportare la configurazione OPNsense

Quando il firewall sarà configurato si userà System > Configuration > Backups per un export completo, con protezione tramite password e scelta esplicita sull'inclusione delle statistiche RRD. Il file e la password vanno custoditi secondo il fascicolo, con data, versione e impronta della copia. La cronologia sul firewall non sostituisce una copia fuori dal suo dispositivo di avvio. [Configurazione e backup OPNsense](https://docs.opnsense.org/manual/backups.html).

La prima prova di recupero usa un ambiente separato e isolato dalla rete attiva. Si identifica il file esatto e si verifica la possibilità di aprirlo; poi si recupera la configurazione completa sulla destinazione di prova. Un export parziale non è la scorciatoia predefinita, perché i componenti della configurazione hanno dipendenze. Su hardware diverso si controllano le assegnazioni delle interfacce dalla console: nomi diversi possono richiedere una correzione e impedire il riavvio automatico. Le impostazioni di console del backup sono escluse dall'importazione per default, secondo il manuale, e si verificano prima di cambiare questa scelta. [Limiti del ripristino OPNsense](https://docs.opnsense.org/manual/backups.html).

Il test si considera riuscito soltanto dopo aver verificato assegnazione delle porte, accesso di gestione dalla postazione prevista e almeno un flusso ammesso e uno negato del contratto. Non si collega una copia del firewall alla LAN attiva per vedere se parte: potrebbero essere ripristinati indirizzi, DHCP, tunnel e altre identità già in uso. Il punto atteso e la verifica discriminante entrano nel [verbale](07-modello-di-verbale-di-collaudo.md).

L'automazione remota resta successiva a questa prima qualificazione. La documentazione descrive backup remoti e un giro mattutino dopo le modifiche: un servizio ospitato sul NAS spento a quell'ora non costituisce una destinazione raggiungibile. Si controlleranno orario, risultato e copia recuperabile, mantenendo comunque il fascicolo fuori dai servizi del lab. Non si installa Nextcloud per creare una dipendenza di recupero del firewall dal server che il firewall deve rendere raggiungibile. [Backup remoto e pianificazione OPNsense](https://docs.opnsense.org/manual/how-tos/cloud_backup.html).

## RETE-02: switch e access point

Il modello e il firmware effettivamente installati determinano come salvare e ripristinare la configurazione. Prima si verifica che la configurazione corrente sia anche persistente dopo un riavvio; poi si esporta il file ove disponibile e si prova il recupero in una finestra predisposta. Non si inventano ora pulsanti o comandi per apparati ancora assenti. Se il dispositivo non offre un export, il manifest di ricostruzione deve essere sufficientemente preciso da rifare e collaudare le impostazioni.

Per lo switch il passaggio discriminante comprende tagging del trunk, VLAN delle porte di accesso e raggiungibilità della gestione dalla porta di recupero prevista. Per gli access point comprende l'associazione di un client di prova e la sua collocazione nella VLAN attesa, insieme al blocco di una destinazione non ammessa. Una schermata con gli stessi nomi SSID non prova la segmentazione. Gli export restano legati alla versione e al modello: la loro portabilità si verifica, non si presume.

## Ordine di recupero e accesso senza circoli

Si parte dall'incidente effettivo e dai componenti ancora disponibili. La [porta di recupero](../23-studio-home-lab/09-accesso-amministrativo.md) è utile quando lo switch conserva VLAN e porta 8 correttamente configurate; non supera da sola la perdita della configurazione dello switch. La console locale di firewall, NAS e nodo PVE è il percorso da predisporre quando il percorso instradato o lo switch non sono disponibili.

Il fascicolo distingue indirizzo di gestione, presenza di tag VLAN sulla porta del dispositivo e capacità del client di recupero. Non si presume che un collegamento diretto dal portatile possa raggiungere un'interfaccia soltanto taggata. La configurazione di emergenza va provata con console disponibile, senza collegare indiscriminatamente WAN, LAN e trunk a uno switch tornato a impostazioni piatte.

L'ordine di base proposto è recuperare la possibilità di leggere il fascicolo, predisporre l'accesso locale e ricostruire la gestione di firewall e switch necessari al percorso. Si raggiunge quindi il NAS o, se il NAS è guasto, la copia distinta sul server; si recuperano storage e guest con le [procedure dedicate](04-procedure-di-backup-e-ripristino.md). DNS filtrante, dashboard e altri guest non devono essere necessari per leggere l'unica copia delle credenziali di recupero di PVE. Si documenta come usare gli indirizzi di gestione anche senza il resolver abituale.

Se si ripristina il firewall, il collegamento esterno e i servizi che potrebbero interferire con la rete restano isolati fino alla verifica di porte e regole. Se manca soltanto un guest, non si ripristina l'intera rete per recuperarlo. Il tempo di recupero comprende ricerca del supporto, apertura dell'archivio, ricostruzione della gestione e attesa delle macchine spente, oltre al trasferimento dei dati.

## Stato al 20/10/2026

Nessun export di rete, supporto di emergenza o prova di ripristino di queste configurazioni è stato osservato nel lavoro autonomo. OPNsense richiede prima il censimento fisico e la configurazione prevista dalla roadmap; switch e access point richiedono installazione e collaudo. Il fascicolo è una condizione di accettazione da preparare a quelle tappe. La sua dimensione misurata entra fra le allocazioni fisse del budget della destinazione scelta, senza una quota inventata per far rientrare il calcolo.
