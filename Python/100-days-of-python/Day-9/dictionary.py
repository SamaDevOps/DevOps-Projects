# new dictionary

car_properties_dictionary = {
    "color" : "grey",
    "make" : "toyota",
    "model" : "vitz"
}


print(car_properties_dictionary["make"])

# adding new items to dictionary
car_properties_dictionary["year"] = "2015"

print(car_properties_dictionary)

# Create empty dictionary
emp_dictionary = {}

print(emp_dictionary)

# Edit an item in a dictionary

car_properties_dictionary["year"] = "2023"

print(car_properties_dictionary)

# Loop through a dictionary
for thing in car_properties_dictionary:
    print(car_properties_dictionary[thing])