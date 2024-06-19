# In-built functions
y = max(230, 237, 3948, 31)
print("max value is", y)

m = min(230, 237, 3948, 31)
print("min value is", m)

w = pow(2, 4)
print("power is", w)


# User-defined function
def student():
    print("Cyril")


student()  # Calling a function


def person():
    print("person is walking")


person()


# Parameters and Arguments
def add(num1, num2):
    print(num1 + num2)

add(1, 2)
add(67, 876)

def Employee(fullname, email, salary, maritalstatus, position):
    print(fullname, email, salary, maritalstatus, position)

Employee("Sam Okumu", "sokumu@you.co.ke", 25994,"Single", "HR")
Employee("Kutty Bomba", "kbomba@you.co.ke", 235994,"Married", "CEO")
Employee("Luis Figo", "figol@you.co.ke", 20994,"Single", "Driver")
Employee("Victor Osimhen", "vosimhen@you.co.ke", 20994,"Single", "Driver")