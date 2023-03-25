import random

random_number = random.randint(1,100)
print(random_number)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

def guess_game(chance):
    game_end= False
    while not game_end:
        if chance >= 1:
            guess = int(input("Make a guess : "))
            if guess == random_number:
                print("YOu GueSsed RiGht YoU WoN!!")
                game_end = True
            elif guess > random_number:
                print("Value is too high")
                chance -= 1
                if chance == 0:
                    game_end = True
                    print("You failed")
                else:
                    print(f"You have {chance} chances left")
            elif guess < random_number:
                print("Value is too low")
                chance -= 1
                if chance == 0:
                    game_end = True
                    print("You failed")
                else:
                    print(f"You have {chance} chances left")
        else:
            game_end = True
            print("You failed")


if difficulty == "easy":
    print("You have 10 chances left")
    guess_game(10)
elif difficulty == "hard":
    print("You have 5 chances left")
    guess_game(5)
    

