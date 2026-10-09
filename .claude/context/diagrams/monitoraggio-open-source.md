---
generated-from-commit: 86b5c8a61a55a48997d7757592aa4d91da9e8581
generated-from-branch: main
generated-date: 2026-08-25
covers-paths:
  - docs/03-spunti-di-sviluppo/09-monitoraggio/**
  - docs/03-spunti-di-sviluppo/08-malware-analysis-free-open-source-solutions/**
last-verified-commit: ee63b19
---

# Workflow di monitoraggio e analisi

> Trasposizione testuale e versionabile dei due flussi descritti nel documento sorgente: il monitoraggio di sicurezza continuo e il percorso di analisi di un campione sospetto. L'immagine dello schema della prima stesura è stata eliminata l'8/10/2026 (ADR-027).

## Monitoraggio continuo

Dall'8/10/2026 il flusso è quello del [piano unificato](../../../docs/03-spunti-di-sviluppo/23-studio-home-lab/10-piano-unificato-hardware-e-stack.md), descritto tecnicamente in [Monitoraggio di sicurezza con Wazuh e Suricata](../../../docs/03-spunti-di-sviluppo/23-studio-home-lab/11-monitoraggio-wazuh-suricata.md) e approvato dall'utente (ADR-028). La trascrizione dello schema della prima stesura, che collegava Wazuh a ELK, Snort, Sagan, MozDef, OSSIM e Apache Metron, è stata tolta insieme alle sue fonti su indicazione dell'utente (ADR-027), perché quei componenti sono archiviati, ritirati o sostituiti.

```
  [ PC della VLAN 10, laboratorio ] --agente, TCP 1514--+
                                                       |
  [ OPNsense: filtro, accessi, VPN ]                    v
  [ Suricata in OPNsense ] --plugin os-wazuh-agent--> [ Wazuh su Proxmox ]
                                                       ^   server, indicizzatore,
  [ switch, AP nella VLAN 99, NAS ] --syslog, UDP 514--+   dashboard nella VLAN 99
```

Wazuh è il solo centro: correla gli eventi degli host, i log degli apparati e gli allarmi di Suricata, li conserva per 90 giorni e li mostra. Suricata parte in sola rilevazione e la risposta attiva resta spenta finché gli allarmi non sono stati letti per settimane.

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
