# Introduzione

La separazione tra rete principale e guest avviene “a monte” sul modem/router (nel momento in cui non c’è un firewall opzionale aggiuntivo per cui conviene metterlo in bridge), non dipende dal tipo di connessione del dispositivo; quindi, main e guest è indipendente se mi conetto in ethernet o wi-fi con i dispositivi.

Se ti connetti via Ethernet a una porta del modem configurata per la rete principale, sei sulla rete principale. Se il modem ha porte dedicate alla guest (alcuni modelli sì, altri no) o se il firewall interno assegna comunque la guest a qualsiasi porta, quel traffico resta isolato.

Anche se ti connetti via Wi-Fi, la rete guest rimane isolata dalla principale grazie alla sottorete separata e alle regole del firewall interno. In pratica, l’isolamento non è solo “logico” sul Wi-Fi: è reale a livello di sottorete IP e firewall, quindi gli ospiti non possono mai raggiungere i tuoi dispositivi principali, sia che siano cablati sia che siano wireless.
