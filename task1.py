#!python3
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Jackson's Gui")
label1=tk.Label(window,text="Hello World!")
dogphoto=PhotoImage(file="dog.png")
label2= tk.Label(window, image=dogphoto)
button=tk.Button(window,text="Hello World!")
label1.pack()
label2.pack()
button.pack()
window.geometry("240x480")
window.mainloop()