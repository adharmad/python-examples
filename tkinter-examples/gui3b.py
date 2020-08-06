from Tkinter import *
from sys import stdout, exit

widget =Button(None, 
		text='Hello event world!', 
		command=(lambda: stdout.write('Hello world\n') or exit()) )
widget.pack()
widget.mainloop()