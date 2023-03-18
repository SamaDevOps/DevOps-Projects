import random

print("Welcome to Black Jack 21")

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_card1 = deck[random.randrange(0,12)]
computer_card2 = 0
computer_card_total = computer_card1
player_card1 = deck[random.randrange(0,12)]
player_card2 = deck[random.randrange(0,12)]
player_card3 = 0
player_card_total = player_card1 + player_card2

want_to_play = True 

def who_won(player, computer):
    if player > 21:
        print(f"your cards : [{player_card1},{player_card2},{player_card3}] , current score : [{player}]")
        print(f"computers first card [{computer}]")
        print("You lose")
    elif player <= 21 and computer < 17:
        computer_card2 = deck[random.randrange(0,12)]
        computer += computer_card2
        if computer > player:
            print(f"your cards : [{player_card1},{player_card2},{player_card3}] , current score : [{player}]")
            print(f"computers cards : [{computer_card1},{computer_card2}] , current score : [{computer}]")
            print("You lose")
        else:
            print(f"your cards : [{player_card1},{player_card2},{player_card3}] , current score : [{player}]")
            print(f"computers cards : [{computer_card1},{computer_card2}] , current score : [{computer}]")
            print("You win")

# while want_to_play:
print(f"your cards : [{player_card1},{player_card2}] , current score : [{player_card_total}]")
print(f"computers first card : [{computer_card1}]")
if player_card_total == 21:
    print("you win")
elif player_card_total > 21:
    who_won(player=player_card_total, computer=computer_card_total)
else:
    third_card = input("Type 'y' to get another card type 'n' to pass : ")
    if third_card == "y":
        player_card3 = deck[random.randrange(0,12)]
        player_card_total += player_card3
    who_won(player=player_card_total, computer=computer_card_total)