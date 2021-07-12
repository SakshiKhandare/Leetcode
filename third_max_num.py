'''
Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

Example:
Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        
        if len(nums) > 2:
            res = nums[-3]
        else:
            res = max(nums)
    
        return res