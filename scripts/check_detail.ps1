$src1 = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials\01_Tien_xu_ly_Nguyen_lieu"
$dst1 = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\2 Ref lib\01_Tien_xu_ly_Nguyen_lieu"
$src2 = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials\02_Doping_va_Gel_hoa"
$dst2 = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\2 Ref lib\02_Doping_va_Gel_hoa"

Write-Host "=== 01: Src image dirs ===" 
Get-ChildItem -Path $src1 -Directory | ForEach-Object { Write-Host "  SRC: $($_.Name)" }
Write-Host "=== 01: Dst image dirs ==="
Get-ChildItem -Path $dst1 -Directory | ForEach-Object { Write-Host "  DST: $($_.Name)" }

Write-Host ""
Write-Host "=== 01: Src file count recurse: $(  (Get-ChildItem -Path $src1 -Recurse -File).Count )"
Write-Host "=== 01: Dst file count recurse: $(  (Get-ChildItem -Path $dst1 -Recurse -File).Count )"

Write-Host ""
Write-Host "=== 02: Src dirs ==="
Get-ChildItem -Path $src2 -Directory | ForEach-Object { Write-Host "  SRC: $($_.Name)" }
Write-Host "=== 02: Dst dirs ==="
Get-ChildItem -Path $dst2 -Directory | ForEach-Object { Write-Host "  DST: $($_.Name)" }
Write-Host "=== 02: Src file count: $(  (Get-ChildItem -Path $src2 -Recurse -File).Count )"
Write-Host "=== 02: Dst file count: $(  (Get-ChildItem -Path $dst2 -Recurse -File).Count )"
