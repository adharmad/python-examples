from Tkinter import *
import sys

def greeting():
	print 'Hello stdout World!...'

win = Frame()
win.pack()
Button(win, text='Hello', command=greeting).pack(side=LEFT, expand=YES, fill=Y)
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Quit', command=sys.exit).pack(side=RIGHT, expand=YES, fill=Y)

win.mainloop()