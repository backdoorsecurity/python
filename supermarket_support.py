#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jan 15, 2019 10:05:17 AM

import sqlite3
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



def validateLogin(user,pass1):
    connection=sqlite3.connect("D:\login.db")
    cursor=connection.cursor()
    sql="select * from login where username='"+user+"'"
    #cursor.execute("select * from login where username="+user )
    cursor.execute(sql)
    validate=cursor.fetchone()
    if validate[1]==pass1:
        print("Login Successful")
    else:
        print("Login Failed")



def checkLogin():
    global username,password
    username=w.Entry1.get()
    password=w.Entry1_1.get()
    
    
    validateLogin(username,password)
##    print(username)
##    print(password)
    sys.stdout.flush()



def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import supermarket
    supermarket.vp_start_gui()
    
