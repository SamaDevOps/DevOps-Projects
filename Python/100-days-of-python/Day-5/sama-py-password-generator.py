import random

# Code I did
# print("Welcome to the Sama pyPassword Generator!")

# english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# special_char_set = ["!","@","#","$","%","&","(",")"]
# number_set = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# how_many_letters = int(input("How many letters would you like in your password? : "))
# how_many_symbol = int(input("How many symbols would you like? : "))
# how_many_numbers = int(input("How many numbers would you like? : "))

# english_letters = how_many_letters - (how_many_symbol + how_many_numbers)

# generated_password = []
# for i in range(1,english_letters+1):
    
#     random_letter_index = random.randint(0,len(english_alphabet)-1)
#     generated_password.append(english_alphabet[random_letter_index])

# for i in range(1,how_many_symbol+1):
#     random_letter_index = random.randint(0,len(special_char_set)-1)
#     generated_password.append(special_char_set[random_letter_index])
    
# for i in range(1,how_many_numbers+1):
#     random_letter_index = random.randint(0,len(number_set)-1)
#     generated_password.append(number_set[random_letter_index])

# final_password = []
# for length in range(0,len(generated_password)):
#     random_index_to_pop = random.randint(0,len(generated_password)-1)
#     final_password.append(generated_password.pop(random_index_to_pop))
   
# output = ""
# for i in range(0,len(final_password)):
#     output += final_password[i]
# print(output)


# A Better way

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ["!","@","#","$","%","&","(",")"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

how_many_letters = int(input("How many letters would you like in your password? : "))
how_many_symbol = int(input("How many symbols would you like? : "))
how_many_numbers = int(input("How many numbers would you like? : "))

password_list = []
password = ""

for i in range(1,how_many_letters + 1):
    password_list.append(random.choice(letters))

for i in range(1,how_many_symbol + 1):
    password_list.append(random.choice(symbols))
    
for i in range(1,how_many_numbers + 1):
    password_list.append(random.choice(numbers))
    
random.shuffle(password_list)

for char in password_list:
    password += char
    
print(f"Your new password is {password}")