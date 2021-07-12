'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Input: s = "anagram", t = "nagaram"
Output: true
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
          
        s = sorted(s)
        t = sorted(t)
        s = "".join(s)
        t = "".join(t)
   
        if s == t:
            return True
        else:
            return False
        