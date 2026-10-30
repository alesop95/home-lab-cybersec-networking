# OPNsense: aggiornamento prima della messa in servizio

Verifica delle fonti ufficiali del29/10/2026, ADR-048. Il [verbale](../../verbale-installazione-opnsense.md) documenta l’installazione del16/01/2026 di OPNsense25.7 senza rete configurata. Non è stata letta oggi la console della macchina: versione attuale, stato del disco e configurazione reale non accertati. Non si dichiara un aggiornamento eseguito.

## Versione da preparare

Le [release notes Community26.7](https://docs.opnsense.org/releases/CE_26.7.html), S277, riportano26.7.7 del13/10/2026 come ultima voce consultata. Il [comunicato ufficiale del21/10](https://forum.opnsense.org/index.php?topic=53191.msg276103), S278, aggiunge un hotfix per CVE-2026-109618 e CVE-2026-109619: sulla Community26.7.7 porta PHP a8.5.12. Quindi il criterio non è vedere soltanto26.7.7: occorre anche applicare gli aggiornamenti di sicurezza successivi e verificare la versione del pacchetto correttivo o una revisione successiva che lo includa. Il servizio captive portal, se usato, va riavviato come indicato dal produttore; non risulta adottato qui.

L’immagine installabile e il livello dei pacchetti aggiornati sono cose diverse. Le note rimandano a immagini della serie26.7: non si inventa una ISO chiamata26.7.7 e non si riutilizza una checksum relativa a un’immagine diversa. Prima del download effettivo si ricontrollano versione Production corrente, architettura, tipo immagine per l’apparato, checksum e firma ufficiali. La Business Edition segue numeri differenti e non determina la versione Community scelta.

Non abbiamo elementi per attribuire un exploit alla macchina del lab o affermare che qualsiasi problema del vecchio sistema sia questa CVE. L’installazione storica25.7 non è la base da attivare oggi davanti alla rete domestica. La sicurezza richiede versione mantenuta, patch, configurazione e gestione protetta; il solo aggiornamento non chiude tutto il disegno.

## Percorso operativo da eseguire alla console

Prima si accende il firewall in una finestra dedicata con monitor/tastiera o console disponibile e si legge versione, interfacce e presenza di configurazione da conservare. Si esporta la configurazione e la si archivia nel livello privato con hash e indicazione della versione. Non si sovrascrive il disco finché non è chiaro se quel sistema contiene lavoro da mantenere. Il NAS resta sul proprio percorso operativo.

Se la macchina è ancora l’installazione vuota del verbale, una reinstallazione della release Production corrente seguita dagli aggiornamenti è il candidato più semplice, da rendere concreto dopo la lettura. Se contiene impostazioni, si valuta il percorso supportato di upgrade e il recupero prima di cambiare versione principale. Non si prescrive un salto diretto da25.7 a26.7.7 senza verificarne i passaggi supportati. Le nuove schermate26.7 possono differire dalla guida storica: si aggiorna il documento sulla UI realmente vista.

La [guida ufficiale aggiornamenti](https://docs.opnsense.org/manual/updates.html), S283, indica System > Firmware > Settings con Release Type Production e System > Firmware > Status > Check for updates per gli aggiornamenti. Per gli upgrade principali raccomanda console disponibile; la fase offline interrompe web e SSH. Ripetere verifica e aggiornamento fino al livello corrente, poi leggere versione del sistema e pacchetti interessati e l’esito degli audit disponibili. Nessun valore è già stato impostato qui.

Il riscontro discriminante del hotfix è leggere il pacchetto PHP corretto sulla macchina dopo l’aggiornamento, non il nome del file scaricato. Il collaudo operativo comprende riavvio, interfaccia di gestione raggiungibile dalla zona prevista e rifiutata dalle zone escluse, DHCP/DNS/ora e traffico necessario secondo la guida domestica. Conservare un export della configurazione dopo la tappa e una via di ripristino prima di spostare il cablaggio della casa. Download, reinstallazione e collaudo sono ancora aperti, nessuna scansione della rete aziendale richiesta.

Raccordi: [governo della sicurezza](20-governo-sicurezza-e-privacy-domestiche.md), [guida in casa](05-guida-configurazione-opnsense-in-casa.md) e [piano di lavoro](04-piano-di-lavoro.md). La versione va riverificata al giorno dell’intervento:26.7.7 più hotfix è il riscontro di oggi, non una versione da fissare per sempre nel progetto.
