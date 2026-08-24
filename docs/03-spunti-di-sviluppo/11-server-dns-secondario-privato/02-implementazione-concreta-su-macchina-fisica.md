# Implementazione concreta su macchina fisica

Basta un sistema operativo minimale come Debian stable o Rocky Linux minimal addirittura paradossalmente con niente desktop, niente servizi extra.

Si può installare Unbound dai repository ufficiali e Unbound gira come servizio non privilegiato. La configurazione è dichiarativa e auditabile.

Unbound opera in modalità recursive resolver, non forwarder con DNSSEC che è attivo e obbligatorio.

Cache in RAM, opzionalmente slab per performance multicore e access control settata a solo subnet LAN autorizzata.
