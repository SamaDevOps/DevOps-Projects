import random

print("Welcome to the Sama pyPassword Generator!")

password_length = int(input("How many letters would you like in your password? : "))

symbol_number = int(input("How many symbols would you like? : "))
numbers_number = int(input("How many numbers would you like? : "))

password_length_without_special = password_length - (symbol_number + numbers_number)

letters_choosed = random.sample(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],password_length_without_special)
numbers_choosed = random.sample(range(10),numbers_number)
symbols_choosed = random.sample(["!","@","#","$","%","&","(",")"],symbol_number)

list_1 = letters_choosed + numbers_choosed + symbols_choosed

for items in letters_choosed:
    print(letters_choosed[items])


# print(password_length_without_special)
# print(numbers_choosed)
# print(letters_choosed)
# print(symbols_choosed)
# print(list_1)
