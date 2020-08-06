from Tkinter import *

def quit():
	print 'Hello, I must get going...'
	import sys; sys.exit()

widget =Button(None, text='Hello event world!', command=quit)
widget.pack()
widget.mainloop()