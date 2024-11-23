from tkinter import *

import webbrowser
def Mem():
    webbrowser.open('https://humanbenchmark.com/tests/memory')

def F1timer():
    webbrowser.open("https://f1-start.glitch.me")

def Tp():
    webbrowser.open("https://monkeytype.com")

def GH():
    webbrowser.open('https://github.com/XShucks/Ultimate-1v1')

Menu = Tk() #makes a window instance titled the first word
Menu.geometry ("1920x1080")# changes window size to whatever you want it to be (the size is in the perenthesis)
Menu.title("Chalenge Menu")
Menu.config (background='red')

Reaction = Button(Menu,text='Reaction Speed')
Reaction.config(command=F1timer)
Reaction.config(font=('TektonPro'))
Reaction.config(bg='#ad2d2d')
Reaction.config(activebackground='black')
Reaction.config(activeforeground='white')
Reaction.pack()

Memory = Button(Menu,text='Memory Test')
Memory.config(font=('TektonPro'))
Memory.config(bg='#ad2d2d')
Memory.config(activebackground='black')
Memory.config(activeforeground='white')
Memory.config(command=Mem)
Memory.pack()

Type = Button(Menu,text='Typing Test')
Type.config(font=('TektonPro'))
Type.config(bg='#ad2d2d')
Type.config(activebackground='black')
Type.config(activeforeground='white')
Type.config(command=Tp)
Type.pack()

Github = Button(Menu,text='Github Page')
Github.config(font=('TektonPro'))
Github.config(bg='#ad2d2d')
Github.config(activebackground='black')
Github.config(activeforeground='white')
Github.pack(side=BOTTOM, pady=10)

Menu.mainloop() #displays that mf

