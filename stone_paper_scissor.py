import random

win = 0
lose = 0
draw = 0

youdict = {1:"stone",2:"paper",3:"scissor"}

print("Welcome to 'Stone, Paper, Scissor' Game")

for round in range(1,11):

    computer = random.choice([1,2,3])
    print(f"\nRound no = {round}")

    try:
        you = int(input("Enter your choice (1=stone,2=paper,3=scissor): "))
    except:
        print("Invalid input!")
        continue

    if you not in [1,2,3]:
        print("Please enter a valid number")
        continue

    print(f"You chose {youdict[you]}")
    print(f"Computer chose {youdict[computer]}")

    if you == computer:
        print("Draw")
        draw += 1
    elif (you == 1 and computer == 3) or (you == 2 and computer == 1) or (you == 3 and computer == 2):
        print("You Win!")
        win += 1
    else:
        print("You Lose!")
        lose += 1

print("\nFinal Score")
print("Wins:", win)
print("Losses:", lose)
print("Draws:", draw)
