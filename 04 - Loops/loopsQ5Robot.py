from random import randint


def botstep(bx, by):
    botcom = []
    if bx != 5:
        botcom.append(1)
    if bx != 0:
        botcom.append(2)
    if by != 5:
        botcom.append(3)
    if by != 0:
        botcom.append(4)
    stt = botcom[randint(1, len(botcom)) - 1]
    if stt == 1:
        bx += 1
    elif stt == 2:
        bx -= 1
    elif stt == 3:
        by += 1
    else:
        by -= 1
    return bx, by


def botrun():
    # starting position
    bx = 3
    by = 3

    # movement function
    stepcount = 0

    # row of crates
    northbox = [0] * 5
    southbox = [1] * 5
    iscarry = False

    while True:
        if northbox == [1] * 5:
            break
        bx, by = botstep(bx, by)
        stepcount += 1
        # pick up
        if by == 5 and southbox[bx - 1] == 1 and not iscarry:
            southbox[bx - 1] = 0
            iscarry = True

        # drop down
        if by == 0 and northbox[bx - 1] == 0 and iscarry:
            northbox[bx - 1] = 1
            iscarry = False
    return stepcount

# taking average
stepavg=0
for n in range(1000):
    stepavg+=botrun()
print(int(stepavg/1000))

#approximately 620