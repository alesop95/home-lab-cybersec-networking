# Stack Linux domestico con soli strumenti open source

> Scheda di progettazione, non descrizione di uno stato di fatto. Nessuna delle componenti descritte qui e' installata: la macchina che le ospitera' e' il server della zona esposta previsto dalla topologia, e la zona esposta non esiste ancora perche' il firewall non e' configurato.

## Il vincolo che la scheda soddisfa

Una macchina Linux domestica che ospiti servizi propri deve reggersi su soli strumenti e librerie open source, senza componenti a licenza commerciale nemmeno nello strato di gestione. Non e' una preferenza ideologica ma una conseguenza dei due scopi del progetto. Il primo e' l'indipendenza da servizi di terzi, che e' il tema di [Alternative privacy-oriented](../../alternative-privacy-oriented.md): sostituire un servizio in nuvola con uno self-hosted non ha senso se al suo posto si introduce una dipendenza da un fornitore diverso, con un contratto e una data di scadenza. Il secondo e' l'ispezionabilita': in un progetto il cui oggetto e' la sicurezza, un componente di cui non si puo' leggere il codice e' una parte di perimetro che si accetta per fiducia, e su una macchina esposta verso Internet e' esattamente la parte che non si vuole accettare per fiducia.

## L'impianto in cinque strati

L'architettura di riferimento e' a cinque strati, ciascuno con una sola responsabilita', ed e' la forma consolidata di un server applicativo domestico.

```
                    [ client ]
                        |
                      HTTPS
                        |
  +---------------------|-------------------------------------+
  |  UBUNTU SERVER LTS  |           sistema operativo host     |
  |                     v                                      |
  |   [ NGINX ]  reverse proxy, termina TLS     [ PHP-FPM ]    |
  |       |  unica porta pubblicata all'esterno       ^        |
  |       |  HTTP interno verso i container           |        |
  |       v                                           v        |
  |  +--------------------------------------------------+      |
  |  |  DOCKER           [ PORTAINER ] console web       |      |
  |  |                                                   |      |
  |  |  [ APP 1 ]  [ APP 2 ]  [ APP 3 ]  [ APP 4 ]  ...  |      |
  |  +--------------------------------------------------+      |
  |          |            |             |                      |
  |          v            v             v                      |
  |     [ PostgreSQL ]              [ MariaDB ]                 |
  |      servizi dati condivisi fra piu' applicazioni           |
  +------------------------------------------------------------+
```

Il sistema operativo host e' una distribuzione a supporto esteso, nell'impianto di riferimento Ubuntu Server nella sua edizione LTS, perche' una macchina che resta accesa e raggiungibile senza qualcuno che la sorvegli ha bisogno di aggiornamenti di sicurezza garantiti per anni e non di funzionalita' recenti. La versione che compare nel materiale di riferimento e' la 24.04 LTS; se nel frattempo e' uscita una LTS successiva la scelta va rifatta sulla piu' recente, ed e' una verifica da compiere al momento dell'installazione invece di ereditarla da qui.

Sopra il sistema operativo sta Docker, che e' il motore di esecuzione dei contenitori. La ragione per cui c'e' non e' la moda ma la pulizia del sistema ospite: ogni applicazione porta con se' le proprie dipendenze dentro la propria immagine, quindi due applicazioni che pretendono versioni incompatibili della stessa libreria convivono senza negoziare, e il sistema ospite resta una base sottile che si aggiorna senza rompere niente. La conseguenza che conta sul piano della sicurezza e' che ogni servizio gira con un filesystem e uno spazio dei processi propri, quindi la compromissione di un'applicazione non e' immediatamente la compromissione della macchina.

Portainer e' la console web di gestione dei contenitori, e va capito per quello che e': non e' un secondo strato di esecuzione sopra Docker, e' un'interfaccia che parla allo stesso demone Docker al posto della riga di comando. Sostituisce la memoria dei comandi con un elenco visibile di cio' che gira, dei volumi, delle reti e dei registri, che e' esattamente cio' che serve quando si rimette mano a una macchina dopo mesi. Va usata l'edizione Community, che e' quella open source: Portainer esiste anche in un'edizione commerciale, e su questo punto la distinzione fra le due edizioni e' la differenza fra rispettare il vincolo di apertura e crederlo rispettato.

I contenitori applicativi sono il livello che cambia nel tempo ed e' il solo motivo per cui la macchina esiste. Sono tanti quanti sono i servizi ospitati, ciascuno indipendente dagli altri, e si aggiungono e si rimuovono senza toccare gli strati sotto.

NGINX sta davanti a tutto come proxy inverso e termina il TLS. E' la decisione architetturale piu' importante dell'intero impianto, e conviene enunciarla per esteso: il client parla in HTTPS con NGINX e NGINX parla in HTTP con i contenitori su una rete interna, quindi la cifratura si configura, si rinnova e si controlla in un punto solo invece che in ognuno dei servizi ospitati. Accanto a NGINX vive un interprete PHP in modalita' FPM, che serve le applicazioni PHP non contenitorizzate senza che il proxy debba eseguire codice applicativo.

I servizi dati stanno in fondo e sono condivisi. PostgreSQL e MariaDB convivono perche' le applicazioni pretendono l'uno o l'altro e non si lasciano convincere, e MariaDB in particolare e' la scelta coerente con il vincolo di apertura, essendo la derivazione di MySQL che ha conservato una licenza libera. Tenerli come servizi condivisi invece di infilare un motore dentro ogni contenitore applicativo concentra in un punto solo i salvataggi, i ripristini e gli aggiornamenti, che sono la parte del lavoro che si paga davvero nel tempo.

## Perche' questo impianto si sposa con il doppio NAT di questa linea

Il punto di contatto con l'architettura di rete non e' evidente a prima vista ed e' la ragione principale per cui questa scheda esiste. La catena WAN di questo progetto impone una traduzione di indirizzo su due apparati in serie, il modem dell'operatore e poi il firewall, quindi ogni servizio che si voglia raggiungere da Internet richiede una regola di inoltro su entrambi. Pubblicare direttamente ogni contenitore significherebbe moltiplicare quelle regole per il numero dei servizi, cioe' mantenere a mano due tabelle che divergono appena si aggiunge qualcosa.

Con il proxy inverso davanti, invece, attraversa i due apparati una porta sola, quella del traffico HTTPS, e la distinzione fra i servizi avviene dentro la macchina in base al nome richiesto. Le regole da mantenere restano due in tutto e non due per servizio, e cio' che e' raggiungibile dall'esterno coincide con cio' che il proxy ha deciso di esporre invece che con cio' che qualcuno ha dimenticato di chiudere. La superficie d'attacco pubblicata smette di crescere con il numero delle applicazioni, ed e' il genere di proprieta' che si apprezza al terzo servizio, non al primo.

Resta il vincolo, gia' enunciato nella scheda del firewall, per cui la macchina che esegue questo stack non e' e non diventa il firewall: OPNsense non ospita servizi che non siano di sicurezza, altrimenti smette di essere un punto deterministico. Lo stack descritto qui vive su una macchina distinta, collocata nella zona esposta prevista dalla topologia, dalla quale non esiste nessun percorso verso la LAN principale.

## Cosa resta da decidere

Quali applicazioni ospitare e' materia di [Alternative privacy-oriented](../../alternative-privacy-oriented.md) e non di questa scheda, che descrive il telaio e non il contenuto. Restano aperte tre scelte che il diagramma di riferimento non copre: quale meccanismo rinnova i certificati sul proxy, dove e con quale frequenza si salvano i volumi dei due motori di dati, e se i contenitori debbano girare come utente non privilegiato, che e' la differenza fra l'isolamento nominale dei contenitori e quello effettivo.
