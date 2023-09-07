def bubble(arr, n):
	for i in range (n):
		max_ind = n-1
		for j in range (0, max_ind):
			if arr[j] < arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
			max_ind = max_ind -1
	return arr 
arr=[2,5,1,1,1,1,1,3,6,7,1,2000,200]
print (bubble(arr, len (arr))) 
