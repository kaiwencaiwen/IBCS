import pickle
import operator
with open("Pickles/byyear.pickle", "rb") as f:
    by_year = pickle.load(f)
with open("Pickles/byactress.pickle", "rb") as f:
    by_actress = pickle.load(f)
with open("Pickles/bydirector.pickle", "rb") as f:
    by_director = pickle.load(f)
with open("Pickles/bygenre.pickle", "rb") as f:
    by_genre = pickle.load(f)
with open("Pickles/byactor.pickle", "rb") as f:
    by_actor = pickle.load(f)
with open("Pickles/details.pickle", "rb") as f:
    details = pickle.load(f)
# Task 4


def avgry():
    avg_runtime_year = {}
    for year, detail in by_year.items():
        totallen = 0
        moviescount = 0
        for c in detail:
            if c[1] != "":
                totallen += int(c[1])
                moviescount += 1
        if moviescount != 0:
            avg_runtime_year[year] = totallen / moviescount
    return avg_runtime_year


def dm():
    directors_moviecount = {}
    for director, detail in by_director.items():
        directors_moviecount[director] = len(detail)
    return directors_moviecount


def am():
    actor_moviecount = {}
    for actor, detail in by_actor.items():
        actor_moviecount[actor] = len(detail)
    return actor_moviecount


def ym():
    year_moviecount = {}
    for year, detail in by_year.items():
        year_moviecount[year] = len(detail)
    return year_moviecount


def gm():
    genre_moviecount = {}
    for genre, detail in by_genre.items():
        genre_moviecount[genre] = len(detail)
    return genre_moviecount


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
    cross = []
    for actor, actresses in actor_actress.items():
        for actress, crosstime in actresses.items():
            if crosstime >= 2 and actress != "" and actor != "":
                cross.append((actor, actress))
    return cross


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


def dirawd():
    director_award = {}
    for director, movis in by_director.items():
        da = 0
        for m in movis:
            if m[8] == "Yes":
                da += 1
        director_award[director] = da
    return sorted(director_award.items(), key=operator.itemgetter(1))


# Pickle it!
with open("Pickles/average_runtime_year.pickle", "wb") as f:
    pickle.dump(avgry(), f)

with open("Pickles/directors_moviecount.pickle", "wb") as f:
    pickle.dump(dm(), f)
with open("Pickles/year_moviecount.pickle", "wb") as f:
    pickle.dump(ym(), f)
with open("Pickles/genre_moviecount.pickle", "wb") as f:
    pickle.dump(gm(), f)
with open("Pickles/actor_moviecount.pickle", "wb") as f:
    pickle.dump(am(), f)

with open("Pickles/genre_popularity.pickle", "wb") as f:
    pickle.dump(gpop(), f)
with open("Pickles/year_popularity.pickle", "wb") as f:
    pickle.dump(ypop(), f)
with open("Pickles/actor_popularity.pickle", "wb") as f:
    pickle.dump(actpop(), f)
with open("Pickles/director_popularity.pickle", "wb") as f:
    pickle.dump(dirpop(), f)

with open("Pickles/decade_genrecount.pickle", "wb") as f:
    pickle.dump(decg(), f)

with open("Pickles/actor_actress_cross.pickle", "wb") as f:
    pickle.dump(act2(), f)

with open("Pickles/actor_award.pickle", "wb") as f:
    pickle.dump(actawd(), f)
with open("Pickles/director_award.pickle", "wb") as f:
    pickle.dump(dirawd(), f)
