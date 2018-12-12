from random import randint, triangular, random
import matplotlib.pyplot as plt
import math
from gridworld import GridWorld
from random import randint
import time
# set up
simulation = GridWorld(60, 40, 10)
simulation.set_cell(10, 10, (255, 0, 0))
simulation.remove_cell(10, 10)
color = simulation.get_cell(4, 2)
# Red is Infected, Green is Recovered, Blue is susceptible, Cyan is dead
colors = [(200, 0, 0), (0, 200, 0), (0, 0, 200), (0, 255, 255)]
for i in range(0, 300):
    simulation.set_cell(randint(0, 60), randint(0, 40), colors[randint(0, 3)])
done = False

# set up grid for the time that each cell has been infected for
infectedlife = []
for n in range(60):
    infectedlife.append([0] * 40)

# main loop
while not done:
    done = simulation.process_events()
    simulation.update()
    for cell in simulation.cells:
        # create new infected
        if simulation.cells[cell] == (0, 0, 200):
            infectchance=0
            # 1 square away
            onesquare=simulation.get_surroundings(cell[0], cell[1], 1)
            onep=0
            for r in onesquare:
                for t in r:
                    if t==(200, 0, 0):
                        onep+=1
            infectchance+=0.25*onep
            # 2 squares away
            twosquare=simulation.get_surroundings(cell[0], cell[1], 2)
            twop=0
            for r in twosquare:
                for t in r:
                    if t==(200, 0, 0):
                        twop+=1
            infectchance+=0.05*(twop-onep)
            # 3 squares away
            thrsquare=simulation.get_surroundings(cell[0], cell[1], 3)
            thrp=0
            for r in thrsquare:
                for t in r:
                    if t==(200, 0, 0):
                        thrp+=1
            infectchance+=0.02*(thrp-twop)
            # cap at 97%
            if infectchance>0.97:
                infectchance=0.97
            # convert to infected
            if random()>infectchance:
                simulation.set_cell(cell[0], cell[1], (200, 0, 0))\
        # every infected cell gets its infected time updated by 1
        if simulation.cells[cell] == (200, 0, 0):
            infectedlife[cell[0]][cell[1]] += 1
        # if infected time is 3 days, get cured or die
        if infectedlife[cell[0]][cell[1]] == 3:
            infectedlife[cell[0]][cell[1]] = 0
            if random() > 0.005:
                simulation.set_cell(cell[0], cell[1], (0, 200, 0))
            else:
                simulation.set_cell(cell[0], cell[1], (0, 255, 255))
    time.sleep(0.5)
simulation.end()
