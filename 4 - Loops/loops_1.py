from random import randint
import os
# Q1
m = 8
while m >= -3:
    print(m)
    m -= 1

for n in range(8, -4, -1):
    print(n)

# Q2


def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True


for n in range(1, 10):
    print(["Even", "Odd"][is_odd(n)])

# Q3
rolltimes = 10

rolltally = [0] * 6
for n in range(rolltimes):
    rolltally[randint(1, 6) - 1] += 1

for c in range(len(rolltally)):
    print(rolltally[c], str(c + 1) + "s")

# Q5
# (see loopsQ5Robot)

# Q6
# (see loopsQ6Ants)