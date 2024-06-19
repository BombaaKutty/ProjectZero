temperature = 32

if temperature < 25:
    print("It is cold")
elif temperature > 25:
    print("It is hot")
else:
    print("Normal temperature")

# A program that returns the largest number among three numbers
first = 56
second = 66
third = 46

if first > second and first > third:
    print(first,"is the largest number")
elif second > first and second > third:
    print(second,"is the largest number")
else:
    print(third,"is the largest number")



# Assignment - A python program that checks whether the program is odd or even

number = 0
if number == 0:
    print(number,"is neutral")
elif number == 0:
    print(number, "is even")
else:
    print(number, "is odd")


# A python program that returns the area of a rectangle
# A = L * W
length = 20
width = 5
area = length * width
print("The area is",area)

# A program that returns the area of a trapezium
# A = 0.5 * H * ( a + b )
height = 25
a = 4
b = 10
area = (0.5) * height * ( a + b )
print("The area is",area)