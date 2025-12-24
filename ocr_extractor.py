from pdf2image import convert_from_path
import pytesseract
from pathlib import Path

def extract_text_ocr(pdf_path: Path) -> str:
    images=convert_from_path(pdf_path)
    text=""

    for img in images:
        text +=pytesseract.image_to_string(img)

    return text    

if __name__ == "__main__":
    print("OCR extractor loaded successfully")

    sample_pdf=Path("scan.pdf")
    extracted_text= extract_text_ocr(sample_pdf)

    print(extracted_text[:500])
