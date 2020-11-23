# Print Statements
from math import *  # Accesses more Python math methods
print("Hello World")

# Variables
full_name = "Ben Worlidge"
age = "29"
print("Hello, my name is " + full_name + " and I am " + age + " years old.")
age = "26"  # redeclare
print("Wait, I forgot, I'm actually " + age + ".")

# Strings
print("This is a \n linebreak")
# Backslash renders the following character literally
print("This is a \"quotation mark\"")
phrase = "I am Ben Worlidge"
print(phrase.lower())  # Make Uppercase
print(phrase.upper())  # Make Lowercase
print(phrase.isupper())  # Boolean on whether upper or lower
print(len(phrase))  # Length
print(phrase[5])
# Returns index of first character. Can also use several letters or words.
print(phrase.index("B"))
# Replace first argument with second. Can also use with words.
print(phrase.replace("B", "W"))


print(4 * 8 + 5)
print(4 * (8 + 5))  # Parenthesis specifies order of operation
print(10 % 3)  # Like JS, modulus functions the same way

num = -22
print(str(num))  # Convert to string
print(abs(num))  # Absolute value
print(pow(5, 6))  # Takes first number to the power of second
print(max(4, 10, 20, 3, 40))  # Prints max number
print(min(4, 10, 20, 3, 40))  # Prints min number
print(round(4.7))  # Rounds to nearest whole
print(floor(3.4))  # Always rounds down
print(ceil(3.4))  # Always rounds up
print(sqrt(49))  # Squareroot
