def bigfunc():
	def smallfunc(a):
		return("hello"+a)
	return smallfunc

print(bigfunc()("hihi"))