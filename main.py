from tkinter import *

value = ''  # empty sting that holds the value to be displayed


# functions
def click(num):
    global value  # changed the variable to global for reading the data inside it
    value = value + str(num)  # adding the pressed buttons value to the variable
    eqn.set(value)  # setting the empty sting of eqn to value


def calc():
    global value
    try:  # tries the risky code
        total = str(eval(value))  # runs the python code (which is passed as an argument) within the program.
    except:  # if error is found runs expect
        total = 'ERROR'
        eqn.set(total)  # setting the value of eqn to total
        value = ''  # sets the values to total which is calculated answer
    else:  # if error is not found runs else
        eqn.set(total)  # setting the value of eqn to total
        value = total  # sets the values to total which is calculated answer


def clear():
    global value
    value = ''  # value is changed to empty string
    eqn.set('')  # eqn is changed to empty string


# Back function
def back():
    global value
    try:
        a = value[-1]
        if a in value:
            value = value.replace(a, '', 1)  # replaces character of a in the character of value only once
            eqn.set(value)
    except:
        value=''
        eqn.set(value)  # sets eqn to the value


root = Tk()
root.configure(background='black')  # changes the board background to black
root.iconbitmap('logo.ico')  # icon of the calculator
root.title('Calculator')

eqn = StringVar()  # holding a empty string

# entry(display) portion
e = Entry(
    root,
    textvariable=eqn,  # inputs value in the entry
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

# Buttons

button_1 = Button(
    root,
    text='1',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,  # boarder of the button
    activeforeground='#fdc703',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click(1)
)

button_2 = Button(
    root,
    text='2',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,  # boarder of the button
    activeforeground='#fdc703',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click(2)
)

button_3 = Button(
    root,
    text='3',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,  # boarder of the button
    activeforeground='#fdc703',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click(3)
)

button_4 = Button(
    root,
    text='4',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,  # boarder of the button
    activeforeground='#fdc703',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click(4)
)

button_5 = Button(
    root,
    text='5',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,  # boarder of the button
    activeforeground='#fdc703',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click(5)
)

button_6 = Button(
    root,
    text='6',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,  # boarder of the button
    activeforeground='#fdc703',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click(6)
)

button_7 = Button(
    root,
    text='7',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,  # boarder of the button
    activeforeground='#fdc703',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click(7)
)

button_8 = Button(
    root,
    text='8',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,  # boarder of the button
    activeforeground='#fdc703',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click(8)
)

button_9 = Button(
    root,
    text='9',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,  # boarder of the button
    activeforeground='#fdc703',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click(9)
)

button_0 = Button(
    root,
    text='0',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,  # boarder of the button
    activeforeground='#fdc703',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click(0)
)

button_00 = Button(
    root,
    text='00',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,  # boarder of the button
    activeforeground='#fdc703',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click('00')
)

button_dot = Button(
    root,
    text='.',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,  # boarder of the button
    activeforeground='#fdc703',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click('.')
)

button_add = Button(
    root,
    text='+',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,  # boarder of the button
    activeforeground='#6adbd9',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click('+')
)

button_sub = Button(
    root,
    text='-',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,  # boarder of the button
    activeforeground='#6adbd9',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click('-')
)

button_mul = Button(
    root,
    text='*',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,  # boarder of the button
    activeforeground='#6adbd9',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click('*')
)

button_div = Button(
    root,
    text='÷',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,  # boarder of the button
    activeforeground='#6adbd9',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click("/")
)

button_mod = Button(
    root,
    text='M',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,  # boarder of the button
    activeforeground='#6adbd9',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click('%')
)

button_equal = Button(
    root,
    text='=',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,  # boarder of the button
    activeforeground='#6adbd9',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=calc
)

button_clear = Button(
    root,
    text='C',
    font=('Digital-7', 50),
    bg='black',
    fg='red',
    bd=0,  # boarder of the button
    activeforeground='red',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=clear
)

button_back = Button(
    root,
    text='⇚',
    font=('Digital-7', 50),
    bg='black',
    fg='red',
    bd=0,  # boarder of the button
    activeforeground='red',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=back
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
button_0.grid(row=6, column=0, padx=5, pady=5)
button_00.grid(row=6, column=1, padx=5, pady=5)
button_dot.grid(row=6, column=2, padx=5, pady=5)
button_equal.grid(row=6, column=3, padx=5, pady=5)

mainloop()
