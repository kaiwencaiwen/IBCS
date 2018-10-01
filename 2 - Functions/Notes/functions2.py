#------------------------------------------------------------
# Creating your own functions
#------------------------------------------------------------

# One of the most important parts of programming is being able
# to create your own functions and do it well. When you create
# your own function you should try to stick to the following
# guidelines:
#       1). Meaningful name
#       2). Short and does one thing well
#       3). Documented

# Why should you do this?
# Well, imagine if you started using Python and instead of using
# function likes abs, pow, print, the function names that were
# used were a, pw, pr instead. Code wouldn't be as readable
# probably even by yourself once it because too complex.

#------------------------------------------------------------
# Four types of functions
#------------------------------------------------------------

# Ok, so how do you create a function in Python?
# You need a function definition, the stuff the function does
# and an optional return statement

#       def function_name(parameters):
#           do stuff here
#           return

# Notice that everything after the first line, which is
# the function definition, is indented. This is SUPER important!

# Lets look at some examples:

# Example 1: A function that prints out a number.


def print_a_number(num_to_print):
    print(num_to_print)

# Example 2: A function that adds 5 to a number and returns it.


def add_five(num_to_add):
    num_to_add += 5
    return num_to_add

# Example 3: A function that just returns 5.


def give_me_five():
    return 5

# Example 4: A function that just prints


def say_hi():
    print("Hi")

# As you can see functions / procedures will have
# parameters    |   no return
# parameters    |   return
# no parameters |   return
# no parameters |   no return

#------------------------------------------------------------
# Complete Example
#------------------------------------------------------------

# In this example we'll create a function that has two numbers
# parameters and return them.


def add_up(num1, num2):
    total = num1 + num2
    return total

# A better way of doing this is the following:


def add_up(num1, num2):
    return num1 + num2


# Now we can call it!
result = add_up(5.34, 20)
print(result)
print(add_up(1, 2))
print(add_up(45.34, 34.2))
print(add_up("What's", " up?"))

# You may notice we have no way up making users put in numbers
# since Python is dynamically typed.

print("IMPORTANT:\nDYNAMIC TYPING vs STATIC TYPING")

# Let's call it again and look at how variables from outside
# get passed in.

# For reference
# def add_up(num1, num2):
#     return num1 + num2

a = 10
b = 5
c = add_up(a, b)
print(c)

#------------------------------------------------------------
# Practice
#------------------------------------------------------------


def foo1(a, b):
    a += b
    return a

# 1) What is this function's definition?
# 2) How many parameters does this function take?
# 3) What does this function return?
# 4) Can you tell what type this function returns?


def mean(a, b, c, d, e):
    # Body
    # Goes
    # Here
    return

# 5) This function should find the mean of 5 variables.
#    Ccmplete the body and return the value.

# 6) Write a function that takes in a numerator and denominator
#    and returns a printout that looks like following:
#    The fraction is 3/4 and the decimal value is 0.75
