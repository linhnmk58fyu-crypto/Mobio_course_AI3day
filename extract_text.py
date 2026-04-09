import zipfile
import xml.etree.ElementTree as ET

def get_docx_text(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = ET.fromstring(xml_content)
    
    # Define the namespaces used in the document
    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    }
    
    paragraphs = []
    for paragraph in tree.findall('.//w:p', namespaces):
        texts = paragraph.findall('.//w:t', namespaces)
        if texts:
            paragraphs.append(''.join([t.text for t in texts]))
    
    return '\n'.join(paragraphs)

if __name__ == "__main__":
    import sys
    path = "Bidding Playbook.docx"
    text = get_docx_text(path)
    with open("playbook_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Extracted text to playbook_text.txt")
