my_value = 1


def check_scope():
    my_value = 2
    print(f"value within function is {my_value}")

check_scope()
print(f"value globally available is {my_value}")

