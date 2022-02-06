from ctypes import windll, Structure, c_long, byref
from time import sleep
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]
def queryMousePosition():
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return { "x": pt.x, "y": pt.y}

if __name__ == "__main__":
    while True:
        print(queryMousePosition())
        sleep(0.1)
