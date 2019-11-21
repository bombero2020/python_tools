from tkinter import *
from mongodb_conector import findall

window = Tk()

window.title("Base de datos personal")

window.geometry('350x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
findall()

def clicked():
    res = "Welcome to " + txt.get()

    lbl.configure(text=res)


btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()