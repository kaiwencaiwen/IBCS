import math
# Q1
a = int(input())
b = int(input())


def mixdivide(a, b):
    mix = str(a // b) + " "
    mix += str(a % b)
    mix += "/" + str(b)

    return mix


print(mixdivide(a, b))

# Q2
str2 = input()


def findvowels(str2):
    v = 0
    for c in str2:
        if c.lower() in "aeiou":
            v += 1
    print(v)


# Q3
str3 = input()
vowels = ["a", "e", "i", "o", "u"]


def findvowels2(str3):
    v = [0, 0, 0, 0, 0]
    for num in range(0, 4):
        for c in str3:
            if c.lower() in vowels[num]:
                v[num] += 1
    print(v)

# Q4


def findvowels2(str3):
    v = [0, 0, 0, 0, 0]
    for num in range(0, 4):
        for c in str3:
            if c.lower() in vowels[num]:
                v[num] += 1
        return(v[0], v[1], v[2], v[3], v[4])


# Q5
radius = int(input())


def volumecalc(radius):
    return ((radius**3) * 4 / 3 * math.pi)


print(volumecalc(radius))


def areacalc(radius):
    return ((radius**2) * 4 * math.pi)


print(areacalc(radius))

# Q6


def neatlypresented(r, v, a):
    print("Given a sphere with radius of " + str(r) +
          ", the volume is " + str(v(r)) + " and the area is" + str(a(r)))


neatlypresented(radius, volumecalc, areacalc)

# Q7


def details(name="No name", age="No age", weight="Weightless"):
    print(name, age, weight)


details()

# Q8
RGB=(255,255,255)
RGBH=""
for n in RGB:
	RGBH+=hex(n)
print(RGBH)
