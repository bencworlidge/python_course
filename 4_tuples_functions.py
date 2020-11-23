# Tuples are immutable and are typically used when data can't change (like const)
coordinates = (45, 60)
print(coordinates[1])


# Functions
def sayhello(name, age):
    # str() turns number into string
    print("Hello " + name + "! You are " + str(age) + ".")


sayhello("Ben", 29)


# Return statement
def cube(num):
    return num * num * num


print(cube(20))
