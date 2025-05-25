#Leetcode Problem Link -> https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")  
        maxv = 0
        count = 0

        # First window of size k
        for i in range(k):
            if s[i] in vowels:
                count += 1
        maxv = count

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            maxv = max(maxv, count)

        return maxv

