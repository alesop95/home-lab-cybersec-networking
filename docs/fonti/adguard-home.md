---
tags: [fonti, dns, adguard]
---

# AdGuard Home: lettura dell'articolo e adattamento al lab

Fonte U04 nel [registro](../../SOURCES.md): [articolo su Ubuntu Server 26.04 e Compose](https://www.raffaelechiatto.com/installazione-e-configurazione-base-di-adguard-home-su-ubuntu-server-26-04-con-docker-compose/), pubblicato il 17/09/2026 e letto il 22/09/2026. Il browser di ricerca non lo recuperava; il testo e' stato ottenuto dall'API pubblica WordPress con lo slug dell'articolo. Il primo estrattore HTML aveva selezionato un articolo correlato: quel risultato non e' stato usato come contenuto della fonte.

L'articolo propone volumi `work` e `conf`, liberazione della porta 53 da `systemd-resolved`, immagine `latest`, wizard sulla 3000, dashboard sulla 80 e pubblicazione di porte opzionali per DNS cifrato. Illustra impostazione del DNS nei client/DHCP, blocklist e aggiornamento con Compose. Segnala correttamente il punto singolo di guasto e propone una seconda istanza. E' una procedura di terzi letta, non eseguita qui.

Le fonti primarie di confronto sono la [guida Docker ufficiale](https://github.com/AdguardTeam/AdGuardHome/wiki/Docker), disponibile anche come [testo raw](https://raw.githubusercontent.com/wiki/AdguardTeam/AdGuardHome/Docker.md), e la [documentazione Unbound di OPNsense](https://docs.opnsense.org/manual/unbound.html). La guida Docker tratta persistenza, IP dei client, DHCP e conflitto con il resolver dell'host. Unbound offre risoluzione e configurazioni locali, incluse liste di blocco: AdGuard non e' un prerequisito per avviare la rete.

## Scelte progettuali derivate, da collaudare

La prima fase usa Unbound sul firewall. AdGuard entra su un host sempre acceso quando questo sara' identificato; il NAS a orario non puo' essere l'unico DNS. Si sceglie un solo punto di filtraggio: AdGuard per liste e statistiche, Unbound a monte per risoluzione e nomi interni. Non configurare un inoltro reciproco che formi un ciclo. Il DHCP resta su OPNsense, con un solo servizio autorevole per segmento.

Il Compose effettivo va preparato dopo scelta di IP, host e politica DNS. La proposta e' fissare versione o digest, pubblicare soltanto le porte necessarie, limitare gestione alla VLAN amministrativa e prevedere backup dei volumi prima dell'aggiornamento. Una versione precedente del container non garantisce il rollback di dati modificati dalla nuova versione. Il conflitto sulla 53 si misura sulle interfacce reali prima di cambiare `systemd-resolved`; il comando del blog non diventa automaticamente una prescrizione per ogni host.

Pubblicare un secondo DNS pubblico ai client puo' consentire risoluzioni che saltano il filtro; due resolver devono rispettare la stessa politica, su host indipendenti se serve continuita'. Si prova prima una sola VLAN, verificando nomi interni, risoluzione TCP/UDP, riavvio, guasto del DNS, IPv6 e dispositivi con DNS cifrato proprio. Il filtraggio per dominio non puo' separare contenuti pubblicitari e leciti serviti dallo stesso dominio. La gestione non viene pubblicata su Internet.

Applicazione nello [studio servizi](../03-spunti-di-sviluppo/23-studio-home-lab/02-servizi-gratuiti.md) e nel [diagramma](../03-spunti-di-sviluppo/23-studio-home-lab/01-architettura.md).
