print("Welcome to the tip calculator")
bill = input("What was the total bill? ")
percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
split = input("How many people to split the bill? ")

bill_float = float(bill)
percentage_float = float(percentage)
split_float = float(split)


total_cost = bill_float + ((bill_float * percentage_float)/100)
cost_of_one = total_cost / split_float
final_count = round(cost_of_one, 2)

print(f"Each person should pay: ${final_count}")


