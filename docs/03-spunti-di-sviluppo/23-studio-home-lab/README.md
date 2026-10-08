# Studio integrato dell'home lab

Studio del 22/09/2026: architettura proposta, servizi senza canoni obbligatori, acquisto Zyxel e inventario. È progettazione documentale; non certifica installazioni, copertura radio o prestazioni. Il consolidamento NAS procede in una sessione distinta: i suoi file operativi e l'avanzamento fisico non sono stati modificati.

La raccomandazione di partenza è OPNsense a valle del Fastweb Seven. Dal 07/10/2026 lo switch è deciso: XMG1915-10EP con due access point cablati e alimentati in PoE ai piani centrali (ADR-017); le alternative con un solo AP e iniettore restano come storia della scelta. La Wi-Fi del Seven resta fuori da OPNsense fino alla migrazione. Per un lab che vuole anche RADIUS/EAP-TLS e monitoraggio SNMP, NWA130BE è il candidato più completo fra quelli confrontati; NWA50BE Pro è l'alternativa economica con limiti espliciti. Nessun acquisto è stato eseguito.

| Documento | Risultato |
|---|---|
| [Architettura e diagrammi](01-architettura.md) | separa stato documentato, proposta fisica, VLAN e flussi ammessi |
| [Servizi gratuiti](02-servizi-gratuiti.md) | confronta alternative, collocazione e costo operativo |
| [Switch e AP Zyxel](03-switch-e-access-point-zyxel.md) | specifiche, budget porte/PoE, prezzi indicativi e collaudo |
| [Piano di lavoro](04-piano-di-lavoro.md) | fasi, dipendenze e criteri di completamento |
| [Guida configurazione OPNsense](05-guida-configurazione-opnsense-in-casa.md) | percorso Seven -> OPNsense, VLAN, Wi-Fi upstream, prove e rollback |
| [Memo acquisti e configurazione](ACQUISTI-E-CONFIGURAZIONE-DA-FINIRE.md) | promemoria operativo copiato anche sul Desktop |
| [Accesso remoto VPN](06-accesso-remoto-vpn.md) | confronto Tailscale/WireGuard, subnet router, collaudo e uso di Tailcat |
| [Monitoraggio con Wazuh e Suricata](11-monitoraggio-wazuh-suricata.md) | componenti, percorsi dei dati con le porte, configurazione, risposta attiva, ripiego, ordine di messa in opera e collaudo |
| [Piano unificato](10-piano-unificato-hardware-e-stack.md) | ruoli dell'hardware, server Proxmox, stack open source per funzione con gli scarti verificati, stato di ogni scelta |
| [Accesso amministrativo](09-accesso-amministrativo.md) | tre ingressi e tre barriere per amministrare firewall, switch, AP e NAS |
| [Regole fra le zone](08-regole-fra-le-zone.md) | alias e regole per interfaccia, in forma di configurazione OPNsense, con il collaudo |
| [Doppio NAT dietro il modem in comodato](07-doppio-nat-dietro-modem-in-comodato.md) | documento didattico: perché due NAT, che cosa cambiano e che cosa no |
| [Inventario canonico](../../05-analisi-del-caso/01-tbc-studio-dispositivi-domestici.md) | dispositivi già citati, lacune e acquisti previsti |
| [Registro fonti](../../../SOURCES.md) | tutte le fonti consegnate, curate e censite |
| [Mappa di lettura](../../fonti/index-fonti.md) | screenshot, AdGuard, Strix, NovaSCM e riscontri di community |

## Assunzioni e decisioni ancora aperte

Al 07/10/2026 sono noti i piani, quattro, e i cavi verso i due AP, già posati; restano ignoti superficie, murature e budget. I due AP sono decisi, ma la copertura del piano terra resta da misurare. Il requisito preesistente è 2,5 GbE: la variante Gigabit compare come compromesso di costo, non come equivalente. Il desiderio di prendere spunto da NovaSCM non implica già la decisione di adottarlo o di usare EAP-TLS in tutta la casa.

L'inventario è completo rispetto alle voci già presenti nei documenti letti, non rispetto a tutti gli apparati fisicamente presenti nell'abitazione. I quattro desktop del consolidamento NAS non vengono identificati con i PC domestici omonimi per numero: la documentazione dice che sono un lotto distinto. Per chiudere il censimento servono osservazioni locali; la ricerca sul web non può produrle.

## Risultati della ricerca che incidono sul progetto

Le [specifiche Zyxel](https://www.zyxel.com/global/en/products/switch/xmg1915-series/specifications) smentiscono la vecchia affermazione che XMG1915 non abbia routing di livello 3. La scelta di progetto resta usare OPNsense come unico router fra zone. La distinzione [NWA50BE Pro BandFlex](https://www.zyxel.com/global/en/products/wireless/nwa50be-pro) rispetto a un AP a tre radio cambia la scelta per chi vuole 5 e 6 GHz simultaneamente. Il [dimensionamento Wazuh](https://documentation.wazuh.com/current/quickstart.html) richiede un host separato adeguato; gli 8 GB del firewall non sono un budget libero per l'intero stack. Il NAS a orario non può sostenere da solo la risoluzione DNS della casa.
