lil = [4, -2, 2, 9, 5, 4, 3, 2, 1, 0, 8]


def bubblesort(lst):

	loops = 0
	tosort = len(lst) - 1
	while loops != len(lst):
		ind = 0
		swapped = False
		while ind != tosort:
			if lst[ind] > lst[ind + 1]:
				swapped = True
				k = lst[ind]
				lst[ind] = lst[ind + 1]
				lst[ind + 1] = k
			ind += 1
		if not swapped:
			break
		loops += 1
		tosort -= 1
	return lst


print(bubblesort(lil))


def selectionsort(lst):
	for startp in range(len(lst)):
		mindex = startp
		for n in range(startp,len(lst)):
			if  lst[mindex]> lst[n]:
				mindex = n
		lst[startp], lst[mindex] = lst[mindex], lst[startp]
	return lst


lil = [0, 3, 5, 225, 84, 36, 1, 6]
print(selectionsort(lil))


lil=[5,3,3,5,23,51,34,20,0,3,1]

def insertionsort(lst):
	for startp in range(1,len(lst)):
		startval=lst[startp]
		compp=startp-1
		while startval<lst[compp] and compp>=0:
			lst[compp+1]=lst[compp]
			compp-=1
		lst[compp+1]=startval
	return lst
print(insertionsort(lil))