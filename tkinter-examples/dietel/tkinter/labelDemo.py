from Tkinter import *

class LabelDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Labels")
        
        self.Label1 = Label(self, text="Label with text")
        self.Label1.pack()
        
        self.Label2 = Label(self, text="Labels with text and a bitmap")
        self.Label2.pack(side=LEFT)

        self.Label3 = Label(self, bitmap="warning")
        self.Label3.pack(side=LEFT)

def main():
    LabelDemo().mainloop()

if __name__ == '__main__':
    main()
