# Interroga Proxmox in sola lettura usando il token in D:\network-design\.env
# Non stampa mai il token.

$cfg = @{}
Get-Content 'D:\network-design\.env' | ForEach-Object {
  if ($_ -match '^\s*([A-Za-z0-9_]+)\s*=\s*(.+)$') {
    $cfg[$Matches[1]] = $Matches[2].Trim().Trim('"').Trim("'")
  }
}

$base = $cfg['PROXMOX_URL'] -replace '/api2/json[/]*$', ''
$base = $base -replace '[/]+$', ''
if ($base -notmatch '^https?://') { $base = 'https://' + $base }

$hdr = @{ Authorization = "PVEAPIToken=$($cfg['PROXMOX_TOKEN_NAME'])=$($cfg['PROXMOX_TOKEN_VALUE'])" }
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = { $true }
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12

function Api($p) {
  try { return (Invoke-RestMethod -Uri ($base + '/api2/json' + $p) -Headers $hdr -TimeoutSec 25).data }
  catch { Write-Output ("  ERRORE " + $p + " -> " + $_.Exception.Message); return $null }
}

Write-Output "base URL: $base"

Write-Output "`n=== VERSIONE ==="
$v = Api '/version'
if ($v) { "Proxmox VE $($v.version)  release $($v.release)" }

Write-Output "`n=== NODI ==="
$nodes = Api '/nodes'
if ($nodes) {
  $nodes | Select-Object node, status, maxcpu,
    @{N='RAM_usata_GB';E={[math]::Round($_.mem/1GB,1)}},
    @{N='RAM_tot_GB';E={[math]::Round($_.maxmem/1GB,1)}} | Format-Table -AutoSize | Out-String
}

foreach ($n in $nodes) {
  $nd = $n.node
  Write-Output "`n=== STORAGE sul nodo $nd ==="
  $st = Api "/nodes/$nd/storage"
  if ($st) {
    $st | Where-Object { $_.active -eq 1 } | Select-Object storage, type, content,
      @{N='Tot_GB';E={[math]::Round($_.total/1GB,1)}},
      @{N='Liberi_GB';E={[math]::Round($_.avail/1GB,1)}} | Format-Table -AutoSize | Out-String
  }

  Write-Output "=== BRIDGE DI RETE sul nodo $nd ==="
  $net = Api "/nodes/$nd/network"
  if ($net) {
    $net | Where-Object { $_.type -eq 'bridge' } | Select-Object iface, cidr, bridge_ports, active, comments |
      Format-Table -AutoSize | Out-String
  }

  Write-Output "=== VM ESISTENTI sul nodo $nd ==="
  $vms = Api "/nodes/$nd/qemu"
  if ($vms) {
    $vms | Sort-Object vmid | Select-Object vmid, name, status,
      @{N='RAM_GB';E={[math]::Round($_.maxmem/1GB,1)}},
      @{N='Disco_GB';E={[math]::Round($_.maxdisk/1GB,1)}} | Format-Table -AutoSize | Out-String
    $used = ($vms | ForEach-Object { [int]$_.vmid })
    Write-Output ("VMID occupati: " + ($used -join ', '))
    $free = @(); $c = 100
    while ($free.Count -lt 4 -and $c -lt 999) { if ($used -notcontains $c) { $free += $c }; $c++ }
    Write-Output ("Primi VMID liberi: " + ($free -join ', '))
  } else { Write-Output "nessuna VM o non leggibile" }

  Write-Output "=== CONTAINER LXC sul nodo $nd ==="
  $ct = Api "/nodes/$nd/lxc"
  if ($ct) { $ct | Sort-Object vmid | Select-Object vmid, name, status | Format-Table -AutoSize | Out-String }

  Write-Output "=== ISO GIA' PRESENTI sul nodo $nd ==="
  foreach ($s in ($st | Where-Object { $_.content -match 'iso' })) {
    $iso = Api "/nodes/$nd/storage/$($s.storage)/content?content=iso"
    if ($iso) {
      Write-Output "--- storage $($s.storage) ---"
      $iso | Select-Object volid, @{N='GB';E={[math]::Round($_.size/1GB,2)}} | Format-Table -AutoSize | Out-String
    }
  }
}

Write-Output "`n=== PERMESSI DEL TOKEN (per capire cosa posso fare) ==="
$perm = Api '/access/permissions'
if ($perm) { $perm | ConvertTo-Json -Depth 5 | Out-String }
