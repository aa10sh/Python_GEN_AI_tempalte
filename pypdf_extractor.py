from pypdf import PdfReader
from pathlib import Path

def extract_text_pypdf(pdf_path: Path) ->str:
     """
    Extract text from a PDF using pypdf.
    Best for simple, text-based PDFs.
    """
     reader=PdfReader(pdf_path)
     text="" 

     for page in reader.pages:
          page_text=page.extract_text()
          if page_text:
               text+=page_text + "\n"

     return text     
     

if __name__ == "__main__":
    print("pypdf extarctor loaded succesfuly")

    sample_pdf=Path("pdf_ka_path")
    extracted_text=extract_text_pypdf(sample_pdf)

    print(extracted_text[:400])




