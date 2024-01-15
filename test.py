import cv2 
import pytesseract
import pyautogui
from PIL import Image

kayit_adresi = "C:/Users/trforever/Documents/GitHub/chromerivals_makro_/image/"

def take_screenshot(ek_adi = "P"):
    Screenshot = pyautogui.screenshot()
    Screenshot.save(kayit_adresi + "screenshot.png")
    crop_image(kayit_adresi, (0, 0, 100, 100), 'cropped.png',ek_adi)
def crop_image(image_path, coords, saved_location, ek_adi = "P"):
    image_obj = Image.open(image_path + "screenshot.png")
    cropped_image = image_obj.crop(coords)
    cropped_image.save(image_path + "cropped_.png")
    image_to_string(image_path + "cropped_.png",ek_adi)
def image_to_string(image_path,ek_adi = "P"):
    image = cv2.imread(image_path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(image)
    print(text)
    if ek_adi == "P":
        pass
    else:
        pass

    return text

if __name__ == '__main__':
    bulunan_ek = take_screenshot()
    print(bulunan_ek)