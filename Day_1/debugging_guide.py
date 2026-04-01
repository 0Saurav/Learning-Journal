# Beginner debugging mindset

# A. Did I spell the variable name correctly?

name = "Saurav"
print(nmae) # error


# B. Did I forget quotes for text?

city = Bhiswa  # wrong
city = "Bhiswa" # correct


# C. Did I forget type conversion?

age = input("Age: ")
print(age + 1) # wrong


# D. Am I mixing string and number incorrectly?


print("Age is " + 21) # Wrong




"""
When we do:
name = "Saurav"

Python roughly does this:
1. Create/store the string object "Saurav"
2. Bind the name name to  that object

Now if you do:

name = "Ram"

Python rebinds name to a different object.

"""