# Project No 1 : Rock, Paper, scissor Game.

import random


def gamewin(Comp, You):
    if Comp == You:
        return None
    elif Comp == 'S':
        if You == 'P':
            return False
        elif You == 'R':
            return True
    elif Comp == 'R':
        if You == 'S':
            return False
        elif You == 'P':
            return True
    elif Comp == 'P':
        if You == 'R':
            return False
        elif You == 'S':
            return True


comp = ()
print("Comp Turn : Rock(R), Paper(P), Scissor(S)")
randomNu = random.randint(1, 3)
if randomNu == 1:
    comp = 'S'
elif randomNu == 2:
    comp = 'R'
elif randomNu == 3:
    comp = 'P'

you = input("Your Turn :Rock(R), Paper(P), Scissor(S)")
a = gamewin(comp, you)

print(f"Computer Chose: {comp}")
print(f"Your Chose: {you}")


if a is None:
    print("The game is tie!")
elif a is True:
    print("You win!")
else:
    print("You Lose!")

