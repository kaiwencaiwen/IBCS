'''
A double bar chart. 

In this code you have to worry about subplots
and using the axis (ax) in order to get your 
bars to line up correctly. 

figure (fig) and axis(ax) are variables which
represent different parts of the plot, and by
changing them you are changing the resulting
values on the bar chart. 

'''

import matplotlib.pyplot as plt
from random import random

means_men = (34, 35, 30, 35, 27)
means_women = (25, 32, 34, 20, 25)

fig, ax = plt.subplots()
bar_width = 0.35

bar1_index = [0, 1, 2, 3, 4]
bar2_index = [0.35, 1.35, 2.35, 3.35, 4.35]
label_tick = [0.18,1.18,2.18,3.18,4.18]

rects1 = ax.bar(bar1_index, means_men, bar_width, color='b',  label='Men')
rects1 = ax.bar(bar2_index, means_women, bar_width, color='r',  label='Women')

ax.set_xlabel('Group')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(label_tick)
ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
ax.legend()

fig.tight_layout()
plt.show()