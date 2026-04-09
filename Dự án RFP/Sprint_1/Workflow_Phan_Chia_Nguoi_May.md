# Phân Nhánh Luồng Làm Việc: Con Người vs. Máy (AI)

*Tài liệu này chia form I-P-O ban đầu thành 2 mạch công việc độc lập/song song để phân định rõ khối rủi ro và khối tự động hóa.*

---

## 1. Mạch Tư Duy Phân Chia Tổng Thể

### CON NGƯỜI (Nhân sự) làm gì?
*Đóng vai trò là "Bộ não chiến lược & Người điều phối"*
1. **Ngoại giao & Giao tiếp:** Trực tiếp tương tác với Khách hàng (KH). Thương lượng, làm rõ các khuất tất mà văn bản không viết rõ.
2. **Xử lý rác/dữ liệu cứng:** Phân loại thủ công ban đầu với các tập tài liệu giấy, file ảnh (scan nhòe), dữ liệu quá lộn xộn chưa thể dùng tool số hóa.
3. **Quyết định bằng trực giác & Kinh nghiệm:** Phán đoán "mùi" rủi ro của gói thầu (Go/No-go). Ước lượng mức độ khó của 1 tính năng kỹ thuật phi tiêu chuẩn (chưa có trong repo lịch sử).
4. **Việc chưa có tool:** Bù đắp các công đoạn hệ thống chưa vươn tay tới được (Ví dụ: đi in ấn bản cứng đóng dấu mộc đỏ công ty).

### MÁY (Agent AI/System) làm gì?
*Đóng vai trò là "Thư ký tốc ký & Bộ máy xử lý quy chuẩn"*
1. **Các công việc đã nằm lòng logic sẵn:** Mapping câu hỏi cũ-mới, tra cứu thông tin trong Database, chấm điểm dựa trên Checklist cố định.
2. **Chỉnh sửa & Xào nấu File:** Tự động copy-paste, tạo folder, nhân bản, đồng bộ font chữ, sửa chính tả, fill gạch đầu dòng vào báo cáo.
3. **Sinh nội dung (Gen AI):** Viết lại cấu trúc câu trả lời cho mượt mà (Gen Draft) dựa trên những ý tưởng cốt lõi con người mớm cho.

---

## 2. Áp Dụng Phân Nhánh Vào 5 Bước Phản Hồi RFP

| Các Bước Thầu | Nhiệm Vụ Của NGƯỜI (Thực Thi) | Nhiệm Vụ Của MÁY (Hỗ Trợ/Chạy Nền) |
| :--- | :--- | :--- |
| **B.1: Tiếp nhận Thầu** | - Chat/ Gọi điện với KH để lấy file thầu.<br>- Đọc bản giấy, đánh giá sơ bộ mức độ "thơm/chua".<br>- Chốt lệnh **GO** để bắt đầu cắm máy làm. | - Scan những file PDF mượt/Docx để ném ra thông tin Mốc Thời Gian.<br>- Check các "lỗi chết người" dựa trên bảng Rule (có vi phạm tính pháp lý không). |
| **B.2: Khởi tạo File** | - Nhặt các file báo cáo tài chính/năng lực nằm tản mác bên ngoài (chưa được hệ thống hóa) đưa vào thư mục chung. | - Sinh cây Folder, tạo file `Excel phản hồi` chuẩn form.<br>- Móc các tài liệu năng lực tiêu chuẩn từ Kho ném tự động vào Folder thầu mới. |
| **B.3: Phản hồi / Viết Nháp** | - Quyết định "Chiến lược đánh": Chỗ này mình đáp ứng kiểu gì? (Không/ Vượt trội/ Tính phí).<br>- Dùng kinh nghiệm note comment sườn vào Excel cho câu hỏi siêu Khó. | - Chạy Mapping tự động: Câu nào giống thầu cũ 100% thì Máy điền sẵn luôn Tuyên bố đáp ứng.<br>- Tự động dùng chữ AI viết thành câu rành mạch (2nd Draft) từ cái chữ nháp lôm côm của Người. |
| **B.4: QC & Trình bày** | - Đọc tổng duyệt nội dung rủi ro thương mại, pháp lý - bằng cảm quan.<br>- Ký tá, in ấn đóng mộc gửi khách. | - Đồng nhất font chữ, căn chỉnh bảng biểu, in đậm các ý theo đúng Rule công ty.<br>- Chấm điểm văn phong xem có logic với nhau không. |
| **B.5: Báo giá (MD)** | - Lôi Technical Lead vào đánh giá Man-day cho mấy món Tùy chỉnh (Customize) dị thường. | - Tự động điền MD cho các tính năng gốc (có sẵn trong báo giá chuẩn).<br>- Tính tổng toán học, nhân đơn giá ra con số nháp. |

---

## 3. Câu Hỏi Trực Tiếp: Khúc Mắc & Phân Vân Cần Chị Làm Rõ

Dựa trên việc chia lại như thế này, em có 3 câu hỏi (điểm nghẽn) rất phân vân cần chị định hướng để thiết kế cho đúng ý chị:

1. **(Về bản giấy lộn xộn):** Hiện tại ở công ty, tài liệu giấy/lộn xộn chiếm khoảng bao nhiêu % các gói thầu? Chị định mua tool OCR vật lý chuyên dụng của bên thứ 3 (như máy scan xịn) hay muốn em (Agent) tự xách việc chạy bằng cơm xử lý mớ text hình ảnh nhòe tẹt đó?
2. **(Về giao tiếp giữa máy và người):** Ở Bước 3, khi con người đọc bản Draft 1 của Máy, dùng trực giác thay đổi chiến lược và viết ra nháp... cái NHÁP đó chị định dùng Nền tảng nào? (Ví dụ: Chị định bôi đỏ vào Sheet trên môi trường Google Sheet, hay định là có 1 cái Tool App nhỏng lên để anh em gõ vào?). Trả lời câu này mới định hình được Máy nối với Người thế nào.
3. **(Về Quyền uy tối thượng):** Nếu Máy tra ra điểm rủi ro là 10 (Chết), nhưng Người bằng kinh nghiệm (quan hệ ngầm với KH) bảo cứ GO đi, thì Máy sẽ chạy bất chấp theo Người đúng không chị? Nghĩa là ở mọi bước, **Quyết định của Người luôn override (chèn đè) được Máy?**
