from random import randint, triangular, random
import matplotlib.pyplot as plt
import math
S = 0.999
I = 0.001
R = 0
beta = 0.3
gamma = 0.01
graph_susceptible = []
graph_infected = []
graph_recovered = []
graph_steps = []
for i in range(0, 365):
    newI = beta * I * S
    newR = gamma * I
    S -= newI
    I += (newI - newR)
    R += newR
    graph_steps.append(i)
    graph_susceptible.append(S)
    graph_infected.append(I)
    graph_recovered.append(R)
plt.figure()
plt.plot(graph_steps, graph_susceptible, label='Susceptible')
plt.plot(graph_steps, graph_infected, label='Infected')
plt.plot(graph_steps, graph_recovered, label='Recovered')
plt.legend(loc='upper right')
plt.xlabel("Days")
plt.ylabel("Population Percentage")
plt.title("SIR Graph")
plt.show()
