age = input("What is your age now : ")

age_left_in_years = 90 - int(age)

age_in_days = age_left_in_years * 365
age_in_weeks = age_left_in_years * 52
age_in_months = age_left_in_years * 12

print(f"You have {age_in_days} days, {age_in_weeks} weeks, and {age_in_months} months left")