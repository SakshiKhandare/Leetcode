'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.

Example:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3
'''

class Solution:
    def isUgly(self, n: int) -> bool:
        if(n<=0):
            return False
        if(n==1):
            return True
        while(n>1):
            if(n%2==0):
                n=n/2
            elif(n%3==0):
                n=n/3
            elif(n%5==0):
                n=n/5
            else:
                return False
        return True