class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        print(self.name, "is watching Euros")


accountant = Person("Mesut", 35, "Male")
print(accountant.name)
print(accountant.age)
print(accountant.gender)
consultant = Person("Faith", 24, "Female")
print(consultant.name)
print(consultant.age)
print(consultant.gender)
doctor = Person("Frank", 35, "Male")
print(doctor.name)
print(doctor.age)
print(doctor.gender)
print(doctor.details())
