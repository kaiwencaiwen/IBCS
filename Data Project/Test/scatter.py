import matplotlib.pyplot as plt
from random import random

x = []
y = []
area = []
colors = []

for i in range(0, 50):
    x.append(random() * 100)
    y.append(random() * 100)
    colors.append(random() * 50)
    area.append(random() * 200)

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()