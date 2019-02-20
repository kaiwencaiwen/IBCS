import matplotlib.pyplot as plt
import numpy as np
from random import randint as rt
# x coords, y coords, red and circles
x=[rt(0,100) for i in range(1000)]
y=plt.plot
plt.hist(x,100)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.show()