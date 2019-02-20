# Q1
# syntax error
print "hi"

# run time error
num = int(input())
# input a


# logic error
a=3

while a>0:
	print(a)
	a+=1
# don't run this, will crash

# Q3
# try excepts
try:
	num=int(input())
except:
	print("num is actually a string!")