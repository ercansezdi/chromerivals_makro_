#!/usr/bin/env python
# -*-coding:utf8-*-
from tkinter import *
import pyautogui
import cv2
import pytesseract
import threading
import keyboard
from tkinter.messagebox import showinfo
import os
import ctypes
import pymongo
import tkinter.ttk
from tkinter import ttk
import datetime
from time import sleep
import sqlite3
import configparser
from tkinter import messagebox
import random
from PIL import Image, ImageTk, ImageFont, ImageDraw


class tkinterGui(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("ToolBox")
        self.parent.geometry("147x197")
        self.variables()
        self.InitGui()

    def InitGui(self):
        ## Airrivals ##
        # Airrivals Menu Screen
        self.timer_button_1 = Button(self.air_toolbox, text="Timer", font=("Helvatica bold", 12),
                                     command=self.run_timer)
        self.timer_button_1.grid(row=0, column=0)
        self.timer_button_2 = Button(self.air_toolbox, text="Auto Upgrade", font=("Helvatica bold", 12),
                                     command=self.run_autoUpgrade)
        self.timer_button_2.grid(row=0, column=1)
        self.timer_button_3 = Button(self.air_toolbox, text="Calc Exp", font=("Helvatica bold", 12),
                                     command=self.run_calcExp)
        self.timer_button_3.grid(row=0, column=2)
        self.timer_button_4 = Button(self.air_toolbox, text="Item Destroy", font=("Helvatica bold", 12),
                                     command=self.run_destroy)
        self.timer_button_4.grid(row=0, column=3)
        self.timer_button_5 = Button(self.air_toolbox, text="Auto Buff", font=("Helvatica bold", 12),
                                     command=self.run_otoBuf)
        self.timer_button_5.grid(row=0, column=4)
        self.timer_button_6 = Button(self.air_toolbox, text="Id Pass", font=("Helvatica bold", 12),
                                     command=self.run_passworDirectory)
        self.timer_button_6.grid(row=0, column=5)
        self.timer_button_7 = Button(self.air_toolbox, text="Killmark", font=("Helvatica bold", 12),
                                     command=self.run_killmark)
        self.timer_button_7.grid(row=0, column=6)
        # Password Directory Screen

        self.treeBox = FancyListbox(self.idPasswd, font=("Helvatica bold", 12), justify=CENTER)
        self.treeBox.grid(row=0, column=0, rowspan=4, columnspan=1, ipady=40)
        self.treeBox_id = FancyListbox(self.idPasswd, font=("Helvatica bold", 12), justify=CENTER)
        self.treeBox_id.grid(row=0, column=1, rowspan=4, columnspan=2, ipadx=50, ipady=40)
        self.treeBox_passwd = FancyListbox(self.idPasswd, font=("Helvatica bold", 12), justify=CENTER)
        self.treeBox_passwd.grid(row=0, column=3, rowspan=4, columnspan=3, ipadx=50, ipady=40)

        self.id = Entry(self.idPasswd, font="Helvatica 12 bold")
        self.id.grid(row=4, column=0, columnspan=2, ipadx=50, padx=1)
        self.id.insert(0, "Kullanıcı Adı")
        self.id.bind("<Button-1>", self.clear_directory_id)
        self.passwd = Entry(self.idPasswd, font="Helvatica 12 bold")
        self.passwd.grid(row=4, column=2, columnspan=2, ipadx=50)
        self.passwd.insert(0, "Şifre")
        self.passwd.bind("<Button-1>", self.clear_directory_passwd)

        self.add = Button(self.idPasswd, text="EKLE", command=self.add_data)
        self.add.grid(row=4, column=4, ipadx=20, pady=2)

        self.text = Label(self.expCalc, text="Exp  : ", font="Helvatica 12 bold")
        self.text.grid(row=0, column=0, columnspan=1)
        self.wExp = Entry(self.expCalc, font="Helvatica 12 bold")
        self.wExp.grid(row=0, column=2, columnspan=3)
        self.basla_x = Button(self.expCalc, text="Hesapla", command=self.calculate_exp, font="Helvatica 12 bold")
        self.basla_x.grid(row=1, column=2, ipadx=60, columnspan=4)
        self.label = Label(self.expCalc, textvariable=self.calc_exp_string, font="Helvatica 12 bold")
        self.label.grid(row=2, column=2, columnspan=4)
        # Timer Screen
        self.canvas = Canvas(self.timer, width=450, height=500)
        self.img = ImageTk.PhotoImage(Image.open("file/bg.png").resize((550, 320), Image.ANTIALIAS))  #
        self.canvas.background = self.img  #
        self.bg = self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        self.canvas.grid(row=0, column=0, columnspan=94, rowspan=24)

        self.label_1 = Label(self.timer, text="Saat", font="Helvatica 12 bold", justify='center', bg="#CCCCCC")
        self.label_1.grid(row=0, column=0, columnspan=1)
        self.label_2 = Label(self.timer, text="Dakika", font="Helvatica 12 bold", justify='center', bg="#CCCCCC")
        self.label_2.grid(row=0, column=1, columnspan=1)
        self.label_3 = Label(self.timer, text="Zaman Fark(Sn)", font="Helvatica 12 bold", justify='center',
                             bg="#CCCCCC")
        self.label_3.grid(row=0, column=2, columnspan=1)
        self.entry_1 = Entry(self.timer, font="Helvatica 12 bold", justify='center')
        self.entry_1.insert(0, "00")
        self.entry_1.grid(row=1, column=0, columnspan=1)
        self.entry_2 = Entry(self.timer, font="Helvatica 12 bold", justify='center')
        self.entry_2.insert(0, "00")
        self.entry_2.grid(row=1, column=1, columnspan=1)
        self.entry_3 = Entry(self.timer, font="Helvatica 12 bold", justify='center')
        self.entry_3.insert(0, "00")
        self.entry_3.grid(row=1, column=2, columnspan=1)

        self.sifirla = Button(self.timer, text="Sıfırla ", font="Helvatica 12 bold", justify='center',
                              command=self.reset)
        self.sifirla.grid(row=2, column=0, columnspan=1, ipadx=30)

        self.zaman_ayarla = Button(self.timer, text="Farkı Ayarla", font="Helvatica 12 bold", justify='center',
                                   command=self.fark_ayarla)
        self.zaman_ayarla.grid(row=2, column=1, columnspan=1, ipadx=30)

        self.degistir = Button(self.timer, text="Değiştir ", font="Helvatica 12 bold", justify='center',
                               command=self.change)
        self.degistir.grid(row=2, column=2, columnspan=1, ipadx=30)
        self.batik = Button(self.timer, image=self.batik_img, command=self.batik_click)
        self.batik.grid(row=4, column=0, padx=9, columnspan=1)
        self.kul = Button(self.timer, image=self.kul_img, command=self.kul_click)
        self.kul.grid(row=5, column=0, padx=9, columnspan=1)

        self.batik_clock = Label(self.timer, textvariable=self.batik_time, font="Helvatica 30 bold", justify='center',
                                 bg="#CCCCCC")
        self.batik_clock.grid(row=4, column=1, columnspan=1)

        self.last_clock_batik = Label(self.timer, textvariable=self.last_batik, font="Helvatica 30 bold",
                                      justify='center',
                                      bg="#CCCCCC")
        self.last_clock_batik.grid(row=4, column=2, columnspan=1)

        self.last_batik.set("00:00:00")
        # 14:22
        self.batik_time.set("00:00:00")
        self.kul_clock = Label(self.timer, textvariable=self.kul_time, font="Helvatica 30 bold", justify='center',
                               bg="#CCCCCC")
        self.kul_clock.grid(row=5, column=1, columnspan=1)
        self.kul_time.set("00:00:00")

        self.last_clock_kul = Label(self.timer, textvariable=self.last_kul, font="Helvatica 30 bold", justify='center',
                                    bg="#CCCCCC")
        self.last_clock_kul.grid(row=5, column=2, columnspan=1)

        self.last_kul.set("00:00:00")
        # İtem Destroy Screen
        self.text_T = Label(self.iDestroy, text="İtem Sayısı : ", font="Helvatica 12 bold")
        self.text_T.grid(row=0, column=0, columnspan=2)
        self.numberOfItems_T = Entry(self.iDestroy, font="Helvatica 12 bold", width=10)
        self.numberOfItems_T.grid(row=0, column=2, columnspan=2)
        self.numberOfItems_T.insert(0, "1")
        self.text_satir = Label(self.iDestroy, text="Satir", font="Helvatica 12 bold")
        self.text_satir.grid(row=1, column=0, columnspan=1)
        self.text_satir1 = Entry(self.iDestroy, font="Helvatica 12 bold", width=5)
        self.text_satir1.grid(row=1, column=1, columnspan=1)
        self.text_satir1.insert(0, "1")
        self.text_sutun = Label(self.iDestroy, text="Sutun", font="Helvatica 12 bold")
        self.text_sutun.grid(row=1, column=2, columnspan=1)
        self.text_sutun1 = Entry(self.iDestroy, font="Helvatica 12 bold", width=5)
        self.text_sutun1.grid(row=1, column=3, columnspan=1)
        self.text_sutun1.insert(0, "1")
        self.basla_T = Button(self.iDestroy, text="Parçala", command=self.check_destroy, font="Helvatica 12 bold")
        self.basla_T.grid(row=2, column=1, ipadx=10, columnspan=4)
        # Upgrade Item Screen
        self.text = Label(self.upgrade, text="İtem Sayısı : ", font="Helvatica 12 bold")
        self.text.grid(row=0, column=0, columnspan=2)
        self.numberOfItems = Entry(self.upgrade, font="Helvatica 12 bold")
        self.numberOfItems.grid(row=0, column=2, columnspan=2)
        self.text_2 = Label(self.upgrade, text="Upgrade Sayısı : ", font="Helvatica 12 bold")
        self.text_2.grid(row=1, column=0, columnspan=2)
        self.upgradeOfItems = Entry(self.upgrade, font="Helvatica 12 bold")
        self.upgradeOfItems.grid(row=1, column=2, columnspan=2)
        self.basla_ = Button(self.upgrade, text="Basla", command=self.check_upgrade, font="Helvatica 12 bold")
        self.basla_.grid(row=2, column=0, ipadx=60, columnspan=3)
        self.checkButton = Checkbutton(self.upgrade, text="e5 Upgrade", variable=self.var)
        self.checkButton.grid(row=2, column=3, columnspan=1)
        # Auto Buff Screen
        self.relog_time_text = Label(self.autoBuff, text="Relog Süresi (Sn) ", font="Helvatica 12 bold")
        self.relog_time_text.grid(row=0, column=0)
        self.relog_time_entry = Entry(self.autoBuff, font="Helvatica 12 bold")
        self.relog_time_entry.grid(row=0, column=1)
        self.relog_time_entry.insert(0, 0)
        self.autobuf_continuous = Button(self.autoBuff, text="Başlat", command=self.buf_control,
                                         font="Helvatica 12 bold")
        self.autobuf_continuous.grid(row=1, column=0, ipadx=100, ipady=5, padx=25, columnspan=2, pady=10)
                                    ## Chromerivals ##
        #SP Time

        self.sp_time = Button(self.chrome_main_frame, text="SP Time", font=("Helvatica bold", 12),
                              command=self.sp_time_)
        self.sp_time.grid(row=0, column=0)
        self.idPass = Button(self.chrome_main_frame, text="ID-PASS", font=("Helvatica bold", 12),
                              command=self.chrome_directory)
        self.idPass.grid(row=0, column=1)

        self.attec = Button(self.chrome_main_frame, text="Search" , font = ("Helvatica bold", 12),
                              command=self.search_ek)
        self.attec.grid(row=0,column=2)

        img = ImageTk.PhotoImage(
            Image.open("file/chrome.jpg").resize((402, 202), Image.ANTIALIAS))  #
        self.chrome_background.background = img  #
        self.bg_info = self.chrome_background.create_image(0, 0, anchor=NW, image=img)  #

        self.chrome_background.grid(row=0, column=0, columnspan=94, rowspan=24)


        self.ch_back_pic = PhotoImage(file='file/back.png')
        self.ch_back = Button(self.sp_time_frame, image=self.ch_back_pic, command=self.ch_back_func)
        self.ch_back.grid(row=0,column=90,pady=5)

        self.ch_reload_pic = PhotoImage(file='file/reload.png')
        self.ch_reload = Button(self.sp_time_frame, image=self.ch_reload_pic, command=self.ch_reload_func)
        self.ch_reload.grid(row=1, column=90, pady=0)
        # Search attachment

        self.chrome_combo_ekList = ttk.Combobox(self.chrome_search_attachment, width=24, textvariable=self.search_combo)
        self.chrome_combo_ekList['values'] = (' Perde Olasılık Ekleri',
                                              ' Perde tecrübe-Nesne Ekleri',
                                              ' Silah Ra-Olasılık Ekleri',
                                              ' Silah Olasılık Ekleri',
                                              ' Silah Ra-Atak Ekleri',
                                              ' Silah Ağırlık Ekleri',
                                              ' PET Ekleri')
        #self.chrome_combo_ekList.bind('<Button-1>', self.set_fixes)
        self.get_fixes = Button(self.chrome_search_attachment, text="Ekleri Getir", font=("Helvatica bold", 10),bg="purple",
                                 command=self.set_fixes)
        self.ettac_list = Listbox(self.chrome_search_attachment,font = ("Helvatica bold", 12),selectmode='multiple')
        self.search_add = Button(self.chrome_search_attachment,text = ">",font = ("Helvatica bold", 14),command=self.ettac_add)
        self.search_remove = Button(self.chrome_search_attachment, text = "<",font = ("Helvatica bold", 14),command = self.ettac_remove)
        self.search_ettac_list_name = Label(self.chrome_search_attachment, text = "Aranan Ekler",font = ("Helvatica bold", 12),bg = "red")
        self.search_ettac_list = Listbox(self.chrome_search_attachment,font = ("Helvatica bold", 12),selectmode='multiple')
        self.coming_ettac = Label(self.chrome_search_attachment, bg="green", textvariable = self.ettac_counter_text)
        self.coming_ettac_list = Listbox(self.chrome_search_attachment,font = ("Helvatica bold", 12))
        self.ettac_counter_text.set("Gelen Ekler ("+ str(self.ettac_counter)+")")
        self.number_of_ettac = Entry(self.chrome_search_attachment,font = ("Helvatica bold", 12),bg="green",fg="white")
        self.number_of_ettac.insert(0,"Ek Sayısı")
        self.number_of_ettac.bind("<1>", self.clear_number_of_ettac)
        self.search_start_stop = Button(self.chrome_search_attachment, text="Başlat",font = ("Helvatica bold", 12),command= self.ettac_check)
        self.ettac_back = Button(self.chrome_search_attachment, text = "Geri" ,font = ("Helvatica bold", 12), command = self.ettac_back_func)
        self.ettac_frame = Frame(self.chrome_search_attachment)
        self.ettac_P = Checkbutton(self.ettac_frame, text="P", variable=self.checkVars_1,onvalue=1, offvalue=0)
        self.ettac_S = Checkbutton(self.ettac_frame, text="S", variable=self.checkVars_2,onvalue=1, offvalue=0)
        self.ettac_P.grid(row=0, column=0)
        self.ettac_S.grid(row=0, column=1)
        self.chrome_combo_ekList.grid(row=0,column=0)
        self.get_fixes.grid(row=0,column=1)
        self.ettac_list.grid(row=1,column=0,rowspan=2)
        self.search_add.grid(row=1, column=1,columnspan=1)
        self.search_remove.grid(row=2,column=1,columnspan=1)

        self.search_ettac_list_name.grid(row=0,column=2)
        self.search_ettac_list.grid(row=1,column=2,rowspan=2)
        self.coming_ettac.grid(row=0,column=3)
        self.coming_ettac_list.grid(row=1,column=3,rowspan=2)
        self.number_of_ettac.grid(row=3,column=0)
        self.search_start_stop.grid(row=3,column=2,ipadx=10)
        self.ettac_back.grid(row=3,column=3,ipadx=10)
        self.ettac_frame.grid(row=3,column=1)
        # Download Lib

        self.downloadButton = Button(self.downloadLib, text = "Download Lib.",font = ("Helvatica bold", 20), command = self.download_function,bg="blue")
        self.downloadButton.grid(row=0,column=0)

                    ## Main Screen  ##

        self.appNames = Listbox(self.mainFrame, font=("Helvatica bold", 12), justify=CENTER)
        self.appNames.grid(row=0, column=0, rowspan=4, columnspan=1, ipady=1)
        for values in self.appName:
            self.appNames.insert(END, values)
        self.mainFrame_button = Button(self.mainFrame, text="Open App", command=self.open_app,
                                       font=("Helvatica bold", 15))
        self.mainFrame_button.grid(row=5, column=0, columnspan=2, ipadx=33)


        self.appNames.selection_set(0)
    def variables(self):
        self.timer = Frame(self.parent)

        self.upgrade = Frame(self.parent)
        self.expCalc = Frame(self.parent)
        self.idPasswd = Frame(self.parent)
        self.iDestroy = Frame(self.parent)
        self.autoBuff = Frame(self.parent)
        self.ikillmark = Frame(self.parent)
        self.buff_contunie = Frame(self.parent)
        self.buf_discontunie = Frame(self.parent)
        self.air_main_frame = Frame(self.parent)
        self.air_toolbox = Frame(self.air_main_frame)
        self.air_toolbox.grid(row=0, column=0)
        # self.air_main_frame.grid(row=0,column=0)
        self.chrome_main_frame = Frame(self.parent)
        self.sp_time_frame = Frame(self.parent)
        self.chrome_idPass_Frame = Frame(self.parent)
        self.chrome_search_attachment = Frame(self.parent)
        self.checkVars_1 = IntVar()
        self.checkVars_2 = IntVar()
        self.search_combo = StringVar()

        self.mainFrame = Frame(self.parent)
        self.table_builder_frame = Frame(self.parent)
        self.mainFrame.grid(row=0, column=0)
        self.downloadLib = Frame(self.parent)

        self.click = [False, False]
        self.database = database()
        self.database.create()
        self.ara = search()
        self.movement = movemont
        self.sayac = 0
        self.calc_exp_string = StringVar()
        self.exp = []
        self.batik_img = ImageTk.PhotoImage(
            Image.open("file/batik.png").resize((125, 60), Image.ANTIALIAS))
        self.kul_img = ImageTk.PhotoImage(
            Image.open("file/kul.PNG").resize((125, 60), Image.ANTIALIAS))
        self.batik_bg = ImageTk.PhotoImage(Image.open("file/batik_bg.png").resize((550, 320), Image.ANTIALIAS))
        self.kul_bg = ImageTk.PhotoImage(Image.open("file/kul_bg.png").resize((550, 320), Image.ANTIALIAS))
        self.batik_time = StringVar()
        self.kul_time = StringVar()
        self.last_batik = StringVar()
        self.last_kul = StringVar()

        self.login = True
        self.path = "file\\"
        self.info = configparser.ConfigParser()
        self.info.read(self.path + "config.ini")
        self.islem = [False, False]
        self.var = IntVar()
        self.autoBuff_tick = False
        self.appName = ["Chromerivals", "Airrivals", "Library Downloader"]
        self.appFrame = [self.chrome_main_frame, self.air_main_frame, self.downloadLib]
        self.appGeometry = ["167x27", "440x30", "140x40"]
        self.chrome_background = Canvas(self.sp_time_frame, width=402, height=202)
        self.ch_loop_exit = True
        self.attec_array = []
        self.ettac_counter_text = StringVar()
        self.ettac_counter = 0
    def set_fixes(self):
        ek_name = self.chrome_combo_ekList.get()
        attachments = self.database.return_attachments_list(ek_name)
        for i in range(0,self.ettac_list.size()):
            self.ettac_list.delete(0,"end")
        for i in attachments:
            self.ettac_list.insert(END, i)
    def clear_number_of_ettac(self,_):
        if self.number_of_ettac.get() == "Ek Sayısı":
            self.number_of_ettac.delete(0,"end")

    def ettac_back_func(self):
        self.remove_all_frame()
        self.parent.geometry("167x27")
        self.chrome_main_frame.grid(row=0,column=0)
    def search_ek(self):
        self.remove_all_frame()
        self.chrome_search_attachment.grid(row=0,column=0)
        self.parent.geometry("500x220")
    def ettac_check(self):
        if int(self.search_ettac_list.size()) == 0:
            showinfo("Uyarı", "Aranacak ek seçilmemiş.")
        else:
            if self.number_of_ettac.get().isnumeric():
                if (self.checkVars_2.get() == 0 and self.checkVars_1.get() == 0) or (self.checkVars_2.get() == 1 and self.checkVars_1.get() == 1):
                    showinfo("Uyarı", "Hangi ek kullanılacağı seçilmemiş \nveya\n Yanlış seçilmiş.")
                else:
                    self.ettac_counter = 0
                    self.ettac_counter_text.set("Gelen Ekler (" + str(self.ettac_counter) + ")")
                    treading = threading.Thread(target=self.start_ettac)
                    treading.start()
                    #self.start_ettac()
            else:
                showinfo("Uyarı", "Ek sayısı yanlış girilmiş.")
    def ettac_add(self):
        selected_ettec_list = self.ettac_list.curselection()

        ettec_name =  self.search_ettac_list.get(0,END)


        for num in selected_ettec_list:
            if not self.ettac_list.get(num) in ettec_name:
                self.search_ettac_list.insert(END, self.ettac_list.get(num))
    def ettac_remove(self):
        selected_ettec_search = self.search_ettac_list.curselection()
        for i in selected_ettec_search:
            self.search_ettac_list.delete(i)
    def start_ettac(self):
        #self.movement.move(640, 720)  # kart
        #self.movement.doubleClick()
        #self.movement.click_button()
        #self.movement.move(640, 840)  # silme
        #self.movement.move(670, 840)  # Basma
        #self.movement.move(700, 840)  # perde silah
        #self.movement.move(1270, 690)  # Ek bas onay butonu

        counter = 0
        aranan_ekler = []
        for i in self.search_ettac_list.get(0,END):
            aranan_ekler.append(i)
        while counter < int(self.number_of_ettac.get()):
            if keyboard.is_pressed('space'):
                counter = int(self.number_of_ettac.get())+1
            self.ek_bas()
            self.ara.screenshoot()
            self.ara.crop_image()
            if self.checkVars_1.get() == 1 and self.checkVars_2.getvar() == 0:
                name = self.ara.read_text("P")
            else:
                name = self.ara.read_text("S")


            if name in aranan_ekler:
                counter = int(self.number_of_ettac.get())
                self.coming_ettac_list.insert("end", name)
            else:
                self.ettac_counter += 1
                self.coming_ettac_list.insert("end",name)
                self.ettac_counter_text.set("Gelen Ekler (" + str(self.ettac_counter) + ")")
                self.ek_sil()

            counter += 1
    def ek_bas(self):
        self.movement.move(670, 840)
        sleep(0.1)
        self.movement.doubleClick()
        sleep(0.1)
        self.movement.move(700, 840)
        sleep(0.1)
        self.movement.doubleClick()
        sleep(0.1)
        self.movement.move(1270, 690)
        sleep(0.1)
        self.movement.click_button()
        sleep(0.2)
        self.movement.click_button()
    def ek_sil(self):
        self.movement.move(640, 840)
        sleep(0.1)
        self.movement.doubleClick()
        sleep(0.1)
        self.movement.move(700, 840)  # perde silah
        sleep(0.1)
        self.movement.doubleClick()
        sleep(0.1)
        self.movement.move(1270, 690)  # Ek bas onay butonu
        sleep(0.1)
        self.movement.click_button()
        sleep(0.2)
        self.movement.click_button()
    def chrome_directory(self):


        self.remove = Button(self.idPasswd, text="GERİ", command=self.ch_idPass_back)
        self.remove.grid(row=4, column=5, ipadx=20, pady=2)

        self.run_passworDirectory()
    def ch_idPass_back(self):
        self.remove_all_frame()
        self.parent.geometry("167x27")
        self.chrome_main_frame.grid(row=0, column=0)
    def ch_back_func(self):
        self.remove_all_frame()
        self.ch_loop_exit = False
        self.parent.geometry("167x27")
        self.chrome_main_frame.grid(row=0,column=0)
    def ch_reload_func(self):
        self.remove_all_frame()
        self.ch_loop_exit = False
        root.after(1000, run.sp_time_)

    def download_function(self):
        libs = ["keyboard", "pillow", "pymongo", "pymongo[srv]","opencv","pytesseract"]
        for i in libs:
            os.system("pip install " + i)


    def open_app(self):
        selected_app = self.appNames.get(ACTIVE)

        for appName, appFrame, appGeo in zip(self.appName, self.appFrame, self.appGeometry):
            if appName == selected_app:
                self.mainFrame.grid_remove()
                self.parent.title(appName)
                appFrame.grid(row=0, column=0)
                self.parent.geometry(appGeo),
    def sp_time_(self):
        self.sp_hours = ["01:05", "02:55", "04:45", "06:35", "08:25", "10:15", "12:05", "13:55", "15:45", "17:35",
                         "21:15", "23:05"]

        today = datetime.datetime.today() - datetime.timedelta(minutes=120)
        day = today.strftime("%d.%m.%Y")
        for time in self.sp_hours:
            sp_time = datetime.datetime.strptime(day + "-" + time, "%d.%m.%Y-%H:%M")
            if today < sp_time:
                self.next_sp_time = sp_time
                break
        self.remove_all_frame()
        self.sp_time_frame.grid(row=1, column=0)
        self.parent.geometry(str(402) + "x" + str(202))
        self.ch_loop_exit = True
        self.sp_time_loop()
    def sp_time_loop(self):
        counter = 0
        while counter < len(self.sp_hours):
            today = datetime.datetime.today() - datetime.timedelta(minutes=120)
            sp_time = datetime.datetime.strptime(today.strftime("%d.%m.%Y") + "-" + self.sp_hours[counter], "%d.%m.%Y-%H:%M")
            if today < sp_time:
                self.next_sp_time = sp_time
                break
            counter += 1
            last_sp_time = datetime.datetime.strptime(today.strftime("%d.%m.%Y") + "-" + self.sp_hours[counter - 1], "%d.%m.%Y-%H:%M")
        if counter == len(self.sp_hours):
            last_sp_time = datetime.datetime.strptime(today.strftime("%d.%m.%Y") + "-" + self.sp_hours[-1],"%d.%m.%Y-%H:%M")
            self.next_sp_time = datetime.datetime.strptime(today.strftime("%d.%m.%Y") + "-" + self.sp_hours[counter - 1], "%d.%m.%Y-%H:%M") + datetime.timedelta(minutes=120)
        sp = self.next_sp_time - today

        img = Image.open("file/chrome.jpg")

        d = ImageDraw.Draw(img)
        d.text((700, 25), str(last_sp_time.strftime("%H:%M:%S")), font=ImageFont.truetype('file/javatext.ttf', 80),
               fill=(0, 0, 0))
        d.text((700, 160), "0"+str(sp).split(".")[0],
               font=ImageFont.truetype('file/javatext.ttf', 80),fill=(0, 0, 0))

        d.text((700, 290), (sp_time.strftime("%H:%M:%S")), font=ImageFont.truetype('file/javatext.ttf', 80),
               fill=(0, 0, 0))

        today = datetime.datetime.today() - datetime.timedelta(minutes=120)
        d.text((20, 510), today.strftime("%d/%m/%Y") + " - " + today.strftime("%H:%M:%S"), font=ImageFont.truetype('file/javatext.ttf', 80),
               fill=(0, 0, 0))

        img.save("file/chromerivals_sp_time.jpg")
        self.img = ImageTk.PhotoImage(
            Image.open("file/chromerivals_sp_time.jpg").resize((402, 202), Image.ANTIALIAS))  #

        self.chrome_background.itemconfig(self.bg_info, image=self.img)
        self.chrome_background.update

        if self.ch_loop_exit:
            root.after(1000, run.sp_time_loop)
    def kill_mark(self):
        for i in range(0, int(self.ent.get())):
            self.movement.move(810, 1050)
            self.movement.doubleClick()
            sleep(0.1)
            self.movement.move(935, 565)
            self.movement.click_button()
            sleep(0.1)
        self.toaster.show_toast("Airrivals", "İşlem Tamamlandı", threaded=True, icon_path=None, duration=3)
        self.toaster.notification_active()
    def remove_all_frame(self):
        self.timer.grid_remove()
        self.upgrade.grid_remove()
        self.expCalc.grid_remove()
        self.idPasswd.grid_remove()
        self.iDestroy.grid_remove()
        self.buf_discontunie.grid_remove()
        self.buff_contunie.grid_remove()
        self.ikillmark.grid_remove()
        self.autoBuff.grid_remove()
        self.chrome_main_frame.grid_remove()
        self.sp_time_frame.grid_remove()
        self.chrome_idPass_Frame.grid_remove()
        self.chrome_search_attachment.grid_remove()
    def run_killmark(self):
        self.parent.title("Killmark")
        showinfo("Uyarı", "Oyuna Etki etmesi için\n Yönetici olarak çalıştırınız. !")
        self.parent.geometry("385x100")
        self.remove_all_frame()
        self.ikillmark.grid(row=1, column=0)

        self.text = Label(self.ikillmark, text="Killmark Sayısı", font="Helvatica 12 bold")
        self.text.grid(row=0, column=0)
        self.ent = Entry(self.ikillmark, font="Helvatica 12 bold")
        self.ent.grid(row=0, column=1)
        self.ent.insert(0, 0)
        self.st = Button(self.ikillmark, text="Başlat", command=self.check_killmark,
                         font="Helvatica 12 bold")
        self.st.grid(row=1, column=0, ipadx=100, ipady=5, padx=25, columnspan=2, pady=10)
    def check_killmark(self):
        if self.ent.get() == "":
            showinfo("HATA !", "Boş Bırakılamaz !!")
        else:
            if self.ent.get().isnumeric():
                showinfo("UYARI !", "3 Saniye İçinde Ekrana Geçiniz.")
                self.date = datetime.datetime.today() + datetime.timedelta(seconds=3)
                self.waiting_killmark()
            else:
                showinfo("HATA !", "Harf Girilemez !")
    def waiting_killmark(self):
        if datetime.datetime.today() > self.date:
            self.kill_mark()
        else:
            root.after(500, run.waiting_killmark)
    def run_otoBuf(self):
        self.popup = Toplevel()
        self.verification_label_1 = Label(self.popup,
                                          text="Bu uygulamayı yönetici tarafından şifrelenmiştir. \nUygulamayı kullanmak için şifre girmeniz gerekmektedir.",
                                          font="Helvatica 12 bold")
        self.verification_label_1.grid(row=0, column=0, columnspan=3)
        self.verification_label_2 = Label(self.popup, text="Şifre :", font="Helvatica 12 bold")
        self.verification_label_2.grid(row=1, column=0)
        self.verification_entry = Entry(self.popup, font="Helvatica 12 bold")
        self.verification_entry.grid(row=1, column=1)
        self.verification_button = Button(self.popup, text="Onayla", command=self.run_otoBuf_start,
                                          font="Helvatica 12 bold")
        self.verification_button.grid(row=2, column=0, columnspan=3)
    def run_otoBuf_start(self):
        passwd = self.verification_entry.get()
        self.popup.destroy()
        if passwd == "147896325":
            self.parent.title("Auto Buff")
            showinfo("Uyarı", "Oyuna Etki etmesi için\n Yönetici olarak çalıştırınız. !")
            self.parent.geometry("385x100")
            self.remove_all_frame()
            self.autoBuff.grid(row=1, column=0)
        else:
            showinfo("Uyarı", "Şifreyi yanlış girdiniz. !")
    def buf_control(self):
        question = messagebox.askquestion('Doğrulayınız',
                                          "Relog Süresi 0 ise 6 dk bir buff vermektendir. Relog süresi 0'dan farklı ise buf verip girilen süre kadar sonra relog'a çıkıp tekrar buf vermektedir. \n 0 - Akıllı Sp 1, 2 ve 3. skill barına istediğiniz buf skilini koyabilirsiniz. Bu ayarlamalar 1. skill penceresi için geçerlidir. Gerekli ayarlamalardan emin misiniz ? ",
                                          icon='warning')
        if question == "yes":
            self.autoBuff_tick = True
            sleep(3)
            self.autobuff_loop()
        else:
            showinfo("Uyarı", "Gerekli ayarlamalar sonra tekrar bekleriz !")
    def autobuff_loop(self):

        if self.relog_time_entry.get() == "0":
            self.open_buf()
            if self.autoBuff_tick:
                root.after(360000, run.autobuff_loop)
        elif int(self.relog_time_entry.get()) < 0:
            pass
        else:
            self.open_buf()
            if self.autoBuff_tick:
                sleep(int(self.relog_time_entry.get()))
                self.relog()
    def autobuff_relog_timer(self):
        root.after(1000, run.autobuff_loop)
    def open_buf(self):
        self.movement.move(810, 1050)
        self.movement.doubleClick()
        sleep(0.3)
        self.move(840, 1050)
        self.movement.doubleClick()
        sleep(0.3)
        self.movement.move(870, 1050)
        self.movement.doubleClick()
        sleep(0.3)
        self.movement.move(900, 1050)
        self.movement.doubleClick()
    def relog(self):
        keyboard.press("escape")
        keyboard.release("escape")
        self.movement.move(1000, 760)
        self.move.click_button()
        sleep(20)
        self.movement.doubleClick()
        sleep(10)
        keyboard.press_and_release('b')
        keyboard.press("enter")
        keyboard.release("enter")
        root.after(100, run.autobuff_loop)
    def check_upgrade(self):
        if self.numberOfItems.get() == "" or self.upgradeOfItems.get() == "":
            showinfo("HATA !", "Boş Bırakılamaz !!")
        else:
            if self.numberOfItems.get().isnumeric() and self.upgradeOfItems.get().isnumeric():
                showinfo("UYARI !", "3 Saniye İçinde Ekrana Geçiniz.")
                self.date = datetime.datetime.today() + datetime.timedelta(seconds=3)
                self.waiting_upgrade()
            else:
                showinfo("HATA !", "Harf Girilemez !")
    def waiting_upgrade(self):
        if datetime.datetime.today() > self.date:
            self.start_upgrade()
        else:
            root.after(500, run.waiting_upgrade)
    def start_upgrade(self):
        yukseltim = int(self.upgradeOfItems.get()) * int(self.numberOfItems.get())
        for i in range(0, yukseltim):
            self.movement.move(640, 720)  # kart
            self.movement.doubleClick()
            sleep(0.1)
            self.movement.move(670, 720)  # item
            self.movement.doubleClick()
            sleep(0.1)
            self.movement.move(1270, 690)  # onay
            self.movement.click_button()
            self.movement.click_button()
            sleep(0.1)
            self.movement.move(540, 550)
            sleep(0.1)
            if int(self.var.get()) == 0:
                self.movement.move(1270, 690)  # onay
                self.movement.click_button()
                self.movement.click_button()
                sleep(0.1)

            else:
                self.movement.move(955, 555)
                rst = random.randint(0, 100)
                self.movement.click_button()
                self.movement.click_button()

                sleep(0.1)

                self.movement.move(1270, 690)
                # while rst > 0.5:

                #    if rst < 0.5:
                self.movement.click_button()
                self.movement.click_button()

                sleep(0.1)
                self.movement.move(995, 555)
                sleep(0.1)
                self.movement.move(1270, 690)
                self.movement.click_button()
                self.movement.click_button()
    def run_autoUpgrade(self):
        self.parent.title("Auto Upgrade")
        showinfo("Uyarı", "Oyuna Etki etmesi için\n Yönetici olarak çalıştırınız. !")
        self.parent.geometry("385x100")
        self.remove_all_frame()
        self.upgrade.grid(row=1, column=0)
    def check_destroy(self):
        if self.numberOfItems_T.get() == "":
            showinfo("HATA !", "Boş Bırakılamaz !!")
        else:
            if self.numberOfItems_T.get().isnumeric():
                if int(self.text_sutun1.get()) > 10 or int(self.text_satir1.get()) > 10:
                    showinfo("HATA !", "Satır ve Sutun 10'dan fazla olamaz !")
                else:
                    showinfo("UYARI !", "3 Saniye İçinde Ekrana Geçiniz.")

                    self.date = datetime.datetime.today() + datetime.timedelta(seconds=3)
                    self.waiting_destroy()
            else:
                showinfo("HATA !", "Harf Girilemez !")
    def waiting_destroy(self):
        if datetime.datetime.today() > self.date:
            self.start_destroy()
        else:
            root.after(500, run.waiting_destroy)
    def start_destroy(self):
        yukseltim = int(self.numberOfItems_T.get())
        for i in range(0, yukseltim):
            if int(self.text_sutun1.get()) < 5:
                self.movement.move(640 + (int(self.text_sutun1.get()) - 1) * 30,
                                   720 + (int(self.text_satir1.get()) - 1) * 30)
            else:
                self.movement.move(480 + (int(self.text_sutun1.get()) - 1) * 30,
                                   570 + (int(self.text_satir1.get()) - 1) * 30)
            self.movement.doubleClick()
            sleep(0.05)
            self.movement.move(1130, 770)  # parçaladı
            self.movement.click_button()
            self.movement.click_button()
            sleep(1)
            self.movement.move(1190, 770)  # topla üzerine geldi
            sleep(0.05)
            self.movement.click_button()
            self.movement.click_button()
    def run_destroy(self):
        self.parent.title("Item Destroy")
        showinfo("Uyarı", "Oyuna Etki etmesi için\n Yönetici olarak çalıştırınız. !")
        self.parent.geometry("385x100")
        self.remove_all_frame()
        self.iDestroy.grid(row=1, column=0)
    def fark_ayarla(self):
        self.database.update_config(self.entry_3.get())
    def run_timer(self):
        self.parent.title("Boss Timer")
        self.parent.geometry("450x320")
        self.remove_all_frame()
        self.timer.grid(row=1, column=0)
        self.entry_3.delete(0, "end")
        self.entry_3.insert(0, self.database.return_config_time())

        self.client = pymongo.MongoClient(
            "mongodb+srv://bosstimer:timerboss@cluster0.zxtp6.mongodb.net/Cluster0?retryWrites=true&w=majority")
        tre = threading.Thread(target=self.pull_data)
        tre.start()
        root.after(250, run.loop)
    def return_mongodb(self):
        conn = self.client["Cluster0"]
        db = conn['boss']
        simple = db.find_one({"id": "001"})
        simple = str(simple)
        simple = simple.strip().split(",")
        return_data = [True, True]
        for i in simple:
            split_ = i.strip().split(":")
            if split_[0].split("'")[1] == "kul":
                return_data[1] = split_[1].split("'")[1]
            elif split_[0].split("'")[1] == "batik":
                return_data[0] = split_[1].split("'")[1]
            else:
                pass
        return return_data
    def pull_data(self):
        self.return_data = self.return_mongodb()
        root.after(1000, run.pull_data)
    def reset(self):
        hour = (datetime.datetime.today()).strftime("%H")
        minute = (datetime.datetime.today()).strftime("%M")
        date = hour + "/" + minute + "/" + "00"

        if self.islem[0]:
            self.update_database("kul", date)
        elif self.islem[1]:
            self.update_database("batik", date)
        else:
            showinfo("Hata Mesajı", "Kristal Seçilmedi.")
    def change(self):
        today = datetime.datetime.today().strftime("%d:%m:%y")
        time = self.entry_1.get() + "/" + self.entry_2.get()
        time = datetime.datetime.strptime(time + "/00_" + today, "%H/%M/%S_%d:%m:%y")
        value = time.strftime("%H/%M/%S")
        if self.islem[0]:
            self.update_database("kul", value)
        elif self.islem[1]:
            self.update_database("batik", value)
        else:
            showinfo("Hata Mesajı", "Kristal Seçilmedi.")
    def kul_click(self):
        self.islem[0] = True
        self.islem[1] = False
        self.canvas.itemconfig(self.bg, image=self.kul_bg)
    def batik_click(self):
        self.islem[0] = False
        self.islem[1] = True
        self.canvas.itemconfig(self.bg, image=self.batik_bg)
    def update_database(self, typew, value):
        conn = self.client["Cluster0"]
        db = conn['boss']
        if typew == "kul":
            db.update_one({}, {"$set": {'kul': value}})
        else:
            db.update_one({}, {"$set": {'batik': value}})
    def loop(self):
        today = datetime.datetime.today().strftime("%d:%m:%y")
        if self.login:
            self.return_data = self.return_mongodb()
            self.login = False

        self.batik_saat = (datetime.datetime.strptime(str(self.return_data[0]) + "_" + today,
                                                      "%H/%M/%S_%d:%m:%y") + datetime.timedelta(
            hours=3) + datetime.timedelta(
            seconds=int(self.database.return_config_time())) - datetime.datetime.today()).seconds
        data = str(self.return_data[0]).split("/")
        self.last_batik.set("{}:{}:?".format(data[0], data[1]))
        saat = self.batik_saat // 3600
        dakika = (self.batik_saat - saat * 3600) // 60
        saniye = (self.batik_saat - saat * 3600 - dakika * 60)
        if saat < 10:
            saat = "0" + str(saat)
        if dakika < 10:
            dakika = "0" + str(dakika)
        if saniye < 10:
            saniye = "0" + str(saniye)
        if int(saat) < 4:
            self.batik_time.set("{}:{}:{}".format(saat, dakika, saniye))
        self.kul_saat = (datetime.datetime.strptime(self.return_data[1] + "_" + today,
                                                    "%H/%M/%S_%d:%m:%y") + datetime.timedelta(
            hours=1) + datetime.timedelta(
            seconds=int(self.database.return_config_time())) - datetime.datetime.today()).seconds
        data = str(self.return_data[1]).split("/")

        self.last_kul.set("{}:{}:?".format(data[0], data[1]))

        saat = self.kul_saat // 3600
        dakika = (self.kul_saat - saat * 3600) // 60
        saniye = (self.kul_saat - saat * 3600 - dakika * 60)
        if saat < 10:
            saat = "0" + str(saat)
        if dakika < 10:
            dakika = "0" + str(dakika)
        if saniye < 10:
            saniye = "0" + str(saniye)
        if int(saat) < 2:
            self.kul_time.set("{}:{}:{}".format(saat, dakika, saniye))
        root.after(1000, run.loop)
    def run_calcExp(self):
        self.parent.title("Experiment Calculator")
        self.parent.geometry("385x80")
        self.remove_all_frame()
        self.expCalc.grid(row=1, column=0)
        self.exp = []
        self.experiment()
    def experiment(self):
        dat = """1 0 -
2 91 91
3 232 141
4 453 221
5 844 391
6 1.555 711
7 2.796 1.241
8 4.837 2.041
9 8.008 3.171
10 12.699 4.691
11 19.360 6.661
12 28.501 9.141
13 40.692 12.191
14 56.563 15.871
15 76.804 20.241
16 102.165 25.361
17 133.456 31.291
18 171.547 38.091
19 217.368 45.821
20 271.909 54.541
21 336.220 64.311
22 411.411 75.191
23 498.652 87.241
24 599.173 100.521
25 714.264 115.091
26 845.275 131.011
27 993.616 148.341
28 1.160.757 167.141
29 1.348.228 187.471
30 1.557.619 209.391
31 1.790.580 232.961
32 2.048.821 258.241
33 2.334.112 285.291
34 2.648.283 314.171
35 2.993.224 344.941
36 3.370.885 377.661
37 3.783.276 412.391
38 4.232.467 449.191
39 4.720.588 488.121
40 5.249.829 529.241
41 5.822.440 572.611
42 6.440.731 618.291
43 7.107.072 666.341
44 7.823.893 716.821
45 8.593.684 769.791
46 9.418.995 825.311
47 10.302.436 883.441
48 11.246.677 944.241
49 12.254.448 1.007.771
50 13.328.539 1.074.091
51 14.471.800 1.143.261
52 15.687.141 1.215.341
53 16.977.532 1.290.391
54 18.346.003 1.368.471
55 19.795.644 1.449.641
56 21.329.605 1.533.961
57 22.951.096 1.621.491
58 24.663.387 1.712.291
59 26.469.808 1.806.421
60 28.373.749 1.903.941
61 30.378.660 2.004.911
62 32.784.553 2.405.893
63 35.671.624 2.887.071
64 39.136.109 3.464.485
65 43.293.491 4.157.382
66 48.282.349 4.988.858
67 54.268.978 5.986.629
68 61.452.932 7.183.954
69 70.073.676 8.620.744
70 80.418.568 10.344.892
71 92.832.438 12.413.870
72 107.729.082 14.896.644
73 125.605.054 17.875.972
74 147.056.220 21.451.166
75 172.797.619 25.741.399
76 203.687.297 30.889.678
77 240.754.910 37.067.613
78 285.236.045 44.481.135
79 338.613.407 53.377.362
80 402.666.241 64.052.834
81 479.529.641 76.863.400
82 571.765.721 92.236.080
83 682.449.017 110.683.296
84 815.268.972 132.819.955
85 974.652.918 159.383.946
86 1.165.913.653 191.260.735
87 1.395.426.535 229.512.882
88 1.670.841.993 275.415.458
89 2.001.340.542 330.498.549
90 2.397.938.800 396.598.258
91 2.873.856.709 475.917.909
92 3.444.958.199 571.101.490
93 4.130.279.987 685.321.788
94 4.952.666.132 822.386.145
95 5.939.529.506 986.863.374
96 7.123.765.554 1.184.236.048
97 8.544.848.811 1.421.083.257
98 10.250.148.719 1.705.299.908
99 12.296.508.608 2.046.359.889
100 14.752.140.474 2.455.631.866
101 17.698.898.713 2.946.758.239
102 20.645.656.952 2.946.758.239
103 23.592.415.191 2.946.758.239
104 26.539.173.430 2.946.758.239
105 29.485.931.669 2.946.758.239
106 32.432.689.908 2.946.758.239
107 35.379.448.147 2.946.758.239
108 38.326.206.386 2.946.758.239
109 41.272.964.625 2.946.758.239
110 44.219.722.864 2.946.758.239
"""
        dat = dat.split(" ")
        for i in range(1, len(dat), 2):
            veri = dat[i].split(".")
            num = ""
            for z in veri:
                num += z

            self.exp.append(float(num))
    def calculate_exp(self):
        stt = ""
        exp = str(self.wExp.get()).strip().split(".")
        space = ""
        for i in exp:
            space += i
        exp = space.replace(",", ".")
        exp = float(exp)
        try:
            lvl = 2
            for i in self.exp:
                if self.exp[lvl - 1] < exp and exp < self.exp[lvl]:
                    stt += str(lvl)
                    num = (exp - self.exp[lvl - 1]) * 100 / (self.exp[lvl] - self.exp[lvl - 1])
                    stt += "  Seviye  "
                    stt += "%" + str(round(num, 2))
                    self.calc_exp_string.set(str(stt))
                lvl += 1
        except:
            pass
    def run_passworDirectory(self):
        self.parent.title("Password Directory")
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
        self.id.insert(0, "Kullanıcı Adı")
        self.passwd.delete(0, END)
        self.passwd.insert(0, "Şifre")
    def delete_contacs(self):
        try:
            pass
            # curItem = self.tree.focus()
            # self.database.delete(self.tree.item(curItem)["values"][0])
            # self.tree.delete(curItem)
        except:
            showinfo("HATA ! ", "Silinecek veri seçilmedi.")
        self.update_contacs()
    def add_data(self):
        self.database.add([self.id.get(), self.passwd.get()])
        self.update_contacs()
    def clear_directory_id(self, _):
        self.click = [True, False]
        if str(self.passwd.get()) == "":
            self.passwd.insert(0, "Şifre")
        if str(self.id.get()) == "Kullanıcı Adı":
            self.id.delete(0, END)
    def clear_directory_passwd(self, _):
        self.click = [False, True]
        if str(self.id.get()) == "":
            self.id.insert(0, "Kullanıcı Adı")
        if str(self.passwd.get()) == "Şifre":
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

        if ek_name == ' Perde Olasılık Ekleri':
            name = "perde_olasılık.db"
        elif ek_name == ' Perde tecrübe-Nesne Ekleri':
            name = "perde_tecrube_nesne.db"
        elif ek_name == ' Silah Ra-Olasılık Ekleri':
            name = "silah_ra_ols.db"
        elif ek_name == ' Silah Olasılık Ekleri':
            name = "silah_olasılık.db"
        elif ek_name == ' Silah Ra-Atak Ekleri':
            name = "silah_ra_atak.db"
        elif ek_name == ' Silah Ağırlık Ekleri':
            name = "silah_agirlik.db"
        else:
            name = "pet_ekleri.db"
        baglan = sqlite3.connect("file/fixes/" + name)
        veri = baglan.cursor()
        values = veri.execute("select * from attachments_list").fetchall()
        array = []
        for i in values:
            array.append(i[0])
        return array
    def add(self, variable):
        if str(variable[0]) == "Kullanıcı Adı" or str(variable[1]) == "Şifre":
            showinfo("Hata Mesajı", "Kullanıcı Adı veya Şifre Boş bırakılamaz.")
        else:
            try:
                baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_passwd"])
                veri = baglan.cursor()
                veri.execute("INSERT INTO password (id, sifre) VALUES (?,?)", (variable[0], variable[1]))
                baglan.commit()
                baglan.close()
            except sqlite3.IntegrityError:
                showinfo("HATA ! ", "Kullanıcı Adı Zaten Eklenmiş.")

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
        self.popup_menu.add_command(label="Kopyala",
                                    command=self.copy)
        self.bind("<Button-3>", self.popup)
        self.popup_menu.add_command(label="Delete",
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
        MsgBox = messagebox.askquestion('Onaylayınız', 'Bak silcem emin misin ?',
                                        icon='warning')
        if MsgBox == 'yes':
            for i in self.curselection()[::-1]:
                self.database.delete(i)

        else:
            messagebox.showinfo('İptal ', 'Az daha siliyordum :)')

class movemont:
    def click_button():
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

    def doubleClick():
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)

    def move(X, Y):
        ctypes.windll.user32.SetCursorPos(X, Y)

class search:
    def screenshoot(self):
        Screenshot = pyautogui.screenshot()
        Screenshot.save("image/ek.png")
    def crop_image(self):
        img = Image.open("image/ek.PNG")
        img_right_area = (1585, 987, 1850, 1005)
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
        if "‘" in text:
            text = text.split("‘")[1]
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
