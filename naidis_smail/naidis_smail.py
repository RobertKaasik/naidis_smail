from tkinter import *
def head():
    global headA
    if headA.get()=="on":
        c.create_oval((15,15,450,450))
    elif headA.get()=="off":
        c.create_oval((15,15,450,450),outline="white")
def mouth():
    global mouthA
    if mouthA.get()=="on":
        c.create_oval((100,350,350,350),fill="black")
    elif mouthA.get()=="off":
        c.create_oval((100,350,350,350),outline="white",fill="white")
def nose():
    global noseA
    if noseA.get()=="on":
        c.create_oval((175,200,350,350),fill="red")
    elif noseA.get()=="off":
        c.create_oval((175,200,350,350),outline="white",fill="white")
def eye():
    global eyeA
    if eyeA.get()=="on":
        c.create_oval((125,100,175,150),fill="blue")
    elif eyeA.get()=="off":
        c.create_oval((125,100,175,150),outline="white",fill="white")
def eye2():
    global eye2A
    if eye2A.get()=="on":
        c.create_oval((250,100,300,150),fill="blue")
    elif eye2A.get()=="off":
        c.create_oval((250,100,300,150),outline="white",fill="white")
def unibrow():
    global unibrowA
    if unibrowA.get()=="on":
        c.create_line((380,80,80,80),fill="brown")
    elif unibrowA.get()=="off":
        c.create_line((380,80,80,80),fill="white")
from tkinter import *
tk = Tk()
fm=Frame(tk)
fm.pack(side=RIGHT)
c = Canvas(tk, width=1000, height=500, bg="white") 
c.create_oval((15,15,450,450))#Голова
c.create_oval((125,100,175,150),fill="Blue")#Глаз1
c.create_oval((250,100,300,150),fill="Blue")#Глаз2
c.create_oval((175,200,350,350),fill="red")#Нос
c.create_oval((100,350,350,400),fill="black")#Рот
c.create_line((380,80,80,80),fill="brown")#монобровь
c.pack(side=LEFT)
headA=StringVar()
head=Checkbutton(fm,text="Head",font="Arial 29", fg="black",variable=headA,onvalue="on",offvalue="off",command=head)
mouthA=StringVar()
mouth=Checkbutton(fm,text="Mouth",font="Arial 29", fg="black",variable=mouthA,onvalue="on",offvalue="off",command=mouth) 
noseA=StringVar()
nose=Checkbutton(fm,text="Nose",font="Arial 29", fg="black",variable=noseA,onvalue="on",offvalue="off",command=nose) 
eyeA=StringVar()
eye=Checkbutton(fm,text="Left eye",font="Arial 29", fg="black",variable=eyeA,onvalue="on",offvalue="off",command=eye)
eye2A=StringVar()
eye2=Checkbutton(fm,text="Right eye",font="Arial 29", fg="black",variable=eye2A,onvalue="on",offvalue="off",command=eye2)
unibrowA=StringVar()
unibrow=Checkbutton(fm,text="Unibrow",font="Arial 29", fg="black",variable=unibrowA,onvalue="on",offvalue="off",command=unibrow)


head.pack(side=RIGHT)
mouth.pack(side=RIGHT)
nose.pack(side=RIGHT)
eye.pack(side=RIGHT)
eye2.pack(side=RIGHT)
unibrow.pack(side=RIGHT)

tk.mainloop()
