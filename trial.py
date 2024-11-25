print("Hello world!")
if 5 > 2:
  print("Five is greater than two!")
# In Python, variables are created when you assign a value to it:   
x = 5
y = "Hello, World!"

# Comments starts with a #, and Python will ignore them:

# Comments can be placed at the end of a line, and Python will ignore the rest of the line:
x=5
y=7
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

a = 4       # x is of type int
a = "Sally" # x is now of type str
print(a)

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y)) 

# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# in the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x = 5
y = "John"
print(x, y)

