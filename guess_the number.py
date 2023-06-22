import random

def number_guessing_game():
    print("Welcome to the number guessing game !")
    print("I am thinking of a number between 1 and 100")

    secret = random.randint(1, 100)
    guesses = 0
    guessed = False

    while not guessed:
        guess = int(input("Enter your guess : "))
        guesses += 1

        if guess == secret:
            print("you guessed it")
            print(f"it took you {guesses} attempts.")
            guessed = True

        elif guess < secret:
            print("too low")

        elif guess > secret:
            print("too high")

        else:
            print("something went wrong")

number_guessing_game()





