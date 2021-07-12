'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example:
Input: num1 = "11", num2 = "123"
Output: "134"
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def func(n):
            value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
            result = 0
            for digit in n:
                result = 10 * result + value[digit]

            return result

        ans = func(num1) + func(num2)
        return str(ans)