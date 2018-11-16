import matplotlib.pyplot as plt
import random
data = []
total = 10
for i in range(0, 100):
    total += random.random() * 2 - 1
    data.append(total)

plt.plot(data, 'b-')
plt.show()
