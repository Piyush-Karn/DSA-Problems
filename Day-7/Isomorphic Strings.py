# Leetcode Problem Link -> https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


# Test cases
o1 = Solution()
print(o1.isIsomorphic(s = "egg", t = "add"))     # True
print(o1.isIsomorphic(s = "foo", t = "bar"))     # False
print(o1.isIsomorphic(s = "paper", t = "title")) # True

