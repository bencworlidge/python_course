name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
print("Hello " + name + "! You are " + age + " years old!")

# CALCULATOR

num1 = input("Please enter a number: ")
num2 = input("Please enter a second number: ")
result = int(num1) + int(num2)  # int converts strings to whole number
result = float(num1) + float(num2)  # float accepts decimals
print(result)

# MADLIBS Game

color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a Celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
