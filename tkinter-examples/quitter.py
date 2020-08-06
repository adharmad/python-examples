from Tkinter import *
from tkMessageBox import askokcancel

class Quitter(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		widget=Button(self, text='Quit', command=self.quit)
		widget.pack(side=LEFT)
	def quit(self):
		ans = askokcancel('Verify exit', "Really Quit?")
		if ans:
			import sys; sys.exit()

if __name__ == '__main__':
	Quitter().mainloop()
