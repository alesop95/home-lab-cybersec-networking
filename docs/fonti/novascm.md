---
tags: [fonti, inventario, provisioning]
---

# NovaSCM: cosa riprendere e cosa provare

Fonti U06, S06-S08 nel [registro](../../SOURCES.md), consultate il 22/09/2026. Il dominio [NovaSCM](https://novascm.polariscore.it/) contiene un iframe verso la [pagina effettiva](https://www.polariscore.it/novascm/), letta tramite HTTP. Il sito dichiara scansione rete, inventario flotta, deploy Windows, Wi-Fi con certificati EAP-TLS e licenza MIT. Presenta anche una Linux Edition e descrive un primo deploy PXE completato, con ulteriori validazioni di enrollment ancora da fare: indicazione utile sullo stato del progetto, non collaudo nostro.

Il [repository collegato](https://github.com/ClaudioBecchis/NovaSCM) descrive console Windows WPF, server API multipiattaforma, agenti, workflow, gestione di VM e container Proxmox. La console da sola non copre tutte le funzioni del server. Il testo della licenza e la release effettivamente utilizzabile vanno riverificati prima dell'adozione; la presentazione web della Linux Edition non dimostra che sia inclusa nel medesimo artefatto Windows.

## Trasferimento al progetto

L'idea piu' utile subito e' collegare ciascun dispositivo a stato, sistema operativo, ultima osservazione, software, ruolo e interventi. Questo entra nell'[inventario del lab](../05-analisi-del-caso/01-tbc-studio-dispositivi-domestici.md) senza aspettare di installare una piattaforma. Il passo successivo e' rendere ripetibili configurazione e verifica di una VM di prova.

NovaSCM e' candidato sperimentale per provisioning e workflow, da confrontare con [GLPI](https://www.glpi-project.org/en/features/) per inventario patrimoniale, [NetBox](https://netboxlabs.com/docs/netbox/) per rete e indirizzamento, [MeshCentral](https://github.com/Ylianst/MeshCentral) per assistenza remota. Hanno scopi diversi; installarli tutti creerebbe registri duplicati da riconciliare. La prima autorita' resta l'inventario versionato e anonimizzato con dettagli operativi privati.

Il pilota proposto usa una VM Windows sacrificabile: enrollment, rilevamento inventario, workflow innocuo verificabile, riavvio, rimozione agente e ripristino del database. PXE e DHCP si provano solo nella VLAN LAB. Per EAP-TLS servono anche autorita' certificati, RADIUS, supporto dell'AP e gestione revoche; il solo software non aggiunge queste funzioni a un AP che non le supporta. Questa esigenza e' collegata allo [studio Zyxel](../03-spunti-di-sviluppo/23-studio-home-lab/03-switch-e-access-point-zyxel.md).
