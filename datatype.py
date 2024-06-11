# Datatype
number = 60 # Int
num = 45.35 # Float
greeting = "Hello World" # str
isPythonInteresting = True # boolean

fruits  = ["apple", "banana", "cherry","mango","orange"]  # List
cars = ("BMW","Toyota","Mercedes","JDM","Porsche") # Tuple
countries = {"Kenya","Argentina", "Germany","Uganda"} # Set
student = {
    "firstname" : "Goldridge",
    "age" : 22,
    "course" : "MIT",
    "nationality" : "English",
} # Dictionary


print(num)
print(isPythonInteresting)
print(fruits)
print(cars)
print(countries)
print(student["firstname"])

# Determining datatype
print(type(isPythonInteresting))
print(type(fruits))
print(type(cars))

# Typecasting is converting one datatype to another
print(int(num))
print(float(number))