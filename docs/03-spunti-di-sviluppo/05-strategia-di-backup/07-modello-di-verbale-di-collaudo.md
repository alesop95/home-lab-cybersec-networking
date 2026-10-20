# Modello di verbale di collaudo dei backup

Modello vuoto collegato a [Permessi, finestre e collaudo](05-permessi-finestre-e-collaudo.md). Copiarlo nel livello privato per le prove reali; pubblicare soltanto un resoconto anonimizzato dopo avere verificato dati identificanti e segreti. La compilazione del modello non è una prova eseguita e nessun campo vuoto equivale a un esito positivo.

## Identificazione e perimetro

| Campo | Valore da compilare |
|---|---|
| stato | NON ESEGUITO |
| riferimento della procedura | scegliere PVE-01/02, HOST-01, NAS-01/02/03, RETE-01/02, file restic, Windows Veeam o il futuro scenario PBS se adottato |
| data, ora e fuso | inizio e termine effettivi con offset |
| versione | sistema, programma di backup, formato del repository o archivio |
| sorgente logica | segnaposto del dispositivo e oggetto da proteggere |
| originale | posizione privata e come viene protetto dalle scritture della prova |
| destinazione backup | macchina, supporto, dataset o repository, capacità e quota |
| destinazione restore | spazio distinto, vuoto o predisposto, con capacità verificata |
| punti selezionati | ID esatto, data e perimetro di ciascuno |
| inclusioni ed esclusioni | dischi, mount, cartelle, metadati e dipendenze esterne |
| consistenza | arresto, export applicativo o snapshot/agent effettivamente verificato |
| accesso e sblocco | nomi logici delle credenziali e luogo privato di custodia, senza valori |
| rete di prova | isolamento e metodo usato per verificarlo prima dell'avvio |

## Atteso prima della prova

Si scrive quale dato, versione, impronta e comportamento del servizio debbano essere recuperati. Per dati artificiali si descrivono A e B e il passaggio che li rende diversi. Si dichiara quale difetto dovrebbe far fallire la prova: assenza del bind mount, versione sbagliata, identità non autorizzata, NAS irraggiungibile o altra condizione pertinente. Un generico «funziona» non consente di discriminare questi casi.

## Evidenza ottenuta

| Controllo | Atteso | Osservato | Esito e riferimento privato |
|---|---|---|---|
| backup | punto nuovo completo del perimetro scelto | da compilare | NON ESEGUITO |
| spazio | picco entro budget, margine e quota | byte misurati e momento della lettura | NON ESEGUITO |
| accesso | credenziale corretta ammessa, altra identità respinta | da compilare | NON ESEGUITO |
| selezione | archivio/ID e versione richiesti | da compilare | NON ESEGUITO |
| contenuto | impronta e file previsti | da compilare | NON ESEGUITO |
| metadati | permessi e attributi dichiarati necessari | da compilare | NON ESEGUITO |
| applicazione | richiesta funzionale con risultato atteso | da compilare o non pertinente con motivo | NON ESEGUITO |
| indipendenza | lettura della copia con l'originale indisponibile | metodo e dipendenze effettive | NON ESEGUITO |
| tempo | durata completa, incluse preparazione e attese | tempi parziali e totale | NON ESEGUITO |
| pulizia | rimossi soltanto artefatti di prova identificati | da compilare | NON ESEGUITO |

Si conservano log originali, codici di uscita, avvisi, impronte, elenco del perimetro e mappatura privata dei dispositivi. Un codice zero riguarda il perimetro dichiarato dallo strumento; si verificano separatamente sorgenti assenti o escluse. Non si inseriscono password nei log o nel verbale. I log grezzi possono rivelare account, percorsi e indirizzi e restano privati.

## Esito e limiti

La conclusione sceglie un esito fra riuscito per il perimetro provato, fallito, parziale e non eseguito. Si elencano i contenuti ancora senza copia, i passaggi non provati e le dipendenze che non erano disponibili. Ogni difetto apre una pendenza con il prossimo controllo concreto. Si aggiorna l'ultimo punto completo soltanto dopo aver verificato il giro; l'ultimo recupero collaudato rimane un campo distinto.

Una prova con una piccola cartella artificiale qualifica quel percorso di prova, non il volume reale. Una prova file non chiude il recupero di sistema e una VM accesa non chiude la consistenza applicativa. Si rivede il verbale dopo cambi di versione, layout, permessi o cifratura, secondo il piano di collaudo.
