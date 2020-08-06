from Tkinter import *
root = Tk()
labelfont = ('courier', 24, 'bold')
widget = Label(root, text='Hello config world')
widget.config(bg='black', fg='yellow')
widget.config(font=labelfont)
widget.pack(expand=YES, fill=BOTH)
root.mainloop()
