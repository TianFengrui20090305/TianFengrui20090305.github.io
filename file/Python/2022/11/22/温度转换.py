import tkinter as tk
import tkinter.messagebox
IsNum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
win=tk.Tk()
win.title("温度转换")
win.geometry("250x200")
var_C=tk.StringVar()
var_C.set('')
var_F=tk.StringVar()
var_F.set('')

def IsNumDef(Str, Num):
    for i in range(Num):
        pd=False
        for j in range(10):
            if Str[i]==IsNum[j]:
               pd=True
        if pd==False:
            return 0
    return 1

def CtoF():
    C=var_C.get()
    if C!='' and IsNumDef(C, len(C)):
        F=float(C)*1.8+32
        var_F.set(str(F))
    else:
        tkinter.messagebox.showinfo(title='ERROR', message='你食不食油饼')
def FtoC():
    F=var_F.get()
    if F!='' and IsNumDef(F, len(F)):
        C=((5/9)*(float(F)-32))
        var_C.set(str(C))
    else:
        tkinter.messagebox.showinfo(title='ERROR', message='你食不食油饼')
def cancle():
    var_C.set('')
    var_F.set('')
def _quit():
    win.quit()
    win.destroy()
CzhuanF=tk.Label(win,text='摄氏温度C：',width=80)
FzhuanC=tk.Label(win,text='华氏温度F：',width=80)
entC=tk.Entry(win,width=100,textvariable=var_C)
entF=tk.Entry(win,width=100,textvariable=var_F)
but_CzhuanF=tk.Button(win,text='C转F',command=CtoF)
but_FzhuanC=tk.Button(win,text='F转C',command=FtoC)
but_Cancle=tk.Button(win,text='重置',command=cancle)
but_quit=tk.Button(win,text='退出',command=_quit)
CzhuanF.place(x=20,y=10,width=80,height=20)
FzhuanC.place(x=20,y=40,width=80,height=20)
entC.place(x=120,y=10,width=80,height=20)
entF.place(x=120,y=40,width=80,height=20)
but_CzhuanF.place(x=30,y=80,width=50,height=20)
but_FzhuanC.place(x=100,y=80,width=50,height=20)
but_Cancle.place(x=30,y=110,width=50,height=20)
but_quit.place(x=100,y=110,width=50,height=20)
win.mainloop()