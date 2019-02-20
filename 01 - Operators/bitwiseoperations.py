# Q1a
a = int(input())
b = 1
if a & b == 1:
    print("it's odd")
else:
    print("it's even")

# Q2
a = int(input())
n = int(input())
b = 1 << (n - 1)
if a & b == 2**(n - 1):
    print("nth bit is 1")
else:
    print("nth bit is 0")

# Q3
if a & b != 2**(n - 1):
    a = a | b

# Q4
if a & b == 2**(n - 1):
    a = a ^ b

# Q5
a = 32
print(a ^ a)
# answer is 0

# Q6
# create a value with 1 on the nth bit and run XOR operation with other number

# Q7
# changes every 1 to 0 and every 0 to 1

# Q8
a = int(input())
a = ~a
b = 1
while True:
    c = a | b
    if c != a:
        a = c
        break
    b = b << 1
a = ~a
print(a)

# Q9
a = int(input())
n = 1
while True:
    b = 1 << (n - 1)
    c = a | b
    if c == a:
        break
    n += 1
print("n is", n)
a = ~b

# Q10
a = int(input())
n = 1
while True:
    b = 1 << (n - 1)
    c = a | b
    if c != a:
        break
    n += 1
print("n is", n)
a = b

# Q11
a = int(input())
alist = list(bin(a))[2:]
alist = alist[::-1]
a = ''.join(alist)
print(int(a, 2))

# Q12
a = input()
b = input()
a = (a ^ b) ^ a
b = (b ^ a) ^ b
print(a, b)
