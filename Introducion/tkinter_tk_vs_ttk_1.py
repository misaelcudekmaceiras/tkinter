#Esto es codigo Tk puro

from tkinter import *


root = Tk()



l1 = Label(text="Test", fg="black", bg="white")  #fg bg no exiten en ttk
l2 = Label(text="Test", fg="black", bg="white")  #fg bg no exiten en ttk

print(dir(l1))

l1.pack()
l2.pack()

root.mainloop()