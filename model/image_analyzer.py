from PIL import Image
import pytesseract
import os

# =========================
# AUTO DETECT TESSERACT
# =========================

possible_paths = [

    r"C:\Program Files\Tesseract-OCR\tesseract.exe",

    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
]

for path in possible_paths:

    if os.path.exists(path):

        pytesseract.pytesseract.tesseract_cmd = path

        break


# =========================
# OCR FUNCTION
# =========================

def extract_text_from_image(image_path):

    try:

        image = Image.open(image_path)

        text = pytesseract.image_to_string(image)

        if text.strip() == "":

            return (
                "No readable text detected in image."
            )

        return text

    except Exception as e:

        return (
            f"Image analysis failed: {str(e)}"
        )