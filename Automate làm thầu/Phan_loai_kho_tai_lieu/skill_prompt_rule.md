### 1. BỘ QUY TẮC (RULES) - RÀ SOÁT VÀ THỰC THI

Đây là các quy tắc bắt buộc phải tuân thủ trước khi đặt bút viết hoặc sau khi hoàn thành bản thảo.

* **Rule 1: Quy tắc "Tên riêng & Thuật ngữ"**
  * Sử dụng hàm *Find & Replace* để đảm bảo không tồn tại tên ngân hàng cũ.
  * Chuyển đổi 100% từ "Doanh nghiệp/Khách hàng" sang "Ngân hàng" (trừ khi đang mô tả về khách hàng của ngân hàng).
  * Sử dụng đúng thuật ngữ chức danh của hồ sơ mời thầu (ví dụ: RM, CBB, SRBO, P. QHKH).
* **Rule 2: Quy tắc "Dẫn chiếu 3 lớp"**
  * Mọi câu trả lời "Đáp ứng" phải đi kèm dẫn chiếu theo format: `[Mã tài liệu] -> [Chương/Mục] -> [Số trang/Số hình]`.
  * Ví dụ:  *Tham chiếu: GP-01 -> Chương 3 -> Mục 3.2.1 (Trang 45)* .
* **Rule 3: Quy tắc "Xử lý Định dạng (Anti-Format)"**
  * Cấm copy trực tiếp định dạng từ file gốc. Mọi nội dung dán vào Master File phải chọn  *Paste as Plain Text* .
  * Chỉ sử dụng định dạng **Bold** cho các thông số định lượng và từ khóa hành động (ví dụ:  **P95 < 2s** ,  **Tự động** ,  **Real-time** ).
* **Rule 4: Quy tắc "Bằng chứng thị giác"**
  * **In-cell Image:** Ảnh minh họa phải đặt trong ô, có viền đỏ khoanh vùng tính năng.

---

### 2. BỘ KỸ NĂNG (SKILLS) - PHÂN TÍCH VÀ ĐIỀU CHỈNH HÀNH VĂN

Bộ kỹ năng này giúp người viết thầu điều chỉnh nội dung tùy theo đối tượng cạnh tranh và yêu cầu cụ thể mà không cần phán đoán chủ quan.

* **Skill 1: Kỹ năng "Hành văn đối ứng" (Tone & Mood Adjusting)**

  * **Nhóm đối thủ Global:** Tập trung vào sự phù hợp địa phương (Local Fit), khả năng tùy biến (Customization) và tuân thủ pháp lý Việt Nam (Thông tư 09, An ninh mạng).
  * **Nhóm đối thủ Local/SI:** Tập trung vào tiêu chuẩn kiến trúc Enterprise (Enterprise Standard) và năng lực xử lý tải thực tế (Proven Performance tại các ngân hàng đã triển khai).
* **Skill 2: Kỹ năng "Bóc tách yêu cầu"**

  * Phân tích yêu cầu thầu thuộc nhóm **Must have (M)** hay  **Optional (O)** .
  * Với yêu cầu (M): Diễn giải tập trung vào sự ổn định và sẵn có của tính năng.
  * Với yêu cầu (O): Diễn giải tập trung vào sự linh hoạt và khả năng mở rộng trong tương lai.
* **Skill 3: Kỹ năng "Cảnh báo rủi ro pháp lý & Chi phí"**

  * Nhận diện các yêu cầu đòi hỏi tích hợp bên thứ 3 (OCR, SMS, Email, Maps API) để đưa ra lưu ý về chi phí phát sinh cho khách hàng ngay trong phần diễn giải.
* **Skill 4: Kỹ năng "Bằng chứng hóa" (Evidence-based Writing)**

  * Chuyển đổi các mô tả tính năng trừu tượng thành các bước thao tác cụ thể hoặc thông số kỹ thuật có thể đo lường.
  * *Ví dụ:* Thay vì nói "Hệ thống chạy nhanh", hãy viết "**P95 < 2s** với quy mô **5.000 user** đồng thời".

---

### 3. BỘ CẤU TRÚC PROMPT (PROMPTS) - DÀNH CHO VIỆC TẠO NỘI DUNG

Để tạo ra phần diễn giải chi tiết, hãy sử dụng cấu trúc prompt dựa trên dữ liệu đầu vào cụ thể thay vì cảm tính.

**Prompt mẫu để tạo nội dung diễn giải:**

> **Context:** Tôi đang trả lời yêu cầu RFP của ngân hàng [Tên Ngân hàng].
> **Yêu cầu từ hồ sơ thầu:** [Copy nội dung yêu cầu trong file Excel vào đây].
> **Dữ liệu thực tế của Mobio:** [Mô tả ngắn gọn tính năng hiện có của Mobio hoặc copy mục lục tài liệu kỹ thuật].
> **Task:** Viết nội dung cho cột "Diễn giải tuyên bố đáp ứng" theo các tiêu chuẩn sau:
>
> 1. Khẳng định mức độ đáp ứng (Đáp ứng hoàn toàn/Đáp ứng vượt trội).
> 2. Mô tả chi tiết cách hệ thống xử lý yêu cầu này (Sử dụng dữ liệu thực tế, không hứa hẹn).
> 3. Nếu là yêu cầu kỹ thuật, hãy mô tả luồng dữ liệu (Data flow) hoặc cấu trúc thành phần (Component).
> 4. Nếu là yêu cầu nghiệp vụ, hãy mô tả quy trình thao tác từ lúc bắt đầu đến khi kết thúc.
> 5. **Constraint: **Thay "Doanh nghiệp" bằng "Ngân hàng", bôi đậm các con số và thông số kỹ thuật. Trình bày dưới dạng các đầu dòng rõ ràng;
>
> * **Tuyệt đối không bịa đặt:** Không hứa hẹn các tính năng chưa có trong Roadmap hoặc chưa được Product Team xác nhận.
> * **Highlight nghi vấn:** Mọi nội dung chưa rõ về kỹ thuật hoặc chưa có dữ liệu kiểm chứng **phải được bôi màu vàng (Highlight)** để chuyển bộ phận giải đáp.
> * **Xác thực tên đơn vị:** Cấm tuyệt đối việc nhầm lẫn tên các Ngân hàng đối tác trong phần diễn giải.

---

### 4. MẪU DIỄN GIẢI THỰC TẾ (REFERENCE EXAMPLES)

Dựa trên các file bạn đã cung cấp, đây là cách áp dụng các Rule và Skill trên:

* **Ví dụ về Năng lực pháp lý (Rule 1 & 3):**
  "**Đáp ứng vượt trội!** Nhà thầu là doanh nghiệp được thành lập từ năm  **2017** , có hơn **8 năm** kinh nghiệm. Vốn điều lệ đạt  **35.253.230.000 VNĐ** , vượt mức yêu cầu tối thiểu của Ngân hàng."
* **Ví dụ về Hiệu năng (Rule 3 & Skill 1):**
  "**Đáp ứng hoàn toàn!** Cam kết thời gian phản hồi đạt mức  **P95 < 2 giây** . Hệ thống vận hành trên nền tảng  **Kubernetes** , cho phép **Auto-scaling** linh hoạt theo tải thực tế tại các dự án tương đương (~5.000 - 8.000 user)."
* **Ví dụ về Tính năng Offline (Skill 3):**
  "**Không đáp ứng (Giải trình):** Hệ thống ưu tiên mô hình **Online-first** để đảm bảo an toàn dữ liệu theo tiêu chuẩn ngân hàng, tránh rủi ro rò rỉ dữ liệu khi thiết bị bị mất hoặc thất lạc."

Bộ Skill/Prompt/Rule này tập trung vào việc chuẩn hóa quy trình sản xuất nội dung thầu, giúp bạn duy trì chất lượng hồ sơ đồng nhất và chính xác.
