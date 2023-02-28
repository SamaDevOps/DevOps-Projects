print("Welcome to the Love calculator")

name1 = (input("Enter your name : ")).lower()
name2 = (input("Enter their name : ")).lower()

two_names = name1 + name2

t_count = int(two_names.count("t"))
r_count = int(two_names.count("r"))
u_count = int(two_names.count("u"))
e_count = int(two_names.count("e"))

first_digit = t_count + r_count + u_count + e_count

l_count = int(two_names.count("l"))
o_count = int(two_names.count("o"))
v_count = int(two_names.count("v"))
e_count = int(two_names.count("e"))

second_digit = l_count + o_count + v_count + e_count
love_number = str(first_digit) + str(second_digit)

if love_number < "10" or love_number > "90":
    print(f"Your score is {love_number}, you go together like coke and mentos.")
elif love_number < "50" and love_number > "40":
    print(f"Your score is {love_number}, you are alright together.")
else:
    print(f"Your score is {love_number}")