from paddleocr import PaddleOCR
from pathlib import Path

def Extract_paddle_OCR(image_path: Path) ->str:
    """
    Extract text from an image using PaddleOCR.
    Best for high-accuracy OCR on scanned documents.
    """
    ocr= PaddleOCR(use_angle_cls=True,lang="en")
    result=ocr.ocr(str(image_path))
    text=""
    for line in result:
        text += line[1][0]+ "\n"

    return text    

if __name__ == "__main__":
    print("paddle OCR loaded successfully")

    sample_image=Path("page.png")
    extracted_text=Extract_paddle_OCR(sample_image)

    print(extracted_text[:400])
