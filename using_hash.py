
#https://www.python-course.eu/tkinter_entry_widgets.php
import tkinter as tk # Python 3.x Version
# import Tkinter as tk # Python 2.x Version
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from tkinter import *
import hashlib

root = tk.Tk()
root.geometry('600x100') # anchura x altura
root.configure(bg = 'beige')
root.title('Hashing Coorp.')

label = tk.Label(root, text="Introduce el texto", padx=10, pady=10) # Create a text label
label.grid(row=0, column=0) # Pack it into the window
content = StringVar()
e1 = tk.Entry(root, text='Caption', width=15, textvariable=content)
e1.grid(row=0, column=1)
e1.focus_set()


def hide_text():
    if show_text.get():
        e1.configure(show="*")
    else:
        e1.configure(show="")


show_text = BooleanVar()
show_text.set(False)  # set check state
chk = Checkbutton(root, text='Ver texto', var=show_text, command=hide_text)
chk.grid(row=0, column=2)
label2 = tk.Label(root, text="------>", padx=10, pady=10)
label2.grid(row=0, column=3)

hash_text = StringVar()
e2 = tk.Entry(root, text='El hash', width=30, textvariable=hash_text)
e2.grid(row=0, column=4)
label2 = tk.Label(root, text="El hash", padx=10, pady=10)
label2.grid(row=0, column=5)




def generate_hash():
    '''Esta función debera generar un hash para el texto de entrada'''
    text = content.get()
    hash_generated = hashlib.sha256(str(text).encode('utf-8')).hexdigest()
    print(hash_generated)
    hash_text.set(str(hash_generated))
    return hash_generated


hash_button = ttk.Button(root,text='HashMe', command=generate_hash)
hash_button.grid(row=4, column=2)
salir_button = ttk.Button(root, text='Salir', command=quit)
salir_button.grid(row=4, column=4)

root.mainloop()
