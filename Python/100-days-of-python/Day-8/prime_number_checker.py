def prime_check(number):
    prime_count = 0
    for i in range(1,number+1):
        # print(i)
        if number % i == 0:
            prime_count += 1
            # print(f"prime count {prime_count}")
    if prime_count <= 2:
        print("It's a prime number")
    else:
        print("It's not a prime number")
        
prime_input = int(input("Please enter a number to check : "))

prime_check(number=prime_input)