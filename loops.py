# While loop
# Incrementing values
number = 24
while number <= 29:
    print(number)
    number += 1

num = 105
while num <= 110:
    print("Number is",num)
    num += 1

# Decrementing values
count = 10
while count >= 1:
    print(count)
    count -= 1

# Break and continue statements
x = 25
while x <= 30:
    print(x)
    if x == 28:
        break
    x += 1

b = 0
while b <= 5:
    b +=1
    if b == 3:
        continue
    print(b)


# For loop
for y in range(11):
    print(y)

for z in range(1,9):
    print(z)

for mynumber in range(10,21,7):
    print(mynumber)

languages = ['Python','C++','Java','Javascript','C#','C++']
for lang in languages:
    print(lang)
