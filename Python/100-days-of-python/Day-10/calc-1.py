from art import logo

answer = 0
conti = "y"
continued = False

def plus_op(first_number,second_number):
    answer = first_number + second_number
    return answer

def minus_op(first_number,second_number):
    answer = first_number - second_number
    return answer

def multi_op(first_number,second_number):
    answer = first_number * second_number
    return answer

def division_op(first_number,second_number):
    answer = first_number / second_number
    return answer
print(logo)
first_number = int(input("What's the first number? : "))

while conti == "y":
    operation = input("+\n-\n*\n/\nPick and operation : ")
    second_number = int(input("What's the next number? : "))
    if operation == "+":
        if continued:
            answer = plus_op(first_number=answer,second_number=second_number)
        else:
            answer = plus_op(first_number=first_number,second_number=second_number)
    elif operation == "-":
        if continued:
            answer = minus_op(first_number=answer,second_number=second_number)
        else:
            answer = minus_op(first_number=first_number,second_number=second_number)
    elif operation == "*":
        if continued:
            answer = multi_op(first_number=answer,second_number=second_number)
        else:
            answer = multi_op(first_number=first_number,second_number=second_number)
    elif operation == "/":
        if continued:
            answer = division_op(first_number=answer,second_number=second_number)
        else:
            answer = division_op(first_number=first_number,second_number=second_number)
        
    conti = input("Do you want to continue y/n : ")
    
    if conti == "y":
        continued = True
        
print(f"Final answer is {answer}")