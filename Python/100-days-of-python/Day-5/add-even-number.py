total_even = 0
total_even2 = 0

for number in range(1,101):
    if number % 2 == 0:
        total_even += number

print(total_even)

for number in range(2,101,2):
    total_even2 += number
print(total_even2) 