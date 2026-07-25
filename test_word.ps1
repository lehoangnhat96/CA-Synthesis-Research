$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open("D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\DCLV_CA_02.07 Fe-N CA.docx")

$find = $doc.Content.Find
$find.ClearFormatting()
$find.Replacement.ClearFormatting()

# Find.Execute(FindText, MatchCase, MatchWholeWord, MatchWildcards, MatchSoundsLike, MatchAllWordForms, Forward, Wrap, Format, ReplaceWith, Replace)
$result = $find.Execute("Xiong", $false, $false, $false, $false, $false, $true, 1, $false, "Xiong_TEST", 2)

Write-Host "Replacement result: $result"
$doc.SaveAs("D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\DCLV_CA_02.07 Fe-N CA_Test.docx")
$doc.Close()
$word.Quit()
