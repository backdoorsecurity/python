#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Sep 22, 2018 09:17:45 AM

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

import socketgui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    socketgui_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    socketgui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+650+150")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.27, rely=0.07, height=23, width=181)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Socket Gui''')
        self.Label1.configure(width=181)

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.12, rely=0.27, height=21, width=41)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''Client''')

        self.tex41 = Text(top)
        self.tex41.place(relx=0.07, rely=0.4, relheight=0.09, relwidth=0.24)
        self.tex41.configure(background="white")
        self.tex41.configure(font="TkTextFont")
        self.tex41.configure(foreground="black")
        self.tex41.configure(highlightbackground="#d9d9d9")
        self.tex41.configure(highlightcolor="black")
        self.tex41.configure(insertbackground="black")
        self.tex41.configure(selectbackground="#c4c4c4")
        self.tex41.configure(selectforeground="black")
        self.tex41.configure(width=144)
        self.tex41.configure(wrap=WORD)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.07, rely=0.33, height=23, width=77)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''IP Address''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.5, rely=0.33, height=23, width=31)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''port''')

        self.Text2 = Text(top)
        self.Text2.place(relx=0.45, rely=0.4, relheight=0.09, relwidth=0.19)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=114)
        self.Text2.configure(wrap=WORD)

        self.Connect = ttk.Button(top)
        self.Connect.place(relx=0.75, rely=0.4, height=47, width=128)
        self.Connect.configure(takefocus="")
        self.Connect.configure(text='''Connect''')
        self.Connect.configure(width=128)

        self.Text3 = Text(top)
        self.Text3.place(relx=0.08, rely=0.58, relheight=0.4, relwidth=0.87)
        self.Text3.configure(background="white")
        self.Text3.configure(font="TkTextFont")
        self.Text3.configure(foreground="black")
        self.Text3.configure(highlightbackground="#d9d9d9")
        self.Text3.configure(highlightcolor="black")
        self.Text3.configure(insertbackground="black")
        self.Text3.configure(selectbackground="#c4c4c4")
        self.Text3.configure(selectforeground="black")
        self.Text3.configure(width=524)
        self.Text3.configure(wrap=WORD)






if __name__ == '__main__':
    vp_start_gui()


