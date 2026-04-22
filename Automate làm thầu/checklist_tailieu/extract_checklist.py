import os
import csv
import re
import glob
import pandas as pd

INPUT_DIR = "INPUT"
OUTPUT_DIR = "OUTPUT"
MAPPING_FILE = "mapping_tu_khoa.csv"

def load_mapping():
    mapping_rules = []
    try:
        with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                nhom = row['Nhóm']
                tu_khoa = [k.strip().lower() for k in row['Từ khóa'].split(',')]
                ten_tai_lieu = row['Tên tài liệu']
                mapping_rules.append({'nhom': nhom, 'tu_khoa': tu_khoa, 'ten_tai_lieu': ten_tai_lieu})
    except Exception as e:
        print(f"Lỗi đọc file mapping: {e}")
    return mapping_rules

def process_text_content(content, mapping_rules):
    results = []
    # Chia thành các câu hoặc theo dòng để quét
    sentences = re.split(r'(?<=[.!?]) +|\n+', content)
    for sentence in sentences:
        if len(sentence.strip()) < 10: 
            continue
            
        sentence_lower = sentence.lower().strip()
        matched = False
        
        # Thử tìm mapping phù hợp nhất
        for rule in mapping_rules:
            if any(keyword in sentence_lower for keyword in rule['tu_khoa'] if keyword):
                
                ten_tai_lieu = rule['ten_tai_lieu']
                
                if "bản sao" in sentence_lower:
                    ten_tai_lieu += " (bản công chứng)"
                
                ghi_chu = "M" if any(w in sentence_lower for w in ["bắt buộc", "yêu cầu", "phải có", "đề nghị"]) else "O^^"
                
                results.append({
                    "Nhóm": rule['nhom'],
                    "Tên tài liệu": ten_tai_lieu,
                    "Mục đích": f"Chứng minh ({sentence[:40]}...)",
                    "Ghi chú (M/O)": ghi_chu
                })
                matched = True
                break
                

            
    return results

def extract_text_from_excel(filepath):
    """
    Quét qua tất cả các sheet trong file Excel, gộp các text lại phục vụ extract.
    """
    text_chunks = []
    try:
        xls = pd.ExcelFile(filepath)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            for col in df.columns:
                # Gắn tên cột như một dòng context (nếu là dạng text)
                if isinstance(col, str) and len(col) > 5:
                    text_chunks.append(col)
                # Parse các cell trong cột
                for val in df[col].dropna():
                    val_str = str(val).strip()
                    if len(val_str) > 5:
                        text_chunks.append(val_str)
    except Exception as e:
        print(f"Lỗi khi đọc file Excel {filepath}: {e}")
    
    return "\n".join(text_chunks)

def process_file(filepath, mapping_rules):
    ext = os.path.splitext(filepath)[1].lower()
    
    if ext in ['.xlsx', '.xls']:
        content = extract_text_from_excel(filepath)
    else:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(filepath, 'r', encoding='cp1252') as f:
                content = f.read()
    
    return process_text_content(content, mapping_rules)

def main():
    mapping_rules = load_mapping()
    
    files = glob.glob(os.path.join(INPUT_DIR, "*.txt")) \
          + glob.glob(os.path.join(INPUT_DIR, "*.xlsx")) \
          + glob.glob(os.path.join(INPUT_DIR, "*.xls"))
          
    files = [f for f in files if not os.path.basename(f).startswith("~$")]

    if not files:
        print("Không tìm thấy file hợp lệ (.txt, .xlsx, .xls) trong thư mục INPUT.")
        return

    all_results = []
    
    for fp in files:
        print(f"Đang xử lý: {fp}")
        rs = process_file(fp, mapping_rules)
        all_results.extend(rs)
        
    out_file = os.path.join(OUTPUT_DIR, "Standard_Checklist.csv")
    with open(out_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["STT", "Nhóm", "Tên tài liệu", "Mục đích", "Ghi chú (M/O)"])
        writer.writeheader()
        
        # Lọc trùng lặp dựa trên Tên tài liệu
        unique_results = []
        seen_docs = set()
        for row in all_results:
            doc_name = row["Tên tài liệu"]
            if doc_name not in seen_docs:
                seen_docs.add(doc_name)
                unique_results.append(row)
        
        # Cập nhật số thứ tự (tránh lỗi duplicate do nối file)
        for i, row in enumerate(unique_results):
            row["STT"] = i + 1
            writer.writerow(row)
            
    print("--------------------------------------------------")
    print(f"Đã xuất bảng checklist ({len(unique_results)} mục) tại {out_file}.")

if __name__ == '__main__':
    main()
