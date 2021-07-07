'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Example:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        
        start=1
        end=x
        ans = 0

        while(start<=end):
            mid = start + (end-start)//2
            if mid<=x/mid:
                ans = mid
                start = mid+1
            else:
                end = mid-1
                
        return int(ans)
