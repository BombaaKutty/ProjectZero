courses = ["MIT","Cyber Security","Data Science"]
print(courses)

# Accessing an element in an array
print(courses[0])

# Adding a new element in an array
courses.append("Android Development")
print(courses)

# Deleting elements in an array
courses.remove("MIT")
print(courses)

# Looping through an array
for course in courses:
    print(course)