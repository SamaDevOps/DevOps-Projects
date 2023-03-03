import random

coin_flip = random.randrange(0,2,1)

print(coin_flip)

user_choice = int(input("Please enter 1 for heads 0 for tails : "))

if user_choice == 0 and coin_flip == 0:
    print("you fliped tails lap fliped tails, its a draw")
elif user_choice == 0 and coin_flip == 1:
    print("you fliped tails lap fliped heads, you loose")

if user_choice == 1 and coin_flip == 1:
    print("you fliped heads lap fliped heads, its a draw")
elif user_choice == 1 and coin_flip == 0:
    print("you fliped heads lap fliped tails, you win")