'''
Count the number of prime numbers less than a non-negative number, n.

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

def isPrime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

class Solution:
    def countPrimes(self, n: int) -> int:
        c = 0
        for i in range(2,n):
            if isPrime(i):
                c = c+1
                #primes.append(i)

        return c
        #print(primes)