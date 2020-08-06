import sys
from Tkinter import *
widget = Button(None, text='Hello Widget world!', command=sys.exit)
widget.pack()
widget.mainloop()