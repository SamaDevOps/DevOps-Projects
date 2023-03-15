import os

print("Hey there Welcome to Sama Auction!")
bidder_data = {}
anymore = "yes"
highest_bid = 0
highest_bidder = ""

while anymore == "yes":
    name = input("Please enter your name : ")
    bid = int(input("Please enter your best bid : "))
    
    bidder_data[name] = bid
    
    anymore = input("Do you want to continue yes/no : ")
    os.system('clear')

for bidder in bidder_data:
    if highest_bid == 0:
        highest_bid = bidder_data[bidder]
        highest_bidder = bidder
    elif highest_bid <= bidder_data[bidder]:
        highest_bid = bidder_data[bidder]
        highest_bidder = bidder

print(f"Winner is {highest_bidder} with ${highest_bid}")


