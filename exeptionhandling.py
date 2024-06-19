try:

    print(number)
except:
        print("Error ocurred")


finally:
    print("Great")


x = 54
y = 0
print(x/y)
try:
    print(x/y)
except:
    print("Arithmetic error ocurred")
finally:
    print("Great")