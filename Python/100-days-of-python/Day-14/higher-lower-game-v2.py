import logo
import celebs
import random

win_count = 0
celeb_dict = celebs.celeb
celeb_list = list(celeb_dict.keys())
round_winner = []
round_winner_val = 0
random_celeb_name_1 = ""
random_celeb_name_2 = ""
random_celeb_val_1 = 0
random_celeb_val_2 = 0
game_end = False

def pick_random_celeb_name():
    if (len(celeb_list) - 1) >= 0:
        random_celeb_index = random.randint(0, len(celeb_list) - 1)
    else:
        print("game over")
    print(random_celeb_index)
    random_celeb_name = celeb_list.pop(random_celeb_index)
    return random_celeb_name

def pick_random_celeb_val(random_celeb_name):
    random_celeb_val = celeb_dict.pop(random_celeb_name)
    return random_celeb_val

def random1_gen():
    random_celeb_name_1 = pick_random_celeb_name()
    random_celeb_val_1 = pick_random_celeb_val(random_celeb_name_1)
    # print(f"Random celeb 1 is {random_celeb_name_1} and value is {random_celeb_val_1}")
    return random_celeb_name_1, random_celeb_val_1
    
celeb1 = random1_gen()
print(celeb1)

def random2_gen():
    random_celeb_name_2 = pick_random_celeb_name()
    random_celeb_val_2 = pick_random_celeb_val(random_celeb_name_2)
    # print(f"Random celeb 2 is {random_celeb_name_2} and value is {random_celeb_val_2}")
    return random_celeb_name_2, random_celeb_val_2

celeb2 = random2_gen()
print(celeb2)

while not game_end:

    player_guess = input("What is your guess 'A' or 'B' : ")

    if win_count == 0:
        print(f"yoooooooooo {win_count}")
        if player_guess == "A":
            if celeb1[1] > celeb2[1]:
                win_count += 1
                print(f"You won score is {win_count}")
                round_winner.clear()
                round_winner.append(celeb1[0])
                round_winner.append(celeb1[1])
                if (len(celeb_list) - 1) >= 0:
                    print(f"round winner is {round_winner}")
                    celeb2 = random2_gen()
                    print(f"next is {celeb2}")
                else:
                    print("Game Over")
                    game_end = True
            else:
                print(f"You loose score is {win_count}")
                game_end = True
        else:
            if celeb2[1] > celeb1[1]:
                win_count += 1
                print(f"You won score is {win_count}")
                round_winner.clear()
                round_winner.append(celeb2[0])
                round_winner.append(celeb2[1])
                if (len(celeb_list) - 1) >= 0:
                    print(f"round winner is {round_winner}")
                    celeb2= random2_gen()
                    print(f"next is {celeb2}")
                else:
                    print("Game Over")
                    game_end = True
            else:
                print(f"You loose score is {win_count}")
                game_end = True
    else:
        print("im in the else part")
        if player_guess == "A":
            if round_winner[1] > celeb2[1]:
                win_count += 1
                print(f"You won score is {win_count}")
                if (len(celeb_list) - 1) >= 0:
                    print(f"round winner is {round_winner}")
                    celeb2 = random2_gen()
                    print(f"next is {celeb2}")
                else:
                    print("Game Over")
                    game_end = True
            else:
                print(f"You loose score is {win_count}")
                game_end = True
        else:
            if celeb2[1] > round_winner[1]:
                win_count += 1
                print(f"You won score is {win_count}")
                round_winner.clear()
                round_winner.append(celeb2[0])
                round_winner.append(celeb2[1])
                if (len(celeb_list) - 1) >= 0:
                    print(f"round winner is {round_winner}")
                    celeb2 = random2_gen()
                    print(f"next is {celeb2}")
                else:
                    print("Game Over")
                    game_end = True
            else:
                print(f"You loose score is {win_count}")
                game_end = True