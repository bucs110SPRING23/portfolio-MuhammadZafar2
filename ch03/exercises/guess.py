import random
num=random.randrange(1,11)


for x in range(3):
    user=int(input("What is the number you think of?: "))
    if user>num:
        print("You are high")
    elif user<num:
        print("You are low")
    else:
        print("You won")
        break
