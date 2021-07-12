'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example:
Input: num1 = "123", num2 = "456"
Output: "56088"
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def func(n):
            value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
            result = 0
            for digit in n:
                result = 10 * result + value[digit]

            return result

        ans = func(num1) * func(num2)
        return str(ans)