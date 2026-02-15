"""
Built-in Data Types

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type: 	        str
Numeric Types: 	    int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	    dict
Set Types: 	        set, frozenset
Boolean Type: 	    bool
Binary Types: 	    bytes, bytearray, memoryview
None Type: 	        NoneType
"""
x = 5
print(type(x))


#Example                                        Data Type
x = "Hello World" 	                            #str
x = 20 	                                        #int
x = 20.5 	                                    #float
x = 3+5j	                                    #complex
x = ["apple", "banana", "cherry"] 	            #list
x = ("apple", "banana", "cherry") 	            #tuple
x = range(6) 	                                #range
x = {"name" : "John", "age" : 36} 	            #dict
x = {"apple", "banana", "cherry"} 	            #set
x = frozenset({"apple", "banana", "cherry"}) 	#frozenset
x = True 	                                    #bool
x = b"Hello" 	                                #bytes
x = bytearray(5) 	                            #bytearray
x = memoryview(bytes(5)) 	                    #memoryview
x = None 	                                    #NoneType

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#or '''...'''

#Strings are Arrays
a = "Hello, World!"
print(a[1]) #prints "a"
#Slice From the Start
b = "Hello, World!"
print(b[:5]) # prints "Hello"
print(b[7:]) # prints "World!"
#Negative Indexing
"""
Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
"""
print(b[-5:-2]) #prints "orl"
#UPPER CASE
print(b.upper())
#lower case
print(b.lower())
#Remove whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#Repace String
print(a.replace("H", "J"))
#Split String
print(a.split(",")) #prints ['Hello', ' World!']
print(a.split())    #prints ['Hello,', 'World!'
#Looping Through a String
for x in "banana":
  print(x)

#String Length
a = "Hello World!"
print(len(a)) #prints 12

#Check String
txt = "The best things in life are free!"
print("free" in txt)
#with if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#if not
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Format
#this will not work:
"""
 age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)
"""
#F-Strings
age = 30
price = 50
txt = f"My name is John, i am {age} years old"
print(txt)
txt = f"The price is {age:.5f} dollars" #prints The price is 30.00000 dollars
print(txt)
txt = f"My name is John, i am {6*5} years old"
print(txt)
#escape characters
txt = "We are the so-called \"Vikings\" from the north." #We are the so-called "Vikings" from the north.
print(txt)
"""
Code 	  Result
\' 	      Single Quote
\\ 	      Backslash
\n 	      New Line
\r 	      Carriage Return
\t 	      Tab
\b 	      Backspace
\f     	  Form Feed
\ooo 	  Octal value
"""
#\xhh 	  Hex value



"""Setting the Specific Data Type"""

#Example 	                                    Data Type
x = str("Hello World") 	                        #str
x = int(20) 	                                #int        - note float -> int it cuts off everything after the comma 2.8 -> 2
x = float(20.5) 	                            #float      - note int -> float it will add a .0 at the end 1 -> 1.0 or "3" -> 3.0
x = complex(1j) 	                            #complex
x = list(("apple", "banana", "cherry")) 	    #list
x = tuple(("apple", "banana", "cherry")) 	    #tuple
x = range(6) 	                                #range
x = dict(name="John", age=36) 	                #dict
x = set(("apple", "banana", "cherry")) 	        #set
x = frozenset(("apple", "banana", "cherry")) 	#frozenset
x = bool(5) 	                                #bool
x = bytes(5) 	                                #bytes
x = bytearray(5) 	                            #bytearray
x = memoryview(bytes(5)) 	                    #memoryview




"""Random Numbers"""

import random
print(random.randrange(1, 10)) # lowest number to highes 1,2,3,...,9



