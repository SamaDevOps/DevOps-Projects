height = float(input("enter your height in m : "))
weight = float(input("enter your weight in kg : "))

bmi = weight / (height * height)

if bmi < 18.5:
    print(f"your BMI is {bmi}, you are underweight")
elif bmi < 25:
    print(f"your BMI is {bmi}, you are normal weight")
elif bmi < 30:
    print(f"your BMI is {bmi}, you are  overweight")
elif bmi < 35:
    print(f"your BMI is {bmi}, you are  obese")
else:
    print(f"your BMI is {bmi}, you are  clinically obese")