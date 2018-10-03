# Q1A
count = 0
while count < 10:
    print(count * 10)
    count += 1

# Q1B
count = 0
while count > -5.1:
    print(round(count, 2))
    count -= 0.2

# Q1C
count = 0
while count < 10:

    count += 1

# Q2A
b = 2
a = 1
for count in range(0, 5):
    a = b * a + 1
print(a)

# Q2B
for loop in range(0, 100):
    if loop % 3 and loop % 8:
        print(loop)
        
# Q2C
height = 13
height = int(height / 2)
justify = 2*height-1
spacing = 3
print(" " * justify, end="")
print("*")
for topdown in range(2):
    for n in range(height):
        if topdown:
            justify += 1
            spacing -= 2
        else:
            justify -= 1
            spacing = 2 * n + 1
        print(" " * justify, end="")
        print("*", end="")
        print(" " * spacing, end="")
        print("*")
    height -= 1
print(" " * (justify + 1), end="")
print("*")
