$sourceBase = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials"
$destBase   = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\2 Ref lib"

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

Write-Host "=== SYNC MISSING FILES ===" 
Write-Host ""

foreach ($cat in $categories) {
    $srcCat = Join-Path $sourceBase $cat
    $dstCat = Join-Path $destBase $cat

    if (-not (Test-Path $srcCat)) {
        Write-Host "SKIP (src not found): $cat"
        continue
    }

    New-Item -ItemType Directory -Path $dstCat -Force | Out-Null

    # === Copy missing FILES ===
    $srcFiles = Get-ChildItem -Path $srcCat -File
    foreach ($f in $srcFiles) {
        $dstFile = Join-Path $dstCat $f.Name
        if (-not (Test-Path $dstFile)) {
            Copy-Item -Path $f.FullName -Destination $dstFile -Force
            Write-Host "  [NEW FILE] $cat / $($f.Name)"
        }
    }

    # === Copy missing DIRECTORIES (image folders) ===
    $srcDirs = Get-ChildItem -Path $srcCat -Directory
    foreach ($d in $srcDirs) {
        $dstDir = Join-Path $dstCat $d.Name
        if (-not (Test-Path $dstDir)) {
            # Folder does not exist at all - copy entire folder
            Copy-Item -Path $d.FullName -Destination $dstDir -Recurse -Force
            $imgCount = (Get-ChildItem -Path $d.FullName -File).Count
            Write-Host "  [NEW DIR] $cat / $($d.Name) ($imgCount images)"
        } else {
            # Folder exists - check for missing files inside
            $srcImgs = Get-ChildItem -Path $d.FullName -File
            foreach ($img in $srcImgs) {
                $dstImg = Join-Path $dstDir $img.Name
                if (-not (Test-Path $dstImg)) {
                    Copy-Item -Path $img.FullName -Destination $dstImg -Force
                    Write-Host "  [NEW IMG] $cat / $($d.Name) / $($img.Name)"
                }
            }
        }
    }
}

# === Copy uncategorized root files ===
Write-Host ""
Write-Host "=== COPY ROOT (uncategorized) FILES ==="
$rootFiles = Get-ChildItem -Path $sourceBase -File
foreach ($f in $rootFiles) {
    $dstFile = Join-Path $destBase $f.Name
    if (-not (Test-Path $dstFile)) {
        Copy-Item -Path $f.FullName -Destination $dstFile -Force
        Write-Host "  [ROOT FILE] $($f.Name)"
    }
}

# Copy root image folders (e.g. TOM_TAT_NTXPhuong_images)
$rootDirs = Get-ChildItem -Path $sourceBase -Directory | Where-Object { $_.Name -notmatch "^\d{2}_" -and $_.Name -ne ".obsidian" }
foreach ($d in $rootDirs) {
    $dstDir = Join-Path $destBase $d.Name
    if (-not (Test-Path $dstDir)) {
        Copy-Item -Path $d.FullName -Destination $dstDir -Recurse -Force
        Write-Host "  [ROOT DIR] $($d.Name)"
    }
}

Write-Host ""
Write-Host "=== DONE - All missing items copied. ==="
