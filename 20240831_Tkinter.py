# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:39:09 2024

@author: cclin
"""

import tkinter as tk

import tkinter.messagebox

def clickMe():
    tkinter.messagebox.showinfo(title='提示',message='good')

window = tk.Tk()

window.title("我的第一個GUI程式")

window.geometry('300x300')

label = tk.Label(window,text="我的GUI")

label = tk.Label(window,text="-我的GUI-",bg="#04D",fg="#6CF")

label.pack()

entry = tk.Entry(window,width = 30)

entry.pack()

button = tk.Button(window,text = "按鈕",command = clickMe)

button.pack()

window.mainloop()