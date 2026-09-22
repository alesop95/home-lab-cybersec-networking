# Studio d'acquisto: switch gestito a otto porte e due o tre AP Zyxel

Ritorno allo [quadro generale](README.md). Valutazione del 22/09/2026, basata sulle fonti S09-S26 e S47-S48 del [registro](../../../SOURCES.md). La scelta e' condizionata da budget, punti Ethernet e misure radio non ancora disponibili; i prezzi riportati sono indicazioni da pagine indicizzate, non un carrello confermato.

## Raccomandazione

Per mantenere l'obiettivo 2,5 GbE e alimentare due o tre AP, il candidato principale e' XMG1915-10EP. Il suffisso conta: `10E` non ha PoE, `10EP` lo ha. Il numero dieci comprende otto porte rame e due SFP+, quindi soddisfa il requisito di otto porte RJ45. La precedente scelta 10E con un iniettore era riferita a un solo AP: il nuovo fabbisogno merita il confronto economico aggiornato.

Per l'home lab completo propongo due NWA130BE: il supporto 802.1X/RADIUS e SNMP consente gli esperimenti derivati da NovaSCM e il monitoraggio rete, mentre le tre radio evitano la scelta fra 5 e 6 GHz. Per contenere la spesa, due NWA50BE Pro sono coerenti con una casa segmentata a password personali; rinunciano a quei due requisiti del lab. E' anche possibile un NWA130BE nella zona di sperimentazione e un 50BE Pro per copertura: gli SSID enterprise saranno disponibili solo sugli AP che li supportano.

## Confronto switch

| Modello | Porte e potenza | Gestione / limite nel progetto | Esito |
|---|---|---|---|
| XMG1915-10EP | 8 x 2,5 GbE PoE++, 2 x SFP+ 10G; budget totale 130 W, fino a 60 W su singola porta | fanless, gestione locale e opzione Nebula; routing statico disponibile ma da non usare fra zone | candidato principale |
| XMG1915-10E | 8 x 2,5 GbE, 2 x SFP+ 10G; nessun PoE | fanless; richiede alimentatori locali o iniettori multigigabit | alternativa se cablaggio/alimentazione la rendono piu' economica |
| GS1915-8EP | 8 porte Gigabit; budget PoE 60 W | Gigabit riduce la banda utile rispetto al progetto; tre AP piu' esigenti eccedono il budget | compromesso solo se si accetta 1 GbE |
| XMG1915-18EP | 16 x 2,5 GbE, 2 x SFP+; 8 porte PoE, budget 180 W | ha raffreddamento attivo; supera il requisito di otto porte | rivalutare solo se il censimento esaurisce le porte |

Specifiche da [Zyxel XMG1915](https://www.zyxel.com/global/en/products/switch/xmg1915-series/specifications), [funzioni](https://www.zyxel.com/global/en/products/switch/xmg1915-series/features) e [GS1915](https://www.zyxel.com/global/en/products/switch/gs1915-series). Non tutte le porte del 18EP sono PoE. Due SFP+ non sono due RJ45 aggiuntive immediatamente utilizzabili: occorrono cavi/moduli e dispositivi compatibili. Non sono previsti moduli rame aggiuntivi nel costo base.

GS1200/GS1900 emersi nella ricerca non sono la prima scelta per questa rete multigigabit. Un prezzo inferiore non compensa automaticamente perdita di funzioni, velocita' o durata di supporto; non si afferma che tutta una famiglia sia fuori supporto sulla base di un risultato di ricerca relativo a un singolo modello.

## Confronto access point

| AP | Radio / uplink | Assorbimento PoE dichiarato | RADIUS e SNMP | Quando ha senso |
|---|---|---|---|---|
| NWA50BE Pro | Wi-Fi 7; 2,4 + 5 oppure 6 GHz; 1 x 2,5 GbE | 16 W, 802.3at | no autenticazione enterprise; no SNMP nella specifica | costo contenuto, VLAN e SSID personali |
| NWA130BE | Wi-Fi 7; 2,4 + 5 + 6 GHz simultanei; 2 x 2,5 GbE | 24 W, 802.3at | 802.1X/RADIUS e SNMP | candidato preferito per casa e laboratorio |
| NWA50AX Pro | Wi-Fi 6, 2,4 + 5 GHz; 1 x 2,5 GbE | 20,5 W, 802.3at | verificare requisiti sulla variante prima dell'ordine | solo se il prezzo e' nettamente favorevole |
| NWA90BE Pro | Wi-Fi 7 BandFlex, due radio | da ricontrollare per il preventivo selezionato | 802.1X/RADIUS; SNMP assente | alternativa se serve EAP-TLS senza tre bande simultanee |

Riferimenti diretti: [50BE Pro](https://www.zyxel.com/global/en/products/wireless/nwa50be-pro/specifications), [130BE](https://www.zyxel.com/global/en/products/wireless/nwa130be/specifications), [50AX Pro](https://www.zyxel.com/global/en/products/wireless/nwa50ax-pro/specifications), [90BE Pro](https://www.zyxel.com/global/en/products/wireless/nwa90be-pro/specifications). Il 50BE Pro non diventa compatibile con EAP-TLS installando un server RADIUS. Il secondo connettore del 130BE non viene assunto come uscita PoE o come raddoppio automatico della banda. Candidati outdoor e collegamenti punto-punto richiedono uno studio distinto se emerge un'area esterna.

## Dimensionamento PoE

| Configurazione | Somma degli assorbimenti dichiarati | Riserva prudenziale di progetto +25% | Rispetto a 130 W |
|---|---|---|---|
| 2 x NWA50BE Pro | 32 W | 40 W | ampio margine |
| 3 x NWA50BE Pro | 48 W | 60 W | ampio margine |
| 2 x NWA130BE | 48 W | 60 W | ampio margine |
| 3 x NWA130BE | 72 W | 90 W | 40 W rispetto alla riserva proposta |
| 3 x NWA50AX Pro | 61,5 W | 76,875 W | compatibile col budget totale |

Questi sono calcoli dai dati di targa, non consumi misurati. La riserva del 25% e' un criterio di progetto, non una prescrizione Zyxel, e non sostituisce verifica di perdite sui cavi e allocazione PoE per classe. Tre dispositivi PoE+ che riservano 30 W ciascuno impegnerebbero 90 W: rientrano comunque nei 130 W. Il 60 W del GS1915-8EP non garantisce tre 130BE e non va confrontato solo con l'idle. Altri dispositivi PoE, come telecamere, vanno aggiunti al conto prima dell'acquisto. Accensione simultanea e reset alimentazione per porta entrano nel collaudo.

## Otto porte sono abbastanza?

| Porta rame | Assegnazione proposta | Modalita' |
|---|---|---|
| 1 | uplink verso OPNsense | trunk con sole VLAN necessarie |
| 2 | AP 1 | trunk e PoE |
| 3 | AP 2 | trunk e PoE |
| 4 | AP 3 eventuale | riserva; trunk e PoE solo quando attivato |
| 5 | NAS | access VLAN 30; velocita' dettata dalla NIC effettiva |
| 6 | host servizi | access VLAN 30; trunk solo se ospita VM di zone distinte |
| 7 | workstation | access VLAN 10 |
| 8 | porta per recupero o altro client | access VLAN 99 durante manutenzione, da documentare |

Con tre AP, firewall, NAS, host e workstation sono gia' sette porte occupate. PS5, TV e ulteriori desktop cablati consumerebbero la riserva: otto porte bastano al nucleo, non necessariamente a tutta la casa. La [tabella dispositivi](../../05-analisi-del-caso/01-tbc-studio-dispositivi-domestici.md) deve produrre il conteggio delle connessioni simultanee. Un'espansione gestita su SFP+ e' possibile come progetto futuro, ma implica un secondo apparato e costo. Non si presume un NAS 10G non ancora previsto.

## Costi indicativi e alternativa senza PoE

Riferimenti letti il 22/09/2026: [10EP](https://www.idealo.it/confronta-prezzi/203921679/zyxel-xmg1915-10ep.html) 288,17 euro, [50BE Pro](https://www.idealo.it/confronta-prezzi/207723303/zyxel-nwa50be-pro.html) 102,70 euro, [130BE](https://www.idealo.it/confronta-prezzi/204014075/zyxel-nwa130be.html) 188,62 euro nella pagina aperta. Gli indici dei primi due hanno cache rispettivamente settimanale e mensile; la pagina 130BE era aggiornata dal crawler il giorno precedente. Per il 130BE il risultato di ricerca dava 169,14 euro: non e' il valore usato nel totale, perche' la pagina aperta mostrava un dato diverso.

| Scenario | Totale aritmetico apparati | Esclusioni |
|---|---|---|
| 10EP + 2 x 50BE Pro | 493,57 euro | trasporto, posa, cavi, eventuale UPS |
| 10EP + 3 x 50BE Pro | 596,27 euro | come sopra |
| 10EP + 2 x 130BE | 665,41 euro | come sopra |
| 10EP + 3 x 130BE | 854,03 euro | come sopra |
| 10EP + 130BE + 50BE Pro | 579,49 euro | copertura enterprise solo sull'AP compatibile |

Questi totali non sono preventivi e non attestano disponibilita', IVA o costo finale del venditore selezionato. Prima dell'ordine si controllano codice EU, garanzia, dotazione, IVA e spedizione al checkout.

Il [10E senza PoE](https://www.idealo.it/confronta-prezzi/203921684/zyxel-xmg1915-10e.html) compare a 195,22 euro nell'indice: differenza indicativa 92,95 euro dal 10EP. Con due AP la soglia e' 46,475 euro per alimentazione aggiuntiva per AP, con tre 30,983 euro, prima di prese, ingombri e cablaggio. Non e' il prezzo di un iniettore: e' il punto di pareggio calcolato. Se ogni AP ha gia' una presa e l'alimentatore adatto incluso, il 10E puo' costare meno; il PoE centralizzato facilita alimentazione e riavvio dalla sede dello switch. Un iniettore Gigabit puo' annullare il vantaggio dell'uplink a 2,5 GbE: serve compatibilita' sia dati sia PoE+ verificata sul modello esatto.

## Gestione gratuita, firmware e supporto

La gestione standalone soddisfa l'obiettivo di amministrazione locale senza controller a pagamento. [Nebula Base](https://www.zyxel.com/global/en/products/nebula-cloud-center/nebula-control-center/plans-and-pricing) e' l'opzione cloud senza licenza per il suo insieme di funzioni; non si considera una prova temporanea Pro come funzionalita' gratuita permanente. Si verifica sul piano vigente cio' che serve davvero, in particolare storico e aggiornamenti programmati. Non e' prevista l'adozione di Nebula come prerequisito del lab.

La ricerca ha individuato un [avviso Zyxel del 04/08/2026](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-command-injection-and-improper-authentication-vulnerabilities-in-certain-aps-fwa7-and-security-routers-08-04-2026) che comprende candidati della tabella. Per CVE-2026-8508 indica patch `7.40(ACPC.1)C0` per 50BE Pro, `7.40(ACIL.1)C0` per 130BE e `7.40(ACPE.1)C0` per 90BE Pro; per 50AX Pro indica `7.12(ACGE.0)C0` nelle tabelle delle due vulnerabilita'. Sono riferimenti di correzione per quell'avviso, non una dichiarazione che tali versioni saranno le piu' recenti al momento dell'installazione. Il collaudo deve registrare firmware corretto per modello e stato degli advisory aggiornati.

La [pagina EOL](https://www.zyxel.com/global/en/support/end-of-life) resta il controllo prima dell'acquisto. La ricerca non ha stabilito una data garantita di fine supporto dei candidati: assenza di un risultato non equivale a supporto perpetuo. Garanzia hardware e aggiornamenti di sicurezza sono cose diverse.

## Due o tre AP: criterio di copertura e collaudo

Si propone backhaul Ethernet per ogni AP, stesso insieme di SSID/VLAN dove applicabile e canali differenziati. Non serve chiamare mesh un insieme di AP cablati. Se i cavi non sono disponibili, vanno confrontati costo di posa, collocazione e modalita' wireless supportata prima di cambiare progetto. Con superfici e muri ignoti non si promette copertura in metri quadrati.

Nel sopralluogo si annotano stanza/piano con etichette anonime, ostacoli, quota di montaggio, prese e passaggi cavo. Si parte con due AP; il terzo si aggiunge solo per una zona scoperta misurata o carico reale. Obiettivi iniziali di progetto, non soglie universali: circa -67 dBm e SNR almeno 25 dB nelle zone di uso critico, verificati coi client effettivi, piu' prova di chiamata in movimento e trasferimento locale. Nella banda 2,4 GHz si parte da 20 MHz; sui 5 GHz si confrontano 40/80 MHz secondo interferenza, senza imporre massima larghezza. Il profilo paese deve essere Italia e i canali consentiti vanno gestiti dal firmware regionale.

La prova comprende ottenimento DHCP in ogni SSID, isolamento ospiti/IoT verso NAS e gestione, raggiungibilita' amministrativa, spegnimento/riavvio di un AP, riconnessione dopo interruzione PoE, roaming dei telefoni, client legacy e comportamento con MLO. Si registrano modello del client, firmware, luogo, banda, RSSI/SNR, throughput e data. Le [testimonianze di community](../../fonti/zyxel-e-community.md) motivano queste prove; non sostituiscono la misura nella casa.
