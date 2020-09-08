# to keep track of how won, how much
import random

player_win = 0
computer_win = 0
winning_score = 3

while computer_win < winning_score and\
      player_win < winning_score:
    print(f"Player score: {player_win} Computer score: {computer_win}")
    print("Rock...paper...Scissors...")
    rand_no = random.randint(0, 2)
    if rand_no == 0:
        computer = "rock"
    elif rand_no == 1:
        computer = "paper"
    else:
        computer = "scissors"

    player = input("Make your move: ")
    print(f"Computer player: {computer}")

    if player != "rock" and player != "paper" and player != "scissors":
        print("Please select rock scissors or paper!")
    else:
        if player == computer:
            print("draw! same choice")

        elif player == "rock":
            if computer == "scissors":
                print("player wins")
                player_win += 1
            else:
                print("computer wins")
                computer_win += 1
        elif player == "paper":
            if computer == "scissors":
                print("computer wins")
                computer_win += 1
            else:
                print("player wins")
                player_win += 1
        elif player == "scissors":
            if computer == "rock":
                print("computer wins")
                computer_win += 1
            else:
                print("player wins")
                player_win += 1


if player_win == computer_win:
    print("Its a TIE")
elif player_win > computer_win:
    print("Congratulations! You Won!")
else:
    print("Oh no :( Computer won!")
