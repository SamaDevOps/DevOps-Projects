import logo
import random

# print(logo.game_logo)
win_count = 0
celeb_dict = {"aaa" : 1, "bbb" : 2, "ccc" : 3, "ddd" : 4}
celeb_list = ["aaa", "bbb", "ccc", "ddd"]
random_index = random.randint(0, len(celeb_list) - 1)
print(random_index)
celeb_name = ""
celeb_value = 0
random_celeb1_name = ""
random_celeb1_value = 0
random_celeb2_name = ""
random_celeb2_value = 0
round_winner_name = ""
round_winner_value = 0

def random_celeb_name_selector(random_index):
    celeb_name = celeb_list.pop(random_index)
    return celeb_name

def random_celeb_value_selector(random_celeb1_name):
    celeb_value = celeb_dict.pop(random_celeb1_name)
    return celeb_value


print(celeb_dict)



def go_round():
    win_count = 0
    
    random_celeb1_name = random_celeb_name_selector(random_index)
    random_celeb1_value = random_celeb_value_selector(random_celeb1_name)
    print(f"A random celeb is {random_celeb1_name} value is {random_celeb1_value}")
    
    random_celeb2_name = random_celeb_name_selector(random_index)
    random_celeb2_value = random_celeb_value_selector(random_celeb2_name)
    print(f"B random celeb is {random_celeb2_name} value is {random_celeb2_value}")

    my_choice = input("Who has more followers? 'A' or 'B' : ")

    if my_choice == "A":
        if random_celeb1_value < random_celeb2_value:
            print(f"you are wrong your score is {win_count}")
        else:
            win_count += 1
            print(f"You are correct your score is {win_count}")
            round_winner_name = random_celeb1_name
            round_winner_value = random_celeb1_value
            new_random_val = random.randint(0, len(celeb_list) - 1)
            random_celeb2_name = random_celeb_name_selector(new_random_val)
            random_celeb2_value = random_celeb_value_selector(random_celeb2_name)
            go_round()
            
    else:
        if random_celeb2_value < random_celeb1_value:
            print(f"you are wrong your score is {win_count}")
        else:
            win_count += 1
            print(f"You are correct your score is {win_count}")
            round_winner_name = random_celeb2_name
            round_winner_value = random_celeb2_value
            new_random_val = random.randint(0, len(celeb_list) - 1)
            random_celeb2_name = random_celeb_name_selector(new_random_val)
            random_celeb2_value = random_celeb_value_selector(random_celeb2_name)
            go_round()
        
while not win_count < 0:
    go_round()