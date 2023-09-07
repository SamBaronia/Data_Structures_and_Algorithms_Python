def QuickSort(arr):

	if len(arr) <= 1:
		return arr
	else:
		pivot = arr.pop()
	
	larger = []
	smaller = []

	for i in arr:
		if i > pivot:
			larger.append(i)

		else:
			smaller.append(i)

	return QuickSort(smaller) + [pivot] + QuickSort(larger)

arr = [3,5,3,1,45,7,21,3,5,67,7,3,2,1,3,5,7,63,32,41324,2,1,1,1,1]
print (QuickSort(arr))