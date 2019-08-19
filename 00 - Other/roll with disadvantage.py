from random import random

def rollwithd(trials,disd):
	sum=0
	for n in range(trials):
		min=random()
		for d in range(disd-1):
			q=random()
			if q<min:
				min=q
		sum+=min
	return (sum/trials)

for n in range(1,10):
	print("Average lowest of",n, "rolls: ",end="")
	print(rollwithd(1000000,n))

# advantage
def rollwitha(trials,ad):
	sum=0
	for n in range(trials):
		max=random()
		for d in range(ad-1):
			q=random()
			if q>max:
				max=q
		sum+=max
	return (sum/trials)

for n in range(1,10):
	print("Average highest of",n, "rolls: ",end="")
	print(rollwitha(1000000,n))