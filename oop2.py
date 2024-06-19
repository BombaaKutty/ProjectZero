class Students:
    def __init__(self, firstname, lastname, course, language):
        self.firstname = firstname
        self.lastname = lastname
        self.course = course
        self.language = language

    def sleep(self):
        print(self.firstname, "is sleeping")


C = Students("Caleb", "Ndungu", "MIT", "Python")
print(C.firstname)
print(C.lastname)
print(C.course)
print(C.language)
C.sleep()

Cl = Students("Clarence", "Kinyanjui", "MIT", "Kotlin")
print(Cl.firstname)
print(Cl.lastname)
print(Cl.course)
print(Cl.language)
Cl.sleep()
