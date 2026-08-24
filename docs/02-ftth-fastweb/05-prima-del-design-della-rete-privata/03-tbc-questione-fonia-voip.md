# [TBC] Questione fonia VoIP

L’unica variabile che può complicare lo schema è la fonia VoIP Fastweb. Se il Seven è necessario per la terminazione SIP e non hai le credenziali, lo lasci dietro al firewall e gli consenti uscita verso Internet come qualsiasi altro host. Dal punto di vista IP non cambia nulla: rimane un client nella tua LAN.

La fonia Fastweb è VoIP basata su SIP, cioè Session Initiation Protocol, con traffico voce RTP, Real-time Transport Protocol. Il punto critico è che le credenziali SIP e i parametri di registrazione non sono sempre forniti al cliente. Senza username, password, registrar e proxy ufficiali, non puoi configurare direttamente un tuo ATA o un tuo centralino su OPNsense.

In questa topologia il Seven, se deve gestire la fonia, diventa semplicemente un client SIP dentro la tua LAN. Collegato allo switch, riceve un IP da OPNsense e si registra verso i server Fastweb attraverso il firewall. Dal punto di vista tecnico funziona, perché il NAT di OPNsense traduce il traffico SIP/RTP come farebbe con qualsiasi altro flusso UDP.

L’unico rischio reale è legato alla gestione del SIP attraverso NAT. SIP è notoriamente sensibile a NAT simmetrici o a firewall troppo restrittivi. In OPNsense questo si controlla disabilitando eventuali SIP helper automatici e lasciando passare il traffico in uscita verso Internet senza manipolazioni applicative non necessarie. In un’architettura standard, con NAT outbound automatico e stato firewall regolare, la registrazione SIP del Seven funziona.

Quindi non c’è un problema strutturale. Il vincolo è solo l’accesso o meno alle credenziali VoIP. Se non le hai, devi tenere il Seven per la fonia. Se le hai, puoi eliminare completamente il Seven e terminare la voce su un tuo dispositivo SIP.
