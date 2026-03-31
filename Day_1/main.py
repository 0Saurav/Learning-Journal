# Variables : A variable is a name that refers to a value.

name = 'Saurav'
age = 20

"""
Here name refers to Saurav
Age refers to 20
"""

"""
A variable is not a box in the strictest Python sense

A variable is a label attached to an object/value.

VARIABLE --> NAME -> VALUE
"""

# Creating a variable

# variable_name = value

name  = "Saurav"
age = 21
height = 5.10
is_student = True

# Common Data types you'll meet immediately

# String (str) = Text Values

name  = "Python"
city = "Kathmandu"
# A string must be inside quotes.

# Integer (int) = Whole numbers

age = 24
marks = 95

# Float (float) = Decimal numbers

price = 99.99
height = 5.10

# Boolean (bool) = only two values

is_online = True
is_logged_in = False

"""True and False must start wih capital letters."""

# Rules for naming variables : Python allows flexibility, but there are rules

# Valid variable names

name = "Ram"
age1 = 25
user_name = "Hari"
total_marks = 500

# Invalid varaible names
# 1name = "Ram"  ---> cannot start with number
# user-name = "Hari" --> hyphen not allowed
# class = "Python"  --> reserved keyword


# Best practices for namig variables (write names that exlain the meaning)

# Bad 
x = 'Saurav'
y = 24
z = True

# Good
student_name = "Saurav"
student_age = 21
is_enrolled = True


# Python naming convention : snake_case
"""Use lowercase letters and words separated by _ """

student_name = "Saurav"
total_price = 1500
phone_number = "9609399999"



# Variables can change (tats why they're called variables)

age = 20
print(age)

age = 21
print(age)

# So the variable name can stay the same but the value can change.

# Python is dynamically typed

"""In python you do not declare the type manually in normal code."""

x = 10
x = "hello"
x = 3.14


# Python decided the type at runtime based on the value.

value = 10 
print(type(value))

value = "hello"
print(type(value))



# type() -> checking data type

name = "Saurav"
age = 21
height = 5.10
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# print() -> Displaying output --> used to show output on the screen

print(value)

print("Hello python")

# Printing text vs variables

print("My name is Saurav")

name  = "Saurav"
print(name)


# print() automatically adds a new line

print("Hello")
print("World")

# Each print() ends with a newline by default


# The " end= " parameter in print() -> we can control what print() adds at the end

print("Hello", end="\n") # this is default behavior

print("Hello", end=" ")
print("World")  # same line with a space

print("Python", end="-")
print("Beginner")



# The sep= parameter in print() -> python will separate items with spaces by default

print("Saurav", 21, "Nepal")

# Custom separator
print("Saurav", 24, "Nepal", sep= " | ")



# Printing special characters
# New lines: \n

print("Hello\nWorld")

# Tab: \t

print("Name:\tsaurav")



# Using quotes inside the strings

print("He said, 'Hello'")
print('He said, "Hello"')


# Escape characters \

print("He said, \"Hello\"")


# String Concatenation (joining strings) --> Using +

first_name = "Saurav"
last_name = "Sen"

full_name = first_name + " " + last_name
print(full_name)

# + works nicely for string + string but not automatically for string + number


# Common error: string + integer

age = 21
# print("My age is " + age) --> TypeError

"""Because "My age is " is a string
age is an integer"""

# Correct ways
# Method 1 - convert manually with use of str()

age = 21
print("My age is " + str(age))

# Method 2 - use commas (better)
age = 21
print("My age is", age)

# Method 3 - Use f-string (best modern way / Pythonic way) 
age = 21
print(f"My age is {age}")




# fstrings -> lets you insert variables directly into a string.
# f"some text {variables}"

name = "Saurav"
age = 21

print(f"My name is {name} and I am {age} years old.")




