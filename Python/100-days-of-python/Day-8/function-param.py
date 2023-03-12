# def greet(name):
#     print(f"Hey {name}")
#     print("How are you?")
    
# name_input = input("Please enter you name : ")

# greet(name_input)





# Functions with more positional arguments

def greet_with(name,name2,time):
    print(f"Hey {name} {name2}, {time}")
    
greet_with("Samadhi","Mabadawila","Good morning")



# Functions with keyword arguments

def greet_with_kyword(nam,nam2,time2):
    print(f"Hey {nam} {nam2} {time2}")
    
greet_with_kyword(time2 = "Good night", nam2 = "maba", nam = "sama")