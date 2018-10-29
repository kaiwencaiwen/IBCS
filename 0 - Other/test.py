
def my_gen():
	n=0
	for i in range(10):
		n+=1
		yield n

a=my_gen()
print(next(a))
print(next(a))
print(next(a))