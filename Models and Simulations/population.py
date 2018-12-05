from random import randint, triangular, random
import matplotlib.pyplot as plt
import math
population = 1
step = 12
birth_rate = 0.85
death_rate = 0.2
predator_rate = 0.10
starvation_rate_baseline = 0.3
current_starvation_rate = starvation_rate_baseline
time = 0
x_coords = []
y_coords = []
for i in range(0, 6):
    population -= int(population * death_rate)
    current_starvation_rate = starvation_rate_baseline * \
        math.log(population, 10)
    population -= int(current_starvation_rate * population)
    if population < 1000:
        population -= int(population * predator_rate)
    else:
        population -= int(population * predator_rate * 1.2)
    for j in range(0, population):
        if random() <= birth_rate:
            population += int(triangular(1, 15, 20))
    x_coords.append(i * step)
    y_coords.append(population)
plt.figure()
plt.plot(x_coords, y_coords)
plt.xlabel("Hours")
plt.ylabel("Population")
plt.title("Tribble Population Growth")
plt.show()
