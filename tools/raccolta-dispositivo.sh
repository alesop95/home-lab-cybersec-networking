#!/usr/bin/env bash
# Raccolta in sola lettura dei dati di rete e di sistema di un PC Linux, per la scheda
# dispositivo di ADR-021. Equivalente di raccolta-dispositivo.ps1. Non modifica nulla e non
# richiede root: legge /etc/os-release, /sys/class/dmi/id, /proc, `ip`, e se presenti
# `ethtool` e `iw`. Senza root `ethtool` puo' non riportare tutto: lo si dichiara nell'uscita.
#
# Non raccoglie numeri di serie ne' identificativi di prodotto. L'uscita contiene dati reali
# (nome macchina, MAC) e va SOLO in _notes/, ignorata da git.
#
# Uso:  bash tools/raccolta-dispositivo.sh PC-02 [cartella-di-uscita]

set -u
ID="${1:?serve un Id documentale, per esempio PC-02}"
USCITA="${2:-_notes/censimento/raccolte}"
mkdir -p "$USCITA"
FILE="$USCITA/$ID-$(date +%F).json"

leggi() { [ -r "$1" ] && tr -d '\n' < "$1" || true; }
js() { python3 -c 'import json,sys; print(json.dumps(sys.stdin.read().rstrip("\n")))'; }

{
  echo "{"
  echo "\"formato\": \"raccolta-dispositivo/1\","
  echo "\"id\": $(printf '%s' "$ID" | js),"
  echo "\"raccolto_il\": $(date +%FT%T | js),"
  echo "\"piattaforma\": \"linux\","
  echo "\"nome_macchina\": $(hostname | js),"
  echo "\"os_release\": $(cat /etc/os-release 2>/dev/null | js),"
  echo "\"kernel\": $(uname -r | js),"
  echo "\"hardware\": {"
  echo "  \"produttore\": $(leggi /sys/class/dmi/id/sys_vendor | js),"
  echo "  \"modello\": $(leggi /sys/class/dmi/id/product_name | js),"
  echo "  \"scheda_madre\": $(echo "$(leggi /sys/class/dmi/id/board_vendor) $(leggi /sys/class/dmi/id/board_name)" | js),"
  echo "  \"processore\": $(grep -m1 'model name' /proc/cpuinfo | cut -d: -f2- | js),"
  echo "  \"memoria_kb\": $(grep -m1 MemTotal /proc/meminfo | awk '{print $2}' | js)"
  echo "},"
  echo "\"ip_link\": $(ip -j link 2>/dev/null | js),"
  echo "\"ethtool\": {"
  primo=1
  for dev in $(ls /sys/class/net); do
    [ "$dev" = "lo" ] && continue
    [ $primo -eq 0 ] && echo ","
    primo=0
    if command -v ethtool >/dev/null 2>&1; then
      echo "  $(printf '%s' "$dev" | js): $(ethtool "$dev" 2>&1 | js)"
    else
      echo "  $(printf '%s' "$dev" | js): \"ethtool non installato\""
    fi
  done
  echo "},"
  if command -v iw >/dev/null 2>&1; then
    echo "\"iw_list\": $(iw list 2>&1 | js),"
    echo "\"iw_dev\": $(iw dev 2>&1 | js)"
  else
    echo "\"iw_list\": \"iw non installato\","
    echo "\"iw_dev\": \"iw non installato\""
  fi
  echo "}"
} > "$FILE"

python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$FILE" && echo "raccolta scritta in $FILE"
