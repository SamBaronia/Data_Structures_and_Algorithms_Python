#Defining the function
def lin(arr, x):
	#Looping through the elements of array
	for i in range (0, len(arr)):

		#if found, return the position of the element
		if (arr[i] == x):			
			return i + 1
	#if not found, return -1
	return -1

#Driver code
arr = [4,6,33,5,8,6]
x = 8

#Calling the function and printing it

res = lin (arr, x)
print (res)