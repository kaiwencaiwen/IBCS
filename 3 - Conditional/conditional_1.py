# Q1
age = 18


def driveage(age):
    if age >= 18:
        print("yes drive")
    else:
        print("no drive")


driveage(age)

# Q2
sideA = 3
sideB = 4
sideC = 6


def aor(sa, sb, sc):
    if sa**2 + sb**2 > sc**2:
        print("acute")
    elif sa**2 + sb**2 < sc**2:
        if sc > sa + sb:
            print("no")
        else:
            print("obtuse")
    elif sa**2 + sb**2 == sc**2:
        print("right")
    else:
        print("idk")


def bigaor(sideA, sideB, sideC):
    if sideC >= sideB and sideC >= sideA:
        aor(sideA, sideB, sideC)
    elif sideB >= sideA and sideB >= sideC:
        aor(sideC, sideA, sideB)
    elif sideA >= sideC and sideA >= sideB:
        aor(sideB, sideC, sideA)


bigaor(sideA, sideB, sideC)

# Q3
fzbz = 30


def fizzbuzz(fzbz):
    if fzbz % 15 == 0:
        print("fizzbuzz")
    elif fzbz % 3 == 0:
        print("fizz")
    elif fzbz % 5 == 0:
        print("buzz")
    else:
        print("huh?")


fizzbuzz(fzbz)

# Q4
import math
combn = 4
combr = 2


def combos(combn, combr):
    return math.factorial(combn) / (math.factorial(combr) * math.factorial(combn - combr))


print(combos(combn, combr))

# Q5
import random


def insult():
    print("you look like a" + [" dog", " cat", "n egg", " hippo",
                               "n umbrella", " depressed teenager"][random.randint(0, 5)])


insult()

# Q6
guess1 = 3
guess2 = 4
guess3 = 6


def diceroll(guess1, guess2, guess3):
    rights = 0
    if random.randint(1, 6) == guess1:
        rights += 1
    if random.randint(1, 6) == guess2:
        rights += 1
    if random.randint(1, 6) == guess3:
        rights += 1
    return rights


print(diceroll(guess1, guess2, guess3))

# Extension
# Q1
range1 = 1.4
range2 = 1.5


def rangen(range1, range2):
    if type(range1) == int:
        return random.randint(range1, range2)
    elif type(range1) == float:
        return random.uniform(range1, range2)
    elif type(range1) == str:
        return chr(random.randint(ord(range1), ord(range2)))


print(rangen(range1, range2))

# Q2a
m = 0
n = 1


def fibgen(n, m, a):
    for i in range(0, a):
        if i == 0:
            yield 0
        elif i == 1:
            yield 1
        else:
            yield m + n
            m, n = n, m + n


my_generator = fibgen(n, m, 10)
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))

# Q2b
primnum = 2
primlist = []


def prigen(primnum, a):
    for i in range(0, a):
        if i == 0:
            yield 1
        else:
            while True:
                isprim = True
                for n in primlist:
                    if primnum % n == 0:
                        isprim = False
                if isprim:
                    primlist.append(primnum)
                    yield primnum
                else:
                    primnum += 1


mg = prigen(primnum, 10)
print(next(mg))
print(next(mg))
print(next(mg))
print(next(mg))
print(next(mg))
print(next(mg))
print(next(mg))
print(next(mg))

# Q2c


def macrogen(a):
    for i in range(0, a):
        randstart = random.randint(0, 20)
        randend = random.randint(30, 50)

        def microgen(b):
            for i in range(0, b):
                yield random.randint(randstart, randend)
        yield microgen


macgen = macrogen(10)
print(next(next(macgen)(4)))

# this is too meta, I'm now in the 4th dimension
