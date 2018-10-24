# Q1
adict = {"a": 34, "b": 55, "c": 43, "d": 3, "e": 23}

# Q2
import string,random
namedict = {}
for n in range(100):
    randname = random.choice(string.ascii_lowercase) + random.choice(
        string.ascii_lowercase) + random.choice(string.ascii_lowercase)
    randage = random.randint(1, 100)
    namedict[randname] = randage
print(namedict)

validkey = 0
for f in range(100):
    randcheck = random.choice(string.ascii_lowercase) + random.choice(
        string.ascii_lowercase) + random.choice(string.ascii_lowercase)

    if randcheck in namedict:
        print(randcheck)
        validkey += 1

print("percent of valid keys", validkey / 100)
