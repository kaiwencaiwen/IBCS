a = 10
b = 20
c = 30


def foo1(a, b):
    a = b + c
    print(a)


def foo2(b, c):
    b = a + c
    print(b)


def foo3(a, c):
    c = a + b
    print(c)


# Q1a 34
# Q1b 16
# Q1c 27
# Q1d Error: None type

# Q2
def foo1(a, d):
    a = b + c
    print(a)

# Q3


def foo4(d, e, f):
    sumlocal = d + e + f
    sumglobal = a + b + c
    return sumlocal, sumglobal


print(foo4(1, 2, 3))

# Q4


def add(num1, num2):
    return num1 + num2


def triple(num):
    return add(num, add(num, num))


def quadruple(num):
    return add(num, triple(num, num))
# Q5