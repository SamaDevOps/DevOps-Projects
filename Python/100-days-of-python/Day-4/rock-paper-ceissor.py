import random

print("Welcome to R P C")

lap_number = random.randrange(0,3,1)
print(lap_number)
my_number = int(input("Please enter number 0 for rock, 1 for paper and 2 for ceissor : "))

rock = 0
paper = 1
ceissor = 2


if my_number == 0 and  lap_number == 0:
    print("Your drew rock lap drew rock\nThis is a draw")
elif my_number == 0 and lap_number == 1:
    print("Your drew rock lap drew paper\nYou Loose!!!")
elif my_number == 0 and lap_number == 2:
    print("Your drew rock lap drew ceissor\nYou Won!!!")
    
if my_number == 1 and lap_number == 1:
    print("Your drew paper lap drew paper this is a draw")
elif my_number == 1 and lap_number == 0:
    print("Your drew paper lap drew rock\nYou Won!!!")
elif my_number == 1 and lap_number == 2:
    print("Your drew paper lap drew ceissor\nYou Loose!!!")
    
if my_number == 2 and lap_number == 2:
    print("Your drew ceissor lap drew ceissor this is a draw")
elif my_number == 2 and lap_number == 0:
    print("Your drew ceissor lap drew rock\nYou Loose!!!")
elif my_number == 2 and lap_number == 1:
    print("Your drew ceissor lap drew paper\nYou Won!!!")   
    