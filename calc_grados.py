# -*- coding: cp1252 -*-
from Tkinter import *
root=Tk()
root.title("Convertidor de grados")
root.geometry('400x300')

def delete():
    grados.delete(0,END)
    Lblrd=Label(text="                                                                    ").place(x=240, y=120)

def cf():
    n=text1.get()
    op1=(n*1.8)+32
    Lblr=Label(text=op1).place(x=240, y=120)

def ck():
    n=text1.get()
    op2=n+273.14
    Lblr1=Label(text=op2).place(x=240, y=120)

def fk():
    n=text1.get()
    op3=((n-32)/1.8)+273.14
    Lblr2=Label(text=op3).place(x=240, y=120)

def fc():
    n=text1.get()
    op4=(n-32)/1.8
    Lblr3=Label(text=op4).place(x=240, y=120)

def kf():
    n=text1.get()
    op5=((n-273)*1.8)+32
    Lblr3=Label(text=op5).place(x=240, y=120)

def kc():
    n=text1.get()
    op6=(n-273.14)
    Lblr3=Label(text=op6).place(x=240, y=120)
    
lnlgrados=Label(root, text="ingresa los grados")
lnlgrados.grid(row=2,column=1)

text1=DoubleVar()
grados=Entry(root,width=30,textvariable=text1)
grados.grid(row=2, column=2)


bot1=Button(root,text="C a F", command=cf)
bot1.place(x=20, y=30)

bot2=Button(root,text="C a K", command=ck)
bot2.place(x=80, y=30)

bot3=Button(root,text="F a K", command=fk)
bot3.place(x=20, y=80)

bot4=Button(root,text="F a C", command=fc)
bot4.place(x=80, y=80)

bot5=Button(root,text="K a F", command=kf)
bot5.place(x=20, y=130)

bot6=Button(root,text="K a C", command=kc)
bot6.place(x=80, y=130)

bot7=Button(root, text="DELETE", command=delete)
bot7.place(x=230, y=80)

Lb=Label(text="Resultado=").place(x=180,y=120)

root.mainloop()
