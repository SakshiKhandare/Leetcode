'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :
Input: nums = [1,2,3,1]
Output: true
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i) 
        return False