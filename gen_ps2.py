import re
import sys

file_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered_restored.md"

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(?m)^# TÀI LIỆU THAM KHẢO', text)
body = parts[0]

old_to_new = {}
next_new_id = 1
pattern2 = r'(?:\\?\[)([0-9,\s\-]+)(?:\\?\])'

for m in re.finditer(pattern2, body):
    inner = m.group(1).replace(' ', '')
    for p in inner.split(','):
        if '-' in p:
            start_s, end_s = p.split('-')
            for num in range(int(start_s), int(end_s) + 1):
                if num not in old_to_new:
                    old_to_new[num] = next_new_id
                    next_new_id += 1
        else:
            num = int(p)
            if num not in old_to_new:
                old_to_new[num] = next_new_id
                next_new_id += 1

replacements = {}
for m in re.finditer(pattern2, body):
    full_match_clean = "[" + m.group(1) + "]"
    inner = m.group(1).replace(' ', '')
    
    new_parts = []
    for p in inner.split(','):
        if '-' in p:
            start_s, end_s = p.split('-')
            start, end = int(start_s), int(end_s)
            new_nums = []
            for num in range(start, end + 1):
                new_nums.append(old_to_new[num])
            if len(new_nums) > 2 and new_nums == list(range(new_nums[0], new_nums[-1] + 1)):
                new_parts.append(f"{new_nums[0]}-{new_nums[-1]}")
            else:
                new_parts.extend(map(str, new_nums))
        else:
            num = int(p)
            new_parts.append(str(old_to_new[num]))
            
    new_string = f"{{{{{', '.join(new_parts)}}}}}"
    if full_match_clean not in replacements:
        replacements[full_match_clean] = new_string

ps_script = """$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open("D:\\1 Master's Ana Chem\\1 Master's thesis\\Carbon Aerogel\\Thesi grad\\DCLV_CA_02.07 Fe-N CA_Renumbered.docx")
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

"""

ps_script += 'Replace-Text "Thuyết Kén phân tử (Inclusion Complex Theory) được mô tả bởi Cai & Zhang [6] cho cơ chế hòa tan cellulose trong hệ NaOH/Urea. Cơ chế này được giả định tương tự cho hệ dung môi amoniac/urea/nước được sử dụng trong đề tài [22, 23], trong đó hòa tan cellulose hòa tan cellulose theo cơ chế phối trí đa thành phần ở nhiệt độ lạnh." "Thuyết Kén phân tử (Inclusion Complex Theory) được xây dựng bởi nhóm GS. Lina Zhang: cơ chế hòa tan được mô tả qua hành vi gel hóa đặc biệt của cellulose trong hệ kiềm/urea {{6}}, trong đó Urea đóng vai trò tạo lớp vỏ bảo vệ quanh chuỗi cellulose thông qua tương tác van der Waals và liên kết hydro — điều được xác nhận trực tiếp bằng kỹ thuật NMR bởi Xiong và cộng sự {{52}}. Cơ chế này được giả định tương tự cho hệ dung môi amoniac/urea/nước được sử dụng trong đề tài {{17, 41}}, trong đó cellulose hòa tan theo cơ chế phối trí đa thành phần ở nhiệt độ lạnh."\n'

ps_script += 'Replace-Text "Quá trình hòa tan là phản ứng tỏa nhiệt (ΔH < 0) và giảm entropy (ΔS < 0), do đó sol chỉ ổn định và đồng nhất ở nhiệt độ ≤ 10°C (tối ưu 0 - 5°C)." "Quá trình hòa tan là phản ứng tỏa nhiệt (ΔH < 0) và giảm entropy (ΔS < 0) — được Cai và Zhang xác nhận bằng phân tích nhiệt lượng quét vi sai (DSC) {{53}} — do đó sol chỉ ổn định và đồng nhất ở nhiệt độ ≤ 10°C (tối ưu 0 - 5°C)."\n'

for old_s in sorted(replacements.keys(), key=len, reverse=True):
    new_s = replacements[old_s]
    ps_script += f"Replace-Text '{old_s}' '{new_s}'\n"

ps_script += "Replace-Text '{{' '['\n"
ps_script += "Replace-Text '}}' ']'\n"

ps_script += """
$doc.Save()
$doc.Close()
$word.Quit()
"""

with open('run_word.ps1', 'w', encoding='utf-8-sig') as f:
    f.write(ps_script)

print("PowerShell script generated with utf-8-sig!")
