import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Users\Jignesh\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image
img = Image.open('Screenshot 2024-01-14 191638.png')
text = tess.image_to_string(img)

