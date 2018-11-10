import pickle

with open ("Pickles/actor_actress_cross.pickle","rb") as f:
    actor_actress=pickle.load(f)
print(actor_actress)