# Metriche in tempo reale con Netdata

Ritorno allo [studio](README.md). Studio del 15/10/2026, nato da una segnalazione dell'utente: il progetto [Netdata](https://github.com/netdata/netdata) come possibilità per sorvegliare le macchine del laboratorio di casa, e in generale dove serva vedere come stanno. La domanda a cui risponde questo documento è se Netdata sia il candidato giusto per l'unica voce di monitoraggio rimasta pendente nel [piano unificato](10-piano-unificato-hardware-e-stack.md), cioè il raccoglitore di metriche, e che cosa comporterebbe adottarlo nella rete già decisa. Fonti S106, S107, S108 e S109 del [registro](../../../SOURCES.md).

Stato al 15/10/2026: nessuna decisione. Netdata entra nel progetto come candidato proposto, non come scelta, e nulla è installato né misurato sulle macchine di casa. I numeri di consumo di risorse scritti qui sono dichiarazioni del produttore, etichettate come tali, e la sezione sulla misura dice come sostituirli con letture vere.

## Il buco che riempirebbe

Il monitoraggio del progetto è deciso dall'8/10/2026 con ADR-028 e descritto in [Monitoraggio di sicurezza con Wazuh e Suricata](11-monitoraggio-wazuh-suricata.md): Wazuh al centro, Suricata dentro OPNsense, syslog dagli apparati. Quel flusso risponde a che cosa è successo, cioè accessi, processi, modifiche ai file, regole del firewall che scattano, pacchetti riconosciuti da una firma. Non risponde a come sta andando: quanto è carico il processore del server mentre l'indicizzatore scrive, quanto spazio resta nel pool del NAS, a che temperatura lavora un disco, quanti bit al secondo passano sulla porta di trunk dello switch, quando una scheda di rete comincia a scartare pacchetti.

Sono due domande diverse e non si sostituiscono. Un *evento* è un fatto discreto con un prima e un dopo, e si conserva perché qualcuno lo leggerà dopo; una *metrica* è un numero campionato di continuo, e serve a vedere una tendenza e a confrontare due istanti. Il piano unificato lo riconosce già da sé: nella tabella dello stack la riga delle metriche di switch, access point e host è l'unica marcata come pendente, con un raccoglitore da scegliere. Netdata è una risposta possibile a quella riga, e questo studio la valuta.

La riga vale più di quanto sembri in un laboratorio domestico, perché due decisioni già prese producono numeri che qualcuno deve guardare. ADR-028 mette Suricata sul firewall e chiede di misurare il carico dell'i3 prima e dopo l'accensione: senza un raccoglitore quella misura si fa a mano, una volta, e non si rivede più. ADR-034 fissa una soglia in token al secondo e in memoria residente per decidere se tenere il modello linguistico locale, e la memoria residente di un processo durante un carico di minuti è esattamente ciò che un raccoglitore di metriche legge senza che nessuno stia davanti allo schermo.

## Che cos'è, in fatti verificabili

Netdata è un agente di monitoraggio che campiona al secondo, con dashboard propria, allarmi inclusi e rilevamento automatico di ciò che gira sulla macchina. L'agente è sotto licenza GPL-3.0; l'interfaccia utente non è aperta, pur essendo utilizzabile gratuitamente, e Netdata Cloud è un servizio chiuso con un piano gratuito e piani a pagamento (S106). Il repository esiste dal giugno 2013, al 15/10/2026 ha circa 81.000 stelle e un aggiornamento dello stesso giorno, e l'ultima versione pubblicata è la 2.12.1 dell'8/10/2026 (S106). È quindi l'opposto del caso colibri: un progetto vecchio di dodici anni, con una società dietro e un modello commerciale dichiarato.

I fatti che contano per la decisione vengono tutti dalla documentazione del progetto. La raccolta è al secondo e la conservazione è a livelli, cioè al secondo, al minuto e all'ora, scelti automaticamente in base allo zoom; il progetto dichiara circa mezzo byte per campione, scrittura su disco ogni diciassette minuti con compressione ZSTD, e la possibilità di tenere tutto in memoria senza scrivere nulla su disco (S106). La durata della conservazione la decide lo spazio disponibile. Il catalogo dichiara oltre ottocento integrazioni, fra risorse di sistema, contenitori, macchine virtuali, sensori hardware, servizi e applicazioni, con il supporto di OpenMetrics e StatsD; l'apparato di rete si legge via SNMP[^1] con un raccoglitore dedicato. Ogni agente addestra sul posto un modello statistico per metrica e segnala i valori anomali, senza mandare niente fuori. Gli allarmi sono centinaia e già scritti, e le notifiche vanno a posta elettronica e a una lista di servizi di messaggistica (S106).

Un agente può trasmettere le proprie metriche a un altro agente, detto *parent*, che le conserva più a lungo, mostra tutti i nodi in una dashboard sola e tiene gli allarmi; la catena può avere più livelli (S106). È la forma che conta qui, perché permette un punto unico di consultazione senza mandare niente a un servizio esterno: Netdata Cloud è facoltativo, e il progetto dichiara che i dati restano nella propria infrastruttura.

Il raccoglitore SNMP, che è la parte che riguarda switch e access point, interroga qualunque apparato che esponga SNMP, riconosce il modello confrontando `sysObjectID` e `sysDescr` con un catalogo di profili e ne ricava il traffico per porta, i pacchetti, gli errori, gli scarti e lo stato amministrativo e operativo di ogni interfaccia; parla SNMP v1, v2c e v3, e sa anche scoprire da sé gli apparati di una sottorete, ma la scoperta è spenta per impostazione predefinita (S108). Due avvertenze della stessa pagina pesano sulla configurazione: un apparato poco potente può non rispondere in tempo, e conviene allora allungare il periodo di interrogazione; e la configurazione del raccoglitore dall'interfaccia richiede un piano Cloud a pagamento, mentre il file `go.d/snmp.conf` resta gratuito e si modifica con `edit-config`.

## Dove starebbe, nella rete già decisa

La forma che rispetta le decisioni prese è un parent sul server Proxmox e un agente su ogni macchina che ha senso sorvegliare, più l'interrogazione SNMP degli apparati fatta dal parent.

| Componente | Dove | Che cosa fa | Stato |
|---|---|---|---|
| parent Netdata | macchina virtuale o contenitore sul server Proxmox, VLAN 30 | raccoglie i figli, conserva lo storico, tiene allarmi e dashboard | proposto |
| agente | server Proxmox stesso, macchine del laboratorio, PC fissi della VLAN 10 | metriche della macchina, trasmesse al parent | proposto |
| raccoglitore SNMP | dentro il parent | traffico e stato per porta dello switch XMG1915 e dei due NWA130BE | proposto |
| agente sul firewall | OPNsense, plugin `netdata` | metriche del firewall senza SNMP | da verificare |

Il NAS è il punto incerto, per la stessa ragione già scritta per Wazuh: TrueNAS SCALE non è pensato per installarvi software estraneo, quindi o si accetta di leggerlo via SNMP, che TrueNAS espone, o non lo si sorveglia con un agente. La scelta non è obbligata adesso.

Sul firewall esiste un plugin, e va presentato per quello che è. Nel repository dei plugin di OPNsense la cartella `net-mgmt/netdata` esiste, con versione 1.2 revisione 1, descrizione «Real-time performance monitoring», un manutentore a titolo personale e la sola dipendenza dal pacchetto FreeBSD `netdata` (S109). Non esiste una pagina del manuale ufficiale che lo descriva, a differenza di `os-wazuh-agent`, che il manuale documenta pur dichiarandolo a supporto comunitario molto limitato (S93). La lettura prudente è che il plugin stia nella stessa categoria di fragilità, o in una peggiore, e che il firewall sia il posto dove conviene meno aggiungere software: la via senza plugin è interrogare OPNsense via SNMP dal parent, perdendo la profondità delle metriche interne e guadagnando una dipendenza in meno su una macchina che deve stare in piedi.

## I percorsi dei dati

Le porte sono quelle predefinite del progetto. Gli indirizzi sono quelli del piano di indirizzamento, e restano proposte finché la rete non esiste.

| Da | A | Che cosa | Porta | Stato |
|---|---|---|---|---|
| agenti su host delle VLAN 10, 30 e 60 | parent, VLAN 30 | trasmissione delle metriche | TCP 19999 | proposto |
| parent, VLAN 30 | switch e access point, VLAN 99 | interrogazione SNMP | UDP 161 | proposto |
| workstation ADMIN e tunnel WireGuard | dashboard del parent | consultazione | TCP 19999 | proposto, solo dalla VLAN 99 |
| parent | Internet | Netdata Cloud, telemetria anonima, aggiornamenti | TCP 443 | da negare, salvo decisione contraria |

L'ultima riga è una scelta di progetto, non una limitazione del prodotto: l'agente funziona per intero senza collegarsi al servizio del produttore, e in un laboratorio che documenta la rete di una casa il percorso che porta metriche fuori si apre solo se qualcuno lo decide, sapendo che cosa porta con sé.

La dashboard nella VLAN 99 è la stessa regola di ADR-025 applicata a un servizio nuovo: le interfacce di amministrazione ascoltano dove ascoltano le altre, e non si raggiungono dalla rete di casa. Se il parent vive nella VLAN 30 insieme a Wazuh, gli serve la stessa seconda scheda di rete nella VLAN 99 che la macchina virtuale di Wazuh ha già, oppure si accetta una regola puntuale dalla sola workstation ADMIN verso il suo indirizzo e la sua porta.

## Il punto delicato: la dashboard non chiede credenziali

È il fatto che decide la configurazione, e va scritto prima dei pregi. La dashboard locale dell'agente non è autenticata per impostazione predefinita, ascolta sulla porta 19999 e il valore predefinito di `allow connections from` è `localhost *`, cioè accetta anche le connessioni esterne; su un indirizzo pubblico sarebbe accessibile a chiunque (S107). Il progetto stesso lo dichiara e indica le difese disponibili: legare l'ascolto a un indirizzo preciso con `bind to` nella sezione `[web]` di `netdata.conf`, restringere con `allow connections from` e le sue varianti per funzione, cifrare con SSL, mettere davanti un proxy inverso che autentichi, far passare la consultazione dal parent invece che dai singoli nodi, oppure attivare la protezione con token. La protezione con token richiede che l'agente sia collegato a Netdata Cloud, quindi in questo progetto non è una via, e disattivare del tutto la dashboard con `mode = none` non si fa su un parent, perché chiuderebbe anche i flussi dei figli (S107).

Ne segue una configurazione minima, da scrivere nel documento di messa in opera il giorno in cui si decidesse di adottarlo. Sugli agenti figli la dashboard locale si lega al solo indirizzo necessario alla trasmissione, o si restringe alla sorgente del parent. Sul parent l'ascolto si lega all'indirizzo della VLAN 99 e all'indirizzo locale, non a tutte le interfacce. Le regole del firewall fra le zone restano l'ultima barriera e non la prima, perché un servizio che ascolta ovunque dentro la propria VLAN è già esposto a tutto ciò che in quella VLAN si trova, e la VLAN 60 del laboratorio è per definizione il posto dove girano cose di cui non ci si fida.

## Che cosa costa

Il produttore dichiara circa il cinque per cento di un processore e circa 150 MiB di memoria su un sistema di produzione con le impostazioni predefinite, e sotto l'uno per cento e circa 100 MiB spegnendo apprendimento automatico e allarmi e tenendo i dati in memoria (S106). Sono dichiarazioni del produttore, non misure di questo progetto, e il numero che conta qui non è quello dell'agente singolo ma quello del parent, che tiene lo storico di tutti i nodi e che il produttore non quantifica in una riga sola.

Il bilancio della memoria del server è stretto e già scritto: 24 GB dopo ADR-032, di cui 8 a Wazuh, 2 a Proxmox, mezzo ad AdGuard Home, e circa 12 che restano al laboratorio. Un parent con un paio di gigabyte toglierebbe quelli al laboratorio, non a Wazuh. Sul disco il conto si fa in anticipo, perché il progetto dichiara circa mezzo byte per campione: mille metriche campionate al secondo per trenta giorni stanno sotto il gigabyte e mezzo nella sola risoluzione al secondo, che è poco rispetto ai 50 GB di Wazuh. Resta da decidere quanto storico tenere, e la risposta onesta è che in una casa la risoluzione al secondo serve per i giorni recenti e per capire un episodio, mentre per la tendenza bastano i livelli aggregati.

Sul consumo elettrico non si aggiunge niente: le macchine che il parent sorveglia sono accese comunque, e il parent gira su una di esse. Il costo vero è di attenzione, cioè una dashboard in più da guardare e allarmi in più da regolare, e si paga solo se gli allarmi si leggono.

## Le alternative già in tabella

Il progetto non arriva a Netdata a mani vuote, e le voci già censite vanno confrontate invece che ignorate.

| Candidato | Che cosa copre | Perché Netdata se ne distingue |
|---|---|---|
| [Beszel](https://github.com/henrygd/beszel), già in [Servizi gratuiti](02-servizi-gratuiti.md) | processore, memoria, dischi e contenitori di più host, con agenti leggeri | molto più leggero e molto più povero: niente SNMP, niente metriche per servizio, niente allarmi strutturati |
| [LibreNMS](https://docs.librenms.org/), già in [Servizi gratuiti](02-servizi-gratuiti.md) con priorità P2 | apparati di rete via SNMP, con storico per porta e mappa | è la specialità opposta: forte sugli apparati, debole sugli host, e chiede un suo stack con base di dati e server web |
| Prometheus con Grafana, citato nel laboratorio di [Autore-LinkedIn-B](../21-idee-setup-da-profili-linkedin-interessanti/02-home-lab-cybersecurity-infrastructure-autore-linkedin-b.md) | metriche di qualunque cosa esponga un punto di raccolta, con pannelli costruiti a mano | due componenti da installare, configurare e aggiornare, più gli esportatori; più potente sul lungo periodo e molto più lavoro per arrivare alla prima schermata |
| Zabbix, citato nel [nodo di diagnostica](../09-monitoraggio/01-nodo-di-analisi-e-diagnostica-rete.md) | host e apparati insieme, con server, base di dati e agenti | copre lo stesso perimetro di Netdata con un impianto più pesante e una configurazione più esplicita; è la scelta di chi vuole modellare tutto |
| Uptime Kuma, già P1 in [Servizi gratuiti](02-servizi-gratuiti.md) | se un servizio risponde | non è un'alternativa ma il complemento: dice se qualcosa è vivo, non come sta |

Il motivo per cui Netdata è il candidato naturale di questo progetto è che tiene insieme host e apparati in un pezzo solo, senza un secondo stack da mantenere, e mostra qualcosa di utile dieci minuti dopo l'installazione invece che dopo un pomeriggio di pannelli. I motivi per diffidarne sono due e vanno scritti con la stessa chiarezza: l'interfaccia non è aperta e la configurazione di alcune parti dall'interfaccia è riservata a un piano a pagamento (S106, S108), quindi una parte del valore sta fuori dalla licenza libera; e il prodotto spinge verso il proprio servizio in rete, che in questo progetto resta chiuso per scelta.

## Quello che resta da verificare prima di decidere

Quattro cose, nessuna delle quali si chiude leggendo documentazione. Se il plugin `netdata` di OPNsense sia presente nell'elenco dei plugin della versione installata e se funzioni, oppure se si rinunci all'agente sul firewall e lo si legga via SNMP. Se i profili SNMP del catalogo riconoscano lo XMG1915 e i NWA130BE, cosa che si sa solo interrogandoli una volta comprati, e che intanto non blocca niente, perché il traffico per porta si ricava dalla IF-MIB[^2] standard anche senza un profilo di marca. Quanto occupa davvero il parent sul server, cioè memoria residente e spazio su disco dopo una settimana con il numero di nodi reale. E se gli allarmi di Netdata si sovrappongano a quelli di Wazuh al punto da dover spegnere qualcosa, perché due sistemi che mandano la stessa notifica producono l'effetto opposto a quello voluto, cioè notifiche che non si leggono più.

## Da dove si riparte

La decisione spetta all'utente e non è urgente: il raccoglitore di metriche è pendente dall'8/10/2026 e non blocca la rete, che si configura comunque. Se la risposta è sì, Netdata entra nello stack del piano unificato al posto della riga pendente, con stato proposto, e la messa in opera si colloca dopo Proxmox e dopo Wazuh, perché sorvegliare una macchina ha senso quando la macchina fa qualcosa. Se la risposta è no, la riga resta pendente con LibreNMS e Zabbix come candidati già censiti.

L'occasione più vicina per provarlo senza impegno è il nodo di laboratorio: un agente installato lì durante la misura di ADR-034 darebbe la memoria residente e il carico del processore durante l'inferenza senza stare davanti allo schermo, che è uno dei quattro numeri che quella misura chiede. È un uso di un pomeriggio, su una macchina accesa a richiesta e in una VLAN senza uscita, e non impegna il progetto ad adottarlo.

[^1]: *SNMP*, Simple Network Management Protocol - protocollo con cui un sistema di gestione interroga apparati di rete per leggerne contatori e stato, per esempio il traffico di ogni porta di uno switch. Nel progetto è già citato come requisito degli access point confrontati.

[^2]: *IF-MIB* - la porzione standard dell'albero informativo SNMP che descrive le interfacce di rete di un apparato, uguale per tutti i costruttori, da cui si leggono traffico, errori e stato di ogni porta senza bisogno di conoscere il modello.
