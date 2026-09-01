#!/usr/bin/env bash
# Interroga Proxmox in sola lettura. Legge il token da D:\network-design\.env, non lo stampa mai.
ENVF="/d/network-design/.env"
BASE=$(grep -E '^PROXMOX_URL=' "$ENVF" | head -1 | cut -d= -f2- | tr -d '"'"'"' \r' | sed 's|/api2/json/*$||' | sed 's|/*$||')
TN=$(grep -E '^PROXMOX_TOKEN_NAME=' "$ENVF" | head -1 | cut -d= -f2- | tr -d '"'"'"' \r')
TV=$(grep -E '^PROXMOX_TOKEN_VALUE=' "$ENVF" | head -1 | cut -d= -f2- | tr -d '"'"'"' \r')
AUTH="Authorization: PVEAPIToken=${TN}=${TV}"
api() { curl -sk -m 30 -H "$AUTH" "${BASE}/api2/json$1"; }
export -f api 2>/dev/null
echo "base: $BASE"
echo "=== /version ==="; api /version | head -c 600; echo
echo "=== /nodes ==="; api /nodes | head -c 1200; echo
