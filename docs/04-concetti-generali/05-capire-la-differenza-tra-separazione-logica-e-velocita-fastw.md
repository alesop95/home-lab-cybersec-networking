# Capire la differenza tra separazione logica e velocità (Fastweb Seven FTTH)

Nel momento in cui si utilizzano anche le altre 2 porte LAN a 1 Gbps nella versione fibra FTTH, ad esempio se alla 2.5G collego il NAS e alle altre 2 porte LAN a 1Gbps le tre reti che si creano come sono separate? In un’ipotesi tale di base senza switch, lo scenario sarebbe il Seven FTTH con 1 porta LAN 2,5 Gbit/s (collegamento NAS) e 2 porte LAN 1 Gbit/s (collegamento altri dispositivi (PC, smart TV, ecc.)). In questo caso tutte le porte fanno parte dello switch interno del Seven. Va considerato che senza VLAN (default, configurazione “out-of-the-box”):

   1. Tutte le porte appartengono alla stessa LAN fisica.
   1. Il NAS collegato a 2,5G può comunicare con i dispositivi sulle porte 1G *senza alcuna separazione logica*.
   1. La differenza di velocità è solo fisica (quindi NAS ↔ porta 2,5G è fino a 2,5 Gbit/s mentre NAS ↔ porte 1G è massimo 1 Gbit/s per singolo device). Senza VLAN, le porte 1G non sono “separate” dal NAS; sono solo più lente.

Con VLAN tagging (segmentazione logica) invece si possono creare VLAN separate per ogni “rete logica” (es. VLAN 10 per NAS/media, VLAN 20 per LAN PC, VLAN 30 per IoT).

In generale la separazione logica non dipende dalla velocità: ad esempio anche se ci si affida ad una soluzione senza switch 2.5G (alternativa più semplice) il NAS può entrare comunque anche lui da solo dentro la 2,5Gbps e le porte 1Gbps possono far parte di reti *logiche* diverse se è possibile configurare VLAN nel router poi la velocità massima reale per ogni device rimane quella fisica: 2,5Gbps porta 2,5 Gbps; porte 1Gbps → 1Gbps. Quindi faccio fare a quel router lo "switch" l'importante è che sia il NAS che il router taggano come VLAN.

Anche usando solo il Fastweb Seven, NAS su 2,5 Gbps e dispositivi su 1 Gbps possono essere messi in reti logiche diverse tramite VLAN, a condizione che router e NAS supportino 802.1Q e si configuri configuri il tagging correttamente per costruire una rete ordinata senza toccare la parte fisica.

La configurazione di rete base che vorrei installare è mettere il Seven collegato ad uno switch 2.5G tramite porta LAN 2.5G e poi collegare un NAS su una porta 2.5G dello switch (o direttamente sulla LAN 2.5G del Seven). Fare poi un po' di segmentazione: quindi usare switch che supporta VLAN (managed) o fare VLAN sul Seven (se supporta interfacce virtuali) assumendo che il NAS che compro supporta VLAN tagging.

La rete ruota attorno al Fastweb Seven come gateway principale. Dallo Seven esce un uplink verso uno switch managed 2.5 Gbps. Lo switch gestisce delle VLAN, quindi:

- VLAN 10: rete principale (192.168.10.0/24): PC, PS5, dispositivi cablati. DHCP attivo.
- VLAN 20: IoT / Smart (192.168.20.0/24): TV, dispositivi domotici. DHCP attivo.
- VLAN 30: storage/Server (192.168.30.0/24): NAS con IP statico (192.168.30.10).
- Guest Wi-Fi: rimane in VLAN separata (può essere VLAN 40 se lo switch lo supporta) con solo DHCP, niente accesso laterale alle altre reti. La rete Guest usa un pool DHCP isolato con accesso solo a Internet.

La topologia fisica (base) è:

- Fastweb Seven (modem/router) - collegato a Internet (WAN)
- Switch managed 2.5Gbps (es. 1x uplink 2.5G) - collegato alla LAN del modem
- PC-Workstation (LAN principale)
- NAS / Server multimediale (static IP)
- PC-Gaming / SmartTV / IoT (varie subnet)

Se il Fastweb Seven non supporta trunk 802.1Q: allora solo la LAN principale passa direttamente, e tutte le VLAN vengono gestite da un router proprio a valle.
