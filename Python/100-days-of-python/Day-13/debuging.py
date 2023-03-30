# def my_function():
#     for i in range(1, 21):
#         print(i)
#         if i == 20:
#             print("You got it")
# my_function()


# from random import randint
# imgs = ["😀", "😡", "👻", "✌", "🐸", "🍔"]
# img_num = randint(0, 5)
# print(imgs[img_num])

year = int(input("What's your year of birth? :"))
if year > 1980 and year <= 1994:
    print("You are a millenial")
elif year > 1994:
    print("You are a Gen Z")
