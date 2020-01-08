
from tkinter import *

root = Tk()
root.title("To moje pierwsze GUI")
root.geometry("500x420")

app = Frame(root)
app.grid()
lbl = Label(app, text= "Jestem etykietą")
lbl.grid()

b1 = Button(app, text= "Pierwszy przycisk")
b1.grid()

b2 = Button(app)
b2.grid()
b2.configure(text="Drugi")

b3 = Button(app)
b3.grid()
b3["text"] = "MOzńa tez w ten sposob poprawic"

root.mainloop()