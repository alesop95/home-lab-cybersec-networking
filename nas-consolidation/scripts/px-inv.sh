#!/usr/bin/env bash
ENVF="/d/network-design/.env"
BASE=$(grep -E '^PROXMOX_URL=' "$ENVF" | head -1 | cut -d= -f2- | tr -d '"'"'"' \r' | sed 's|/api2/json/*$||' | sed 's|/*$||')
TN=$(grep -E '^PROXMOX_TOKEN_NAME=' "$ENVF" | head -1 | cut -d= -f2- | tr -d '"'"'"' \r')
TV=$(grep -E '^PROXMOX_TOKEN_VALUE=' "$ENVF" | head -1 | cut -d= -f2- | tr -d '"'"'"' \r')
AUTH="Authorization: PVEAPIToken=${TN}=${TV}"
api() { curl -sk -m 30 -H "$AUTH" "${BASE}/api2/json$1"; }

echo "=== PERMESSI DEL TOKEN ==="
api /access/permissions | python -c "
import json,sys
d=json.load(sys.stdin).get('data',{})
if not d: print('  nessun permesso restituito')
for path,rights in sorted(d.items()):
    on=[k for k,v in rights.items() if v]
    print(f'  {path}: {\", \".join(sorted(on)) if on else \"(nessuno)\"}')
" 2>/dev/null || api /access/permissions

echo
echo "=== STORAGE ==="
api /nodes/pve/storage | python -c "
import json,sys
for s in json.load(sys.stdin)['data']:
    if s.get('active'):
        print(f\"  {s['storage']:<16} {s.get('type',''):<10} cont={s.get('content','')[:40]:<40} tot={s.get('total',0)/2**30:8.1f}GB liberi={s.get('avail',0)/2**30:8.1f}GB\")
" 2>/dev/null

echo
echo "=== BRIDGE ==="
api /nodes/pve/network | python -c "
import json,sys
for n in json.load(sys.stdin)['data']:
    if n.get('type')=='bridge':
        print(f\"  {n['iface']:<12} cidr={n.get('cidr','-'):<20} ports={n.get('bridge_ports','-'):<20} active={n.get('active','')} {n.get('comments','').strip()}\")
" 2>/dev/null

echo
echo "=== VM ESISTENTI ==="
api /nodes/pve/qemu | python -c "
import json,sys
vms=json.load(sys.stdin)['data']
for v in sorted(vms,key=lambda x:int(x['vmid'])):
    print(f\"  {v['vmid']:<6} {v.get('name','')[:34]:<34} {v.get('status',''):<9} RAM={v.get('maxmem',0)/2**30:6.1f}GB disco={v.get('maxdisk',0)/2**30:7.1f}GB\")
used={int(v['vmid']) for v in vms}
free=[i for i in range(100,400) if i not in used][:6]
print('  VMID liberi:', free)
" 2>/dev/null

echo
echo "=== LXC ==="
api /nodes/pve/lxc | python -c "
import json,sys
for c in sorted(json.load(sys.stdin)['data'],key=lambda x:int(x['vmid'])):
    print(f\"  {c['vmid']:<6} {c.get('name','')[:34]:<34} {c.get('status','')}\")
" 2>/dev/null

echo
echo "=== ISO PRESENTI ==="
for s in local; do
  api "/nodes/pve/storage/$s/content?content=iso" | python -c "
import json,sys
d=json.load(sys.stdin).get('data') or []
for i in d: print(f\"  {i['volid']:<60} {i.get('size',0)/2**30:6.2f}GB\")
" 2>/dev/null
done
