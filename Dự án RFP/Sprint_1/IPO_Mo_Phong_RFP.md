# Mô Phỏng Quy Trình Phản Hồi RFP & Đánh Giá Điểm Mù (Gap Analysis)
*Dành cho: Phân tích luồng nghiệp vụ dưới góc nhìn nhân sự mới handle dự án.*

---

## PHẦN 1: MÔ PHỎNG LUỒNG LÀM VIỆC THEO FORMAT I-P-O

Dưới vai trò là nhân sự mới (và cũng là Agent AI) được giao xử lý từ A-Z một gói thầu mới gửi tới, em sẽ chạy quy trình như sau:

### Bước 1: Tiếp nhận và phân tích đề bài
- **Input (I):** File hồ sơ RFP hoặc Email thông báo mời thầu từ khách hàng. Bộ tiêu chí đánh giá quy định sẵn.
- **Process (P):** 
  - Đọc quét toàn bộ văn bản để bóc tách các thông tin cơ bản (Tên, Chủ đầu tư, Deadline, Hình thức nộp).
  - Đối chiếu nội dung đề bài với bộ "Tiêu chí chết/Gây loại" để tìm ra các rủi ro năng lực hoặc tài chính, đánh giá bằng thang điểm từ 1-10.
- **Output (O):** Bảng "Thông tin gói thầu" đã điền. Bảng danh sách "Các điểm bất thường" kèm cảnh báo rủi ro.

### Bước 2: Khởi tạo không gian làm việc (Workplace)
- **Input (I):** Bảng Thông tin gói thầu vừa xuất ra (từ Bước 1), dữ liệu Kho tài liệu thầu cũ (Knowledge Base).
- **Process (P):**
  - Tự động tạo thư mục Dự án thầu mới.
  - Lên danh sách những tài liệu cần phải nộp nộp (Ví dụ: ĐKKD, BCTC, Hồ sơ năng lực...). 
  - Truy xuất vào Kho tài liệu cũ để tìm bản cứng/bản PDF mới nhất của văn bản cần nộp và clone (nhân bản) thả vào thư mục mới tạo. Tạo các file mẫu (trống) đối với những tài liệu chưa có sẵn.
  - Tạo cấu trúc bảng Excel theo dõi phản hồi RFP.
- **Output (O):** Thư mục thầu vật lý, File Checklist Hồ sơ, File Mẫu Bảng phản hồi RFP (trống nội dung, chỉ có cột).

### Bước 3: Phản hồi Requirement (Giải quyết năng lực cốt lõi)
- **Input (I):** Danh sách các yêu cầu trong file RFP, Kho tài liệu thầu (Các câu trả lời cũ của dự án cùng Domain). Bộ ma trận tuyên bố đáp ứng.
- **Process (P):** 
  - Phân loại nhanh các ý (Đâu là kỹ thuật, đâu là tính năng module, đâu là năng lực nhà thầu).
  - Mapping (So khớp): Tìm trong Kho tài liệu cũ câu hỏi tương tự -> Lôi câu trả lời cũ ra đo % trùng lặp.
  - Nêu Khuyến nghị: Từ phân loại cũ, gợi ý cách trả lời dựa trên "Ma trận đáp ứng" (Vượt trội, Một phần, Không đáp ứng...).
  - Sinh bản Nháp 1 (1st Draft) dạng gạch đầu dòng ngẵn gọn. Sau đó người dùng (chị) vào Review và comment Feedback vào cột bên cạnh. Nhận feedback, AI viết lại hoàn chỉnh (2nd Draft).
  - Với câu hỏi hoàn toàn MỚI, sẽ đánh dấu để ưu tiên cập nhật ngược lại vào thư viện sau khi làm xong.
- **Output (O):** Bảng Mapping yêu cầu; Bảng Phản hồi RFP hoàn thiện (Bản Final).

### Bước 4: Kiểm soát Chất lượng (QC) & Trình bày
- **Input (I):** Bản Final Phản hồi RFP ở Bước 3. Bộ tiêu chuẩn format độ dài. Tiêu chí phản hồi dự thầu.
- **Process (P):** 
  - Đóng vai "Người chấm thầu" để rà soát toàn bộ những câu Tuyên bố đáp ứng phần cứng.
  - Chấm điểm logic của từng câu. Đưa ra Feedback yêu cầu chỉnh sửa nếu câu văn thiếu tính khách quan hoặc mâu thuẫn lẫn nhau giữa các module.
  - Format lại toàn bộ form chữ, in đậm câu chốt hạ đầu tiên, đồng bộ size font.
- **Output (O):** Bảng Phản hồi (Version đã làm đẹp và Check QC). Sheet chấm điểm nội bộ.

### Bước 5: Ước tính Man-Day (MD) & Lên giá
- **Input (I):** Bảng Phản hồi (những mục cần phải tùy biến/phát triển mới ở Bước 3). Dữ liệu MD và MD Rate cũ của hệ thống.
- **Process (P):** 
  - Tính toán độ khó những món Code mới bằng cách tham khảo lịch sử các Task tương tự.
  - Áp dụng công thức `Thời gian dự kiến (MD) * Đơn giá (MD rate)`.
- **Output (O):** Quotation sơ bộ (Bảng chào giá & Effort list).

---

## PHẦN 2: ĐÁNH GIÁ NHƯỢC ĐIỂM (GAP) & LỖ HỔNG XUYÊN SUỐT QUY TRÌNH

Sau khi đóng vai và chạy mô phỏng ngầm trong đầu, em nhận ra có một số nhược điểm lớn (Gap) mà tài liệu Use Case chưa làm rõ. Nếu áp dụng thực tế ngay sẽ đứt gãy luồng:

> [!WARNING]
> Mức độ cảnh báo: Cao - Cần làm rõ trước khi bắt tay lập trình cơ chế.

### 1. Gap ở Bước 1: Quyết định "Go / No Go" ngay từ đầu
- **Nhược điểm:** Quy trình bảo là *Khởi tạo Document -> Phản hồi RFP (draft/mapping)...* ngay sau khi trích xuất thông tin. Nhưng thực tế ở Bước 1, nếu AI phát hiện ra các **"Điểm rủi ro/Yếu tố gây loại"** (ví dụ yêu cầu pháp lý không thỏa mãn, tỉ lệ rủi ro = 9/10), thì lẽ ra quy trình phải TẠM DỪNG (Pending) để Hội đồng/Giám đốc đưa ra quyết định **Go / No-go** (Có làm thầu này hay bỏ).
- **Lỗ hổng:** Cứ để AI chạy cắm đầu sang Bước 2, Bước 3 (Sinh file, Mapping dữ liệu) khi chưa chốt "Go" sẽ tốn token và tài nguyên con người (phải vào review Draft 1 của một cái thầu sắp bị vứt đi).

### 2. Gap ở Bước 3: Touchpoint giữa AI và Con Người trên Excel
- **Nhược điểm:** Môi trường ghi nhận Draft 1/ Draft 2 đang hiểu trên file Excel. AI sinh ra Draft 1, người dùng chê và gõ nội dung Feedback... Sau đó AI phải đọc lại file Excel. Nhưng làm sao để **Trigger (kích hoạt) AI lần hai**? 
- **Lỗ hổng:** Chưa có nút bấm hay cơ chế nào ghi nhận "Chị đã feedback xong bảng excel rồi đấy, AI chạy Draft 2 đi". Nếu file làm việc là Google Sheet thả chung Cloud thì AI có quyền hook (móc) dữ liệu không? Quy trình chưa mention giải pháp kỹ thuật tương tác hai chiều này.

### 3. Gap ở Bước 5: Ước tính MD cực kỳ nhạy cảm
- **Nhược điểm:** Tham chiếu lịch sử sinh MD cho báo giá tính năng code "Tương tự" là hành động rất rủi ro. Tính năng *"Báo cáo"* của Khách hàng A có thế mất 5 MD, nhưng *"Báo cáo"* Khách hàng B phức tạp hơn nhiều có thể mất 30 MD.
- **Lỗ hổng:** Không có vòng lặp (Review) của Technical Lead / SA trong Bước 5. Quy trình đang để Output ra thẳng Quotation. Bắt buộc phải có touchpoint để SA (Kỹ sư trưởng) duyệt lại cái MD này trước khi AI ra Báo giá cuối.

### 4. Gap về Cấu trúc dữ liệu chống nhiễu (Dữ liệu Rác)
- **Nhược điểm:** Bước 3.3 có dòng: *Thêm câu hỏi & trả lời Mới vào lại Knowledge Base*.
- **Lỗ hổng:** Ai là người phê duyệt cái Câu trả lời Mới đó đạt chuẩn "Chân lý" (Single Source of Truth) để được nạp vào não AI? Nếu một dự án có bạn nhân viên trả lời sai/hứa lèo khách hàng, và AI học ngay câu đấy nhét vào Kho dữ liệu... thì các dự án sau AI sẽ tiếp tục hứa lèo. Chưa có cơ chế **Kiểm duyệt học máy (Approve to Train)**.

### 5. Gap về Định dạng tài liệu đầu vào
- **Lỗ hổng:** Đề bài RFP của nhiều Chủ đầu tư Việt Nam thường gửi dưới dạng PDF bản scan mờ, có đóng mộc đỏ hoặc hình ảnh chụp màn hình, không phải lúc nào cũng là file `.docx`. Quy trình chưa hề nhắc đến khâu **OCR (Nhận diện ký tự quang học)**. Nếu ném cho AI một cục hình ảnh, Bước 1 sẽ tạch ngay lập tức.
