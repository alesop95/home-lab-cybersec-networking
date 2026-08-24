# Switch 2,5Gbps managed

## Introduzione

Uno switch 2,5 Gbps a 8 porte unmanaged è un dispositivo plug-and-play che opera a livello 2 con configurazione fissa: negozia automaticamente velocità e duplex, apprende le MAC address table e inoltra i frame senza possibilità di intervento. Non espone interfacce di gestione, quindi non puoi creare VLAN, priorità QoS, mirroring, limitazioni di banda o controlli sul traffico; l’obiettivo è solo fornire connettività multi-gigabit stabile tra i dispositivi domestici.

Uno switch managed a 2,5 Gbps introduce un piano di controllo accessibile via web/CLI/SNMP. Permette segmentazione tramite VLAN 802.1Q, gestione delle priorità con QoS (802.1p/DSCP), link aggregation (LACP) se supportato, port mirroring per diagnostica, storm control, eventuale IGMP snooping per multicast e talvolta ACL di base.

Questo consente isolamento logico tra reti (es. IoT vs LAN principale), ottimizzazione del traffico sensibile alla latenza e visibilità statistica su errori e saturazione delle porte.

In ambito domestico, la differenza pratica è che l’unmanaged offre solo switching trasparente a 2,5 Gbps, mentre il managed consente controllo topologico e qualitativo del traffico, utile se hai più sottoreti, NAS ad alta banda, Wi-Fi 6/6E/7 con backhaul multi-gigabit o necessità di troubleshooting preciso.

Se con il Fastweb Seven si ha 1 porta LAN a 2,5 Gbps, allo switch si possono collegare sicuramente un NAS di rete e anche 3-4 macchine (PC Windows, Linux ecc…). Rimanendo quindi nel campo degli switch 2,5 Gbps gestiti, questi offrono funzionalità avanzate per configurare, monitorare e ottimizzare la rete:

- VLAN (Virtual LAN): segmentazione della rete per sicurezza e gestione del traffico
- QoS (Quality of Service): prioritizzazione del traffico per applicazioni critiche
- Link Aggregation/LACP: combinazione di porte per maggiore larghezza di banda
- Port Mirroring: monitoraggio del traffico di rete per diagnosi
- IGMP Snooping: gestione ottimizzata del traffico multicast
- Storm Control: prevenzione di congestioni di rete
- Spanning Tree Protocol: prevenzione di loop nella rete
- Sicurezza delle porte: controllo dell’accesso e limitazione MAC
- SNMP: monitoraggio remoto dello switch
- Interfaccia Web: gestione tramite browser

Il cavo tra modem e switch può negoziare fino a 2,5 Gbps se entrambi lo supportano e i singoli dispositivi collegati a una porta RJ-45 dello switch possono comunicare fino a 2,5 Gbps se la scheda di rete lo supporta. Se ci sono due porte SFP+ da 10 Gbps servono solo per uplink verso un NAS o un altro switch/server con moduli compatibili. Ciò significa che se si ha un modem che consegna 2,5 Gbps, uno switch XMG1915 sfrutterà quella velocità su ogni porta RJ-45 2,5 Gbps (non è limitato a 1 Gbps come nella serie GS1915).

## ZYXEL XMG1915-10E

### Ratio

Un esempio di switch managed è lo XMG1915-10E dalla ZYXEL [https://www.zyxel.com/it/it/products/switch/8-16-port-2-5gbe-smart-managed-switch-with-2-sfp-uplink-xmg1915-series/overview](https://www.zyxel.com/it/it/products/switch/8-16-port-2-5gbe-smart-managed-switch-with-2-sfp-uplink-xmg1915-series/overview) le cui specifiche sono [https://www.zyxel.com/uk/en-gb/products/switch/8-16-port-2-5gbe-smart-managed-switch-with-2-sfp-uplink-xmg1915-series/specifications](https://www.zyxel.com/uk/en-gb/products/switch/8-16-port-2-5gbe-smart-managed-switch-with-2-sfp-uplink-xmg1915-series/specifications).

La serie XMG1915 di Zyxel è una linea di switch Multi-Gigabit Smart Managed con porte fino a 2,5 Gbps su RJ-45 + 2 porte SFP+ da 10 Gbps per uplink. In particolare, il modello XMG1915-10E - 8 porte 2,5 Gbps + 2 SFP+; NON ha PoE. PoE (Power over Ethernet) serve solo se devi alimentare dispositivi tramite lo stesso cavo di rete (es. access point Wi-Fi, telecamere IP, telefoni VoIP). Se non hai dispositivi che richiedono alimentazione PoE, uno switch senza PoE è tecnicamente identico per i dati a uno con PoE, la differenza è solo l’alimentazione via cavo. PoE servirebbe solo se uno prevede di alimentare AP Wi-Fi o telecamere senza alimentatori separati. Il Seven Booster Fastweb Casa Pro NON è PoE. L’alimentazione avviene tramite alimentatore separato collegato alla presa elettrica (classe standard per dispositivi Fastweb), questo significa che non serve uno switch PoE solo per alimentarlo. PoE servirebbe solo se volessi alimentare dispositivi come AP Wi-Fi aggiuntivi o telecamere IP via Ethernet senza usare prese elettriche aggiuntive.

La Zyxel XMG1915 è un 8 porte 2,5 GbE con 2 uplink SFP e gestione layer 2 avanzata. Non PoE, cosa non necessaria poiché l’unico dispositivo che bisogna collegare è al piano di sotto un Access Point che sostituirà Il Fastweb Secure Extender e si metterà un adattatore. Supporta VLAN, LACP, QoS e funzioni di monitoring come SNMP. È comparabile al MikroTik CRS310 su funzioni layer 2 e uplink, e anche sul prezzo, ma non ha routing layer 3 ma con un prezzo generalmente più basso del MikroTik. Zyxel XMG1915 offre un compromesso tra funzionalità gestionali avanzate e costo, senza la complessità del MikroTik.

Inoltre, la differenza tra Zyxel XMG1915-10E e invece Ubiquiti USW-Flex-2.5G-5 nel contesto di gestione non è equivalente perché Zyxel XMG1915-10E è uno switch managed layer 2 completamente *autonomo*: le VLAN create sullo switch si comportano come reti logiche separate ma il traffic tra VLAN viene sempre routato nel firewall esterno (giusto per ricordare il contesto di rete). Le porte SFP+ da 10 Gbps come uplink consentono collegamenti ad altri apparati ad alta velocità se in futuro ne servisse l’integrazione. L’Ubiquiti USW-Flex-2.5G-5 invece è, di fatto, uno switch la cui gestione dipende dal UniFi Controller. Tecnicamente l’hardware supporta VLAN e funzionalità smart, ma senza UniFi Controller non ha una vera interfaccia di configurazione locale. In assenza del controller il comportamento base è simile a un unmanaged, con funzionalità gestite minime o non accessibili. La gestione VLAN, il monitoraggio e le configurazioni avanzate richiedono il controller UniFi (software installato su un computer/NAS o UniFi OS su Dream Router/Cloud Key). Questo introduce una dipendenza infrastrutturale non necessaria e che in questo caso specifico è un limite perché significa non avere un’interfaccia di gestione standalone sullo switch e dover mantenere un controller attivo per impostare o modificare VLAN, QoS, port isolation, ecc. Questa dipendenza da controller centralizzato è il motivo principale per cui la Zyxel viene considerata più adatta nel tuo contesto: è managed nativamente e non richiede altri apparati/software per sfruttare le funzionalità di gestione. Zyxel XMG1915, al contrario, è managed nativamente: ha un’interfaccia web locale direttamente sullo switch e tutte le funzioni di gestione layer 2 sono accessibili senza bisogno di software esterno. Per il contesto descritto, una LAN 2,5 Gbps a valle di un firewall, senza infrastruttura UniFi preesistente, la Zyxel permette di configurare VLAN, QoS, uplink SFP e monitoraggio senza introdurre dipendenze da controller esterni.

Con la Zyxel XMG1915-10E è possibile creare VLAN 802.1Q isolate tra porte fisiche o gruppi di porte, applicare QoS avanzato per prioritizzare traffico voce, video o dati, configurare link aggregation (LACP) per combinare due porte e aumentare throughput o ridondanza, abilitare port mirroring per monitoraggio del traffico, impostare storm control per limitare broadcast o multicast e utilizzare SNMP (Simple Network Management Protocol) per raccolta dati e integrazione in sistemi di monitoring. Le porte SFP+ consentono uplink ottici o rame fino a 10 Gbps, utili per collegamenti verso server o altri switch ad alta velocità. Tutte queste funzionalità sono disponibili tramite interfaccia web locale, senza necessità di software esterno o controller. Nel contesto di una singola LAN 2,5 Gbps a valle del firewall domestico, con gestione locale e indipendente come requisito, la Zyxel XMG1915-10E è l’unica scelta che soddisfa pienamente le condizioni: managed, non PoE, multi-gigabit, con uplink SFP, funzionalità layer 2 avanzate accessibili nativamente, senza introdurre complessità o dipendenze esterne.

### Alternative valutate

#### MikroTik CRS310-8G+2S+IN (aborted)

Il MikroTik CRS310-8G+2S+IN è uno switch layer 3 gestito con 8 porte Gigabit e 2 porte SFP+ da 10 Gbps. È completamente gestibile via RouterOS, consente VLAN, routing tra VLAN, LACP, monitoraggio SNMP, QoS avanzato, firewall e altre funzioni enterprise. Non ha PoE, soddisfa il requisito. Il prezzo è più alto, ma offre capacità di uplink 10 Gbps e gestione avanzata. L’interfaccia web è più complessa rispetto a un TP-Link, e la curva di apprendimento è maggiore. È quindi una soluzione molto più completa e futura-proof rispetto al TP-Link, ma non economica.

##### Supporto al layer 3 in questo contesto

Il supporto al routing layer 3 significa che lo switch può instradare traffico tra reti o VLAN differenti senza passare da un router esterno. In termini pratici, le VLAN sono reti logiche separate; uno switch layer 2 può solo separare e trasmettere traffico all’interno della stessa VLAN, mentre per comunicare tra VLAN serve un router o uno switch layer 3.

Avere layer 3 integrato consente di centralizzare la gestione del traffico inter-VLAN, ridurre la latenza perché il routing avviene internamente allo switch, e applicare regole di firewalling o QoS direttamente tra reti interne senza uscire verso un apparato separato.

Se a valle del firewall c’è una sola LAN 2,5 Gbps e non si prevede di segmentare reti con comunicazione tra loro *senza* passare dal firewall, il routing layer 3 nello switch non è necessario. Uno switch layer 2 basta: permette di creare VLAN interne alla LAN, separando traffico tra dispositivi o servizi, ma tutte le comunicazioni tra VLAN dovranno comunque transitare dal firewall/router esterno che farà il routing tra di esse. In pratica, con un singolo segmento LAN a 2,5 Gbps, non ci sono reti multiple, tra cui il traffico debba essere instradato internamente allo switch. Le VLAN su layer 2 servono solo per organizzare, isolare o applicare QoS dentro la stessa LAN, ma non cambiano la necessità di un router per uscire verso Internet o altre reti esterne.

Questo significa che in questo scenario l’assenza di layer 3 sullo switch non è un limite rilevante e uno switch layer 2 gestito copre pienamente le necessità operative.

#### Ubiquiti USW-Flex-2.5G-5 (aborted)

L’Ubiquiti USW-Flex-2.5G-5 è uno switch compatto da 5 porte 2,5 Gbps gestito tramite UniFi Controller. Non ha PoE sulle porte principali, ha management centralizzato e VLAN, ma non supporta routing layer 3 tra VLAN. Uplink SFP assente. È più costoso del TP-Link, più semplice del MikroTik in termini di funzionalità, e richiede l’infrastruttura UniFi per sfruttare al meglio le capacità di gestione.

L’Ubiquiti USW-Flex-2.5G-5, pur essendo anch’esso privo di PoE e con porte 2,5 Gbps, non è unmanaged puro come il TP-Link. Richiede una base di management UniFi per essere pienamente gestito (controller software UniFi o UniFi OS). Senza controller, il comportamento base può risultare equiparabile a un unmanaged, ma l’ interfaccia di gestione locale standalone potrebbe non offrire la stessa granularità di funzioni layer 2 di uno switch gestito reale come Zyxel. In pratica l’Ubiquiti è pensato per entrare in un ecosistema di management centralizzato UniFi.

.

### [TBC] Configurazione nella rete
