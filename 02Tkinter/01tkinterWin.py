# add 更改项目到桌面 bepythonlearning


from tkinter import *
win1 = Tk()
win1.title("yangyangmir2")
txt=Label(win1,text="\n\nyangyang传奇2\n\n",bg="yellow").pack()

scrw=win1.winfo_screenwidth()
scrh=win1.winfo_screenheight()
x= (scrw-1024)/2
y=(scrh-768)/2
win1.geometry('%dx%d+%d+%d' % (1024,768,x,y))
# win.geometry("1024x768-0-0")
win1.configure(bg="yellow")
win1.maxsize(1024,1024)
win1.minsize(768,768)
win1.resizable(0,0)
# win.state("zoomed")
# win.iconify()
win1.iconbitmap('icon57.ico')
# iconbitmap("")
win1.mainloop()