# SIEM analysis

Riscritto l'8/10/2026 su indicazione dell'utente (ADR-027): da questo documento sono state tolte le parti sugli strumenti scartati dal [piano unificato](../23-studio-home-lab/10-piano-unificato-hardware-e-stack.md), cioè OSSIM, lo stack ELK separato con Elasticsearch, Apache Metron, MozDef, Sagan e Snort, insieme all'immagine dello schema che li collegava. Le ragioni dello scarto, verificate sulle fonti, sono nel piano unificato. Il flusso adottato, Wazuh al centro con Suricata integrato in OPNsense, è descritto tecnicamente in [Monitoraggio di sicurezza con Wazuh e Suricata](../23-studio-home-lab/11-monitoraggio-wazuh-suricata.md). Resta qui il testo dell'autore sui componenti che il progetto usa o che non ha ancora valutato.

## SIEM

### Wazuh

Soluzione on-premises che offre rilevamento delle minacce, gestione degli incidenti e supporto alla conformità. Derivato da OSSEC, integra funzionalità SIEM, IDS e monitoraggio host.

Per una rete domestica molto complessa con molti dispositivi, VLAN, IoT, server interni, firewall avanzati, Wazuh è un ottima scelta. È gratuito, moderno e attivo come progetto e unisce SIEM, IDS HIDS, monitoraggio host e integrazione log. È più leggero e gestibile di OSSIM o Metron (che richiedono infrastrutture importanti). È più completo di Snort, che è solo IDS. È più semplice da integrare rispetto a ELK “puro”, che richiede più lavoro di orchestrazione.

Wazuh si colloca al centro del sistema di logging, quindi gli endpoint (PC, server, VM, NAS) inviano log tramite l’agenze Wazuh. Il firewall invia log via syslog verso Wazuh. Eventuali strumenti IDS come Snort possono inviare eventi a Wazuh. Wazuh correla eventi, genera alert, monitora l’integrità dei file e il comportamento degli host.

In una rete domestica complessa, Wazuh funge da mini-SOC interno, offrendo visibilità completa e centralizzata sulle attività di sicurezza.

Guardare anche il progetto Home Lab Cybersecurity & Infrastructure (Autore-LinkedIn-B). Nella chat con [Autore-LinkedIn-A](https://www.linkedin.com/in/ACoAABSc9aABi8vyWB72YzZwoXloPfaest2-sm0), e nella home Lab che aveva postato ancora non era stata creata la VM lxc di Wazuh e la sua rete è controllata anche da lui una vera bomba come endpoint opensource molto potente.

Nota dell'8/10/2026: i confronti di questa sezione con OSSIM, Metron, Snort ed ELK restano come ragionamento dell'autore. Nel progetto il rilevamento sul traffico lo fa Suricata dentro OPNsense, e i suoi eventi arrivano a Wazuh con il plugin `os-wazuh-agent` del firewall.

## Analisi log

### Splunk Free

Versione gratuita di Splunk che permette l’indicizzazione fino a 500 MB giornalieri per analisi dei dati in tempo reale e gestione di alert. Ideale per piccoli ambienti di test o reti ridotte.

Nota dell'8/10/2026: Splunk Free non è un software open source e il progetto non lo adotta; la sezione resta come voce del censimento dell'autore.
