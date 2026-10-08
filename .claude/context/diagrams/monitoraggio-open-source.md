---
generated-from-commit: 86b5c8a61a55a48997d7757592aa4d91da9e8581
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - docs/03-spunti-di-sviluppo/09-monitoraggio/**
  - docs/03-spunti-di-sviluppo/08-malware-analysis-free-open-source-solutions/**
last-verified-commit: 6769dc4
---

# Workflow di monitoraggio e analisi

> Trasposizione testuale e versionabile dei due flussi descritti nel documento sorgente: il monitoraggio di sicurezza continuo e il percorso di analisi di un campione sospetto. Il primo esiste anche come immagine alla radice del progetto, non versionata; questo diagramma la sostituisce e ne corregge un difetto, cioè che l'immagine mostrava due volte lo stesso componente senza distinguerne il ruolo.

## Monitoraggio continuo

Aggiornamento dell'8/10/2026: verificati sulle fonti, MozDef è archiviato dal 2021, OSSIM è ritirato da fine 2024, Apache Metron è ritirato dal 2020, Sagan è fermo alla versione del 2021, e OPNsense non integra Snort. Il flusso adottato dal [piano unificato](../../../docs/03-spunti-di-sviluppo/23-studio-home-lab/10-piano-unificato-hardware-e-stack.md) è quindi più corto: agenti e syslog verso Wazuh su Proxmox, Suricata nel firewall, l'indicizzatore di Wazuh al posto di uno stack ELK separato. Il diagramma che segue resta come trascrizione dello schema del documento sorgente.

Il flusso ha un centro chiaro, Wazuh, che raccoglie dagli endpoint e correla, e una spina dorsale di indicizzazione, lo stack Elasticsearch con i suoi contorni, dove confluisce tutto il resto. Nessuno di questi componenti è installato: il flusso è un piano.

```
  [ endpoint: PC, server, VM, NAS ]
              |
              | agente Wazuh
              v
        [ WAZUH ]  <----- eventi IDS ------ [ SNORT ]
     SIEM + HIDS + FIM                    analisi pacchetti
     correlazione, alert                  in ingresso e uscita
              |                                  ^
              |                                  |
              |                            traffico di rete
              v
   [ ELK: Elasticsearch + Logstash + Beats + Kibana ]
     indicizzazione, ricerca, dashboard
              ^                    |
              |                    v
   log via syslog            [ SAGAN ]
   dal firewall e            correlazione log
   dagli apparati            in tempo reale
                                   |
                                   v
                             [ MOZDEF ]
                        orchestrazione incidenti,
                        vista in stile SOC
                                   |
                                   v
                     [ OSSIM o Apache Metron ]
                     estensione opzionale, solo se
                     il volume lo giustifica
```

La lettura corretta è che Wazuh è l'unico componente indispensabile per iniziare, perché da solo copre SIEM, rilevamento sull'host e controllo di integrità dei file, ed è più leggero di OSSIM e più completo di Snort da solo. Snort aggiunge la visibilità sul traffico, che Wazuh non ha; lo stack ELK aggiunge la capacità di interrogare grandi volumi, che serve solo quando i volumi ci sono; Sagan e MozDef sono raffinamenti che hanno senso quando esistono già più sorgenti da correlare e incidenti da gestire come tali. Adottarli tutti insieme in una rete domestica sarebbe sovradimensionato, e il documento sorgente lo dice esplicitamente.

Sulla sonda di rete i documenti divergono, e la differenza va tenuta presente. L'analisi del monitoraggio sotto `09-monitoraggio/` ragiona su Snort come componente separato; lo studio home lab del 22/09/2026, nei servizi gratuiti, indica invece Suricata integrato in OPNsense, in sola rilevazione prima di qualunque blocco e solo dopo test prestazionali sul firewall. La seconda strada non aggiunge una macchina e usa il motore che il firewall già include, quindi è quella da cui partire; la scelta definitiva resta alla fase 5.

## Il posto del monitoraggio nella rete

Il nodo di monitoraggio non è il firewall. Il documento sorgente è netto su questo punto: il firewall deve restare un apparato deterministico che non esegue servizi estranei alla sicurezza di rete. Il SIEM vive quindi su una macchina separata nella LAN, o in una macchina virtuale sull'hypervisor, e riceve i log del firewall via syslog come li riceverebbe da qualunque altro apparato.

```
   [ FIREWALL ] --syslog--> [ nodo SIEM in LAN ] <--agenti-- [ endpoint ]
       |                            |
   nessun servizio             Wazuh, ELK, dashboard
   estraneo qui                virtualizzati su Proxmox
```

Accanto al SIEM il documento prevede un nodo di diagnostica separato, basato su una distribuzione con strumenti di rete preinstallati, da usare per analisi puntuali con analizzatore di pacchetti, scanner di porte e visualizzazione della topologia. È uno strumento da postazione, non un servizio permanente, e può vivere anche come sistema avviabile da chiavetta.

## Analisi di un campione sospetto

Il secondo flusso è un percorso a fasi, non un'architettura: nessuno di questi strumenti resta in esecuzione, si usano uno dopo l'altro su un singolo artefatto.

```
  campione
     |
     v
  [ reputazione ]  VirusTotal
     |            verifica rapida, firme gia' note
     v
  [ analisi statica ]  PeStudio (metadati, stringhe, import)
     |                 YARA (regole e famiglie note)
     |                 CyberChef (decodifica payload e script)
     v
  [ reverse engineering ]  Ghidra (codice, funzioni, flussi)
     |                     x64dbg o Radare2 (esecuzione passo passo)
     |                     Frida (instrumentation dinamica selettiva)
     v
  [ analisi dinamica ]  Cuckoo Sandbox (on-premise, configurabile)
     |                  Hybrid Analysis (servizio, report strutturati)
     v
  [ effetti sul sistema ]  Process Monitor (file, registro, processi)
     |                     Autoruns (meccanismi di persistenza)
     v
  [ analisi di rete ]  Wireshark (traffico generato)
     |                 Fiddler (HTTP e HTTPS verso eventuale C2)
     v
  indicatori di compromissione e report
```

La sequenza non è rigida: si scende di fase solo se la precedente lascia dubbi, e si torna indietro quando l'analisi dinamica rivela qualcosa che va cercato di nuovo nel binario. Il vincolo vero, che il documento sorgente non affronta e che va risolto prima di eseguire qualunque campione, è l'isolamento: la sandbox deve stare su una rete che non può raggiungere né la LAN né Internet senza controllo, il che nel piano di segmentazione significa una VLAN dedicata con regole di uscita esplicite, oggi non prevista. Va aggiunto al piano prima di questa attività, non dopo.
