# -*- coding: utf-8 -*-
"""
@author: beyourself
@contact: 29098663@qq.com
@file: 2.1layoutPack.py
@time: 2024-07-06 19:59
@version: 1.0
@desc: pythonGUI project
"""

# widget.pack()
import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title('widget layout')
window.geometry('500x500')
# txt1="传奇二"
# txt2="魔兽世界"
# txt3="游戏"


# Label(window, text=txt1,bg="red").pack(side="bottom")
# Label(window, text=txt2,bg="green").pack(side="bottom")
# Label(window, text=txt3,bg="blue").pack(side="bottom")


# Label(window, text=txt1,bg="red",width=20).pack(side="bottom",padx=20,pady=5)
# Label(window, text=txt2,bg="green",width=20).pack(side="bottom",padx=20,pady=5)
# Label(window, text=txt3,bg="blue",width=20).pack(side="bottom",padx=20,pady=5)


# Label(window, text=txt1,bg="red").pack(side="bottom",padx=20,pady=5,ipadx=5,ipady=5)
# Label(window, text=txt2,bg="green").pack(side="bottom",padx=20,pady=5,ipadx=5,ipady=5)
# Label(window, text=txt3,bg="blue").pack(side="bottom",padx=20,pady=5,ipadx=5,ipady=5)


# Label(window, text=txt1,bg="red").pack(side="bottom",fill="y")
# Label(window, text=txt2,bg="green").pack(side="bottom",fill="y")
# Label(window, text=txt3,bg="blue").pack(side="bottom",fill="y")


# Label(window, text=txt1,bg="red").pack(side="bottom",fill="y",expand=True)
# Label(window, text=txt2,bg="green").pack(side="bottom",fill="y",expand=True)
# Label(window, text=txt3,bg="blue").pack(side="bottom",fill="y",expand=True)


Label(window,text='下一步',bg="yellow").pack(anchor="s",side="right",padx=10,pady=10)

window.mainloop()