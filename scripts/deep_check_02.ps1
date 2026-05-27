$src2 = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials\02_Doping_va_Gel_hoa"
$dst2 = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\2 Ref lib\02_Doping_va_Gel_hoa"

Write-Host "=== So sanh tung subfolder trong 02 ==="

$srcDirs = Get-ChildItem -Path $src2 -Directory
$dstDirMap = @{}
$dstDirList = Get-ChildItem -Path $dst2 -Directory
foreach ($d in $dstDirList) { $dstDirMap[$d.Name] = $d.FullName }

foreach ($d in $srcDirs) {
    if (-not $dstDirMap.ContainsKey($d.Name)) {
        $cnt = (Get-ChildItem -Path $d.FullName -Recurse -File).Count
        Write-Host "  MISSING DIR ($cnt files): $($d.Name)"
    } else {
        $srcCnt = (Get-ChildItem -Path $d.FullName -Recurse -File).Count
        $dstCnt = (Get-ChildItem -Path $dstDirMap[$d.Name] -Recurse -File).Count
        if ($srcCnt -ne $dstCnt) {
            Write-Host "  PARTIAL ($srcCnt vs $dstCnt): $($d.Name)"
        }
    }
}

Write-Host ""
Write-Host "Total src dirs: $($srcDirs.Count)"
Write-Host "Total dst dirs: $($dstDirList.Count)"
Write-Host ""
Write-Host "=== Src file count (top-level only) ==="
Write-Host "Files in src root: $((Get-ChildItem -Path $src2 -File).Count)"
Write-Host "Files in dst root: $((Get-ChildItem -Path $dst2 -File).Count)"
Write-Host ""
Write-Host "=== Src recursive total ==="
Write-Host "Src total: $((Get-ChildItem -Path $src2 -Recurse -File).Count)"
Write-Host "Dst total: $((Get-ChildItem -Path $dst2 -Recurse -File).Count)"
