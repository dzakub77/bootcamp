
from tkinter import *

class Apka2(Frame):
    def __init__(self, master):
        super(Apka2, self).__init__(master)
        self.grid()
        self.b_clicks = 0
        self.create_widget()

    def create_widget(self):
        self.b = Button(self, text="Liczba kliknięć = 0")
        self.b['command'] = self.update_count
        self.b.grid()

    def update_count(self):
        self.b_clicks += 1
        self.b['text'] = "Liczba kliknięć = " + str(self.b_clicks)

root = Tk()
root.title('Tym razem liczenie kliknięć')
root.geometry("500x400")
app = Apka2(root)
root.mainloop()