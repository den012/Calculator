import random
run=True

print("Do you want to roll the dice? Y/N")
while run:
    choice=input()
    if choice=='Y' or choice=='y':
        print("Dice number:",random.randrange(1,6))
        print("Do you want to roll again? Y/N")
    elif choice=='N' or choice=='n':
        print("Ok see you next time!")
        exit()
    else:
        print("Wrong input check again")