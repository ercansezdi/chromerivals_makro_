import ctypes
from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
from time import sleep


import win32api
import win32con 

class movemont:
    def click_button():
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
    

    def doubleClick():
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)

    def move(X, Y):
        ctypes.windll.user32.SetCursorPos(X, Y)

    def click_move(x1,y1,x2,y2):
        ctypes.windll.user32.SetCursorPos(x1, y1)
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
        ctypes.windll.user32.SetCursorPos(x2, y2)
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

    def queryMousePosition():
	    pt = POINT()
	    windll.user32.GetCursorPos(byref(pt))
	    return { "x": pt.x, "y": pt.y}
    def scroll_up():
        for _ in range(abs(40)):
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, win32con.WHEEL_DELTA, 0)

class tkinterGui(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("ToolBox")
        
        self.gui()



    def gui(self):

        
        self.movement = movemont
       
        self.row1_column1 = [810,560] #ilk satir sutun adres
        self.row1_column1_disp = [640,710]
        self.trash_all_accept = [1000,550] #hepsini seç
        self.trash_accept = [930,575] # onayla
        self.dissolition_accept = [1125,750]
        self.dissolition_accept_v = [1190,750]
        self.dissolition_panel = [1150,650]


        self.token_panel = [1200,780]
        self.token_start = [1170,840]
        self.token_accept = [1240,840]

        self.trash = [1090,765] # trash icon

        self.deleteItemFrame = Frame(self.parent)
        self.deleteItemFrame.grid(row=0,column=0)
        self.parent.geometry("300x100")


        self.delete_item_canvas = Canvas(self.deleteItemFrame, width=310, height=100)
        img = ImageTk.PhotoImage(Image.open('file\error.png').resize((310, 100), Image.ANTIALIAS))  #
        self.delete_item_canvas.background = img  #
        bg_pic = self.delete_item_canvas.create_image(0, 0, anchor=NW, image=img)
        self.delete_item_canvas.grid(row=0, column=0, rowspan=310, columnspan=100)

        self.satir = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=5)
        self.satir.insert(0,"Row")
        self.sutun = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=7)
        self.sutun.insert(0,"Column")
        self.numbef_of_fragmented_item = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=7)
        self.numbef_of_fragmented_item.insert(0,"Number")
        fragmented_item_button = Button(self.deleteItemFrame, text = "Dissolution", command = self.dissolution_item_func)

        self.satir2 = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=5)
        self.satir2.insert(0,"Row")
        self.sutun2 = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=7)
        self.sutun2.insert(0,"Column")
        self.numbef_of_fragmented_item2 = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=7)
        self.numbef_of_fragmented_item2.insert(0,"Number")
        fragmented_item_button2 = Button(self.deleteItemFrame, text = "Delete", command = self.delete_item_func)


        self.satir3 = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=5)
        self.satir3.insert(0,"Row")
        self.sutun3 = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=7)
        self.sutun3.insert(0,"Column")
        self.numbef_of_fragmented_item3 = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=7)
        self.numbef_of_fragmented_item3.insert(0,"Number")
        fragmented_item_button3 = Button(self.deleteItemFrame, text = "Başla", command = self.break_a_token)

        y=0
        self.delete_item_canvas.create_window(5, 5+y, anchor=NW, window=self.satir)
        self.delete_item_canvas.create_window(47, 5+y, anchor=NW, window=self.sutun)
        self.delete_item_canvas.create_window(103, 5+y, anchor=NW, window=self.numbef_of_fragmented_item)
        self.delete_item_canvas.create_window(160, 5+y, anchor=NW, window=fragmented_item_button)
        y=25
        self.delete_item_canvas.create_window(5, 5+y, anchor=NW, window=self.satir2)
        self.delete_item_canvas.create_window(47, 5+y, anchor=NW, window=self.sutun2)
        self.delete_item_canvas.create_window(103, 5+y, anchor=NW, window=self.numbef_of_fragmented_item2)
        self.delete_item_canvas.create_window(160, 5+y, anchor=NW, window=fragmented_item_button2)

        y=50
        self.delete_item_canvas.create_window(5, 5+y, anchor=NW, window=self.satir3)
        self.delete_item_canvas.create_window(47, 5+y, anchor=NW, window=self.sutun3)
        self.delete_item_canvas.create_window(103, 5+y, anchor=NW, window=self.numbef_of_fragmented_item3)
        self.delete_item_canvas.create_window(160, 5+y, anchor=NW, window=fragmented_item_button3)





    def break_a_token(self):
        if self.satir3.get().isnumeric() and self.sutun3.get().isnumeric() and self.numbef_of_fragmented_item3.get().isnumeric():
            satir = int(self.satir3.get())
            sutun = int(self.sutun3.get())
            number = int(self.numbef_of_fragmented_item3.get())
            for i in range(0,number):
                self.movement.move(self.row1_column1_disp[0] +(sutun -1)*32,self.row1_column1_disp[1] + (satir-1)*32)
                sleep(0.1)
                self.movement.scroll_up()
                sleep(0.5)
                self.movement.click_move(self.row1_column1_disp[0] +(sutun -1)*32,self.row1_column1_disp[1] + (satir-1)*32,self.token_panel[0],self.token_panel[1])
                sleep(0.1)
                self.movement.move(self.token_start[0],self.token_start[1])
                self.movement.click_button()
                sleep(4.5)
                self.movement.move(self.token_accept[0],self.token_accept[1])
                self.movement.click_button()

    def dissolution_item_func(self):
        
        if self.satir.get().isnumeric() and self.sutun.get().isnumeric() and self.numbef_of_fragmented_item.get().isnumeric():
            satir = int(self.satir.get())
            sutun = int(self.sutun.get())
            number = int(self.numbef_of_fragmented_item.get())
            for i in range(0,number):
                self.movement.click_move(self.row1_column1_disp[0] +(sutun -1)*32,self.row1_column1_disp[1] + (satir-1)*32,self.dissolition_panel[0],self.dissolition_panel[1])
                sleep(0.1)
                self.movement.move(self.dissolition_accept[0],self.dissolition_accept[1])
                self.movement.click_button()
                sleep(2)
                self.movement.move(self.dissolition_accept_v[0],self.dissolition_accept_v[1])
                self.movement.click_button()
                
                    

    def delete_item_func(self):
        print(1)
        if self.satir2.get().isnumeric() and self.sutun2.get().isnumeric() and self.numbef_of_fragmented_item2.get().isnumeric():
            satir = int(self.satir2.get())
            sutun = int(self.sutun2.get())
            number = int(self.numbef_of_fragmented_item2.get())
            for i in range(0,number):
                self.movement.move(self.row1_column1[0] +(sutun -1)*32,self.row1_column1[1] + (satir-1)*32)

                self.movement.scroll_up()
                sleep(0.1)
                self.movement.click_move(self.row1_column1[0] +(sutun -1)*32,self.row1_column1[1] + (satir-1)*32,self.trash[0],self.trash[1])
                self.movement.move(self.trash_all_accept[0],self.trash_all_accept[1])
                sleep(0.1)
                self.movement.click_button()
                self.movement.click_button()
                self.movement.move(self.trash_accept[0],self.trash_accept[1])
                sleep(0.1)
                self.movement.click_button()
                self.movement.move(self.trash_accept[0],self.trash_accept[1]-5)
                sleep(0.1)
                self.movement.click_button()


if __name__ == "__main__":
    root = Tk()
    root.call('tk', 'scaling', 1.0)
    run = tkinterGui(root)
    root.mainloop()
