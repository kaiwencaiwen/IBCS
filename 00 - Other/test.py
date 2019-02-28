
sub1 = "AA AB".split(" ")
sub2 = "AB BB".split(" ")
sub3 = "B AA".split(" ")
steps, initial, final = "4 AB AAAB".split(" ")
steps = int(steps)
subs = [sub1, sub2, sub3]
treeofbeens = {}
currentpos = []


def explore(inp, s):
    for n in range(0, len(inp) - len(subs[s][0]) + 1):
        seg = inp[n:n + len(subs[s][0])]
        if subs[s][0] == seg:
            # initial = initial[:n] + subs[s][1] + initial[n + len(subs[s][0]):]
            rule = s + 1
            startpos = n + 1
            print("PATH FOUND", rule, startpos)
            available.append([rule, startpos])


def applymod(inp, rule, startpos):
    inp = inp[:startpos - 1] + subs[rule - 1][1] + \
        inp[startpos - 1 + len(subs[rule - 1][0]):]
    return inp


bigtree = {}
biglist = []
level = 1
available = []
explore(initial, 0)
explore(initial, 1)
explore(initial, 2)
for n in available:
    biglist.append([n])
print(biglist)
while level < steps:
    # GOING DOWN LEVELS
    level += 1
    newlist = []
    for k in range(len(biglist)):
        currentstr = initial
        for move in biglist[k]:
            currentstr = applymod(currentstr, move[0], move[1])
        available = []
        explore(currentstr, 0)
        explore(currentstr, 1)
        explore(currentstr, 2)
        for n in available:
            newlist.append(biglist[k] + [n])
    biglist = newlist
print(biglist)

for path in biglist:
    trystr = initial
    for move in path:
        trystr = applymod(trystr, move[0], move[1])
        print(trystr)
    if trystr == final:
        print("FINALLY FOUND")
        success = path
        break
# final output
print(success)
trystr = initial
for n in range(steps):
    trystr = applymod(trystr, success[n][0], success[n][1])
    print(path[n][0], path[n][1], trystr)
