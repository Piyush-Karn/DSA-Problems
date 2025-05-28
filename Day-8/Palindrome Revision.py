# Leetcode Problem Link -> https://leetcode.com/problems/palindrome-number/description/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        return x == x[::-1]

o1=Solution()
print(o1.isPalindrome(121))
print(o1.isPalindrome(-121))
print(o1.isPalindrome(10))