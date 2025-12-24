import fitz  # PyMuPDF


def extract_text(pdf_path: str) -> str:
    doc = fitz.open(r"C:\Users\Adarsh Singh\OneDrive\Desktop\Python_template\Text_Extraction\health_report.pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    return text


if __name__ == "__main__":
    print("Radhe Radhe")
    text = extract_text("health_report.pdf")
    print(text[:500])  # print only first 500 chars
