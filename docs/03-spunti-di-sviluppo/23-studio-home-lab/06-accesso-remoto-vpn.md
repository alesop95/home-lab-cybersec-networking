# Accesso remoto al laboratorio: Tailscale e WireGuard

L'accesso remoto è compatibile con la topologia attuale, ma non cambia la catena WAN: `ONT -> Fastweb Seven -> OPNsense`. La VPN deve terminare su OPNsense oppure su un host sempre acceso a valle. L'IP pubblico statico aiuta soprattutto WireGuard esposto direttamente; Tailscale normalmente evita di pubblicare una porta sul Seven e usa un overlay autenticato.

## Scelta iniziale consigliata

Per una prima fase si può installare Tailscale su un host Linux sempre acceso nella VLAN servizi e usarlo come *subnet router* verso una sola rete di gestione o verso le VLAN necessarie. La documentazione ufficiale distingue chiaramente il routing Layer 3 dalle policy di accesso: pubblicizzare una subnet non equivale ad autorizzare ogni porta. Le regole del tailnet e quelle OPNsense devono entrambe limitare le destinazioni.

Il nodo Tailscale non va collocato sul NAS se il NAS viene spento o acceso a orario. Non si configura un exit node come effetto collaterale: per amministrare il lab serve un subnet router, mentre l'exit node instrada anche il traffico Internet del client remoto.

## Perimetro minimo

La prima policy deve consentire soltanto:

| Origine remota | Destinazione | Porte |
|---|---|---|
| dispositivo personale autorizzato | gestione OPNsense, switch e AP | HTTPS/SSH strettamente necessari |
| dispositivo personale autorizzato | host e servizi del lab | solo porte documentate |
| altri dispositivi del tailnet | nessuna rete domestica | negato |

Le VLAN ospiti e IoT non vengono pubblicizzate. Se serve raggiungere più VLAN, il nodo Tailscale deve annunciare le reti una alla volta e OPNsense deve consentire il traffico dalla subnet Tailscale soltanto verso gli indirizzi necessari. Si preferisce il source NAT predefinito di Tailscale nella prima prova; disabilitarlo richiede rotte di ritorno esplicite e un collaudo più complesso.

## Sequenza di collaudo

1. Installare Tailscale su un host sempre acceso e autenticare il nodo con un account dedicato.
2. Pubblicizzare soltanto la subnet di gestione, dopo aver verificato che non si sovrapponga a reti usate dal client remoto.
3. Approvare la rotta nella console amministrativa Tailscale e applicare grants/ACL con una sola destinazione di test.
4. Creare su OPNsense una regola dalla rete del nodo verso il solo servizio di test; negare il resto e controllare i log.
5. Provare da rete mobile o altra rete esterna, quindi revocare il dispositivo e verificare che l'accesso scompaia.

## WireGuard diretto su OPNsense

WireGuard su OPNsense resta l'alternativa più controllabile per il progetto definitivo: il firewall possiede chiavi, peer, routing e policy in un unico punto. Con il Seven a monte occorre inoltrare dal Seven la porta UDP scelta verso la WAN privata di OPNsense e verificare che il firewall non blocchi reti private sulla WAN. Il test richiede quindi una regola sul Seven e una sulla WAN OPNsense, oltre alla configurazione dei peer.

La decisione non è “Tailscale sicuro o WireGuard sicuro”. Tailscale riduce il lavoro sul NAT e accelera il primo accesso, ma aggiunge un piano di controllo e un host sempre acceso. WireGuard diretto riduce le dipendenze esterne e rende il firewall il punto di enforcement, ma richiede port forwarding, gestione delle chiavi e un collaudo IPv4/IPv6 più esplicito.

## Tailcat: collegamenti occasionali fra due macchine

Richiesta dell'utente del 07/10/2026: potersi collegare in modo sicuro fra una macchina di casa e una esterna con [Tailcat](https://github.com/tailscale/tailcat), presentato da [IlSoftware](https://www.ilsoftware.it/focus/tailcat-collega-due-pc-ovunque-senza-vpn-account-porte-aperte/). Tailcat è uno strumento di Tailscale, con licenza BSD a tre clausole, che il README descrive come netcat sul piano dati di Tailscale senza il piano di controllo: usa WireGuard per cifrare, `magicsock` per attraversare il NAT e i relay DERP pubblici di Tailscale come punto d'incontro e come ripiego. Non servono account, tailnet, privilegi di amministratore né porte aperte sul Seven, perché entrambi i lati si collegano in uscita. Funziona quindi anche attraverso il doppio NAT, come spiegato nel [documento dedicato](07-doppio-nat-dietro-modem-in-comodato.md).

Il modello d'uso è diverso da quello delle due soluzioni sopra. Un lato lancia `tailcat` o `tailcat serve` e stampa un indirizzo; l'altro vi si collega con `tailcat <indirizzo>`. Si possono scambiare testo e file, esporre porte locali con `serve`, condividere una cartella, aprire una shell con `tailcat ssh` e inoltrare porte con `forward`, oltre a un proxy `socks`. Le chiavi sono effimere per impostazione predefinita e spariscono alla chiusura; quelle salvate con `genkey` restano valide finché non si cancellano. È uno strumento per sessioni puntuali fra due macchine, non un accesso permanente alla rete.

Tre caratteristiche ne decidono l'uso sicuro, e tutte e tre vengono dal README. L'indirizzo stampato è una credenziale al portatore: chi lo conosce si collega, quindi si passa solo per un canale fidato e non si pubblica mai. La modalità `no-auth-ssh` dà una shell a chiunque abbia l'indirizzo e in questa casa non si usa; per la shell si usa `serve ssh` con `--ssh-authorized-keys`, e per gli altri servizi si restringono i client con `--allow`. Infine il progetto non promette stabilità né di interfaccia né di protocollo, e i relay pubblici non hanno garanzie di disponibilità: va trattato come uno strumento sperimentale.

C'è poi una conseguenza di rete che riguarda il firewall. Tailcat attraversa il perimetro in uscita, quindi OPNsense non vede un servizio esposto ma solo connessioni UDP e HTTPS verso i relay. Chi si collega a una macchina di casa raggiunge ciò che quella macchina raggiunge, e con `forward` o `socks` può arrivare anche ad altri host della sua VLAN o di quelle che le regole le aprono. La collocazione proposta è quindi questa: Tailcat si esegue solo su macchine della VLAN 10 o della VLAN di gestione, mai su IoT, ospiti o laboratorio, e le regole di uscita di OPNsense per quelle tre VLAN non devono consentirlo. Per un accesso stabile alla gestione della rete resta WireGuard su OPNsense; Tailcat è l'aggiunta per i collegamenti occasionali che non meritano un inoltro sul Seven. Nessuna prova è stata eseguita: le affermazioni vengono dal README e dall'articolo, fonti S55 e S56.

## Fonti e limiti

La documentazione ufficiale Tailscale su [subnet router e quickstart](https://tailscale.com/kb/1017/install/), [CLI](https://tailscale.com/kb/1080/cli), [exit node](https://tailscale.com/kb/1103/exit-nodes/) e [policy](https://tailscale.com/docs/reference/syntax/policy-file) è la base del confronto. Le pagine descrivono il comportamento del prodotto, non la configurazione specifica di questa casa. Nessuna VPN è stata installata o collaudata in questa sessione.
