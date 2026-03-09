# In python a person does not need to declare the data type of the variable.

a=5
b=6
print(a+b)

# How to give a user input to the Python code?

input("Enter a number:")
# Now remember by default the data type of the input is string. 
# So if you want to convert it into an integer, you can use the int() function.
# SO, let me show you 

a=input("Enter another number: ")
print(a)
print(type(a))

# If u run the previous line it will show you that the data type of an input is by default string.

# Now, lets convert it into an integer

a=int(a)
print(a)
print(type(a))

# Now, if u run the previous line it will show you that the data type of an input is now integer

# So the concept is pretty simple, you can use the int() function to convert a string into an integer.

# During the time of invoking the input function, you can directly convert the input into an integer by using the int() function.

a=int(input("Enter another number: "))
print(a)
print(type(a))

# See you can use the int() function to convert the input into an integer
# You can also use the float() function to convert the input into a float.
a=float(input("Enter another number: "))
print(a)
print(type(a))
