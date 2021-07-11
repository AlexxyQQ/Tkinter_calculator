from _ast import Lambda
from tkinter import *

# Tkinter

root = Tk()
root.configure(background='black')  # changes the board background to black

root.title('Calculator')

eqn = StringVar()  # holding a empty string
e = Entry(
    root,
    textvariable=eqn,
    width=15,
    borderwidth=0,
    font=('Digital-7', 50),
    fg='#fdc703',
    bg='Black',
    )
e.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=15,
    pady=15,
    ipady=10,
    )

mainloop()