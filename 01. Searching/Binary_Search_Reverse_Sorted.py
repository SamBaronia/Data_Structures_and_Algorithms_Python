def Binarysearch(arr, x):
	start = 0
	end = len (arr) - 1

	while start <= end :
		mid = start + (end - start)//2

		if arr[mid] == x:
			return mid + 1

		if arr[mid] > x:
			start = mid + 1

		else:
			end = mid - 1
	return -1 

arr = [15,11,10,9,8,6,4,3,2]
print (Binarysearch(arr, 2))