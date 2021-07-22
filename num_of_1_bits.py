'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        #print(n)
        one_count = 0
        for i in n:
            if i == "1":
                one_count+=1
        return one_count