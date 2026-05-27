$folder = "D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials"
$files = Get-ChildItem -Path $folder -File -Filter "*.md"
$allFiles = @($files)
foreach ($f in $allFiles) {
    Write-Host "==== FILE: $($f.Name) ===="
    $content = Get-Content -Path $f.FullName -TotalCount 30
    $content | Out-String | Write-Host
    Write-Host ""
}
