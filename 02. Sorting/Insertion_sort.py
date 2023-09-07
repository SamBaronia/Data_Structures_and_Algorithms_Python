def insertion(arr, n):
	for i in range (1, n):
		j = i
		while arr[j-1] > arr [j] and j >0:
			arr[j] , arr[j-1] = arr [j-1], arr[j]
			j -= 1

	return arr

print(insertion([2,3,6,1,3,4], 6))