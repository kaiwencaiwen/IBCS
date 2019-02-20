from random import randint, triangular, random
import matplotlib.pyplot as plt
import math
menpop = 84
womenpop = 91
fertile_rate = 0.6
birth_rate = 0.3
male_birth_rate = 0.5
death_rate = 0.05
predator_rate = 0.10
starvation_rate= 0.00000045
waste_accumulation_rate=0.5
time = 0
x_coords = []
y_coords = []
for i in range(0, 500):
    menpop -= int(menpop * death_rate)
    womenpop -= int(womenpop * death_rate)    
    if (menpop+womenpop)>1000:
        menpop-=int(300*menpop/(menpop+womenpop))
        womenpop-=int(300*womenpop/(menpop+womenpop))
    menpop-=int((menpop**3)*starvation_rate)
    womenpop-=int((womenpop**3)*starvation_rate)
    menpop-=int(i**waste_accumulation_rate)
    womenpop-=int(i**waste_accumulation_rate)

    for j in range(0, (menpop + womenpop)):
        if random() <= fertile_rate:
            if random() <= birth_rate:
                if random() <= male_birth_rate:
                    menpop += 1
                else:
                    womenpop += 1
    x_coords.append(i)
    y_coords.append(menpop + womenpop)
plt.figure()
plt.plot(x_coords, y_coords)
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Hopetopia Population Growth")
plt.show()

# years to reach optimal population: 15.5 years
# years to reach maximum population: 23.0 years
