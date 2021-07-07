'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for n in nums:
            if n==0:
                max_count = max(count,max_count)
                count = 0
            else:
                count = count + 1
                
        return max(count,max_count)