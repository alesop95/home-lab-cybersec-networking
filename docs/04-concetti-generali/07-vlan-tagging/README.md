# VLAN tagging

Stiamo parlando di VLAN tagging a più livelli, quindi concetto tecnico preciso: ogni dispositivo coinvolto (modem/router, switch, NAS) deve supportare VLAN tagging, altrimenti la segmentazione non funziona.

Una VLAN (Virtual LAN) è una rete logica separata all’interno della stessa infrastruttura fisica e il tagging significa che ogni pacchetto ethernet viene “marcato” con un ID VLAN (numerico, ad esempio 10, 20, 30) che identifica a quale rete logica appartiene. Lo scopo è permettere a più reti logiche di condividere lo stesso cablaggio fisico, senza interferire tra loro.

Nel modem/router (seven si devono quindi poter creare interfacce virtuali VLAN sullo stesso collegamento fisico, dunque la porta LAN 2,5 Gbit/s può trasportare pacchetti della VLAN 10 (IoT) e VLAN 20 (LAN principale) insieme, ma separati logicamente.

Lo switch deve capire il tag VLAN nei pacchetti (802.1Q standard) e se è unmanaged, non riconosce i tag perciò tutte le VLAN vengono “mischiate” perdendo la segmentazione. Se invece è managed, si possono configurare:

- Una porta *trunk*: porta più VLAN contemporaneamente (es. verso modem/router o NAS).
- Una porta access: appartiene a una sola VLAN (es. PC o dispositivo specifico).

Il NAS deve invece riconoscere il tag VLAN sul traffico in ingress e si possono configurare più interfacce virtuali (VLAN) per segmentare. Ad esempio si può usare VLAN 10 per backup/IoT, VLAN 20 per media/Server e VLAN 30 per la rete amministrativa.

Tutto funziona solo se modem, switch e NAS supportano tagging 802.1Q. Quindi VLAN tagging è il modo di “etichettare” i pacchetti Ethernet per far convivere più reti logiche sulla stessa infrastruttura fisica, permettendo segmentazione, sicurezza e gestione più pulita della rete.

Una nota importante è che:

- Il router tagga/untagga ogni porta in base a come le configuri.
- Il NAS tagga solo se tu gli dici di farlo (perché di solito sta su una singola VLAN, ma può stare su più VLAN se lo configuri).

Nessuna rete si “separa” automaticamente perché la porta è diversa, ma lo decide la configurazione VLAN del router.

## Contenuti

- [Perché un PC difficilmente deve farlo](01-perche-un-pc-difficilmente-deve-farlo.md)
- [VLAN tagging richiesto dal provider](02-vlan-tagging-richiesto-dal-provider.md)
