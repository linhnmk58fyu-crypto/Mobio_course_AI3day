# Báo Cáo Các Hạng Mục Còn Thiếu & Hành Động Của Chị
*Dựa trên việc bóc tách tài liệu Use Case và Kế hoạch thiết lập RFP đã thống nhất, dưới đây liệt kê các hạng mục thông tin "đầu vào" bị thiếu chưa thể tự động điền sinh, cần chị chủ động rà soát và cung cấp để em cấu hình tự động hóa.*

## 1. Thông tin cấu trúc dữ liệu / Knowledge Base
- **Tình trạng:** CHƯA CÓ
- **Cần chị làm:** Cấp quyền cho AI/System truy cập vào **Kho tài liệu thầu cũ** (tài liệu mẫu, các bản doc/excel của dự án cũ) hoặc đính kèm 1-2 folder dự án thầu mẫu tiêu biểu vào đây. Nếu không nhận được, AI không có dữ liệu để thực thi cơ chế "tìm kiếm & so khớp bản nháp".
- **Cách thức:** Paste link Drive hoặc Upload bộ thư mục mẫu vào thư mục `Dự án RFP`.

## 2. Danh sách Nhóm/Tag/Rule Phân loại nghiệp vụ
- **Tình trạng:** CHƯA CÓ
- **Cần chị làm:** Cần cung cấp bộ quy tắc phân loại nhóm tính năng (Module) và các thẻ Tag chuyên môn (VD: KHCN, KHDN, Kiến trúc, Bảo mật...). Đây là xương sống để AI đánh tag khi import vào file JSON và query ra đúng câu trả lời.
- **Cách thức:** Gửi file list hoặc điền vào ô chat.

## 3. Danh sách Nhân sự (Danh bạ PIC)
- **Tình trạng:** CHƯA CÓ
- **Cần chị làm:** Cần cung cấp danh sách tên/email của các nhân sự đóng vai trò PO, SA, AM, PD. Việc này giúp AI tự động điền đúng tên người chịu trách nhiệm (PIC) vào cột Assignment của Template Excel.

## 4. Bộ tiêu chí rủi ro và Thang điểm chấm QC
- **Tình trạng:** CHƯA RÕ RÀNG
- **Cần chị làm:** Trong Use Case có nhắc đến AI sẽ "Đánh giá theo thang 1-10 dựa trên các điểm bất thường/bộ tiêu chí đánh giá", nhưng không có bộ tiêu chí này ở file đính kèm. Chị cần cung cấp **bảng tiêu chí rủi ro** (Ví dụ: Yêu cầu giao source code = Rủi ro 10đ...) để AI có căn cứ học.
- **Cách thức:** Upload file tài liệu (excel/word/pdf) chứa bộ tiêu chí hoặc paste trực tiếp.

## 5. Chọn Công cụ chạy (Kích hoạt Workflow)
- **Tình trạng:** CHƯA XÁC ĐỊNH
- **Cần chị làm:** Cần chị xác nhận luồng Trigger. Chị muốn mỗi khi nhận 1 hồ sơ thầu mới thì quy trình Extract này chạy bằng cách nào? (Chạy command bằng lệnh ở folder này? Gửi email vào hòm thư nào đó? Hay upload lên 1 web app?)

---
👉 **Note:** Các file Template đầu ra phục vụ quá trình làm việc đã được em tạo sẵn bằng định dạng Markdown (các bảng excel format mẫu) tại `Sprint_1/Templates/`. Chị có thể kiểm tra ở thư mục cây bên trái.
