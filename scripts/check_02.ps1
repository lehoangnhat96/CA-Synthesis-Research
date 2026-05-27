$src2 = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials\02_Doping_va_Gel_hoa"
$dst2 = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\2 Ref lib\02_Doping_va_Gel_hoa"

Write-Host "=== Missing image subfolders in 02 ==="
$srcDirs = Get-ChildItem -Path $src2 -Directory
$dstDirs = Get-ChildItem -Path $dst2 -Directory | Select-Object -ExpandProperty Name

foreach ($d in $srcDirs) {
    if ($dstDirs -notcontains $d.Name) {
        Write-Host "  MISSING DIR: $($d.Name)"
    } else {
        # Check files inside
        $srcImgs = (Get-ChildItem -Path $d.FullName -Recurse -File).Count
        $dstImgs = (Get-ChildItem -Path (Join-Path $dst2 $d.Name) -Recurse -File).Count
        if ($srcImgs -ne $dstImgs) {
            Write-Host "  PARTIAL: $($d.Name) | src=$srcImgs dst=$dstImgs"
        }
    }
}

Write-Host ""
Write-Host "=== Missing files (non-dir) in 02 ==="
$srcFiles = Get-ChildItem -Path $src2 -File
$dstFiles = Get-ChildItem -Path $dst2 -File | Select-Object -ExpandProperty Name

foreach ($f in $srcFiles) {
    if ($dstFiles -notcontains $f.Name) {
        Write-Host "  MISSING FILE: $($f.Name)"
    }
}
