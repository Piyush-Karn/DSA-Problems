# Leetcode Problem Link -> https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)

# Test Cases
o1 = Solution()
print(o1.reverseWords(s="the sky is blue"))              
print(o1.reverseWords(s="  hello world  "))            
print(o1.reverseWords(s="a good   example"))             
print(o1.reverseWords(s="  Bob    Loves  Alice   "))     
