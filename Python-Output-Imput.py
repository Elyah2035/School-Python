"""Print text"""
print("Hello World!")

#Text in Python must be inside quotes.
#You can use either " double quotes or ' single quotes:

print("hello world")
#or
print('hello world')

"""
on default the print function is ending itself
if u want to print multiple words on the same line u can use the end parameter
"""

print("Hello World!", end=" ")
print("I will print on the same line.")

#Note that we add a space after end=" " for better readability.

"""Print Numbers"""

print(1)
print(12)
print(123)

#u can also do calculations in a print function
print(5 + 5)
print(5 * 5)

"""mixing text and numbers"""
a = 5
b = "9"
print("I am", 21,"years old")
print("I am" + "21" + "years old")
print("i am", a, "years old")
print("i am" + b, "years old")
