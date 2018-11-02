import operator
# task 1
attributes = []
details = []
with open("Assets/movies.txt", "r", encoding='utf-8') as f:
    attributes = tuple(f.readline().strip().replace("\t", "").split(";"))
    f.readline()
    fline = f.readlines()
for l in range(len(fline)):
    c = tuple(fline[l].strip().replace("\t", "").split(";"))
    details.append(c)

# task 2
with open("Assets/movie.tsv", "w", encoding="utf-8") as f:
    for l in range(len(attributes)):
        f.write(attributes[l])
        if l != len(attributes) - 1:
            f.write("\t")
    f.write("\n")
    for c in details:
        for l in range(len(c)):
            f.write(c[l])
            if l != len(c) - 1:
                f.write("\t")
        f.write("\n")

# task 3
by_year = {}
by_director = {}
by_actor = {}
by_genre = {}
by_actress = {}


def createdict(dname, ind):
    for c in details:
        try:
            dname[c[ind]].append(c)
        except:
            dname[c[ind]] = [c]


createdict(by_year, 0)
createdict(by_director, 6)
createdict(by_actor, 4)
createdict(by_genre, 3)
createdict(by_actress, 5)

# task 4


def avgry():
    avg_runtime_year = {}
    for year, detail in by_year.items():
        totallen = 0
        moviescount = 0
        for c in detail:
            if c[1] != "":
                totallen += int(c[1])
                moviescount += 1
        avg_runtime_year[year] = totallen / moviescount
    return avg_runtime_year


print(avgry())


def dm():
    directors_moviecount = {}
    for director, detail in by_director.items():
        directors_moviecount[director] = len(detail)
    return directors_moviecount


print(dm())


def am():
    actor_moviecount = {}
    for actor, detail in by_actor.items():
        actor_moviecount[actor] = len(detail)
    return actor_moviecount


print(am())


def ym():
    year_moviecount = {}
    for year, detail in by_year.items():
        year_moviecount[year] = len(detail)
    return year_moviecount


print(ym())


def gm():
    genre_moviecount = {}
    for genre, detail in by_genre.items():
        genre_moviecount[genre] = len(detail)
    return genre_moviecount


print(gm())


def ypop():
    year_popularity = {}
    for year, detail in by_year.items():
        totalpop = 0
        moviescount = 0
        for c in detail:
            if c[7] != "":
                totalpop += int(c[7])
                moviescount += 1
        try:
            year_popularity[year] = totalpop / moviescount
        except:
            pass
    return year_popularity


print(ypop())


def gpop():
    genre_popularity = {}
    for genre, detail in by_genre.items():
        totalpop = 0
        moviescount = 0
        for c in detail:
            if c[7] != "":
                totalpop += int(c[7])
                moviescount += 1
        try:
            genre_popularity[genre] = totalpop / moviescount
        except:
            pass
    return genre_popularity


print(gpop())


def decg():
    decade_genrecount = {}
    for movi in details:
        if "19" + str(movi[0])[2] + "0s" in decade_genrecount:
            if movi[3] in decade_genrecount["19" + str(movi[0])[2] + "0s"]:
                decade_genrecount["19" + str(movi[0])[2] + "0s"][movi[3]] += 1
            else:
                decade_genrecount["19" + str(movi[0])[2] + "0s"][movi[3]] = 1
        else:
            decade_genrecount["19" + str(movi[0])[2] + "0s"] = {movi[3]: 1}
    return decade_genrecount


print(decg())

# Task 5


def act2():
    actor_actress = {}
    for actor, movis in by_actor.items():
        actor_actress[actor] = {}
        for m in movis:
            try:
                actor_actress[actor][m[5]] += 1
            except:
                actor_actress[actor][m[5]] = 1

    for actor, actresses in actor_actress.items():
        for actress, crosstime in actresses.items():
            if crosstime >= 2 and actress != "" and actor != "":
                print(actor, "and", actress)


act2()


def actpop():
    actor_popularity = {}
    for actor, movis in by_actor.items():
        ap = 0
        mcount = 0
        for m in movis:
            if m[7] != "":
                ap += int(m[7])
                mcount += 1
        if mcount != 0:
            actor_popularity[actor] = ap / mcount
    return sorted(actor_popularity.items(), key=operator.itemgetter(1))


print(actpop())


def dirpop():
    director_popularity = {}
    for director, movis in by_director.items():
        dp = 0
        mcount = 0
        for m in movis:
            if m[7] != "":
                dp += int(m[7])
                mcount += 1
        if mcount != 0:
            director_popularity[director] = dp / mcount
    return sorted(director_popularity.items(), key=operator.itemgetter(1))


print(dirpop())


def actawd():
    actor_award = {}
    for actor, movis in by_actor.items():
        aa = 0
        mcount = 0
        for m in movis:
            if m[8] == "Yes":
                aa += 1
        actor_award[actor] = aa
    return sorted(actor_award.items(), key=operator.itemgetter(1))


print(actawd())


def dirawd():
    director_award = {}
    for director, movis in by_director.items():
        da = 0
        for m in movis:
            if m[8] == "Yes":
                da += 1
        director_award[director] = da
    return sorted(director_award.items(), key=operator.itemgetter(1))


print(dirawd())