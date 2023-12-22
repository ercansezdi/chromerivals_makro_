#!/usr/bin/env python
 # -*- coding: utf-8 -*-
"""
@auther : ercan sezdi
@date : 15.12.2023
@description : chromerivals makro
@github : ercansezdi/chromerivals_makro_
@apikey Gork3m-Player-Z5X96djv
@apiurl https://api.chromerivals.net/docs/#/


"""
import os 

def compare_code():
    path = "C:\\Users\\trforever\\Documents\\GitHub\\chromerivals_makro_"
    uic_path = "pyuic5.exe -o {}test.py {}untitled.ui".format(path+"\\icons\\",path+"\\icons\\")
    qrc_path = "pyrcc5.exe -o {}new_qrc_rc.py {}new_qrc.qrc".format(path+"\\icons\\",path+"\\icons\\")

    os.system(uic_path)
    os.system(qrc_path)
    os.system("move {}test.py {}main_ui.py".format(path+"\\icons\\",path+"\\"))
    os.system("move {}new_qrc_rc.py {}new_qrc_rc.py".format(path+"\\icons\\",path+"\\"))



compare_code()

import datetime
from time import sleep,strftime
import threading
import sqlite3
import pyperclip
from PIL import Image, ImageTk, ImageFont, ImageDraw
import keyboard
import mouse
import pyautogui
import cv2
import pytesseract
from functools import partial
import win32api
import win32con 
import ctypes
from PIL import Image
import datetime
import json
from collections import namedtuple

from main_ui import Ui_MainWindow
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  Qt, QUrl,QSize,QObject, pyqtSignal, pyqtSlot, QTimer,QRect,QMetaEnum
from PyQt5.QtGui import QKeyEvent,QCloseEvent,QPixmap,QIcon,QPalette, QImage
import sqlite3
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from threading import Thread
from random import randint
from time import strftime
import requests

class defaults():
    def __init__(self):
        self.api_key = "Gork3m-Player-Z5X96djv"
        self.istek_url = "https://api.chromerivals.net/"
        self.save_path = "C:\\Users\\trforever\\Documents\\GitHub\\chromerivals_makro_\\file\\"
        self.save_db_path = "C:\\Users\\trforever\\Documents\\GitHub\\chromerivals_makro_\\db\\"
        self.bosses_ids = {"764182069386432500":"Hornian Queen","761944773358538800":"Mountain Sage","763119997668053000":"Messenger","764588735659528200":"Pathos","761944773417259000":"Prog. Military Base","764588486207492100":"Energy Core","763156516252438500":"Shirne","764588735747608600":"Nipar Bridge","764182069545816000":"Quetzalcoatl","764588735781163000":"Gryphon","764199142942593000":"Rock Emperor","764111152580939800":"Ordin","764273742804176900":"Azimuth","763156515245805600":"Egma Schill","764182736305934300":"Skadi","762916803910324200":"Gigantic God","761950599683002400":"Bishop Black","762284072524337200":"Bishop Green","761950599590727700":"Bishop Blue","761950599724945400":"Bishop Red","764182736435957800":"Sekhmete","764280926703210500":"Black Widow","764182736767307800":"Echelon","764182736704393200":"Guardian of Vatallus","762172289146966000":"RM-230","762284072566280200":"Eater","762284072604028900":"Death Worm","762284072750829600":"NGC Calcani","762284072692109300":"Overlord-01","762284072889241600":"Saleos","762284072956350500":"Tetzlica","762284073019265000":"Overhead Completion","762172820695306200":"Lord Kreacia","762284072637583400":"NGC Mothership"}
        self.weapon_re_attachment = ["Legend", "Bio", "Meteo", "Ultra", "Deus", "Trekki", "Tachyon", "Terra", "Solace", "Attack", "Silence", "Faith", "Faithful", "Elite", "Chimera", "Epic", "Ether", "Amazing", "Criminal", "Shooting-Star", "Judgement", "Dispel", "Glacial", "Nova", "Universe", "Double", "Hell", "Flare", "Bite", "Hera"]
        self.armor_eva_attachment  = ["Ose", "Critter", "Macha", "Maurader", "Metatron", "Methadrone", "Miasma", "Origin", "Orobas", "Caina", "Tyranny"]
        self.armor_exp_attachment = ["Azatoth", "Aeon", "Cross", "Oberon", "Ovid", "Creed", "Avnas"]
        self.armor_drop_attachment = ["Forseti", "Hypnos", "Laomedon", "Oracle"]
        self.pet_attachment = ["Azael", "Baphomet", "Beretta", "Berith", "Brigandine", "Bright", "Brilliance", "Fantasy", "Hegemony", "Helios", "Hydra", "Hysteria", "Kimaris", "Knuckle", "Krishna", "Malebolge", "Malevolent", "Morgoth", "Morrigan", "Nexus", "Nightmare", "Nigor", "Nymph", "Orichalcum", "Paladin", "Plate", "Plexus", "Prime", "Principal", "Pristine", "Prodigy", "Ritona", "Robur", "Rosmerta", "Rudianos", "Sacrilege", "Sanctity", "Sanctum", "Schiavona", "Trinity"]
        self.wepaon_prob_attachment = ["Agareth", "Asmodi", "Kobal", "Navas", "Warrior", "Aloken", "Hound", "Luciper", "Proson", "Tobit"]
        self.weapon_attack_attachment = ["Max", "Squire", "Rukieper", "Foras", "Major", "Mareves"]
        self.armor_pierce_attachment = ["Crocell", "Cthulhu", "Testament", "Eibon"]
        self.wepoan_pierce_attachment = ["Bandit", "Adversary", "Bane", "Challenger"]
        self.total_p_s = ["zirh_p_basma", "zirh_p_silme", "zirh_s_basma", "zirh_s_silme", "pet_p_basma", "pet_p_silme", "pet_s_basma", "pet_s_silme", "silah_p_basma", "silah_p_silme", "silah_s_basma", "silah_s_silme","total"]
        self.attachment_names = ["weapon_re_attachment", "armor_eva_attachment", "armor_exp_attachment", "armor_drop_attachment", "pet_attachment", "wepaon_prob_attachment", "weapon_attack_attachment", "armor_pierce_attachment", "wepoan_pierce_attachment","total_p_s"]

        
        self.total_drop_item_count = 6611
class create_sql():
    def __init__(self,type_):
        self.default = defaults()
        # self.start_for_bosses()
        # self.start_for_attachments()
        self.start_for_id_pass()
    def start_for_id_pass(self):
        self.firstTime = True
        if not os.path.exists(self.default.save_db_path):
            os.mkdir(self.default.save_db_path)
        self.db = sqlite3.connect( self.default.save_db_path + "airrivals_database.db")
        self.cursor = self.db.cursor()
        self.create_table_for_id_pass()
    def start_for_attachments(self):
        self.firstTime = True
        if not os.path.exists(self.default.save_db_path):
            os.mkdir(self.default.save_db_path)
        self.db = sqlite3.connect( self.default.save_db_path + "airrivals_database.db")
        self.cursor = self.db.cursor()
        self.create_table_for_attachments()
    def create_table_for_id_pass(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS id_pass (id TEXT, pass TEXT, information TEXT)""")
        self.db.commit()
    def create_table_for_attachments(self):
        for i in self.default.attachment_names:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS {} (name TEXT, count INT)""".format(str(i)))
        for i in self.default.weapon_re_attachment:
            self.cursor.execute("INSERT INTO weapon_re_attachment VALUES(?,?)",(i, 0))
        for i in self.default.armor_eva_attachment:
            self.cursor.execute("INSERT INTO armor_eva_attachment VALUES(?,?)",(i, 0))
        for i in self.default.armor_exp_attachment:
            self.cursor.execute("INSERT INTO armor_exp_attachment VALUES(?,?)",(i, 0))
        for i in self.default.armor_drop_attachment:
            self.cursor.execute("INSERT INTO armor_drop_attachment VALUES(?,?)",(i, 0))
        for i in self.default.pet_attachment:
            self.cursor.execute("INSERT INTO pet_attachment VALUES(?,?)",(i, 0))
        for i in self.default.wepaon_prob_attachment:
            self.cursor.execute("INSERT INTO wepaon_prob_attachment VALUES(?,?)",(i, 0))
        for i in self.default.weapon_attack_attachment:
            self.cursor.execute("INSERT INTO weapon_attack_attachment VALUES(?,?)",(i, 0))
        for i in self.default.armor_pierce_attachment:
            self.cursor.execute("INSERT INTO armor_pierce_attachment VALUES(?,?)",(i, 0))
        for i in self.default.wepoan_pierce_attachment:
            self.cursor.execute("INSERT INTO wepoan_pierce_attachment VALUES(?,?)",(i, 0))
        for i in self.default.total_p_s:
            self.cursor.execute("INSERT INTO total_p_s VALUES(?,?)",(i, 0))
        self.db.commit()
    def start_for_bosses(self):
        self.firstTime = False
        if not os.path.exists(self.default.save_db_path):
            os.mkdir(self.default.save_db_path)
        self.db = sqlite3.connect( self.default.save_db_path + "airrivals_database.db")
        self.cursor = self.db.cursor()
        if (os.path.exists(self.default.save_db_path + "airrivals_database.db")):
            self.firstTime = True
            self.create_table_for_bosses()
            for i in self.default.bosses_ids:
                self.insert_boss_id(i,self.default.bosses_ids[i])
    def create_table_for_bosses(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS bosses_ids (id TEXT, name TEXT)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS bosses (id TEXT, name TEXT, level INT, hp INT, speed INT, range INT, recoveryValue INT, recoveryTime INT, experience INT, tier INT)""")
        self.cursor.execute
        self.db.commit()
    def create_special_table_for_bosses(self, table_name):
        table_name = "drop_" + str(table_name)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS '{}' (bos_id TEXT, boss_name TEXT, id TEXT, name TEXT, level INT, gear INT, iconId INT, minimumCount INT, maximumCount INT, dropProbability INT)""".format(str(table_name)))
        self.db.commit()
    def insert_boss(self, id, name, level, hp, speed, range, recoveryValue, recoveryTime, experience, tier):
        self.cursor.execute("INSERT INTO bosses VALUES(?,?,?,?,?,?,?,?,?,?)",(id, name, level, hp, speed, range, recoveryValue, recoveryTime, experience, tier))
        self.db.commit()
    def insert_boss_id(self, id, name):
        self.cursor.execute("INSERT INTO bosses_ids VALUES(?,?)",(id, name))
        self.db.commit()
    def insert_item_for_bosses(self, bos_id, boss_name, id, name, level, gear, iconId, minimumCount, maximumCount, dropProbability):
        nama = "drop_" + str(bos_id)
        self.cursor.execute("INSERT INTO {} VALUES(?,?,?,?,?,?,?,?,?,?)".format(nama),(bos_id, boss_name, id, name, level, gear, iconId, minimumCount, maximumCount, dropProbability))
        self.db.commit()
    def create_database(self):
        pass
        # if not (os.path.exists(self.default.save_db_path + "airrivals_database.db")):
        #     self.database = create_sql("bosses")
        #     if self.database.get_firstTime():
        #         for i in self.default.bosses_ids:
        #             self.database.create_special_table_for_bosses(i)
        #             self.get_boss_information(i)
        # if not (os.path.exists(self.default.save_db_path + "airrivals_database.db")):
        # self.database = create_sql("attachments")
    # def get_firstTime(self):
    #     return self.firstTime
class database():
    def __init__(self):
        self.default = defaults()
        self.db = sqlite3.connect( self.default.save_db_path + "airrivals_database.db")
        self.cursor = self.db.cursor()
    def get_bosses(self):
        self.cursor.execute("SELECT * FROM bosses_ids")
        return self.cursor.fetchall()
    def get_boss_information(self, boss_id):
        table_name = "drop_" + str(boss_id)
        self.cursor.execute("SELECT * FROM {}".format(table_name))
        return self.cursor.fetchall()
    def add_id_pass(self, id, pass_, information):
        self.cursor.execute("INSERT INTO id_pass VALUES(?,?,?)",(id, pass_, information))
        self.db.commit()
    def get_id_pass(self):
        self.cursor.execute("SELECT * FROM id_pass")
        return self.cursor.fetchall()
    def delete_id_pass(self, id):
        self.cursor.execute("DELETE FROM id_pass WHERE id = ?", (id,))
        self.db.commit()
    def update_id_pass(self, id, pass_, information):
        self.cursor.execute("UPDATE id_pass SET pass = ?, information = ? WHERE id = ?", (pass_, information, id))
        self.db.commit()
    def get_attachments(self, attachment_name):
        self.cursor.execute("SELECT * FROM {}".format(attachment_name))
        return self.cursor.fetchall()
    def delete_macro(self, id):
        self.cursor.execute("DELETE FROM macro WHERE id = ?", (id,))
        self.db.commit()
    def macro_events_keys(self, start,stop,save,play):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS macro_events_keys (start TEXT, stop TEXT, save TEXT, play TEXT)""")
        self.cursor.execute("INSERT INTO macro_events_keys VALUES(?,?,?,?)",(start, stop, save, play))
        self.db.commit()
    def update_macro_events_keys(self, start,stop,save,play):
        self.cursor.execute("UPDATE macro_events_keys SET start = ?, stop = ?, save = ?, play = ?", (start, stop, save, play))
        self.db.commit()
    def get_macro_events_keys(self):
        try:
            self.cursor.execute("SELECT * FROM macro_events_keys")
            return self.cursor.fetchall()
        except:
            return []
    def add_macro_event(self,id, event_mouse,event_keyboard, description= "", speed = 1):
        time = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS macro (id TEXT, event_mouse TEXT,event_keyboard TEXT, time TEXT, speed INT, description TEXT)""")
        self.cursor.execute("INSERT INTO macro VALUES(?,?,?,?,?,?)",(id, event_mouse,event_keyboard, time, description, speed))
        if len(self.cursor.execute("SELECT * FROM macro WHERE id = ?", (id,)).fetchall()) != 0:
            self.cursor.execute("UPDATE macro SET event_mouse = ?, event_keyboard = ?, time = ?, description = ?, speed = ? WHERE id = ?", (event_mouse, event_keyboard, time, description,speed, id,))
        self.db.commit()
    def update_speed_and_description(self, id, speed, description):
        self.cursor.execute("UPDATE macro SET speed = ?, description = ? WHERE id = ?", (speed, description, id,))
        self.db.commit()
    def number_of_macro(self):
        try:
            return len(self.cursor.execute("SELECT * FROM macro").fetchall())
        except:
            return 0
    def get_macro(self):
        try:
            self.cursor.execute("SELECT * FROM macro")
            return self.cursor.fetchall()
        except:
            return []
    def get_macro_using_description(self,description):
        try:
            self.cursor.execute("SELECT * FROM macro WHERE description = ?", (description,))
            return self.cursor.fetchall()
        except:
            return []
    def get_macro_using_id(self,id):
        try:
            self.cursor.execute("SELECT * FROM macro WHERE id = ?", (id,))
            return self.cursor.fetchall()
        except:
            return []
    def add_attachment_p_macro(self, p_macro, macro_name_basma, macro_name_silme):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS attachment_macro_p (macro TEXT, macro_name_basma TEXT, macro_name_silme TEXT)""")
        if ( macro_name_basma != ""):
            if len(self.cursor.execute("SELECT * FROM attachment_macro_p WHERE macro = ?", (p_macro,)).fetchall()) != 0:
                self.cursor.execute("UPDATE attachment_macro_p SET macro_name_basma = ? WHERE macro = ?", (macro_name_basma, p_macro,))
            else:
                self.cursor.execute("INSERT INTO attachment_macro_p VALUES(?,?,?)",(p_macro, macro_name_silme, macro_name_silme))
        if ( macro_name_silme != ""):
            if len(self.cursor.execute("SELECT * FROM attachment_macro_p WHERE macro = ?", (p_macro,)).fetchall()) != 0:
                self.cursor.execute("UPDATE attachment_macro_p SET macro_name_silme = ? WHERE macro = ?", (macro_name_silme, p_macro,))
            else:
                self.cursor.execute("INSERT INTO attachment_macro_p VALUES(?,?,?)",(p_macro, macro_name_basma, macro_name_silme))

        self.db.commit()
    def add_attachment_s_macro(self, s_macro, macro_name_basma, macro_name_silme):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS attachment_macro_s (macro TEXT, macro_name_basma TEXT, macro_name_silme TEXT)""")
        if ( macro_name_basma != ""):
            if len(self.cursor.execute("SELECT * FROM attachment_macro_s WHERE macro = ?", (s_macro,)).fetchall()) != 0:
                self.cursor.execute("UPDATE attachment_macro_s SET macro_name_basma = ? WHERE macro = ?", (macro_name_basma, s_macro,))
            else:
                self.cursor.execute("INSERT INTO attachment_macro_s VALUES(?,?,?)",(s_macro, macro_name_basma,macro_name_silme))
        if ( macro_name_silme != ""):
            if len(self.cursor.execute("SELECT * FROM attachment_macro_s WHERE macro = ?", (s_macro,)).fetchall()) != 0:
                self.cursor.execute("UPDATE attachment_macro_s SET macro_name_silme = ? WHERE macro = ?", (macro_name_silme, s_macro,))
            else:
                self.cursor.execute("INSERT INTO attachment_macro_s VALUES(?,?,?)",(s_macro,macro_name_basma, macro_name_silme))

        self.db.commit()
    def get_attachment_p_s_macro(self, p_s):
        if p_s:
            try:
                self.cursor.execute("SELECT * FROM attachment_macro_p")
                return self.cursor.fetchall()
            except:
                return []
        else:
            try:
                self.cursor.execute("SELECT * FROM attachment_macro_s")
                return self.cursor.fetchall()
            except:
                return []


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        #full screen
        # self.showMaximized()
        self.applicatin_version = "1.4.2"
        self.setWindowIcon(QIcon(":/new/chromerivals_logo.png"))
        self.setWindowTitle("Chromerivals Makro")
        self.default = defaults()
        self.database = database()
        self.variables()
        # self.create_database()
        self.headers = {'accept': '*/*',
                    'Cr-Api-Key': self.default.api_key,}
        

        self.ui.show_boss.clicked.connect(partial(self.ui.stackedWidget.setCurrentIndex, 1))
        self.ui.show_boss.clicked.connect(lambda: self.open_boss_page())
        self.ui.general_search.clicked.connect(lambda: self.open_search_page())
        self.ui.information.clicked.connect(lambda: self.open_information_page())
        self.ui.oyuncu_bilgi.setToolTip("Dakikada bir güncellenir.")
        self.ui.id_pass.clicked.connect(lambda: self.open_id_pass_page())
        self.ui.ekle_database.clicked.connect(lambda: self.add_id_pass())
        self.ui.search_athect.clicked.connect(lambda: self.open_search_attachment_page())
        self.ui.macro.clicked.connect(lambda: self.open_macro_page())
        ###########################################
        self.ui.p_ekle.clicked.connect(lambda: self.add_attachment("p_ekle"))
        self.ui.p_sil.clicked.connect(lambda: self.delete_attachment("p_sil"))
        self.ui.s_ekle.clicked.connect(lambda: self.add_attachment("s_ekle"))
        self.ui.s_sil.clicked.connect(lambda: self.delete_attachment("s_sil"))
        self.ui.p_ek_sayi.setValidator(QtGui.QIntValidator())
        self.ui.s_ek_sayi.setValidator(QtGui.QIntValidator())
        self.ui.p_izin.stateChanged.connect(lambda: self.state_changed("p_izin"))
        self.ui.s_izin.stateChanged.connect(lambda: self.state_changed("s_izin"))
        ####################
        self.ui.start_record_macro.clicked.connect(lambda: self.update_macro_keys("start"))
        self.ui.stop_record_macro.clicked.connect(lambda: self.update_macro_keys("stop"))
        self.ui.test_start_macro.clicked.connect(lambda: self.update_macro_keys("save"))
        self.ui.save_macro.clicked.connect(lambda: self.update_macro_keys("play"))
        self.ui.p_macro_ata.clicked.connect(lambda: self.set_p_macro())
        self.ui.p_silme_ata.clicked.connect(lambda: self.set_p_silme_macro())
        self.ui.s_macro_ata.clicked.connect(lambda: self.set_s_macro())
        self.ui.s_silme_ata.clicked.connect(lambda: self.set_s_silme_macro())
        self.ui.start_attachment.clicked.connect(lambda: self.start_attachment())
        self.ui.stop_macro.clicked.connect(lambda: self.stop_all_macro())


        self.ui.chart.hide()
        self.ui.label_6.hide()



        """
        self.get_kills(filter = None ) -- filter verilirse sadece o isimdeki killleri getirir
        """
        self.setup_for_app()
        self.get_news()
        self.ui.stackedWidget.setCurrentIndex(0)

        ###############
        # self.open_search_attachment_page()
        self.open_macro_page()

    def set_p_macro(self):
        macros_names = self.database.get_macro()
        if len(macros_names) != 0:
            #create widget 
            self.macro_widget = QWidget()
            self.macro_widget.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.macro_widget.setObjectName("macro_widget")
            self.macro_widget.resize(400, 200)
            self.macro_widget.setMinimumSize(QtCore.QSize(400, 200))
            self.macro_widget.setMaximumSize(QtCore.QSize(400, 200))
            self.macro_widget.setWindowTitle("P için makro ata")
            self.macro_widget.setWindowIcon(QIcon(":/new/chromerivals_logo.png"))
            self.macro_widget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
            self.macro_widget.setWindowModality(QtCore.Qt.ApplicationModal)

            self.macro_widget.show()
            #create layout
            self.macro_layout = QVBoxLayout()
            self.macro_layout.setObjectName("macro_layout")
            self.macro_widget.setLayout(self.macro_layout)
            #create combobox

            self.macro_combobox = QComboBox()
            self.macro_combobox.setObjectName("macro_combobox")
            self.macro_combobox.setStyleSheet("background-color: rgb(255, 255, 255); font: 700 12pt \"Segoe UI\";")
            self.macro_combobox.setMinimumSize(QtCore.QSize(380, 50))
            self.macro_combobox.setMaximumSize(QtCore.QSize(380, 50))
            self.macro_layout.addWidget(self.macro_combobox)

            for i in macros_names:
                self.macro_combobox.addItem(i[5])
            #create button
            self.macro_button = QPushButton()
            self.macro_button.setObjectName("macro_button")
            self.macro_button.setStyleSheet("background-color: rgb(255, 255, 255); font: 700 12pt \"Segoe UI\";")
            self.macro_button.setMinimumSize(QtCore.QSize(380, 50))
            self.macro_button.setMaximumSize(QtCore.QSize(380, 50))
            self.macro_button.setText("Ata")
            self.macro_button.clicked.connect(lambda: self.p_macro_button_clicked())
            self.macro_layout.addWidget(self.macro_button)
        else:
            QMessageBox.warning(self, "Warning", "No macro found")
    def set_p_silme_macro(self):
        macros_names = self.database.get_macro()
        if len(macros_names) != 0:
            #create widget 
            self.macro_widget = QWidget()
            self.macro_widget.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.macro_widget.setObjectName("macro_widget")
            self.macro_widget.resize(400, 200)
            self.macro_widget.setMinimumSize(QtCore.QSize(400, 200))
            self.macro_widget.setMaximumSize(QtCore.QSize(400, 200))
            self.macro_widget.setWindowTitle("P için makro ata")
            self.macro_widget.setWindowIcon(QIcon(":/new/chromerivals_logo.png"))
            self.macro_widget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
            self.macro_widget.setWindowModality(QtCore.Qt.ApplicationModal)

            self.macro_widget.show()
            #create layout
            self.macro_layout = QVBoxLayout()
            self.macro_layout.setObjectName("macro_layout")
            self.macro_widget.setLayout(self.macro_layout)
            #create combobox

            self.macro_combobox = QComboBox()
            self.macro_combobox.setObjectName("macro_combobox")
            self.macro_combobox.setStyleSheet("background-color: rgb(255, 255, 255); font: 700 12pt \"Segoe UI\";")
            self.macro_combobox.setMinimumSize(QtCore.QSize(380, 50))
            self.macro_combobox.setMaximumSize(QtCore.QSize(380, 50))
            self.macro_layout.addWidget(self.macro_combobox)

            for i in macros_names:
                self.macro_combobox.addItem(i[5])
            #create button
            self.macro_button = QPushButton()
            self.macro_button.setObjectName("macro_button")
            self.macro_button.setStyleSheet("background-color: rgb(255, 255, 255); font: 700 12pt \"Segoe UI\";")
            self.macro_button.setMinimumSize(QtCore.QSize(380, 50))
            self.macro_button.setMaximumSize(QtCore.QSize(380, 50))
            self.macro_button.setText("Ata")
            self.macro_button.clicked.connect(lambda: self.p_silme_macro_button_clicked())
            self.macro_layout.addWidget(self.macro_button)
        else:
            QMessageBox.warning(self, "Warning", "No macro found")
    def set_s_macro(self):
        #get macros 
        macros_names = self.database.get_macro()
        if len(macros_names) != 0:
            #create widget 
            self.macro_widget = QWidget()
            self.macro_widget.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.macro_widget.setObjectName("macro_widget")
            self.macro_widget.resize(400, 200)
            self.macro_widget.setMinimumSize(QtCore.QSize(400, 200))
            self.macro_widget.setMaximumSize(QtCore.QSize(400, 200))
            self.macro_widget.setWindowTitle("S için makro ata")
            self.macro_widget.setWindowIcon(QIcon(":/new/chromerivals_logo.png"))
            self.macro_widget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
            self.macro_widget.setWindowModality(QtCore.Qt.ApplicationModal)

            self.macro_widget.show()
            #create layout
            self.macro_layout = QVBoxLayout()
            self.macro_layout.setObjectName("macro_layout")
            self.macro_widget.setLayout(self.macro_layout)
            #create combobox

            self.macro_combobox = QComboBox()
            self.macro_combobox.setObjectName("macro_combobox")
            self.macro_combobox.setStyleSheet("background-color: rgb(255, 255, 255); font: 700 12pt \"Segoe UI\";")
            self.macro_combobox.setMinimumSize(QtCore.QSize(380, 50))
            self.macro_combobox.setMaximumSize(QtCore.QSize(380, 50))
            self.macro_layout.addWidget(self.macro_combobox)

            for i in macros_names:
                self.macro_combobox.addItem(i[5])
            #create button
            self.macro_button = QPushButton()
            self.macro_button.setObjectName("macro_button")
            self.macro_button.setStyleSheet("background-color: rgb(255, 255, 255); font: 700 12pt \"Segoe UI\";")
            self.macro_button.setMinimumSize(QtCore.QSize(380, 50))
            self.macro_button.setMaximumSize(QtCore.QSize(380, 50))
            self.macro_button.setText("Ata")
            self.macro_button.clicked.connect(lambda: self.s_macro_button_clicked())
            self.macro_layout.addWidget(self.macro_button)
        else:
            QMessageBox.warning(self, "Warning", "No macro found")
    def check_startable_attachment(self):
        result = (self.ui.p_izin.isChecked() and self.ui.p_macro_basma_adi.text() != "" and self.ui.p_macro_silme_adi.text() != "" and self.ui.p_ek_sayi != ""  and int(self.ui.p_ek_sayi.text()) > 0 and self.ui.aranan_on_ek.count() > 0)
        result = result or (self.ui.s_izin.isChecked() and self.ui.s_macro_basma_adi.text() != "" and self.ui.s_macro_silme_adi.text() != "" and self.ui.s_ek_sayi != "" and int(self.ui.s_ek_sayi.text()) > 0 and self.ui.aranan_son_ek.count() > 0)
        return result
    def start_attachment(self):
        if(self.check_startable_attachment()):
            QTimer.singleShot(1000, self.start_attachment_now)
    def set_s_silme_macro(self):
        #get macros 
        macros_names = self.database.get_macro()
        if len(macros_names) != 0:
            #create widget 
            self.macro_widget = QWidget()
            self.macro_widget.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.macro_widget.setObjectName("macro_widget")
            self.macro_widget.resize(400, 200)
            self.macro_widget.setMinimumSize(QtCore.QSize(400, 200))
            self.macro_widget.setMaximumSize(QtCore.QSize(400, 200))
            self.macro_widget.setWindowTitle("S için makro ata")
            self.macro_widget.setWindowIcon(QIcon(":/new/chromerivals_logo.png"))
            self.macro_widget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
            self.macro_widget.setWindowModality(QtCore.Qt.ApplicationModal)

            self.macro_widget.show()
            #create layout
            self.macro_layout = QVBoxLayout()
            self.macro_layout.setObjectName("macro_layout")
            self.macro_widget.setLayout(self.macro_layout)
            #create combobox

            self.macro_combobox = QComboBox()
            self.macro_combobox.setObjectName("macro_combobox")
            self.macro_combobox.setStyleSheet("background-color: rgb(255, 255, 255); font: 700 12pt \"Segoe UI\";")
            self.macro_combobox.setMinimumSize(QtCore.QSize(380, 50))
            self.macro_combobox.setMaximumSize(QtCore.QSize(380, 50))
            self.macro_layout.addWidget(self.macro_combobox)

            for i in macros_names:
                self.macro_combobox.addItem(i[5])
            #create button
            self.macro_button = QPushButton()
            self.macro_button.setObjectName("macro_button")
            self.macro_button.setStyleSheet("background-color: rgb(255, 255, 255); font: 700 12pt \"Segoe UI\";")
            self.macro_button.setMinimumSize(QtCore.QSize(380, 50))
            self.macro_button.setMaximumSize(QtCore.QSize(380, 50))
            self.macro_button.setText("Ata")
            self.macro_button.clicked.connect(lambda: self.s_silme_macro_button_clicked())
            self.macro_layout.addWidget(self.macro_button)
        else:
            QMessageBox.warning(self, "Warning", "No macro found")
    def s_silme_macro_button_clicked(self):
        choosed_macro = self.macro_combobox.currentText()

        self.macro_widget.close()
        self.macro_widget = None
        self.macro_combobox = None
        self.macro_button = None
        self.macro_layout = None
        self.macro_widget = None
        self.ui.s_macro_silme_adi.setText(choosed_macro)
        self.database.add_attachment_s_macro("s_macro", "", choosed_macro)
        macroo = self.database.get_macro_using_description(choosed_macro)
        self.attachment_s_silme_macro = self.text_to_move_event(macroo[0][2])
    def p_silme_macro_button_clicked(self):
        choosed_macro = self.macro_combobox.currentText()
        self.macro_widget.close()
        self.macro_widget = None
        self.macro_combobox = None
        self.macro_button = None
        self.macro_layout = None
        self.macro_widget = None
        self.ui.p_macro_silme_adi.setText(choosed_macro)
        self.database.add_attachment_p_macro("p_macro",  "",choosed_macro)
        macroo = self.database.get_macro_using_description(choosed_macro)
        self.attachment_p_silme_macro = self.text_to_move_event(macroo[0][2])
    def start_attachment_now(self):
        if(self.arama_izin[0]): # p için izin verildi
            pass
        if self.arama_izin[1]: # s için izin verildi
            pass

    def s_macro_button_clicked(self):
        choosed_macro = self.macro_combobox.currentText()
        self.macro_widget.close()
        self.macro_widget = None
        self.macro_combobox = None
        self.macro_button = None
        self.macro_layout = None
        self.macro_widget = None
        self.ui.s_macro_basma_adi.setText(choosed_macro)
        self.database.add_attachment_s_macro("s_macro",  choosed_macro, "")
        macroo = self.database.get_macro_using_description(choosed_macro)
        self.attachment_p_macro = self.text_to_move_event(macroo[0][2])

    def p_macro_button_clicked(self):
        choosed_macro = self.macro_combobox.currentText()
        self.macro_widget.close()
        self.macro_widget = None
        self.macro_combobox = None
        self.macro_button = None
        self.macro_layout = None
        self.macro_widget = None
        self.ui.p_macro_basma_adi.setText(choosed_macro)
        self.database.add_attachment_p_macro("p_macro", choosed_macro,"")
        macroo = self.database.get_macro_using_description(choosed_macro)
        self.attachment_s_macro = self.text_to_move_event(macroo[0][2])


    def update_macro_keys(self, name):
        self.kayit = True
        self.update_key = name
        # self.kayit_key = None
        if name == "start":
            self.ui.start_record_macro.setText("Start Record Macro ({})".format("Waiting..."))
        elif name == "stop":
            self.ui.stop_record_macro.setText("Stop Record Macro ({})".format("Waiting..."))
        elif name == "play":
            self.ui.test_start_macro.setText("TEST Start ({})".format("Waiting..."))
        elif name == "save":
            self.ui.save_macro.setText("Save Macro ({})".format("Waiting..."))

    def ek_sayi_changed(self, name):
        if name == "p_ek_sayi":
            self.ui.label_3.setText("Aranacak On Ekler)")
        elif name == "s_ek_sayi":
            self.ui.label_8.setText("Aranacak Son Ekler)")
    def state_changed(self, name):
        if name == "p_izin":
            if self.ui.p_izin.isChecked():
                self.arama_izin[0] = True
            else:
                self.arama_izin[0] = False
        elif name == "s_izin":
            if self.ui.s_izin.isChecked():
                self.arama_izin[1] = True
            else:
                self.arama_izin[1] = False
    def open_boss_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.boss_list.clear()
        self.ui.boss_list.setStyleSheet("background-color: rgb(255, 255, 255); font: 700 12pt \"Segoe UI\";")
        for i in self.default.bosses_ids:
            self.ui.boss_list.addItem(self.default.bosses_ids[i])
        self.ui.boss_list.currentIndexChanged.connect(self.boss_list_clicked)
        self.boss_list_clicked()
    def open_information_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def open_id_pass_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.create_id_pass_table()
    def open_search_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        for i in range(self.ui.search_table.rowCount()):
            self.ui.search_table.removeRow(0)

        for i in range(self.ui.search_table.columnCount()):
            self.ui.search_table.removeColumn(0)

        self.ui.search_table.clear()
        self.ui.general_search_button.clicked.connect(self.search_button_clicked)
        basliklar = ["items", "monsters", "fixes", "gears"]
        self.ui.ne_aranacak.clear()
        for i in basliklar:
            self.ui.ne_aranacak.addItem(i)
    def open_search_attachment_page(self):
        self.aranacak_on_ekler = []
        self.aranacak_son_ekler = []
        self.arama_izin = [False,False]
        macro_adlari = self.database.get_attachment_p_s_macro(True)
        if len(macro_adlari) != 0:
            self.attachment_p_macro = None
            self.attachment_p_silme_macro = None
            for i in macro_adlari:
                if i[0] == "p_macro":
                    # try:
                    if True:
                        self.ui.p_macro_basma_adi.setText(i[1])
                        macroo = self.database.get_macro_using_description(i[1])
                        self.attachment_p_macro = self.text_to_move_event(macroo[0][2])
                    # except:
                    #     self.ui.p_macro_basma_adi.setText("Not found")
                    try:
                        self.ui.p_macro_silme_adi.setText(i[2])
                        macroo = self.database.get_macro_using_description(i[2])
                        self.attachment_p_silme_macro = self.text_to_move_event(macroo[0][2])
                    except:
                        self.ui.p_macro_silme_adi.setText("Not found")
                else:
                    self.ui.p_macro_basma_adi.setText("Not found")
                    self.ui.p_macro_silme_adi.setText("Not found")
                # elif i[0] == "s_macro":
                #     try:
                #         macroo = self.database.get_macro_using_description(i[1])
                #         self.attachment_s_macro = self.text_to_move_event(macroo[0])
                #         self.ui.s_macro_basma_adi.setText(i[1])
                #     except:
                #         self.ui.s_macro_basma_adi.setText("Not found")
        else:
            self.ui.p_macro_basma_adi.setText("Not found")
            self.ui.p_macro_silme_adi.setText("Not found")
        
        macro_adlari = self.database.get_attachment_p_s_macro(False)
        if len(macro_adlari) != 0:
            self.attachment_s_macro = None
            self.attachment_s_silme_macro = None
            for i in macro_adlari:
                if i[0] == "s_macro":
                    try:
                        self.ui.s_macro_basma_adi.setText(i[1])
                        macroo = self.database.get_macro_using_description(i[1])
                        self.attachment_s_macro = self.text_to_move_event(macroo[0][2])
                    except:
                        self.ui.s_macro_basma_adi.setText("Not found")
                    try:
                        self.ui.s_macro_silme_adi.setText(i[2])
                        macroo = self.database.get_macro_using_description(i[2])
                        self.attachment_s_silme_macro = self.text_to_move_event(macroo[0][2])
                    except:
                        self.ui.s_macro_silme_adi.setText("Not found")
                else:
                    self.ui.s_macro_basma_adi.setText("Not found")
                    self.ui.s_macro_silme_adi.setText("Not found")
        self.ui.stackedWidget.setCurrentIndex(5)
        ek_isimler = self.default.attachment_names
        self.ui.aranan_widget.clear()
        for i in ek_isimler:
            if i != "total_p_s":
                self.ui.aranan_widget.addItem(i)
        self.ui.aranan_widget.currentIndexChanged.connect(self.aranan_widget_changed)
    def open_macro_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.create_macro_list()
    def key_to_name(self, key):
        key = int(key)
        try:
            key_str =  chr(key)
        except:
            key_str = ""
            if key == Qt.Key_F1:
                key_str = "F1"
            elif key == Qt.Key_F2:
                key_str = "F2"
            elif key == Qt.Key_F3:
                key_str = "F3"
            elif key == Qt.Key_F4:
                key_str = "F4"
            elif key == Qt.Key_F5:
                key_str = "F5"
            elif key == Qt.Key_F6:
                key_str = "F6"
            elif key == Qt.Key_F7:
                key_str = "F7"
            elif key == Qt.Key_F8:
                key_str = "F8"
            elif key == Qt.Key_F9:
                key_str = "F9"
            elif key == Qt.Key_F10:
                key_str = "F10"
            elif key == Qt.Key_F11:
                key_str = "F11"
            elif key == Qt.Key_F12:
                key_str = "F12"
            elif key == Qt.Key_Escape:
                key_str = "Escape"
            elif key == Qt.Key_Tab:
                key_str = "Tab"
            elif key == Qt.Key_Backspace:
                key_str = "Backspace"
            elif key == Qt.Key_Return:
                key_str = "Return"
            elif key == Qt.Key_Enter:
                key_str = "Enter"
            elif key == Qt.Key_Insert:
                key_str = "Insert"
            elif key == Qt.Key_Delete:
                key_str = "Delete"
            elif key == Qt.Key_Pause:
                key_str = "Pause"
            elif key == Qt.Key_Print:
                key_str = "Print"
            elif key == Qt.Key_SysReq:
                key_str = "SysReq"
            elif key == Qt.Key_Clear:
                key_str = "Clear"
            elif key == Qt.Key_Home:
                key_str = "Home"
            elif key == Qt.Key_End:
                key_str = "End"
            elif key == Qt.Key_Left:
                key_str = "Left"
            elif key == Qt.Key_Up:
                key_str = "Up"
            elif key == Qt.Key_Right:
                key_str = "Right"
            elif key == Qt.Key_Down:
                key_str = "Down"
            elif key == Qt.Key_Shift:
                key_str = "Shift"
            elif key == Qt.Key_Control:
                key_str = "Control"
            elif key == Qt.Key_Meta:
                key_str = "Meta"
            elif key == Qt.Key_Alt:
                key_str = "Alt"
            elif key == Qt.Key_CapsLock:
                key_str = "CapsLock"
            elif key == Qt.Key_NumLock:
                key_str = "NumLock"
            elif key == Qt.Key_ScrollLock:
                key_str = "ScrollLock"
            elif key == Qt.Key_PageUp:
                key_str = "PageUp"
            elif key == Qt.Key_PageDown:
                key_str = "PageDown"
            elif key == Qt.Key_Space:
                key_str = "Space"
            elif key == Qt.Key_Exclam:
                key_str = "Exclam"
            else:
                key_str = "Unknown"

        return key_str
        
    def create_macro_list(self):
        result = self.database.get_macro_events_keys()
        if len(result) == 0:
            self.database.macro_events_keys(16777264,16777266,16777267,16777268)
        else:
            keys = self.database.get_macro_events_keys()[0]
            self.macro_keys[0] = int(keys[0])
            self.macro_keys[1] = int(keys[1])
            self.macro_keys[2] = int(keys[3])
            self.macro_keys[3] = int(keys[2])

            self.ui.start_record_macro.setText("Start Record Macro ({})".format(self.key_to_name(self.macro_keys[0])))
            self.ui.stop_record_macro.setText("Stop Record Macro ({})".format(self.key_to_name(self.macro_keys[1])))
            self.ui.test_start_macro.setText("Test Start ({})".format(self.key_to_name(self.macro_keys[2])))
            self.ui.save_macro.setText("Save Macro ({})".format(self.key_to_name(self.macro_keys[3])))

        macrolar = self.database.get_macro()
        self.ui.macro_list.clear()
        self.ui.macro_list.setColumnCount(3)
        self.ui.macro_list.setHorizontalHeaderLabels(["id", "speed", "description"])
        self.ui.macro_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.macro_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.macro_list.setRowCount(len(macrolar))
        self.ui.macro_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.update_macro.clicked.connect(lambda: self.update_macro())
        self.ui.delete_macro.clicked.connect(lambda: self.delete_macro())
        self.ui.try_macro.clicked.connect(lambda: self.try_macro())
        for i in macrolar:
            id = i[0]
            speed = i[4]
            description = i[5]
            item1 = QTableWidgetItem(str(id))
            item1.setTextAlignment(Qt.AlignCenter)
            self.ui.macro_list.setItem(macrolar.index(i), 0, item1)
            item2 = QTableWidgetItem(str(speed))
            item2.setTextAlignment(Qt.AlignCenter)
            self.ui.macro_list.setItem(macrolar.index(i), 1, item2)
            item3 = QTableWidgetItem(str(description))
            item3.setTextAlignment(Qt.AlignCenter)
            self.ui.macro_list.setItem(macrolar.index(i), 2, item3)

    def try_macro(self):
        try:
            id = self.ui.macro_list.item(self.ui.macro_list.currentRow(), 0).text()
            macro = self.database.get_macro_using_id(id)
            if len(macro) != 0:
                mouse_event = macro[0][2]
                mouse_event = self.text_to_move_event(mouse_event)
                speed = macro[0][4]
                self.mouse_events = mouse_event
                self.go_on_macro(speed)
        except:
            pass
    def update_macro(self):
        try:
            id = self.ui.macro_list.item(self.ui.macro_list.currentRow(), 0).text()
            speed = self.ui.macro_list.item(self.ui.macro_list.currentRow(), 1).text()
            description = self.ui.macro_list.item(self.ui.macro_list.currentRow(), 2).text()
            new_speed, ok = QInputDialog.getText(self, "Update speed", "Speed")
            if ok:
                speed = new_speed
                new_description, ok = QInputDialog.getText(self, "Update description", "Description")
                if ok:
                    description = new_description
                    self.database.update_speed_and_description(id, speed,description)
                    self.create_macro_list()
                else:
                    QMessageBox.warning(self, "Warning", "Please fill all the blanks")
            else:
                QMessageBox.warning(self, "Warning", "Please fill all the blanks")
        except:
            QMessageBox.warning(self, "Warning", "No macro selected")
    def delete_macro(self):
        try:
            id = self.ui.macro_list.item(self.ui.macro_list.currentRow(), 0).text()
            self.database.delete_macro(id)
            self.create_macro_list()
        except:
            QMessageBox.warning(self, "Warning", "No macro selected")
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == 16777249:
            self.stop_all_macro()
        if(not self.kayit):
            if event.key() == Qt.Key_Escape:
                self.close()
            elif event.key() == self.macro_keys[0]:
                self.thread = threading.Thread(target = lambda :self.record_mac())
                self.thread.start()
            elif event.key() == self.macro_keys[2]:
                self.thread = threading.Thread(target = lambda :self.open_macro())
                self.thread.start()
            elif event.key() == self.macro_keys[3]:
                self.save_macro_db()
        else:
            self.kayit = False
            self.kayit_key = event.key()
            str_hali = self.key_to_name(event.key())
            if self.update_key == "start":
                self.macro_keys[0] = event.key()
                self.ui.start_record_macro.setText("Start Record Macro ({})".format(str_hali))
            elif self.update_key == "stop":
                self.macro_keys[1] = event.key()
                self.ui.stop_record_macro.setText("Stop Record Macro ({})".format(str_hali))
            elif self.update_key == "save":
                self.macro_keys[2] = event.key()
                self.ui.test_start_macro.setText("Test Start ({})".format(str_hali))
            elif self.update_key == "play":
                self.macro_keys[3] = event.key()
                self.ui.save_macro.setText("Save Macro ({})".format(str_hali))
            self.database.update_macro_events_keys(self.macro_keys[0],self.macro_keys[1],self.macro_keys[2],self.macro_keys[3])
            
    def text_to_move_event(self, text):
        try:
            xoxx = []
            MoveEvent = namedtuple('MoveEvent', ['x', 'y', 'time'])
            ButtonEvent = namedtuple('ButtonEvent', ['event_type', 'button', 'time'])
            text = str(text)
            for item in text.split('),'):
                try:
                    if "[" in item:
                        item = item.replace("[", "")
                    if ")]" in item:
                        item = item.replace("]", "")
                    if "MoveEvent(" in item:
                        item = item.replace("MoveEvent(", "")
                    if "(" in item:
                        item = item.replace("(", "")
                    if ")" in item:
                        item = item.replace(")", "")
                    item = item.split(",")
                    x = int(item[0].split("=")[1])
                    y = int(item[1].split("=")[1])
                    time = float(item[2].split("=")[1])
                    move_event = MoveEvent(x=x, y=y, time=time)
                except:
                    if "[" in item:
                        item = item.replace("[", "")
                    if ")]" in item:
                        item = item.replace("]", "")
                    if "ButtonEventevent_type(" in item:
                        item = item.replace("ButtonEventevent_type(", "")
                    if "(" in item:
                        item = item.replace("(", "")
                    if ")" in item:
                        item = item.replace(")", "")
                    event = item[0].split("=")[1]
                    event = event.replace("'", "")
                    buttonc = item[1].split("=")[1]
                    buttonc = buttonc.replace("'", "")
                    time = item[2].split("=")[1]
                    time = float(time)
                    move_event = ButtonEvent(event_type=event, button=buttonc, time=time)
                xoxx.append(move_event)
            return xoxx
        except:
            return []
    def record_mac(self): #f1
        mouse_events = []
        mouse.hook(mouse_events.append)
        keyboard.start_recording()
        keyboard.wait(self.key_to_name(self.macro_keys[1]))
        mouse.unhook(mouse_events.append)
        self.keyboard_events = keyboard.stop_recording()
        self.mouse_events = mouse_events
    def open_macro(self): #f3
        m_thread = threading.Thread(target = lambda :mouse.play(self.mouse_events))
        m_thread.start()
        m_thread.join()
    def save_macro_db(self): #f4
        if len(self.mouse_events) != 0 and len(self.keyboard_events) != 0:
            description, ok = QInputDialog.getText(self, "Description", "Description")
            if ok:
                self.database.add_macro_event("macro_" + str(self.database.number_of_macro()), str(self.keyboard_events), str(self.mouse_events), description)
                self.mouse_events = []
                self.keyboard_events = []
                self.create_macro_list()
            else:
                QMessageBox.warning(self, "Warning", "Please fill all the blanks")
    def stop_all_macro(self): #space
        self.stop = True
    def go_on_macro(self,speed = 1):
        self.last_time = 0
        self.stop = False
        self.sira = 0
        QTimer.singleShot(1000 , lambda: self.trigger_go_on_macro())
    def start_macro(self,macro_name, macro_speed = 1):
        self.mouse_events = macro_name
        self.last_time = 0
        self.stop = False
        self.sira = 0
        QTimer.singleShot(10 , lambda: self.trigger_go_on_macro())
    def trigger_go_on_macro(self):
        try:
            event = self.mouse_events[self.sira]
            if "ButtonEvent" in str(event):
                if event.event_type == "up":
                        mouse.release(event.button)
                else:
                    mouse.press(event.button)
            elif "MoveEvent" in str(event):
                mouse.move(event.x, event.y)
            print(self.last_time, self.stop)
            if not self.stop:
                self.sira += 1
                time = event.time - self.last_time
                time = time / 1.0
                if self.last_time != 0:
                    try:
                        sleep(time)
                    except:
                        pass
                QTimer.singleShot(1 , lambda: self.trigger_go_on_macro())
            else:
                self.sira = 0
                self.stop = False

            self.last_time = event.time
        except:
            pass

    def mouse_record(self):#f1
        self.ui.record.setEnabled(False)
        self.ui.record.setText("Kayıt Ediliyor...")
        self.ui.record.setStyleSheet("background-color: rgb(255, 0, 0);")
    def add_attachment(self, attachment_name):
        try:
            ek_adi = self.ui.aranan_listbox.currentItem().text()
        except:
            return 
        if attachment_name == "p_ekle":
            try:
                if not ek_adi in self.aranacak_on_ekler:
                    self.aranacak_on_ekler.append(ek_adi)
                    self.ui.aranan_on_ek.addItem(ek_adi)
            except:
                pass
        elif attachment_name == "s_ekle":
            if not ek_adi in self.aranacak_son_ekler:
                try:
                    self.aranacak_son_ekler.append(ek_adi)
                    self.ui.aranan_son_ek.addItem(ek_adi)
                except:
                    pass
    def delete_attachment(self, attachment_name):
        if attachment_name == "p_sil":
            try:
                ek_adi = self.ui.aranan_on_ek.currentItem().text()
                self.aranacak_on_ekler.remove(ek_adi)
                self.ui.aranan_on_ek.clear()
                for i in self.aranacak_on_ekler:
                    self.ui.aranan_on_ek.addItem(i)
            except:
                pass
        elif attachment_name == "s_sil":
            try:
                ek_adi = self.ui.aranan_son_ek.currentItem().text()
                self.aranacak_son_ekler.remove(ek_adi)
                self.ui.aranan_son_ek.clear()
                for i in self.aranacak_son_ekler:
                    self.ui.aranan_son_ek.addItem(i)
            except:
                pass
    def aranan_widget_changed(self):
        self.ui.aranan_listbox.clear()
        name = self.ui.aranan_widget.currentText()
        if name != "":
            data = self.database.get_attachments(name)
            for i in data:
                self.ui.aranan_listbox.addItem(str(i[0]))
    def create_id_pass_table(self):
        self.ui.id_pass_table.clear()
        self.ui.id_pass_table.setColumnCount(3)
        self.ui.id_pass_table.setHorizontalHeaderLabels(["id", "pass", "information"])
        self.ui.id_pass_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.id_pass_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.id_pass_table.setRowCount(len(self.database.get_id_pass()))
        #add right click menu
        self.ui.id_pass_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.id_pass_table.customContextMenuRequested.connect(self.right_click_menu)
        self.ui.id_pass_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        max_word = 0
        for i in range(len(self.database.get_id_pass())):
            id = self.database.get_id_pass()[i][0]
            pass_ = self.database.get_id_pass()[i][1]
            information = self.database.get_id_pass()[i][2]
            if len(id) > max_word:
                max_word = len(id)
            if len(pass_) > max_word:
                max_word = len(pass_)
            try:
                if len(information) > max_word:
                    max_word = len(information)
            except:
                pass
            item1 = QTableWidgetItem(str(id))
            item1.setTextAlignment(Qt.AlignCenter)
            self.ui.id_pass_table.setItem(i, 0, item1)
            item2 = QTableWidgetItem(str(pass_))
            item2.setTextAlignment(Qt.AlignCenter)
            self.ui.id_pass_table.setItem(i, 1, item2)
            item3 = QTableWidgetItem(str(information))
            item3.setTextAlignment(Qt.AlignCenter)
            self.ui.id_pass_table.setItem(i, 2, item3)
    def add_id_pass(self):
        id = self.ui.id_line.text()
        pass_ = self.ui.pass_line.text()
        information = self.ui.information_line.text()
        if id == "" or pass_ == "" or information == "":
            QMessageBox.warning(self, "Warning", "Please fill all the blanks")
        else:
            self.database.add_id_pass(id, pass_, information)
            self.create_id_pass_table()
    def right_click_menu(self, position):
        #copy id, copy pass, delete, edit information
        menu = QMenu()
        copy_id = menu.addAction("Copy id")
        copy_pass = menu.addAction("Copy pass")
        delete = menu.addAction("Delete")
        update = menu.addAction("Update information")

        if self.ui.id_pass_table.itemAt(position) is None:
            pass
        else:
            action = menu.exec_(self.ui.id_pass_table.mapToGlobal(position))
            if action == copy_id:
                id = self.ui.id_pass_table.item(self.ui.id_pass_table.currentRow(), 0).text()
                pyperclip.copy(id)
            elif action == copy_pass:
                pass_ = self.ui.id_pass_table.item(self.ui.id_pass_table.currentRow(), 1).text()
                pyperclip.copy(pass_)
            elif action == update:
                information, ok = QInputDialog.getText(self, "Update information", "Information")
                if ok:
                    id = self.ui.id_pass_table.item(self.ui.id_pass_table.currentRow(), 0).text()
                    pass_ = self.ui.id_pass_table.item(self.ui.id_pass_table.currentRow(), 1).text()
                    self.database.update_id_pass(id, pass_, information)
                    self.create_id_pass_table()
 
            elif action == delete:
                id = self.ui.id_pass_table.item(self.ui.id_pass_table.currentRow(), 0).text()
                self.database.delete_id_pass(id)
                self.create_id_pass_table()
    def search_button_clicked(self):
        data = self.search_general(self.ui.search_line.text())
        self.ui.search_table.clear()

        aranacak = self.ui.ne_aranacak.currentText()
        if aranacak == "items":
            baslik = ["item_id", "item_name", "level", "gear"]
            self.ui.search_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        elif aranacak == "monsters":
            baslik = ["id", "name", "level"]
            self.ui.search_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        elif aranacak == "fixes":
            baslik = ["name", "probability", "functions"]
            self.ui.search_table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        elif aranacak == "gears":
            baslik = ["id", "name", "level", "gear", "nation"]
            self.ui.search_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            baslik = ["not found", "not found", "not found"]
        self.ui.search_table.setHorizontalHeaderLabels(baslik)
        self.ui.search_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.search_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.search_table.setColumnCount(len(baslik))
        self.ui.search_table.setRowCount(len(data))

        max_word = 0
        item_counter = 0
        if aranacak == "fixes":
            for i in data:
                fixes_information = data[i]
                name = fixes_information["name"]
                probability = str(fixes_information["probability"]) + " %"
                functions = str(fixes_information["functions"])
                item1 = QTableWidgetItem(str(name))
                item1.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 0, item1)
                item2 = QTableWidgetItem(str(probability))
                item2.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 1, item2)
                functions = str(functions)
                functions = functions.replace("[", "")
                functions = functions.replace("]", "")
                functions = functions.replace("'", "")
                functions = functions.replace('"', "")
                # functions = functions.replace("Accuracy", "Olasılık")
                # functions = functions.replace("Attack", "Saldırı")
                # functions = functions.replace("Attack Speed", "Saldırı Hızı")
                # functions = functions.replace("Weapon's", "Silah")
                # functions = functions.replace("Weapons", "Silah")
                # functions = functions.replace("Pierce", "Delme")
                # functions = functions.replace("Reattack", "Tekrar Saldırı")
                # functions = functions.replace("recovery", "yenileme")
                # functions = functions.replace("rare", "oranı")
                # functions = functions.replace("speed", "hızı")
                # functions = functions.replace("time", "zaman")
                # functions = functions.replace("Adv", "Gelişmiş")
                # functions = functions.replace("Std", "Standart")
                # functions = functions.replace("Shield", "Kalkan")
                # functions = functions.replace("Capacity", "Kapasite")
                # functions = functions.replace("Range", "Menzil")

                item3 = QTableWidgetItem(str(functions))
                item3.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 2, item3)
                if len(name) > max_word:
                    max_word = len(name)
                if len(probability) > max_word:
                    max_word = len(probability)
                if len(functions) > max_word:
                    max_word = len(functions)
                self.ui.search_table.setColumnWidth(0, max_word )
                self.ui.search_table.setColumnWidth(1, max_word )
                self.ui.search_table.setColumnWidth(2, max_word * 10)
                item_counter += 1
        if aranacak == "items":
            for i in data:
                #["item_id", "item_name", "level", "gear"]
                item_id = i["itemCode"]["idString"]
                item_name = self.clear_slash(i["name"])
                level = i["level"]
                gear = i["gear"]
                if gear == 3840:
                    gear = "A - Gear"
                elif gear == 15:    
                    gear = "B - Gear"
                elif gear == 61440:
                    gear = "I - Gear"
                elif gear == 240:
                    gear = "M - Gear"
                elif gear == 61680:
                    gear = "M - Gear + I - Gear"
                elif gear == 61695:
                    gear = "M - Gear + I - Gear + B - Gear"
                item1 = QTableWidgetItem(str(item_id))
                item1.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 0, item1)
                item2 = QTableWidgetItem(str(item_name))
                item2.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 1, item2)
                item3 = QTableWidgetItem(str(level))
                item3.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 2, item3)
                item4 = QTableWidgetItem(str(gear))
                item4.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 3, item4)

                item_counter += 1
        if aranacak == "monsters":
            for i in data:
                #["id", "name", "level"]
                id = i["monsterCode"]["idString"]
                name = self.clear_slash(i["name"])
                level = i["level"]
                item1 = QTableWidgetItem(str(id))
                item1.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 0, item1)
                item2 = QTableWidgetItem(str(name))
                item2.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 1, item2)
                item3 = QTableWidgetItem(str(level))
                item3.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 2, item3)
                item_counter += 1
        if aranacak == "gears":
            for i in data:
                #["id", "name", "level", "gear", "nation"]
                id = i["gearCode"]["idString"]
                name = self.clear_slash(i["name"])
                level = i["level"]
                gear = i["gear"]
                if gear == 4096:
                    gear = "I - Gear"
                elif gear == 1:
                    gear = "B - Gear"
                elif  gear == 16:
                    gear = "M - Gear"
                elif gear == 256:
                    gear = "A - Gear"
                else:
                    gear = "N/A"
                nation = i["nation"]
                if nation == 4:
                    nation = "ANI"
                elif nation == 2:
                    nation = "BCU"
                else:
                    nation = "N/A"
                item = QTableWidgetItem(str(id))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 0, item)
                item1 = QTableWidgetItem(str(name))
                item1.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 1, item1)
                item2 = QTableWidgetItem(str(level))
                item2.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 2, item2)
                item3 = QTableWidgetItem(str(gear))
                item3.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 3, item3)
                item4 = QTableWidgetItem(str(nation))
                item4.setTextAlignment(Qt.AlignCenter)
                self.ui.search_table.setItem(item_counter, 4, item4)



                item_counter += 1
    def setup_for_app(self):
        self.update_clock()
        result = self.mothership_time()
        self.savunma_anamgemi_saati =  datetime.datetime.strptime(result["ani"][0] + " " + result["ani"][1], '%Y-%m-%d %H:%M:%S')
        self.saldiri_anagemi_saati =  datetime.datetime.strptime(result["bcu"][0] + " " + result["bcu"][1], '%Y-%m-%d %H:%M:%S')
        # self.savunma_anamgemi_saati = datetime.datetime.strptime("2021-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')
        # self.saldiri_anagemi_saati = datetime.datetime.strptime("2021-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')
    def boss_list_clicked(self):
        basliklar = ["boss_id", "boss_name",  "drop_id","drop_name",  "level", "minimumCount", "maximumCount", "dropProbability"]
        self.ui.boss_drop_table.clear()
        current_index = self.ui.boss_list.currentIndex()
        boss_name = self.ui.boss_list.currentText()
        boss_id = list(self.default.bosses_ids.keys())[current_index]
        info = self.database.get_boss_information(boss_id)
        self.ui.boss_drop_table.setColumnCount(len(basliklar))
        self.ui.boss_drop_table.setRowCount(len(info))
        self.ui.boss_drop_table.setHorizontalHeaderLabels(basliklar)
        self.ui.boss_drop_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.boss_drop_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.boss_drop_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        max_word = 0
        for i in range(len(info)):
            boss_idx = info[i][0]
            boss_name = info[i][1]
            drop_name = info[i][3]
            drop_id = info[i][2]
            level = info[i][4]
            minimumCount = info[i][7]
            maximumCount = info[i][8]
            dropProbability = info[i][9]
            if len(drop_name) > max_word:
                max_word = len(drop_name)
            if len(str(dropProbability)) > max_word:
                max_word = len(str(dropProbability))
            if len(str(minimumCount)) > max_word:
                max_word = len(str(minimumCount))
            if len(str(maximumCount)) > max_word:
                max_word = len(str(maximumCount))
            if len(str(level)) > max_word:
                max_word = len(str(level))
            if len(str(drop_id)) > max_word:
                max_word = len(str(drop_id))
            if len(str(boss_idx)) > max_word:
                max_word = len(str(boss_idx))
            item1= QTableWidgetItem(str(boss_idx))
            item1.setTextAlignment(Qt.AlignCenter)
            self.ui.boss_drop_table.setItem(i, 0, item1)
            item2 = QTableWidgetItem(str(boss_name))
            item2.setTextAlignment(Qt.AlignCenter)
            self.ui.boss_drop_table.setItem(i, 1, item2)
            item3 = QTableWidgetItem(str(drop_id))
            item3.setTextAlignment(Qt.AlignCenter)
            self.ui.boss_drop_table.setItem(i, 3, item3)
            item4 = QTableWidgetItem(str(drop_name))
            item4.setTextAlignment(Qt.AlignCenter)
            self.ui.boss_drop_table.setItem(i, 2, item4)
            item5 = QTableWidgetItem(str(level))
            item5.setTextAlignment(Qt.AlignCenter)
            self.ui.boss_drop_table.setItem(i, 4, item5)
            item6 = QTableWidgetItem(str(minimumCount))
            item6.setTextAlignment(Qt.AlignCenter)
            self.ui.boss_drop_table.setItem(i, 5, item6)
            item7 = QTableWidgetItem(str(maximumCount))
            self.ui.boss_drop_table.setItem(i, 6, item7)
            item7.setTextAlignment(Qt.AlignCenter)
            item8 = QTableWidgetItem(str(dropProbability) + " %")
            self.ui.boss_drop_table.setItem(i, 7, item8)


        self.ui.boss_drop_table.setColumnWidth(0, max_word * 6)
        self.ui.boss_drop_table.setColumnWidth(1, max_word * 6)
        self.ui.boss_drop_table.setColumnWidth(2, max_word * 6)
        self.ui.boss_drop_table.setColumnWidth(3, max_word * 6)
        self.ui.boss_drop_table.setColumnWidth(4, max_word * 6)
        self.ui.boss_drop_table.setColumnWidth(5, max_word * 6)
        self.ui.boss_drop_table.setColumnWidth(6, max_word * 6)
        self.ui.boss_drop_table.setColumnWidth(7, max_word * 6)
    def print_beutiful_json (self, json_data):
        print(json.dumps(json_data, indent=4, sort_keys=True))
    def variables(self):
        self.total_count = 0
        self.update_key = ""
        self.download_percent = 0
        self.kayit = False
        self.kayit_key = None
        self.savunma_anamgemi_saati = datetime.datetime.now()
        self.saldiri_anagemi_saati = datetime.datetime.now()
        self.anagemi_renk_degisim = [False,False]
        self.aranacak_on_ekler = []
        self.aranacak_son_ekler = []
        self.arama_izin = [False,False]
        self.mouse_events = []
        self.macro_keys = [16777264, 16777265, 16777266, 16777267, 16777268]
        self.attachment_p_macro = None
        self.attachment_s_macro = None
        self.attachment_p_silme_macro = None
        self.attachment_s_silme_macro = None
        self.stop = False
    def clear_slash(self, name):
        word = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o", "p","q","r","s","t","u","v","w","x","y","z"]
        for w in word:
            if "\\"+w in name:
                name = name.replace("\\"+w,"")
        return name
    def get_boss_information(self, boss_id):
        #/pedia/monster/{boss_id}
        url = self.default.istek_url + "pedia/monster/" + boss_id
        r = requests.get(url, headers=self.headers)
        result = r.json()["result"]
        name = result["name"]
        boss_name = self.clear_slash(boss_name)
        level = result["level"]
        hp = result["hp"]
        speed = result["speed"]
        range = result["range"]
        recoveryValue = result["recoveryValue"]
        recoveryTime = result["recoveryTime"]
        experience = result["experience"]
        tier = result["tier"]
        drop = result["drop"]
        self.database.insert_boss(boss_id, boss_name, level, hp, speed, range, recoveryValue, recoveryTime, experience, tier)
        for i in drop:
            itemCode = i["referenceItem"]["itemCode"]["idString"]
            item_name = i["referenceItem"]["name"]
            item_name = self.clear_slash(item_name)
            level = i["referenceItem"]["level"]
            gear = i["referenceItem"]["gear"]
            iconId = i["referenceItem"]["iconId"]
            minimumCount = i["minimumCount"]
            maximumCount = i["maximumCount"]
            dropProbability = i["dropProbability"] 
            self.database.insert_item_for_bosses(boss_id, boss_name, itemCode, item_name, level, gear, iconId, minimumCount, maximumCount, dropProbability)
            self.total_count += 1
            self.download_percent = (self.total_count / self.default.total_drop_item_count) * 100 
            self.download_percent = str(self.download_percent)[:5]
            self.download_percent = float(self.download_percent)
    def get_id_code_for_fixes(self, fixes_name, item_code = 2):
        url = self.default.istek_url + "pedia/search/" + fixes_name
        params = { "filterItemKind": "18"}
        r = requests.get(url, headers=self.headers, params=params)
        chooses = ["items", "monsters", "fixes", "gears"]
        r = r.json()["result"]
        all_item_code = []
        for i in r[chooses[item_code]]:
            i = i["fixCode"]
            i = i["idString"]
            all_item_code.append(i)
        return all_item_code
        # return []
    def get_kills(self, filter_name = None):
        #/info/server/kills
        url = self.default.istek_url + "info/server/kills"
        r = requests.get(url, headers=self.headers)
        result = r.json()
        result_kills = {}
        count = 0
        for kill in result["result"]:

            kill_time = kill["killTime"]
            kill_map = self.clear_slash(kill["killMapName"])
            killPossitionX = kill["killPositionX"]
            killPossitionY = kill["killPositionY"]
            killPossitionZ = kill["killPositionZ"]


            killerCharacterName = self.clear_slash(kill["killerCharacterName"])
            killerFame = kill["killerFame"]
            killerDeaths = kill["killerDeaths"]
            killerNation = str(kill["killerNation"])

            if killerNation == "4":
                killerNation = "ANI"
            elif killerNation == "2":
                killerNation = "BCU"
            else:
                killerNation = "N/A"
            victimCharacterName = self.clear_slash(kill["victimCharacterName"])
            victimFame = kill["victimFame"]
            victimDeaths = kill["victimDeaths"]
            victimNation = str(kill["victimNation"])
            if victimNation == "4":
                victimNation = "ANI"
            elif victimNation == "2":
                victimNation = "BCU"
            else:
                victimNation = "N/A"
            if filter_name != None:
                if filter_name in killerCharacterName or filter_name in victimCharacterName:
                    result_kills[count] = {"kill_time":kill_time, "kill_map":kill_map, "killPossitionX":killPossitionX, "killPossitionY":killPossitionY, "killPossitionZ":killPossitionZ, "killerCharacterName":killerCharacterName, "killerFame":killerFame, "killerDeaths":killerDeaths, "killerNation":killerNation, "victimCharacterName":victimCharacterName, "victimFame":victimFame, "victimDeaths":victimDeaths, "victimNation":victimNation}
            else:
                result_kills[count] = {"kill_time":kill_time, "kill_map":kill_map, "killPossitionX":killPossitionX, "killPossitionY":killPossitionY, "killPossitionZ":killPossitionZ, "killerCharacterName":killerCharacterName, "killerFame":killerFame, "killerDeaths":killerDeaths, "killerNation":killerNation, "victimCharacterName":victimCharacterName, "victimFame":victimFame, "victimDeaths":victimDeaths, "victimNation":victimNation}
            count += 1
        return result_kills
        # return {}
    def search_fixes(self, fixes_name):
        fixes_id = self.get_id_code_for_fixes(fixes_name)
        return_dict = {}
        if len(fixes_id) != 0:
            for fix in fixes_id:
                url = self.default.istek_url + "pedia/fix/" + str(fix)
                r = requests.get(url, headers=self.headers)
                r = r.json()["result"]
                if r != None:
                    dict_ = {}
                    dict_["name"] = self.clear_slash(r["name"])
                    dict_["functions"] = r["functions"]
                    dict_["probability"] = r["probability"]
                    if not "of" in dict_["name"]:
                        return_dict[fix] = dict_
            return return_dict
        else:
            return {}
        # return {}
    def search_general(self, general_name):
        aranacak = self.ui.ne_aranacak.currentText()

        if aranacak == "":
            aranacak = "items"
        if aranacak == "fixes":
            return self.search_fixes(general_name)
        else:
            url = self.default.istek_url + "pedia/search/" + general_name
            r = requests.get(url, headers=self.headers)
            r = r.json()["result"]

        try:
            return r[aranacak]
        except:
            return []
        
        # return []
    def mothership_time(self):
        #/info/motherships
        url = self.default.istek_url + "info/motherships"
        r = requests.get(url, headers=self.headers)
        r = r.json()
        json_= {}
        json_["ani"] = r["result"]["ani"].split("T")
        json_["bcu"] = r["result"]["bcu"].split("T")
        return json_
        # return {}
    def get_news(self):
        #/info/server/stats
        url = self.default.istek_url + "info/server/stats"
        r = requests.get(url, headers=self.headers)
        r = r.json()
        veri = {}
        veri["updateDate"] = r["updatedAt"].split(".")[0].split("T")
        veri["registeredUsers"] = r["result"]["registeredUsers"]
        veri["createdGears"] = r["result"]["createdGears"]
        veri["createdBrigades"] = r["result"]["createdBrigades"]
        guncelleme_zamani = veri["updateDate"][1]
        kayit_olan = veri["registeredUsers"]
        tugay_olusturan = veri["createdBrigades"]
        oyuncu_olusturan = veri["createdGears"]
        text = "Güncelleme Zamanı : {}\nYeni Kayıt : {}\nYeni Tugay : {}\nYeni Oyuncu : {}".format(guncelleme_zamani, kayit_olan, tugay_olusturan, oyuncu_olusturan)
        self.ui.oyuncu_bilgi.setText(text)
        QTimer.singleShot(60000, self.update_clock)
    def update_clock(self):
        date = datetime.datetime.now()
        date = date - datetime.timedelta(hours=2)
        date = date.strftime("%H:%M:%S")
        self.ui.saat_tarih.setText( "   "+date +"   ")
        self.update_information()
        QTimer.singleShot(1000, self.update_clock)
    def seconds_to_time(self, seconds):
        day = seconds // (24 * 3600)
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        seconds = seconds
        return_time = str(hour) + " h " + str(minutes) + " m " + str(seconds) + " s"
        return [return_time, day]
    def update_information(self):
        all = ""
        savunma_kalan_zaman = self.savunma_anamgemi_saati - datetime.datetime.now() + datetime.timedelta(hours=2)
        day = savunma_kalan_zaman.days
        savunma_kalan_zaman = savunma_kalan_zaman.seconds
        if savunma_kalan_zaman < 86400 and day == 0:
            if self.anagemi_renk_degisim[0]:
                self.ui.savunma.setStyleSheet("background-color: rgb(255, 255, 255); font: 700 20pt \"Segoe UI\"; border-radius: 15px; ")
                self.anagemi_renk_degisim[0] = False
            else:
                self.ui.savunma.setStyleSheet("background-color: rgb(255, 0, 0); font: 700 20pt \"Segoe UI\"; border-radius: 15px;")
                self.anagemi_renk_degisim[0] = True
        self.ui.savunma.setText("   SAVUNMA ANAGEMI : {} d ".format(day) + self.seconds_to_time(savunma_kalan_zaman)[0] +"   ")
        saldiri_kalan_zaman = self.saldiri_anagemi_saati - datetime.datetime.now() + datetime.timedelta(hours=2)
        day = saldiri_kalan_zaman.days
        saldiri_kalan_zaman = saldiri_kalan_zaman.seconds
        if saldiri_kalan_zaman < 86400 and day == 0:
            if self.anagemi_renk_degisim[1]:
                self.anagemi_renk_degisim[1] = False
                self.ui.saldiri.setStyleSheet("background-color: rgb(255, 255, 255); font: 700 20pt \"Segoe UI\"; border-radius: 15px;")

            else:
                self.ui.saldiri.setStyleSheet("background-color: rgb(0, 255, 0); font: 700 20pt \"Segoe UI\"; border-radius: 15px; ")

                self.anagemi_renk_degisim[1] = True
        self.ui.saldiri.setText("   SALDIRI ANAGEMI:  {} d ".format(day) +self.seconds_to_time(saldiri_kalan_zaman)[0] +"   ")
        all += "Savunma Anagemi : {},       Saldiri Anagemi : {}".format(str(self.savunma_anamgemi_saati.strftime("%d/%m/%y %H:%M:%S")), str(self.saldiri_anagemi_saati.strftime("%d/%m/%y %H:%M:%S")))
        

        
        self.ui.bottom_label.setText(all)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

