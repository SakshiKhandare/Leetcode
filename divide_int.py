'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.

Example:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
'''

import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend*divisor < 0:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
     
        val=0
        while (dividend >= divisor):
            dividend -= divisor
            val += 1
            
        if val == 2**31:
            return 2**31-1
        return int(math.trunc(sign*val))