# Piano unificato: hardware, server Proxmox e stack open source

Ritorno allo [studio](README.md). Documento di progetto dell'8/10/2026, chiesto dall'utente per riorganizzare il progetto attorno a tutte le informazioni raccolte, con la migliore soluzione open source per ogni funzione e con un server Proxmox su macchina fisica ricavato dall'hardware disponibile. Ogni scelta porta il suo stato: *deciso* se c'è una decisione registrata, *proposto* se aspetta l'utente, *pendente* se aspetta un dato, *scartato* se è esclusa con una ragione. Nulla di quanto descritto è installato.

## L'hardware e il suo ruolo

| Macchina | Che cosa è | Ruolo | Stato |
|---|---|---|---|
| NET-04, firewall | i3 di settima generazione, 8 GB, SSD 120 GB, tre schede di rete | OPNsense | deciso; installato il 16/01/2026, non configurato |
| `PC-DESKTOP-A` | base del consolidamento, 32 GB DDR4, due SSD SATA, due NVMe | NAS con TrueNAS SCALE (ADR-015, ADR-026) | deciso; montaggio fermo al Passo 1.6 |
| `linux-desktop-A` | ASRock H270M Pro4, i7-7700 a 4 core e 8 thread, 16 GB DDR4 in quattro moduli, rete Intel I219-V, nessun disco | server Proxmox, cioè l'host di servizio sempre acceso SRV-01 | proposto |
| `PC-DESKTOP-B` | ASUS B150-PRO, i7-6700, senza memoria né disco | scorta gemella del NAS, non si tocca | deciso dall'inventario delle scorte |
| `linux-desktop-B` | ASUS Z97-P, i7-4790, 16 GB DDR3, nessun disco | secondo nodo sacrificabile per prove distruttive, solo se serve | proposto, priorità bassa |
| due PC da fotografare | da identificare | da decidere dopo le foto | pendente |

La scelta di `linux-desktop-A` per Proxmox viene dall'[inventario delle scorte](../02-storage-di-rete-nas/06-inventario-delle-scorte-dopo-il-consolidamento.md), che la indica già come candidata naturale a un nodo ipervisore: è la più recente, conserva tutta la sua memoria e ha l'unica scheda di rete Intel del gruppo, la famiglia che gli ipervisori open source trattano meglio. Le manca soltanto un disco. Proxmox VE, oggi alla versione 9.2 su Debian 13, richiede le estensioni di virtualizzazione attive nel firmware e consiglia dischi ridondanti per l'uso continuo (S88); sul processore Intel le dichiara presenti, e l'impostazione del firmware va controllata alla prima accensione, come l'inventario raccomanda per la macchina gemella. Le foto dei due PC ancora da guardare possono cambiare il quadro, per esempio se uno dei due ha più memoria.

## Il server Proxmox

È l'host di servizio sempre acceso che il progetto aspettava senza averlo individuato: ospita i servizi che non possono stare sul NAS, che si accende a orario, né sul firewall, che non esegue servizi estranei alla sicurezza di rete.

La rete è un solo cavo dalla scheda Intel alla porta 6 dello switch, configurata come trunk con le VLAN 30, 60 e 99. Su Proxmox un unico bridge consapevole delle VLAN assegna ogni macchina virtuale alla sua zona. L'interfaccia di amministrazione di Proxmox sta nella sola VLAN 99, secondo ADR-025.

| Ospite | Tipo | Zona | Memoria | Disco | Stato |
|---|---|---|---|---|---|
| Wazuh, server, indicizzatore e dashboard insieme | macchina virtuale | VLAN 30 | 8 GB | 50 GB | proposto |
| AdGuard Home, DNS filtrante davanti a Unbound | contenitore | VLAN 30 | 0,5 GB | 2 GB | proposto |
| macchine del laboratorio | macchine virtuali | VLAN 60 | il resto, circa 4 GB | secondo l'esperimento | proposto |
| Proxmox stesso | sistema ospite | VLAN 99 | 2 GB | sistema | proposto |

Il conto della memoria è il vincolo vero. Wazuh, nella configurazione con i tre componenti sulla stessa macchina, chiede 4 vCPU, 8 GB di memoria e 50 GB di spazio per un massimo di 25 agenti e 90 giorni di allarmi (S87). Con 16 GB restano circa 4 GB per il laboratorio, che bastano per due o tre macchine leggere alla volta. Portare la macchina a 32 GB toglie il vincolo; che la scheda accetti 64 GB in quattro alloggiamenti va verificato sulla scheda del costruttore, e il costo dei moduli va cercato. È una decisione dell'utente, non un requisito di partenza.

Il disco da comprare è uno solo, un SSD SATA da 500 GB o 1 TB. Un secondo SSD in specchio è ciò che Proxmox consiglia, e si può aggiungere dopo. Le copie delle macchine virtuali vanno sul NAS, nella sua finestra di accensione.

## Lo stack open source, funzione per funzione

| Funzione | Scelta | Dove | Stato |
|---|---|---|---|
| firewall, routing, VPN | OPNsense, WireGuard | NET-04 | deciso |
| rilevamento sul traffico | Suricata integrato in OPNsense, prima in sola rilevazione | NET-04 | deciso (ADR-028) |
| SIEM, rilevamento sugli host, integrità dei file | Wazuh | Proxmox, VLAN 30, dashboard nella VLAN 99 | deciso (ADR-028) |
| raccolta dei log di firewall e apparati | plugin os-wazuh-agent per il firewall e gli allarmi di Suricata; syslog per switch, AP e NAS | NET-04, apparati | deciso (ADR-028), dettaglio in [Monitoraggio](11-monitoraggio-wazuh-suricata.md) |
| indicizzazione e ricerca | l'indicizzatore di Wazuh, incluso | Proxmox | proposto |
| DNS | Unbound su OPNsense, poi AdGuard Home | NET-04, poi Proxmox | deciso dallo studio del 22/09/2026 |
| storage e copie | TrueNAS SCALE | NAS | deciso |
| scansione delle vulnerabilità | Greenbone OpenVAS, acceso quando serve | Proxmox, VLAN 60 | proposto, fase 6 |
| gestione remota degli endpoint | MeshCentral, dagli studi del documento sorgente | Proxmox, VLAN 30 | proposto, fase 4 |
| metriche di switch, AP e host | lettura SNMP dall'host di servizio, con un raccoglitore da scegliere | Proxmox | pendente |
| analisi di campioni sospetti | zona isolata a parte, non la VLAN 60 | da progettare | pendente, fase 6 |

### Che cosa resta dello schema del documento sorgente

Lo schema di monitoraggio della prima stesura, con Wazuh, ELK, Snort, Sagan, MozDef e OSSIM, metteva insieme gli strumenti open source più citati. Verificati l'8/10/2026, la metà non è più una scelta possibile.

| Componente | Stato del progetto a monte | Esito nel piano |
|---|---|---|
| Wazuh | attivo | resta, al centro |
| ELK separato | attivo | scartato: Wazuh porta già il proprio indicizzatore e la propria dashboard, e uno stack separato duplicherebbe memoria e manutenzione su una macchina da 16 GB |
| Snort | attivo, ma gli sviluppatori di OPNsense non intendono integrarlo e indicano Suricata (S89) | sostituito da Suricata, già nel firewall |
| Sagan | ultima versione stabile del febbraio 2021 (S86) | scartato: la correlazione dei log la fa Wazuh |
| MozDef | deprecato e archiviato da Mozilla, ultimo aggiornamento nel 2021 (S84) | scartato |
| OSSIM | ritirato da LevelBlue a fine 2024 (S85) | scartato |
| Apache Metron, citato come estensione | ritirato nel dicembre 2020 e archiviato nel 2021 (S90) | scartato |
| Security Onion, alternativa integrata | attivo, ma chiede almeno 24 GB di memoria anche nella forma più piccola (S91) | scartato per questa macchina; da riconsiderare con un host dedicato |

Il flusso che ne risulta è più corto e tutto mantenuto. Gli endpoint mandano eventi a Wazuh con il suo agente; il firewall e gli apparati mandano i log a Wazuh via syslog; Suricata, nel firewall, rileva sul traffico e i suoi allarmi confluiscono nello stesso punto; Wazuh correla, conserva e mostra.

```
  [ endpoint: PC, NAS, VM ] --agente--> [ Wazuh su Proxmox, VLAN 30 ]
                                               ^          |
  [ OPNsense + Suricata ] --syslog e allarmi---+          v
  [ switch, AP ] ---------------syslog---------+     allarmi, ricerca,
                                                     dashboard
```

## In che ordine, e che cosa è pendente

La sequenza rispetta la roadmap. La rete viene prima, cioè firewall, switch e AP, perché senza segmentazione ogni servizio finirebbe in una rete piatta. Proxmox viene subito dopo il collaudo delle VLAN, perché porta DNS filtrante e monitoraggio. Il NAS procede in parallelo, perché si assembla senza toccare la rete.

Decisioni aspettate dall'utente: quale macchina diventa il server Proxmox, confrontando `linux-desktop-A` con i due PC da fotografare; se portarla a 32 GB con i moduli DDR4 di uno di quei due PC, che diventerebbe una scorta, come ha proposto l'utente l'8/10/2026. Dati aspettati: le foto dei due PC; la verifica delle estensioni di virtualizzazione nel firmware; il massimo di memoria della scheda e la compatibilità dei moduli; il prezzo di un SSD; il raccoglitore di metriche. Chiusi l'8/10/2026: Suricata al posto di Snort e l'integrazione con Wazuh, con il plugin di OPNsense (ADR-028). Da progettare più avanti: la zona isolata per l'analisi dei campioni.
