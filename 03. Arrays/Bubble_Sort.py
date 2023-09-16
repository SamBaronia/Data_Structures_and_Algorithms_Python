#URL = https://practice.geeksforgeeks.org/problems/bubble-sort/1

#User function Template for python3
def bubbleSort(self,arr, n):
    # code here
    for i in range (n):
        maxi = n-1 
        for j in range (0, maxi):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+ 1] = arr[j+ 1], arr[j]
            maxi -= 1
    return arr