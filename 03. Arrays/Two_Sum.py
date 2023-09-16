#URL  : https://leetcode.com/problems/two-sum/description/

#1. Usingh hashmap.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict ()
        for i in range (len (nums)):
            if target - nums[i] in d:
                return (d[target-nums[i]], i)
            d[nums[i]] = i
        return [-1,-1]


#2 : Using loops

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]