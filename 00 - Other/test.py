thenum=int(input())
# J = int(input())
# print (int(((J-1)*(J-2)*(J-3))/6))
if thenum<=5:
	left=thenum
	right=0
else:
	left=5
	right=thenum-5

count=0
while left>=right:
	count+=1
	left-=1
	right+=1

print(count)