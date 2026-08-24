# [TBC] Alternativa modem libero (PPPoE??? dal firewall)

Nel contesto che stiamo descrivendo, stiamo parlando di una linea FTTH (Fiber To The Home) gestita da Fastweb con un terminale ottico (ONT, Optical Network Terminal) ZYXEL PM5100-T1, che è un apparato GPON (Gigabit Passive Optical Network). Questo ONT riceve la fibra dalla borchia ottica e fornisce l’uscita Ethernet a 2,5 Gbps.

La topologia corretta sarebbe, per mantenere 2,5 Gbps end-to-end collegare l’ONT alla WAN di OPNsense e la porta LAN 2,5 Gbps di OPNsense collegata a uno switch 2,5 Gbps. Da quello switch escono tutte le diramazioni: verso il modem (sulla sua LAN 2,5 Gbps), verso i client multigig, verso eventuali server o NAS. In questo scenario il modem è solo un endpoint layer 2 collegato allo switch. Non è più il centro della LAN. Il centro diventa lo switch multigig. Questo non è possibile farlo con il modem di default fornito da Fastweb.

Se invece il modem libero stesse nello switch (managed) a 2,5Gbps è come se fosse in parallelo con tutto il resto a valle del firewall, perché se si collega la porta LAN 2,5 Gbps di OPNsense a uno switch managed 2,5 Gbps, quello switch diventa il punto di distribuzione layer 2 della LAN. Tutti i dispositivi collegati a quello switch, incluso il modem sulla sua porta LAN 2,5 Gbps, sono sullo stesso dominio Ethernet. Sono in parallelo dal punto di vista topologico, non in cascata dietro il Seven. Il firewall resta l’unico dispositivo layer 3 tra WAN e LAN. Lo switch fa solo commutazione di frame Ethernet in base agli indirizzi MAC. Il modem, con DHCP e NAT disattivati, è semplicemente un bridge Ethernet + access point Wi-Fi e non crea una sottorete propria, non introduce routing, non modifica i flussi IP. È un host layer 2 con più porte, come qualsiasi altro switch con radio integrata.

Il traffico tra due client collegati allo switch non passa da OPNsense. Il traffico tra un client LAN e Internet sì, perché il default gateway dei client è l’IP LAN di OPNsense. Questo è il comportamento corretto e desiderato. Se lo switch è managed si possono poi anche introdurre VLAN, separare reti, fare trunk verso OPNsense e segmentare Wi-Fi e LAN cablata in modo pulito. In quel caso il Seven può essere collegato con una porta access su una VLAN specifica oppure, se supporta tagging 802.1Q lato LAN, con un trunk. Dipende dalle sue capacità firmware

La questione centrale allora è capire, nel momento in cui si ha un modem libero, quale protocollo di accesso e quali requisiti di VLAN siano richiesti per collegare direttamente il tuo firewall alla porta WAN dell’ONT.

![](assets/img-0004.png)

![](assets/img-0005.png)

![](assets/img-0006.png)

![](assets/img-0007.png)

![](assets/img-0008.png)

