import matplotlib.pyplot as plt
import numpy as np
# x coords, y coords, red and circles
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

# numpy arange
someline = np.arange(0.0, 9.0, 0.1)
lines= plt.plot(someline, someline, "b--", linewidth=5.0)
# set property
plt.setp(lines,color="g")
# x min, x max, y min, y max on axis
plt.axis([0, 6, 0, 20])

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.show()
