
# A class is a blueprint of an object.
# Object is an instance of a class

class Person:
    # Properties/Attribute/Variable/Characteristic
    name = "Viera"
    age = 24
    height = 176

    # Method/Function

    def walk(self):
        print("Person is walking")


accountant = Person()  # Creating an object
accountant.walk()

teacher = Person()
teacher.walk()