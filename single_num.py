'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example:
Input: nums = [4,1,2,1,2]
Output: 4
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        res = []

        for i in range(len(nums)):
            if nums[i] not in res:
                res.append(nums[i])
            else: 
                res.remove(nums[i])

        return res[0]