# Think Outloud

- **Phân tích yêu cầu**: User yêu cầu "Dựa vào file này ...quytrinhtonghop.md, hãy tạo cho tôi input dựa trên yêu cầu tại đây: ...Master_Knowledge_Base. Đây là input: ...RFP_Response".
- **Sự nhập nhằng (Ambiguity)**:
  - Có thể user nhầm từ "output" thành "input" trong câu đầu tiên. Cụ thể ý của user là: "Hãy xử lý và tạo cho tôi output dựa trên rule ở thư mục A. Và đây là data input ở thư mục B."
  - Nhưng do dùng từ "tạo cho tôi input", cũng có khả năng user đang đề xuất AI tạo giúp một "System Prompt" (hay Input Context) thật chuẩn và đóng gói để user tự đi chạy trên các công cụ AI khác.
- **Tiếp cận**: 
  - Các file Excel rất lớn (27-74MB), không thể đọc thả vào prompt. Nếu user muốn tạo file CSV từ số liệu này (như các conversation trước), ta phải dùng thư viện `pandas` (Python) để quy hoạch thành code pipeline.
  - Phù hợp nhất lúc này: Tạo một **Implementation Plan** trình bày 2 kịch bản hiểu và hỏi user muốn đi theo hướng nào. Đề xuất Hướng 1 là viết Script Python đọc file Excel vì nó tự động hóa đúng luồng (như conversation 98e2d0cc "Automating RFP Compliance Mapping").
