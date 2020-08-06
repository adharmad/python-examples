from sys import exit
from Tkinter import *
from gui6 import Hello

parent = Frame()
parent.pack()
Hello(parent).pack(side=RIGHT)
Button(parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop()
