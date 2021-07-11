from tkinter import *

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
    fg='#6adbd9',
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
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_2 = Button(
    root,
    text='2',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_3 = Button(
    root,
    text='3',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_4 = Button(
    root,
    text='4',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_5 = Button(
    root,
    text='5',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_6 = Button(
    root,
    text='6',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_7 = Button(
    root,
    text='7',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_8 = Button(
    root,
    text='8',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_9 = Button(
    root,
    text='9',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_0 = Button(
    root,
    text='0',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_00 = Button(
    root,
    text='00',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_dot = Button(
    root,
    text='.',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_add = Button(
    root,
    text='+',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_sub = Button(
    root,
    text='-',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_mul = Button(
    root,
    text='*',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_div = Button(
    root,
    text='÷',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_expo = Button(
    root,
    text='^',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_mod = Button(
    root,
    text='M',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_equal = Button(
    root,
    text='=',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_clear = Button(
    root,
    text='C',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

button_back = Button(
    root,
    text='⇦',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0, # boarder of the button
    activeforeground='#fdc703', # when pressed text color
    activebackground='black', # when pressed background color
    )

#placements

button_clear.grid(row=2, column=0, padx=5, pady=5)
button_mod.grid(row=2, column=1, padx=5, pady=5)
button_back.grid(row=2, column=2, padx=5, pady=5)
button_div.grid(row=2, column=3, padx=5, pady=5)
button_7.grid(row=3, column=0, padx=5, pady=5)
button_8.grid(row=3, column=1, padx=5, pady=5)
button_9.grid(row=3, column=2, padx=5, pady=5)
button_mul.grid(row=3, column=3, padx=5, pady=5)
button_4.grid(row=4, column=0, padx=5, pady=5)
button_5.grid(row=4, column=1, padx=5, pady=5)
button_6.grid(row=4, column=2, padx=5, pady=5)
button_sub.grid(row=4, column=3, padx=5, pady=5)
button_1.grid(row=5, column=0, padx=5, pady=5)
button_2.grid(row=5, column=1, padx=5, pady=5)
button_3.grid(row=5, column=2, padx=5, pady=5)
button_add.grid(row=5, column=3, padx=5, pady=5)
button_0.grid(row=6, column=0, padx=5, pady=5)
button_00.grid(row=6, column=1, padx=5, pady=5)
button_dot.grid(row=6, column=2, padx=5, pady=5)
button_equal.grid(row=6, column=3, padx=5, pady=5)



mainloop()