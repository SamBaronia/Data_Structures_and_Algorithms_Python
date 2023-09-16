class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #Taking first element as our Pivot and that's why starting our loop from 
        #second element of the array
        for i in range (1, len (nums)):

            #Adding it with the previous value and replacing element of the array

            nums[i] = nums[i] + nums[i-1]
            
        return nums