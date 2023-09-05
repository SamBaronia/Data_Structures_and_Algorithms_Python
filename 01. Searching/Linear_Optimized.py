#the time complexity of the following Linear search program is O(Logn) - Best case

def lin (arr, x):
	left = 0
	n = len(arr)
	right = n -1

	for i in range (left ,right):
		if arr[left] == x:
			return (left+1)
		if arr [right] ==x :
			return (right + 1)
			

		left += 1
		right -= 1

	return "Not Found"

print (lin([4,6,7,42,23], 66))
