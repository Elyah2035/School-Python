#In Python, variables are created when you assign a value to it:
#unlike in other programming languages u dont need to
#asinge the variable type the programming language does it itself
#sometimes stupid tho-

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

"""Casting"""
"""If you want to specify the data type of a variable, this can be done with casting."""
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

"""Getting the type Variable"""
"""with type()"""
x = 5
y = "John"
print(type(x))
print(type(y))

"""Case sensitive!!!"""
A = 1
a = "applepie"
#A will not overwrite a, they are compleat different variables

print(A)
print(a)


"""
                                        Variable Names

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords.
"""

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#not allowed !!!
#2myvar = "John"  nuh uh
#my-var = "John"  - is a oporator and would mean a calculation
#my var = "John"  no space!


#Camel Case
#Each word, except the first, starts with a capital letter:

myVariableName = "John0"

#Pascal Case
#Each word starts with a capital letter:

MyVariableName = "John1"

#Snake case
#Each word is separated by an underscore character:

my_variable_name = "John2"
print("------------------------------")
"""Many Values to Multiple Variables"""
x, y, z = "Apple", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Note: Make sure the number of variables matches the number of values, or else you will get an error.
print("------------------------------")
"""One Value to Multiple Variables"""
x = y = z = "Cherry"
print(x)
print(y)
print(z)

print("------------------------------")
"""Unpack a Collection"""
#If you have a collection of values in a list, tuple etc.
#Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("------------------------------")
"""Output Variables"""
x = "Pyra is a woman"
print(x)

x = "Pyra"
y = "is"
z = "a woman"
print(x, y, z)

#You can also use the + operator to output multiple variables:
x = "Pyra "
y = "is "
z = "a woman"
print(x + y + z)

#Notice the space character after "Python " and "is ",
#without them the result would be "Pythonisawesome".

#For numbers, the + character works as a mathematical operator:
x = 5
y = 9
print(x + y)

#In the print() function,
#when you try to combine a string and a number with the + operator, Python will give you an error:
#x = "Matte"
#y = 5
#print(x + y)

#corect way:

x = 5
y = "Mate"
print(x, y)

"""Global Variables"""
#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.
x = "Ligar"

def myFunc():
    print(x)

myFunc()

#If you create a variable with the same name inside a function,
#this variable will be local, and can only be used inside the function.
#The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)

"""The global Keyword"""

#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

#To create a global variable inside a function, you can use the global keyword.

def myFunc():
    global x
    x = 5

myFunc()
print("I am", x)

#Also, use the global keyword if you want to change a global variable inside a function.

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("i am " + x)



