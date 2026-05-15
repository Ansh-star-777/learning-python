import random
import math

print(random.randint(0,10))
print(random.random())
print(random.choice("ansh"))
print(random.choice([1,3,5,6]))
# print(random.seed(4))
print(random.randint(0,10))

print("--------------------")

print(math.sqrt(2))
print(random.choice(["stone","paper","scissors"]))

print("--------------------")

while True:
    chosen = input("choose rock,paper,scissors shoot!!")
    computer_chosen = random.choice(["rock","paper","scissors"])
    print("Computer has chosen:",computer_chosen)
    if chosen == computer_chosen:
        print("it's a tie")
    elif chosen == "rock" and computer_chosen == "paper":
        print("The computer has won you human")
    elif chosen == "paper" and computer_chosen == "rock":
        print("you have won happy happy happy")
    elif chosen == "paper" and computer_chosen == "scissors":
        print("you have lost by the robotings")
    elif chosen == "scissors" and computer_chosen == "paper":
        print("human has won")
    elif chosen == "rock" and computer_chosen == "scissors":
        print("human has won again")
    else:
        print("else block")
