import pickle
import matplotlib.pyplot as plt
from random import random
with open("Pickles/actor_actress_cross.pickle", "rb") as f:
    actor_actress_cross = pickle.load(f)
with open("Pickles/actor_award.pickle", "rb") as f:
    actor_award = pickle.load(f)
with open("Pickles/actor_moviecount.pickle", "rb") as f:
    actor_moviecount = pickle.load(f)
with open("Pickles/actor_popularity.pickle", "rb") as f:
    actor_popularity = pickle.load(f)
with open("Pickles/average_runtime_year.pickle", "rb") as f:
    average_runtime_year = pickle.load(f)
with open("Pickles/byactor.pickle", "rb") as f:
    byactor = pickle.load(f)
with open("Pickles/byactress.pickle", "rb") as f:
    byactress = pickle.load(f)
with open("Pickles/bydirector.pickle", "rb") as f:
    bydirector = pickle.load(f)
with open("Pickles/bygenre.pickle", "rb") as f:
    bygenre = pickle.load(f)
with open("Pickles/byyear.pickle", "rb") as f:
    byyear = pickle.load(f)
with open("Pickles/decade_genrecount.pickle", "rb") as f:
    decade_genrecount = pickle.load(f)
with open("Pickles/details.pickle", "rb") as f:
    details = pickle.load(f)
with open("Pickles/director_award.pickle", "rb") as f:
    director_award = pickle.load(f)
with open("Pickles/director_moviecount.pickle", "rb") as f:
    director_moviecount = pickle.load(f)
with open("Pickles/director_popularity.pickle", "rb") as f:
    director_popularity = pickle.load(f)
with open("Pickles/genre_moviecount.pickle", "rb") as f:
    genre_moviecount = pickle.load(f)
with open("Pickles/genre_popularity.pickle", "rb") as f:
    genre_popularity = pickle.load(f)
with open("Pickles/year_moviecount.pickle", "rb") as f:
    year_moviecount = pickle.load(f)
with open("Pickles/year_popularity.pickle", "rb") as f:
    year_popularity = pickle.load(f)
# Graph 1
label_tick=[i for i in range(0,90,10)]
label_tick=tuple(label_tick)

yearlabels=[]
for n in range(1920,2001):
    if n%10==0:
        yearlabels.append(n)

year_popularity = sorted(year_popularity.items(), key=lambda kv: kv[0])

popval = [int(i[1]) for i in year_popularity]

fig, ax = plt.subplots()
bar_width = 0.5

bar1_index = [i for i in range(len(year_popularity))]

rects1 = ax.bar(bar1_index, popval, bar_width, color='b')

ax.set_xlabel('Year')
ax.set_ylabel('Popularity')
ax.set_title('Popularity of movies by year')
ax.set_xticks(label_tick)
ax.set_xticklabels(yearlabels)

fig.tight_layout()
plt.show()

# Graph 2
label_tick=[i for i in range(0,80,10)]
label_tick=tuple(label_tick)

yearlabels=[]
for n in range(1920,2000):
    if n%10==0:
        yearlabels.append(n)

decade_genrecount = sorted(decade_genrecount.items(), key=lambda kv: kv[0])

barcolors=["r","m","b","g","k"]
labels=["Action","Drama","Comedy","Horror","Mystery"]
biglist=[]
def compilelist(labeln):
    elist=[]
    for n in decade_genrecount:
        try:
            elist.append(n[1][labeln])
        except:
            elist.append(0)
    return elist
for n in range(5):
    biglist.append(compilelist(labels[n]))

fig, ax = plt.subplots()
def makealine(colorv,listn,labeln):
    ax.plot([i for i in range(0,80,10)], listn, color=colorv,marker='o',label=labeln)
for n in range(5):
    makealine(barcolors[n],biglist[n],labels[n])

ax.axis([0, 1, 0, 250])
ax.set_xlabel('Decade')
ax.set_ylabel('Amount')
ax.set_title('Number of movies by genre per decade')
ax.set_xticks(label_tick)
ax.set_xticklabels(yearlabels)
plt.legend()
plt.show()

# Graph 3
x = []
y = []
area=[]
for n in director_popularity:
    for m in director_award:
        if n[0]==m[0]:
            x.append(n[1])
            y.append(m[1])
            area.append(10*director_moviecount[n[0]])
plt.axis([0, 100, 0, 10])
plt.xlabel('Popularity')
plt.ylabel('Awards')
plt.title('Directors popualrity and awards won\n(size = amount of movies made)')
plt.scatter(x, y,s=area, alpha=0.5)
plt.show()