from Tkinter import *

def hello(event):
	print 'Press twice to exit'

def quit(event):
	print 'Hello I must get going...'
	import sys; sys.exit()

widget = Button(None, text='hello event world')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)
widget.mainloop()
