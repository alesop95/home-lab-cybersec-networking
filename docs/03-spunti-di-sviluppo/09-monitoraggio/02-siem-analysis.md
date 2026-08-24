# SIEM analysis

## Introduzione e workflow

Un workflow di sicurezza realmente completo può essere composto interamente da soluzioni open-source integrando funzioni SIEM, IDS, correlazione degli eventi e analisi centralizzata. La base del sistema è rappresentata da Wazuh, che svolge il ruolo di piattaforma centrale per il rilevamento delle minacce, il monitoraggio degli host e la gestione degli incidenti. Gli endpoint, i server e i dispositivi critici inviano i loro log direttamente a Wazuh tramite agenti dedicati, permettendo una visione dettagliata delle attività interne, del controllo dell’integrità dei file e dell'identificazione di comportamenti anomali.

![](assets/img-0022.png)

*Parallelamente*, il firewall e gli apparati di rete esterni inviano i log attraverso syslog verso il cluster Elasticsearch, che costituisce il motore di indicizzazione e memorizzazione dell’intero sistema. L’insieme Elasticsearch, Logstash, Beats e Kibana - noto come ELK Stack fornisce l’infrastruttura di raccolta, trasformazione e visualizzazione, consentendo di trattare grandi volumi di dati con interrogazioni rapide e dashboard personalizzate.

Per rafforzare la protezione della rete, Snort viene collocato nel punto in cui il traffico entra ed esce dall’infrastruttura, con il compito di analizzare in tempo reale i pacchetti e generare allarmi in caso di minacce note o pattern sospetti. Gli eventi generati da Snort vengono inviati a Wazuh e arricchiti da quest’ultimo con dati contestuali relativi agli host coinvolti, migliorando significativamente la qualità della correlazione.

A questo livello interviene Sagan, che viene posizionato come motore di correlazione in tempo reale basato sui log, utile per unire informazioni provenienti da fonti differenti, individuare collegamenti tra eventi distinti e generare alert più precisi rispetto all’analisi dei singoli log.

La parte superiore del workflow può essere affidata a MozDef, che funge da orchestratore degli incidenti, permettendo di gestire i flussi di eventi attraverso microservizi e di integrarsi con dashboard o sistemi di notifica già esistenti. MozDef consente di creare una vista operativa simile a quella di un SOC, aggregando gli alert provenienti da Wazuh, Sagan e Snort e trasformandoli in incidenti strutturati. In situazioni dove occorre anche un ambiente SIEM più completo, OSSIM o Apache Metron possono estendere la capacità di analisi, soprattutto quando il volume dei log e degli eventi richiede una soluzione capace di arricchire e normalizzare i dati tramite pipeline avanzate, pur rimanendo gratuite.

L’intero sistema lavora come un ecosistema unico: gli endpoint inviano eventi a Wazuh, la rete genera traffico analizzato da Snort, i log scorrono attraverso ELK, la correlazione avviene tramite Sagan e la gestione operativa si concentra in MozDef. Il risultato è un workflow fluido, modulare e completamente open-source, capace di coprire raccolta, analisi, correlazione, rilevamento e gestione degli incidenti senza dipendenza da soluzioni proprietarie.

## SIEM completi / piattaforme di security operations

### OSSIM

Offre modalità sia server-agent che serverless, con analisi dei log per mail server, database e molte altre fonti. È una delle piattaforme SIEM open-source più complete e strutturate disponibili gratuitamente.

### ELK Stack

Combina Elasticsearch con strumenti come Kibana, Beats e Logstash per offrire una soluzione SIEM completa, modulare e ampiamente estendibile. È adottata come standard open-source per la centralizzazione dei log.

#### Elasticsearch

Permette di combinare vari tipi di log e di scorrerli facilmente, gestendo grandi volumi di dati con prestazioni elevate. Rappresenta la *base* di molte architetture SIEM open-source.

### Wazuh

Soluzione on-premises che offre rilevamento delle minacce, gestione degli incidenti e supporto alla conformità. Derivato da OSSEC, integra funzionalità SIEM, IDS e monitoraggio host.

Per una rete domestica molto complessa con molti dispositivi, VLAN, IoT, server interni, firewall avanzati, Wazuh è un ottima scelta. È gratuito, moderno e attivo come progetto e unisce SIEM, IDS HIDS, monitoraggio host e integrazione log. È più leggero e gestibile di OSSIM o Metron (che richiedono infrastrutture importanti). È più completo di Snort, che è solo IDS. È più semplice da integrare rispetto a ELK “puro”, che richiede più lavoro di orchestrazione.

Wazuh si colloca al centro del sistema di logging, quindi gli endpoint (PC, server, VM, NAS) inviano log tramite l’agenze Wazuh. Il firewall invia log via syslog verso Wazuh. Eventuali strumenti IDS come Snort possono inviare eventi a Wazuh. Wazuh correla eventi, genera alert, monitora l’integrità dei file e il comportamento degli host.

In una rete domestica complessa, Wazuh funge da mini-SOC interno, offrendo visibilità completa e centralizzata sulle attività di sicurezza.

Guardare anche il progetto Home Lab Cybersecurity & Infrastructure (Autore-LinkedIn-B). Nella chat con [Autore-LinkedIn-A](https://www.linkedin.com/in/ACoAABSc9aABi8vyWB72YzZwoXloPfaest2-sm0), e nella home Lab che aveva postato ancora non era stata creata la VM lxc di Wazuh e la sua rete è controllata anche da lui una vera bomba come endpoint opensource molto potente.

### Apache Metron

Combina funzioni tipiche di un SOC all’interno di una piattaforma centralizzata progettata per la rilevazione di minacce su larga scala. Utilizza pipeline avanzate di ingest e analisi dei dati.

### MozDef

Strumento basato su microservizi che può integrarsi con piattaforme di terze parti per fornire insight di sicurezza chiari e strutturati. Progettato da Mozilla per orchestrare eventi e incidenti.

## Analisi log / correlazione

### Sagan

Strumento di analisi e correlazione dei log in tempo reale, compatibile con console grafiche come Snorby ed EveBox. È indicato per chi necessita di un motore veloce e leggero per la correlazione.

### Splunk Free

Versione gratuita di Splunk che permette l’indicizzazione fino a 500 MB giornalieri per analisi dei dati in tempo reale e gestione di alert. Ideale per piccoli ambienti di test o reti ridotte.

## IDS / rilevamento traffico

### Snort

Analizza il traffico di rete in tempo reale, con funzionalità adatte principalmente a professionisti esperti. È uno dei principali IDS open-source per rilevamento di attacchi e anomalie.
