import sys
from Tkinter import Toplevel, Button, Label

# two independant windows but part of the same process
win1 = Toplevel()
win2 = Toplevel()

Button(win1, text='Spam', command=sys.exit).pack()
Button(win2, text='SPAM', command=sys.exit).pack()

Label(text='Popups').pack()
win1.mainloop()