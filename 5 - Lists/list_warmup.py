import random
# Q1
lalist = ['a', 'z', 'd', 'g']

lalist[-1], lalist[0] = lalist[0], lalist[-1]
print(lalist)

# Q2
lalist = ['a', 'z', 'd', 'g']
lalist = lalist[1:3] + lalist + lalist[1:3]
print(lalist)

# Q3
lalist = ['a', 'z', 'd', 'g']
lalist = lalist[1::2] + lalist[::2]
print(lalist)

# Q4
sumlist = ["a", "b", "c", "d"]
for sumitem in sumlist:
    print(sumitem * 5)

# Q5
randlist = []
while len(randlist) < 100:
    randnum = random.randint(1, 100)
    if randnum % 2 == 1 and randnum % 7 != 0:
        randlist.append(randnum)
print(randlist)

# Q6
biglist = []
for number in range(50):
    smallist = []
    for factor in range(1, number + 1):
        if number % factor == 0:
            smallist.append(factor)
    biglist.append(smallist)
print(biglist)
