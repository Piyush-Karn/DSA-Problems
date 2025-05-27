# Leetcode Problem Link -> https://leetcode.com/problems/first-unique-character-in-a-string/description/

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1=Counter(s)
        for i in dict1.keys():
            if dict1[i] == 1:
                return s.index(i)
        return -1

o1 = Solution()
print(o1.firstUniqChar("leetcode"))
print(o1.firstUniqChar("loveleetcode"))
print(o1.firstUniqChar("aabb"))