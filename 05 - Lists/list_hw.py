import random
import math
# Q1


def sixfirstlast(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True
    return False


print(sixfirstlast([6, 0, 0, 1]))


# Q2
def revlist(nums):
    return nums[::-1]


print(revlist([3, 2, 1]))


# Q3
def firstlast(nums):
    return[nums[0], nums[-1]]


print(firstlast([3, 2, 1, 1, 2, 5]))


# Q4
def twoorthree(nums):
    for item in nums:
        if item == 2 or item == 3:
            return True
    return False


print(twoorthree([1, 2, 5]))


# Q5
def evennums(nums):
    evencount = 0
    for item in nums:
        if item % 2 == 0:
            evencount += 1
    return evencount


print(evennums([1, 3, 5, 4, 5, 3]))


# Q6
def weirdlistsum(nums):
    weirdcount = 0
    for numindex in range(len(nums)):
        if nums[numindex] != 13 and nums[numindex - 1] != 13:
            weirdcount += nums[numindex]
    return weirdcount


print(weirdlistsum([1, 1, 13, 4, 5]))


# Q7
def averageof(nums):
    maxnum = -99
    minnum = 99
    for item in nums:
        if item > maxnum:
            maxnum = item
        if item < minnum:
            minnum = item
    nums.remove(maxnum)
    nums.remove(minnum)
    numsavg = 0
    for item in nums:
        numsavg += item
    numsavg = int(numsavg / len(nums))
    return numsavg


print(averageof([0, 1, 4, 5, 10, 8, 7]))


# Q8
def ispalindrome(nums):
    if nums[::-1] == nums:
        return True
    return False


print(ispalindrome([7, 4, 5, 4, 7]))


# Q9
def uniquestring(strings):
    lowstrings = []
    for item in strings:
        lowstrings.append(item.lower())
    lowstrings = list(set(lowstrings))
    return lowstrings


print(uniquestring(["pala", "mala", "bala", "PAla", "MalA", "pala"]))


# Q10
def makecoords():
    coordlist = []
    for n in range(100):
        coordlist.append((random.randint(-100, 100),
                          random.randint(-100, 100), random.randint(-100, 100)))
    return coordlist


def shortdis(coordlist):
    shortdis = 1000
    for coord in range(len(coordlist)):
        for coord2 in range(len(coordlist)):
            if coord != coord2:
                dis = math.sqrt((coordlist[coord][0] - coordlist[coord2][0])**2 + (
                    coordlist[coord][1] - coordlist[coord2][1])**2 + (coordlist[coord][2] - coordlist[coord2][2])**2)
                if dis < shortdis:
                    shortcoord = [coordlist[coord], coordlist[coord2]]
    return shortcoord


print(shortdis(makecoords()))


# Q11
def makenums():
    randnums = []
    for n in range(100):
        randnums.append(random.randint(0, 1000))
    return randnums


def twentyaway(nums):
    edgynum = []
    nums.sort()
    for numindex in range(len(nums)):
        if numindex == 0:
            if nums[numindex + 1] - nums[numindex] > 20:
                edgynum.append(nums[numindex])
        elif numindex == len(nums)-1:
            if nums[numindex] - nums[numindex - 1] > 20:
                edgynum.append(nums[numindex])
        elif nums[numindex] - nums[numindex - 1] > 20 and nums[numindex + 1] - nums[numindex] > 20:
            edgynum.append(nums[numindex])
    return edgynum


print(twentyaway(makenums()))
