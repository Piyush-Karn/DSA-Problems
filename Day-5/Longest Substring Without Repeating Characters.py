# Leetcode Problem Link -> https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        s=list(s)
        win=[]
        for i in range(len(s)):
            if s[i] not in win:
                win.append(s[i])
    
            elif s[i] in win:
                index = win.index(s[i])
                win = win[index + 1:]  
                win.append(s[i])
            max_length=max(max_length,len(win))

        return max_length

o1 = Solution()
print(o1.lengthOfLongestSubstring("abcabcbb"))
print(o1.lengthOfLongestSubstring("bbbbb"))
print(o1.lengthOfLongestSubstring("pwwkew"))