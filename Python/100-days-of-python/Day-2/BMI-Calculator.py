height = input("input your height in meters: ")
weight = input("input your weight in kg: ")


bmi = float(weight) / float(height) ** 2
bmi_int = int(bmi)

print("Your BMI value is : " + str(bmi_int))
