
import os
import shutil

if __name__ == "__main__":
    path = str(os.getcwd()) + "\Documents"
    source = str(os.getcwd()) + "\ChromeRivals Makro"
    dest = shutil.move(source, path, copy_function = shutil.copytree)
