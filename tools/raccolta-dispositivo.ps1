# Raccolta in sola lettura dei dati di rete e di sistema di un PC Windows, per la scheda
# dispositivo di ADR-021. Non modifica nulla: legge da CIM, dai cmdlet di rete e da netsh.
#
# Che cosa raccoglie: sistema operativo e build, produttore e modello, processore, memoria,
# schede di rete fisiche con velocita' negoziata e velocita' ammesse dal driver, driver Wi-Fi
# con standard radio e autenticazioni supportate, connessione Wi-Fi corrente.
# Che cosa NON raccoglie, per minimizzazione: numeri di serie, product ID, chiavi di licenza,
# utenti, programmi installati.
#
# L'uscita contiene dati reali (nome macchina, indirizzi MAC, SSID) e va SOLO in _notes/,
# ignorata da git. La scheda pubblica si ricava con tools/scheda-da-raccolta.py, che anonimizza.
#
# Uso, dalla radice del progetto o copiando lo script sul PC da censire:
#   powershell -NoProfile -ExecutionPolicy Bypass -File tools/raccolta-dispositivo.ps1 -Id PC-01
# Il file si chiama <Id>-<data>.json: l'Id e' quello documentale del censimento, non il nome macchina.

param(
    [Parameter(Mandatory = $true)][string]$Id,
    [string]$Uscita = "_notes\censimento\raccolte"
)

$ErrorActionPreference = "Continue"

function Leggi-Netsh([string[]]$argomenti) {
    # netsh stampa nella lingua del sistema: si conservano le righe grezze e si estraggono
    # le coppie chiave-valore senza tradurle, lasciando l'interpretazione allo script Python.
    $righe = & netsh @argomenti 2>$null
    if (-not $righe) { return @() }
    $coppie = @()
    foreach ($r in $righe) {
        if ($r -match '^\s*([^:]+?)\s*:\s*(.*)$') {
            $coppie += [ordered]@{ chiave = $Matches[1].Trim(); valore = $Matches[2].Trim() }
        }
    }
    return $coppie
}

$sistema = Get-CimInstance Win32_OperatingSystem
$macchina = Get-CimInstance Win32_ComputerSystem
$cpu = Get-CimInstance Win32_Processor | Select-Object -First 1
# Sui PC assemblati il modello di sistema e' un segnaposto del firmware ("System Product
# Name"): si legge anche la scheda madre, senza il suo numero di serie.
$scheda_madre = Get-CimInstance Win32_BaseBoard | Select-Object -First 1

$schede = @()
foreach ($a in (Get-NetAdapter -Physical -ErrorAction SilentlyContinue)) {
    $velocita = $null
    $prop = Get-NetAdapterAdvancedProperty -Name $a.Name -ErrorAction SilentlyContinue |
        Where-Object { $_.RegistryKeyword -eq "*SpeedDuplex" } | Select-Object -First 1
    if ($prop) { $velocita = @($prop.ValidDisplayValues) }
    $schede += [ordered]@{
        nome              = $a.Name
        descrizione       = $a.InterfaceDescription
        tipo_fisico       = $a.PhysicalMediaType
        stato             = [string]$a.Status
        velocita_negoziata = $a.LinkSpeed
        velocita_ammesse  = $velocita
        driver_fornitore  = $a.DriverProvider
        driver_versione   = $a.DriverVersion
        mac               = $a.MacAddress
    }
}

$dati = [ordered]@{
    formato          = "raccolta-dispositivo/1"
    id               = $Id
    raccolto_il      = (Get-Date).ToString("s")
    piattaforma      = "windows"
    nome_macchina    = $env:COMPUTERNAME
    sistema          = [ordered]@{
        nome     = $sistema.Caption
        versione = $sistema.Version
        build    = $sistema.BuildNumber
        architettura = $sistema.OSArchitecture
    }
    hardware         = [ordered]@{
        produttore  = $macchina.Manufacturer
        modello     = $macchina.Model
        scheda_madre = ("{0} {1}" -f $scheda_madre.Manufacturer, $scheda_madre.Product).Trim()
        processore  = $cpu.Name
        memoria_gb  = [math]::Round($macchina.TotalPhysicalMemory / 1GB, 1)
    }
    schede_di_rete   = $schede
    wifi_driver      = Leggi-Netsh @("wlan", "show", "drivers")
    wifi_connessione = Leggi-Netsh @("wlan", "show", "interfaces")
}

if (-not (Test-Path $Uscita)) { New-Item -ItemType Directory -Path $Uscita -Force | Out-Null }
$file = Join-Path $Uscita ("{0}-{1}.json" -f $Id, (Get-Date).ToString("yyyy-MM-dd"))
$dati | ConvertTo-Json -Depth 6 | Out-File -FilePath $file -Encoding utf8
Write-Output ("raccolta scritta in {0}: {1} schede di rete fisiche" -f $file, $schede.Count)
