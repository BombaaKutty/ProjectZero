# Parent Class
class Animal:
    def speak(self):
        print("Animal is speaking")

# Child class
class Bee(Animal):
    def buzz(self):
        print("Bee is buzzing")

class Duck(Bee):
    def quacks(self):
        print("Duck is quacking")

a = Animal()
a.speak()

b = Bee()
b.buzz()
b.speak()

d = Duck()
d.quacks()
d.speak()
d.buzz()