# Leetcode Problem Link -> https://leetcode.com/problems/valid-anagram/
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        sets=set(s)
        for i in sets:
            if s.count(i)!=t.count(i):
                return False
        return True               
