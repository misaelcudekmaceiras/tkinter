from tkinter import *
from tkinter import ttk
root = Tk()   #creo un objeto Tk

#widget

frm = ttk.Frame(root, padding=10)

frm.grid()

ttk.Label(frm, text="Hola Mundo!").grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0 , row=0)

root.mainloop()

print('Hola Mundo') 