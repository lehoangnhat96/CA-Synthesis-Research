$root = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials"
$dst4 = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials\04_Cam_bien_Dien_hoa_Sinh_hoc"

# Get remaining files in root (not inside any subfolder)
$rootFiles = Get-ChildItem -Path $root -File

Write-Host "Files con lai trong root:"
foreach ($f in $rootFiles) {
    Write-Host "  -> $($f.Name)"
    $dstFile = Join-Path $dst4 $f.Name
    Move-Item -Path $f.FullName -Destination $dstFile -Force
    Write-Host "     [MOVED] to 04_Cam_bien_Dien_hoa_Sinh_hoc"
}

# Also check for image folders
$rootDirs = Get-ChildItem -Path $root -Directory | Where-Object { $_.Name -notmatch "^0[0-9]_" -and $_.Name -ne ".obsidian" }
foreach ($d in $rootDirs) {
    Write-Host "  DIR: $($d.Name)"
    $dstDir = Join-Path $dst4 $d.Name
    Move-Item -Path $d.FullName -Destination $dstDir -Force
    Write-Host "     [MOVED DIR] to 04_Cam_bien_Dien_hoa_Sinh_hoc"
}

Write-Host ""
Write-Host "=== Final check ==="
$remaining = Get-ChildItem -Path $root -File
Write-Host "Files con lai: $($remaining.Count)"
