#------------------------------------------------------------
# Function calls
#------------------------------------------------------------
# What is a function and what is this weird gray text?
# The gray text is a comment!
# A function a way to create a single location for doing something.

# When we use a function we're calling it.
# Examples of function calls

print("Hi!")                #print prints stuff to the screen
print(abs(-4))              #abs finds absolute value
print(pow(2, 5))            #pow is for "power of"
print(bin(50))              #bin gives the binary of an number
print(abs(-4), pow(2, 5), bin(50))

# In these function calls you may have notice that some have
# commas and are doing more than one thing at a time. To
# understand this we need to look at how functions are
# created in Python.


#------------------------------------------------------------
# Parameters vs. Arguments
#------------------------------------------------------------
# Functions have something called a parameter list. It defines
# what arguments the function is looking for.  Some functions
# take 0 arguments while other functions take 1, 2, 3 or can
# be flexible in how many they take.

# Parameter is what the function is expecting
# Argument is the actual thing you pass the function.

# For example look at abs( )
abs(-4)
abs(10)
abs(-4.23)

# The abs function is expecting a number parameter. In this case
# it was passed arguments of -4, 10, -4.23.

#------------------------------------------------------------
# Return values
#------------------------------------------------------------

# Not only do you pass arguments to functions but the functions
# will sometimes return things back to you. If a function DOESN'T
# return something then it's called a procedure. How do you know
# if it's a function or a procedure?

var1 = abs(-50)        # returns 50 and puts it in var1
var2 = pow(2, 5)       # returns 32 and puts it in var2
var3 = print("Hi")     # What does this do?

# We can check return type by using the
# type function on the above variables

print(type(var1), type(var2), type(var3))

# A function that returns None is really called a procedure, but
# most of the time people use the words interchangeably even
# though it's incorrect. Note that a function doesn't need to
# return anything and it doesn't need to have parameters either.
# We'll discuss this more in the next section.


#------------------------------------------------------------
# Summarize and practice
#------------------------------------------------------------

# What type do the following function calls return?
# 1) abs(-5.0)
# 2) pow(2, 0.2)
# 3) bin(45)
# 4) ord('5')
# 5) int('100')
# 6) str(56.02)