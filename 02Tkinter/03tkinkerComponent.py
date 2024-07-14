# -*- coding: utf-8 -*-
"""
@author: beyourself
@contact: 29098663@qq.com
@file: 03tkinkerComponent.py
@time: 2024-07-14 9:12
@version: 1.0
@desc: pythonGUI project
"""

def show():
    Label(win,image=img).pack()

from tkinter import *

win=Tk()
img=PhotoImage(file='pic/bb.png')
but1=Button(win,text="添加图片",command=show).pack()
win.mainloop()