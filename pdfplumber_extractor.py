import pdfplumber
from pathlib import Path

def extract_text_pdfplumber(pdf_path: Path) ->str:
    """Best for structured PDFs and tables"""
    text=""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text=page.extract_text()
            if page_text:
                text +=page_text + "\n"

    return text            

if __name__ == "__main__":
    print("pdfplumber extractor loaded successfully")

    sample_pdf =Path("pdf_ka_path")
    extracted_text=extract_text_pdfplumber(sample_pdf)

    print(extracted_text[:500])

