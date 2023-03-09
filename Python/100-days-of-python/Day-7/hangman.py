import random

hangman = (
    
"""
   ________
    |/   |     
    |   (_) -- (Helpppp)  
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    """,
    
"""
   ________
    |/   |     
    |   (_) -- (Well Shit!)  
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    """,

"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    """,
    
    """
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    """,

"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    """,

"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    """,
    
"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    """,)

word_list = ["applepie", "pizza", "newzealand", "science","nawoda","paper"]

random_word = word_list[random.randint(0,len(word_list)-1)]
choosen_word = random_word

choosen_word_list_form = []
empty_line = []
length_of_word = 0
life_count = 5
wrong_answer = False




while length_of_word < (len(choosen_word)):
    empty_line += "_"
    length_of_word += 1

for letter in choosen_word:
    choosen_word_list_form += letter
    

# print(empty_line)
# print(choosen_word_list_form)

print("Save this poor guy!")
print(hangman[0])

while choosen_word_list_form != empty_line:
    if life_count > 0:
        letter_count = 0
        letter_input = input("Please enter letter you guess : ")
        if choosen_word.find(letter_input) >= 0: 
            for letter in choosen_word:
                if letter == letter_input:
                    empty_line[letter_count] = letter
                    print(empty_line)
                    if choosen_word_list_form == empty_line:
                        print("Game Over you win")
                elif empty_line[letter_count] != letter:
                    if empty_line[letter_count] == "_":
                        empty_line[letter_count] = "_"                                
                letter_count += 1    
        else:
            life_count -= 1   
            print(hangman[life_count+1])
    elif life_count == 0:
        print("Game Over")
        print(f"Hidden word was {choosen_word}")
        break