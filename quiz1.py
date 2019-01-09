def asoy(A):
	q = sorted(A)
	a = 1
	for items in q:
		if items == a:
			a += 1
		elif items > a:
			pass
	return a


arr = [3,-2,99,-1,0,4,1,2,8,5]

print(asoy(arr))