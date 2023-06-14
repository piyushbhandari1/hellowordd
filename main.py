import functools
import time
import random
import os
import shutil


#first_name = "Bro"
#last_name = " code"
#full_name = first_name + last_name
#print("hello " + full_name)
#print(type(name))

#age = 21
#age = age + 1
#print("your age is " +str(age))
#print(type(age))

#height = 255.5
#print(height)
#print(type(height))
#print("your height is " + str(height) +"cms")

#human = false
#print("are you a human?" +str(human))
#print(type(human))


#name = "bro "
#age = 21
#attractive = True

#name, age, attractive = "bro ", 21, True
#print(name + str(age) + " " + str(attractive))


#anshu = 30
#ankur = 28
#miky = 25
#tharik = 20

#anshu, ankur, miky, tharik = 30, 28, 25, 20

#print(anshu, ankur, miky, tharik)


#name = "ankur"
#print(len(name))
#print(name.find("k"))
#print(name.capitalize())
#print(name.upper())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("u"))
#print(name.replace("n", "e"))
#print(name*3)


#x= 1
##z = "3"

#y = int(y)
#z = int(z)
#x = float(x)





#print(z*2)
#print(z)
#print(x)

#name = input("what is your name?")
#age = int(input("how old are you?"))
#height = float(input("how tall are you?"))


#age = age + 1

#print("welcome to the show " + name + " Hope u will anjoy")
#print("you are going to be " + str(age) + "years old")
#print("you are " + str(height) + " cms tall")





import math

#pi = 3.14

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(420))


#x = 1
#y = 2
#z = 3
#print(max(x,y,z))
#print(min(x,y,z))

#SLICINGGG

#name = "Piyush Bhandari"

#first_name = name[0:6]
#last_name = name[7:15]
#funky_name = name[0:15:2]
#reversed_name = name[::-1]
#print(first_name)
#print(last_name)
#print(reversed_name)


#website1 = "http://google.com"
#website2 = "http://wikipedia.com"
#slice = slice(7,-4)


#print(website1[slice])
#print(website2[slice])



#If elseif elif statements !!

#age = int(input("How old are you? "))

#if age == 100:
   # print("Happy cenctuary")

#elif age>+ 18:
 #   print("u an adult")



#elif age < 0:
 #   print("you r nt born yet")
#else:
 #   print("u a child")



#Logical operators and or not

#temp = int(input("what is the temperature outside? "))

#if not(temp >= 0 and temp <+ 30):
    #print("the temp is bad tday, stay inside")

#elif not (temp < 0 or temp > 30):

 #   print("the temp is good tday")
  #  print("go outside")

# while loop

# while 1 == 1:
 #   print("help im stuck in this loop")



#name = ""

#while len(name) == 0:
  #  name = input("Enter your name: ")

#print("Hello, " + name + "!")

# For Looooops

#for i in range (11):
  #  print(i)

#for i in range(50, 101):
  #  print(i)

#for i in "Piyush bhandari":
 #   print(i)

#for seconds in range(10,0,-1):
  #  print(seconds)
 #   time.sleep(1)
#print("happy new year !!!")


# Nested loops

#rows = int(input("how many rows? "))
#columns = int(input("how many columns? "))
#symbol = input("enter a symbol of your choice: ")

#for i in range(rows):
  #  for j in range(columns):
 #       print(symbol, end="")
 #   print()


  #loop control statemenets
  # Break Continue Pass

#while True:
   # name = input("enter your name: ")
    #if name != "":
       # break

#phone_number = "123-456-7890"
#for i in phone_number:
  #  if i == "-":
  #      continue
  #  print(i, end="")


#for i in range(1,21):
  #  if i == 13:
  #      pass
  #  else:
  #      print(i, end="")


  # lists

#food = ["pizza", "ham", "hotdog", "burger"]

#food[0] = "sushi"

#food.append("ice cream")
#food.remove("hotdog")
#food.pop()
#food.insert(0,"cake")
#food.sort()
#food.clear()
#for x in food:
   # print(x)


#### 2D LISTS
#drinks = ["coffee", "soda", "tea"]
#dinner = ["pizza", "hamburger", "hotdog"]
#dessert = ["cake", "ice cream"]

#food = [drinks, dinner, dessert]

#print(food[2][0])


#### tuples

#student = ("Bro", 21, "male")
#print(student.count("Bro"))
#print(student.index("male"))

#for x in student:
  #  print(x)

#if "Bro" in student:
 #   print("Bro is here")

 # Set !!!

#utensils = {"fork", "spoon", "knife"}
#dishes = {"bowl", "plate" "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()

#utensils.update(dishes)
#dinner_table = utensils.union(dishes)


#for x in dinner_table:
   # print(x)

#print(utensils.difference(dishes))



## DICTIONARY

#capitals = {"usa": "washington dc",
          #  "india" : "new delhi",
          #  "china" : "beijing",
          #  "russia" : "moscow"}

#capitals.update({"germany":"berlin"})
#capitals.update({"usa":"las vegas"})
#capitals.pop("china")
#capitals.clear()

#print(capitals["russia"])
#print(capitals.get("germany"))
#print(capitals.keys())
#print(capitals.values())

#for key, value in capitals.items():
   # print(key, value)

#index operator

#name = "piyush bhandari"

#if(name[0].islower()):
   # name = name.capitalize()

#firstname = name[0:3].upper()
#lastname = name[5:].upper()
#lastchar = name[-1]

#print(lastchar)


# Function !!!

#def hello(firstname, lastname, age):
   # print("hello " +firstname+ " " +lastname)
  #  print("you are " + str(age)+ " years old")



#hello("piyush", "bhandari ", 25)


#return statement

#def multiply(number1, number2):
   # result = number1 * number2
    #return result

#x = multiply(6,8)

#print(x)


#def add_numbers(a, b):
  #  result = a + b
  #  return result

#jama = add_numbers(2, 3)
#print(jama)


#Keyword arguments

#def hello(first, middle, last):
   # print("hello "+ first +" " + middle + " " + last)

#hello("Alok", "nath", "kaad")
#hello(last="Alok", first="nath", middle="kaad")


#nested function calls in python

#print(round(abs(float(input("Enter a whole positive number: ")))))

# Scope !

#name = "Bro"

#def display_name():
   # name = "Code"
  #  print(name)


# args parameter

#def add(*args):
  #  sum = 0

  #  args = list(args)
   # args[0] = 0

    #for i in args:
     #   sum += i
  #  return sum

# print(add(1,2,3,4))


# kwargs

#def hello(**kwargs):

    #print("hello" + kwargs['first'] + "  " + kwargs['last'])
#    print("Hello", end=" ")
 #   for key, value in kwargs.items():
  #      print(value,end= " ")
#
#hello(first="bro", middle="dude", last="code", title="thanks")


#str format

#animal = "cow"
#item = "moon"

#print("the " +animal +" jumped over the " + item)

#print(" The {} jumped over the {}".format("bull",item))
#print(" The {1} jumped over the {0}".format(animal,item)) #positional argument
#print(" The {item} jumped over the {animal}".format(animal="cow",item="moon")) #keyword


#text = " The {} jumped over the {}"
#print(text.format(animal,item))


#name = "Bro"

#print("hello, my name is {}".format("name"))
#print("hello, my name is {:10} .Nice to meet me" .format("name"))
#print("hello, my name is {:<10} .Nice to meet me" .format("name"))
#print("hello, my name is {:>10} .Nice to meet me" .format("name"))
#print("hello, my name is {:^10} .Nice to meet me" .format("name"))


#number = 3.14159

#print("the number pi is {:.3f}".format(number))
##print("the number pi is {:b}".format(number))
#print("the number pi is {:o}".format(number))
#print("the number pi is {:X}".format(number))
#print("the number pi is {:E}".format(number))



# Random Module (import random)

#x = random.randint(1,6)
#y = random.random()
#mylist = ["Rock", "Paper", "Scissorz"]
#z = random.choice(mylist)

#cards = [1,2,3,4,5,6,7,8,9,"k", "q", "a", "j"]
#random.shuffle(cards)

#print(cards)


# Exception handling

#try:
 #   numerator = int(input("Enter a number to divide: "))
 #   denominator = int(input("Enter a number to divide by: "))
  #  result = numerator / denominator

    #print(result)

#except ZeroDivisionError as e:
   # print(e)
    #print("you cant divide by zero sir")

#except ValueError as e:
   ## print(e)
   # print("enter only numbers pls")

#except Exception as e:
  #  print(e)
  #  print("something went wrong!")
#else:
  #  print(result)

#finally:
  #  print("this will always be executed at the end")


#file detection

#path = "C:\\Users\\PIYUSH\\Desktop\\folder"
#C:\Users\PIYUSH\Desktop

#if os.path.exists(path):
   # print("that location exists")
  #  if os.path.isfile(path):
  #      print("that is a file")
  #  elif os.path.isdir(path):
     #   print("that is a directory!")

#else:
   # print("that location dsnt exists")

   # Reading files in python
#try:

   # with open('test.txt') as file:
   #     print(file.read())
#except FileNotFoundError:
  #  print("that file was not found")


#text = "have a great day"

#with open('test.txt','a') as file:
   # file.write(text)

# copyfile() contents of file only
#copy() copyfile + permissions + destination can b a directory
#copy2() copy() + copies metadata

#shutil.copyfile('test.txt','copy.txt') #src, dst

# Move a file +

#source = "testt.txt"
#destination = "C:\\Users\\PIYUSH\\Desktop\\testt.txt"

#try:
    #if os.path.exists(destination):
   #     print("there is already a file there")
  #  else:
   #     os.replace(source,destination)
   #     print(source+ " was moved")

#except FileNotFoundError:
  #  print(source+ " was not found")

  # deleting files

#path = "test.txt"
#path = "empty_folder" #does not delete empty directories
#try:

  #os.remove(path) #delete a file
    #os.rmdir(path)  # delet an empty directory
   #shutil.rmtree(path) #delete a directory containing files


#except FileNotFoundError:
   # print("the file was nt found")
#except PermissionError:
 #   print("u dont have permission to delete empty folders")
#else:
    #print(path+ " was deleted")

    # MODULES a file containing python code


# rock paper scissors game !!!

# random
#while True:
#    choices = ["rock", "paper", "scissors"]
#
#    computer = random.choice(choices)
#    player = None
#
#
#    while player not in choices:
#        player = input("rock, paper or scissors ? ").lower()
#
#    if player == computer:
#        print("computer: ", computer)
#        print("player: ",player)
#        print("TIE!")

#    elif player == "rock" :
#        if computer == "paper":
#            print("computer: ", computer)
#            print("player: ", player)
#            print("You lose!")

#        if computer == "scissors":
#            print("computer: ", computer)
#            print("player: ", player)
#            print("You win!")


#    elif player == "scissors" :
#        if computer == "rock":
#            print("computer: ", computer)
#            print("player: ", player)
#            print("You lose!")

#        if computer == "paper":
#            print("computer: ", computer)
#            print("player: ", player)
#            print("You win!")

#    elif player == "paper" :
#        if computer == "scissors":
#            print("computer: ", computer)
#            print("player: ", player)
#            print("You lose!")

#        if computer == "rock":
#            print("computer: ", computer)
#            print("player: ", player)
#            print("You win!")

#    playagain = input("play again? (yes/no): ").lower()
#    if playagain != "yes":
#        break

#print("bye!!")


#######   Quiz Gamee  !!!

# -------------------------------------------- #
#def newgame():
#    guesses = []
#    correct_guesses = 0
#    question_num = 0

#    for key in questions:
#        print("-----------------------------------------")
#        print(key)
#        for i in options[question_num]:
#            print(i)
#        guess = input("Enter (A, B, C OR D) : ")
#        guess = guess.upper()
#        guesses.append(guess)

#        correct_guesses += checkanswer(questions.get(key),guess)
#        question_num += 1

#    displayscore(correct_guesses, guesses)
#
#
#
# -------------------------------------------- #

#def checkanswer(answer, guess):
#    if answer == guess:
#        print("correct!")
#        return 1
#    else:
#        print("wrong")
#        return 0
#
# -------------------------------------------- #


#def displayscore(correct_guesses, guesses):
#    print("-----------------------------")
#    print("results")
#    print("-----------------------------")
#    print("Answers: ", end=" ")
#    for i in questions:
#        print(questions.get(i), end=" ")
#    print()

#    print("Guesses: ", end=" ")
#    for i in guesses:
#        print(i, end=" ")
#    print()

#    score = int((correct_guesses/len(questions))*100)
#    print("Your score is: " + str(score) +" %")




# -------------------------------------------- #

#def playagain():
#    response = input("do u wanna play again? (yes or no): ")
#    response= response.upper()

#    if response == "YES":
#        return True
#    else:
#        return False

# -------------------------------------------- #

#questions = {
#    "which game in ps4 is a car game?  : ": "A",
#    "which is called the mother of all exercises? : ": "B",
#    "pepsiman was originally launched for wich gaming console? : ": "C",
#    "is the earth round? : ": "A"
#}

#options = [["A.Crew 2", "B. GTA V", "C. COD", "D. God of war"],
#           ["A. Bicep curls", "B. Squats", "C. Chest press", "D. Planks"],
#           ["A. PS3", "B. PS2", "C. PS1", "D. XBOX"],
#           ["A. TRUE", "B. FALSE", "C. SOMETIMES", "D. WHEN IT RAINS"]]


#newgame()

#while playagain():
#    newgame()

#print("Byeee")

# O O P

#from car import Car

#car_1 = Car("chevy", "corvette", 2021, "black")
#car2 = Car("ford", "mustang", 21, "blakk")



#Car.wheels = 2

#print(car_1.wheels)
#print(car2.wheels)


#class Animal:
#    alive = True

#    def eat(self):
#        print("This animal is eating")

#    def sleep(self):
#        print("This animal is sleeping")

###class Rabbit(Animal):
##    def run(self):
#        print("this rabbit is running")

#class Fish(Animal):
#    def swim(self):
#        print("this fish is swimming")

##class Hawk(Animal):
 #   def fly(self):
#        print("this hawk is flyin")

#rabbit = Rabbit()
#fish = Fish()
#hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.sleep()
#rabbit.run()
#fish.swim()
#hawk.fly()


####### Multilevel Inheritence

#class Organism:
#    alive = True

#class Animal(Organism):
#    def eat(self):
#        print("This animal is eating")

#class Dog(Animal):
#    def bark(self):
#        print("this dog is barking")

#dog = Dog()
#print(dog.alive)
#dog.eat()
#dog.bark()


# Multiple inheritence

#class Prey:
#    def flee(self):
#        print("this animal flees")

#class Predator:
#    def hunt(self):
#        print("this animal hunts")

#class Rabbit(Prey):
#    pass

#class Hawk(Predator):
#    pass

#class Fish(Prey,Predator):
#    pass

#rabbit = Rabbit()
#hawk = Hawk()
#fish = Fish()

#rabbit.flee()
#hawk.hunt()
#fish.hunt()


# Method over riding

#class Animal:
#    def eat(self):
#        print("This animal is eating")

#class Rabbit(Animal):
#    def eat(self):
#        print("This rabbit is eating a carrot")

#rabbit = Rabbit()
#rabbit.eat()


#class Car:
#    def turnon(self):
#        print("u start the engine")
#        return self

#    def drive(self):
 #       print("u drive")
 #       return self

#    def brake(self):
#        print("u brake")
 #       return self

 #   def turnoff(self):
#        print("u turn off the engine")
#        return self


#car = Car()
#car.turnon().brake().drive()



#  Super Function

#super().__init__(length, width)


# Abstract Class
#from abc import ABC, abstractmethod
#class Vehicle(ABC):
 #   @abstractmethod
 #   def go(self):
 #       pass

#class Car(Vehicle):
 #   def go(self):
 #       print("You drive the car")

##class Bike(Vehicle):
  #  def go(self):
   #     print("You ride the bike")
#
#ehicle = Vehicle()
#car = Car()
#bike = Bike()

#vehicle.go()
#bike.go()



#    Objects as arguments


#class Car:
  #  color = None

#class Motorcycle:
 #   color = None

#def change_color(car, color):
  #  car.color = color

#car1 = Car()
#car2 = Car()
#car3 = Car()
#bike = Motorcycle()

#change_color(car1,"red")
#change_color(car2,"black")
#change_color(car3,"pink")
#change_color(bike, "blaaack")

#print(car1.color)
#print(car2.color)
#print(car3.color)
#print(bike.color)


# Duck typing

#Walrus operator :=

# functions to Variables

#def hello():
 #   print("Hello")

#print(hello)
#hi = hello
#print(hi)

#say = print

#say("does it wrk?")

# Highter order functions

#def loud(text):
#    return text.upper()

#def quiet(text):
##def hello(func):
 #   text = func("Hello")
#    print(text)

#hello(loud)


# LAMBDA

#def double (x):
#    return x * 2

#print(double(5))

#double = lambda x:x * 2

#print(double(5))


#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#fruits = ["apple", "banana", "orange", "strawberry"]

#print(len(fruits))

#fruits[0] = "fineapple"
#fruits.append("fineapple")
#fruits.remove("apple")
#fruits.insert(0,"guava")
#fruits.sort()
#fruits.reverse()
#print(fruits.index("apple"))

#print(fruits)

# Sort method

#students = ["squidward", "Sandy", "Alice", "Bob"]


#students.sort(reverse=True)
#students.sort()

#sorted_students = sorted(students)

#for i in sorted_students:
 #   print(i)

#students = [("squidward", "F" , 60),
 #           ("Sandy", "A", 33),
 #           ("Alice", "A", 18),
 #           ("Bob", "C", 99)]


#grade = lambda grades:grades[1]
#students.sort(key=grade)

#for i in students:
 #   print(i)


 # maps

#store = [("shirt",20.00),
 #        ("pants",25.00),
 #        ("jackets",50.00),
  #       ("socks",10.00)]

#to_euros = lambda data: (data[0], data[1]*0.82)
#store_euros = list(map(to_euros, store))

#for i in store_euros:
  #  print(i)


  # Filter Function

#items =  [("shirt",20.00),
     #    ("pants",25.00),
     #    ("jackets",50.00),
      #   ("socks",10.00)]

#money = lambda data:data[1] >= 20.00

#expensiveshii = list(filter(money, items))
#for i in expensiveshii:
 #   print(i)

 # reduce function

import functools

#letters = ["H","E","L","L","O"]
#word = functools.reduce(lambda x, y, : x + y,letters)
#print(word)

#factorial = [5,4,3,2,1,]
#result = functools.reduce(lambda x,y,: x * y, factorial)
#print(result)

# list comprehension

# list = [expression for item in iterable]

#squares = []
#for i in range(1,11):
#    squares.append(i * i)
#print(squares)

#squares = [i * i for i in range(1,11)]
#print(squares)

# Dictionary comprehensions

#dictionary = {key: expressions for (key,value) in iterable}

#cities_in_F = {"new york":32, "Boston" : 75, "LA" : 100, "Chicago" : 50}

#cities_in_c = {key: round((value-32)*5/9)for (key,value) in cities_in_F.items()}
#print(cities_in_c)

# Zip Function

#username = ["Dude", "Bro", "Mister"]
#password = ["p@ssword", "abc123", "guest"]

#users = zip(username, password)

#for i in users:
  #  print(i)

 # if name = main

#1, module can be run as standalone program
#2, module can be imported and used by other modules

#if __name__ == '__main__':
 #   print("running this module directly")
#else:
 #   print("running this module INdirectly")

 # Time Module !!!!!!

import time

#print(time.ctime(0))

#print(time.time())

#print(time.ctime(time.time()))

#time_object = time.localtime()
#time_object = time.gmtime()
# print(time_object)
#local_time = time.strftime("%B %d %Y %H: %M: %S", time_object)
#print(local_time)

#time_string = "20 April, 2020"
#time_object = time.strptime(time_string,"%d %B, %Y")
#print(time_object)

#time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
#time_string = time.asctime(time_tuple)
#print(time_string )

# Multi Threading : flow of execution
# multi threads makes each thread do its own thing
#cpu bound use multiprocessing
#io bound multithreading

import threading
import time

#def eat():
 #   time.sleep(3)
 #   print("u eat")
#def drink():
   # time.sleep(4)
   # print("u sleep")
#def study():
 #   time.sleep(5)
  #  print("u studyyy")

#x = threading.Thread(target=eat, args=())
#x.start()

#y = threading.Thread(target=drink(), args=())
#y.start()

#z = threading.Thread(target=study(), args=())
#z.start()

#eat()
#drink()
#study()

#print((threading.active_count()))
#print(threading.enumerate())

#print(threading.active_count())
#print(threading.enumerate())

#def timer():
    #print()
    #print()
    #count = 0
    #while True:
     #   time.sleep(1)
      #  count += 1
       # print("logged in for ", count, "seconds")


#x = threading.Thread(target=timer, daemon=True)
#x.start()

#x.setDaemon(True)

#answer = input("u wana exit?")


#Multi Processing

#from multiprocessing import Process, cpu_count
#import time

#def counter(num):
  #  count = 0
 #   while count < num:
  ###      count += 1

#def main():

  #  a = Process(target=counter, args=(1000000000,))
  #  a.start()

 #   a.join()
 #   print("finished in ", time.perf_counter(), "seconds")

#if __name__ == '__main__':
  #  main()

#Practice

#even_numbers = [2,4,6,8,10]
#odd_numbers = [1,3,5,7,9,]

#merged_list = [x for pair in zip(odd_numbers, even_numbers) for x in pair]
#print(merged_list)

#name = "john bro how are you?"
#age = 23
#print(len(name))
#print("Hello " + name + " " + str(age))

#print(name.index("g"))
#print(name.count("g"))
#print(name[3:7])
#print(name[3:7:2])
#print(name[::-1])
#print(name.upper())
#print(name.lower())

#if name.startswith("oops"):
#    print("yes its is")

#else:
 #   print("wtf")


#astring = "Hello world!"
#afewwords = astring.split(" ")

#name = "John"
#age = 23
#if name == "John" and age == 23:
  #  print("Your name is John, and you are also 23 years old.")

#if name == "John" or name == "Rick":
 #   print("Your name is either John or Rick.")

#else:
 #   pass

#for x in range (2,11,):
 #   print(x)


#class NumberHolder:

 #   def __init__(self, number):
#     self.number = number

  # GUI

#from tkinter import *

#count = 0

#def click():
   # global count
  #  count+=1
 #   print(count)


#window = Tk()
#window.geometry("600x600")
#window.title("First GUI Program")

#icon = PhotoImage(file='halleyo.png')
#window.iconphoto(True,icon)
#window.config(background="grey")

#photo = PhotoImage(file='logoo.png')

#label = Label(window,
  #            text="Hello World!",
    #          font=('Arial',40,'bold'),
    #          fg='white',
    #          bg='black',
    #          relief=RAISED,
     #         bd=10,
      #        padx=20,
       #       pady=20,
       #       image=photo,
       #       compound='top')
#label.pack()

#button = Button(window,
          #      text="Click Here",
                #command= click,
           #     font=("Comic Sans",30),
            #    fg="white",
             #   bg="black",
              #  activebackground="white",
       #         activeforeground="black",
        #        state=ACTIVE,
         #       image=photo,
          #      compound='top')
#button.pack()

#label.place(x=0, y=0)
#window.mainloop()

# Labels !!


# Entry box
#from tkinter import *
#def submit():
    #username = entry.get()
    #print("hello")
#window = Tk()

#entry = Entry(window,
            #  font=("Arial",50))

#entry.pack(side=LEFT)

#submit_button = Button(window,text="Submit",command=submit)
#submit_button.pack(side=RIGHT)

#window.mainloop()



#Buttons

#from tkinter import *

#count = 0

#def click():
 #   global count
 #   count += 1
 #   print(count)

#window = Tk()

#photo = PhotoImage(file='hi.png')

#button = Button(window,
#                text="click me",
 #               command=click,
  #              font=("Comic Sans",30),
   #             fg="green",
    #            bg="black",
     #           activeforeground="green",
      #          activebackground="black",
       #         state=ACTIVE,
        #        #image=photo,
         #       compound='bottom')

#button.pack()
#window.mainloop()


# Entry Box

#from tkinter import *

#def submit():
 #   username = entry.get()
  #  print("hello " + username)
   # entry.config(state=DISABLED)
#def delete() :
#    entry.delete(0,END)

#def BackSpace() :
#    entry.delete(len(entry.get())-1, END)


#window = Tk()



##             font=("Arial", 50),
  #            fg="green",
   #           bg="black",
     #         show="*",
    #          )

#entry.insert(0,'Mr/Mrs: ')

#entry.pack(side=LEFT)
#submit = Button(window, text="Submit", command=submit)
#submit.pack(side=RIGHT)

#delete = Button(window, text="Delete", command=delete)
#delete.pack(side=RIGHT)

#BackSpace = Button(window, text="BackSpace", command=BackSpace)
#BackSpace.pack(side=RIGHT)

#window.mainloop()

#from tkinter import *

#def display () :
  #  if(x.get()==1):
    #    print("You agree!")
  #  else:
  #      print("You don't agree!")


#window = Tk()

#x = IntVar()

#check_button = Checkbutton(window,
#                           text="I agree ",
 #                          variable=x,
  #                         onvalue=1,
   #                        offvalue=0,
    #                       command=display,
     #                      font=('Arial', 20),
      #                     fg='green',
       #                    bg='black',
        #                   activeforeground='green',
         #                  activebackground='black',
          #                 padx=25,
           #                pady=25)
#

#check_button.pack()
#window.mainloop()#


#from tkinter import *

#food = ["pizza", "burger", "hotdog"]

#def order ():
 #   if(x.get()==0):
#       print("you ordered pizza")
 #   elif(x.get()==1):
    #    print("you ordered burgir")
  #  else:
      # print("You ordered hotdog")

#window = Tk()
#x = IntVar()
#for index in range(len(food)):
 #   radiobutton = Radiobutton(window, text=food[index],
  #                            variable=x,
   #                           value=index,
    #                          padx = 25, pady= 25,
     #                         font=("Impact", 40),
      #                        indicatoron=0,
       #                       width=15,
        #                      command=order
         #                     )
#
 #   radiobutton.pack(anchor=W)

#window.mainloop()

# Scale

#from tkinter import *
#def submit():
  #  print("The temp. is: "+ str(scale.get()) + " degrees C")
#window = Tk()

#scale = Scale(window,from_=100, to=0,
#              length=500,
 #             orient=VERTICAL,
  #           font=('consolas',20),
   #           tickinterval=10,
  #            showvalue=1,
   #           resolution= 5,
    #          troughcolor='blue',
     #         fg='red',
      #        bg='black'
       #       )
#scale.set(((scale['from']-scale['to'])/2)+scale['to'])
#scale.pack()

#button = Button(window,text='Submit',command=submit)
#button.pack()
#window.mainloop()


#  Listbox


#def submit () :

    #food = []
   # for index in listbox.curselection():
   #     food.insert(index, listbox.get(index))

   # print("You have ordered: ")
   # for index in food:
    #    print(index)
#print(listbox.get(listbox.curselection()))

#def add():
  #  listbox.insert(listbox.size(),entrybox.get())
  #  listbox.config(height=listbox.size())

#def delete():
 #   #listbox.delete(listbox.curselection())
   # for index in reversed(listbox.curselection()):
   #     listbox.delete(index)
   # listbox.config(height=listbox.size())


#from tkinter import *

#window = Tk()

#listbox = Listbox(window,
             #     bg="#f7ffde",
             #     font=("Constantia",35),
             #     #width=18,
             #     selectmode=MULTIPLE
           #       )
#listbox.pack()

#listbox.insert(1,"PIZZA")
#listbox.insert(2,"PASTA")
#listbox.insert(3,"GIRLY BREAD")
#listbox.insert(4,"SOUP")
#listbox.insert(5,"SALAD")

#listbox.config(height=listbox.size())

#entrybox = Entry(window)
#entrybox.pack()

#submitButton = Button(window,text="submit",command=submit)
#submitButton.pack()

#addbutton = Button(window, text="add", command=add)
#addbutton.pack()

#deletebutton = Button(window, text="delete", command=delete)
#deletebutton.pack()

#window.mainloop()

# Messagebox

from tkinter import *
from tkinter import messagebox

#def click():
   # messagebox.showinfo(title='info msg box', message=' u a good man')
  # messagebox.showwarning(title='Warning ! ', message=' u a good man')
  # messagebox.showerror(title='Warning ! ', message=' smthin is off')
  #if messagebox.askokcancel(title='ask ok / cancel ! ', message=' do u wanna do it?') :
    #print('u did a thing')
  #else:
  #    print('byeee')

    #if messagebox.askretrycancel(title='ask retry / cancel ! ', message=' do u wanna retry?'):
      #  print('u retried a thing')
    #else:
     #   print('u cancelled a thing')
    #if messagebox.askyesno(title='ask yes or no', message='do u like cake?') :
     #   print('i like cake too')
    #else:
     #   print('wth?')

    #answer = messagebox.askquestion(title='ask question', message='do u like pie?')
    #if(answer == 'yes'):
      #  print('i like pie too')
   # else:
    #    print('y dont ya like it ?')
   # answer = messagebox.askyesnocancel(title='yes no cancel',
                                      # message='do u like to code?',
                                      # icon='warning')
    #if (answer == True):
     #   print("u like to code")
    #elif(answer == False):
     #   print("wth are u doing here?")
    #else:
       # print("answer d question")

#window = Tk()

#button = Button(window,command=click, text='click me')
#button.pack()

#window.mainloop()

# Colorchooser

#from tkinter import *
#from tkinter import colorchooser

#def click():
 #   color = colorchooser.askcolor()
  #  #print(color)
   # colorhex = color[1]
    ##print(colorhex)
    #window.config(bg=colorhex)


#window = Tk()
#window.geometry("420x420")
#button = Button(text='click',
 #               command=click)

#button.pack()
#window.mainloop()

#   Text Area !!!


from tkinter import *

#def submit():
 #   input = text.get("1.0",END)
#    print(input)

#window = Tk()
#text = Text(window,bg="light yellow",
    #        font=("Ink Free",15),
     #       height=8,
     #       width=20,
      #      padx=20,
       #     pady=2,
        #    fg="purple")
#text.pack()
#button = Button(window,text="Submit",command=submit)
#button.pack()

#window.mainloop()

# Open a file

#from tkinter import*
#from tkinter import filedialog


#def openfile():
 #   filepath = filedialog.askopenfilename(initialdir="C:\\Users\\PIYUSH\\PycharmProjects\\hellowordd",
  #                                        title="Open File",
   #                                       filetypes= (("text files","*txt"),
    #                                      ("all files", "*.*")))
    #file = open(filepath,'r')
    #print(file.read())
    #file.close()

#window = Tk()
#button = Button(text="Open",command=openfile)
#button.pack()
#window.mainloop()

# Saving a file

from tkinter import *
from tkinter import filedialog

#def savefile():
  #  file = filedialog.asksaveasfile(initialdir="C:\\Users\\PIYUSH\\Desktop",defaultextension='.txt',
 #                                   filetypes=[
  #                                      ("text file",".txt"),
   #                                     ("html file", ".html"),
    #                                    ("all files", ".*")
     #                               ])


    #if file is None:
     #   return
    #filetext = str(text.get(1.0,END))
#    filetext = input("Enter some text ig")
 #   file.write(file.text)
  #  file.close()

#windows = Tk()
#button = Button(text='save',command=savefile)
#button.pack()
#text = Text(windows)
#text.pack()

#windows.mainloop()




#from tkinter import *

#def openfile():
 #   print("you opened a file")

#def savefile():
 #   print("you saved a file")

#def cutfile():
 #   print("you cut a file")

#def copyfile():
 #   print("you copied a file")

#def pastefile():
 #   print("you pasted a file")


#window = Tk()
#openimage = PhotoImage(file='file.png')
#saveimage = PhotoImage(file='save.png')
#exitimage = PhotoImage(file='exit.png')

#menubar = Menu(window)
#window.config(menu=menubar)

#filemenu= Menu(menubar,tearoff=0,font=("MV Boli",15))
#menubar.add_cascade(label="File", menu=filemenu)
#filemenu.add_command(label="open",command=openfile,compound='left')#image=openimage,)
#filemenu.add_command(label="save",command=savefile,  compound='left')
#filemenu.add_separator()
#filemenu.add_command(label="exit",command=quit,compound='left')


#editmenu= Menu(menubar,tearoff=0,font=("MV Boli",15))
#menubar.add_cascade(label="Edit", menu=editmenu)
#editmenu.add_command(label="cut",command=cutfile,)
#editmenu.add_command(label="copy",command=copyfile,)
#editmenu.add_command(label="paste",command=pastefile,)

#window.mainloop()


#  Frames

#from tkinter import *

#window = Tk()
#frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
#frame.place(x=0,y=0)
#frame.pack()
#button = Button(window,text="W", font=("Consolas", 25),width=3)
#button.pack()
#Button(frame,text="W", font=("Consolas", 25),width=3).pack(side=TOP)
#Button(frame,text="A", font=("Consolas", 25),width=3).pack(side=LEFT)
#Button(frame,text="S", font=("Consolas", 25),width=3).pack(side=LEFT)
#Button(frame,text="D", font=("Consolas", 25),width=3).pack(side=LEFT)




#def createwindow ():
   # newwindow = Tk()   #Toplevel()
    #oldwindow.destroy()
#oldwindow = Tk()
#Button(oldwindow,text="create new window",command=createwindow).pack()

#oldwindow.mainloop()

#tabs in pythonnn

#from tkinter import *
#from tkinter import ttk

#window = Tk()

#notebook = ttk.Notebook(window)
#tab1 = Frame(notebook)
#tab2 = Frame(notebook)
#notebook.add(tab1,text="tab 1")
#notebook.add(tab2,text="tab 2")
#notebook.pack(expand=True,fill="both")

#Label(tab1,text="namaste from T1",width=50,height=25).pack()
#Label(tab2,text="hola from T2",width=40,height=35).pack()

#window.mainloop()


#  GRID  !!!

#from tkinter import *
#window = Tk()

#title = Label(window,text="Enter your info: ",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

#firstnamelabel = Label(window,text="First name: ",width=20,bg="pink").grid(row=1,column=0)
#firstnameentry = Entry(window).grid(row=1,column=1)

#lastnamelabel = Label(window,text="Last name: ",width=20,bg="pink").grid(row=2,column=0)
#lastnameentry = Entry(window).grid(row=2,column=1)

#emaillabel = Label(window,text="Email: ",width=20,bg="pink").grid(row=3,column=0)
#emailentry = Entry(window).grid(row=3,column=1)

#submit = Button(window, text="Submit").grid(row=4,column=0,columnspan=2)



#window.mainloop()

# Progress bar

#from tkinter import *
#from tkinter.ttk import *
#import time

#def start ():
#    gb = 65
#    download = 0
#    speed = 1
#    while(download<gb):
 #       time.sleep(0.05)
 #       bar['value']+=(speed/gb)*100
##        download+=speed
 #       percent.set(str(int((download/gb)*100))+" %")
 #       text.set(str(download)+"/"+str(gb)+" gb completed")
 #       window.update_idletasks()


#window = Tk()

#percent = StringVar()
#text = StringVar()
#bar = Progressbar(window,orient=HORIZONTAL,length=300)
#bar.pack(pady=10)



#percentlabel = Label(window,textvariable=percent).pack()
#tasklabel = Label(window,textvariable=text).pack()

#button = Button(window, text="download",command=start).pack()

#from tkinter import *
#window = Tk()

#canvas = Canvas(window,height=500,width=500)
#canvas.create_line(0,0,500,500,fill="pink",width=8)
#canvas.create_line(0,500,500,0,fill="blue",width=8)
#canvas.create_rectangle(50,50,250,250,fill="purple")
#points = [250,0,500,500,0,500]
#canvas.create_polygon(points,fill="grey",outline="black",width=5)
#canvas.create_arc(0,0,500,500,fill="pink",style=PIESLICE,start=270,extent=180)
#canvas.create_arc(0,0,500,500,fill='red',extent=180,width=6)
#canvas.create_arc(0,0,500,500,fill='white',extent=180,start=180,width=6)
#canvas.create_oval(190,190,310,310,fill="white",width=8)
#canvas.pack()

#window.mainloop()

print("this is a test")