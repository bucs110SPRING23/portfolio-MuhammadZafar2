import random

computer_num=random.randrange(1,1000)
user_num=int(input("What number do you choose?: "))

guesses=0
while computer_num!= user_num:
    
    guesses+=1
    print("You are wrong try again")
    print(guesses)
    user_num=int(input("What number do you choose?: "))
        
print(f"computer number was {computer_num} and the number of guesses is {guesses +1}")
    




