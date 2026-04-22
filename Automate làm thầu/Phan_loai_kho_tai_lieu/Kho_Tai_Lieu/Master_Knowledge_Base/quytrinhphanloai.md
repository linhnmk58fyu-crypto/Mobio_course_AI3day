### LUỒNG CÔNG VIỆC PHÂN LOẠI YÊU CẦU TỰ ĐỘNG (SEQUENTIAL FLOW)

**Quy ước:**

Nhóm 1: Nghiệp vụ (Functional))

Nhóm 2: Kỹ thuật (Technical)

Nhóm 3: Tài chính & Pháp lý

Nhóm 4: Năng lực triển khai

Nhóm 5: Chuyển giao & Đào tạo

#### Bước 1: Tiếp nhận & Nhận diện Bối cảnh (Context Identification)

Đây là bước "làm sạch" để tránh rác dữ liệu từ các thầu cũ.

* **Hành động:** Xác định tên Ngân hàng và các thuật ngữ chức danh đặc thù (Ví dụ: LPBank gọi là "Nhân viên kinh doanh", SeABank gọi là "CBB").
* **Mục tiêu:** Tạo bộ lọc ngôn ngữ để AI hoặc người viết không bị nhầm lẫn khi đọc yêu cầu.

#### Bước 2: Phân tích Đối tượng Thụ hưởng (Entity Analysis)

Thay vì chỉ đọc từ khóa, bước này phân tích xem **ai/cái gì** là đối tượng chính của yêu cầu.

* **Quy tắc phân loại:**
  * Nếu đối tượng là **Người dùng/Cán bộ** (thao tác, xem, báo cáo, chỉ tiêu KPI) ->  **Nhóm 1 (Nghiệp vụ)** .
  * Nếu đối tượng là **Hệ thống/Dữ liệu** (kết nối, bảo mật, lưu trữ, hiệu năng, phân quyền DB) ->  **Nhóm 2 (Kỹ thuật)** .
  * Nếu đối tượng là **Pháp nhân/Tiền** (giấy phép, vốn, bảo lãnh) ->  **Nhóm 3 (Pháp lý)** .
  * Nếu đối tượng là **Kinh nghiệm/Nhân sự** (hợp đồng cũ, CV, kế hoạch) ->  **Nhóm 4 (Năng lực triển khai)** .

#### Bước 3: Quét Từ khóa & Gán Nhãn (Keyword Mapping)

Thực hiện quét nhanh các từ khóa trọng tâm để gán nhãn sơ bộ cho yêu cầu.

* **Nhóm 1:** KPI, Dashboard, Lead, Customer 360, Phân quyền User.
* **Nhóm 2:** API, Microservices, Kafka, Security, ISO 27001, Phân quyền DB.
* **Nhóm 5:** Đào tạo, Chuyển giao, SLA, Manual, Bảo hành.

Nếu yêu cầu là nghiệp vụ rồi thì sẽ để ở bước nghiệp vụ, không đổi sang nhóm khác vì từ khóa.

Ví dụ: SLA có trong yêu cầu nghiệp vụ => giữ nguyên nhóm 1, không đổi sang nhóm 5.

#### Bước 4: Áp dụng Ràng buộc Kiểm soát (Constraint Validation)

Đây là bước quan trọng để đảm bảo tính Senior và trung thực.

* **Rule 1 (Highlight nghi vấn):** Nếu yêu cầu không rõ ràng (ví dụ chỉ ghi mỗi từ "Báo cáo"), hệ thống tự động gắn nhãn **[CẦN LÀM RÕ]** và highlight vàng.
* **Rule 2 (Anti-Fake):** Nếu yêu cầu vượt quá tính năng chuẩn của Mobio, gắn nhãn  **[GAP - CẦN PRODUCT CONFIRM]** .
* **Rule 3 (Security-First):** Các yêu cầu liên quan đến Cloud/On-premise hoặc Thông tư 09 phải được ưu tiên đẩy vào Nhóm 2 để thẩm định tính tuân thủ.

#### Bước 5: Đóng gói & Chuyển giao (Packaging)

* **Hành động:** Tự động chia yêu cầu vào 5 Tab tương ứng trong Master File.
* **Kết quả:** Mỗi nhóm sẽ nhận được đúng phần việc của mình với các ghi chú rủi ro/cảnh báo đã được Presales phân tích trước.
