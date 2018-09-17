#------------------------------------------------------------
# Returning more than one value
#------------------------------------------------------------

# One of the interesting things about Python is that it allows
# you to return more than 1 value at a time. Many languages do
# not let you do this. Take for example the code below:

def two_val(a, b):
    result1 = a + b
    result2 = a - b
    return result1, result2

x, y = two_val(10, 5)
print(x, y)