---
generated-from-commit: e89779723cb1ed715b781763011255a81a82700e
generated-from-branch: main
generated-date: 2026-08-24
covers-paths:
  - docs/**
last-verified-commit: e89779723cb1ed715b781763011255a81a82700e
---

# Roadmap

> Scheda tecnica. Fasi del progetto in ordine di dipendenza, non di preferenza: ogni fase assume che la precedente sia chiusa, e saltarne una produce lavoro da rifare. Le date non sono impegni: sono l'ordine in cui le cose possono accadere.

## Fase 0, conclusa: raccolta e studio

Durata effettiva dal gennaio al marzo 2026, con code successive. Ha prodotto il documento sorgente nella sua estensione attuale, il ticket all'operatore con la conferma del vincolo sull'ONT, la richiesta e l'ottenimento dell'indirizzo pubblico statico, il confronto fra le distribuzioni firewall, la scelta dello switch con le due alternative scartate, e l'installazione del sistema operativo del firewall il 16 gennaio 2026.

L'esito architetturale della fase e' uno solo e vale tutto il resto: il firewall non puo' essere l'apparato di frontiera, quindi la topologia e' a cascata dietro il modem dell'operatore, con doppio NAT e wireless inizialmente scoperto.

## Fase 1, in corso: documentazione versionata e pubblicabile

E' la feature descritta in `current-work.md`. Chiude quando il repository e' su un remoto pubblico con il guard-rail di anonimizzazione verde.

## Fase 2: configurazione del firewall

E' il primo lavoro che cambia lo stato della rete, e dipende dalla fase 1 solo nel senso che conviene avere la documentazione in ordine prima di modificarla.

Si comincia identificando fisicamente le tre interfacce dalla console del firewall, correlando nome di driver, indirizzo hardware e connettore con la verifica a LED. Si prosegue con l'assegnazione dei ruoli, ricordando che dopo l'assegnazione il firewall crea una regola permissiva sulla sola LAN mentre le altre zone partono chiuse in ingresso, quindi un errore di assegnazione espone verso l'esterno oppure taglia fuori dall'interfaccia di gestione. Si configurano poi gli indirizzi delle tre reti, verificando che non si sovrappongano, e infine le regole, partendo dal contratto fra zone descritto in `design-and-security.md`.

Resta da riverificare, prima di considerare chiusa la fase, l'avviso sulla generazione dei template osservato durante il boot dell'ambiente live.

## Fase 3: switch, segmentazione e wireless

Dipende dalla fase 2, perche' senza le interfacce del firewall configurate non c'e' nulla a cui collegare il trunk.

Si acquista e si configura lo switch gestito, definendo le VLAN e quali porte sono di accesso e quale e' il trunk verso il firewall. Si portano gli access point a valle dello switch, alimentati via iniettore, e si spegne o si degrada a rete ospiti la radio del modem. La fase chiude il buco strutturale del progetto, cioe' il wireless fuori dal perimetro, ed e' per questo che non e' facoltativa.

Il passaggio del cavo verso il piano inferiore e' la parte materialmente piu' difficile e ha una sua analisi dedicata nel documento sorgente, con la preferenza per un unico cavo continuo in rame solido invece che tratte accoppiate, e con la nota che la presa esistente a parete e' cablata come telefonica su cavo dati, quindi non utilizzabile come presa Ethernet finche' non viene riterminata su tutte e quattro le coppie.

## Fase 4: servizi interni

Dipende dalla fase 3 per la segmentazione, perche' ogni servizio va collocato in una zona e non in una rete piatta.

Nell'ordine di dipendenza: l'hypervisor sull'hardware disponibile, poi il resolver DNS interno con il motore di policy davanti, che e' il servizio con il maggior rapporto fra beneficio e sforzo e che richiede la regola di uscita sul firewall per essere reale; poi lo storage di rete, poi la gestione endpoint, ora nella variante con indirizzo statico dato che l'indirizzo dinamico e' decaduto.

## Fase 5: monitoraggio

Dipende dalla fase 4 perche' un SIEM senza sorgenti da correlare non serve a niente. Si parte dal solo componente centrale, che copre da solo SIEM, rilevamento sull'host e integrita' dei file, con gli agenti sugli endpoint e i log del firewall via syslog. L'indicizzazione con lo stack completo, la sonda sul traffico e i motori di correlazione si aggiungono solo se e quando il volume lo giustifica.

## Fase 6: verifica di sicurezza

Dipende da tutto il resto, perche' si verifica cio' che esiste. Scansione delle vulnerabilita' dall'interno su una macchina virtuale dedicata, con gli obiettivi definiti per rete. Prima di questa fase va aggiunta al piano di segmentazione una zona isolata per l'analisi dei campioni, oggi non prevista: eseguire codice sospetto su una rete che raggiunge la LAN vanifica l'intera architettura.

## Fase 7: la sezione oggi vuota

La macrosezione della documentazione destinata alla rete effettivamente realizzata si riempie man mano che le fasi da 2 a 6 si chiudono. Va scritta a valle di ogni fase e non alla fine di tutto, perche' scritta alla fine sarebbe ricostruzione a memoria e non documentazione.

## Fuori roadmap

Sono idee presenti nel documento sorgente che non hanno una collocazione nella sequenza sopra e che si affrontano solo se emerge un bisogno concreto: le telecamere esterne, con il problema irrisolto dell'alimentazione fuori dal portone; il rack; la telefonia su apparato proprio, che dipende dalla disponibilita' delle credenziali della fonia; e la posta self-hosted, che e' il servizio con il rapporto peggiore fra manutenzione richiesta e beneficio in un contesto domestico.
