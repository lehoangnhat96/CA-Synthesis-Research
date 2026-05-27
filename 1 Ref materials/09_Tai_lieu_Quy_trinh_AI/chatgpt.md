## **Báo cáo thẩm định và định hướng phát triển carbon aerogel sinh khối cho màng điện cực điện hóa và biosensor** 

## **Executive summary** 

Tôi đọc tài liệu tải lên theo đúng hướng người dùng bổ sung: mọi kết quả phải quy về việc xây dựng **tài liệu nền** và **quy trình tổng hợp carbon aerogel từ sinh khối** để làm **màng điện cực** , phục vụ **phân tích điện hóa** hoặc **biosensor điện hóa** . Khi đối chiếu với nguồn DOI gốc, phần lõi mạnh nhất của tài liệu là trục công nghệ **xơ dừa → cellulose aerogel → carbon aerogel N-doped → điện cực điện hóa** . Trục này được hỗ trợ khá chắc bởi các bài gốc về cellulose aerogel từ xơ dừa, direct pyrolysis tạo N- doped carbon aerogel từ hệ ammonia–urea, và nghiên cứu điều khiển dạng N-doping theo nhiệt độ pyrolysis trong hệ coir/PEFB. Đồng thời, các review và bài gốc về biomass-derived carbon cho thấy cùng một “khung nền vật liệu” có thể đi sang các hướng **paracetamol** , **ion kim loại nặng** , **dopamine/uric acid** , **H₂O₂** , và xa hơn là **glucose/biosensor** . 1 

Điểm cần tách bạch là: tài liệu tải lên có một số nhận định đã đúng về mặt cơ chế tổng quát nhưng **chưa đủ mạnh để xem là dữ kiện đã xác lập cho biosensor** . Cụ thể, các mệnh đề như **“700 °C là tối ưu chung cho mọi ứng dụng sensing”** , **“Fe–Nₓ chắc chắn là active site tốt nhất cho paracetamol hoặc Pb²⁺/Zn²⁺”** , hay **“công thức NH₄OH:urea:H₂O và chuỗi Fe impregnation–acid leach–anneal hiện tại là tối ưu cho biosensor”** vẫn cần thí nghiệm xác nhận riêng. Lý do là dữ liệu DOI mạnh nhất hiện có chủ yếu xác nhận chúng trong bối cảnh **ORR / seawater battery / catalyst science** , còn chuyển sang **điện phân tích** hay **biosensor** thì cơ chế hấp phụ, pH, nền điện giải, mode đo, và selectivity thay đổi đáng kể. Việc định lượng và phân biệt **Fe hạt** , **Fe carbide** , và **Fe–Nₓ atomically dispersed** cũng không thể làm chỉ bằng XPS phần trăm nguyên tố; cần các phép đo chuyên sâu hơn như nitrite stripping, Mössbauer, hoặc kinetic probe methods. 2 

Về quyết định kỹ thuật, nếu mục tiêu cuối cùng là xây dựng một **platform biosensor điện hóa** từ N-CA/ Fe/N-CA xơ dừa, con đường có xác suất thành công cao nhất không phải là nhảy thẳng vào biosensor hoàn chỉnh, mà là đi theo chuỗi nhân quả sau: **làm chủ cellulose aerogel và N-CA trước** , dùng nó để tạo **màng điện cực lặp lại được** , kiểm tra **CV/EIS + một analyte hóa học dễ** như paracetamol để chuẩn hóa film formation, sau đó mới mở nhánh sang **Pb²⁺/Zn²⁺ bằng stripping voltammetry** hoặc **biosensor có lớp nhận biết sinh học** . Nói ngắn gọn: ưu tiên **N-CA làm baseline** , chỉ đưa **Fe** vào khi có dữ liệu chứng minh Fe thực sự làm tăng tốc độ truyền điện tử hoặc selectivity theo mục tiêu phân tích, thay vì chỉ tăng độ phức tạp tổng hợp. 3 

## **Bài toán và giả định** 

## **Bài toán** 

Bài toán thực chất không phải là “liệu xơ dừa có làm được carbon aerogel hay không”, vì điều đó đã có dữ liệu hỗ trợ. Bài toán đúng hơn là: **làm thế nào chuyển một quy trình carbon aerogel từ xơ dừa thành một platform màng điện cực có thể tái dùng cho nhiều bài toán điện hóa** , rồi từ đó chọn ra hướng nào đáng đầu tư cho biosensor. Quy trình phải đi từ tiền xử lý sinh khối, sol–gel/freeze-drying, 

1 

pyrolysis, kiểm soát dị nguyên tử và/hoặc Fe, đến công thức ink, cách phủ màng, phép đo điện hóa, và quy tắc hiệu chuẩn trong mẫu thực. Chuỗi nguyên nhân – hệ quả này phù hợp với những gì các review gần đây nhấn mạnh: giá trị thật của biomass-derived carbon nằm ở chỗ **cấu trúc xốp + dị nguyên tử + bề mặt chức năng hóa + khả năng làm điện cực** được thiết kế thống nhất như một platform, chứ không phải từng ứng dụng rời rạc. 4 

## **Các giả định tôi buộc phải dùng** 

Do tài liệu tải lên chưa cung cấp đủ mọi thông số thực nghiệm chi tiết kèm nguồn gốc DOI truy hồi được, dưới đây là **các giả định tối thiểu** tôi dùng để hoàn thành báo cáo. Tôi không thêm chi tiết ngoài mức cần thiết. 

|||Mức độ|
|---|---|---|
|Giả định dùng trong báo cáo|Vì sao cần giả định|chắc|
|||chắn|
|N-CA là**nitrogen-doped carbon aerogel**từ xơ|Tài liệu tải lên xoay quanh đúng||
|dừa; Fe/N-CA là phiên bản có Fe nhằm tạo tâm|cặp vật liệu này, nhưng chưa|Trung|
|hoạt tính kiểu Fe–N–C hoặc ít nhất là Fe-containing|chuẩn hóa định nghĩa cấu trúc Fe|bình|
|N-doped carbon|ở mức site chemistry||
||Phần lớn literature biomass-||
|Định dạng điện cực mục tiêu là**màng phủ trên**<br>**GCE/SPCE hoặc nền trơ tương đương**, không|carbon electroanalysis dùng<br>dạng modifer flm; literature|Cao<br>5|
|phải monolith tự chống hoàn toàn|binder-free aerogel có, nhưng ít||
||hơn cho biosensor thực dụng||
|“Biosensor” ở đây được hiểu là**điện cực**<br>**transducer dựa trên N-CA/Fe/N-CA**, có thể cần<br>thêm enzyme/aptamer/antibody hoặc catalyst phụ<br>tùy analyte|Nếu không chốt nghĩa này,<br>không thể đánh giá tương thích<br>với paracetamol hay ion sensing|Cao<br>6|
|“Tương thích %” là**độ tái sử dụng kỹ thuật**của|Điều này cho phép so sánh các||
|cùng platform vật liệu–điện cực–đo điện hóa,|hướng ứng dụng một cách định|Cao|
|không phải xác suất thành công thương mại|lượng và nhất quán||
|Một số thông số rất cụ thể nêu trong tài liệu tải|||
|lên, như**tỉ lệ NH₄OH:urea:H₂O**,**chuỗi Fe**<br>**impregnation–HCl–anneal**, hay**ưu tiên không**<br>**bleach để giữ reactive surface cho Fe**, hiện được<br>coi là**giả thuyết làm việc**, chưa xem là chuẩn tối|Tôi chưa tìm được đủ dữ liệu<br>primary accessible để xác nhận<br>độc lập ở đúng hệ coir biosensor|Thấp<br>đến<br>trung<br>bình|
|ưu đã xác lập|||




![](_images/chatgpt_images/_temp_9d4eb1fe_convert_.pdf-0002-04.png)


**----- Start of picture text -----**<br>
Paracetamol<br>Pb2+ và Zn2+<br>Xơ dừa Tiền xửlý cellulose Sol-gel và freeze-dry N-CA qua pyrolysis Fe/N-CA qua Fe loading vàxửlý sau Màng điện cực CV và EIS chuẩn hóa nền Dopamine và uric acid<br>H2O2<br>Glucose hoặc biosensor có<br>lớp nhận biết<br>**----- End of picture text -----**<br>


2 

Sơ đồ trên phản ánh đúng cấu trúc tái sử dụng mà literature về 3D biomass-derived carbon và biomassderived electrochemical sensors mô tả: **phần dùng chung nằm ở vật liệu và giao diện điện cực** , còn **phần tách nhánh nằm ở cơ chế phát hiện, điều kiện điện giải và hiệu chuẩn mẫu thực** . 7 

## **Xác thực dữ liệu và giả thiết chính** 

Cơ chế thẩm định tôi dùng là đi từ **tiền chất → cấu trúc aerogel → hóa học N/Fe → hành vi interface điện cực → mode đo điện hóa** . Nếu mắt xích nào thiếu bằng chứng gốc, tôi không nâng nó lên thành “sự thật nền”, chỉ giữ ở mức giả thuyết cần kiểm chứng. Cách làm này quan trọng vì cùng một carbon xốp có thể rất tốt cho ORR nhưng chưa chắc tối ưu cho paracetamol, và một vật liệu tốt cho DPV hữu cơ chưa chắc tốt cho SWASV kim loại nặng. 8 

## **Bảng xác thực** 

||||||Hàm ý trực tiếp|
|---|---|---|---|---|---|
|Mục chính trong tài<br>liệu|Kết luận xác<br>thực<br>Nguồn DOI ưu tiên và<br>chứng cứ chính|||Độ tin<br>cậy|cho quy trình<br>carbon aerogel<br>làm màng điện|
||||||cực|
||Fauziyah et al.,_Cellulose_|||||
|Xơ dừa có thể chuyển<br>thành**cellulose**<br>**aerogel**bằng route<br>alkali–urea|**Được xác**<br>**thực**<br>2019, DOI**10.1007/**<br>**s10570-019-02753-x**; coir<br>fbers cho cellulose<br>aerogels bằng sulfur-free<br>NaOH–urea, và tiền xử lý<br>ảnh hưởng mạnh đến tính|||Rất<br>cao|Đây là nền quy<br>trình bắt buộc<br>phải tái lập trước<br>khi bàn đến N-<br>CA/Fe/N-CA|
||chất aerogel.||9|||
||Fauziyah et al.,_Ind. Eng._|||||
||_Chem. Res._2020, DOI|||||
|Từ cellulose aerogel<br>xơ dừa có thể đi thẳng<br>sang**N-doped carbon**<br>**aerogel**bằng<br>pyrolysis|**Được xác**<br>**thực**<br>**10.1021/acs.iecr.0c03771**;<br>abstract xác nhận direct<br>pyrolysis của cellulose<br>aerogel từ coir dùng<br>ammonia–urea system tạo|||Rất<br>cao|Đây là bằng<br>chứng mạnh<br>nhất cho nhánh<br>N-CA từ xơ dừa|
||N-doped carbon aerogel.|||||
||10|||||
|Nhiệt độ pyrolysis<br>điều khiển dạng N-<br>doping;**600 °C**<br>**pyrrolic, 700 °C**<br>**pyridinic, 800 °C**<br>**graphitic**trong hệ<br>coir/PEFB|**Được xác**<br>**thực**<br>Susanto et al.,_ACS Omega_<br>2024, DOI**10.1021/**<br>**acsomega.3c09297**; bài<br>gốc nêu rõ sự chuyển ưu<br>thế pyrrolic→pyridinic→<br>graphitic khi tăng nhiệt độ.<br>11|||Rất<br>cao|700 °C là điểm<br>hợp lý để tối đa<br>hóa pyridinic-N<br>nếu mục tiêu là<br>tăng site hoạt<br>tính bề mặt|



3 

|||||||Hàm ý trực tiếp|
|---|---|---|---|---|---|---|
|Mục chính trong tài<br>liệu|Kết luận xác<br>thực<br>Nguồn DOI ưu tiên và<br>chứng cứ chính||||Độ tin<br>cậy|cho quy trình<br>carbon aerogel<br>làm màng điện|
|||||||cực|
|**Pyridinic-N**là dạng<br>có lợi nhất cho ORR<br>trong hệ coir/PEFB đã<br>khảo sát|**Được xác**<br>**thực**<br>**nhưng chỉ**<br>**trong ngữ**<br>**cảnh ORR**<br>Cùng DOI**10.1021/**<br>**acsomega.3c09297**; bài<br>báo kết luận pyridinic-N<br>cho hiệu năng ORR tốt hơn<br>pyrrolic và graphitic trong<br>seawater battery.<br>12||||Cao|Có thể dùng làm<br>lý do chọn nhiệt<br>độ, nhưng<br>**không được**<br>**suy rộng tự**<br>**động**sang mọi<br>analyte sensing|
||Cheng et al.,_J. Phys. Chem._||||||
||_C_2016, DOI**10.1021/**||||||
|Biomass-derived|**acs.jpcc.5b11280**; Jiao et||||||
|carbon aerogels/|al.,_Nanomaterials_2023,|||||Khẳng định việc|
|carbon materials có<br>thể dùng chung cho|**Được xác**<br>**thực**<br>DOI**10.3390/**<br>**nano13172397**; các review||||Cao|tái dụng<br>platform vật liệu|
|**supercapacitor, ORR/**|chỉ ra|aerogel carbon||sinh||là hợp lý|
|**OER, sensors**|khối được dùng rộng|||ở lưu|||
||trữ năng lượng và điện||||||
||hóa.|13|||||
||Mehmandoust et al.,_Ind._||||||
|Biomass-derived<br>carbon là nền tốt cho<br>**điện cực cảm biến**<br>**điện hóa**với thuốc,<br>thuốc nhuộm, ion kim<br>loại nặng|**Được xác**<br>**thực**<br>_Eng. Chem. Res._2022, DOI<br>**10.1021/acs.iecr.2c03058**;<br>Onfray & Thiam,<br>_Micromachines_2023, DOI<br>**10.3390/mi14091688**;<br>Wang et al.,_Anal. Chem._<br>2014, DOI**10.1021/**||||Rất<br>cao|Ủng hộ cách viết<br>tài liệu theo<br>hướng “một quy<br>trình vật liệu –<br>nhiều nhánh<br>phân tích điện<br>hóa”|
||**ac401563m**.<br>14||||||
|Hướng**paracetamol**<br>là nhánh ứng dụng<br>thật sự tương thích<br>với biomass-derived<br>carbon|**Được xác**<br>**thực**<br>Kim et al.,_Sens. Actuators B_<br>2018, DOI**10.1016/j.snb.**<br>**2017.12.066**; kelp-derived<br>carbon cho AP với DPV/CV,<br>LOD**0.004 μM**, linear range<br>**0.01–20 μM**theo dữ liệu<br>tổng hợp và trích dẫn thứ<br>cấp truy hồi được.<br>15||||Cao|Đây là bài thử<br>tốt để chuẩn hóa<br>ink, flm, Rct,<br>peak separation<br>và anti-fouling<br>trước khi sang<br>biosensor|



4 

|||||Hàm ý trực tiếp|
|---|---|---|---|---|
|Mục chính trong tài<br>liệu|Kết luận xác<br>thực<br>Nguồn DOI ưu tiên và<br>chứng cứ chính||Độ tin<br>cậy|cho quy trình<br>carbon aerogel<br>làm màng điện|
|||||cực|
||Baikeli et al.,_RSC Adv._2019,||||
||DOI**10.1039/C9RA03925B**;||||
|Hướng**Pb²⁺**bằng<br>biomass-derived N-<br>doped carbon là khả<br>thi|**Được xác**<br>**thực**<br>N-doped activated<br>nanoporous carbon từ<br>almond shells, DPASV,<br>linear**2–120 mg/L**, LOD**0.7**<br>**mg/L**, pH tối ưu**5.0**,||Rất<br>cao|Cực hữu ích để<br>thiết kế protocol<br>stripping cho<br>nhánh ion<br>sensing|
||deposition potential**−1.3 V**,||||
||deposition time**330 s**.<br>16||||
|Nhánh**kim loại nặng**<br>**đồng thời**thường<br>cần composite hoặc<br>chất hỗ trợ như**Bi**để<br>tăng stripping<br>performance|**Được xác**<br>**thực**<br>Zhu et al.,_J. Electrochem._<br>_Soc._2020, DOI<br>**10.1149/1945-7111/ab82f7**;<br>biomass-derived lotus-root-<br>like porous carbon/Bi<br>composite cho<br>simultaneous Pb²⁺/Cd²⁺.||Cao|Có nghĩa là Fe/<br>N-CA thuần có<br>thể**chưa đủ**,<br>đặc biệt nếu<br>muốn<br>simultaneous<br>Zn/Pb ở mức vết|
||17||||
||Malko et al.,_Nat. Commun._||||
||2016, DOI**10.1038/**<br>**ncomms13285**; Bates et al.,|||Nếu mục tiêu là<br>Fe/N-CA “có cơ|
|Fe–N–C active site<br>**không thể định**<br>**lượng đáng tin chỉ**<br>**bằng XPS at%**|**Được xác**<br>**thực mạnh**<br>_JACS_2023, DOI**10.1021/**<br>**jacs.3c08790**; literature<br>dùng nitrite stripping,<br>Mössbauer, CO<br>chemisorption, kinetic<br>probe để đếm site FeNₓ.||Rất<br>cao|chế”, phải lập<br>hẳn nhánh định<br>lượng site,<br>không thể dừng<br>ở XPS/N tổng|
||18||||
|Acid leaching + anneal<br>là post-treatment<br>thường gặp trong Fe–<br>N–C để loại Fe<br>aggregates và cải<br>thiện site accessibility|**Được hỗ**<br>**trợ nhưng**<br>**chưa xác**<br>**nhận riêng**<br>**cho coir**<br>**biosensor**<br>Kim et al. 2023 về<br>posttreatment Fe–N–C và<br>các bài FeNC liên quan cho<br>thấy acid treatment/second<br>heat treatment có vai trò<br>quan trọng.<br>19||Trung<br>bình|Có thể dùng làm<br>hướng thiết kế<br>Fe/N-CA, nhưng<br>cần thực nghiệm<br>chứng minh trên<br>hệ xơ dừa của<br>bạn|
|Công thức<br>**NH₄OH:urea:H₂O rất**<br>**cụ thể**, ưu thế<br>“honeycomb<br>preservation”, và lựa<br>chọn**không bleach**<br>**để Fe tẩm tốt hơn**|**Chưa xác**<br>**thực đủ**<br>Tôi chưa thu được primary<br>source accessible đủ chi tiết<br>để xác nhận độc lập các<br>mệnh đề này trong đúng<br>hệ coir–biosensor.||Thấp|Giữ ở mức**giả**<br>**thuyết làm việc**,<br>không nên viết<br>như dữ kiện<br>chắc chắn trong<br>tài liệu chính|



5 

|||||Hàm ý trực tiếp|
|---|---|---|---|---|
|Mục chính trong tài<br>liệu|Kết luận xác<br>thực|Nguồn DOI ưu tiên và<br>chứng cứ chính|Độ tin<br>cậy|cho quy trình<br>carbon aerogel<br>làm màng điện|
|||||cực|
|DOI được nêu trong<br>tài liệu cho một số<br>hướng khác, như<br>**10.3390/s24092787**<br>hoặc**10.1016/j.cej.**<br>**2024.081841**, hiện<br>**chưa đủ chứng cứ**<br>**xác thực**|**Chưa xác**<br>**thực đủ**|Trong lần tra cứu này tôi<br>chưa kết nối được các DOI<br>đó với đúng bài gốc như<br>cách tài liệu mô tả; vì vậy<br>chưa dùng chúng làm nền<br>kết luận.|Thấp|Không nên dựa<br>vào các DOI này<br>để ra quyết định<br>thực nghiệm cho<br>đến khi kiểm tra<br>thư viện/bài gốc<br>đầy đủ|



Kết luận của phần xác thực là: **phần nền vật liệu và N-doping đã đủ chắc để viết thành quy trình platform** , còn **nhánh Fe/N-CA cho biosensor** vẫn cần được chuyển từ mức “ý tưởng tốt” sang mức “site chemistry có chứng cứ”. Nếu bỏ qua bước đó, tài liệu sẽ mạnh ở mô tả tổng hợp nhưng yếu ở phần cơ chế cảm biến. 20 

## **Bảng tương thích** 

## **Thuật toán chấm tương thích** 

Tôi chấm “Tương thích %” theo đúng logic tái sử dụng quy trình. Mỗi hướng ứng dụng được so với **hướng đích: electrochemical biosensor dựa trên N-CA/Fe/N-CA từ xơ dừa** . Công thức dùng là: 


![](_images/chatgpt_images/_temp_9d4eb1fe_convert_.pdf-0006-05.png)


Trong đó _wi_ là trọng số theo tổng 100 điểm, còn _si_ ∈ [0, 1] là mức tái sử dụng thực tế. Tôi dùng 8 tiêu chí: **vật liệu** 20, **cơ chế phát hiện** 15, **pH/điện giải** 10, **electrode fabrication** 15, **measurement technique** 15, **LOD/linear range target** 10, **selectivity/interferences** 10, **sample matrix** 5. Cấu trúc chấm này bám theo đúng các biến số mà literature về biomass-derived electrochemical sensors và heavy metal / drug sensing cho thấy là có tính quyết định đến chất lượng điện cực. 21 

6 

## **Bảng tương thích** 

|Hướng ứng<br>dụng|Tương<br>thích<br>%|Các phần dùng<br>chung|Các phần cần điều<br>chỉnh/riêng|Cơ sở chấm %|
|---|---|---|---|---|
|**Paracetamol**<br>**sensor hóa**<br>**học**|**87%**|Cùng nền porous<br>carbon/N-doped<br>carbon; cùng logic<br>modifer flm trên<br>GCE; cùng gói<br>characterization<br>SEM–Raman–XPS–<br>BET–CV–EIS; thường<br>dùng DPV/CV; cùng<br>nhu cầu giảm Rct và<br>tăng active area|Không có lớp nhận<br>biết sinh học; cần tối<br>ưu pH gần trung tính<br>và anti-fouling đối với<br>phenolic oxidation; Fe<br>có thể không cần thiết<br>và đôi khi còn làm<br>tăng nền|Kelp-derived<br>biomass carbon đã<br>chứng minh AP<br>detection bằng CV/<br>DPV với LOD 0.004<br>μM và linear 0.01–20<br>μM, nên đây là<br>nhánh tái sử dụng<br>rất cao cho platform<br>N-CA.<br>15|
|**Pb²⁺/Zn²⁺ ion**<br>**sensing**|**79%**|Cùng nền carbon<br>flm, cùng mục tiêu<br>conductivity/<br>porosity/surface<br>defects, cùng CV/EIS<br>pre-check, cùng nhu<br>cầu ổn định màng và<br>tái lặp flm loading|Phải chuyển sang<br>stripping mode; cần<br>pH acetate acid hơn,<br>có bước<br>preconcentration, tối<br>ưu deposition<br>potential/time;<br>selectivity phụ thuộc<br>intermetallic<br>interference; nhiều<br>trường hợp cần Bi<br>hoặc chelator phụ|N-doped biomass<br>carbon cho Pb²⁺<br>bằng DPASV đã có<br>dữ liệu trực tiếp;<br>đồng thời literature<br>simultaneous heavy-<br>metal cho thấy khi đi<br>sang Zn/Pb, phần<br>riêng lớn nhất nằm<br>ở thông số stripping<br>và quản trị nhiễu,<br>không nằm ở lõi<br>carbon aerogel.<br>22|
|||Cùng near-neutral||Biomass-derived|
|||electrolyte; cùng||N,S-doped porous|
|||GCE modifer|Nếu dùng biosensor|carbon đã cho|
|||strategy; cùng yêu|thật sự thì vẫn cần|simultaneous DA/UA|
|**Dopamine/**||cầu peak separation,|biorecognition; còn|với LOD 0.1 μM và|
|**uric acid**<br>**trong**|**88%**|low background<br>current, anti-|nếu theo non-<br>enzymatic direct|ứng dụng trong<br>urine; vì vậy đây là|
|**biofuid**||interference và real-|sensing thì cần tối ưu|hướng gần|
|||sample validation;|peak resolution giữa|biosensor nhất về|
|||cùng có thể hưởng|DA/UA/AA|điều kiện pH, matrix|
|||lợi từ N-doping và||và đích phân tích|
|||cấu trúc xốp 3D||sinh học.<br>23|



7 

|Hướng ứng<br>dụng|Tương<br>thích<br>%|Các phần dùng<br>chung|Các phần cần điều<br>chỉnh/riêng<br>Cơ sở chấm %|Các phần cần điều<br>chỉnh/riêng<br>Cơ sở chấm %|Các phần cần điều<br>chỉnh/riêng<br>Cơ sở chấm %||
|---|---|---|---|---|---|---|
|**H₂O₂ sensing**<br>**và tiền đề**<br>**cho oxidase**<br>**biosensor**|**87%**|Cùng logic<br>transducer carbon<br>xốp dị nguyên tử;<br>cùng cần high ECSA,<br>low Rct, stable flm;<br>rất phù hợp để dùng<br>như lớp trung gian<br>cho oxidase-based<br>biosensor|Cần quyết định non-<br>enzymatic hay<br>enzymatic; nếu<br>enzymatic thì phải<br>triển khai bước<br>immobilization và<br>kiểm soát direct<br>electron transfer/<br>mediator<br>Biomass-derived N,P<br>co-doped carbon đã<br>được báo cáo cho<br>non-enzymatic H₂O₂<br>sensing; về mặt<br>platform, đây là cầu<br>nối tự nhiên nhất<br>giữa chemical<br>sensing và<br>biosensor.<br>24||||
||||Literature biomass-||||
|**Glucose**<br>**biosensor**|**70%**|Có thể dùng cùng<br>khung vật liệu<br>aerogel làm scafold<br>dẫn điện, tăng diện<br>tích bề mặt và giữ<br>enzyme/catalyst;<br>cùng workfow<br>chuẩn hóa flm và<br>điện hóa nền|Thường cần thêm Ni/<br>Cu/Co/Pd hoặc<br>enzyme GOx; pH/điện<br>thế làm việc khác<br>đáng kể; anti-<br>interference trong<br>serum phức tạp hơn;<br>cần biomolecule<br>immobilization ổn<br>định<br>derived carbon cho<br>glucose khá phong<br>phú nhưng thường<br>phải thêm catalyst<br>kim loại hoặc<br>enzyme; vì vậy “lõi<br>carbon aerogel”<br>dùng lại được,<br>nhưng phần nhận<br>biết/phản ứng là<br>workstream riêng.||||
||||25||||
||||Tính tương||thích||
|**Biomarker**<br>**biosensor**<br>**kiểu**<br>**aptamer/**<br>**antibody**|**64%**|Cùng scafold<br>carbon aerogel,<br>cùng nhu cầu<br>surface area lớn và<br>charge transfer tốt,<br>cùng EIS/DPV là<br>phép đo phổ biến|Phải mở thêm hoàn<br>toàn nhánh hóa học<br>gắn biomolecule,<br>blocking, chống hấp<br>phụ không đặc hiệu,<br>ổn định sinh học, ma<br>trận serum/plasma<br>thực<br>giảm vì phần quyết<br>định độ chọn lọc<br>không còn nằm chủ<br>yếu ở carbon<br>aerogel, mà ở<br>immobilization<br>chemistry và<br>recognition layer.||||
||||6||||



## **Diễn giải kỹ hơn theo nhân quả** 

Paracetamol đạt mức tương thích rất cao vì nó chia sẻ gần như trọn bộ **xương sống kỹ thuật** với biosensor platform: cùng kiểu carbon xốp dị nguyên tử, cùng cần màng ổn định trên GCE, cùng dùng CV/EIS để đọc charge transfer, và cùng tối ưu tín hiệu qua DPV. Điểm khác nằm ở việc paracetamol là **direct electrocatalytic sensing** , nên bạn chưa phải xử lý bài toán gắn biomolecule. Vì thế nó là bài test trung gian tốt nhất để chứng minh N-CA của bạn thật sự “điện hóa được”, trước khi đẩy hệ sang biosensor. 26 

Pb²⁺/Zn²⁺ có mức tương thích thấp hơn một chút vì cơ chế chuyển từ **direct oxidation/reduction của phân tử hữu cơ** sang **stripping voltammetry có bước lắng đọng trước** . Nghĩa là phần vật liệu dùng chung vẫn lớn, nhưng phần riêng gồm **điện giải acetate acid hơn, điện thế lắng đọng, thời gian lắng** 

8 

**đọng, nhiễu Cu²⁺, khả năng cần Bi film/composite** sẽ chi phối mạnh độ nhạy thật. Cặp Pb/Zn vì thế không phải là “ứng dụng kém tương thích”, mà là “ứng dụng đòi một protocol đo riêng”. 22 

Dopamine/uric acid và H₂O₂ là hai hướng tiềm năng nhất nếu mục tiêu lâu dài là **biosensor theo ngữ cảnh sinh học** , vì chúng giữ được điều kiện gần trung tính hơn, ma trận mẫu gần biosensor hơn, và cùng tận dụng lợi thế của carbon xốp dị nguyên tử trong hấp phụ phân tử, tách peak, và truyền điện tử. Ngược lại, glucose hay biomarker aptamer có tương thích thấp hơn vì từ thời điểm bạn thêm enzyme/ aptamer/antibody, **lớp nhận biết** bắt đầu quyết định hiệu năng nhiều không kém lớp carbon. 27 

## **Thông tin riêng cần tự nghiên cứu cho biosensor điện hóa** 

Điểm mấu chốt là: **biosensor điện hóa không chỉ là “sensor thường + thêm enzyme”** . Khi chuyển sang biosensor, chuỗi nguyên nhân thay đổi: bề mặt carbon không còn chỉ phải dẫn điện và hấp phụ analyte, mà còn phải **giữ được recognition layer** , **không làm mất hoạt tính sinh học** , **giảm fouling** , và **ổn định trong mẫu thực** . Vì vậy đây là phần cần được tách thành work-package riêng trong tài liệu nghiên cứu. 28 

Mức Thông tin riêng phải tự Cách kiểm chứng nhanh Vì sao bắt buộc cho biosensor ưu tìm/nghiên cứu nhất tiên Pyridinic/graphitic/pyrrolic N quyết định phân bố điện tích bề **Ổn định N-doping sau** XPS trước/sau 100–500 mặt, wettability và hoạt tính Rất **pyrolysis và sau cycling** chu kỳ CV; Raman trước/ điện hóa; nếu film cycling làm cao **điện hóa** sau ngâm đệm thay đổi bề mặt thì dữ liệu biosensor sẽ trôi Nitrite stripping như Fe tổng hay Fe at% không nói screening; Mössbauer/ **Định lượng thật sự của** được bao nhiêu site có ích; đây Rất XAS nếu muốn khẳng **Fe–N–C active sites** là chỗ dễ ngộ nhận nhất khi viết cao định mạnh cơ chế site cơ chế Fe/N-CA chemistry 18 Nếu còn Fe hạt, tín hiệu có thể TEM-EDS + XRD + **Phân biệt Fe hạt, Fe** tăng nhưng selectivity và Rất Mössbauer/XAS; ít nhất **carbide và Fe–Nₓ phân** stability giảm; đồng thời nền cao phải có XRD/TEM sau **tán** dòng tăng và cơ chế bị mơ hồ acid-leach Màng điện cực thất bại thường **Electrode ink** Thiết kế ma trận 3×3 với do ink, không phải do carbon; **formulation** : tỷ lệ Rất solids loading và binder quá đặc gây nứt, quá loãng gây carbon/binder/dung môi/ cao khác nhau; so sánh Rct, load thấp, binder sai gây block sonication ΔEp, độ lặp lại transfer So sánh EIS/CV của cùng Binder quyết định bám dính, ion **Loại binder** : chitosan/ carbon với từng binder; transport, biocompatibility và Rất Nafion/PEDOT:PSS hoặc nếu có biomolecule thì electrostatic environment cho cao khác theo dõi retained activity biomolecule 

So sánh EIS/CV của cùng carbon với từng binder; nếu có biomolecule thì theo dõi retained activity 29 

9 

|Thông tin riêng phải tự<br>tìm/nghiên cứu|Vì sao bắt buộc cho biosensor|Mức<br>ưu<br>tiên|Cách kiểm chứng nhanh<br>nhất|
|---|---|---|---|
|**Film loading và**<br>**thickness tối ưu**|Film dày tăng active area nhưng<br>cũng tăng điện trở khuếch tán<br>và capacitive current; biosensor<br>đặc biệt nhạy với lỗi này|Rất<br>cao|Cân loading theo μg/cm²<br>hoặc μL/drop; mapping<br>dòng nền và độ nhạy|
|**Bufer composition,**<br>**ionic strength, pH**<br>**window**|Biosensor lệ thuộc mạnh vào pH<br>và lực ion; điều kiện tối ưu cho<br>carbon không chắc tối ưu cho<br>biomolecule|Rất<br>cao|pH-map 4–9; theo dõi<br>peak current, baseline và<br>stability|
|**Measurement**<br>**technique phù hợp**:<br>DPV, SWV, amperometry,<br>EIS hay SWASV|Mỗi analyte và mỗi biosensor<br>cần mode đo khác nhau; chọn<br>sai mode làm mất ưu thế vật liệu|Rất<br>cao|So cùng một điện cực<br>trên 2–3 mode đo với<br>cùng analyte mục tiêu|
||||Tối ưu deposition|
|**Preconcentration**|Đây là phần riêng hoàn toàn so||potential, deposition|
|**parameters cho SWASV/**<br>**DPASV**nếu giữ nhánh|với biosensor phân tử; bỏ qua sẽ<br>dẫn đến kết luận sai về bản thân|Cao|time, quiet time,<br>frequency/amplitude/|
|Pb²⁺/Zn²⁺|vật liệu||step size theo DOE nhỏ|
||||30|
|**Interferences panel**|Biosensor chỉ có giá trị khi<br>chứng minh chống nhiễu; với<br>kim loại có Cu²⁺, với biofuid có<br>AA/UA/glucose/protein|Rất<br>cao|Thiết kế panel nhiễu<br>theo ma trận thật, không<br>chỉ ion đơn lẻ|
|**Calibration protocol**:||||
|external, standard<br>addition, blank<br>correction, drift|Ma trận sinh học và nước thực<br>gây matrix efect; calib sai thì<br>LOD và recovery vô nghĩa|Rất<br>cao|So sánh đường chuẩn<br>trong đệm sạch và trong<br>mẫu spike|
|correction||||
|**Reproducibility và**<br>**batch-to-batch**|Biosensor mà chỉ có một điện<br>cực đẹp là chưa đủ; cần kiểm<br>được quy trình tổng hợp và quy<br>trình phủ màng|Rất<br>cao|Ít nhất 5–6 điện cực độc<br>lập, 2–3 batch vật liệu,<br>báo RSD rõ ràng<br>16|
|**Real sample**|||Chọn một ma trận duy|
|**preparation**: lọc, pha|Đây là nơi phần lớn biosensor|Rất|nhất trước: nước máy,|
|loãng, protein removal,|thất bại khi rời dung dịch chuẩn|cao|urine giả, serum giả, hay|
|pH adjustment|||viên thuốc|
|**Biofouling và**<br>**passivation bề mặt**<br>**carbon**|Carbon xốp rất dễ hút protein<br>hoặc sản phẩm oxi hóa phenolic;<br>đó là trade-of giữa active area<br>và ổn định dài hạn|Cao|Chạy lặp nhiều lần trong<br>mẫu thật rồi đo suy giảm<br>peak/current|



10 

|Thông tin riêng phải tự<br>tìm/nghiên cứu|Vì sao bắt buộc cho biosensor|Mức<br>ưu<br>tiên|Cách kiểm chứng nhanh<br>nhất|
|---|---|---|---|
||||Thử một chemistry đơn|
|**Hóa học gắn**<br>**biomolecule**nếu đi đúng<br>nghĩa biosensor|Recognition layer quyết định độ<br>chọn lọc; không thể để phần này<br>ở mức “sẽ tính sau”|Rất<br>cao|giản trước, ví dụ chitosan<br>+ glutaraldehyde hoặc<br>EDC/NHS trên bề mặt|
||||oxy hóa|
|**Shelf-life và điều kiện**<br>**lưu trữ**|Với biosensor, tính ổn định theo<br>ngày/tuần quan trọng hơn<br>sensor hóa học thuần|Cao|Theo dõi tín hiệu sau 1,<br>3, 7, 14 ngày ở 4 °C và<br>nhiệt độ phòng|



Nếu phải chọn “các thông tin riêng” quan trọng nhất để bổ sung ngay vào tài liệu, tôi sẽ chọn bốn nhóm đầu tiên, vì chúng giải được bốn nút thắt nguyên nhân lớn nhất: **site chemistry** , **film formation** , **điều kiện điện giải/mode đo** , và **độ tin cậy phân tích** . Nếu bốn nhóm này chưa khóa được, mọi phần “biosensor” phía sau đều sẽ yếu về cơ chế và khó lặp lại. 31 

## **Danh mục tài liệu ưu tiên** 

Tôi sắp xếp nguồn theo tiêu chí: **độ gần với hệ xơ dừa/N-CA/Fe/N-CA** , rồi đến **độ hữu ích cho quy trình màng điện cực** , rồi mới đến **độ rộng review** . Vì người dùng yêu cầu có định hướng “xây dựng tài liệu”, tôi không chỉ liệt kê nguồn mà còn ghi rõ **cần trích gì từ mỗi nguồn** . 

|Mức||||
|---|---|---|---|
|ưu|Tài liệu|Vì sao phải đọc trước|Cần trích cụ thể|
|tiên||||
||||Tiền xử lý xơ dừa; kappa/|
|Rất<br>cao|**Fauziyah et al., Cellulose**<br>**2019, DOI 10.1007/**<br>**s10570-019-02753-x**<br>9|Nguồn gốc coir<br>cellulose aerogel đáng<br>tin nhất|lignin; điều kiện alkali–urea;<br>ảnh hưởng của pretreatment<br>lên aerogel; yield và tính|
||||chất vật lý|
|Rất<br>cao|**Fauziyah et al., Ind. Eng.**<br>**Chem. Res. 2020, DOI**<br>**10.1021/acs.iecr.0c03771**<br>10|Nguồn gần nhất với<br>route coir→N-doped<br>carbon aerogel|Công thức ammonia–urea;<br>điều kiện pyrolysis; đặc<br>trưng N-CA; cách chứng<br>minh N được đưa vào carbon|
|Rất<br>cao|**Susanto et al., ACS Omega**<br>**2024, DOI 10.1021/**<br>**acsomega.3c09297**<br>11|Nguồn mạnh nhất về<br>điều khiển dạng N-<br>doping ngay trong hệ<br>coir/PEFB|Quan hệ nhiệt độ–dạng N; vì<br>sao pyridinic-N tăng hoạt<br>tính; dữ liệu XPS N1s; cách<br>tác giả liên hệ cấu trúc với|
||||ORR|
|||Bài “platform” kinh điển|Kiểu điện cực; cách chuyển|
|Rất<br>cao|**Wang et al., Anal. Chem.**<br>**2014, DOI 10.1021/**<br>**ac401563m**<br>32|cho biomass-derived<br>carbon trong<br>electrochemical|vật liệu biomass carbon<br>thành sensing platform; các<br>analyte đã chứng minh; cách|
|||sensing/biosensing|báo performance|



11 

|Mức||||
|---|---|---|---|
|ưu|Tài liệu|Vì sao phải đọc trước|Cần trích cụ thể|
|tiên||||
||||Bản đồ ứng dụng theo loại|
|Rất<br>cao|**Onfray & Thiam,**<br>**Micromachines 2023, DOI**<br>**10.3390/mi14091688**<br>33|Review ngắn gọn, thực<br>dụng, bám đúng<br>electrochemical sensing|biomass carbon; kỹ thuật cải<br>thiện hoạt tính sensing; ví dụ<br>điển hình cho dược phẩm,|
||||kim loại nặng, biomolecule|
||||Cách chuẩn bị electrode|
|Rất<br>cao|**Kim et al., Sens. Actuators**<br>**B 2018, DOI 10.1016/j.snb.**<br>**2017.12.066**<br>34|Nguồn chính cho nhánh<br>paracetamol|modifer; đệm sử dụng; DPV/<br>CV conditions; LOD, linear<br>range, anti-interference với|
||||AA/DA; real sample nếu có|
||||pH acetate, deposition|
|Rất<br>cao|**Baikeli et al., RSC Adv. 2019,**<br>**DOI 10.1039/C9RA03925B**<br>16|Nguồn trực diện nhất<br>cho Pb²⁺ trên N-doped<br>biomass carbon|potential, deposition time,<br>Nafon ratio, interference<br>của Cu²⁺, repeatability,<br>reproducibility, recovery|
||||trong nước máy|
||**Zhu et al., J. Electrochem.**|Nguồn chỉ ra khi nào|Vai trò Bi; simultaneous|
|Rất|**Soc. 2020, DOI**|nên ghép thêm Bi/|detection; cấu trúc carbon/|
|cao|**10.1149/1945-7111/ab82f7**|composite cho heavy-|Bi; trade-of giữa composite|
||17|metal stripping|complexity và sensitivity|
||||Protocol nitrite adsorption/|
|Rất<br>cao|**Malko et al., Nat. Commun.**<br>**2016, DOI 10.1038/**<br>**ncomms13285**<br>35|Bài nền cho active-site<br>counting của Fe–N–C|stripping; cách liên hệ site<br>density với activity; giới hạn<br>của chỉ dùng bulk|
||||composition|
||||Khi nào nên dùng kinetic|
|Rất<br>cao|**Bates et al., JACS 2023, DOI**<br>**10.1021/jacs.3c08790**<br>36|Bài hiện đại hơn về định<br>lượng FeNₓ bằng kinetic<br>probe|method; mối tương quan với<br>Mössbauer/CO<br>chemisorption; cách<br>benchmark Fe/N-CA nếu bạn|
||||đi sâu cơ chế|
|Cao|**Yang et al., Mater. Chem.**<br>**Phys. 2022, DOI 10.1016/**<br>**j.matchemphys.**<br>**2022.126825**<br>37|Nguồn tốt cho nhánh<br>biomolecule gần sinh<br>học|NaOH/thiourea route; near-<br>neutral DA/UA sensing; thiết<br>kế peak separation; urine<br>real sample|
||||Design rules của 3D carbon|
|Cao|**Li et al., Adv. Mater.**<br>**Technol. 2023, DOI 10.1002/**<br>**admt.202300666**<br>38|Review gần nhất về 3D<br>biomass-derived carbon<br>cho electrochemical<br>biosensors|cho biosensor; chọn analyte;<br>chọn morphology; các lỗi<br>thường gặp khi chuyển từ<br>carbon material sang|
||||biosensor thật|



12 

|Mức||||
|---|---|---|---|
|ưu|Tài liệu|Vì sao phải đọc trước|Cần trích cụ thể|
|tiên||||
||||Những hạn chế hiện còn của|
|Cao|**Wang et al., Molecules**<br>**2025, DOI 10.3390/**<br>**molecules30143046**<br>39|Review mới để cập nhật<br>khoảng trống hiện nay|biomass-derived carbon<br>sensors; lỗ hổng về<br>reproducibility, matrix efect,<br>scale-up, cơ chế|
||||Quan hệ giữa cấu trúc|
|Cao|**Cheng et al., J. Phys. Chem.**<br>**C 2016, DOI 10.1021/**<br>**acs.jpcc.5b11280**<br>40|Hữu ích cho tư duy<br>electrode architecture<br>và binder-free design|aerogel, diện tích bề mặt,<br>vận chuyển điện tích và hiệu<br>năng điện cực; tham số nào<br>đáng đưa vào tài liệu quy|
||||trình|
|Phụ<br>trợ<br>tiếng<br>Việt|**Tóm tắt luận án/tài liệu**<br>**tiếng Việt về cellulose**<br>**aerogel từ xơ dừa của**<br>**HCMUT, không DOI**<br>41|Không dùng để xác<br>thực cơ chế chính,<br>nhưng hữu ích để nội<br>địa hóa vật liệu và thuật<br>ngữ|Thuật ngữ Việt hóa, bối cảnh<br>nguyên liệu xơ dừa Việt<br>Nam, cách trình bày quy<br>trình địa phương, dữ liệu<br>hấp phụ nếu cần phần tổng<br>quan nền|



Nếu phải rút gọn xuống chỉ **5 nguồn bắt buộc đầu tiên** để bắt đầu viết ngay tài liệu nền, tôi sẽ chọn: **Cellulose 2019** , **IECR 2020** , **ACS Omega 2024** , **Analytical Chemistry 2014** , và **RSC Advances 2019** . Năm nguồn này đủ để dựng được một tài liệu chặt theo chuỗi: **tiền xử lý xơ dừa → tạo aerogel → tạo N-CA → biến thành sensing platform → triển khai protocol ion sensing thực tế** . 42 

## **Kết luận và giới hạn** 

## **Kết luận ngắn gọn** 

Kết luận ngắn gọn nhất nhưng chính xác là: **hướng carbon aerogel từ xơ dừa để làm màng điện cực điện hóa là khả thi và đã có nền DOI đủ mạnh; hướng biosensor điện hóa dựa trên N-CA là khả thi cao; còn Fe/N-CA chỉ nên được nâng thành hướng chính khi bạn bổ sung định lượng site FeNₓ và chứng minh lợi ích thật trên analyte mục tiêu** . Paracetamol là nhánh gần nhất để chuẩn hóa platform; Pb²⁺/Zn²⁺ là nhánh tốt để mở rộng sang ion sensing nhưng cần một protocol stripping riêng; còn dopamine/uric acid và H₂O₂ là hai nhánh tiềm năng nhất nếu muốn dịch chuyển từ “sensor điện hóa” sang “biosensor theo ngữ cảnh sinh học”. 43 

## **Khuyến nghị thực nghiệm tiếp theo** 

Quyết định thực nghiệm nên theo thứ tự sau đây. Bước đầu, hãy lấy **N-CA không Fe** làm baseline và khóa ba biến nền: **tổng hợp lặp lại được** , **ink phủ màng lặp lại được** , và **nền điện hóa ổn định qua CV/EIS** . Chỉ sau khi N-CA vượt baseline này mới nên sang paracetamol. Nếu N-CA không cho tín hiệu hoặc Rct không cải thiện so với bare GCE/carbon black, thì thêm Fe sẽ chỉ làm tăng độ phức tạp mà chưa giải đúng vấn đề. 44 

Sau khi khóa N-CA, hãy chạy hai “test case” tối thiểu. Test case thứ nhất là **paracetamol bằng DPV/CV** trong đệm gần trung tính để đọc năng lực electrocatalytic cơ bản của film. Test case thứ hai là **Pb²⁺** 

13 

**bằng DPASV/SWASV** trong acetate pH khoảng 5 để đọc năng lực preconcentration và stripping. Hai case này cắt đôi toàn bộ không gian ứng dụng: một bên là **redox hữu cơ phân tử** , một bên là **kim loại vết có bước lắng đọng trước** . Nếu cùng một vật liệu đi được tốt cả hai case, khi đó mới có nền đủ chắc để thiết kế biosensor thật sự. 45 

Nếu kết quả cho thấy Fe có ích, bước tiếp theo không phải là viết “Fe–Nₓ đóng vai trò active sites” ngay, mà là chứng minh bằng một hướng định lượng site. Ở mức thực dụng, bạn có thể dùng **nitrite stripping** như một screening method cho FeNₓ; nếu cần bài bản hơn, mới mở sang Mössbauer/XAS. Điều này sẽ làm tài liệu của bạn khác hẳn kiểu viết “có Fe nên hoạt tính cao”, vốn rất dễ bị phản biện. 18 

## **Giới hạn và câu hỏi mở** 

Báo cáo này có ba giới hạn chính. Thứ nhất, một số thông số rất cụ thể trong tài liệu tải lên, đặc biệt tỉ lệ **NH₄OH:urea:H₂O** , logic **không bleach** để hỗ trợ Fe impregnation, và chuỗi **HCl leach–anneal** cho Fe/NCA, hiện tôi chưa xác thực độc lập đến mức có thể coi là chuẩn. Thứ hai, vài DOI được nêu trong tài liệu chưa xác minh được hoàn toàn trong lần rà soát này nên tôi không dùng để chống lưng cho kết luận. Thứ ba, “Tương thích %” là **điểm số kỹ thuật để ưu tiên hướng nghiên cứu** , không phải dự đoán xác suất thành công cuối cùng. Vì vậy, nếu cần một tài liệu nội bộ thật chắc, các phần đang mang nhãn “chưa xác thực đủ” nên được đưa vào mục **giả thuyết nghiên cứu** chứ không nên viết ở giọng khẳng định. 

1 3 9 42 https://link.springer.com/article/10.1007/s10570-019-02753-x https://link.springer.com/article/10.1007/s10570-019-02753-x 

2 8 11 12 Controlling N-Doping Nature at Carbon Aerogels from Biomass ... https://scholar.its.ac.id/en/publications/controlling-n-doping-nature-at-carbon-aerogels-from-biomass-for-e/? utm_source=chatgpt.com 

4 14 Biomass-Derived Carbon Materials as an Emerging Platform ... https://pubs.acs.org/doi/10.1021/acs.iecr.2c03058?utm_source=chatgpt.com 

5 13 40 Biomass-Derived Carbon Fiber Aerogel as a Binder-Free ... https://pubs.acs.org/doi/10.1021/acs.jpcc.5b11280?utm_source=chatgpt.com 

6 28 29 https://www.mdpi.com/2079-6374/11/7/239 https://www.mdpi.com/2079-6374/11/7/239 

7 38 https://advanced.onlinelibrary.wiley.com/doi/10.1002/admt.202300666 https://advanced.onlinelibrary.wiley.com/doi/10.1002/admt.202300666 

10 20 https://pubs.acs.org/doi/10.1021/acs.iecr.0c03771 https://pubs.acs.org/doi/10.1021/acs.iecr.0c03771 

15 26 34 43 45 https://research.polyu.edu.hk/en/publications/novel-two-step-activation-of-biomassderived-carbon-for-highly-se/ 

https://research.polyu.edu.hk/en/publications/novel-two-step-activation-of-biomass-derived-carbon-for-highly-se/ 

16 22 30 https://pubs.rsc.org/en/content/articlepdf/2019/ra/c9ra03925b https://pubs.rsc.org/en/content/articlepdf/2019/ra/c9ra03925b 

14 

17 

## https://www.researchgate.net/publication/ 

## Like_Hierarchical_Porous_CarbonBismuth_Composite 

https://www.researchgate.net/publication/ 

341097357_Ultrasensitive_and_Simultaneous_Electrochemical_Determination_of_Pb_2_and_Cd_2_Based_on_Biomass_Derived_Lotus_RootLike_Hierarchical_Porous_CarbonBismuth_Composite 

18 31 35 https://www.nature.com/articles/ncomms13285 https://www.nature.com/articles/ncomms13285 

> 19 https://hal.science/hal-05087937/document https://hal.science/hal-05087937/document 

21 33 Biomass-Derived Carbon-Based Electrodes for Electrochemical Sensing: A Review | MDPI https://www.mdpi.com/2072-666X/14/9/1688 

23 27 37 https://www.sciencedirect.com/science/article/abs/pii/S0254058422011312 https://www.sciencedirect.com/science/article/abs/pii/S0254058422011312 

> 24 https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/abs/10.1002/elan.201800717 https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/abs/10.1002/elan.201800717 

> 25 https://pubs.rsc.org/en/content/articlelanding/2015/ra/c5ra22495k 

https://pubs.rsc.org/en/content/articlelanding/2015/ra/c5ra22495k 

32 44 https://pubs.acs.org/doi/10.1021/ac401563m https://pubs.acs.org/doi/10.1021/ac401563m 

> 36 https://pubs.acs.org/doi/10.1021/jacs.3c08790 https://pubs.acs.org/doi/10.1021/jacs.3c08790 

> 39 https://pubmed.ncbi.nlm.nih.gov/40733312/ 

https://pubmed.ncbi.nlm.nih.gov/40733312/ 

> 41 https://grad.hcmut.edu.vn/hv/download/LATS/2080916/TOM_TAT_NTXPhuong.pdf https://grad.hcmut.edu.vn/hv/download/LATS/2080916/TOM_TAT_NTXPhuong.pdf 

15 

