# Q1
alist = [1, 2, 0, 2, 5]


def sort(l):
    alist.sort()
    return alist[0:2]


print(sort(alist))

# Q2
blist = [1, 24, 6, 49, 4, 3, 1]


def removeodd(l):
    newl = []
    for n in l:
        if n % 2 == 0:
            newl.append(n)
    return newl


print(removeodd(blist))

# Q3
clist = ["b", 3, "c", 45, 1, "z"]
dlist = [12, "g", "s", "c", 33, 14, 4]


def sortlistsn(list1, list2):
    slist = []
    nlist = []
    for n in list1:
        if type(n) == int:
            nlist.append(n)
        else:
            slist.append(n)
    for n in list2:
        if type(n) == int:
            nlist.append(n)
        else:
            slist.append(n)
    slist.sort()
    nlist.sort()
    return slist, nlist


print(sortlistsn(clist, dlist))
