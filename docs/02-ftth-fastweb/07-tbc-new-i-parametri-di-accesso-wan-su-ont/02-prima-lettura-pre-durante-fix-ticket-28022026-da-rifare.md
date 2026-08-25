# Prima lettura pre/durante fix ticket 28022026 (da rifare)

Dalla pagina “Informazioni generali > Internet” emergeva un fatto tecnico preciso: l’indirizzo IP pubblico assegnato al gateway è 203.0.113.10 e la connessione WAN indicata attiva è “LTE/MBB1 - dhcp - Up”. Questo dato è anomalo rispetto a una linea FTTH pura, perché LTE/MBB1 indica l’interfaccia di backup mobile del modem Fastweb Seven.

Il modem Fastweb Seven è infatti un dispositivo ibrido con connettività mobile integrata che entra in funzione quando la connessione primaria GPON non è operativa.

Infatti, nella stessa schermata compare:

Interfaccia GPON - tipo cu.ax - stato Down - IP 0.0.0.0 Interfaccia LTE/MBB1 - tipo dhcp - stato Up - IP 203.0.113.10

Questo significa che, nel momento in cui è stata catturata la schermata, il traffico Internet non stava transitando sulla fibra GPON ma sulla connessione mobile di backup. Il valore “Up time di connessione 10 giorni” rafforza questo dato (ed effettivamente era così, quello era il momento in cui si era appena modificato il parametro da parte dell’operatore). Non è quindi possibile dedurre da questi parametri quale sia il protocollo di accesso della linea FTTH, perché in quel momento la FTTH non era la connessione attiva.

Questa osservazione è dunque importante perché spiega anche il comportamento descritto nel ticket Fastweb. Quando il supporto parla di “valore VLAN fuori posto” si riferisce quasi certamente alla configurazione del servizio GPON.

In ogni caso, prima di passare al passaggio successivo, cioè determinare se la linea Fastweb utilizzi DHCP o PPPoE e se sia presente una VLAN specifica, serve chiarire un punto tecnico osservato nei dati del modem. Finché la fibra non risulta attiva nella schermata WAN non è possibile leggere i parametri reali della connessione FTTH. Occorre quindi verificare lo stato WAN quando la voce GPON è Up e mostra un indirizzo IP reale. Solo in quel momento è possibile dedurre il protocollo di accesso utilizzato dalla linea.

## Approfondimento parametri WAN su ONT (OLT)

La rete FTTH GPON utilizza tipicamente VLAN per separare servizi a livello Ethernet tra ONT (il dispositivo che converte il segnale ottico della fibra in Ethernet) e OLT (Optical Line Terminal) ed è l’apparato dell’operatore nella centrale.

Nel modello di accesso FTTH usato dagli operatori italiani esistono tre elementi concatenati che devono combaciare:

1. livello fisico GPON tra OLT e ONT
1. livello Ethernet tra ONT e modem
1. livello IP tra modem e rete del provider

Il parametro VLAN appartiene al livello Ethernet. Se il traffico del cliente deve essere inserito nella VLAN 835 (numero puramente esemplificativo) e l’apparato invia pacchetti senza tag oppure con VLAN diversa, l’OLT scarta completamente il traffico. In quel caso non viene ottenuto né lease DHCP né sessione PPPoE, indipendentemente dal fatto che le credenziali siano corrette.

Questo coincide esattamente con l’osservazione fatta: la VLAN è logicamente precedente al protocollo di accesso. Prima deve esistere il corretto incapsulamento Ethernet VLAN-tagged, poi sopra quel circuito logico può transitare PPPoE oppure DHCP.

## Approfondimento MAC address binding

Il secondo punto riguarda il comportamento dell’ONT rispetto al MAC address. Di solito, gli ONT usati nelle reti FTTH possono implementare MAC binding verso il CPE (Customer Premises Equipment), cioè il modem/router dell’utente. In questo modello l’OLT apprende il MAC address visto sulla porta Ethernet dell’ONT e consente il traffico solo da quell’indirizzo. Questo non è uno standard obbligatorio ma una politica di rete adottata da alcuni operatori.

Non è possibile verificarlo deterministicamente direttamente dai dati forniti, perché il modem non espone la configurazione GPON completa. Tuttavia, il comportamento riportato da Fornitore-A che ha fatto la prova è coerente con questa architettura: collegando direttamente il firewall all’ONT il traffico non viene accettato perché il MAC address cambia rispetto a quello registrato del modem Fastweb. Questo spiega anche perché l’assistenza abbia detto che non è possibile collegare un altro dispositivo direttamente all’ONT. In quel modello di rete l’ONT non è realmente neutrale: è associato logicamente al modem dell’operatore.
