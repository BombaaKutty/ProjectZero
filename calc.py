# Assignment
# A simple calculator program

first_value = int(input("Enter first number: "))
calc = input("Enter operator: ")
second_value = int(input("Enter second number: "))
if calc == "+":
    print(first_value + second_value)
elif calc == "-":
    print(first_value - second_value)
elif calc == "*":
    print(first_value * second_value)
elif calc == "/":
    if second_value == 0:
        print("Can't divide by zero")
    else:
        print(first_value / second_value)