from Tkinter import *

class HelloCallable:	
	def __init__(self):
		self.msg = 'Hello __call__ world'

	def __call__(self):
		print self.msg
		import sys; sys.exit()

if __name__ == '__main__':
	widget = Button(None, text='hello event world', command=HelloCallable())
	widget.pack()
	widget.mainloop()
