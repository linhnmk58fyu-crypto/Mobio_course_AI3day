# Kế Hoạch Triển Khai Thực Thi (Implementation Plan)

**Mục tiêu:** Xây dựng hệ thống tự động hóa quy trình phản hồi thầu RFP có sự phối hợp nhịp nhàng giữa Nhân Sự và AI (Human-in-the-loop). Bản kế hoạch này kết hợp chặt chẽ giữa 5 nền tảng kiến trúc hệ thống và 5 bước nghiệp vụ chuyên môn (I-P-O).

---

## PHẦN 1: TÍCH HỢP 5 NỀN TẢNG VÀO QUY TRÌNH THỰC CHIẾN

### Nền tảng 1: Phân Định Ranh Giới (Áp dụng xuyên suốt)
Quy tắc bất biến: AI chạy các khâu tính toán số lượng/lọc tìm, Con Người chốt chặn chiến lược và rủi ro.
- **Trong Bước 1 (Tiếp nhận & Extract):** MÁY trích xuất deadline, lọc tiêu chí chết -> NGƯỜI quyết định "Go hay No-go".
- **Trong Bước 2 (Khởi tạo vùng việc):** MÁY tạo 100% folder và nhặt các tài liệu hành chính mẫu từ kho thả vào.

### Nền tảng 2: Chuẩn Hóa Kho Tri Thức (Mỏ neo cho Bước 3)
- **Chuẩn hóa Database:** Trước khi "cắm máy" chạy tự động, phải có kịch bản dọn dẹp các hồ sơ thầu cũ. Format bắt buộc để học là định dạng JSON bao gồm: `Câu Hỏi - Tuyên Bố Đáp Ứng - Lời Trả Lời - Tags (Công nghệ/Nghiệp vụ) - Version`.
- **Approve to Train:** Những câu hỏi hoàn toàn mới sau khi chốt thầu sinh ra ở Bước 3.3 phải qua 1 vòng KIỂM DUYỆT (Approve) của Quản lý mới được nạp ngược lại vào não hệ thống. Tránh tình trạng rác kiến thức.

### Nền tảng 3: Vòng Lặp Phản Hồi (Tâm điểm Bước 3.3)
Quy trình "Trò gõ nháp - Thầy sửa lỗi" được vận hành tại khâu sinh nội dung phản hồi RFP:
- **Vòng AI:** Ráp kiến thức từ Kho, nhả ra bản Draft 1 dạng gạch đầu dòng ngắn dọc theo các Cell Excel.
- **Vòng NGƯỜI:** Đọc lướt, comment note định hướng (Ví dụ: "Nhấn mạnh bảo mật cho cái này nha mày") vào cột bên cạnh.
- **Vòng AI 2:** Tiếp nhận comment, tự sinh form văn bản uyển chuyển, chuẩn văn phong (Draft 2).

### Nền tảng 4: Cấy Bộ Quy Tắc Chuyên Gia 
Đóng gói quy trình não bộ của một Solution Architect (SA) thành rule cố định cho Máy:
- **Ma trận chiến lược (Cho Bước 3.2):** Máy bám vào rule để tự đưa ra kết luận (Ví dụ gặp câu Yêu cầu Bắt buộc + Chưa có sẵn = Cam kết Customize có tính phí).
- **Format Formatter (Cho Bước 4.2):** Tự động bôi đậm câu chủ đề đầu tiên, ép kích thước font tiêu chuẩn mà không cần tay người bôi đen.

### Nền tảng 5: QC Độc Lập & Lên Giá MD
- **QC nội dung (Trong Bước 4.1):** Tạo một con Agent đóng vai "Khách Hàng Khó Tính" – không tham gia viết nháp, chỉ nhảy vào đọc bản Final và chấm điểm 1-10 để lôi ra các lỗi logic mâu thuẫn (Ví dụ: Phía trên bảo có, ở dưới lại lỡ mồm bảo không có).
- **Đóng Dấu MD (Trong Bước 5):** AI tự fill Man-day chuẩn, Technical Lead chỉ cần vào verify đúng những ô Customize khó để chốt bảng giá cuối.

---

## PHẦN 2: LỘ TRÌNH CÔNG VIỆC TRIỂN KHAI THỰC CHIẾN (EXECUTION PATH)

Dựa trên cấu trúc trên, đây là danh sách các đầu việc (Sprint) cần giải quyết để hệ thống thành hình:

### Giai đoạn 1: Khởi nguồn Dữ Liệu (Data Preparation)
1. Thu thập Kho tài liệu RFP gốc từ khách hàng và các mẫu phản hồi cũ.
2. Code bộ công cụ trích xuất (Script) để cào sạch rác và băm tài liệu cũ thành dạng JSON/Database truy vấn siêu tốc (Vector Database).
3. Cấp quyền nhúng (Embed) cho kho dữ liệu.

### Giai đoạn 2: Lập Trình Cơ Chế Chạy (Automation Workflow Setup)
1. **Tool 1 (Bước 1+2):** Code bot tự extract file gửi tới, chấm rủi ro, sinh file Excel sườn và tạo Thư mục Thầu tự động.
2. **Tool 2 (Bước 3):** Code hệ thống tìm kiếm (Search) nhúng so khớp Vector: Đối chiếu text từ RFP mới với JSON cũ, tìm ra % trùng.
3. **Tool 3 (Feedback Node):** Hook cổng kết nối vào Excel/G-Sheet để bắt được khi nào Người Dùng gõ Feedback xong thì AI tự lấy đó Gen lại bản 2nd Draft.

### Giai đoạn 3: Tối ưu và Chạy thử (QC & Sandbox)
1. Code Rule định dạng bản in cho đẹp (Bold/Font size).
2. Viết Prompt "đóng vai Audit/Sở ban ngành" cho con Agent QC chấm điểm chéo.
3. Chạy 1 RFP mẫu thực tế (Sandbox) từ đầu đến đuôi để đo đạc độ mượt, loại bỏ các khúc mắc chạm lỗi kỹ thuật.

*(Chị duyệt Kế hoạch này là em bắt đầu cắm mặt làm Giai đoạn 1 luôn nha!)*
