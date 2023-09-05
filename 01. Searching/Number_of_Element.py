def first(arr, x):

	start = 0
	end = len (arr)- 1
	first = -1
	while start <= end :

		mid = start + (end - start)//2
		if arr[mid] == x:
			first = mid
			end = mid - 1
		elif arr[mid] > x:
			end = mid - 1
		else:
			start = mid + 1
	return first 

def last(arr, x):
	start = 0
	end = len (arr)- 1
	last = -1
	while start <= end :
		mid = start + (end - start)//2
		if arr[mid] == x:
			last = mid
			start = mid + 1
		elif arr[mid] > x:
			end = mid - 1

		else:
			start = mid + 1
	return last +1 


arr = [1,2,3,5,5,5,11,11,11,11,11,11,11,11,11,11]
print (last (arr, 11) - first (arr, 11))