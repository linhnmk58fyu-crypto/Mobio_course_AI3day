import zipfile
import xml.etree.ElementTree as ET
import sys

def get_docx_text(path):
    try:
        document = zipfile.ZipFile(path)
        xml_content = document.read('word/document.xml')
        document.close()
        tree = ET.XML(xml_content)
        
        WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        PARA = WORD_NAMESPACE + 'p'
        TEXT = WORD_NAMESPACE + 't'
        
        paragraphs = []
        for paragraph in tree.iter(PARA):
            texts = [node.text
                     for node in paragraph.iter(TEXT)
                     if node.text]
            if texts:
                paragraphs.append(''.join(texts))
        return '\n'.join(paragraphs)
    except Exception as e:
        return str(e)

file_path = "c:\\Users\\linhn\\Khoa_Hoc_Antigravity\\Dự án RFP\\PD - Use case Phản hồi RFP.docx"
text = get_docx_text(file_path)

with open("c:\\Users\\linhn\\Khoa_Hoc_Antigravity\\Dự án RFP\\output.txt", "w", encoding="utf-8") as f:
    f.write(text)
