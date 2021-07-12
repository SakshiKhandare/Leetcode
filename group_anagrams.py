'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            sortedWord = ''.join(sorted(s))
            if sortedWord not in res:
                res[sortedWord] = [s]
            else:
                res[sortedWord].append(s)
                
        final_res = []
        for val in res.values():
            final_res.append(val)
        
        return final_res
        