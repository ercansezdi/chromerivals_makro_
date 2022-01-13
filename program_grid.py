#!/usr/bin/env python
 # -*- coding: utf-8 -*-
from tkinter import *
import threading
from tkinter.messagebox import showinfo
import os
import tkinter.ttk
from tkinter import ttk
import datetime
from time import sleep
import sqlite3
import configparser
from tkinter import messagebox
import random
import subprocess
import pyperclip
from PIL import Image, ImageTk, ImageFont, ImageDraw
import keyboard
import ctypes
import pymongo
import pyautogui
import cv2
import pytesseract
from functools import partial
import requests

class tkinterGui(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("ToolBox")
        
        self.loading_variables_set()
        
    def InitGui(self):
       

        self.canvas = Canvas(self.chrome_search_attachment, width=630, height=250)
        img = ImageTk.PhotoImage(Image.open('file\chrome_wallpaper.png').resize((630, 250), Image.ANTIALIAS))  #
        self.canvas.background = img  #
        bg_pic = self.canvas.create_image(0, 0, anchor=NW, image=img)
        self.canvas.grid(row=0, column=0, rowspan=630, columnspan=250)

        self.treeBox = FancyListbox(self.idPasswd, font=("Helvatica bold", 12), justify=CENTER)
        self.treeBox.grid(row=0, column=0, rowspan=4, columnspan=1, ipady=40)
        self.treeBox_id = FancyListbox(self.idPasswd, font=("Helvatica bold", 12), justify=CENTER)
        self.treeBox_id.grid(row=0, column=1, rowspan=4, columnspan=2, ipadx=50, ipady=40)
        self.treeBox_passwd = FancyListbox(self.idPasswd, font=("Helvatica bold", 12), justify=CENTER)
        self.treeBox_passwd.grid(row=0, column=3, rowspan=4, columnspan=3, ipadx=50, ipady=40)
        self.id = Entry(self.idPasswd, font="Helvatica 12 bold")
        self.id.grid(row=4, column=0, columnspan=2, ipadx=50, padx=1)
        self.id.insert(0, self.info[self.language]["username"])
        self.id.bind("<Button-1>", self.clear_directory_id)
        self.passwd = Entry(self.idPasswd, font="Helvatica 12 bold")
        self.passwd.grid(row=4, column=2, columnspan=2, ipadx=50)
        self.passwd.insert(0, self.info[self.language]["passwd"])
        self.passwd.bind("<Button-1>", self.clear_directory_passwd)

        self.add = Button(self.idPasswd, text=self.info[self.language]["add"], command=self.add_data)
        self.add.grid(row=4, column=4, ipadx=20, pady=2)




        # Search attachment

        self.chrome_combo_ekList = ttk.Combobox(self.chrome_search_attachment, width=24, textvariable=self.search_combo)
        self.chrome_combo_ekList['values'] = (self.info[self.language]["armor_accuracy"],
                                              self.info[self.language]["armor_experience_rate"],
                                              self.info[self.language]["armor_drop_rate"],
                                              #self.info[self.language]["armor_pierce"],
                                              self.info[self.language]["weapon_accuracy"],
                                              self.info[self.language]["weapon_ra_accuracy"],
                                              self.info[self.language]["weapon_ra_attack"],
                                              self.info[self.language]["weapon_weight"],
                                              #self.info[self.language]["weapon_pierce"],
                                              self.info[self.language]["pet"])
        self.get_fixes = Button(self.chrome_search_attachment, text=self.info[self.language]["show_attachment"], font=("Helvatica bold", 10),bg="purple",
                                 command=self.set_fixes)
        self.ettac_list = Listbox(self.chrome_search_attachment,font = ("Helvatica bold", 12),selectmode='multiple')

        self.search_add_p = Button(self.chrome_search_attachment,text = "P>",font = ("Helvatica bold", 10),command=self.ettac_add_p)
        self.search_remove_p = Button(self.chrome_search_attachment, text = "P<",font = ("Helvatica bold", 10),command = self.ettac_remove_p)

        self.search_add_s = Button(self.chrome_search_attachment,text = "S>",font = ("Helvatica bold", 10),command=self.ettac_add_s)
        self.search_remove_s = Button(self.chrome_search_attachment, text = "S<",font = ("Helvatica bold", 10),command = self.ettac_remove_s)




        self.search_ettac_list_name = Label(self.chrome_search_attachment, text = self.info[self.language]["prefixes_to_search"],font = ("Helvatica bold", 12),bg = "red")
        self.search_ettac_list = Listbox(self.chrome_search_attachment,font = ("Helvatica bold", 12),selectmode='multiple')
        self.search_ettac_list_name_s = Label(self.chrome_search_attachment, text = self.info[self.language]["suffix_to_search"],font = ("Helvatica bold", 12),bg = "red")
        self.search_ettac_list_2 = Listbox(self.chrome_search_attachment,font = ("Helvatica bold", 12),selectmode='multiple')

        self.coming_ettac = Label(self.chrome_search_attachment, bg="green", textvariable=self.ettac_counter_text,font = ("Helvatica bold", 12))
        self.coming_ettac_list = Listbox(self.chrome_search_attachment, font=("Helvatica bold", 12))

        self.number_of_ettac_P = Entry(self.chrome_search_attachment,font = ("Helvatica bold", 13),bg="green",width=5)
        self.number_of_ettac_P.insert(0,"0")

        self.number_of_ettac_S = Entry(self.chrome_search_attachment, font=("Helvatica bold", 13), bg="green",width=5)
        self.number_of_ettac_S.insert(0, "0")
        self.ettac_counter_text.set(self.info[self.language]["fixes"] + " (" + str(self.ettac_counter) + ")")

        self.search_start_stop = Button(self.chrome_search_attachment, text= self.info[self.language]["run"],font = ("Helvatica bold", 12),command= self.ettac_check)
        self.ettac_P = Checkbutton(self.chrome_search_attachment, text="P", variable=self.checkVars_1,onvalue=1, offvalue=0)
        self.ettac_S = Checkbutton(self.chrome_search_attachment, text="S", variable=self.checkVars_2,onvalue=1, offvalue=0)
        

        #Menu
        self.menubar = Menu(self.parent)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = self.info[self.language]["apps"], menu = self.filemenu)
        self.filemenu.add_command(label = "ID-Pass", command = self.run_passworDirectory)
        self.filemenu.add_command(label = "Search", command = self.search_ek)
        #self.filemenu.add_command(label = "Delete Item", command = self.delete_items)
        self.filemenu.add_separator()

        self.help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label =  self.info[self.language]["language"], menu = self.help_menu)
        if self.language == "turkish":
            self.help_menu.add_command(label = ("→"+self.info["turkish"]["local_language"]+"←"), command = partial(self.change_language, "turkish"))
        else:
            self.help_menu.add_command(label = (self.info["turkish"]["local_language"]), command = partial(self.change_language, "turkish"))
        if self.language == "english":
            self.help_menu.add_command(label = "→"+self.info["english"]["local_language"]+"←", command = partial(self.change_language, "english"))
        else:
            self.help_menu.add_command(label = self.info["english"]["local_language"], command = partial(self.change_language, "english"))


        self.resolition_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label =  self.info[self.language]["resolition"], menu = self.resolition_menu)

        if self.resolition == "1920x1080":
            self.resolition_menu.add_command(label = "→1920x1080←", command = partial(self.change_resolition, "1920x1080"))
        else:
            self.resolition_menu.add_command(label = "1920x1080", command = partial(self.change_resolition, "1920x1080"))
        if self.resolition == "1600x900":
            self.resolition_menu.add_command(label = "→1600x900←", command = partial(self.change_resolition, "1600x900"))
        else:
            self.resolition_menu.add_command(label = "1600x900", command = partial(self.change_resolition, "1600x900"))
        if self.resolition == "1440x900":
            self.resolition_menu.add_command(label = "→1440x900←", command = partial(self.change_resolition, "1440x900"))
        else:
            self.resolition_menu.add_command(label = "1440x900", command = partial(self.change_resolition, "1440x900"))
        if self.resolition == "1280x800":
             self.resolition_menu.add_command(label = "→1280x800←", command = partial(self.change_resolition, "1280x800"))
        else:
            self.resolition_menu.add_command(label = "1280x800", command = partial(self.change_resolition, "1280x800"))
        

        self.help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label =  self.info[self.language]["help"], menu = self.help_menu)
        self.help_menu.add_command(label = self.info[self.language]["about"], command = self.about)
        self.help_menu.add_command(label = self.info[self.language]["check_update"], command = self.check_update)


        root.config(menu=self.menubar)



        self.canvas.create_window(10, 10, anchor=NW, window=self.chrome_combo_ekList)
        self.canvas.create_window(175, 10, anchor=NW, window=self.search_ettac_list_name)
        self.canvas.create_window(325,10, anchor=NW, window=self.search_ettac_list_name_s)
        self.canvas.create_window(490, 10, anchor=NW, window=self.coming_ettac)

        self.canvas.create_window(10, 40, anchor=NW, window=self.ettac_list)
        self.canvas.create_window(160, 40, anchor=NW, window=self.search_ettac_list)
        self.canvas.create_window(310, 40, anchor=NW, window=self.search_ettac_list_2)
        self.canvas.create_window(460, 40, anchor=NW, window=self.coming_ettac_list)

        self.canvas.create_window(165, 205, anchor=NW, window=self.ettac_P)
        self.canvas.create_window(205, 206, anchor=NW, window=self.number_of_ettac_P)
        self.canvas.create_window(250, 205, anchor=NW, window=self.search_add_p)
        self.canvas.create_window(275, 205,anchor=NW, window=self.search_remove_p)

        self.canvas.create_window(315, 205, anchor=NW, window=self.ettac_S)
        self.canvas.create_window(355, 206, anchor=NW, window=self.number_of_ettac_S)
        self.canvas.create_window(400, 205, anchor=NW, window=self.search_add_s)
        self.canvas.create_window(425, 205, anchor=NW, window=self.search_remove_s)

        self.canvas.create_window(50, 205, anchor=NW, window=self.get_fixes)
        self.canvas.create_window(510, 205, anchor=NW, window=self.search_start_stop)
        
                #Dissolition and delete item
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

  

  
        self.search_ek()
    def variables(self):
        self.path = "file\\"
        self.info = configparser.ConfigParser()
        self.info.read(self.path + "config.ini")
        self.idPasswd = Frame(self.parent)
        self.deleteItemFrame = Frame(self.parent)
        self.chrome_idPass_Frame = Frame(self.parent)
        self.chrome_search_attachment = Frame(self.parent)
        self.checkVars_1 = IntVar()
        self.checkVars_2 = IntVar()
        self.search_combo = StringVar()

        self.mainFrame = Frame(self.parent)
        self.table_builder_frame = Frame(self.parent)
        self.mainFrame.grid(row=0, column=0)

        self.click = [False, False]
        self.database = database()
        self.database.create()
        self.ara = search()
        self.movement = movemont
        self.sayac = 0
        self.login = True
        
        self.language = self.info["info"]["language"]
        self.resolition = self.info["info"]["resolition"]

        


        
        self.Psilme = [self.info[self.resolition]["Psilme"].split(",")[0],self.info[self.resolition]["Psilme"].split(",")[1]] 
        self.Pbasma = [self.info[self.resolition]["Pbasma"].split(",")[0],self.info[self.resolition]["Pbasma"].split(",")[1]]
        self.Ssilme = [self.info[self.resolition]["Ssilme"].split(",")[0],self.info[self.resolition]["Ssilme"].split(",")[1]]
        self.Sbasma = [self.info[self.resolition]["Sbasma"].split(",")[0],self.info[self.resolition]["Sbasma"].split(",")[1]]
        self.silah = [self.info[self.resolition]["silah"].split(",")[0],self.info[self.resolition]["silah"].split(",")[1]] 
        self.onay = [self.info[self.resolition]["onay"].split(",")[0],self.info[self.resolition]["onay"].split(",")[1]] 


        self.trash = [self.info[self.resolition]["trash"].split(",")[0],self.info[self.resolition]["trash"].split(",")[1]] 
        self.row1_column1 = [self.info[self.resolition]["row1_column1"].split(",")[0],self.info[self.resolition]["row1_column1"].split(",")[1]] 
        self.row1_column1_disp = [self.info[self.resolition]["row1_column1_disp"].split(",")[0],self.info[self.resolition]["row1_column1_disp"].split(",")[1]]
        self.trash_all_accept = [self.info[self.resolition]["trash_all_accept"].split(",")[0],self.info[self.resolition]["trash_all_accept"].split(",")[1]] 
        self.trash_accept = [self.info[self.resolition]["trash_accept"].split(",")[0],self.info[self.resolition]["trash_accept"].split(",")[1]]
        self.dissolition_accept = [self.info[self.resolition]["dissolition_accept"].split(",")[0],self.info[self.resolition]["dissolition_accept"].split(",")[1]]
        self.dissolition_accept_v = [self.info[self.resolition]["dissolition_accept_v"].split(",")[0],self.info[self.resolition]["dissolition_accept_v"].split(",")[1]]
        self.dissolition_panel = [self.info[self.resolition]["dissolition_panel"].split(",")[0],self.info[self.resolition]["dissolition_panel"].split(",")[1]]





        
        self.islem = [False, False]
        self.var = IntVar()
        self.autoBuff_tick = False
        self.ch_loop_exit = True
        self.attec_array = []
        self.ettac_counter_text = StringVar()
        self.ettac_counter = 0


    


    def donothing(self):
        pass
    def check_update(self):
        if int(self.info["info"]["version"]) < 10:
            link = self.info["info"]["update_link"]+"version_v_0"+str(int( self.info["info"]["version"])+1) + ".zip"
        else:
                link = self.info["info"]["update_link"]+"version_v_"+str(int( self.info["info"]["version"])+1) + ".zip"
        print(link)
        sorgu = requests.head(link, allow_redirects=True)

        if str(sorgu) == "<Response [200]>":
            MsgBox = messagebox.askquestion(self.info[self.language]["notice_4"], self.info[self.language]["notice_14"],
                                        icon='warning')
            if MsgBox ==self.info[self.language]["yes"]:
                 if int(self.info["info"]["version"]) < 10:
                    self.info['info']['version'] = "0"+str(int( self.info["info"]["version"])+1)
                 else:
                    self.info['info']['version'] = str(int( self.info["info"]["version"])+1)
                    with open('file\config.ini', 'w') as configfile:
                        self.info.write(configfile)
                #and download 
        else:
            showinfo(self.info[self.language]["notice_4"], self.info[self.language]["notice_15"])


    def about(self):
        pass
    def change_resolition(self,resoliton):
        self.resolition = resoliton
        self.info['info']['resolition'] = resoliton
        with open('file\config.ini', 'w') as configfile:
            self.info.write(configfile)
        self.Psilme = [self.info[self.resolition]["Psilme"].split(",")[0],self.info[self.resolition]["Psilme"].split(",")[1]] 
        self.Pbasma = [self.info[self.resolition]["Pbasma"].split(",")[0],self.info[self.resolition]["Pbasma"].split(",")[1]]
        self.Ssilme = [self.info[self.resolition]["Ssilme"].split(",")[0],self.info[self.resolition]["Ssilme"].split(",")[1]]
        self.Sbasma = [self.info[self.resolition]["Sbasma"].split(",")[0],self.info[self.resolition]["Sbasma"].split(",")[1]]
        self.silah = [self.info[self.resolition]["silah"].split(",")[0],self.info[self.resolition]["silah"].split(",")[1]] 
        self.onay = [self.info[self.resolition]["onay"].split(",")[0],self.info[self.resolition]["onay"].split(",")[1]] 


        self.trash = [self.info[self.resolition]["trash"].split(",")[0],self.info[self.resolition]["trash"].split(",")[1]] 
        self.row1_column1 = [self.info[self.resolition]["row1_column1"].split(",")[0],self.info[self.resolition]["row1_column1"].split(",")[1]] 
        self.row1_column1_disp = [self.info[self.resolition]["row1_column1_disp"].split(",")[0],self.info[self.resolition]["row1_column1_disp"].split(",")[1]]
        self.trash_all_accept = [self.info[self.resolition]["trash_all_accept"].split(",")[0],self.info[self.resolition]["trash_all_accept"].split(",")[1]] 
        self.trash_accept = [self.info[self.resolition]["trash_accept"].split(",")[0],self.info[self.resolition]["trash_accept"].split(",")[1]]
        self.dissolition_accept = [self.info[self.resolition]["dissolition_accept"].split(",")[0],self.info[self.resolition]["dissolition_accept"].split(",")[1]]
        self.dissolition_accept_v = [self.info[self.resolition]["dissolition_accept_v"].split(",")[0],self.info[self.resolition]["dissolition_accept_v"].split(",")[1]]
        self.dissolition_panel = [self.info[self.resolition]["dissolition_panel"].split(",")[0],self.info[self.resolition]["dissolition_panel"].split(",")[1]]
        self.update_language()

    def update_language(self):
        self.menubar.delete(0, 'end')
        self.menubar = Menu(self.parent)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = self.info[self.language]["apps"], menu = self.filemenu)
        self.filemenu.add_command(label = "ID-Pass", command = self.run_passworDirectory)
        self.filemenu.add_command(label = "Search", command = self.search_ek)
        self.filemenu.add_command(label = "Delete Item", command = self.delete_items)
        self.filemenu.add_separator()

        self.help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label =  self.info[self.language]["language"], menu = self.help_menu)
        if self.language == "turkish":
            self.help_menu.add_command(label = ("→"+self.info["turkish"]["local_language"]+"←"), command = partial(self.change_language, "turkish"))
        else:
            self.help_menu.add_command(label = (self.info["turkish"]["local_language"]), command = partial(self.change_language, "turkish"))
        if self.language == "english":
            self.help_menu.add_command(label = "→"+self.info["english"]["local_language"]+"←", command = partial(self.change_language, "english"))
        else:
            self.help_menu.add_command(label = self.info["english"]["local_language"], command = partial(self.change_language, "english"))

        self.resolition_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label =  self.info[self.language]["resolition"], menu = self.resolition_menu)
        if self.resolition == "1920x1080":
            self.resolition_menu.add_command(label = "→1920x1080←", command = partial(self.change_resolition, "1920x1080"))
        else:
            self.resolition_menu.add_command(label = "1920x1080", command = partial(self.change_resolition, "1920x1080"))

        if self.resolition == "1600x900":
            self.resolition_menu.add_command(label = "→1600x900←", command = partial(self.change_resolition, "1600x900"))
        else:
            self.resolition_menu.add_command(label = "1600x900", command = partial(self.change_resolition, "1600x900"))

        if self.resolition == "1440x900":
            self.resolition_menu.add_command(label = "→1440x900←", command = partial(self.change_resolition, "1440x900"))
        else:
            self.resolition_menu.add_command(label = "1440x900", command = partial(self.change_resolition, "1440x900"))
        if self.resolition == "1280x800":
             self.resolition_menu.add_command(label = "→1280x800←", command = partial(self.change_resolition, "1280x800"))
        else:
            self.resolition_menu.add_command(label = "1280x800", command = partial(self.change_resolition, "1280x800"))

        self.help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label =  self.info[self.language]["help"], menu = self.help_menu)
        self.help_menu.add_command(label = self.info[self.language]["about"], command = self.donothing)
        self.help_menu.add_command(label = self.info[self.language]["check_update"], command = self.check_update)
        root.config(menu=self.menubar)
        self.parent.title("Toolbox")
        self.id.delete(0, END)
        self.id.insert(0, self.info[self.language]["username"])
        self.passwd.delete(0, END)
        self.passwd.insert(0, self.info[self.language]["passwd"])
        self.add.config(text = self.info[self.language]["add"])
        self.chrome_combo_ekList.set('')
        self.chrome_combo_ekList['values'] = (self.info[self.language]["armor_accuracy"],
                                              self.info[self.language]["armor_experience_rate"],
                                              self.info[self.language]["armor_drop_rate"],
                                              self.info[self.language]["armor_pierce"],
                                              self.info[self.language]["weapon_accuracy"],
                                              self.info[self.language]["weapon_ra_accuracy"],
                                              self.info[self.language]["weapon_ra_attack"],
                                              self.info[self.language]["weapon_weight"],
                                              self.info[self.language]["weapon_pierce"],
                                              self.info[self.language]["pet"])
      
        self.get_fixes.config(text = self.info[self.language]["show_attachment"])
        

        self.search_ettac_list_name.config(text = self.info[self.language]["prefixes_to_search"])
        self.search_ettac_list_name_s.config(text = self.info[self.language]["suffix_to_search"])
        self.ettac_counter_text.set(self.info[self.language]["fixes"] + " (" + str(self.ettac_counter) + ")")

        self.search_start_stop.config(text= self.info[self.language]["run"])
    def loading_screen(self):
        self.loading_canvas = Canvas(self.loading_frame, width=310, height=100)
        img = ImageTk.PhotoImage(Image.open('file\error.png').resize((310, 100), Image.ANTIALIAS))  #
        self.loading_canvas.background = img  #
        bg_pic = self.loading_canvas.create_image(0, 0, anchor=NW, image=img)
        self.loading_canvas.grid(row=0, column=0, rowspan=310, columnspan=100)
        progress = ttk.Progressbar(self.loading_canvas, orient = HORIZONTAL,length = 250, mode = 'determinate')
        percent_text = Label(self.loading_frame, textvariable= self.percent_textvar, font =("Helvatica",12))
        uuid = Label(self.loading_frame, textvariable= self.uuid, font =("Helvatica",12))
        copy = Button(self.loading_frame, text=  self.info[self.language]["copy"], font =("Helvatica",10),command=self.copy_uuid)
        warning1 = Label(self.loading_frame, text=  self.info[self.language]["notice_1"], font =("Helvatica",12))
        warning2 = Label(self.loading_frame, text=  self.info[self.language]["notice_2"], font =("Helvatica",12))
        if self.return_mongodb():
            self.loading_variables_destroy()
        else:
            self.parent.geometry("310x100")
            self.loading_canvas.create_window(10, 10, anchor=NW, window=warning1)
            self.loading_canvas.create_window(10, 35, anchor=NW, window=warning2)
            self.loading_canvas.create_window(260, 60, anchor=NW, window=copy)
            self.loading_canvas.create_window(10, 60, anchor=NW, window=uuid)
    def loading_variables_set(self):
        self.parent.geometry("700x300")
        self.loading_frame = Frame(self.parent)
        self.loading_frame.grid(row=0,column=0)
        self.percent_textvar = StringVar()
        self.uuid = StringVar()
        current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        self.uuid.set(current_machine_id)
        self.percent_textvar.set("0.00%")
        self.variables()
        self.loading_screen()
    def loading_variables_destroy(self):
        self.parent.geometry("147x197")
        self.loading_frame.grid_remove()
        self.variables()
        self.InitGui()
    def copy_uuid(self):

       pyperclip.copy(self.uuid.get())

    def change_language(self,language):
        self.info['info']['language'] = language
        self.language = language
        with open('file\config.ini', 'w') as configfile:
            self.info.write(configfile)
        self.update_language()
    def return_mongodb(self):

        self.client = pymongo.MongoClient(
            "mongodb+srv://bosstimer:timerboss@cluster0.zxtp6.mongodb.net/Cluster0?retryWrites=true&w=majority")
        conn = self.client["UUID"]
        db = conn['uuids']
        
        uuid = str(db.find_one({str(subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()):"True"}))
        if uuid == "None":
            return False
        else:
            return True
        return True      
    def delete_items(self):
        self.remove_all_frame()
        self.parent.title( self.info[self.language]["notice_9"])
        self.deleteItemFrame.grid(row=0,column=0)
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
                sleep(1)
                self.movement.move(self.dissolition_accept_v[0],self.dissolition_accept_v[1])
                self.movement.click_button()                                   
    def delete_item_func(self):
        if self.satir2.get().isnumeric() and self.sutun2.get().isnumeric() and self.numbef_of_fragmented_item2.get().isnumeric():
            satir = int(self.satir2.get())
            sutun = int(self.sutun2.get())
            number = int(self.numbef_of_fragmented_item2.get())
            for i in range(0,number):

                self.movement.click_move(self.row1_column1[0] +(sutun -1)*32,self.row1_column1[1] + (satir-1)*32,self.trash[0],self.trash[1])
                self.movement.move(self.trash_all_accept[0],self.trash_all_accept[1])
                self.movement.click_button()
                self.movement.click_button()
                self.movement.move(self.trash_accept[0],self.trash_accept[1])
                self.movement.click_button()
                self.movement.move(self.trash_accept[0],self.trash_accept[1]-5)
                self.movement.click_button()
                sleep(0.1)
    def set_fixes(self):
        ek_name = self.chrome_combo_ekList.get()
        attachments = self.database.return_attachments_list(ek_name)
        for i in range(0,self.ettac_list.size()):
            self.ettac_list.delete(0,"end")
        for i in attachments:
            self.ettac_list.insert(END, i)
    def search_ek(self):
        self.remove_all_frame()
        self.chrome_search_attachment.grid(row=0,column=0)
        self.parent.title( self.info[self.language]["notice_8"])
        self.parent.geometry("630x250")
    def ettac_check(self):
        if int(self.search_ettac_list.size()) == 0 and int(self.search_ettac_list_2.size()) == 0:
            showinfo( self.info[self.language]["notice_4"],  self.info[self.language]["notice_3"])
        else:
            if self.number_of_ettac_P.get().isnumeric() and self.number_of_ettac_S.get().isnumeric():
                if (self.checkVars_2.get() == 0 and self.checkVars_1.get() == 0):
                    showinfo( self.info[self.language]["notice_4"], self.info[self.language]["notice_5"])
                else:
                    for i in range(0,self.ettac_counter):
                        self.coming_ettac_list.delete(0,END)
                    self.ettac_counter = 0
                    self.ettac_counter_text.set(self.info[self.language]["fixes"] + " (" + str(self.ettac_counter) + ")")
                    treading = threading.Thread(target=self.start_ettac)
                    treading.start()
            else:
                showinfo(self.info[self.language]["notice_4"],self.info[self.language]["notice_6"] )
    def ettac_add_p(self):
        selected_ettec_list = self.ettac_list.curselection()

        ettec_name =  self.search_ettac_list.get(0,END)

        for num in selected_ettec_list:
            if not self.ettac_list.get(num) in ettec_name:
                self.search_ettac_list.insert(END, self.ettac_list.get(num))
    def ettac_remove_p(self):
        selected_ettec_search = self.search_ettac_list.curselection()
        for i in selected_ettec_search:
            self.search_ettac_list.delete(i)
    def ettac_add_s(self):
        selected_ettec_list = self.ettac_list.curselection()
        ettec_name =  self.search_ettac_list_2.get(0,END)
        for num in selected_ettec_list:
            if not self.ettac_list.get(num) in ettec_name:
                self.search_ettac_list_2.insert(END, self.ettac_list.get(num))
    def ettac_remove_s(self):
        selected_ettec_search = self.search_ettac_list_2.curselection()
        for i in selected_ettec_search:
            self.search_ettac_list_2.delete(i)
    def start_ettac(self):
        counter = 0
        on_aranan_ekler = []
        son_aranan_ekler = []
        for i in self.search_ettac_list.get(0,END):
            on_aranan_ekler.append(i)

        for i in self.search_ettac_list_2.get(0,END):
            son_aranan_ekler.append(i)

        cikma_sarti = [True,True]
        exit = False

        if int(self.number_of_ettac_P.get()) < int(self.number_of_ettac_S.get()):
            max_ek_sayisi = int(self.number_of_ettac_S.get())
        else:
            max_ek_sayisi = int(self.number_of_ettac_P.get())

        while (counter < max_ek_sayisi) and not exit:
            if self.checkVars_1.get() == 1 and self.checkVars_2.get() == 1:
                if cikma_sarti[0]:
                    self.ek_bas("P")
                    self.ara.screenshoot()
                    self.ara.crop_image()
                    name = self.ara.read_text("P")
                    if name in on_aranan_ekler:
                        if self.ettac_counter < 11:
                            self.coming_ettac_list.insert("end", "(P) " + name)
                        cikma_sarti[0] = False
                    else:
                        self.coming_ettac_list.insert("end", "(P) " + name)
                        self.ek_sil("P")
                if cikma_sarti[1]:
                    self.ek_bas("S")
                    self.ara.screenshoot()
                    self.ara.crop_image()
                    name = self.ara.read_text("S")
                    if name in on_aranan_ekler:
                        if self.ettac_counter < 11:
                            self.coming_ettac_list.insert("end", "(S) " + name)
                        cikma_sarti[1] = False
                    else:
                        self.coming_ettac_list.insert("end", "(S) " + name)
                        self.ek_sil("S")

                self.ettac_counter += 1
                counter += 1
                self.ettac_counter_text.set(self.info[self.language]["fixes"] + "(" + str(self.ettac_counter) + ")")
                if int(self.number_of_ettac_P.get()) <= self.ettac_counter:
                    cikma_sarti[0] = False
                if int(self.number_of_ettac_S.get()) <= self.ettac_counter:
                    cikma_sarti[1] = False
                if (not cikma_sarti[0]) and (not cikma_sarti[1]):
                    exit = True

            else:
               
                
                if self.checkVars_1.get() == 1 and self.checkVars_2.get() == 0:
                    self.ek_bas("P")
                    self.ara.screenshoot()
                    self.ara.crop_image()
                    name = self.ara.read_text("P")
                    self.coming_ettac_list.insert("end", "(P) "+name)
                    if name in on_aranan_ekler:
                        exit = True
                    else:
                        self.ettac_counter += 1 
                        self.ettac_counter_text.set(self.info[self.language]["fixes"] + "(" + str(self.ettac_counter) + ")")
                        self.ek_sil("P")
                else:
                    self.ek_bas("P")
                    self.ara.screenshoot()
                    self.ara.crop_image()
                    name = self.ara.read_text("S")
                    self.coming_ettac_list.insert("end", "(S) "+name)
                    if name in son_aranan_ekler:
                        exit = True
                    else:
                        self.ettac_counter += 1 
                        self.ettac_counter_text.set(self.info[self.language]["fixes"] + "(" + str(self.ettac_counter) + ")")
                        self.ek_sil("P")

                counter += 1
            if keyboard.is_pressed('space'):
                exit = True
    def ek_bas(self,sart):
        if sart == "P":
            self.movement.move(self.Pbasma[0], self.Pbasma[1])
            sleep(0.1)
            self.movement.doubleClick()
            sleep(0.1)
            self.movement.move(self.silah[0], self.silah[1])
            sleep(0.1)
            self.movement.doubleClick()
            sleep(0.1)
            self.movement.move(self.onay[0], self.onay[1])
            sleep(0.1)
            self.movement.click_button()
            sleep(0.2)
            self.movement.click_button()
        else:
            self.movement.move(self.Sbasma[0], self.Sbasma[1])
            sleep(0.1)
            self.movement.doubleClick()
            sleep(0.1)
            self.movement.move(self.silah[0], self.silah[1])
            sleep(0.1)
            self.movement.doubleClick()
            sleep(0.1)
            self.movement.move(self.onay[0], self.onay[1])
            sleep(0.1)
            self.movement.click_button()
            sleep(0.2)
            self.movement.click_button()
    def ek_sil(self,sart):
        if sart == "P":
            self.movement.move(self.Psilme[0], self.Psilme[1])
            sleep(0.1)
            self.movement.doubleClick()
            sleep(0.1)
            self.movement.move(self.silah[0], self.silah[1])  # perde silah
            sleep(0.1)
            self.movement.doubleClick()
            sleep(0.1)
            self.movement.move(self.onay[0], self.onay[1])  # Ek bas onay butonu
            sleep(0.1)
            self.movement.click_button()
            sleep(0.2)
            self.movement.click_button()
        else:
            self.movement.move(self.Ssilme[0], self.Ssilme[1])
            sleep(0.1)
            self.movement.doubleClick()
            sleep(0.1)
            self.movement.move(self.silah[0], self.silah[1])  # perde silah
            sleep(0.1)
            self.movement.doubleClick()
            sleep(0.1)
            self.movement.move(self.onay[0], self.onay[1])  # Ek bas onay butonu
            sleep(0.1)
            self.movement.click_button()
            sleep(0.2)
            self.movement.click_button()
    def remove_all_frame(self):
        self.idPasswd.grid_remove()
        self.chrome_idPass_Frame.grid_remove()
        self.chrome_search_attachment.grid_remove()
        self.deleteItemFrame.grid_remove()
    def run_passworDirectory(self):
        self.parent.title( self.info[self.language]["notice_7"])
        self.parent.geometry("645x300")
        self.remove_all_frame()
        self.idPasswd.grid(row=1, column=0)
        self.click = [False, False]
        self.database.create()

        self.update_contacs()
    def update_contacs(self):

        self.treeBox.delete_all()
        self.treeBox_id.delete_all()
        self.treeBox_passwd.delete_all()

        id, passwd = self.database.return_users()
        self.sayac = 0
        for i in range(0, len(id)):
            self.treeBox.insert('end', self.sayac + 1)
            self.treeBox_id.insert('end', id[self.sayac])
            self.treeBox_passwd.insert('end', passwd[self.sayac])
            self.sayac += 1
        self.id.delete(0, END)
        self.id.insert(0, self.info[self.language]["username"])
        self.passwd.delete(0, END)
        self.passwd.insert(0, self.info[self.language]["passwd"])
    def delete_contacs(self):
        try:
            pass
        except:
            showinfo(self.info[self.language]["notice_4"], self.info[self.language]["notice_10"])
        self.update_contacs()
    def add_data(self):
        self.database.add([self.id.get(), self.passwd.get()])
        self.update_contacs()
    def clear_directory_id(self, _):
        self.click = [True, False]
        if str(self.passwd.get()) == "":
            self.passwd.insert(0, self.info[self.language]["passwd"])
        if str(self.id.get()) == self.info["english"]["username"] or str(self.id.get()) == self.info["turkish"]["username"]:
            self.id.delete(0, END)
    def clear_directory_passwd(self, _):
        self.click = [False, True]
        if str(self.id.get()) == "":
            self.id.insert(0, self.info[self.language]["username"])
        if str(self.passwd.get()) ==self.info["english"]["passwd"] or str(self.passwd.get()) == self.info["turkish"]["passwd"]:
            self.passwd.delete(0, END)

class database:
    def __init__(self):
        self.path = "file\\"
        self.info = configparser.ConfigParser()
        self.info.read(self.path + "config.ini")

    def create(self):
        if not (os.path.exists(self.path)):
            os.mkdir(self.path)
        if not (os.path.isfile(self.path + self.info["info"]["databaseName_passwd"])):
            baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_passwd"])
            veri = baglan.cursor()
            veri.execute("""CREATE TABLE {} (
                                'id'	TEXT UNIQUE,
                                'sifre'	TEXT,
                                PRIMARY KEY(id));""".format("password"))
            baglan.commit()
            baglan.close()

        if not (os.path.isfile(self.path + self.info["info"]["databaseName_config"])):
            baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_config"])
            veri = baglan.cursor()
            veri.execute("""CREATE TABLE {} ('delay'	TEXT);""".format("config"))
            baglan.commit()
            baglan.close()
        else:
            pass

    def update_config(self, time):
        baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_config"])
        veri = baglan.cursor()

        veri.execute("INSERT INTO config VALUES(" + time + ")")
        baglan.commit()
        baglan.close()

    def return_config_time(self):
        baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_config"])
        veri = baglan.cursor()
        values = veri.execute("select * from config").fetchall()
        return values[-1][0]

    def return_attachments_list(self,ek_name):

        if ek_name == self.info["turkish"]["armor_accuracy"] or ek_name == self.info["english"]["armor_accuracy"]:
            name = "15972.db"
        elif ek_name == self.info["turkish"]["armor_experience_rate"] or ek_name == self.info["english"]["armor_experience_rate"]:
            name = "15973.db"
        elif ek_name == self.info["turkish"]["armor_drop_rate"] or ek_name == self.info["english"]["armor_drop_rate"] :
            name = "15978.db"
        elif ek_name == self.info["turkish"]["armor_pierce"] or ek_name == self.info["english"]["armor_pierce"]:
            name = "15979.db"
        elif ek_name == self.info["turkish"]["weapon_ra_accuracy"] or ek_name == self.info["english"]["weapon_ra_accuracy"]:
            name = "15971.db"
        elif ek_name == self.info["turkish"]["weapon_accuracy"] or ek_name == self.info["english"]["weapon_accuracy"]:
            name = "15976.db"
        elif ek_name == self.info["turkish"]["weapon_ra_attack"] or ek_name == self.info["english"]["weapon_ra_attack"]:
            name = "15977.db"
        elif ek_name == self.info["turkish"]["weapon_weight"] or ek_name == self.info["english"]["weapon_weight"] :
            name = "15975.db"
        elif ek_name == self.info["turkish"]["weapon_pierce"] or ek_name == self.info["english"]["weapon_pierce"]:
            name = "15980.db"
        else:
            name = "15974.db"
        baglan = sqlite3.connect("file/" + name)
        veri = baglan.cursor()
        values = veri.execute("select * from attachments_list").fetchall()
        array = []
        for i in values:
            array.append(i[0])
        return array
    def add(self, variable):
        if (str(variable[0]) == self.info[self.language]["username"] or str(variable[1]) == self.info[self.language]["passwd"]):
            showinfo(self.info[self.language]["notice_4"], self.info[self.language]["notice_11"])
        else:
            try:
                baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_passwd"])
                veri = baglan.cursor()
                veri.execute("INSERT INTO password (id, sifre) VALUES (?,?)", (variable[0], variable[1]))
                baglan.commit()
                baglan.close()
            except sqlite3.IntegrityError:
                showinfo(self.info[self.language]["notice_4"], self.info[self.language]["notice_12"])

    def delete(self, id):

        baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_passwd"])
        veri = baglan.cursor()
        read = veri.execute("select * from password").fetchall()
        syc = 1
        for i in read:
            if syc == id + 1:
                id = i[0]
            syc += 1
        veri.execute("DELETE from password where id = '" + id + "'")
        baglan.commit()
        baglan.close()

    def return_users(self):
        baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_passwd"])
        veri = baglan.cursor()
        id = []
        passwd = []
        values = veri.execute("select * from password").fetchall()
        for i in values:
            id.append(i[0])
            passwd.append(i[1])
        return id, passwd

class FancyListbox(tkinter.Listbox):

    def __init__(self, parent, *args, **kwargs):
        tkinter.Listbox.__init__(self, parent, *args, **kwargs)
        self.popup_menu = tkinter.Menu(self, tearoff=0)
        self.path = "file\\"
        self.info = configparser.ConfigParser()
        self.info.read(self.path + "config.ini")
        self.language = self.info["info"]["language"]
        self.popup_menu.add_command(label=self.info[self.language]["copy"],
                                    command=self.copy)
        self.bind("<Button-3>", self.popup)
        self.popup_menu.add_command(label=self.info[self.language]["delete"],
                                    command=self.delete_selected)

        self.database = database()

    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def copy(self):
        self.event_generate('<<Copy>>')

    def delete_all(self):
        self.selection_set(0, 'end')
        for i in self.curselection()[::-1]:
            self.delete(i)

    def delete_selected(self):
        MsgBox = messagebox.askquestion(self.info[self.language]["delete"], self.info[self.language]["notice_13"],
                                        icon='warning')
        if MsgBox ==self.info[self.language]["yes"]:
            for i in self.curselection()[::-1]:
                self.database.delete(i)


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

class search:
    def screenshoot(self):
        Screenshot = pyautogui.screenshot()
        Screenshot.save("image/ek.png")
    def crop_image(self):
        path = "file\\"
        info = configparser.ConfigParser()
        info.read(self.path + "config.ini")
        position = info[info["info"]["resolition"]]["img_right_area"].split(",")
        img = Image.open("image/ek.PNG")
        img_right_area = (position[0], position[1], position[2], position[3])
        img_right = img.crop(img_right_area)
        img_right.save("image/cropped.png")
    def read_text(self,choose):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        img = cv2.imread("image/cropped.png")
        text = pytesseract.image_to_string(img)
        text = text.strip()
        if choose == "P":
            if " " in text:
                text = text.split(" ")[0]
        if choose == "S":
            if " " in text:
                text = text.split(" ")[1]
        if "{" in text:
            text = text.split("{")[0]
        if "(" in text:
            text = text.split("(")[0]

        text = text.strip()

        return text


if __name__ == "__main__":
    root = Tk()
    root.call('tk', 'scaling', 1.0)
    run = tkinterGui(root)
    root.mainloop()
