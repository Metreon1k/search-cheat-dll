# Конфигурация
$targetSignature = "net/minecraft/util/math/AxisAlignedBB"
$extensions = @(".dll", ".exe", ".jar")
$excludePath = "C:\Windows"
$searchRoot = "C:\"

Clear-Host

Write-Host ("=" * 60) -ForegroundColor Blue
Write-Host "      SCANN-CHEAT SYSTEM v1.0 | Powered by Metreon1k"
Write-Host ("=" * 60) -ForegroundColor Blue
Write-Host "[*] Target Signature: " -NoNewline; Write-Host $targetSignature -ForegroundColor Yellow
Write-Host "[*] Search Path:      " -NoNewline; Write-Host $searchRoot -ForegroundColor Yellow
Write-Host "[*] Status:           " -NoNewline; Write-Host "Scanning files..." -ForegroundColor Green
Write-Host ""

$foundList = @()
$filesScanned = 0
$startTime = Get-Date


try {
    $files = Get-ChildItem -Path $searchRoot -Include *.dll, *.exe, *.jar -Recurse -ErrorAction SilentlyContinue | 
             Where-Object { $_.FullName -notlike "$excludePath*" }

    foreach ($file in $files) {
        $filesScanned++
        
        if ($filesScanned % 100 -eq 0) {
            Write-Host ("`r[>] Scanned: $filesScanned files...") -NoNewline
        }

        try {
            if (Select-String -Path $file.FullName -Pattern $targetSignature -Quiet) {
                Write-Host ("`r[FOUND] " + $file.FullName) -ForegroundColor Green
                $foundList += $file.FullName
            }
        }
        catch {
            continue
        }
    }
}
catch [System.Management.Automation.BreakException] {
    Write-Host "`n[!] Scanning aborted by user" -ForegroundColor Red
}

$endTime = Get-Date
$duration = [Math]::Round(($endTime - $startTime).TotalSeconds, 2)

Write-Host "`n"
Write-Host ("=" * 60) -ForegroundColor Blue
Write-Host "SCAN COMPLETED in $duration s"
if ($foundList.Count -gt 0) {
    Write-Host "TOTAL MATCHES: " -NoNewline; Write-Host $foundList.Count -ForegroundColor Red
} else {
    Write-Host "TOTAL MATCHES: " -NoNewline; Write-Host "0" -ForegroundColor Green
}
Write-Host ("=" * 60) -ForegroundColor Blue
