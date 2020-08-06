from Tkinter import *
from tkMessageBox import *

def callback():
	if askyesno('Verify', 'Do you really want to quit?'):
		showwarning('Yes', 'Quit not yet implemented')
	else:
		showinfo('No', 'Quit has been cancelled')

errmsg = 'Sorry no spam allowed'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack(fill=X)
mainloop()