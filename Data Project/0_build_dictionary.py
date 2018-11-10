import pickle
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
# Pickle it!
def pickleit(fname,indx):
    elist={}
    for c in details:
        try:
            elist[c[indx]].append(c)
        except:
            elist[c[indx]] = [c]
    with open ("Pickles/by"+fname+".pickle","wb") as f:
        pickle.dump(elist,f)

pickleit("year",0)
pickleit("director",6)
pickleit("actor",4)
pickleit("genre",3)
pickleit("actress",5)

with open ("Pickles/details.pickle","wb") as f:
    pickle.dump(details,f)