def b1nary_search(lst,search_for):
	if search_for in lst:
		return True
	else:
		return False

def binary_search(lst, search_for):
    location = int(len(lst) / 2)
    while len(lst) > 1:
        if lst[location] > search_for:
            del lst[location:]
        else:
            del lst[:location]
        location = int(len(lst) / 2)
    if lst[0] == search_for:
        return True
    return False


print(b1nary_search([1, 2, 4, 8, 10, 22, 54, 69, 221], 26))
