---
covers-paths: ["docs/03-spunti-di-sviluppo/23-studio-home-lab/19-microcontrollori-microserver-e-laboratorio-browser.md", "docs/03-spunti-di-sviluppo/23-studio-home-lab/17-assistente-personale-hermes-nix-e-memoria.md"]
last-verified-commit: 3c876a64c6530edd1482284575a36ca631cce678
---

# Refactor11 - Un nodo che dorme e un assistente sempre pronto

Scheda del29/10/2026. Ritorno al [racconto](studio-didattico-master.md); dettaglio e fonti nello [studio19](../../docs/03-spunti-di-sviluppo/23-studio-home-lab/19-microcontrollori-microserver-e-laboratorio-browser.md).

## La fragilità della parola microserver

La roadmap dell’assistente aveva già questa sequenza reale nello studio17:

```text
Prototipo su host disponibile, prima di acquistare hardware.
```

L’idea di scegliere il processore più piccolo possibile può saltare proprio quel passaggio. Un ESP32 che pubblica un messaggio è un servizio, ma non è per questo l’host Python/Linux dell’agente. Né il Pico dello studio audio dimostra un Raspberry Linux già posseduto. Il nuovo confronto conserva la sequenza e assegna la classe di macchina al compito prima dell’acquisto.

## Il salto: tre costi e due confini

Il costo elettrico appartiene all’intero nodo e alla disponibilità richiesta; il costo dell’inferenza appartiene al modello scelto; il costo operativo appartiene a aggiornamenti, stato e recupero. S273 descrive il sonno della radio: non si può confrontare quel valore con una macchina che risponde sempre senza dichiarare la diversa disponibilità.

Il nuovo studio19 fissa queste due righe reali di progetto:

```text
VLAN40 IoT: nodi MCU non fidati.
VLAN30 servizi: host Linux dell’assistente con autorizzazioni specifiche.
```

Il mezzo radio non decide il livello di fiducia. Un AP associa SSID a VLAN, poi il firewall filtra i flussi tra zone. Condividere la Wi-Fi non significa condividere permessi. Il passo discriminante futuro è tentare un collegamento IoT verso gestione e NAS: deve fallire mentre il broker autorizzato funziona. Una simulazione firmware non prova quel confine fisico.

## Come estendere senza perdere il criterio

Per una nuova scheda aggiungere compito, runtime, disponibilità, RAM, misura alla presa e prova di recupero. Non basta la corrente minima del chip o l’etichetta AI. Riutilizzare prima il prototipo su host disponibile; scegliere il dedicato solo con dati confrontabili. Nessuna prova hardware già compiuta in questa scheda.
