def select(arr, n):
	for i in range(0, n):
		mini = i
		for j in range (i +1, n):
			if arr[j] < arr [mini]:
				mini = j
		arr[i], arr[mini] = arr[mini], arr[i]
	return arr

print(select([2,3,6,1,3,4], 6))