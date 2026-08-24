# Schede di rete (NIC)

Una NIC è semplicemente la Network Interface Card, cioè la scheda che permette a un dispositivo di parlare in rete tramite Ethernet o Wi-Fi. In questo contesto è quasi sempre una scheda Ethernet, integrata nella motherboard o installata su PCIe.

Le varianti principali riguardano velocità, protocollo, driver e uso previsto. Per il domestico oggi esistono NIC a 1GbE, a 2.5GbE come quella Realtek RTL8125, e modelli più professionali a 5GbE o 10GbE basati su chip Intel o Marvell, più stabili sotto carico e con latenze minori.

L’ambito aziendale aggiunge funzionalità come accelerazioni hardware per virtualizzazione, checksum offload più avanzati, supporto SR-IOV, gestione remota e maggiore qualità elettrica delle interfacce. A livello fisico la differenza sta sempre nel link: 1G, 2.5G, 5G e 10G sono standard Ethernet progressivi con requisiti elettrici e di dissipazione diversi.

Per un ambiente domestico spinto, una 2.5GbE è il punto di equilibrio: sfrutta la fibra Fastweb 2.5G, funziona con cablaggi Cat5e, non scalda, costa poco ed è compatibile con qualunque switch 2.5G. La NIC è quindi il collo di bottiglia *locale*: se la porta è 1G, non si supera 1G; se è 2.5G e l’infrastruttura lo supporta, si negozia 2.5G automaticamente.
