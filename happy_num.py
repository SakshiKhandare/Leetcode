'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def func(num):    
            rem = sum = 0;    

            #Calculates the sum of squares of digits    
            while(num > 0):    
                rem = num%10;    
                sum = sum + (rem*rem);    
                num = num//10;    
            return sum;  
    
        result = n;    

        while(result != 1 and result != 4):    
            result = func(result);    

        #Happy number always ends with 1    
        if(result == 1):    
            return True 
        #Unhappy number ends in a cycle of repeating numbers which contain 4    
        elif(result == 4):    
            return False 