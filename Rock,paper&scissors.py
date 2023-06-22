import random
computer_points = 0
player_points = 0
exit = False
while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("rock, paper, scissors or exit? : ").lower()
    computer_input = random.choice(options)

    if user_input == "exit":
        print("You have ended the game !")
        print("computer = " + str(computer_points))
        print("Player = " + str(player_points))
        if computer_points > player_points:
            print("Computer wins")

        elif player_points > computer_points:
            print("You win !")

        else:
            print("the game was a tie")

        exit = True

    elif user_input == "rock":
        if computer_input == "rock":
            print("You chose: " + user_input)
            print("Computer Chose : " + computer_input)
            print("it is a tie !")

        if computer_input == "paper":
            print("You chose: " + user_input)
            print("Computer Chose : " + computer_input)
            print("you lose !")
            computer_points += 1

        if computer_input == "scissors":
            print("You chose: " + user_input)
            print("Computer Chose : " + computer_input)
            print("you win !")
            player_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("You chose: " + user_input)
            print("Computer Chose : " + computer_input)
            print("you win !")
            player_points += 1

        if computer_input == "paper":
            print("You chose: " + user_input)
            print("Computer Chose : " + computer_input)
            print("its a tie !")

        if computer_input == "scissors":
            print("You chose: " + user_input)
            print("Computer Chose : " + computer_input)
            print("you lose !")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("You chose: " + user_input)
            print("Computer Chose : " + computer_input)
            print("computer win !")
            computer_points += 1

        if computer_input == "paper":
            print("You chose: " + user_input)
            print("Computer Chose : " + computer_input)
            print("you win !")
            player_points += 1

        if computer_input == "scissors":
            print("You chose: " + user_input)
            print("Computer Chose : " + computer_input)
            print("tie!")


