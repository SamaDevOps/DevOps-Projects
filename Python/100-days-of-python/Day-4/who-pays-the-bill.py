import random

print("Let's find out who pays the bill")

list_of_people = input("Please enter the names separated by comma : ").split(",")

print(list_of_people)

random_choice = random.randint(0,(len(list_of_people)-1))
print(random_choice)

print(f"Todays lucky winner is {list_of_people[random_choice]}")