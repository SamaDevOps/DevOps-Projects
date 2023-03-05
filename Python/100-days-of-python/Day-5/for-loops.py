import random

fruits = ["Apple" , "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    
#testing
english_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for charactor in english_alphabet:
    i = random.randint(0,len(english_alphabet)-1)
    print(english_alphabet[i])
    
