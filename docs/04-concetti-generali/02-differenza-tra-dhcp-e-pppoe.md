# Differenza tra DHCP e PPPoE

Per Fastweb in contesto FTTH residenziale o professionale, l’ONT espone generalmente l’accesso verso l’apparecchio client in modalità IPoE con DHCP. IPoE (IP over Ethernet) significa che l’ONT assegna dinamicamente un indirizzo IP pubblico all’apparato collegato (che con modem proprietario Fastweb, non può essere il firewall) tramite il protocollo DHCP (Dynamic Host Configuration Protocol), senza la necessità di instaurare una sessione PPPoE.

PPPoE (Point-to-Point Protocol over Ethernet) è invece un protocollo che incapsula i pacchetti IP all’interno di un “tunnel” PPP e richiede username e password per autenticarsi.
