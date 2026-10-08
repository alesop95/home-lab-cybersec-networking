# [TBC] Topologia della rete teorica

## Introduzione (da sopra)

Quello che serve è che la VLAN, se richiesta, è obbligatoria indipendentemente dal fatto che sia DHCP o PPPoE; se nella configurazione del firewall. Se sbagli o non metti il VLAN ID, non ottieni né lease DHCP né sessione PPPoE anche se username e password sono corretti. l’informazione minima necessaria dall’assistenza è duplice e concatenata: quale protocollo di accesso viene utilizzato sulla linea FTTH attiva e se tale protocollo transita su una VLAN specifica, con relativo VLAN ID. Solo con questi parametri di livello 2 e 3 è possibile configurare in modo corretto e ripetibile l’interfaccia WAN su OPNsense dietro ONT. È necessario disporre dei parametri di livello 2 e livello 3 effettivamente utilizzati sulla linea FTTH (i parametri di accesso WAN su ONT).

Mi sono chiesto se effettivamente dall'ONT della FTTH se metto ethernet a 2,5Gbps cat6 poi il provider entrando lì prima del modem con la WAN non smetta di funzionare perchè vede un MAC address diverso da quello della configurazione iniziale. Fastweb mi ha detto non posso farlo, ho immaginato fosse per questo.

Se devo mettere firewall dopo modem mi rimane scoperta da firewall la wi-fi che infrastrutturalmente non è facile da portare al piano sotto con AP su switch PoE (che sto per comprare).Perchè teoricamente la rete wireless, in questo modo, non viene processata dal firewall.

Questo da quello che ho capito uno non lo risolve neanche con modem proprietario (che al momento non mi serve comprare) perché un mio fornitore mi ha detto che ha fatto finta di chiamare l’assistenza tecnica del provider dicendo che non gli funzionava il modem e mettendocene un altro aveva fatto la prova (come volevo fare io) del tipo:

---ONT---WAN in 2,5Gbps firewall---LAN out 2,5gbps firewall --- LAN in 2,5Gbps modem Fastweb

Senza usare la porta WAN del modem perché così il modem praticamente fa solo bridge e la wi-fi anche passa da OPNsense. NON gli funzionava e ha scoperto che il vero motivo è che l’ONT si aspetta (tra i vari parametri) quello che ho detto.

Quindi l’unica configurazione possibile è ---ONT---WAN in 2,5Gbps modem Fastweb.

Dunque, io allora avevo pensato come workaround:

---ONT---WAN in 2,5Gbps modem Fastweb seven---LAN out 2,5gbps modem Fastweb ---WAN 2,5Gbps OPNsense

e da qui settare tutto il networking poi la LAN 2,5Gbps di OPNsense che parlerà con lo switch 8 porte che compro (pensavo ZYXEL XMG1915-10E) e a quel punto prendo una porta da 2,5Gbps e la porto di sotto e da lì access point con adattatore PoE per servire Wi-fi protetta in tutta casa ma al contempo riservarmi la rete cablata per i miei esperimenti.

Nel progetto il ragionamento si chiude proprio con il workaround dell'ultimo paragrafo, che è diventato la topologia adottata: ONT, WAN del Seven, LAN 4 del Seven a 2,5 GbE, WAN di OPNsense, LAN di OPNsense in trunk verso lo switch, e di lì gli access point. Due dettagli sono cambiati dopo. Lo switch è lo XMG1915-10EP con PoE integrato invece del 10E con adattatore, perché gli access point sono due (ADR-017), e i due cavi verso gli AP partono dallo switch al piano più alto e sono già posati (ADR-018). La rete cablata riservata agli esperimenti è diventata la VLAN 60 del piano di segmentazione.

Sul motivo per cui il firewall non può stare fra ONT e modem conviene tenere distinti i livelli di prova. Il divieto è dell'assistenza, per questa linea. La ragione del MAC address atteso dall'ONT è un'ipotesi, sostenuta dalla prova riferita da un fornitore e da uno scambio con Autore-LinkedIn-B su un altro operatore, ma non dimostrata: la documentazione pubblica dell'operatore descrive anche scenari con apparato proprio e non dichiara un vincolo generale. Il progetto per questo non costruisce sul collegamento diretto, ma non lo dichiara impossibile in assoluto. Il primo paragrafo, sui parametri di livello 2 e 3 della WAN, vale solo per quel collegamento diretto, ed è sviluppato nella cartella sui [parametri di accesso WAN](../07-tbc-new-i-parametri-di-accesso-wan-su-ont/README.md).
