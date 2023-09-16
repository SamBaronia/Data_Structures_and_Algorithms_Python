#URL : https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c, maxi = 0, 0 
        for i in range (0, len (nums)):
            if nums[i] == 1:
                c += 1
                if c > maxi:
                    maxi = c
            else:
                c = 0
        return maxi
            