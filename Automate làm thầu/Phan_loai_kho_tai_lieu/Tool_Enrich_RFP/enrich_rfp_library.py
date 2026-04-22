import sys
import pandas as pd
import re
import os
import string
from glob import glob

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# --- CAUTION: DO NOT MODIFY UNLESS NECESSARY ---
input_dir = r"Input_New_RFP"
library_dir = os.path.join(os.path.dirname(__file__), '..', 'Kho_Tai_Lieu', 'RFP_Library')
config_file = r"rfp_mapping_config.csv"

# Make sure Library Directory exists
if not os.path.exists(library_dir):
    print(f"Error: Khong tim thay thu muc Library: {library_dir}")
    exit(1)

if not os.path.exists(input_dir):
    os.makedirs(input_dir)
if not os.path.exists(config_file):
    print(f"Error: Khong tim thay file {config_file}")
    exit(1)

def col2num(col_str):
    """
    Chuyển dạng chữ A->0, B->1... 
    Đồng thời hỗ trợ điền thẳng số cột dạng 1-based (VD 1->0, 3->2).
    """
    col_str = str(col_str).strip()
    if col_str.isdigit():
        val = int(col_str)
        return val - 1 if val > 0 else 0
        
    num = 0
    for c in col_str:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num - 1 if num > 0 else 0

def clean_text(text):
    if pd.isna(text): return "[MISSING_DATA]"
    text = str(text).strip()
    
    # Ẩn danh tên Ngân hàng bằng Regex robust
    banks_regex = r'(?i)\b(LPBank|OCB|SeABank|MBBank|MB|Vietinbank|Vietcombank|Techcombank|VPBank|BIDV|Agribank|ACB|VIB|TPBank|Sacombank|HDBank)\b'
    text = re.sub(banks_regex, '[BANK_NAME]', text)
    
    # Normalize khoảng trắng cứng (newlines, tabs...)
    text = re.sub(r'\s+', ' ', text).strip()
    
    if not text:
        return "[MISSING_DATA]"
    return text

def categorize(req_text, sheet_hint=""):
    text = str(req_text).lower() + " " + str(sheet_hint).lower()
    
    if any(k in text for k in ['api', 'microservices', 'mã hóa', 'bảo mật', 'security', 'kafka', 'k8s', 'cloud', 'tích hợp', 'database', 'công nghệ', 'non functional', 'kiến trúc']):
        return "2__Kỹ_thuật__Technical"
    if any(k in text for k in ['vốn điều lệ', 'báo cáo tài chính kiểm toán', 'báo cáo tài chính năm', 'gpđkkd', 'bảo lãnh dự thầu', 'bảo lãnh bảo hành', 'bảo lãnh thực hiện hợp đồng', 'bảo lãnh tạm ứng', 'nda', 'giấy phép đăng ký kinh doanh']):
        return "3__Tài_chính___Pháp_lý"
    if any(k in text for k in ['hợp đồng tương tự', 'kinh nghiệm nhà thầu', 'kinh nghiệm triển khai', 'biên bản nghiệm thu', 'bbnt', ' cv ', ' pm ', ' ba ', 'thời gian triển khai dự án', 'project plan', 'năng lực triển khai', 'kế hoạch triển khai dự án']):
        return "4__Năng_lực_triển_khai"
    if any(k in text for k in ['tài liệu hướng dẫn', 'tài liệu kỹ thuật', 'đào tạo', 'vận hành hệ thống', 'bảo trì', 'cam kết sla', 'sla hỗ trợ', 'sla xử lý sự cố', 'support', 'chuyển giao', 'bảo hành']):
        return "5__Chuyển_giao___Đào_tạo"
    
    return "1__Nghiệp_vụ__Functional"

def map_group_to_filename(group_name):
    if "1__Nghi" in group_name: return "01_Functional_Answers.xlsx"
    if "2__K" in group_name: return "02_Technical_Answers.xlsx"
    if "3__T" in group_name: return "03_Legal_Answers.xlsx"
    if "4__N" in group_name: return "04_Deployment_Experience.xlsx"
    if "5__Chuy" in group_name: return "05_Training_Transfer.xlsx"
    return "00_Unknown_Answers.xlsx"

print(">> KHOI DONG PIPELINE ENRICHMENT <<\n")

# 1. Đọc Settings
configs = pd.read_csv(config_file).fillna("")
excel_files = glob(os.path.join(input_dir, "*.xlsx"))

if not excel_files:
    print(f"X Thu muc [{input_dir}] hien khong co file Excel moi nao. Dang thoat...")
    exit(0)

all_data = []

# 2. Extract Dữ liệu
for f_path in excel_files:
    f_name = os.path.basename(f_path)
    print(f"[*] Dang Phuc vu File: => {f_name}")
    
    # Tìm luật Config match cho file
    matched_configs = []
    for _, row in configs.iterrows():
        keyword = str(row['FileName_Keyword']).strip()
        if keyword == "" or keyword == ".*" or keyword.lower() in f_name.lower():
            matched_configs.append(row)
            
    if not matched_configs:
        print(f"  -> Bo qua: Khong co config CSV mapping nao match voi chuoi '{f_name}'")
        continue

    try:
        xls = pd.ExcelFile(f_path)
    except Exception as e:
        print(f"  -> Error: Khong doc duoc file {f_name}. Chi tiet: {e}")
        continue
        
    for sheet in xls.sheet_names:
        sheet_conf = None
        for r_conf in matched_configs:
            pat = str(r_conf['SheetName_Keyword']).strip()
            if pat == "" or pat == ".*" or pat.lower() in sheet.lower():
                sheet_conf = r_conf
                break
                
        if sheet_conf is None:
            continue
            
        print(f"  + Sheet '{sheet}': Bat dau quet...")
        req_col = col2num(sheet_conf['Col_Requirement'])
        resp_col = col2num(sheet_conf['Col_Response'])
        start_row_raw = str(sheet_conf['Start_Row']).strip()
        start_row = int(float(start_row_raw)) if (start_row_raw.replace('.','',1).isdigit()) else 1
        hint = str(sheet_conf['Tag_Hint'])
        
        try:
            df = pd.read_excel(xls, sheet_name=sheet, header=None)
            df = df.iloc[start_row-1:]  # 1-based index conversion
            
            # Dien thieu du lieu Merge Cells cho cot Yeu cau
            if req_col < len(df.columns):
                df.iloc[:, req_col] = df.iloc[:, req_col].ffill()
                
            count = 0
            for idx, row in df.iterrows():
                if req_col >= len(row) or resp_col >= len(row): continue
                req_val = row.iloc[req_col]
                resp_val = row.iloc[resp_col]
                
                if pd.isna(req_val) or str(req_val).strip() == "": continue
                
                req_clean = clean_text(req_val)
                resp_clean = clean_text(resp_val)
                cat = categorize(req_clean, sheet_hint=hint)
                
                # Human readable group logic
                human_cat = cat.split("__")[1].replace("_", " ") if "__" in cat else cat
                
                all_data.append({
                    "Ngân hàng": f_name.replace(".xlsx", ""),
                    "Tab": sheet,
                    "Nhóm": human_cat,
                    "Yêu cầu": req_clean,
                    "Diễn giải đáp ứng": resp_clean,
                    "_RawCat": cat # Field xai rieng
                })
                count += 1
            print(f"    => Nhap duoc {count} hanh vi (Rows).")
        except Exception as e:
            print(f"    => Error: Doc data {sheet} thet bai. Chi tiet: {e}")

# 3. Append & Deduplication vao Library
if not all_data:
    print("\n[!] Hoan thanh nhung khong co du lieu nao duoc thay moi.")
    exit()

print(f"\n>> GIAI DOAN MERGE (TRON DU LIEU VOI LIBRARY) <<")

new_df = pd.DataFrame(all_data)
mapping_group = {}

for idx, row in new_df.iterrows():
    dest = map_group_to_filename(row['_RawCat'])
    if dest not in mapping_group:
        mapping_group[dest] = []
    mapping_group[dest].append(row)

modified_files = 0
for target_excel, rows_list in mapping_group.items():
    cur_new_df = pd.DataFrame(rows_list)
    cur_new_df = cur_new_df.drop(columns=['_RawCat'])
    
    target_path = os.path.join(library_dir, target_excel)
    
    if os.path.exists(target_path):
        old_df = pd.read_excel(target_path)
        old_len_raw = len(old_df)
        # Phải dọn rác file cũ trước để không làm sai phép toán tính Added Amount
        old_df = old_df.drop_duplicates(subset=["Ngân hàng", "Yêu cầu", "Diễn giải đáp ứng"], keep="first")
        combined = pd.concat([old_df, cur_new_df], ignore_index=True)
        cleaned_old_duplicates = old_len_raw - len(old_df)
    else:
        cleaned_old_duplicates = 0
        combined = cur_new_df
        
    # Deduplicate logic: Check trùng cả Yêu cầu và Diễn giải
    before_len = len(combined)
    combined = combined.drop_duplicates(subset=["Ngân hàng", "Yêu cầu", "Diễn giải đáp ứng"], keep="first")
    after_len = len(combined)
    
    added_amount = len(cur_new_df) - (before_len - after_len)
    
    if added_amount > 0 or cleaned_old_duplicates > 0:
        combined.to_excel(target_path, index=False)
        modified_files += 1
        msg = f"  [OK] {target_excel}: Nhoi duoc them {added_amount} rows."
        if cleaned_old_duplicates > 0:
            msg += f" (Dong thoi auto-clean {cleaned_old_duplicates} dong rac trung he thong cu)."
        print(msg)
    else:
        print(f"  [SKIP] {target_excel}: Data nay dang ton tai 100% tren he thong (bi trung).")

print(f"\n=> VANG: PIPELINE DA XU LY THANH CONG. Da lam giau duoc vao {modified_files} file tang 2.")
