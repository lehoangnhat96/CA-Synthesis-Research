$root = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials"

# ===== FILE 1: TOM_TAT_NTXPhuong -> 08_Review_va_Tong_quan =====
$dst1 = Join-Path $root "08_Review_va_Tong_quan"

# Move PDF
$src_pdf1 = Join-Path $root "TOM_TAT_NTXPhuong.pdf"
$dst_pdf1 = Join-Path $dst1 "TOM_TAT_NTXPhuong.pdf"
Move-Item -Path $src_pdf1 -Destination $dst_pdf1 -Force
Write-Host "[MOVED] TOM_TAT_NTXPhuong.pdf -> 08_Review_va_Tong_quan"

# Move MD
$src_md1 = Join-Path $root "TOM_TAT_NTXPhuong.md"
$dst_md1 = Join-Path $dst1 "TOM_TAT_NTXPhuong.md"
Move-Item -Path $src_md1 -Destination $dst_md1 -Force
Write-Host "[MOVED] TOM_TAT_NTXPhuong.md -> 08_Review_va_Tong_quan"

# Move images folder
$src_img1 = Join-Path $root "TOM_TAT_NTXPhuong_images"
$dst_img1 = Join-Path $dst1 "TOM_TAT_NTXPhuong_images"
if (Test-Path $src_img1) {
    Move-Item -Path $src_img1 -Destination $dst_img1 -Force
    Write-Host "[MOVED] TOM_TAT_NTXPhuong_images -> 08_Review_va_Tong_quan"
}

# ===== FILE 2: NGHIEN CUU CAM BIEN SINH HOC -> 04_Cam_bien_Dien_hoa_Sinh_hoc =====
$dst4 = Join-Path $root "04_Cam_bien_Dien_hoa_Sinh_hoc"

$camBienFiles = Get-ChildItem -Path $root -File | Where-Object { $_.Name -like "*NGHIEN*" -or $_.Name -like "*NGHI*CAM*" }
$camBienDirs  = Get-ChildItem -Path $root -Directory | Where-Object { $_.Name -like "*NGHIEN*" -or $_.Name -like "*CAM*BI*N*" }

foreach ($f in $camBienFiles) {
    $dstPath = Join-Path $dst4 $f.Name
    Move-Item -Path $f.FullName -Destination $dstPath -Force
    Write-Host "[MOVED] $($f.Name) -> 04_Cam_bien_Dien_hoa_Sinh_hoc"
}
foreach ($d in $camBienDirs) {
    $dstPath = Join-Path $dst4 $d.Name
    Move-Item -Path $d.FullName -Destination $dstPath -Force
    Write-Host "[MOVED DIR] $($d.Name) -> 04_Cam_bien_Dien_hoa_Sinh_hoc"
}

# ===== FILE 3: View of Investigate coir fibers -> 01_Tien_xu_ly_Nguyen_lieu =====
$dst01 = Join-Path $root "01_Tien_xu_ly_Nguyen_lieu"

$coirFiles = Get-ChildItem -Path $root -File | Where-Object { $_.Name -like "*Investigate*" -or $_.Name -like "*coir*" }
$coirDirs  = Get-ChildItem -Path $root -Directory | Where-Object { $_.Name -like "*Investigate*" -or $_.Name -like "*coir*" }

foreach ($f in $coirFiles) {
    $dstPath = Join-Path $dst01 $f.Name
    Move-Item -Path $f.FullName -Destination $dstPath -Force
    Write-Host "[MOVED] $($f.Name) -> 01_Tien_xu_ly_Nguyen_lieu"
}
foreach ($d in $coirDirs) {
    $dstPath = Join-Path $dst01 $d.Name
    Move-Item -Path $d.FullName -Destination $dstPath -Force
    Write-Host "[MOVED DIR] $($d.Name) -> 01_Tien_xu_ly_Nguyen_lieu"
}

Write-Host ""
Write-Host "=== Kiem tra root sau khi phan loai ==="
$remaining = Get-ChildItem -Path $root -File
if ($remaining.Count -eq 0) {
    Write-Host "Root sach - khong con file nao chua phan loai."
} else {
    Write-Host "Con $($remaining.Count) file chua phan loai:"
    foreach ($r in $remaining) { Write-Host "  - $($r.Name)" }
}
