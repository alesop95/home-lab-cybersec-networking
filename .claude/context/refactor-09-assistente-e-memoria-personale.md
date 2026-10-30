---
covers-paths: ["docs/03-spunti-di-sviluppo/23-studio-home-lab/17-assistente-personale-hermes-nix-e-memoria.md", "docs/03-spunti-di-sviluppo/23-studio-home-lab/06-accesso-remoto-vpn.md"]
last-verified-commit: 9499dcae3668e49bb1069664176ca459d386fa53
---

# Refactor09 - Un assistente ha ambiente, memoria e accessi distinti

Scheda del29/10/2026. Ritorno al [racconto](studio-didattico-master.md); riferimento operativo nello [studio17](../../docs/03-spunti-di-sviluppo/23-studio-home-lab/17-assistente-personale-hermes-nix-e-memoria.md). È uno sviluppo documentale, senza servizio installato.

## Com’era e perché disperdeva il ragionamento

La richiesta arriva mentre si prepara il dataset NAS: un computer dal consumo minimo, Hermes, Nix, Tailscale e un brain consultabile con Obsidian. Esistevano già un confronto VPN, uno studio del modello locale e un catalogo del template, ma mancava il collegamento fra quelle parti. La scheda STACK conteneva questa riga reale:

```text
WireGuard su OPNsense per l'accesso stabile, con un solo inoltro UDP sul modem; Tailscale come subnet router per una prima fase
```

Il documento VPN precisava invece che la decisione successiva ammetteva soltanto WireGuard per la gestione. Entrambe le frasi senza data di raccordo potevano sembrare lo stato corrente. Il nuovo requisito dell’utente impone di riconoscere Tailscale come direzione da studiare, senza scambiarlo per una rotta già funzionante.

## Il salto: ogni parte deve lasciare un artefatto recuperabile

La nuova scheda tecnica contiene questa frase reale:

```text
La base di conoscenza deve sopravvivere al cambio di modello o applicazione.
```

Il brain viene quindi descritto come contenuti, fonti e convenzioni. Obsidian è una vista su quei file; Opus5.5 è un modello candidato; Hermes svolge il lavoro e conserva anche stato operativo. Nix descrive l’ambiente, mentre vault e database continuano a cambiare durante l’uso. Il backup deve catturare entrambe le parti. Aver ricostruito i pacchetti non dimostra di aver recuperato l’ultima conversazione.

Lo stesso principio vale per la rete. Una richiesta Telegram in uscita non richiede il medesimo percorso di un client remoto che raggiunge un apparato domestico. Tailscale collega peer o reti autorizzate; i diritti del processo assistente si definiscono separatamente. ADR-045 aggiorna la direzione di progetto mantenendo aperta la verifica delle destinazioni ammesse, incluso l’eventuale raccordo con la gestione prevista da ADR-025.

## Il basso consumo si valuta sul servizio

Il dato utile non è il nome Raspberry né il TDP del processore. Una VM su un server già necessario può aggiungere poca energia; lo stesso server acceso solo per lei deve essere contato per intero. Lo studio17 conserva entrambe le ipotesi, senza inventare watt. Linux ARM64 è supportato da Hermes, ma Nix/NixOS ha una priorità di supporto inferiore: la scelta deve superare aggiornamento, riavvio e recupero prima di guidare un acquisto.

Il futuro esperimento misura lo stesso compito su corpus autorizzato, tempo, RAM, energia e costo del modello. La qualità si controlla tornando alle fonti delle risposte e verificando che una nota e una conversazione sopravvivano a un ripristino. Un login o un processo attivo non misurano questi risultati.

## Come prosegue senza creare memoria concorrente

Questo progetto ha già memoria versionata e registro. Il pacchetto knowledge-wiki viene raccordato allo studio del futuro archivio personale privato; non viene aggiunta un’altra fonte dello stato del lab. La capacità mantenuta dal template si recepirà quando sarà disponibile. A quella tappa si deve chiedere all’utente che cosa significhi «Jev», come richiesto nel suo chiarimento, e leggere l’impianto effettivo prima di definirne l’integrazione.

Fonti e limiti sono censiti nello studio17 e in S250-S260. Non sono provati hardware, modello attraverso Hermes, bot, subnet router o ripristino. Il valore già ottenuto è una proposta coerente e riprendibile, con decisioni future riconoscibili.
