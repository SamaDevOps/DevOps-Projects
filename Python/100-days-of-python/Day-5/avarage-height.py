student_height = [180, 124, 165, 173, 189, 169, 146]
total_height = 0

for height in student_height:
    total_height += height

# roundup_val = round(total_height/len(student_height))
# print(f"Avarage height is {roundup_val}")

number_of_students = 0
for student in student_height:
    number_of_students += 1

roundup_value = round(total_height/number_of_students)
print(f"Avarage height is {roundup_value}")