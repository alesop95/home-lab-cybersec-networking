# Stack Linux domestico con soli strumenti open source

> Scheda di progettazione, non descrizione di uno stato di fatto. Nessuna delle componenti descritte qui è installata: la macchina che le ospiterà è il server della zona esposta previsto dalla topologia, e la zona esposta non esiste ancora perché il firewall non è configurato.

## Il vincolo che la scheda soddisfa

Una macchina Linux domestica che ospiti servizi propri deve reggersi su soli strumenti e librerie open source, senza componenti a licenza commerciale nemmeno nello strato di gestione. Non è una preferenza ideologica ma una conseguenza dei due scopi del progetto. Il primo è l'indipendenza da servizi di terzi, che è il tema di [Alternative privacy-oriented](../../alternative-privacy-oriented.md): sostituire un servizio in nuvola con uno self-hosted non ha senso se al suo posto si introduce una dipendenza da un fornitore diverso, con un contratto e una data di scadenza. Il secondo è l'ispezionabilità: in un progetto il cui oggetto è la sicurezza, un componente di cui non si può leggere il codice è una parte di perimetro che si accetta per fiducia, e su una macchina esposta verso Internet è esattamente la parte che non si vuole accettare per fiducia.

## L'impianto in cinque strati

L'architettura di riferimento è a cinque strati, ciascuno con una sola responsabilità, ed è la forma consolidata di un server applicativo domestico.

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

Il sistema operativo host è una distribuzione a supporto esteso, nell'impianto di riferimento Ubuntu Server nella sua edizione LTS, perché una macchina che resta accesa e raggiungibile senza qualcuno che la sorvegli ha bisogno di aggiornamenti di sicurezza garantiti per anni e non di funzionalità recenti. La versione che compare nel materiale di riferimento è la 24.04 LTS; se nel frattempo è uscita una LTS successiva la scelta va rifatta sulla più recente, ed è una verifica da compiere al momento dell'installazione invece di ereditarla da qui.

Sopra il sistema operativo sta Docker, che è il motore di esecuzione dei contenitori. La ragione per cui c'è non è la moda ma la pulizia del sistema ospite: ogni applicazione porta con sé le proprie dipendenze dentro la propria immagine, quindi due applicazioni che pretendono versioni incompatibili della stessa libreria convivono senza negoziare, e il sistema ospite resta una base sottile che si aggiorna senza rompere niente. La conseguenza che conta sul piano della sicurezza è che ogni servizio gira con un filesystem e uno spazio dei processi propri, quindi la compromissione di un'applicazione non è immediatamente la compromissione della macchina.

Portainer è la console web di gestione dei contenitori, e va capito per quello che è: non è un secondo strato di esecuzione sopra Docker, è un'interfaccia che parla allo stesso demone Docker al posto della riga di comando. Sostituisce la memoria dei comandi con un elenco visibile di ciò che gira, dei volumi, delle reti e dei registri, che è esattamente ciò che serve quando si rimette mano a una macchina dopo mesi. Va usata l'edizione Community, che è quella open source: Portainer esiste anche in un'edizione commerciale, e su questo punto la distinzione fra le due edizioni è la differenza fra rispettare il vincolo di apertura e crederlo rispettato.

I contenitori applicativi sono il livello che cambia nel tempo ed è il solo motivo per cui la macchina esiste. Sono tanti quanti sono i servizi ospitati, ciascuno indipendente dagli altri, e si aggiungono e si rimuovono senza toccare gli strati sotto.

NGINX sta davanti a tutto come proxy inverso e termina il TLS. È la decisione architetturale più importante dell'intero impianto, e conviene enunciarla per esteso: il client parla in HTTPS con NGINX e NGINX parla in HTTP con i contenitori su una rete interna, quindi la cifratura si configura, si rinnova e si controlla in un punto solo invece che in ognuno dei servizi ospitati. Accanto a NGINX vive un interprete PHP in modalità FPM, che serve le applicazioni PHP non contenitorizzate senza che il proxy debba eseguire codice applicativo.

I servizi dati stanno in fondo e sono condivisi. PostgreSQL e MariaDB convivono perché le applicazioni pretendono l'uno o l'altro e non si lasciano convincere, e MariaDB in particolare è la scelta coerente con il vincolo di apertura, essendo la derivazione di MySQL che ha conservato una licenza libera. Tenerli come servizi condivisi invece di infilare un motore dentro ogni contenitore applicativo concentra in un punto solo i salvataggi, i ripristini e gli aggiornamenti, che sono la parte del lavoro che si paga davvero nel tempo.

## Perché questo impianto si sposa con il doppio NAT di questa linea

Il punto di contatto con l'architettura di rete non è evidente a prima vista ed è la ragione principale per cui questa scheda esiste. La catena WAN di questo progetto impone una traduzione di indirizzo su due apparati in serie, il modem dell'operatore e poi il firewall, quindi ogni servizio che si voglia raggiungere da Internet richiede una regola di inoltro su entrambi. Pubblicare direttamente ogni contenitore significherebbe moltiplicare quelle regole per il numero dei servizi, cioè mantenere a mano due tabelle che divergono appena si aggiunge qualcosa.

Con il proxy inverso davanti, invece, attraversa i due apparati una porta sola, quella del traffico HTTPS, e la distinzione fra i servizi avviene dentro la macchina in base al nome richiesto. Le regole da mantenere restano due in tutto e non due per servizio, e ciò che è raggiungibile dall'esterno coincide con ciò che il proxy ha deciso di esporre invece che con ciò che qualcuno ha dimenticato di chiudere. La superficie d'attacco pubblicata smette di crescere con il numero delle applicazioni, ed è il genere di proprietà che si apprezza al terzo servizio, non al primo.

Resta il vincolo, già enunciato nella scheda del firewall, per cui la macchina che esegue questo stack non è e non diventa il firewall: OPNsense non ospita servizi che non siano di sicurezza, altrimenti smette di essere un punto deterministico. Lo stack descritto qui vive su una macchina distinta, collocata nella zona esposta prevista dalla topologia, dalla quale non esiste nessun percorso verso la LAN principale.

## Cosa resta da decidere

Quali applicazioni ospitare è materia di [Alternative privacy-oriented](../../alternative-privacy-oriented.md) e non di questa scheda, che descrive il telaio e non il contenuto. Restano aperte tre scelte che il diagramma di riferimento non copre: quale meccanismo rinnova i certificati sul proxy, dove e con quale frequenza si salvano i volumi dei due motori di dati, e se i contenitori debbano girare come utente non privilegiato, che è la differenza fra l'isolamento nominale dei contenitori e quello effettivo.
