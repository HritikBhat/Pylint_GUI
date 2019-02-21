""" Author: Hritik Bhat"""

import subprocess,re
from tkinter import Button, Text, Label, Tk, Entry, ttk
import tkinter as tk

def install_pylint():
     icmd="pip install pylint"
     inst = subprocess.run(icmd, shell=True)
    
def clicked(txt1,strval):
    if strval not in txt1['values']:
        txt1['values'] = (*txt1['values'], strval)
        
    cmd="pylint "+strval
    DATA.delete('1.0', tk.END)
    try:
        content = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        DATA.insert("1.0", content.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as err:
        text_show=err.output.decode('utf-8')
        DATA.insert("1.0",text_show)
        
        for i in text_show.splitlines():
         if re.search("^Your code",i) is not None:
             display_score.set(i)
             break


ROOT=Tk()
display_score=tk.StringVar()
ROOT.title("Pylint GUI")
ROOT.geometry("700x900")
LB1=Label(ROOT, text="Path:")
LB1.place(x=2, y=40)

TXT1 = ttk.Combobox(ROOT, width=60)
TXT1['values'] = ("")
TXT1.place(x=60, y=40)
TXT1.current()

SETBTN = Button(ROOT, text="Set", height=1, width=10, command=lambda: clicked(TXT1,TXT1.get()))
SETBTN.place(x=500, y=35)

INTBTN = Button(ROOT, text="Install Pylint Library", height=1, width=30, command=lambda: install_pylint())
INTBTN.place(x=450, y=95)


DATA = Text(ROOT, width=95, height=80)
DATA.configure(font=("Black Arial", "10"))
DATA.place(x=15, y=130)

LB2=Label(ROOT, textvariable=display_score)
LB2.place(x=20, y=100)
