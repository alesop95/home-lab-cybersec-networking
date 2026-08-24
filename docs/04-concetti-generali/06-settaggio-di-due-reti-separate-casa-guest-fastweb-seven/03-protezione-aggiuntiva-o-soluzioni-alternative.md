# Protezione aggiuntiva (o soluzioni alternative)

## Questione supporto 802.1Q

Se si vogliono usare più VLAN nella rete (es. LAN principale, IoT, NAS, Guest), il collegamento tra Fastweb Seven e switch managed deve poter trasportare tutte quelle VLAN contemporaneamente. Se il Fastweb Seven non supporta 802.1Q, allora non può capire né gestire VLAN multiple, e quindi non può fornire gateway/DHCP separati per ciascuna VLAN. In quel caso serve un router proprio che faccia da “cervello” delle VLAN. Se il modem/router non lo supporta, non può gestire una rete multi-VLAN come quella che stai progettando.

Quindi se anche faccio tutte le configurazioni a livello fisico e quant'altro se poi però quando passano in quell'unica porta LAN per ritornare al router Fastweb seven per il traffico dati se lui dentro non sa etichettare è inutile che faccio tutti quei collegamenti anche se le segmento nel mio switch fisico.  Se il Fastweb Seven non supporta 802.1Q, allora tutte le VLAN che fai sullo switch arrivano al modem come traffico “non etichettato”, quindi:

- Il modem non distingue le VLAN, le tratta tutte come una singola rete.
- DHCP/Internet saranno forniti solo alla VLAN di default (quella “untagged”).
- Le altre VLAN (IoT, NAS, Guest) non avranno accesso a Internet o al gateway, anche se fisicamente collegate.
- La segmentazione VLAN sullo switch resta solo interna, utile per isolare traffico tra porte, ma non comunica correttamente con il router.

In pratica: senza 802.1Q sul router, la rete multi-VLAN funziona solo internamente allo switch, ma non ha routing verso Internet né DHCP separati per ciascuna VLAN. Significa semplicemente che nell'unica porta LAN a 2,5Gbps dello switch il traffico si rimischia, ma comunque dentro nelle sotto LAN corrispondenti alle porte fisiche del mio switch il traffico comunque è segmentato: **tra le porte dello switch**: le VLAN continuano a funzionare, cioè il traffico tra dispositivi della stessa VLAN resta isolato dalle altre VLAN, ma sulla porta uplink verso il Fastweb Seven: tutto il traffico “taggato” dalle VLAN arriva come traffico non etichettato, quindi il router non distingue le VLAN.

Questo significa che i dispositivi nelle VLAN che non corrispondono alla VLAN di default del router (l’unica) non avranno accesso a Internet né riceveranno DHCP dal modem. Il traffico “rimischiato” avviene solo in uscita verso il router, ma internamente allo switch la segmentazione VLAN rimane attiva e funziona perfettamente per isolare reti locali.

Quindi la VLAN serve ancora per isolamento interno, QoS, sicurezza tra porte, ma per farle comunicare con Internet bisogna avere un router che supporti trunk 802.1Q, oppure mettere il modem in bridge e gestire tutto il routing/VLAN con un router a valle o con altre soluzioni come un firewall in più (opzionale) | cloud o fisico (open-source). Se usi un firewall dedicato con switch gestibile non serve più che il modem gestisca VLAN/tagging ma si creano VLAN separate su quello e sullo switch interno e il firewall diventa il punto centrale di segmentazione, isolamento e gestione traffico. La rete guest e la rete principale passano entrambe dal firewall, che decide regole, isolamento etc… In altre parole, il modem diventa “solo internet” (messo in bridge), e tutta la logica di rete domestica (VLAN, segmentazione main/guest, firewall avanzato) la si gestisce sul dispositivo dedicato.

## Firewall in più (opzionale) | cloud o fisico (open-source)

Se vuoi aggiungere un firewall “in più” con più controllo, ci sono fondamentalmente due strade principali:

1. Soluzione cloud
- Alcuni firewall moderni, come Cloudflare WARP for Teams, Cisco Umbrella o NextDNS, permettono di filtrare il traffico DNS e applicare regole di sicurezza anche su dispositivi in casa.
1. Soluzione hardware/software locale leggero
- Si può usare una macchina dedicata, anche molto leggera, solo per fare da firewall tra modem e rete interna.

La prima soluzione non richiede hardware aggiuntivo ed è facile da gestire; tuttavia, non filtra *tutto* il traffico a livello IP/porta, principalmente DNS e applicazioni web.

Nella seconda soluzione ci sono alcune soluzioni open source molto valide:

- OPNsense o pfSense: firewall professionali open source che si possono installare su un mini-PC o un Raspberry Pi avanzato.
- Basta collocare la macchina tra modem e switch/router interno e c’è gestione di NAT, firewall, VLAN, QoS e segmentazione avanzata. Consente anche VPN, IDS/IPS, controllo avanzato del traffico.
- IPFire: più leggero, adatto a dispositivi con risorse limitate, sempre con possibilità di segmentazione e regole avanzate.

Lo schema tipico è [Modem Fastweb] → [Firewall dedicato] → [Switch LAN] → [Dispositivi main + guest].

Il modem rimane in bridge o NAT base. Tutto il traffico passa dal firewall, che applica regole molto più granulari. E si possono creare VLAN separate per main e guest, e gestirle completamente a livello firewall.

Va considerato che in questo settaggio ricade anche il fatto che il concetto di “a monte” si sposta dal modem al firewall: il firewall decide se un dispositivo è main o guest, assegna IP, applica regole e VLAN, e tutto il traffico passa da lì. La frase “la separazione tra rete principale e guest avviene a monte sul modem/router” si riferiva al comportamento del modem quando gestisce da solo le due reti, senza firewall aggiuntivo dove il modem assegna due sottoreti separate (ad esempio 192.168.1.x per la principale e 192.168.2.x per la guest) e imposta regole *interne di firewall* tra le due.
