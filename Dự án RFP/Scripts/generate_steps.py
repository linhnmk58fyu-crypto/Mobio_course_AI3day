import os

base_dir = "C:\\Users\\linhn\\Khoa_Hoc_Antigravity\\Dự án RFP\\Quy_Trinh_IPO_5_Buoc"

steps_data = {
    "2_Khoi_Tao_File_Folder": {
        "readme": "# README: BƯỚC 2 - KHỞI TẠO TÀI NGUYÊN\nMục tiêu: Xây dựng kho chứa vật lý và nhặt tài liệu hành chính từ kho vào.\n- AI: Tìm file DKKD, BCTC mới nhất và clone.\n- Người: Cấp quyền access.",
        "dod": "# TIÊU CHÍ ĐÁNH GIÁ (DoD) BƯỚC 2\n- [ ] Đã sinh cây thư mục vật lý theo mẫu.\n- [ ] Đã clone đủ các file tài liệu hành chính.\n- [ ] Có file Excel Tracking Phản Hồi rỗng.",
        "index": "# INDEX BƯỚC 2\nChứa các cấu trúc tạo lập...",
        "workflow": "```mermaid\ngraph TD\nA[Nhập Thông tin] --> B[Sinh Cây Folder]\nB --> C[Clone File Mẫu]\n```",
        "inputs": {
            "template": {"File_Mau_Checklist.md": "Template Checklist"},
            "checklist": {"Check_Ho_So.md": "Các loại giấy tờ cần có"},
        },
        "outputs": {
            "1_Cay_Thu_Muc_Project_TEMPLATE.txt": "Cây thư mục rỗng",
            "2_Checklist_Giao_Viec_TEMPLATE.md": "Bảng checklist"
        }
    },
    "3_Phan_Hoi_Requirement": {
        "readme": "# README: BƯỚC 3 - PHẢN HỒI YÊU CẦU\nMục tiêu: AI làm ảo thuật map rỗng 80%, Người xâu kim 20%.",
        "dod": "# TIÊU CHÍ ĐÁNH GIÁ (DoD) BƯỚC 3\n- [ ] File Excel đã điền xong 100% cột Giải Pháp.\n- [ ] Không còn câu nào bị bỏ trống.",
        "index": "# INDEX BƯỚC 3\nKhu vực cốt lõi...",
        "workflow": "```mermaid\ngraph TD\nA[Chạy Mapping] --> B[Gen Draft 1]\nB --> C[Human Feedback]\nC --> D[Gen Draft 2]\n```",
        "inputs": {
            "mockup_data": {"Yeu_Cau_RFP.md": "Danh sách Y/C kỹ thuật"},
            "question_bank": {"Q_And_A.md": "Hỏi đáp"},
        },
        "outputs": {
            "1_Excel_Draft_Response_TEMPLATE.csv": "Form,PIC,Giai Phap,Ty Le",
            "2_Danh_Sach_Thieu_Sot.md": "Nội dung cần làm rõ"
        }
    },
    "4_QC_Va_Format": {
        "readme": "# README: BƯỚC 4 - KIỂM SOÁT ĐỊNH DẠNG & QC\nMục tiêu: Agent Audit sẽ vào xăm soi file và chỉnh trang diện mạo.",
        "dod": "# TIÊU CHÍ ĐÁNH GIÁ (DoD) BƯỚC 4\n- [ ] Format in đậm dòng 1 đạt chuẩn 100%.\n- [ ] Điểm logic chéo > 8/10.",
        "index": "# INDEX BƯỚC 4\n...",
        "workflow": "```mermaid\ngraph TD\nA[Audit Agent] --> B[Chấm điểm logic]\nB --> C[Run Auto Format]\n```",
        "inputs": {
            "guideline": {"Quy_Quy_Format.md": "Chữ 12/Arial/In đậm dòng 1"},
        },
        "outputs": {
            "1_Ban_Final_PDF_TEMPLATE.pdf": "",
            "2_Bang_Cham_Diem_QC_TEMPLATE.md": "Điểm: 9/10"
        }
    },
    "5_Bao_Gia_MD": {
        "readme": "# README: BƯỚC 5 - LÊN GIÁ (ESTIMATE MD)\nMục tiêu: Ra số tiền cuối cùng cho hạng mục Customize.",
        "dod": "# TIÊU CHÍ ĐÁNH GIÁ (DoD) BƯỚC 5\n- [ ] Đã có Technical Lead duyệt file Man-day.\n- [ ] Bảng giá hợp lệ.",
        "index": "# INDEX BƯỚC 5\n...",
        "workflow": "```mermaid\ngraph TD\nA[Tính MD] --> B[Nhân Đơn Giá]\nB --> C[Tech Lead Duyệt]\n```",
        "inputs": {
            "template": {"Bang_Gia_Chuan.md": "Template Giá"},
        },
        "outputs": {
            "1_Bang_Quote_Gia_TEMPLATE.md": "Man-day, Đơn giá",
        }
    }
}

for step, data in steps_data.items():
    step_path = os.path.join(base_dir, step)
    
    # Create files in root
    with open(os.path.join(step_path, "README.md"), "w", encoding="utf-8") as f: f.write(data["readme"])
    with open(os.path.join(step_path, "INDEX.md"), "w", encoding="utf-8") as f: f.write(data["index"])
    with open(os.path.join(step_path, "Tieu_Chi_Danh_Gia.md"), "w", encoding="utf-8") as f: f.write(data["dod"])
    
    # Create workflow
    os.makedirs(os.path.join(step_path, "Process"), exist_ok=True)
    with open(os.path.join(step_path, "Process", "Workflow.md"), "w", encoding="utf-8") as f: f.write(data["workflow"])
    
    # Create Inputs
    inp_base = os.path.join(step_path, "Input")
    os.makedirs(inp_base, exist_ok=True)
    for folder in ["mockup_data", "template", "question_bank", "checklist", "guideline", "tool", "reference"]:
        os.makedirs(os.path.join(inp_base, folder), exist_ok=True)
        
    for inp_folder, files in data.get("inputs", {}).items():
        f_dir = os.path.join(inp_base, inp_folder)
        os.makedirs(f_dir, exist_ok=True)
        for fname, fcontent in files.items():
            with open(os.path.join(f_dir, fname), "w", encoding="utf-8") as f: f.write(fcontent)
            
    # Create Outputs
    out_base = os.path.join(step_path, "Output")
    os.makedirs(out_base, exist_ok=True)
    for fname, fcontent in data.get("outputs", {}).items():
        with open(os.path.join(out_base, fname), "w", encoding="utf-8") as f: f.write(fcontent)

print("Xong!")
