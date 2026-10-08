# Stato e supporto

### Informazioni generali

#### Internet

Parametro - Valore

Indirizzo IP - 203.0.113.10

Gateway - 203.0.113.1

Indirizzo IP DNS primario - 62.101.93.101

Indirizzo IP DNS secondario - 62.101.93.200

Firewall - ON

Indirizzi IPv6 / Lunghezza prefisso IPv6 - N/A (Link-local fe80::/64)

Indirizzo globale IPv6 - N/A

Gateway IPv6 - N/A

Indirizzo IP DNS primario IPv6 - N/A

Indirizzo IP DNS secondario IPv6 - N/A

Lunghezza Prefisso WAN IPv6 - N/A

EUI-64 Lunghezza del prefisso - N/A

IGD Parental - ON

IGD Device Finder - ON

IGD LAN IPv6 Prefisso - N/A

Nel progetto il firewall del Seven resta attivo. IPv6 risulta assente, con il solo indirizzo locale di collegamento: la WAN di OPNsense non chiede IPv6 e la casa resta solo IPv4 finché l'operatore non delega un prefisso. Le funzioni IGD sono quelle di UPnP, trattate nella pagina [Internet](03-internet.md).

#### Rete LAN

Indirizzo IP - 192.168.1.254/24

Gateway predefinito - 192.168.1.254

Indirizzo MAC - 68:B4:XX:XX:XX:EC

Server DHCP - On

Server DHCPv6 - On

Router Advertisement - On

Gateway predefinito IPv6 - (vuoto)

Porta LAN 1 - Inactive - 0 Mbit/s

Porta LAN 2 - Inactive - 0 Mbit/s

Porta LAN 3 - Active - 1 Gbps

Porta LAN 4 - Active - 2.5 Gbps

Nel progetto la porta LAN 4 è l'unica a 2,5 GbE e va alla WAN di OPNsense; la PS5 va su una delle porte da 1 GbE. Il router advertisement e il DHCPv6 accesi, in assenza di un prefisso globale, distribuiscono al più configurazioni locali e non disturbano OPNsense se la sua WAN è configurata senza IPv6.

#### Wi-Fi 2.4GHz

Stato - On

SSID - FASTWEB-XXXXXX (…)

Indirizzo MAC - B8:4F:XX:XX:XX:8A

Sicurezza - WPA2+WPA3

Canale - 10

Larghezza di banda - 20 MHz

#### Wi-Fi 5Ghz

Stato - On

SSID - FASTWEB-XXXXXX (…)

Indirizzo MAC - B8:4F:XX:XX:XX:8E

Sicurezza - WPA2+WPA3

Canale - 36

Larghezza di banda - 80 MHz

Sono i valori di riferimento per coordinare i canali con quelli degli AP, se la radio del Seven resta accesa.

#### Sistema

Numero di serie - <sn-modem>

Versione del firmware - 23.2.0638_FW_023_FGM234B

Tipo e versione hardware - <hw-type-modem>

Tempo di attività dall’ultimo reboot - 0 days, 0 hours and 25 minutes

Versione driver wireless 2.4 GHz - 8.2.1.4

Nel progetto il firmware si annota a ogni rilevazione: un aggiornamento remoto dell'operatore può cambiare il comportamento delle voci del menu.

### Stato della fonia (not-of-interest-here)

### Stato WAN

#### Dettagli connessione WAN

Interfaccia - Tipo - NAI - Stato - Uptime di connessione

GPON - cu.ax - Enabled - Down - 0 s

LTE/MBB1 - dhcp - Unabled - Up - 10 d 9 h

UMTS - mobile - Unabled - Down - 0 s

Interfaccia - Tipo - Indirizzo IP - Maschera IPv4 - Server DNS

GPON - cu.ax - 0.0.0.0 - 0.0.0.0 - (vuoto)

LTE/MBB1 - dhcp - 203.0.113.10 - 255.255.255.0 - 62.101.93.101, 62.101.93.200

UMTS - mobile - 0.0.0.0 - 0.0.0.0 - (vuoto)

La tabella mostra la GPON giù e la connessione LTE su da dieci giorni, con l'indirizzo pubblico: la rilevazione è avvenuta sul collegamento di riserva, come spiega la premessa del [README](README.md). La schermata va rifatta con la fibra attiva.

#### Dettagli connessione Ipv6 WAN (not-of-interest-here)

#### Statistiche IPv4 WAN (not-of-interest-here)

#### Statistiche IPv6 WAN (not-of-interest-here)

### Stato LAN (missing)

Da fotografare.

### Stato GPON

Stato: Up/Down

Velocità in bit massima: 1240Mbps/2490Mbps

Modalità duplex: N/A

Sono le velocità di linea della GPON, condivise sul ramo ottico: il tetto teorico è circa 2,5 Gbps in ricezione e 1,25 Gbps in trasmissione, e la velocità reale va misurata.

### Diagnostica (not-of-interest-here)

Nel progetto serve solo in caso di guasto.

### Riavvio (not-of-interest-here)

### Info
