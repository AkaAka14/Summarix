import PyPDF2
import docx

def extract_text_from_file(file):
    if file.filename.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        return "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    elif file.filename.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join(para.text for para in doc.paragraphs)
    else:
        return file.read().decode("utf-8")
s