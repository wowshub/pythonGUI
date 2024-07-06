# add 更改项目到桌面 bepythonlearning


from tkinter import *
win = Tk()
win.title("yangyangmir2")
txt=Label(win,text="\n\nyangyang传奇2\n\n",bg="yellow").pack()

scrw=win.winfo_screenwidth()
scrh=win.winfo_screenheight()
x= (scrw-1024)/2
y=(scrh-768)/2
win.geometry('%dx%d+%d+%d' % (1024,768,x,y))
# win.geometry("1024x768-0-0")
win.configure(bg="yellow")
win.maxsize(1024,1024)
win.minsize(768,768)
win.resizable(0,0)
# win.state("zoomed")
# win.iconify()
win.iconbitmap('icon57.ico')
# iconbitmap("")
win.mainloop()