import module1
import math
from module1 import say_hello
from math import sqrt
print(module1.var1)


def say_hello(name):
    print("you smell bad " + name)


say_hello("tom")

# Q9 the one in main

# Q10
print(math.ceil(2.5))
print(math.copysign(5.0, -2))
print(math.fabs(-6.0))
print(math.factorial(4))
print(math.floor(2.5))

# Q11


def sqrt(num):
    return num * num


print(sqrt(5))
# it uses the one created in main
