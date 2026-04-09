# README: TỔNG QUAN BƯỚC 1 - TIẾP NHẬN THẦU (GO/NO-GO)

**Mục tiêu cốt lõi:** Ngăn chặn các thầu "rác" lọt vào vòng trong làm tiêu tốn tài nguyên nhân sự và máy móc (Token AI).
**Thời gian xử lý kỳ vọng (SLA):** < 2 giờ làm việc kể từ lúc KH gửi mail.

## Tại sao có bước này?
Khách hàng có thể gửi đề bài thầu qua bất kỳ nguồn nào: Điện thoại, file mềm, giấy cứng. Trong một mớ thông tin lộn xộn đầu vào, quy trình này đóng vai trò như chiếc màng lọc. Nhiệm vụ tối thượng là trả lời được câu hỏi: **"Dự án này rủi ro thế nào? Mobio có chốt làm hay bỏ?"**.

## Trách nhiệm các bên
- **Nhân sự (Human):** Tương tác đa kênh với khách hàng. Quét dọn các file cứng thành mềm để đút cho AI đọc. Lãnh đạo ra quyết định cuối cùng CÓ LÀM HAY KHÔNG (Go/No-go).
- **Hệ thống (AI Agent):** Xài kỹ thuật để đọc và bóc tách Ngày tháng Hạn Chót (Deadline). Dùng "sức trâu" dò mìn các yếu tố pháp lý tiêu cực (VD: Cướp source code) so với Luật công ty để đưa ra cảnh báo đỏ phục vụ Lãnh đạo.

Nếu ỔN (Go) -> Trigger gọi Bước 2 đẻ file.
Nếu KHÔNG ỔN (No-go) -> Giải tán, thu hồi tài nguyên.
