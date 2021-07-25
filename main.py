#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
import math

value = ''  # empty sting that holds the value to be displayed


# functions

def click(num):
    global value  # changed the variable to global for reading the data inside it

    if value == '0':
        value = ''
    value = value + str(num)  # adding the pressed buttons value to the variable
    eqn.set(value)  # setting the empty sting of eqn to value
    if not value.isdigit():  # if string doesnt contain digit then it runs
        try:  # tries the risky code
            total = str(eval(value))  # runs the python code (which is passed as an argument) within the program.
            eqn2.set(total)
        except:
            eqn2.set('..')


def typed(num):
    global value
    a = num.char
    if str(a) == '!':
        try:
            value = e2.get()
            fac()
        except:
            fac()
    else:

        click(a)


def calc():
    global value
    if e.get() == 'ERROR':
        value = ''
        eqn.set('')
    elif e2.get() == '..':
        eqn2.set('')
    elif value == '':
        value = str(e.get())

    try:  # tries the risky code
        if value == '':
            total = e2.get()
        else:
            total = str(eval(value))  # runs the python code (which is passed as an argument) within the program.
    except:
        total = 'ERROR'
        eqn.set(total)  # setting the value of eqn to total
        value = ''  # sets the values to total which is calculated answer
    else:
        eqn.set(total)  # setting the value of eqn to total
        eqn2.set('')  # displays answer in second entry
        value = total  # sets the values to total which is calculated answer
        if value == '0':  # if value is 0 it changes it to empty string because eval can't calculate (01-1)
            value = ''


def ent(event):
    calc()


def sq():
    global value
    if not e.get() == '':
        try:
            a = math.sqrt(int(value))
            eqn.set(a)
            value = str(a)
        except:
            a = 'ERROR'
            eqn.set(a)
            if eqn.get() == 'ERROR':
                eqn2.set('')
                value = ''
    else:
        pass


def fac():
    global value
    if not e.get() == '':
        try:
            a = math.factorial(int(value))
            eqn.set(a)
            value = str(a)
        except:
            a = 'ERROR'
            eqn.set(a)
            if eqn.get() == 'ERROR':
                eqn2.set('')
                value = ''
    else:
        pass


def sin():
    global value
    if not e.get() == '':
        try:
            if '+' or '-' or '*' or '/' or '**' or '//' or '%' in value:
                a_v = eval(value)
                a = math.sin(int(a_v))
                eqn.set(a)
                value = str(a)
                eqn2.set('')
            else:

                a = math.sin(int(value))
                eqn.set(a)
                value = str(a)
        except:
            a = 'ERROR'
            eqn.set(a)
            if eqn.get() == 'ERROR':
                eqn2.set('')
                value = ''
    else:
        pass


def cos():
    global value
    if not e.get() == '':
        try:
            if '+' or '-' or '*' or '/' or '**' or '//' or '%' in value:
                a_v = eval(value)
                a = math.cos(int(a_v))
                eqn.set(a)
                value = str(a)
                eqn2.set('')
            else:

                a = math.cos(int(value))
                eqn.set(a)
                value = str(a)
        except:
            a = 'ERROR'
            eqn.set(a)
            if eqn.get() == 'ERROR':
                eqn2.set('')
                value = ''
    else:
        pass


def tan():
    global value
    if not e.get() == '':
        try:
            if '+' or '-' or '*' or '/' or '**' or '//' or '%' in value:
                a_v = eval(value)
                a = math.tan(int(a_v))
                eqn.set(a)
                value = str(a)
                eqn2.set('')
            else:

                a = math.tan(int(value))
                eqn.set(a)
                value = str(a)
        except:
            a = 'ERROR'
            eqn.set(a)
            if eqn.get() == 'ERROR':
                eqn2.set('')
                value = ''
    else:
        pass


def log():
    global value
    if not e.get() == '':
        try:
            if '+' or '-' or '*' or '/' or '**' or '//' or '%' in value:
                a_v = eval(value)
                a = math.log(int(a_v))
                eqn.set(a)
                value = str(a)
                eqn2.set('')
            else:

                a = math.log(int(value))
                eqn.set(a)
                value = str(a)
        except:
            a = 'ERROR'
            eqn.set(a)
            if eqn.get() == 'ERROR':
                eqn2.set('')
                value = ''
    else:
        pass


def clear():
    global value
    if eqn.get() == 'ERROR':
        eqn2.set('')
    value = ''  # value is changed to empty string
    eqn.set('')  # eqn is changed to empty string
    eqn2.set('')  # eqn2 is changed to empty string


# Back function

def back():
    global value
    try:
        a = ''
        for i in range(len(value) - 1):
            a = a + value[i]
        eqn.set(a)
        value = a
    except:
        value = ''
        eqn.set(value)  # sets eqn to the value

    if not value.isdigit():  # if string doesnt contain digit then it runs
        try:  # tries the risky code
            total = str(eval(value))  # runs the python code (which is passed as an argument) within the program.
            if len(total) <= 4:  # if answer is more that 4 character long it doesnt displays it in answer section
                eqn2.set(total)
            else:
                eqn2.set('')
                pass
        except:
            eqn2.set('')


def typed_back(event):
    back()


root = Tk()
root.configure(background='black')  # changes the board background to black
root.title('Calculator')
root.iconbitmap('logo.ico')

frame3 = LabelFrame(root, padx=10, pady=10, bg='black', bd=0)
frame3.pack(side=TOP)


def frame2f():
    frame2 = LabelFrame(root, padx=10, pady=10, bg='black', bd=0)
    frame2.pack(side=TOP)
    global button_fr

    # Reverting the sign on the button

    def forget():
        frame2.pack_forget()
        global button_fr
        button_fr = Button(
            frame3,
            text='▲',
            font=('Digital-7', 30),
            bg='black',
            fg='#6adbd9',
            bd=0,
            activeforeground='#6adbd9',
            activebackground='black',
            command=frame2f,
        )
        button_fr.grid(row=1, column=1, padx=5, pady=5)

    # inside function button change

    button_fr = Button(
        frame3,
        text='▼',
        font=('Digital-7', 30),
        bg='black',
        fg='#6adbd9',
        bd=0,
        activeforeground='#6adbd9',
        activebackground='black',
        command=forget,
    )
    button_fr.grid(row=1, column=1, padx=5, pady=5)

    # Frame2 Buttons

    button_f1 = Button(
        frame2,
        text='Sin()',
        font=('Digital-7', 30),
        bg='black',
        fg='#6adbd9',
        bd=0,
        activeforeground='#6adbd9',
        activebackground='black',
        command=sin,
    )

    button_f2 = Button(
        frame2,
        text='Cos()',
        font=('Digital-7', 30),
        bg='black',
        fg='#6adbd9',
        bd=0,
        activeforeground='#6adbd9',
        activebackground='black',
        command=cos,
    )

    button_f3 = Button(
        frame2,
        text='Tan()',
        font=('Digital-7', 30),
        bg='black',
        fg='#6adbd9',
        bd=0,
        activeforeground='#6adbd9',
        activebackground='black',
        command=tan,
    )

    button_f4 = Button(
        frame2,
        text='Log()',
        font=('Digital-7', 30),
        bg='black',
        fg='#6adbd9',
        bd=0,
        activeforeground='#6adbd9',
        activebackground='black',
        command=log,
    )

    button_bl = Button(
        frame2,
        text='(',
        font=('Digital-7', 30),
        bg='black',
        fg='#6adbd9',
        bd=0,
        activeforeground='#6adbd9',
        activebackground='black',
        command=lambda: click('('),
    )

    button_br = Button(
        frame2,
        text=')',
        font=('Digital-7', 30),
        bg='black',
        fg='#6adbd9',
        bd=0,
        activeforeground='#6adbd9',
        activebackground='black',
        command=lambda: click(')'),
    )

    button_sq = Button(
        frame2,
        text='√',
        font=('Digital-7', 30),
        bg='black',
        fg='#6adbd9',
        bd=0,
        activeforeground='#6adbd9',
        activebackground='black',
        command=sq,
    )

    button_fac = Button(
        frame2,
        text='!',
        font=('Digital-7', 30),
        bg='black',
        fg='#6adbd9',
        bd=0,
        activeforeground='#6adbd9',
        activebackground='black',
        command=fac,
    )

    button_f1.grid(row=0, column=0, padx=5, pady=5)
    button_f2.grid(row=0, column=1, padx=5, pady=5)
    button_f3.grid(row=0, column=3, padx=5, pady=5)
    button_f4.grid(row=0, column=4, padx=5, pady=5)
    button_bl.grid(row=1, column=0, padx=5, pady=5)
    button_br.grid(row=1, column=1, padx=5, pady=5)
    button_sq.grid(row=1, column=3, padx=5, pady=5)
    button_fac.grid(row=1, column=4, padx=5, pady=5)


frame1 = LabelFrame(root, padx=10, pady=10, bg='black', bd=0)
frame1.pack(side=BOTTOM,)
root.bind('<Return>', ent)
root.bind('<BackSpace>', typed_back)
root.bind('<Key>', typed)

eqn = StringVar()  # holding a empty string
eqn2 = StringVar()  # holding a empty string

# entry(display) input portion

e = Entry(
    frame3,
    textvariable=eqn,
    width=15,
    borderwidth=0,
    font=('Digital-7', 50),
    fg='#6adbd9',
    bg='Black',
    justify='right',
)
e.grid(row=0, column=0, columns=4, ipadx=5, ipady=6)

# entry(display) output portion

e2 = Entry(
    frame3,
    textvariable=eqn2,
    width=10,
    justify='right',
    borderwidth=0,
    font=('Digital-7', 50),
    fg='gray',
    bg='Black',
)
e2.grid(row=1, column=3, columns=4, ipadx=5, ipady=3)

button_fr = Button(
    frame3,
    text='▲',
    font=('Digital-7', 30),
    bg='black',
    fg='#6adbd9',
    bd=0,
    activeforeground='#6adbd9',
    activebackground='black',
    command=frame2f,
)
button_fr.grid(row=1, column=1, padx=5, pady=5)

button_H = Button(
    frame3,
    text='H',
    font=('Digital-7', 30),
    bg='black',
    fg='#6adbd9',
    bd=0,
    activeforeground='#6adbd9',
    activebackground='black',
)
button_H.grid(row=1, column=2, padx=5, pady=5)

# Buttons

button_1 = Button(
    frame1,
    text='1',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='#fdc703',
    activebackground='black',
    command=lambda: click(1),
)

button_2 = Button(
    frame1,
    text='2',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='#fdc703',
    activebackground='black',
    command=lambda: click(2),
)

button_3 = Button(
    frame1,
    text='3',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='#fdc703',
    activebackground='black',
    command=lambda: click(3),
)

button_4 = Button(
    frame1,
    text='4',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='#fdc703',
    activebackground='black',
    command=lambda: click(4),
)

button_5 = Button(
    frame1,
    text='5',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='#fdc703',
    activebackground='black',
    command=lambda: click(5),
)

button_6 = Button(
    frame1,
    text='6',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='#fdc703',
    activebackground='black',
    command=lambda: click(6),
)

button_7 = Button(
    frame1,
    text='7',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='#fdc703',
    activebackground='black',
    command=lambda: click(7),
)

button_8 = Button(
    frame1,
    text='8',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='#fdc703',
    activebackground='black',
    command=lambda: click(8),
)

button_9 = Button(
    frame1,
    text='9',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='#fdc703',
    activebackground='black',
    command=lambda: click(9),
)

button_0 = Button(
    frame1,
    text='0',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='#fdc703',
    activebackground='black',
    command=lambda: click(0),
)

button_00 = Button(
    frame1,
    text='00',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='#fdc703',
    activebackground='black',
    command=lambda: click('00'),
)

button_dot = Button(
    frame1,
    text='.',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='#fdc703',
    activebackground='black',
    command=lambda: click('.'),
)

button_add = Button(
    frame1,
    text='+',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,
    activeforeground='#6adbd9',
    activebackground='black',
    command=lambda: click('+'),
)

button_sub = Button(
    frame1,
    text='-',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,
    activeforeground='#6adbd9',
    activebackground='black',
    command=lambda: click('-'),
)

button_mul = Button(
    frame1,
    text='*',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,
    activeforeground='#6adbd9',
    activebackground='black',
    command=lambda: click('*'),
)

button_div = Button(
    frame1,
    text='÷',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,
    activeforeground='#6adbd9',
    activebackground='black',
    command=lambda: click('/'),
)

button_mod = Button(
    frame1,
    text='M',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,
    activeforeground='#6adbd9',
    activebackground='black',
    command=lambda: click('%'),
)

button_equal = Button(
    frame1,
    text='=',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,
    activeforeground='#6adbd9',
    activebackground='black',
    command=calc,
)

button_clear = Button(
    frame1,
    text='C',
    font=('Digital-7', 50),
    bg='black',
    fg='red',
    bd=0,
    activeforeground='red',
    activebackground='black',
    command=clear,
)

button_back = Button(
    frame1,
    text='⇚',
    font=('Digital-7', 50),
    bg='black',
    fg='red',
    bd=0,
    activeforeground='red',
    activebackground='black',
    command=back,
)

# Placements of buttons

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

button_00.grid(row=6, column=0, padx=5, pady=5)
button_0.grid(row=6, column=1, padx=5, pady=5)
button_dot.grid(row=6, column=2, padx=5, pady=5)
button_equal.grid(row=6, column=3, padx=5, pady=5)

mainloop()
