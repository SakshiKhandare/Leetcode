'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
'''

class Solution:
    def addDigits(self, num: int) -> int:
        s = num
        while(True):
            n = str(s)
            s = sum([int(x) for x in n])
            if(len(str(n))==1):
                return s