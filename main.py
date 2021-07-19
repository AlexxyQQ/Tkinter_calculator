from tkinter import *
import math

value = ''  # empty sting that holds the value to be displayed


# functions
def click(num):
    global value  # changed the variable to global for reading the data inside it
    value = value + str(num)  # adding the pressed buttons value to the variable
    eqn.set(value)  # setting the empty sting of eqn to value

    ''' Calculates total right after pressing any operator buttons '''
    if not value.isdigit():  # if string doesnt contain digit then it runs
        try:  # tries the risky code
            total = str(eval(value))  # runs the python code (which is passed as an argument) within the program.
            if len(total) <= 4:  # if answer is more that 4 character long it doesnt displays it in answer section
                eqn2.set(total)
            else:
                eqn2.set('')
                pass
        except:  # if error is found runs expect
            eqn2.set('')


def calc():
    global value
    """ if user inputs values from keyboard it gets value directly from entry  """
    if e.get() == 'ERROR':
        value = ''
        eqn.set('')
    elif value == '':
        value = str(e.get())

    try:  # tries the risky code
        '''If the user input is given from keyboard it calculates the value'''
        if value == '':
            total = e2.get()
        else:
            total = str(eval(value))  # runs the python code (which is passed as an argument) within the program.

    except:  # if error is found runs expect
        total = 'ERROR'
        eqn.set(total)  # setting the value of eqn to total
        value = ''  # sets the values to total which is calculated answer
    else:  # if error is not found runs else
        eqn.set(total)  # setting the value of eqn to total
        eqn2.set('')  # displays answer in second entry
        value = total  # sets the values to total which is calculated answer
        if value == '0':  # if value is 0 it changes it to empty string because eval can't calculate (01-1)
            value = ''


def sq():
    global value
    if not (e.get() == ''):
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
    if not (e.get() == ''):
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
        '''Proper backspace function that removes only last character of a string'''
        a = ""
        for i in range(len(value) - 1):
            a = a + (value[i])
        eqn.set(a)
        value = a
    except:
        value = ''
        eqn.set(value)  # sets eqn to the value

    ''' Does the calculations even after clicking backspace'''
    if not value.isdigit():  # if string doesnt contain digit then it runs
        try:  # tries the risky code
            total = str(eval(value))  # runs the python code (which is passed as an argument) within the program.
            if len(total) <= 4:  # if answer is more that 4 character long it doesnt displays it in answer section
                eqn2.set(total)
            else:
                eqn2.set('')
                pass
        except:  # if error is found runs expect
            eqn2.set('')


root = Tk()
root.configure(background='black')  # changes the board background to black
root.title('Calculator')
root.iconbitmap('logo.ico')

eqn = StringVar()  # holding a empty string
eqn2 = StringVar()  # holding a empty string

# entry(display) input portion
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
    columns=4,
    ipadx=5,
    ipady=6
)
# entry(display) output portion
e2 = Entry(
    root,
    textvariable=eqn2,  # inputs value in the entry
    width=4,
    justify='right',
    borderwidth=0,
    font=('Digital-7', 50),
    fg='#6adbd9',
    bg='Black',
)
e2.grid(
    row=0,
    column=4,
    ipady=6
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

button_bl = Button(
    root,
    text='(',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,  # boarder of the button
    activeforeground='#6adbd9',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click('(')
)

button_br = Button(
    root,
    text=')',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,  # boarder of the button
    activeforeground='#6adbd9',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=lambda: click(')')
)

button_sq = Button(
    root,
    text='√',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,  # boarder of the button
    activeforeground='#6adbd9',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=sq
)

button_fac = Button(
    root,
    text='!',
    font=('Digital-7', 50),
    bg='black',
    fg='#6adbd9',
    bd=0,  # boarder of the button
    activeforeground='#6adbd9',  # when pressed text color
    activebackground='black',  # when pressed background color
    command=fac
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
button_bl.grid(row=2, column=4, padx=5, pady=5)
button_7.grid(row=3, column=0, padx=5, pady=5)
button_8.grid(row=3, column=1, padx=5, pady=5)
button_9.grid(row=3, column=2, padx=5, pady=5)
button_mul.grid(row=3, column=3, padx=5, pady=5)
button_br.grid(row=3, column=4, padx=5, pady=5)
button_4.grid(row=4, column=0, padx=5, pady=5)
button_5.grid(row=4, column=1, padx=5, pady=5)
button_6.grid(row=4, column=2, padx=5, pady=5)
button_sub.grid(row=4, column=3, padx=5, pady=5)
button_sq.grid(row=4, column=4, padx=5, pady=5)
button_1.grid(row=5, column=0, padx=5, pady=5)
button_2.grid(row=5, column=1, padx=5, pady=5)
button_3.grid(row=5, column=2, padx=5, pady=5)
button_add.grid(row=5, column=3, padx=5, pady=5)
button_fac.grid(row=5, column=4, padx=5, pady=5)
button_00.grid(row=6, column=0, padx=5, pady=5)
button_0.grid(row=6, column=1, padx=5, pady=5)
button_dot.grid(row=6, column=2, padx=5, pady=5)
button_equal.grid(row=6, column=3, padx=5, pady=5)

mainloop()
