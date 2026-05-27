$sourceBase = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials"
$destBase = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\2 Ref lib"

$categories = @(
    "01_Tien_xu_ly_Nguyen_lieu",
    "02_Doping_va_Gel_hoa",
    "03_Say_va_Nung_Nhiet_phan",
    "04_Cam_bien_Dien_hoa_Sinh_hoc",
    "05_Cross_Linker_va_Tao_mang",
    "06_Setup_Do_Dien_hoa",
    "07_Giao_trinh_Ly_thuyet",
    "08_Review_va_Tong_quan",
    "09_Tai_lieu_Quy_trinh_AI"
)

foreach ($cat in $categories) {
    $srcCat = Join-Path $sourceBase $cat
    $dstCat = Join-Path $destBase $cat

    if (-not (Test-Path $srcCat)) {
        Write-Host "SKIP (not found): $cat"
        continue
    }

    New-Item -ItemType Directory -Path $dstCat -Force | Out-Null

    # Copy all files (PDF, MD, etc.)
    $files = Get-ChildItem -Path $srcCat -File
    foreach ($f in $files) {
        $dst = Join-Path $dstCat $f.Name
        Copy-Item -Path $f.FullName -Destination $dst -Force
        Write-Host "  [FILE] $($f.Name)"
    }

    # Copy image subdirectories
    $dirs = Get-ChildItem -Path $srcCat -Directory
    foreach ($d in $dirs) {
        $dstDir = Join-Path $dstCat $d.Name
        Copy-Item -Path $d.FullName -Destination $dstDir -Recurse -Force
        Write-Host "  [DIR]  $($d.Name)"
    }

    Write-Host "=== Processed: $cat ==="
}

Write-Host ""
Write-Host "ALL DONE - Sync complete."
