Bạn nên chia kho tài liệu thành 3 tầng logic để AI dễ dàng định vị phạm vi câu hỏi:

* **Tầng 1: Master_Knowledge_Base (Dữ liệu gốc của Mobio)**
  * `Technical_Architecture.pdf` (Kiến trúc Microservices, K8s, Kafka).
  * `Security_Compliance.pdf` (Thông tư 09, ISO 27001, mã hóa dữ liệu).
  * `Product_Manual_vX.pdf` (Hướng dẫn sử dụng chi tiết từng tính năng).
* **Tầng 2: RFP_Library (Kho lịch sử thầu - Chia theo nhóm yêu cầu)**
  * `01_Functional_Answers.xlsx` (Tổng hợp các câu trả lời về nghiệp vụ đã được duyệt).
  * `02_Technical_Answers.xlsx` (Tổng hợp các câu trả lời về hạ tầng/bảo mật).
  * `04_Deployment_Experience.xlsx` (Danh sách dự án, CV nhân sự, Project Plan mẫu).
* **Tầng 3: Customer_Specific (Dữ liệu riêng từng ngân hàng)**
  * `LPBank/`, `OCB/`, `SeABank/` (Chứa các file RFP gốc và bản final).
