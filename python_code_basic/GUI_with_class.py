
from tkinter import *

class Apka(Frame):
    def __init__(self, master):
        super(Apka, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.b1 = Button(self, text="To jest pierwwszy przycisk")
        self.b1.grid()

        self.b2 = Button(self)
        self.b2.grid()
        self.b2.configure(text="To jest drugi")

        self.b3 = Button(self)
        self.b3.grid()
        self.b3['text'] = 'To jest trzeci'

root = Tk()
root.title("Kolejny GUI, tym razem jako klasa")
root.geometry('500x400')
app = Apka(root)
root.mainloop()
