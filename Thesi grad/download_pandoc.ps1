Continue = 'Stop'

 = "https://github.com/jgm/pandoc/releases/download/3.1.11.1/pandoc-3.1.11.1-windows-x86_64.zip"
 = "pandoc.zip"
 = "pandoc_extract"

Write-Host "Downloading Pandoc..."
 = New-Object System.Net.WebClient
.DownloadFile(, )

Write-Host "Extracting Pandoc..."
if (Test-Path ) { Remove-Item -Recurse -Force  }
Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory(, )
