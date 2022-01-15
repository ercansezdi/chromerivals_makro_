#!/usr/bin/env python
 # -*- coding: utf-8 -*-
from tkinter import *
import threading
from tkinter.messagebox import showinfo
import os
import tkinter.ttk
from tkinter import ttk
import configparser
from tkinter import messagebox
from functools import partial
import requests
import zipfile
from shutil import move,copytree,rmtree
from time import sleep




class tkinterGui(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Updater")



        self.variables()
        self.InitGui()
        
    def InitGui(self):
        self.canvas = Canvas(self.update, width=800, height=445)
        self.canvas.grid(row=0, column=0)
        self.target1 = threading.Thread(target = self.check)
        self.target1.start()


    def variables(self):

        self.path1 = os.getcwd() +"\\updater\\update\\"
        self.path2 = os.getcwd()
        self.info = configparser.ConfigParser()
        self.info.read("file\\config.ini")
        self.update = Frame(self.parent)
        self.update.grid(row=0,column=0)
        input_file_say = 74 
        self.stop = False
        imagelist = []
        for i in range(0,input_file_say+1):
            imagelist.append('file/loading/'+ str(i)+".gif")
        self.giflist = []
        for imagefile in imagelist:
            photo = PhotoImage(file=imagefile)
            self.giflist.append(photo)
    def check(self):
        if int(self.info["info"]["version"]) < 10:
            link = self.info["info"]["update_link"]+"version_v_"+self.info["info"]["version"] + ".zip"
        else:
            link = self.info["info"]["update_link"]+"version_v_"+self.info["info"]["version"] + ".zip"
        sorgu = requests.head(link, allow_redirects=True)     
        
        if sorgu.status_code == 200:
            sorgu = requests.get(link, allow_redirects=True)
            open(os.getcwd() +'\\updater\\update.zip', 'wb').write(sorgu.content)
            self.setup()
    
        else:
            showinfo(self.info["english"]["notice_4"], self.info["english"]["notice_15"])
            self.stop_loading()
        
    def setup(self):
        with zipfile.ZipFile(os.getcwd() +"\\updater\\update.zip", 'r') as zip_ref:
            zip_ref.extractall(os.getcwd()+"\\updater")
        
        
        dirs,files = self.check_path(os.getcwd() +"\\updater\\update\\")
        for i in dirs:
            try:
                copytree ( self.path1+i , self.path2+"\\"+i )
                rmtree(self.path1+i)
            except:
                rmtree(self.path2+"\\"+i)
                copytree ( self.path1+i , self.path2+"\\"+i )
                rmtree(self.path1+i)
        for i in files:
            try:
                move(self.path1 + i, self.path2)
            except:
                os.remove(self.path2+"\\"+i)
                move(self.path1 + i, self.path2)
        rmtree(self.path1)

        os.remove(self.path2+"\\updater\\update.zip")

        self.stop_loading()
        
    def check_path(self,path):
        print(path)
        for (root,dirs,files) in os.walk(path, topdown=True):
            break
    
        return dirs,files


    
               
    def start_loading(self,n=0):
        gif = self.giflist[n%len(self.giflist)]
        self.canvas.create_image(gif.width()//2, gif.height()//2, image=gif)
        if not self.stop:
            root.after(50, self.start_loading, n+1) 
    def stop_loading(self):
        self.stop = True
        sleep(1)
        self.parent.destroy()

    
if __name__ == "__main__":
    root = Tk()
    root.call('tk', 'scaling', 1.0)
    run = tkinterGui(root)
    root.after(1000,run.start_loading)
    root.mainloop()
