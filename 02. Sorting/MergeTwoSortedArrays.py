def Mergetwosorted(arr1, arr2):
	i =0
	j = 0
	l1 = len (arr1)
	l2 = len (arr2)
	arr =[]
	while (i < l1 and j < l2):
		if arr1[i] < arr2[j]:
			arr.append(arr1[i])
			i += 1
		else:
			arr.append(arr2[j])
			j += 1
	while i < l1:
		arr.append(arr1[i])
		i += 1

	while j < l2 :
		arr.append(arr2[j])
		j += 1
	return arr
	
arr1 = [1,3,6,9]
arr2 = [2,3,5,7]

print (Mergetwosorted(arr1, arr2))