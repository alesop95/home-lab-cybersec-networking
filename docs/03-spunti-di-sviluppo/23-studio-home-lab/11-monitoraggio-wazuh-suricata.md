# Monitoraggio di sicurezza con Wazuh e Suricata

Ritorno allo [studio](README.md). Documento tecnico dell'8/10/2026 sul flusso di monitoraggio adottato dal [piano unificato](10-piano-unificato-hardware-e-stack.md) e approvato dall'utente (ADR-028): che cosa fa ogni componente, per quale percorso passa ogni dato, come si configura e in che ordine si mette in opera. Nulla è ancora installato: il server Proxmox che ospiterà Wazuh aspetta il disco e la conferma dell'hardware. I valori marcati come proposta si fissano all'installazione.

## Che cosa deve vedere il monitoraggio, e che cosa no

Il monitoraggio di una rete domestica segmentata deve rispondere a tre domande. Che cosa succede sugli host: processi, accessi, modifiche ai file di sistema, software vulnerabile. Che cosa passa sulla rete: connessioni verso indirizzi noti come malevoli, tentativi di sfruttare servizi, scansioni. Che cosa fanno gli apparati: accessi alle interfacce di gestione, regole del firewall che bloccano, cambi di configurazione. Le tre domande hanno tre sorgenti diverse, e il flusso le porta in un unico punto dove si correlano.

Non deve invece leggere il contenuto del traffico cifrato né diventare un archivio di tutto il traffico: in una casa i volumi sono piccoli ma i dati sono personali, e conservare più del necessario è un rischio in sé.

## I componenti

*Wazuh* è il centro. È composto da tre parti che nella configurazione scelta stanno sulla stessa macchina virtuale: il server, che riceve gli eventi, li decodifica e applica le regole che generano gli allarmi; l'indicizzatore, che conserva e rende interrogabili eventi e allarmi; la dashboard, l'interfaccia web. Con fino a 25 agenti la documentazione indica 4 vCPU, 8 GB di memoria e 50 GB di spazio per 90 giorni di allarmi (S87).

*L'agente Wazuh* gira sugli host. Raccoglie i log del sistema, controlla l'integrità dei file indicati, inventaria il software per confrontarlo con le vulnerabilità note, e manda tutto al server su una connessione cifrata.

*Suricata* è il motore di rilevamento sul traffico già incluso in OPNsense, alla voce Intrusion Detection. Confronta i pacchetti che attraversano le interfacce scelte con insiemi di regole, per esempio quello gratuito ET Open, e scrive gli allarmi in formato EVE JSON.

*Il plugin `os-wazuh-agent` di OPNsense* è l'agente Wazuh del firewall. Manda al server i log delle applicazioni del firewall scelte fra le destinazioni syslog e, se si marca l'opzione degli eventi di intrusion detection, gli allarmi di Suricata dallo stesso flusso EVE che usa OPNsense. Porta anche un'azione di risposta, `opnsense-fw`, che permette al server di far bloccare un indirizzo sorgente al firewall (S93). La documentazione avverte che il plugin è fornito così com'è, con un supporto della comunità molto limitato (S93): è il punto più fragile del flusso, e il paragrafo sul ripiego dice che cosa fare se si rompe.

## I percorsi dei dati

| Da | A | Che cosa | Porta | Stato |
|---|---|---|---|---|
| agenti sui PC della VLAN 10 | Wazuh, VLAN 30 | eventi degli host | TCP 1514 | proposto |
| agenti, alla prima registrazione | Wazuh | iscrizione dell'agente con la password di registrazione | TCP 1515 | proposto |
| OPNsense, plugin | Wazuh | log del firewall e allarmi di Suricata | TCP 1514 | proposto |
| switch e AP, VLAN 99 | Wazuh | syslog degli apparati | UDP 514 | proposto |
| NAS TrueNAS, VLAN 30 | Wazuh, stessa VLAN | syslog del NAS | UDP 514 | proposto, non attraversa il firewall |
| macchine del laboratorio, VLAN 60 | Wazuh | eventi degli host di prova | TCP 1514 e 1515 | proposto, facoltativo |
| workstation ADMIN e tunnel | dashboard di Wazuh, VLAN 99 | consultazione | TCP 443 | proposto |

Le porte sono quelle della documentazione di Wazuh: 1514 TCP per la connessione degli agenti, 1515 TCP per la registrazione, 514 UDP per il raccoglitore syslog, che è spento finché non lo si configura, 443 TCP per la dashboard (S92). La porta 55000 dell'interfaccia di programmazione del server e la 9200 dell'indicizzatore non devono essere raggiungibili da nessuna zona: servono solo dentro la macchina virtuale.

La macchina virtuale di Wazuh ha due schede di rete virtuali. La prima nella VLAN 30, indirizzo `192.168.30.30` proposto, riceve agenti e syslog. La seconda nella VLAN 99, dove si lega la dashboard, così che la consultazione rispetti la regola dell'[accesso amministrativo](09-accesso-amministrativo.md): le interfacce di gestione ascoltano solo nella VLAN 99.

## La configurazione, componente per componente

### Wazuh sul server Proxmox

Si installa con l'assistente della guida rapida, che mette server, indicizzatore e dashboard sulla stessa macchina (S87), su una macchina virtuale Linux supportata con 4 vCPU, 8 GB di memoria e 50 GB di disco. Al termine si cambiano le password generate e si conserva quella dell'amministratore nel gestore di password, non nel progetto. Si imposta una password di registrazione per gli agenti, così che nessun dispositivo possa iscriversi da solo.

Per ricevere il syslog di switch, AP e NAS si aggiunge al file `ossec.conf` del server un blocco `remote` con la connessione syslog, la porta 514, il protocollo e, obbligatoriamente, gli indirizzi ammessi: la documentazione avverte che senza `allowed-ips` la configurazione non ha effetto (S95). Gli indirizzi ammessi sono la VLAN 99 e l'indirizzo del NAS, non l'intera rete.

```xml
<remote>
  <connection>syslog</connection>
  <port>514</port>
  <protocol>udp</protocol>
  <allowed-ips>192.168.99.0/24</allowed-ips>
  <allowed-ips>192.168.30.10</allowed-ips>
  <local_ip>192.168.30.30</local_ip>
</remote>
```

### OPNsense e Suricata

Suricata si attiva prima in sola rilevazione, senza bloccare, come prevedeva già lo studio del 22/09/2026: un falso positivo in modalità di blocco interrompe la rete della casa. Si sceglie un insieme di regole gratuito, si applica alle interfacce interne su cui si vuole vedere il traffico fra le zone e verso Internet, e si misura il carico sull'i3 del firewall prima e dopo, come richiede la pendenza sulle prestazioni. Il passaggio al blocco si valuta solo dopo settimane di allarmi letti e regole regolate.

Il plugin si installa da System, Firmware, Plugins cercando `os-wazuh-agent`, e si configura da Services, Wazuh Agent, Settings: nome o indirizzo del server Wazuh, servizio attivo, password di registrazione, le applicazioni syslog da inviare e l'opzione degli eventi di intrusion detection (S93). Le applicazioni da inviare all'inizio sono il registro del filtro, il server web dell'interfaccia di gestione, il servizio SSH e il servizio della VPN: sono quelle che rispondono alla terza domanda.

### Agenti sugli host

Sui PC Windows e Linux della VLAN 10 si installa l'agente indicando l'indirizzo del server e la password di registrazione. Il NAS TrueNAS non è pensato per installare software estraneo, quindi manda solo il proprio syslog. Le macchine del laboratorio possono avere l'agente se l'esperimento lo prevede, ed è il modo di esercitarsi a vedere un attacco dalla parte del difensore, come nel laboratorio di Autore-LinkedIn-B.

### Le regole del firewall

| Interfaccia | Regola, sopra il blocco di RETI_INTERNE | Porte |
|---|---|---|
| VLAN 10 | consenti VLAN 10 verso WAZUH | TCP 1514, 1515 |
| VLAN 60 | consenti VLAN 60 verso WAZUH, facoltativa | TCP 1514, 1515 |
| VLAN 99 | consenti VLAN 99 verso WAZUH | UDP 514 |
| WireGuard e VLAN 10, solo ADMIN | già coperte dall'alias GESTIONE, che si estende alla dashboard nella VLAN 99 | TCP 443 |

Il traffico che parte dal firewall stesso, cioè il plugin, non passa dalle regole delle interfacce interne. Le regole complete stanno in [Regole fra le zone](08-regole-fra-le-zone.md).

## La risposta attiva

L'azione `opnsense-fw` permette a Wazuh di far bloccare un indirizzo dal firewall quando una regola scatta. La si tiene spenta all'inizio, per la stessa ragione del blocco di Suricata: un falso positivo blocca un dispositivo di casa senza che nessuno sappia perché. Si accende più avanti, per regole precise, per esempio molti tentativi falliti di accesso alla VPN, e con una durata limitata del blocco. La configurazione sta sul server Wazuh, che definisce l'azione e la lega alle regole e all'identificativo dell'agente del firewall (S93).

## Conservazione e riservatezza

Gli allarmi si conservano 90 giorni, il valore su cui la documentazione dimensiona i 50 GB (S87). I log contengono nomi di dispositivi, indirizzi interni e orari di attività della casa: restano sulla macchina virtuale e nelle sue copie sul NAS, non si esportano verso servizi esterni e non si citano nel repository pubblico.

## Il ripiego se il plugin si rompe

Se un aggiornamento di OPNsense rendesse inutilizzabile `os-wazuh-agent`, il firewall può mandare i propri log al raccoglitore syslog di Wazuh con la funzione di log remoto di OPNsense, aggiungendo il suo indirizzo fra gli `allowed-ips`. Si perde l'invio diretto degli eventi di Suricata e la risposta attiva, non la visibilità sul filtro e sugli accessi.

## In che ordine si mette in opera

Prima la rete: VLAN e regole collaudate. Poi Proxmox e la macchina virtuale di Wazuh, con le due schede nella VLAN 30 e nella VLAN 99, e l'accesso alla dashboard dalla workstation ADMIN. Poi un agente su un solo PC, per verificare il percorso. Poi il plugin su OPNsense, senza Suricata. Poi Suricata in sola rilevazione, misurando il carico del firewall. Poi syslog di switch, AP e NAS. Solo alla fine, e solo se gli allarmi sono stati letti per settimane, il blocco di Suricata e la risposta attiva.

## Collaudo

Dal PC con l'agente, un accesso fallito ripetuto genera un allarme sulla dashboard. Una regola di blocco del firewall che scatta compare come evento dell'agente del firewall. Una connessione di prova verso un indirizzo di test che l'insieme di regole riconosce genera un allarme di Suricata. Un accesso alla dashboard da un PC che non è ADMIN non risponde. Da una macchina del laboratorio senza la regola facoltativa l'agente non riesce a collegarsi, e il registro del firewall mostra il blocco.
