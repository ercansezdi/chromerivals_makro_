import os


if __name__ == "__main__":
    os.system("pip install --upgrade pip")
    libs = ["keyboard", "pillow", "pymongo", "pymongo[srv]", "opencv-python", "pytesseract","PyAutoGUI","pyperclip"]
    for i in libs:
        os.system("pip install " + i)

    print("OK")
