# Leetcode Problem Link -> https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''

        def compute_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        len_gcd = compute_gcd(len(str1), len(str2))

        return str1[:len_gcd]

        
o1 = Solution()
print(o1.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(o1.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
print(o1.gcdOfStrings(str1 = "LEET", str2 = "CODE"))