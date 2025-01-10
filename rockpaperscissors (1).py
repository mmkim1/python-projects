#Matthew Kim
#Rock Paper Scissors

#Init
import random

drawnum = 0
winnum = 0
lossnum = 0

#Functions
def game():
    while True:
        global drawnum
        global winnum
        global lossnum

        playerchoice = input("Select rock, paper, or scissors: ").lower
        computerchoice = random.randint(1,3)
        if computerchoice == 1:
            computerchoice = "rock"
        elif computerchoice == 2:
            computerchoice = "paper"
        else:
            computerchoice = "scissors"

        if computerchoice == playerchoice:
            print("it's a draw")
            drawnum = drawnum + 1
        elif playerchoice == "paper" and computerchoice == "rock":
            print("computer chose rock, you win")
            winnum = winnum + 1
        elif playerchoice == "rock" and computerchoice == "scissors":
            print("computer chose scissors, you win")
            winnum = winnum + 1
        elif playerchoice == "scissors" and computerchoice == "paper":
            print("computer chose paper, you win")
            winnum = winnum + 1
        else:
            print("lose")
            lossnum = lossnum + 1

        playagain = input("Play again? yes or no:")
        if playagain == "yes":
            print(str(winnum) + "wins" + str(drawnum) + "draws" + str(lossnum) + "losses")
        else:
            print("thank you for playing")
            print(str(winnum) + "wins" + str(drawnum) + "draws" + str(lossnum) + "losses")
            break


#Main
print("Welcome to Rock Paper Scissors")
game()

