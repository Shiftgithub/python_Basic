# Python Booleans
# Booleans represent one of two values: True or False.

# Boolean Values
# In programming you often need to know if an expression is True or False.

# You can evaluate any expression in Python, and get one of two answers, True or False.

# When you compare two values, the expression is evaluated and Python returns the Boolean answer:

# ExampleGet your own Python Server
print(10 > 9)
print(10 == 9)
print(10 < 9)

# When you run a condition in an if statement, Python returns True or False:

# Example
# Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,

# Example
# Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))
print(bool())

# Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))