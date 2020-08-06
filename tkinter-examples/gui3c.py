from Tkinter import *

class Helloclass:	
	def __init__(self):
		widget = Button(None, text='hello event world', command=self.quit)
		widget.pack()

	def quit(self):
		print 'Hello class method world'
		import sys; sys.exit()

if __name__ == '__main__':
	Helloclass()
	mainloop()
