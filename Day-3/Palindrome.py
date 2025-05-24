# LeetCode Problem: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers can't be palindrome because of the '-' sign
        if x < 0:
            return False
        
        # Convert the number to a string to compare easily
        str_x = str(x)
        
        # Check if the string is the same forwards and backwards
        return str_x == str_x[::-1]
