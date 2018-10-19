# Q1
for r in range(5):
    for n in range(10):
        print("*", end="")
    print("")

# Q2
height = 7
for r in range(height):
    print(" " * (height - 1 - r), end="")
    print("*" * (2 * r + 1))

# Q3
# help! I only know how to make it into a square
width = 91
print("*" * width)
crossdistance = 0
for n in range(width - 2):
    print("*", end="")
    for r in range(width - 2):
        if r == crossdistance:
            print("*", end="")
        elif width - r - 3 == crossdistance:
            print("*", end="")
        else:
            print(" ", end="")
    print("*")
    crossdistance += 1
print("*" * width)

# Q4 - see pygame_1.py
# Q5 - see pygame_2.py
