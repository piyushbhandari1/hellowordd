from tkinter import *
window = Tk()

def buttonpress(num):
    global equationtext

    equationtext = equationtext + str(num)
    equationlabel.set(equationtext)

def equals():

    global equationtext
    try:
        total = str(eval(equationtext))

        equationlabel.set(total)

        equationtext = total

    except ZeroDivisionError:
        equationlabel.set("Can't divide by zero")
        equationtext = ""

    except SyntaxError:
        equationlabel.set("Syntax Error !")
        equationtext = ""


def clear():
    global equationtext
    equationlabel.set("")
    equationtext = ""

window.title("Calculator")
window.geometry("500x500")

equationtext = ""

equationlabel = StringVar()

label = Label(window,textvariable=equationlabel, font=('Arial'),bg='white',width=24,height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,text=1,height=4,width=9,font=35,
                 command=lambda : buttonpress(1))
button1.grid(row=0,column=0)

button2 = Button(frame,text=2,height=4,width=9,font=35,
                 command=lambda : buttonpress(2))
button2.grid(row=0,column=1)

button3 = Button(frame,text=3,height=4,width=9,font=35,
                 command=lambda : buttonpress(3))
button3.grid(row=0,column=2)

button4 = Button(frame,text=4,height=4,width=9,font=35,
                 command=lambda : buttonpress(4))
button4.grid(row=1,column=0)

button5 = Button(frame,text=5,height=4,width=9,font=35,
                 command=lambda : buttonpress(5))
button5.grid(row=1,column=1)

button6 = Button(frame,text=6,height=4,width=9,font=35,
                 command=lambda : buttonpress(6))
button6.grid(row=1,column=2)

button7 = Button(frame,text=7,height=4,width=9,font=35,
                 command=lambda : buttonpress(7))
button7.grid(row=2,column=0)

button8 = Button(frame,text=8,height=4,width=9,font=35,
                 command=lambda : buttonpress(8))
button8.grid(row=2,column=1)

button9 = Button(frame,text=9,height=4,width=9,font=35,
                 command=lambda : buttonpress(9))
button9.grid(row=2,column=2)

button0 = Button(frame,text=0,height=4,width=9,font=35,
                 command=lambda : buttonpress(0))
button0.grid(row=3,column=0)

plus = Button(frame,text='+',height=4,width=9,font=35,
                 command=lambda : buttonpress('+'))
plus.grid(row=0,column=3)

minus = Button(frame,text='-',height=4,width=9,font=35,
                 command=lambda : buttonpress('-'))
minus.grid(row=1,column=3)

multiply = Button(frame,text='*',height=4,width=9,font=35,
                 command=lambda : buttonpress('*'))
multiply.grid(row=2,column=3)

divide = Button(frame,text='/',height=4,width=9,font=35,
                 command=lambda : buttonpress('/'))
divide.grid(row=3,column=3)

equal = Button(frame,text='=',height=4,width=9,font=35,
                 command=equals)
equal.grid(row=3,column=2)

decimal = Button(frame,text=".",height=4,width=9,font=35,
                 command=lambda : buttonpress("."))
decimal.grid(row=3,column=1)

clear = Button(frame,text="Clear",height=4,width=14,font=35,
                 command=clear)
clear.grid(row=4,column=1,columnspan=2)

window.mainloop()

