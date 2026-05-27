Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead(".\2 Quy trình tổng hợp CŨ FULL.docx")
$entry = $zip.Entries | Where-Object { $_.FullName -eq 'word/document.xml' }
$stream = $entry.Open()
$reader = New-Object System.IO.StreamReader($stream)
$xml = $reader.ReadToEnd()
$reader.Close()
$zip.Dispose()
$xml = $xml -replace '<w:p[^>]*>', "`n"
$xml = $xml -replace '<[^>]+>', ''
$xml | Out-File -FilePath 'C:\Users\ADMIN\.gemini\antigravity\brain\1116fdc6-e633-4944-b6a0-c0decb651434\scratch\out1.txt' -Encoding UTF8

$zip2 = [System.IO.Compression.ZipFile]::OpenRead(".\2.1 Tổng hợp C.A 18.05.docx")
$entry2 = $zip2.Entries | Where-Object { $_.FullName -eq 'word/document.xml' }
$stream2 = $entry2.Open()
$reader2 = New-Object System.IO.StreamReader($stream2)
$xml2 = $reader2.ReadToEnd()
$reader2.Close()
$zip2.Dispose()
$xml2 = $xml2 -replace '<w:p[^>]*>', "`n"
$xml2 = $xml2 -replace '<[^>]+>', ''
$xml2 | Out-File -FilePath 'C:\Users\ADMIN\.gemini\antigravity\brain\1116fdc6-e633-4944-b6a0-c0decb651434\scratch\out2.txt' -Encoding UTF8
