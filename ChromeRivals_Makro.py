#!/usr/bin/env python
 # -*- coding: utf-8 -*-

import datetime
from time import sleep,strftime
from tkinter import *
import threading
from tkinter.messagebox import showinfo
import os
import tkinter.ttk
from tkinter import ttk
import sqlite3
import configparser
from tkinter import messagebox
import random
import subprocess
import pyperclip
from PIL import Image, ImageTk, ImageFont, ImageDraw
import keyboard
import ctypes
import pyautogui
import cv2
import pytesseract
from functools import partial
import requests
import json
import win32api
import win32con 


class tkinterGui(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("ToolBox")
        
        self.loading_variables_set()
        
    def InitGui(self):
        if self.verbose:
           print("> InitGui {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
        #Menu
        self.menubar = Menu(self.parent)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = self.config.return_read(self.info_path,self.language,"apps"), menu = self.filemenu)
        self.filemenu.add_command(label = "ID-Pass", command = self.run_passworDirectory)
        self.filemenu.add_command(label = "Search", command = self.search_ek)
        self.filemenu.add_command(label = "Delete Item", command = self.delete_items)
        self.filemenu.add_command(label = "Bosses", command = self.show_bosses)
        

        self.help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label =  self.config.return_read(self.info_path,self.language,"language"), menu = self.help_menu)
        for section in self.config.return_section(self.info_path):
            if section != "info" and (not section[0].isnumeric()):
                if section == self.language:
                    self.help_menu.add_command(label = ("→"+self.config.return_read(self.info_path,section,"local_language")+"←"), command = partial(self.change_language, section))
                else:
                    self.help_menu.add_command(label = (self.config.return_read(self.info_path,section,"local_language")), command = partial(self.change_language, section))


        self.resolition_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label =  self.config.return_read(self.info_path,self.language,"resolition"), menu = self.resolition_menu)
        for section in self.config.return_section(self.info_path):
            if section[0].isnumeric():
                if self.resolition == section:
                    self.resolition_menu.add_command(label = "→"+ section +"←", command = partial(self.change_resolition, section))
                else:
                    self.resolition_menu.add_command(label = section, command = partial(self.change_resolition, section))

        root.config(menu=self.menubar)
  
        if self.verbose:
           print("< InitGui {}".format(datetime.datetime.today().strftime("%H:%M:%S")))

    def variables(self):
        self.verbose = False
        if self.verbose:
           print("> variables {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
        self.path = "file\\"
        self.info_path = self.path + "config.ini"
        self.config = config_parser
        self.idPasswd = Frame(self.parent)
        self.deleteItemFrame = Frame(self.parent)
        self.chrome_idPass_Frame = Frame(self.parent)
        self.chrome_search_attachment = Frame(self.parent)
        self.chrome_bosses = Frame(self.parent)
        self.checkVars_1 = IntVar()
        self.checkVars_2 = IntVar()
        self.search_combo = StringVar()
        self.counter = 1



        self.click = [False, False]
        self.language = self.config.return_read(self.info_path,"info","language")
        self.resolition = self.config.return_read(self.info_path,"info","resolition")
        self.info_image = ImageTk.PhotoImage(Image.open(self.path + 'png\\info.png').resize((25, 20), Image.ANTIALIAS))
        self.istatistik_image = ImageTk.PhotoImage(Image.open(self.path + 'png\\istatistik.png').resize((25, 20), Image.ANTIALIAS))

        self.database = database()
        self.database.create()
        self.ara = search()
        self.movement = movemont
        self.sayac = 0
        self.login = True

        self.Psilme = [int(self.config.return_read(self.info_path,self.resolition,"Psilme").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"Psilme").split(",")[1])] 
        self.Pbasma = [int(self.config.return_read(self.info_path,self.resolition,"Pbasma").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"Pbasma").split(",")[1])]
        self.Ssilme = [int(self.config.return_read(self.info_path,self.resolition,"Ssilme").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"Ssilme").split(",")[1])]
        self.Sbasma = [int(self.config.return_read(self.info_path,self.resolition,"Sbasma").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"Sbasma").split(",")[1])]
        self.silah = [int(self.config.return_read(self.info_path,self.resolition,"silah").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"silah").split(",")[1])] 
        self.onay = [int(self.config.return_read(self.info_path,self.resolition,"onay").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"onay").split(",")[1])] 


        self.trash = [int(self.config.return_read(self.info_path,self.resolition,"trash").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"trash").split(",")[1])] 
        self.row1_column1 = [int(self.config.return_read(self.info_path,self.resolition,"row1_column1").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"row1_column1").split(",")[1])] 
        self.row1_column1_disp = [int(self.config.return_read(self.info_path,self.resolition,"row1_column1_disp").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"row1_column1_disp").split(",")[1])]
        self.trash_all_accept = [int(self.config.return_read(self.info_path,self.resolition,"trash_all_accept").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"trash_all_accept").split(",")[1])] 
        self.trash_accept = [int(self.config.return_read(self.info_path,self.resolition,"trash_accept").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"trash_accept").split(",")[1])]
        self.dissolition_accept = [int(self.config.return_read(self.info_path,self.resolition,"dissolution_accept").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"dissolution_accept").split(",")[1])]
        self.dissolition_accept_v = [int(self.config.return_read(self.info_path,self.resolition,"dissolution_accept_v").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"dissolution_accept_v").split(",")[1])]
        self.dissolition_panel = [int(self.config.return_read(self.info_path,self.resolition,"dissolution_panel").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"dissolution_panel").split(",")[1])]
        self.token_panel = [int(self.config.return_read(self.info_path,self.resolition,"token_panel").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"token_panel").split(",")[1])]
        self.token_start = [int(self.config.return_read(self.info_path,self.resolition,"token_start").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"token_start").split(",")[1])]
        self.token_accept = [int(self.config.return_read(self.info_path,self.resolition,"token_accept").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"token_accept").split(",")[1])]
        self.islem = [False, False]
        self.var = IntVar()
        self.autoBuff_tick = False
        self.ch_loop_exit = True
        self.attec_array = []
        self.ettac_counter_text = StringVar()
        self.ettac_counter = 0

        if self.verbose:
           print("< variables {}".format(datetime.datetime.today().strftime("%H:%M:%S")))

    def donothing(self):
        pass
    def show_bosses(self):
        self.remove_all_frame()
        self.chrome_bosses.grid(row=0,column=0)
        self.parent.geometry("605x255")
        self.boss_canvas = Canvas(self.chrome_bosses, width=605, height=500)
        img = ImageTk.PhotoImage(Image.open('file\\png\\bg.png').resize((605, 500), Image.ANTIALIAS))  #
        self.boss_canvas.background = img  #
        bg_pic = self.boss_canvas.create_image(0, 0, anchor=NW, image=img)
        self.boss_canvas.grid(row=0, column=0, rowspan=500, columnspan=605)
        self.boss_names = self.database.return_boss_names()
        self.boss_names_ekList = ttk.Combobox(self.boss_canvas, width=24, textvariable=self.donothing)

        tuple = ()
        for names in self.boss_names:
            tuple += (names[0],)
        self.boss_names_ekList['values'] = tuple
        self.boss_names_ekList.current(0)
        self.boss_names_ekList.bind("<<ComboboxSelected>>", self.choose_boss)

        self.boss_names_text_info = Text (self.chrome_bosses, height = 5,
                width = 25,
                bg = "light yellow", font = ("Helvatica",12))
        #self.tree = ttk.Treeview(self.chrome_bosses,height = 6)

        columns = ("ek_adi","sayisi" )
        self.tree = ttk.Treeview(self.chrome_bosses, columns=columns, show='headings',height = 10)
        self.tree.heading('ek_adi', text=self.config.return_read(self.info_path,self.language,"boss_name"), anchor='center')
        self.tree.heading('sayisi', text=self.config.return_read(self.info_path,self.language,"boss_Drop_rate"), anchor='center')
        self.tree.column("ek_adi", anchor='center')
        self.tree.column("sayisi", anchor='center')



        self.boss_canvas.create_window(5, 5, anchor=NW, window=self.boss_names_ekList)
        self.boss_canvas.create_window(5, 25, anchor=NW, window=self.boss_names_text_info)
        self.boss_canvas.create_window(200, 25, anchor=NW, window=self.tree)

        


        self.choose_boss("_")
    def choose_boss(self,_):
        boss_name = self.boss_names_ekList.get()
        for name_set in self.boss_names:
            if boss_name in name_set:
                id = name_set[1]

        drops, boss_info = self.return_boss_items(id)
        text_ ="""Name = {}\nLevel = {}\nHp = {}\nRange = {}\nrecoveryTime = {}""".format(boss_info[0].strip("\y").strip("\c").strip("\m").strip("\o"),boss_info[1],boss_info[2],boss_info[3],boss_info[4])
        self.boss_names_text_info.delete('1.0', END)

        self.boss_names_text_info.insert(END,text_)

        if self.counter > 1:
            for i in self.tree.get_children():
                self.tree.delete(i)
        self.tree.insert('', END, text=boss_name, iid=0, open=False)

        self.counter =1
        for drop in drops:
            #text_ = drop.strip("\y").strip("\c").strip("\m") +" -- " + str(drops[drop]) + "%"
            self.tree.insert('', END, values=(drop.strip("\y").strip("\c").strip("\m"),str(drops[drop])+"%"), iid = self.counter, open=False)
            #self.tree.move(self.counter, 0, self.counter-1)
            self.counter +=1



    def return_boss_items(self,id):
        headers = {'accept': '*/*',
                    'Cr-Api-Key': 'Gork3m-Player-Z5X96djv',}
        url = "https://api.chromerivals.net/pedia/monster/" +str(id)
        response = requests.get(url, headers=headers)
        res = json.loads(response.text)
        name = res["result"]["name"]
        level = res["result"]["level"]
        hp = res["result"]["hp"]
        range = res["result"]["range"]
        recoveryTime = res["result"]["recoveryTime"]
        drops = {}
        for drop_items in res["result"]["drop"]:
            drops[drop_items["referenceItem"]["name"]] = drop_items["dropProbability"]

        return drops,[name,level,hp,range,recoveryTime]
    def check_update(self):
        if self.verbose:
           print("> check_update {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
        if int(self.config.return_read(self.info_path,"info","version")) < 10:
            link = self.config.return_read(self.info_path,"info","update_link")+"version_v_0"+str(int( self.config.return_read(self.info_path,"info","version"))+1) + ".zip"
        else:
            link = self.config.return_read(self.info_path,"info","update_link")+"version_v_"+str(int( self.config.return_read(self.info_path,"info","version"))+1) + ".zip"
        sorgu = requests.head(link, allow_redirects=True)
        if sorgu.status_code == 200:

            if int(self.config.return_read(self.info_path,"info","version")) < 10:
                version = "0"+str(int( self.config.return_read(self.info_path,"info","version"))+1)
            else:
                version = str(int( self.config.return_read(self.info_path,"info","version"))+1)
            self.config.write(self.info_path,"version",version)
            try: win32api.WinExec(os.getcwd() + '\\updater\\updater.exe') # Works seamlessly
            except: pass
            if self.verbose:
                print("< check_update {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
            self.parent.destroy()
                 
        else:
            if self.verbose:
                print("< check_update {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
            self.search_ek()
    def about(self):
        pass
    def change_resolition(self,resolution):
        if self.verbose:
           print("> change_resolution {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
        self.config.write(self.info_path,"resolition",resolution)
        self.resolition = resolution

        self.Psilme = [int(self.config.return_read(self.info_path,self.resolition,"Psilme").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"Psilme").split(",")[1])] 
        self.Pbasma = [int(self.config.return_read(self.info_path,self.resolition,"Pbasma").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"Pbasma").split(",")[1])]
        self.Ssilme = [int(self.config.return_read(self.info_path,self.resolition,"Ssilme").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"Ssilme").split(",")[1])]
        self.Sbasma = [int(self.config.return_read(self.info_path,self.resolition,"Sbasma").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"Sbasma").split(",")[1])]
        self.silah = [int(self.config.return_read(self.info_path,self.resolition,"silah").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"silah").split(",")[1])] 
        self.onay = [int(self.config.return_read(self.info_path,self.resolition,"onay").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"onay").split(",")[1])] 


        self.trash = [int(self.config.return_read(self.info_path,self.resolition,"trash").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"trash").split(",")[1])] 
        self.row1_column1 = [int(self.config.return_read(self.info_path,self.resolition,"row1_column1").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"row1_column1").split(",")[1])] 
        self.row1_column1_disp = [int(self.config.return_read(self.info_path,self.resolition,"row1_column1_disp").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"row1_column1_disp").split(",")[1])]
        self.trash_all_accept = [int(self.config.return_read(self.info_path,self.resolition,"trash_all_accept").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"trash_all_accept").split(",")[1])] 
        self.trash_accept = [int(self.config.return_read(self.info_path,self.resolition,"trash_accept").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"trash_accept").split(",")[1])]
        self.dissolition_accept = [int(self.config.return_read(self.info_path,self.resolition,"dissolution_accept").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"dissolution_accept").split(",")[1])]
        self.dissolition_accept_v = [int(self.config.return_read(self.info_path,self.resolition,"dissolution_accept_v").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"dissolution_accept_v").split(",")[1])]
        self.dissolition_panel = [int(self.config.return_read(self.info_path,self.resolition,"dissolution_panel").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"dissolution_panel").split(",")[1])]
        self.token_panel = [int(self.config.return_read(self.info_path,self.resolition,"token_panel").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"token_panel").split(",")[1])]
        self.token_start = [int(self.config.return_read(self.info_path,self.resolition,"token_start").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"token_start").split(",")[1])]
        self.token_accept = [int(self.config.return_read(self.info_path,self.resolition,"token_accept").split(",")[0]),int(self.config.return_read(self.info_path,self.resolition,"token_accept").split(",")[1])]
        if self.verbose:
           print("< chance_resoluiton {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
        self.update_language()
    def update_language(self):
        if self.verbose:
           print("> update_language {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
        self.menubar.delete(0, 'end')
        self.menubar = Menu(self.parent)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = self.config.return_read(self.info_path,self.language,"apps"), menu = self.filemenu)
        self.filemenu.add_command(label = "ID-Pass", command = self.run_passworDirectory)
        self.filemenu.add_command(label = "Search", command = self.search_ek)
        self.filemenu.add_command(label = "Delete Item", command = self.delete_items)
        self.filemenu.add_command(label = "Bosses", command = self.show_bosses)
        

        self.help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label =  self.config.return_read(self.info_path,self.language,"language"), menu = self.help_menu)
        for section in self.config.return_section(self.info_path):
            if section != "info" and (not section[0].isnumeric()):
                if section == self.language:
                    self.help_menu.add_command(label = ("→"+self.config.return_read(self.info_path,section,"local_language")+"←"), command = partial(self.change_language, section))
                else:
                    self.help_menu.add_command(label = (self.config.return_read(self.info_path,section,"local_language")), command = partial(self.change_language, section))

        self.resolition_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label =  self.config.return_read(self.info_path,self.language,"resolition"), menu = self.resolition_menu)
        for section in self.config.return_section(self.info_path):
            if section[0].isnumeric():
                if self.resolition == section:
                    self.resolition_menu.add_command(label = "→"+ section +"←", command = partial(self.change_resolition, section))
                else:
                    self.resolition_menu.add_command(label = section, command = partial(self.change_resolition, section))


        root.config(menu=self.menubar)

        self.parent.title("Toolbox")

        self.chrome_combo_ekList.set('')
        self.chrome_combo_ekList['values'] = (self.config.return_read(self.info_path,self.language,"armor_accuracy"),
                                                self.config.return_read(self.info_path,self.language,"armor_experience_rate"),
                                                self.config.return_read(self.info_path,self.language,"armor_drop_rate"),
                                                #self.config.return_read(self.info_path,self.language,"armor_pierce"),
                                                self.config.return_read(self.info_path,self.language,"weapon_accuracy"),
                                                self.config.return_read(self.info_path,self.language,"weapon_ra_accuracy"),
                                                self.config.return_read(self.info_path,self.language,"weapon_ra_attack"),
                                                self.config.return_read(self.info_path,self.language,"weapon_weight"),
                                                #self.config.return_read(self.info_path,self.language,"weapon_pierce"),
                                                self.config.return_read(self.info_path,self.language,"pet"))
        
      
        

        self.search_ettac_list_name.config(text = self.config.return_read(self.info_path,self.language,"prefixes_to_search"))
        self.search_ettac_list_name_s.config(text = self.config.return_read(self.info_path,self.language,"suffix_to_search"))
        self.ettac_counter_text.set(self.config.return_read(self.info_path,self.language,"fixes") + " (" + str(self.ettac_counter) + ")")

        self.search_start_stop.config(text= self.config.return_read(self.info_path,self.language,"run"))

        
        if self.verbose:
           print("< update_language {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
    def loading_screen(self):
        if self.verbose:
           print("> loading_Screen {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
        self.loading_canvas = Canvas(self.loading_frame, width=310, height=120)
        img = ImageTk.PhotoImage(Image.open('file\\png\\new_error.png').resize((310, 120), Image.ANTIALIAS))  #
        self.loading_canvas.background = img  #
        bg_pic = self.loading_canvas.create_image(0, 0, anchor=NW, image=img)
        self.loading_canvas.grid(row=0, column=0, rowspan=310, columnspan=120)
        progress = ttk.Progressbar(self.loading_canvas, orient = HORIZONTAL,length = 250, mode = 'determinate')
        percent_text = Label(self.loading_frame, textvariable= self.percent_textvar, font =("Helvatica",12))
        uuid = Label(self.loading_frame, textvariable= self.uuid, font =("Helvatica",12))
        copy = Button(self.loading_frame, text=  self.config.return_read(self.info_path,self.language,"copy"), font =("Helvatica",10),command=self.copy_uuid)
        warning1 = Label(self.loading_frame, text=  self.config.return_read(self.info_path,self.language,"notice_1"), font =("Helvatica",12))
        warning2 = Label(self.loading_frame, text=  self.config.return_read(self.info_path,self.language,"notice_2"), font =("Helvatica",12))

        if self.return_licences():
            if self.verbose:
                print("< loading_Screen {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
            self.loading_variables_destroy()
        else:
            self.parent.geometry("310x120")
            self.loading_canvas.create_window(10, 10, anchor=NW, window=warning1)
            self.loading_canvas.create_window(10, 35, anchor=NW, window=warning2)
            self.loading_canvas.create_window(260, 60, anchor=NW, window=copy)
            self.loading_canvas.create_window(10, 60, anchor=NW, window=uuid)
            if self.verbose:
                print("< loading_screen {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
    def loading_variables_set(self):
        self.variables()
        if self.verbose:
           print("> loading_variables_set {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
        self.parent.geometry("700x300")
        self.loading_frame = Frame(self.parent)
        self.loading_frame.grid(row=0,column=0)
        self.percent_textvar = StringVar()
        self.uuid = StringVar()
        current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        self.uuid.set(current_machine_id)
        self.percent_textvar.set("0.00%")
        
        self.loading_screen()
        if self.verbose:
           print("< loading_variables_set {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
    def loading_variables_destroy(self):
        if self.verbose:
           print("> loading_variables_destroy {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
        self.parent.geometry("147x197")
        self.loading_frame.grid_remove()
        self.InitGui()
        self.check_update()
        if self.verbose:
           print("< loading_variables_destroy {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
    def open_help(self):
        pass
    def open_info(self):
        if self.verbose:
           print("> open_info {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
        popup= Toplevel(root)
        popup.geometry("720x735")
        popup.title("Sample Inventory Lineup")
        canvas = Canvas(popup, width=720, height=735)
        img = ImageTk.PhotoImage(Image.open('file\\png\\dizilim.png').resize((720, 735), Image.ANTIALIAS))  #
        canvas.background = img  #
        bg_pic = canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.grid(row=0, column=0, rowspan=720, columnspan=735)
        if self.verbose:
           print("< open_info {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
    def open_statistic(self):
        if self.verbose:
           print("> open_statistic {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
        popup= Toplevel(root)
        popup.geometry("415x235")
        popup.title("Incoming Attachment Statistics")
        canvas = Canvas(popup, width=720, height=735)
        img = ImageTk.PhotoImage(Image.open('file\\png\\bg.png').resize((720, 735), Image.ANTIALIAS))  #
        canvas.background = img  #
        canvas.grid(row=0, column=0, rowspan=720, columnspan=735)

        columns = ("ek_adi", "sayisi")
        tree = ttk.Treeview(popup, columns=columns, show='headings')
        tree.heading('ek_adi', text=self.config.return_read(self.info_path,self.language,"ek_adi"), anchor='center')
        tree.heading('sayisi', text=self.config.return_read(self.info_path,self.language,"number"), anchor='center')
        tree.column("ek_adi", anchor='center')
        tree.column("sayisi", anchor='center')
        data = self.database.return_statistics()
        for contact in data:
            tree.insert('', END, values=contact)



        canvas.create_window(5, 5, anchor=NW, window=tree)
        if self.verbose:
           print("< open_statistic {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
    def copy_uuid(self):

       pyperclip.copy(self.uuid.get())
    def change_language(self,language):
        if self.verbose:
           print("> chance_language {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
        self.language = language
     
        self.config.write(self.info_path,"language",language)
        self.update_language()
        if self.verbose:
           print("< change_language {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
    def break_a_token(self):
        if self.satir3.get().isnumeric() and self.sutun3.get().isnumeric() and self.numbef_of_fragmented_item3.get().isnumeric():
            satir = int(self.satir3.get())
            sutun = int(self.sutun3.get())
            number = int(self.numbef_of_fragmented_item3.get())
            exit = True
            for i in range(0,number):
                if exit:
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
                    if keyboard.is_pressed('space'):
                        exit = False
    def dissolution_item_func(self):
        
        if self.satir.get().isnumeric() and self.sutun.get().isnumeric() and self.numbef_of_fragmented_item.get().isnumeric():
            satir = int(self.satir.get())
            sutun = int(self.sutun.get())
            number = int(self.numbef_of_fragmented_item.get())
            exit = True
            for i in range(0,number):
                if exit:
                    self.movement.click_move(self.row1_column1_disp[0] +(sutun -1)*32,self.row1_column1_disp[1] + (satir-1)*32,self.dissolition_panel[0],self.dissolition_panel[1])
                    sleep(0.1)
                    self.movement.move(self.dissolition_accept[0],self.dissolition_accept[1])
                    self.movement.click_button()
                    sleep(2)
                    self.movement.move(self.dissolition_accept_v[0],self.dissolition_accept_v[1])
                    self.movement.click_button()
                    if keyboard.is_pressed('space'):
                        exit = False                         
    def delete_item_func(self):
        if self.satir2.get().isnumeric() and self.sutun2.get().isnumeric() and self.numbef_of_fragmented_item2.get().isnumeric():
            satir = int(self.satir2.get())
            sutun = int(self.sutun2.get())
            number = int(self.numbef_of_fragmented_item2.get())
            exit = True
            for i in range(0,number) :
                if exit:
                    self.movement.scroll_up()
                    self.movement.move(self.row1_column1[0] +(sutun -1)*32,self.row1_column1[1] + (satir-1)*32)
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
                    if keyboard.is_pressed('space'):
                        exit = False
    def return_licences(self):
        if self.verbose:
           print("> return_licences {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
        
        link = self.config.return_read(self.info_path,"info","licences")+ str(subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()) + ".txt"
        sorgu = requests.head(link, allow_redirects=True)
        if sorgu.status_code == 200:
            if self.verbose:
                print("< return_licences {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
            return True
                 
        else:
            if self.verbose:
                print("< return_mongosb {}".format(datetime.datetime.today().strftime("%H:%M:%S")))
            return False
    
    def delete_items(self):
        self.remove_all_frame()
        self.parent.title( self.config.return_read(self.info_path,self.language,"notice_9"))
        self.parent.geometry("340x102")
        self.deleteItemFrame.grid(row=0,column=0)
        self.delete_item_canvas = Canvas(self.deleteItemFrame, width=340, height=102)
        img = ImageTk.PhotoImage(Image.open('file\\png\\error.png').resize((340, 102), Image.ANTIALIAS))  #
        self.delete_item_canvas.background = img  #
        bg_pic = self.delete_item_canvas.create_image(0, 0, anchor=NW, image=img)
        self.delete_item_canvas.grid(row=0, column=0, rowspan=340, columnspan=102)
        

        self.satir = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=5)
        self.satir.insert(0,self.config.return_read(self.info_path,self.language,"row"))
        self.sutun = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=7)
        self.sutun.insert(0,self.config.return_read(self.info_path,self.language,"column"))
        self.numbef_of_fragmented_item = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=7)
        self.numbef_of_fragmented_item.insert(0,self.config.return_read(self.info_path,self.language,"number"))
        self.fragmented_item_button = Button(self.deleteItemFrame, text = self.config.return_read(self.info_path,self.language,"dissolution_item"), command = self.dissolution_item_func)
        
        



        
        self.satir2 = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=5)
        self.satir2.insert(0,self.config.return_read(self.info_path,self.language,"row"))
        self.sutun2 = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=7)
        self.sutun2.insert(0,self.config.return_read(self.info_path,self.language,"column"))
        self.numbef_of_fragmented_item2 = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=7)
        self.numbef_of_fragmented_item2.insert(0,self.config.return_read(self.info_path,self.language,"number"))
        self.fragmented_item_button2 = Button(self.deleteItemFrame, text = self.config.return_read(self.info_path,self.language,"delete_item"), command = self.delete_item_func)


        self.satir3 = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=5)
        self.satir3.insert(0,self.config.return_read(self.info_path,self.language,"row"))
        self.sutun3 = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=7)
        self.sutun3.insert(0,self.config.return_read(self.info_path,self.language,"column"))
        self.numbef_of_fragmented_item3 = Entry(self.deleteItemFrame, font= ("Helvatica",12),width=7)
        self.numbef_of_fragmented_item3.insert(0,self.config.return_read(self.info_path,self.language,"number"))
        self.fragmented_item_button3 = Button(self.deleteItemFrame, text = self.config.return_read(self.info_path,self.language,"smash_token"), command = self.break_a_token)

        y=0
        self.delete_item_canvas.create_window(5, 5+y, anchor=NW, window=self.satir)
        self.delete_item_canvas.create_window(47, 5+y, anchor=NW, window=self.sutun)
        self.delete_item_canvas.create_window(103, 5+y, anchor=NW, window=self.numbef_of_fragmented_item)
        self.delete_item_canvas.create_window(160, 5+y, anchor=NW, window=self.fragmented_item_button)
        y=25
        self.delete_item_canvas.create_window(5, 5+y, anchor=NW, window=self.satir2)
        self.delete_item_canvas.create_window(47, 5+y, anchor=NW, window=self.sutun2)
        self.delete_item_canvas.create_window(103, 5+y, anchor=NW, window=self.numbef_of_fragmented_item2)
        self.delete_item_canvas.create_window(160, 5+y, anchor=NW, window=self.fragmented_item_button2)

        y=50
        self.delete_item_canvas.create_window(5, 5+y, anchor=NW, window=self.satir3)
        self.delete_item_canvas.create_window(47, 5+y, anchor=NW, window=self.sutun3)
        self.delete_item_canvas.create_window(103, 5+y, anchor=NW, window=self.numbef_of_fragmented_item3)
        self.delete_item_canvas.create_window(160, 5+y, anchor=NW, window=self.fragmented_item_button3)
    def set_fixes(self,_):
        ek_name = self.chrome_combo_ekList.get()
        attachments = self.database.return_attachments_list(ek_name)
        for i in range(0,self.ettac_list.size()):
            self.ettac_list.delete(0,"end")
        for i in attachments:
            self.ettac_list.insert(END, i)
    def search_ek(self):
        self.remove_all_frame()
        
        self.chrome_search_attachment.grid(row=0,column=0)

        self.parent.title( self.config.return_read(self.info_path,self.language,"notice_8"))
        self.parent.geometry("630x250")
        # Search attachment
        self.canvas = Canvas(self.chrome_search_attachment, width=630, height=250)
        img = ImageTk.PhotoImage(Image.open('file\\png\\chrome_wallpaper.png').resize((630, 250), Image.ANTIALIAS))  #
        self.canvas.background = img  #
        bg_pic = self.canvas.create_image(0, 0, anchor=NW, image=img)
        self.canvas.grid(row=0, column=0, rowspan=630, columnspan=250)
        

        self.chrome_combo_ekList = ttk.Combobox(self.chrome_search_attachment, width=24, textvariable=self.search_combo)
        self.chrome_combo_ekList['values'] = (self.config.return_read(self.info_path,self.language,"armor_accuracy"),
                                                self.config.return_read(self.info_path,self.language,"armor_experience_rate"),
                                                self.config.return_read(self.info_path,self.language,"armor_drop_rate"),
                                                #self.config.return_read(self.info_path,self.language,"armor_pierce"),
                                                self.config.return_read(self.info_path,self.language,"weapon_accuracy"),
                                                self.config.return_read(self.info_path,self.language,"weapon_ra_accuracy"),
                                                self.config.return_read(self.info_path,self.language,"weapon_ra_attack"),
                                                self.config.return_read(self.info_path,self.language,"weapon_weight"),
                                                #self.config.return_read(self.info_path,self.language,"weapon_pierce"),
                                                self.config.return_read(self.info_path,self.language,"pet"))
        self.chrome_combo_ekList.bind("<<ComboboxSelected>>", self.set_fixes)
        self.ettac_list = Listbox(self.chrome_search_attachment,font = ("Helvatica bold", 12),selectmode='multiple')

        self.search_add_p = Button(self.chrome_search_attachment,text = "P>",font = ("Helvatica bold", 10),command=self.ettac_add_p)
        self.search_remove_p = Button(self.chrome_search_attachment, text = "P<",font = ("Helvatica bold", 10),command = self.ettac_remove_p)

        self.search_add_s = Button(self.chrome_search_attachment,text = "S>",font = ("Helvatica bold", 10),command=self.ettac_add_s)
        self.search_remove_s = Button(self.chrome_search_attachment, text = "S<",font = ("Helvatica bold", 10),command = self.ettac_remove_s)




        self.search_ettac_list_name = Label(self.chrome_search_attachment, text = self.config.return_read(self.info_path,self.language,"prefixes_to_search"),font = ("Helvatica bold", 12),bg = "red")
        self.search_ettac_list = Listbox(self.chrome_search_attachment,font = ("Helvatica bold", 12),selectmode='multiple')
        self.search_ettac_list_name_s = Label(self.chrome_search_attachment, text = self.config.return_read(self.info_path,self.language,"suffix_to_search"),font = ("Helvatica bold", 12),bg = "red")
        self.search_ettac_list_2 = Listbox(self.chrome_search_attachment,font = ("Helvatica bold", 12),selectmode='multiple')

        self.coming_ettac = Label(self.chrome_search_attachment, bg="green", textvariable=self.ettac_counter_text,font = ("Helvatica bold", 12))
        self.coming_ettac_list = Listbox(self.chrome_search_attachment, font=("Helvatica bold", 12))

        self.number_of_ettac_P = Entry(self.chrome_search_attachment,font = ("Helvatica bold", 13),bg="green",width=5)
        self.number_of_ettac_P.insert(0,"0")

        self.number_of_ettac_S = Entry(self.chrome_search_attachment, font=("Helvatica bold", 13), bg="green",width=5)
        self.number_of_ettac_S.insert(0, "0")
        self.ettac_counter_text.set(self.config.return_read(self.info_path,self.language,"fixes") + " (" + str(self.ettac_counter) + ")")

        self.search_start_stop = Button(self.chrome_search_attachment, text= self.config.return_read(self.info_path,self.language,"run"),font = ("Helvatica bold", 12),command= self.ettac_check)

        self.info_button = Button(self.chrome_search_attachment, image=self.info_image,command = self.open_info)
        self.istatistik_button = Button(self.chrome_search_attachment, image=self.istatistik_image,command = self.open_statistic)

        self.ettac_P = Checkbutton(self.chrome_search_attachment, text="P", variable=self.checkVars_1,onvalue=1, offvalue=0)
        self.ettac_S = Checkbutton(self.chrome_search_attachment, text="S", variable=self.checkVars_2,onvalue=1, offvalue=0)

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

        self.canvas.create_window(540, 205, anchor=NW, window=self.search_start_stop)
        self.canvas.create_window(500, 205, anchor=NW, window=self.info_button)
        self.canvas.create_window(462, 205, anchor=NW, window=self.istatistik_button)
    def ettac_check(self):
        if int(self.search_ettac_list.size()) == 0 and int(self.search_ettac_list_2.size()) == 0:
            showinfo( self.config.return_read(self.info_path,self.language,"notice_4"),  self.config.return_read(self.info_path,self.language,"notice_3"))
        else:
            if self.number_of_ettac_P.get().isnumeric() and self.number_of_ettac_S.get().isnumeric():
                if (self.checkVars_2.get() == 0 and self.checkVars_1.get() == 0):
                    showinfo( self.config.return_read(self.info_path,self.language,"notice_4"),  self.config.return_read(self.info_path,self.language,"notice_5"))
                else:
                    for i in range(0,self.ettac_counter):
                        self.coming_ettac_list.delete(0,END)
                    self.ettac_counter = 0
                    self.ettac_counter_text.set(self.config.return_read(self.info_path,self.language,"fixes") + " (" + str(self.ettac_counter) + ")")
                    treading = threading.Thread(target=self.start_ettac)
                    treading.start()
            else:
                showinfo( self.config.return_read(self.info_path,self.language,"notice_4"),  self.config.return_read(self.info_path,self.language,"notice_6"))
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
        if self.checkVars_1.get() == 1 and self.checkVars_2.get() == 1:
            if int(self.number_of_ettac_P.get()) < int(self.number_of_ettac_S.get()):
                max_ek_sayisi = int(self.number_of_ettac_S.get())
            else:
                max_ek_sayisi = int(self.number_of_ettac_P.get())
        elif self.checkVars_1.get() == 0 and self.checkVars_2.get() == 1:
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
                    if "'" in name:
                        name = name.strip("'")
                    self.database.update_statistics(name)
                    if name in on_aranan_ekler:
                        if self.ettac_counter < 11:
                            self.coming_ettac_list.insert("end", "(P) " + name)
                        cikma_sarti[0] = False
                    else:
                        self.coming_ettac_list.insert("end", "(P) " + name)
                        self.search_ettac_list_name.config(text = self.config.return_read(self.info_path,self.language,"prefixes_to_search")+ "(" + str(self.ettac_counter+1) + ")")
                        
                        self.ek_sil("P")
                if cikma_sarti[1]:
                    self.ek_bas("S")
                    self.ara.screenshoot()
                    self.ara.crop_image()
                    name = self.ara.read_text("S")
                    if "'" in name:
                        name = name.strip("'")
                    self.database.update_statistics(name)
                    if name in on_aranan_ekler:
                        if self.ettac_counter < 11:
                            self.coming_ettac_list.insert("end", "(S) " + name)
                        cikma_sarti[1] = False
                    else:
                        self.coming_ettac_list.insert("end", "(S) " + name)
                        self.search_ettac_list_name_s.config(text = self.config.return_read(self.info_path,self.language,"suffix_to_search")+ "(" + str(self.ettac_counter+1) + ")")
                        self.ek_sil("S")

                self.ettac_counter += 1
                counter += 1
                self.ettac_counter_text.set(self.config.return_read(self.info_path,self.language,"fixes") + "(" + str(self.ettac_counter+1) + ")")
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
                    if "'" in name:
                        name = name.strip("'")
                    self.database.update_statistics(name)
                    self.coming_ettac_list.insert("end", "(P) "+name)
                    if "'" in name:
                        name = name.strip("'")
                    if name in on_aranan_ekler:
                        exit = True
                    else:
                        self.ettac_counter += 1 
                        self.search_ettac_list_name.config(text = self.config.return_read(self.info_path,self.language,"prefixes_to_search")+ "(" + str(self.ettac_counter+1) + ")")
                        self.ettac_counter_text.set(self.config.return_read(self.info_path,self.language,"fixes") + "(" + str(self.ettac_counter) + ")")
                        self.ek_sil("P")
                else:
                    self.ek_bas("P")
                    self.ara.screenshoot()
                    self.ara.crop_image()
                    name = self.ara.read_text("S")
                    if "'" in name:
                        name = name.strip("'")
                    self.database.update_statistics(name)
                    self.coming_ettac_list.insert("end", "(S) "+name)
                    if "'" in name:
                        name = name.strip("'")
                    if name in son_aranan_ekler:
                        exit = True
                    else:
                        self.ettac_counter += 1
                        self.search_ettac_list_name_s.config(text = self.config.return_read(self.info_path,self.language,"prefixes_to_search")+ "(" + str(self.ettac_counter+1) + ")")
                        self.ettac_counter_text.set(self.config.return_read(self.info_path,self.language,"fixes") + "(" + str(self.ettac_counter) + ")")
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
        self.chrome_bosses.grid_remove()
        self.deleteItemFrame.grid_remove()
    def run_passworDirectory(self):
        self.parent.title( self.config.return_read(self.info_path,self.language,"notice_7"))
        self.parent.geometry("645x300")
        self.remove_all_frame()
        
        self.treeBox = FancyListbox(self.idPasswd, font=("Helvatica bold", 12), justify=CENTER)
        self.treeBox_id = FancyListbox(self.idPasswd, font=("Helvatica bold", 12), justify=CENTER)
        self.treeBox_passwd = FancyListbox(self.idPasswd, font=("Helvatica bold", 12), justify=CENTER)
        self.id = Entry(self.idPasswd, font="Helvatica 12 bold")
        self.id.insert(0, self.config.return_read(self.info_path,self.language,"username"))
        self.id.bind("<Button-1>", self.clear_directory_id)
        self.passwd = Entry(self.idPasswd, font="Helvatica 12 bold")
        self.passwd.insert(0, self.config.return_read(self.info_path,self.language,"passwd"))
        self.passwd.bind("<Button-1>", self.clear_directory_passwd)

        self.add = Button(self.idPasswd, text=self.config.return_read(self.info_path,self.language,"add"), command=self.add_data)
        self.treeBox.grid(row=0, column=0, rowspan=4, columnspan=1, ipady=40)
        self.treeBox_id.grid(row=0, column=1, rowspan=4, columnspan=2, ipadx=50, ipady=40)
        self.treeBox_passwd.grid(row=0, column=3, rowspan=4, columnspan=3, ipadx=50, ipady=40)
        self.id.grid(row=4, column=0, columnspan=2, ipadx=50, padx=1)
        self.passwd.grid(row=4, column=2, columnspan=2, ipadx=50)
        self.add.grid(row=4, column=4, ipadx=20, pady=2)
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
        self.id.insert(0, self.config.return_read(self.info_path,self.language,"username"))
        self.passwd.delete(0, END)
        self.passwd.insert(0, self.config.return_read(self.info_path,self.language,"passwd"))
    def delete_contacs(self):
        try:
            pass
        except:
            showinfo(self.config.return_read(self.info_path,self.language,"notice_4"), self.config.return_read(self.info_path,self.language,"notice_10"))
        self.update_contacs()
    def add_data(self):
        self.database.add([self.id.get(), self.passwd.get()])
        self.update_contacs()
    def clear_directory_id(self, _):
        self.click = [True, False]
        if str(self.passwd.get()) == "":
            self.passwd.insert(0, self.config.return_read(self.info_path,self.language,"passwd"))
        if str(self.id.get()) == self.config.return_read(self.info_path,"english","username") or str(self.id.get()) == self.config.return_read(self.info_path,"turkish","username") or str(self.id.get()) == self.config.return_read(self.info_path,"german","username"):
            self.id.delete(0, END)
    def clear_directory_passwd(self, _):
        self.click = [False, True]
        if str(self.id.get()) == "":
            self.id.insert(0, self.config.return_read(self.info_path,self.language,"username"))
        if str(self.passwd.get()) == self.config.return_read(self.info_path,"english","passwd") or str(self.passwd.get()) == self.config.return_read(self.info_path,"turkish","passwd") or str(self.passwd.get()) == self.config.return_read(self.info_path,"german","passwd"):
            self.passwd.delete(0, END)
class config_parser:
    def return_read(address,id1,id2):
        config = configparser.ConfigParser()
        config.read(address)
        ans = config[id1][id2]
        return ans
    def write(address,name,new_name):
        config = configparser.ConfigParser()
        config.read(address)
        config["info"][name] =str( new_name)
        with open(address, 'w') as configfile:
            config.write(configfile)
    def return_section(address):
        config = configparser.ConfigParser()
        config.read(address)
        sec= config.sections()
        return sec


class database:
    def __init__(self):
        self.info = configparser.ConfigParser()
        self.path = "file\\"
        self.info.read(self.path+"config.ini")

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


        if not (os.path.isfile(self.path + self.info["info"]["attachments_statistics"])):
            baglan = sqlite3.connect(self.path + self.info["info"]["attachments_statistics"])
            veri = baglan.cursor()
            veri.execute("""CREATE TABLE {} (
                                            'attachments_name'	TEXT UNIQUE,
                                            'counter'	TEXT,
                                            PRIMARY KEY(attachments_name));""".format("attachments"))
            baglan.commit()
            baglan.close()
            self.create_statistics()
        else:
            pass
    def update_statistics(self,ek_name):
        baglan = sqlite3.connect(self.path + self.info["info"]["attachments_statistics"])
        veri = baglan.cursor()
        rows = veri.execute("SELECT * FROM attachments WHERE attachments_name=?", (ek_name,)).fetchone()
        if rows != None:
            sql = ''' UPDATE attachments
                      SET counter = ?
                  WHERE attachments_name = ?'''
            veri.execute(sql, ( str(int(rows[1])+1), ek_name))
        else:
            pass

        baglan.commit()
        baglan.close()
    def return_statistics(self):
        baglan = sqlite3.connect(self.path + self.info["info"]["attachments_statistics"])
        veri = baglan.cursor()
        values = veri.execute("select * from attachments").fetchall()
        baglan.commit()
        baglan.close()
        return values
    def create_statistics(self):
        attachments = []
        for i in range(15971,15981):
            if not i in (15979,15980):
                attachments.append(str(i)+".db")
        
        baglan = sqlite3.connect(self.path + self.info["info"]["attachments_statistics"])
        veri = baglan.cursor()
        for name in attachments:
            ekler = sqlite3.connect("file\\" + name)
            data = ekler.cursor()
            values = data.execute("select * from attachments_list").fetchall()
            for atchet in values:
                veri.execute("INSERT INTO attachments (attachments_name, counter) VALUES (?,?)", (atchet[0], "0"))
        ekler.commit()
        ekler.close()
        baglan.commit()
        baglan.close()
    def return_config_time(self):
        baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_config"])
        veri = baglan.cursor()
        values = veri.execute("select * from config").fetchall()
        return values[-1][0]
    def return_attachments_statistics(self):
        baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_config"])
        veri = baglan.cursor()
        values = veri.execute("select * from attachments_list").fetchall()
        array = []
        for i in values:
            array.append(i)
        return array
    def return_attachments_list(self,ek_name):

        if ek_name == self.info["turkish"]["armor_accuracy"] or ek_name == self.info["english"]["armor_accuracy"] or ek_name == self.info["german"]["armor_accuracy"]:
            name = "15972.db"
        elif ek_name == self.info["turkish"]["armor_experience_rate"] or ek_name == self.info["english"]["armor_experience_rate"] or ek_name == self.info["german"]["armor_experience_rate"]:
            name = "15973.db"
        elif ek_name == self.info["turkish"]["armor_drop_rate"] or ek_name == self.info["english"]["armor_drop_rate"] or ek_name == self.info["german"]["armor_drop_rate"]:
            name = "15978.db"
        elif ek_name == self.info["turkish"]["armor_pierce"] or ek_name == self.info["english"]["armor_pierce"] or ek_name == self.info["german"]["armor_pierce"]:
            name = "15979.db"
        elif ek_name == self.info["turkish"]["weapon_ra_accuracy"] or ek_name == self.info["english"]["weapon_ra_accuracy"] or ek_name == self.info["german"]["weapon_ra_accuracy"]:
            name = "15971.db"
        elif ek_name == self.info["turkish"]["weapon_accuracy"] or ek_name == self.info["english"]["weapon_accuracy"] or  ek_name == self.info["german"]["weapon_accuracy"]:
            name = "15976.db"
        elif ek_name == self.info["turkish"]["weapon_ra_attack"] or ek_name == self.info["english"]["weapon_ra_attack"] or ek_name == self.info["german"]["weapon_ra_attack"]:
            name = "15977.db"
        elif ek_name == self.info["turkish"]["weapon_weight"] or ek_name == self.info["english"]["weapon_weight"] or ek_name == self.info["german"]["weapon_weight"] :
            name = "15975.db"
        elif ek_name == self.info["turkish"]["weapon_pierce"] or ek_name == self.info["english"]["weapon_pierce"] or ek_name == self.info["german"]["weapon_pierce"]:
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
    def return_boss_names(self):
        baglan = sqlite3.connect(self.path + "14901.db")
        veri = baglan.cursor()
        values = veri.execute("select * from boss").fetchall()
        baglan.commit()
        baglan.close()
        return values
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
    def scroll_up():
        for _ in range(abs(60)):
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, win32con.WHEEL_DELTA, 0)

class search:
    def screenshoot(self):
        Screenshot = pyautogui.screenshot()
        Screenshot.save("image/ek.png")
    def crop_image(self):
        path = "file\\"
        info = configparser.ConfigParser()
        info.read(path + "config.ini")
        position = info[info["info"]["resolition"]]["img_right_area"].split(",")
        img = Image.open("image\\ek.PNG")
        img_right_area = (int(position[0]), int(position[1]), int(position[2]), int(position[3]))
        img_right = img.crop(img_right_area)
        img_right.save("image\\cropped.png")
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
    
