$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open("D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\DCLV_CA_02.07 Fe-N CA_Renumbered.docx")
$wdReplaceAll = 2
$wdFindContinue = 1

function Replace-Text {
    param([string]$FindText, [string]$ReplaceWith)
    $find = $doc.Content.Find
    $find.ClearFormatting()
    $find.Replacement.ClearFormatting()
    $find.Text = $FindText
    $find.Replacement.Text = $ReplaceWith
    $find.Forward = $true
    $find.Wrap = $wdFindContinue
    $find.Format = $false
    $find.MatchCase = $false
    $find.MatchWholeWord = $false
    $find.MatchWildcards = $false
    $find.MatchSoundsLike = $false
    $find.MatchAllWordForms = $false
    $find.Execute([ref][System.Type]::Missing, [ref][System.Type]::Missing, [ref][System.Type]::Missing, [ref][System.Type]::Missing, [ref][System.Type]::Missing, [ref][System.Type]::Missing, [ref][System.Type]::Missing, [ref][System.Type]::Missing, [ref][System.Type]::Missing, [ref]$ReplaceWith, [ref]$wdReplaceAll) | Out-Null
}

Replace-Text "Thuyết Kén phân tử (Inclusion Complex Theory) được mô tả bởi Cai & Zhang [6] cho cơ chế hòa tan cellulose trong hệ NaOH/Urea. Cơ chế này được giả định tương tự cho hệ dung môi amoniac/urea/nước được sử dụng trong đề tài [22, 23], trong đó hòa tan cellulose hòa tan cellulose theo cơ chế phối trí đa thành phần ở nhiệt độ lạnh." "Thuyết Kén phân tử (Inclusion Complex Theory) được xây dựng bởi nhóm GS. Lina Zhang: cơ chế hòa tan được mô tả qua hành vi gel hóa đặc biệt của cellulose trong hệ kiềm/urea {{6}}, trong đó Urea đóng vai trò tạo lớp vỏ bảo vệ quanh chuỗi cellulose thông qua tương tác van der Waals và liên kết hydro — điều được xác nhận trực tiếp bằng kỹ thuật NMR bởi Xiong và cộng sự {{52}}. Cơ chế này được giả định tương tự cho hệ dung môi amoniac/urea/nước được sử dụng trong đề tài {{17, 41}}, trong đó cellulose hòa tan theo cơ chế phối trí đa thành phần ở nhiệt độ lạnh."
Replace-Text "Quá trình hòa tan là phản ứng tỏa nhiệt (ΔH < 0) và giảm entropy (ΔS < 0), do đó sol chỉ ổn định và đồng nhất ở nhiệt độ ≤ 10°C (tối ưu 0 - 5°C)." "Quá trình hòa tan là phản ứng tỏa nhiệt (ΔH < 0) và giảm entropy (ΔS < 0) — được Cai và Zhang xác nhận bằng phân tích nhiệt lượng quét vi sai (DSC) {{53}} — do đó sol chỉ ổn định và đồng nhất ở nhiệt độ ≤ 10°C (tối ưu 0 - 5°C)."
Replace-Text '[22, 21, 27, 29]' '{{17, 49, 19, 20}}'
Replace-Text '[23, 6, 24, 25]' '{{43, 6, 18, 50}}'
Replace-Text '[23, 24, 32]' '{{43, 18, 22}}'
Replace-Text '[22, 23, 24]' '{{17, 43, 18}}'
Replace-Text '[29, 48, 49]' '{{20, 35, 36}}'
Replace-Text '[22, 29, 48]' '{{17, 20, 35}}'
Replace-Text '[38, 36, 37]' '{{27, 52, 26}}'
Replace-Text '[14, 26, 65]' '{{12, 51, 65}}'
Replace-Text '[9, 19, 20]' '{{47, 15, 16}}'
Replace-Text '[6, 7, 8]' '{{6, 7, 9}}'
Replace-Text '[6, 7, 9]' '{{6, 7, 47}}'
Replace-Text '[22, 23]' '{{17, 43}}'
Replace-Text '[23, 38]' '{{43, 27}}'
Replace-Text '[10, 11]' '{{10, 11}}'
Replace-Text '[12, 13]' '{{48, 44}}'
Replace-Text '[15, 16]' '{{8, 41}}'
Replace-Text '[17, 18]' '{{13, 14}}'
Replace-Text '[23, 24]' '{{43, 18}}'
Replace-Text '[16, 27]' '{{41, 19}}'
Replace-Text '[15, 28]' '{{8, 45}}'
Replace-Text '[17, 21]' '{{13, 49}}'
Replace-Text '[27, 29]' '{{19, 20}}'
Replace-Text '[22, 21]' '{{17, 49}}'
Replace-Text '[15, 17]' '{{8, 13}}'
Replace-Text '[23, 32]' '{{43, 22}}'
Replace-Text '[12, 25]' '{{48, 50}}'
Replace-Text '[36, 37]' '{{52, 26}}'
Replace-Text '[21, 29]' '{{49, 20}}'
Replace-Text '[38, 10]' '{{27, 10}}'
Replace-Text '[23, 12]' '{{43, 48}}'
Replace-Text '[49, 50]' '{{36, 37}}'
Replace-Text '[51, 52]' '{{55, 38}}'
Replace-Text '[22, 49]' '{{17, 36}}'
Replace-Text '[55, 56]' '{{40, 57}}'
Replace-Text '[17, 51]' '{{13, 55}}'
Replace-Text '[18, 51]' '{{14, 55}}'
Replace-Text '[18, 49]' '{{14, 36}}'
Replace-Text '[10, 12]' '{{10, 48}}'
Replace-Text '[57, 58]' '{{58, 59}}'
Replace-Text '[23, 25]' '{{43, 50}}'
Replace-Text '[38, 12]' '{{27, 48}}'
Replace-Text '[63, 64]' '{{64, 42}}'
Replace-Text '[58, 64]' '{{59, 42}}'
Replace-Text '[66, 67]' '{{66, 67}}'
Replace-Text '[8, 16]' '{{9, 41}}'
Replace-Text '[7, 29]' '{{7, 20}}'
Replace-Text '[6, 49]' '{{6, 36}}'
Replace-Text '[6, 21]' '{{6, 49}}'
Replace-Text '[2, 61]' '{{2, 62}}'
Replace-Text '[1, 2]' '{{1, 2}}'
Replace-Text '[15]' '{{8}}'
Replace-Text '[10]' '{{10}}'
Replace-Text '[11]' '{{11}}'
Replace-Text '[14]' '{{12}}'
Replace-Text '[17]' '{{13}}'
Replace-Text '[18]' '{{14}}'
Replace-Text '[19]' '{{15}}'
Replace-Text '[20]' '{{16}}'
Replace-Text '[22]' '{{17}}'
Replace-Text '[24]' '{{18}}'
Replace-Text '[27]' '{{19}}'
Replace-Text '[29]' '{{20}}'
Replace-Text '[30]' '{{21}}'
Replace-Text '[32]' '{{22}}'
Replace-Text '[33]' '{{23}}'
Replace-Text '[34]' '{{24}}'
Replace-Text '[35]' '{{25}}'
Replace-Text '[37]' '{{26}}'
Replace-Text '[38]' '{{27}}'
Replace-Text '[39]' '{{28}}'
Replace-Text '[41]' '{{29}}'
Replace-Text '[42]' '{{30}}'
Replace-Text '[43]' '{{31}}'
Replace-Text '[44]' '{{32}}'
Replace-Text '[45]' '{{33}}'
Replace-Text '[47]' '{{34}}'
Replace-Text '[48]' '{{35}}'
Replace-Text '[49]' '{{36}}'
Replace-Text '[50]' '{{37}}'
Replace-Text '[52]' '{{38}}'
Replace-Text '[53]' '{{39}}'
Replace-Text '[55]' '{{40}}'
Replace-Text '[64]' '{{42}}'
Replace-Text '[16]' '{{41}}'
Replace-Text '[13]' '{{44}}'
Replace-Text '[28]' '{{45}}'
Replace-Text '[31]' '{{46}}'
Replace-Text '[21]' '{{49}}'
Replace-Text '[25]' '{{50}}'
Replace-Text '[12]' '{{48}}'
Replace-Text '[26]' '{{51}}'
Replace-Text '[23]' '{{43}}'
Replace-Text '[40]' '{{53}}'
Replace-Text '[46]' '{{54}}'
Replace-Text '[36]' '{{52}}'
Replace-Text '[51]' '{{55}}'
Replace-Text '[54]' '{{56}}'
Replace-Text '[59]' '{{60}}'
Replace-Text '[60]' '{{61}}'
Replace-Text '[61]' '{{62}}'
Replace-Text '[62]' '{{63}}'
Replace-Text '[57]' '{{58}}'
Replace-Text '[1]' '{{1}}'
Replace-Text '[2]' '{{2}}'
Replace-Text '[3]' '{{3}}'
Replace-Text '[4]' '{{4}}'
Replace-Text '[5]' '{{5}}'
Replace-Text '[6]' '{{6}}'
Replace-Text '[7]' '{{7}}'
Replace-Text '[8]' '{{9}}'
Replace-Text '{{' '['
Replace-Text '}}' ']'

$doc.Save()
$doc.Close()
$word.Quit()
