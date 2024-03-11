#Esto es codigo ttk puro

from tkinter import *
from tkinter import ttk


root = Tk()


style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(root,text="Test", style="BW.TLabel")
l2 = ttk.Label(root,text="Test", style="BW.TLabel")

l1.pack()
l2.pack()

root.mainloop()