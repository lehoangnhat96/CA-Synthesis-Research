$categories = @(
    '01_Tien_xu_ly_Nguyen_lieu',
    '02_Doping_va_Gel_hoa',
    '03_Say_va_Nung_Nhiet_phan',
    '04_Cam_bien_Dien_hoa_Sinh_hoc',
    '05_Cross_Linker_va_Tao_mang',
    '06_Setup_Do_Dien_hoa',
    '07_Giao_trinh_Ly_thuyet',
    '08_Review_va_Tong_quan',
    '09_Tai_lieu_Quy_trinh_AI'
)
$src = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials"
$dst = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\2 Ref lib"

Write-Host ("=" * 75)
Write-Host ("{0,-45} {1,8} {2,8} {3,8}" -f "Danh muc", "Src", "Dst", "Status")
Write-Host ("=" * 75)

$totalSrc = 0
$totalDst = 0

foreach ($cat in $categories) {
    $srcPath = Join-Path $src $cat
    $dstPath = Join-Path $dst $cat

    $srcCount = 0
    $dstCount = 0

    if (Test-Path $srcPath) {
        $srcCount = (Get-ChildItem -Path $srcPath -Recurse -File).Count
    }
    if (Test-Path $dstPath) {
        $dstCount = (Get-ChildItem -Path $dstPath -Recurse -File).Count
    }

    $status = if ($srcCount -eq $dstCount) { "OK" } else { "MISSING!" }
    $totalSrc += $srcCount
    $totalDst += $dstCount

    Write-Host ("{0,-45} {1,8} {2,8} {3,8}" -f $cat, $srcCount, $dstCount, $status)
}

Write-Host ("=" * 75)
Write-Host ("{0,-45} {1,8} {2,8}" -f "TONG CONG", $totalSrc, $totalDst)
Write-Host ""

# Check uncategorized files in root of 1 Ref materials
Write-Host "--- File chua phan loai trong root 1 Ref materials ---"
$rootFiles = Get-ChildItem -Path $src -File
if ($rootFiles.Count -eq 0) {
    Write-Host "  (khong co file nao o root)"
} else {
    foreach ($f in $rootFiles) {
        $dstFile = Join-Path $dst $f.Name
        $status = if (Test-Path $dstFile) { "OK" } else { "CHUA COPY" }
        Write-Host ("  [{0}] {1}" -f $status, $f.Name)
    }
}

Write-Host ""
Write-Host "--- Kiem tra file MD vs PDF (moi cap doi) ---"
foreach ($cat in $categories) {
    $dstPath = Join-Path $dst $cat
    if (-not (Test-Path $dstPath)) { continue }
    
    $pdfs = Get-ChildItem -Path $dstPath -File -Filter "*.pdf" | Select-Object -ExpandProperty BaseName
    $mds  = Get-ChildItem -Path $dstPath -File -Filter "*.md"  | Select-Object -ExpandProperty BaseName
    
    $missingMD  = $pdfs | Where-Object { $mds -notcontains $_ }
    $missingPDF = $mds  | Where-Object { $pdfs -notcontains $_ }
    
    if ($missingMD.Count -gt 0 -or $missingPDF.Count -gt 0) {
        Write-Host "  [$cat]"
        foreach ($m in $missingMD)  { Write-Host "    THIEU MD : $m" }
        foreach ($m in $missingPDF) { Write-Host "    THIEU PDF: $m" }
    }
}
Write-Host ""
Write-Host "Kiem tra hoan tat."
