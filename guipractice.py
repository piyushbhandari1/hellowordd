from tkinter import *
"""
food = ["pizza","burger","hotdog"]

def order():
    if x.get()==0:
        print("you ardered pizza")
    elif x.get()==1:
        print("you ordered a burger")
    else:
        print("you ordered a hotdog")

windowz = Tk()
windowz.geometry("500x500")

x = IntVar()
for index in range(len(food)):
    radio = Radiobutton(windowz,text=food[index],
                        variable=x,value=index,
                        padx=25,
                        font=("Arial",50,'bold'),
                        indicatoron=0,width=375,
                        command=order)

    radio.pack(anchor=W)



windowz.mainloop()




count = 0
def click():
    global count
    count += 1
    print("stop pressing the button ! ")
    print(count)

def submit():
    username = entry.get()
    print("hello " + username)
    entry.config(state=DISABLED)
def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END),

def display():
    if(x.get()==1):
        print("you agree")
    else:
        print("u dont agree")




window = Tk()
x = IntVar()

#window.geometry("500x500")
window.title("Let's code")
pic = PhotoImage(file="halleyo.png")
window.iconphoto(True,pic)
window.config(background="silver")

#pict = PhotoImage(file="hi.png")

label = Label(window,text="Coder",
              font=("Arial",40,'bold'),
              bg='silver',
              fg = 'white',
              relief=RAISED,
              bd=10,
              #image=pict
              )

label.pack()

entry = Entry(window,
              font=("Arial",25))
entry.pack(side=LEFT)


button = Button(window,text="order",
                command=click,font=("Comic Sans",15,'bold'),
                width=10, height=2,
                background='grey',
                activeforeground='green',
                activebackground='black')
button.pack()

submit = Button(window,text="Submit",
                command=submit,font=("Comic Sans",15,'bold'),
                width=10, height=2,
                background='grey',
                activeforeground='green',
                activebackground='black')
submit.pack()

delete = Button(window, text= "Delete",command=delete,font=("Comic Sans",15,'bold'),
                width=10, height=2,
                background='grey',
                activeforeground='green',
                activebackground='black')
delete.pack()

abcpic = PhotoImage(file='halleyo.png')

backspace = Button(window, text= "Backspace",command=backspace,font=("Comic Sans",15,'bold'),
                width=10, height=2,
                background='grey',
                activeforeground='green',
                activebackground='black')
backspace.pack()


check = Checkbutton(window,text= "I Agree",
                    variable=x,
                    onvalue=1,
                    offvalue=0,
                    command=display,
                    font=('arial',20),fg='grey',bg='black',
                    activebackground='black',
                    activeforeground='white',padx=25,pady=10,)
                    #image=abcpic,
                    #compound='left')

check.pack(side=BOTTOM)

window.mainloop()



from tkinter import *
def submit():
    print('you have ordered : ')
    print(listbox.get(listbox.curselection()))

window= Tk()

listbox = Listbox(window,bg="#f7ffde",
                  font=("Constantia",35),
                  width=12,
                  )

listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"girlybread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())
submitButton = Button(window,text="Submit",command=submit)
submitButton.pack()
window.mainloop()

import tkinter as tk
from datetime import datetime

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create the listbox to display tasks
listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)

# Create a scrollbar for the listbox
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the listbox and scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create the entry widget to add new tasks
entry = tk.Entry(window, font=("Helvetica", 14))
entry.pack(pady=10)

# Create the buttons
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Create a label for displaying the date and time
date_label = tk.Label(window, font=("Helvetica", 12), anchor=tk.W)
date_label.pack()

# Function to update the date and time label
def update_datetime():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_label.config(text="Date and Time: " + current_datetime)
    window.after(1000, update_datetime)  # Update every 1 second (1000 milliseconds)

# Start updating the date and time label
update_datetime()

# Start the main event loop
window.mainloop()


def openFile():
    print("file has been opened")

def saveFile():
    print("saved !")

def cut():
    print("Cuttt")

def copy():
    print("Copyyy")

def paste():
    print("pasteee")


window = Tk()
menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='open',command=openFile)
filemenu.add_command(label='save',command=saveFile)
filemenu.add_separator()
filemenu.add_command(label='exit',command=quit)

editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='cut',command=cut)
editmenu.add_command(label='copy',command=copy)
editmenu.add_command(label='paste',command=paste)

window.mainloop()



window = Tk()

frame = Frame(window)

Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

frame.pack(side=BOTTOM)

window.mainloop()

def createwindow():
    new_window = Tk()
    new_window.geometry("300x300 ")
window = Tk()
window.geometry("500x500")
Button(window,text="create new window",command=createwindow).pack()


from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
xyz = Frame(notebook)
notebook.add(tab1,text='Tab 1')
notebook.add(tab2,text='Tab 2')
notebook.add(xyz,text='XYZ')
notebook.pack(expand=True,fill="both")

Label(tab1,text="Hello, this is the first tab",width=50,height=25).pack()
Label(tab2,text="Hello, this is the second tab",width=50,height=25).pack()
Label(xyz,text="Hello, this is the XYZ tab",width=50,height=25).pack()
window.mainloop(0)
window.mainloop()

window = Tk()

FirstNameLabel = Label(window,text="First Name : ").grid(row=0,column=0)
FirstNameEntry = Entry(window).grid(row=0,column=1)
window.mainloop()



window = Tk()
window.geometry("500x500")
firstnamelabel = Label(window,text="First Name : ").grid(row=0,column=0)
firstnameentry = Entry(window).grid(row=0,column=1)

lastnamelabel = Label(window,text="Last Name : ").grid(row=1,column=0)
lastnameentry = Entry(window).grid(row=1,column=1)

emaillabel = Label(window,text="Email : ").grid(row=2,column=0)
emailentry = Entry(window).grid(row=2,column=1)


from tkinter.ttk import *
import time
def start():
    task = 10
    x = 0
    while (x < task):
        time.sleep(1)
        bar['value']+=10
        x+=1
        percent.set(str(int((x/task)*100))+"%")
        text.set(str(x)+"/"+str(task)+" tasks completed")
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentlabel = Label(window,textvariable=percent).pack()
tasklabel = Label(window,textvariable=text).pack()

button = Button(window, text='Download',command=start).pack()



window.mainloop()


import time

WIDTH = 750
HEIGHT = 750

xvelocity = 2.5
yvelocity = 1.5



window = Tk()

canvas = Canvas(window,height=HEIGHT,width=WIDTH)
canvas.pack()

pic = PhotoImage(file='ufo.png')
myimage = canvas.create_image(0,0,image=pic,anchor=NW)

imagewidth = pic.width()
imageheight = pic.height()


while True:
    coordinates = canvas.coords(myimage)
    print(coordinates)
    if(coordinates[0]>=WIDTH-imagewidth or coordinates[0] < 0):
        xvelocity = -xvelocity
    if (coordinates[1] >= HEIGHT - imageheight or coordinates[1] < 0):
        yvelocity = -yvelocity

    canvas.move(myimage,xvelocity,yvelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()


import time
from ballz import *
window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volleyball = ballz(canvas,0,0,70,1,1.5,"white")
tennisball = ballz(canvas,0,0,20,1.5,2.5,"green")
basketball = ballz(canvas,0,0,75,2.5,1.5,"orange")

while True:
    volleyball.move()
    tennisball.move()
    basketball.move()

    window.update()
    time.sleep(0.009)

window.mainloop()


from time import *

def update():
    timestring = strftime("%I:%M:%S %p")
    timelabel.config(text=timestring)

    daystring = strftime("%A")
    daylabel.config(text=daystring)

    datestring = strftime("%d%B,%Y")
    datelabel.config(text=datestring)

    window.after(1000,update)

window = Tk()

timelabel = Label(window,font=('Arial',50),fg='green',bg='black')
timelabel.pack()

daylabel = Label(window,font=('Ink Free',30),fg='green',bg='black')
daylabel.pack()

datelabel = Label(window,font=('Ink Free',30),fg='green',bg='black')
datelabel.pack()

update()

window.mainloop()

"""

