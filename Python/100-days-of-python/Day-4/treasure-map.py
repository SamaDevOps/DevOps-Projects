row1 = ["⛰️", "⛰️", "⛰️"]
row2 = ["⛰️", "⛰️", "⛰️"]
row3 = ["⛰️", "⛰️", "⛰️"]

land_list = [row1, row2, row3]

print(f"{land_list[0]}\n{land_list[1]}\n{land_list[2]}")

treasure_location = input("Where do you want to hide the treasure? : ").split(",")

column = int(treasure_location[0])
row = int(treasure_location[1])

land_list[column-1][row-1] = "💎"


print(f"{land_list[0]}\n{land_list[1]}\n{land_list[2]}")