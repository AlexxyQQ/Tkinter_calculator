from _ast import Lambda
from tkinter import *

# Tkinter

root = Tk()
root.configure(background='black')  # changes the board background to black

root.title('Calculator')

eqn = StringVar()  # holding a empty string

#entry(display) portion
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

#buttons

button_1 = Button(
    root,
    text='1',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='#fdc703',
    activebackground='black',
    )

#placements

button_1.grid(row=3, column=0,)

mainloop()