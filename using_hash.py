
#https://www.python-course.eu/tkinter_entry_widgets.php
import tkinter as tk # Python 3.x Version
# import Tkinter as tk # Python 2.x Version

root = tk.Tk()

label = tk.Label(root, text="Introduce el texto") # Create a text label
label.grid(row=0) # Pack it into the window
e1 = tk.Entry(root)
e1.grid(row=0, column=1)
root.mainloop()
