# Nhật Ký Hỏi Đáp & Fix Lỗi Pipeline Enrich RFP

Tài liệu này lưu trữ lại toàn bộ các vấn đề (bug) phát sinh và câu trả lời trong quá trình test chạy thực tế Pipeline làm giàu dữ liệu RFP cùng với file `EIB.xlsx`.

## 1. Vấn Đề: Lỗi không match được Config CSV
- **User hỏi:** `Đang gặp lỗi này: Khong co config CSV mapping nao match voi chuoi 'EIB.xlsx'`
- **Nguyên nhân:** File Excel đầu vào có tên là `EIB.xlsx` nhưng trong bảng tham chiếu `rfp_mapping_config.csv` không có dòng khai báo nào chứa từ khóa "EIB".
- **Giải quyết:** Hướng dẫn User mở file CSV và nhập thêm cấu hình (Tọa độ cột Yêu cầu, Trả lời, Tên sheet) dành riêng cho từ khóa `EIB`.

## 2. Vấn Đề: Lỗi Logic của Pandas (Code rác ValueError)
- **User hỏi:** Bị lỗi Python in ra terminal `ValueError: The truth value of a Series is ambiguous. Use a.empty...` ở dòng 118.
- **Nguyên nhân:** Lỗi cú pháp Python khi sử dụng toán tử `if not sheet_conf:` trên một mảng dữ liệu (Series) của Pandas thay vì dùng `is None`.
- **Giải quyết:** Vào tận Source code của `enrich_rfp_library.py` đổi dòng 118 thành `if sheet_conf is None:`.

## 3. Vấn Đề: Nghi vấn thuật toán chống trùng lặp (Deduplication)
- **User hỏi:** Báo log hệ thống kêu `[SKIP] Data nay dang ton tai 100% tren he thong (bi trung)...` \- Nhưng mà nội dung file mới của mình đang sửa test có giống hệ thống cũ đâu?
- **Nguyên nhân 1:** Ban đầu logic Code chỉ check Trùng lặp bằng hệ tọa độ gộp: `Ngân hàng` + `Yêu cầu`. Nó lờ đi việc check nội dung `Diễn giải đáp ứng`. Do đó cùng ngân hàng, cùng yêu cầu, dù câu trả lời mới tinh thì tool vẫn tưởng là dữ liệu cũ và gạt bỏ.
  -> **Fix:** Thêm điều kiện bắt buộc vào Code dòng số 196: `subset=["Ngân hàng", "Yêu cầu", "Diễn giải đáp ứng"]`.
- **Nguyên nhân 2 (Cực kỳ vi diệu):** Lý do thực sự khiến Tool trả về lượng dữ liệu "Thêm mới = 0" là do lỗi toán học khi đếm. Các Thư viện cũ (do đợt luồng OCB, LPBank, SeABank) thu thập vốn đã bị dính sẵn Hàng Trăm Dòng Rác Duplicate từ chính nội bộ file của nó. Khi gộp cục DataFrame để quét và Drop Duplicates, Tool đã thẳng tay *xóa sạch đống rác di tích* này. Dẫn tới số dong chênh lệch bị Âm. Thuật toán tưởng là thêm dòng thất bại nên In ra chữ `[SKIP]`
  -> **Fix:** Code lại thuật toán Python, tách hệ thống tự động Dọn rác của Data cũ (`cleaned_old_duplicates`) riêng biệt hẳn so với đống Data mới nạp vào. Biến Tool thành công cụ tiện ích 2 tay: Một tay dọn rác kho dữ liệu cũ, Một tay bế data từ file ngân hàng mới nhét vào an toàn.

## 4. Vấn Đề: Băn Khoăn về Dữ Liệu Ló Lọt Lưới (Unclassified)
- **User hỏi:** Có yêu cầu nào bị bỏ qua do hệ thống không biết xếp nó vào phân nhóm 01, 02, 03... không?
- **Trả lời:** **KHÔNG**. Hệ thống được thiết kế bằng lưới lọc Fallback. Hễ một dòng văn bản không mang từ khóa "kỹ thuật", "bảo hành", "pháp lý",... v..v.. thì Hệ Thống sẽ *Tự Động Mặc Định* nhét hết chúng nó vào File to nhất là `01_Functional_Answers.xlsx` (Nghiệp vụ - Chức năng). Chỉ duy nhất bỏ qua nếu cột Excel đó bị khách bỏ trống rỗng (Blank).

## 5. Vấn Đề: Cách Chạy Lệnh Cho Người Không Chuyên
- **User hỏi:** Làm thế nào để chạy lệnh?
- **Trả lời:** 
  1. (Dành cho Dev): Vào cửa sổ Terminal của VS Code, gõ `cd "đường-dẫn-Tool"` rồi gõ lệnh `python enrich_rfp_library.py`.
  2. (Dành cho người thường ngoài Windows File Explorer): Đã tạo sẵn một file tên là **`run_pipeline.bat`**. Người dùng chỉ việc copy file Excel ném vào `Input_New_RFP`, sửa CSV Config xong, rồi **kích đúp chuột** vào file `run_pipeline.bat` là hệ thống có màn hình tự động kích hoạt chạy chữ vèo vèo mà không cần gõ thủ công bất kỳ chữ nào.

### Kết luận
Toàn bộ logic lỗi liên quan đến UTF-8 (lỗi font chữ tiếng Việt in ra màn hình Command Line) và Tọa độ Toán học đã được fix triệt để. Pipeline hiện nay hoàn thiện đạt mức độ Production-Ready (Sẵn sàng chạy thực chiến mọi khối lượng dự án).
