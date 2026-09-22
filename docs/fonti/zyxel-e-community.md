---
tags: [fonti, zyxel, community, acquisti]
---

# Zyxel: come le fonti cambiano la scelta

Riferimenti S09-S26 nel [registro](../../SOURCES.md), ricerca del 22/09/2026. Le specifiche del produttore governano il confronto, le testimonianze servono a definire le prove. Non sono stati pubblicati messaggi nei forum ne' contattati venditori.

La [tabella XMG1915](https://www.zyxel.com/global/en/products/switch/xmg1915-series/specifications) corregge il vecchio documento: la famiglia ha funzioni di routing statico. Nel lab si decide di non usarle per il traffico fra zone, che deve attraversare OPNsense. Il thread [r/homelab sul 18EP](https://www.reddit.com/r/homelab/comments/1cpeo16/looking_to_upgrade_to_25g_any_opinions_on_the/) contiene un'esperienza diretta sul 10EP e commenti sul rumore del 18EP. Sono testimonianze, non statistiche di affidabilita'; la distinzione fra modelli con e senza ventola viene confermata sulla tabella ufficiale.

Il thread [NWA50BE Pro e bande radio](https://community.zyxel.com/en/discussion/30875/help-with-nwa50be-pro) contiene una risposta di personale Zyxel: prima radio a 2,4 GHz, seconda a scelta 5 o 6 GHz. Corrisponde alla [presentazione BandFlex](https://www.zyxel.com/global/en/products/wireless/nwa50be-pro). La conseguenza e' concreta: per tre bande simultanee si valuta NWA130BE, non si acquista il 50BE Pro fidandosi della dicitura commerciale tri-band.

Il thread [VLAN di gestione su NWA50AX](https://community.zyxel.com/en/discussion/14731/nwa50ax-managment-vlan) documenta un problema DHCP risolto allineando tagging fra AP e switch. Modello e firmware sono diversi dai candidati nuovi: non se ne copia la configurazione, se ne ricava una prova obbligatoria di coerenza fra VLAN di gestione, VLAN degli SSID e porta trunk. Il [comunicato MLO](https://community.zyxel.com/en/discussion/28852/heads-up-latest-wi-fi-7-enforces-new-mlo-change-zyxel-implement-in-7-20) motiva una prova separata sui client WPA2/legacy prima di attivare funzioni Wi-Fi 7 per tutti.

Il vecchio thread [budget PoE GS1900](https://community.zyxel.com/en/discussion/1150/gs1900-8hp-poe-budget) distingue riserva per classe e consumo reale. Non dimostra un difetto del futuro XMG1915: suggerisce di misurare accensione simultanea, allocazione e picchi. Analogamente i risultati di ricerca relativi a fine supporto o vulnerabilita' di altre serie restano nel diario come piste; non sono attribuiti ai candidati senza riscontro del produttore.

I prezzi dei comparatori sono segnali di mercato, con cache da una settimana a un mese, non quotazioni garantite al minuto. Il [confronto d'acquisto](../03-spunti-di-sviluppo/23-studio-home-lab/03-switch-e-access-point-zyxel.md) mostra separatamente specifiche, calcoli e stime, e lascia aperti budget, copertura e cablaggio finche' non rilevati.
