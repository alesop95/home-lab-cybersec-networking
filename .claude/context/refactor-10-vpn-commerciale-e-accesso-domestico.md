---
covers-paths: ["docs/03-spunti-di-sviluppo/23-studio-home-lab/18-nordvpn-account-condiviso-e-confini-domestici.md", "docs/03-spunti-di-sviluppo/23-studio-home-lab/06-accesso-remoto-vpn.md", "docs/04-concetti-generali/09-che-cosa-non-e-una-vpn.md"]
last-verified-commit: 9882943b20c06c81ffb4250f5c6743da790a1c69
---

# Refactor10 - Uscire con una VPN e rientrare a casa richiedono confini diversi

Scheda del29/10/2026. Ritorno al [racconto](studio-didattico-master.md); scelte e fonti nello [studio18](../../docs/03-spunti-di-sviluppo/23-studio-home-lab/18-nordvpn-account-condiviso-e-confini-domestici.md). È un raccordo documentale, senza configurazioni di rete eseguite.

## Com’era e perché le etichette non bastavano

Il progetto aveva un confronto di accesso remoto e aveva appena aggiunto Tailscale per l’assistente. L’utente richiama un rapporto sul non uso domestico di NordVPN e sui rischi di un account condiviso. Usare soltanto la parola VPN avrebbe permesso di importare quella esclusione anche dove il bisogno era raggiungere il NAS, oppure di introdurre Meshnet come collegamento già autorizzato.

Gli appunti concettuali contenevano questa frase reale:

```text
Una VPN non protegge il traffico, lo occulta durante il trasporto.
```

Confondeva il limite della protezione applicativa con l’assenza di protezione del canale. Lo stesso testo descriveva tutti i componenti aggiuntivi come filtri DNS/IP; la documentazione del produttore descrive anche funzioni distinte sul dispositivo. Serve conservare il confine, senza negare proprietà che il canale o i componenti possono avere.

## Il salto: nome, identità e percorso

Lo studio18 ora contiene questa frase reale:

```text
Il firewall continua a vedere e governare la connessione esterna del tunnel; non scompare dal percorso.
```

La differenza riguarda ciò che quel controllo vede: la connessione esterna cifrata può attraversarlo mentre il DNS e i flussi interni non seguono il percorso previsto. Perciò la scelta è NordVPN spenta nella rete di casa e nessuna VPN commerciale sull’intero router, senza attribuire al firewall una scomparsa fisica dal cammino dei pacchetti. Il firewall definitivo e i resolver sono ancora da configurare: la scelta non è una misura di protezione già in esercizio.

Meshnet è un altro componente, con permessi propri. Il progetto esclude il suo uso con l’account condiviso; gli accessi a casa restano nel disegno WireGuard e nel nuovo studio Tailscale. L’identità condivisa non entra così nella gestione di NAS, router o archivio personale. Il rapporto locale non viene modificato: si conserva il suo contenuto e si raccordano qui le parti superate dalle decisioni di questo progetto.

## La stessa disciplina vale per gli interruttori

Android distingue VPN sempre attiva dal blocco delle connessioni fuori VPN. Confonderli porta a spiegare un guasto Internet con il nome del prodotto anziché con la policy effettiva. Anche il singolo servizio VPN attivo per profilo conta quando si passa dall’uscita commerciale al tunnel verso casa. Queste proprietà sono verificate nelle fonti Android; la configurazione del telefono concreto non è stata ispezionata.

Il rapporto contiene un’altra semplificazione da non trasferire: su una rete estranea la VPN non è l’unica protezione, perché HTTPS protegge il suo canale. La verifica futura deve misurare bisogno, DNS, raggiungibilità e permessi; un’icona di connessione non dimostra che tutti questi controlli siano al posto giusto. Analogamente, nel banco NAS il tipo di ACL visto in un pannello senza il nome del dataset non si attribuisce automaticamente al figlio documenti: identità dell’oggetto e valore osservato sono entrambi necessari.

Fonti S261-S268 e ADR-046 nello studio18. Restano da provare endpoint, resolver e flussi di accesso; nessun account condiviso o dato personale del monitor è stato aperto dall’agente.
