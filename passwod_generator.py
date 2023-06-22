import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("how long would you like the password to be?"))

    random.shuffle(characters)

    password = []
    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input("do u want to generate a password? (Yes/No) :").lower()

if option == "yes":
    generate_password()

elif option == "no":
    print("Programme ended")
    quit()

else:
    print("Please enter valid input (Yes/No) : ")
    quit()