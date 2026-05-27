$src2 = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials\02_Doping_va_Gel_hoa"
$dst2 = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\2 Ref lib\02_Doping_va_Gel_hoa"

$srcPath1 = Join-Path $src2 "Bio-Based Aerogels for the Removal of Heavy Metal Ions and_images"
$dstPath1 = Join-Path $dst2 "Bio-Based Aerogels for the Removal of Heavy Metal Ions and_images"
$srcPath2 = Join-Path $src2 "CAN NHAC PdDoped Cellulose Carbon Aerogels for Energy Storage Applications_images"
$dstPath2 = Join-Path $dst2 "CAN NHAC PdDoped Cellulose Carbon Aerogels for Energy Storage Applications_images"

if (Test-Path $srcPath1) {
    Copy-Item -Path $srcPath1 -Destination $dstPath1 -Recurse -Force
    Write-Host "Copied: Bio-Based Aerogels_images"
} else { Write-Host "NOT FOUND: Bio-Based Aerogels_images" }

if (Test-Path $srcPath2) {
    Copy-Item -Path $srcPath2 -Destination $dstPath2 -Recurse -Force
    Write-Host "Copied: CAN NHAC PdDoped_images"
} else { Write-Host "NOT FOUND: CAN NHAC PdDoped_images" }

Write-Host "Done."
