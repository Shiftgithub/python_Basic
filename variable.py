x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally"  # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# variable type
x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
print(x)
# double quotes are the same as single quotes:
x = 'John'
print(x)

a = 4
A = "Sally"

# Case-Sensitive
print(a)
print(A)

# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"

# Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

# Example
# Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
# The Python print() function is often used to output variables.

# ExampleGet your own Python Server
x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x = 5
y = "John"
print(x, y)

# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

# Create a variable outside of a function, and use it inside the function

x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

# Create a variable inside a function, with the same name as the global variable

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)
