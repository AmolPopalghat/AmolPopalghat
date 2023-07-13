# Project No 2 : Number Guesses Game.

import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while userGuess != randNumber:
    userGuess = int(input("Enter Your Guess:"))
    guesses += 1
    if userGuess == randNumber:
        print("Your guess is right!")

    else:
        if userGuess > randNumber:
            print("Your Guess is Wrong, Enter a smaller Number!")
        else:
            print("Your Guess is Wrong, Enter a larger Number!")

print(f"You guessed the number in {guesses} guesses")
with open("Project_No_2_hiscore.txt")as f:
    Project_No_2_hiscore = int(f.read())

if guesses < Project_No_2_hiscore:
    print("You have broken the high score!")
    with open("Project_No_2_hiscore.txt", "w")as f:
        f.write(str(guesses))


