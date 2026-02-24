# Сигнатура для поиска cheat dll
$sig = "net/minecraft/util/math/AxisAlignedBB"
$count = 0

Write-Host "`n[>] Начинаю поиск сигнатуры: $sig" -ForegroundColor Cyan

$files = Get-ChildItem "C:\" -Filter *.dll -Recurse -ErrorAction SilentlyContinue | 
         Where-Object { $_.FullName -notlike "C:\Windows\*" }

foreach ($f in $files) {
    try {
        if (Select-String -Path $f.FullName -Pattern $sig -Quiet) {
            Write-Host "[FOUND] $($f.FullName)" -ForegroundColor Green
            $count++
        }
    } catch { continue }
}

Write-Host "`n[!] Готово. Найдено совпадений: $count" -ForegroundColor Yellow
