import math

def paint_calc(height,width):
    area = height * width
    cover = 5
    needed_cans = (area / cover)
    round_up_val = math.ceil(needed_cans)
    print(f"You need roughly {round_up_val} cans")
    
height_input = int(input("Please enter height of the wall : "))
width_input = int(input("PLease enter width of the wall : "))

paint_calc(height_input, width_input)