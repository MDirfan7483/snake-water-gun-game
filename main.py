# 1 for snale
# -1 for snake
# 0 for gun
import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youdict = {"s":1,"w":-1,"g":0}
reverseDict = {1 : "snake", -1:"water", 0:"gun"}
you = youdict[youstr]
print(f" You chose {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")
if computer == you:
    print("Draw")
else:
    if computer == -1 and you == 1:
        print("You Win")
    elif computer == -1 and you == 0:
        print("You Lose")
    elif computer == 1 and you == -1:
        print("You Lose")
    elif computer == 1 and you == 0:
        print("You Win")
    elif computer == 0 and you == -1:
        print("You Win")
    elif computer == 0 and you == 1:
        print("You Lose")
    else:
        print("Something went wrong")
