# Leetcode Problem Link -> https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1,word2=list(word1),list(word2)
        merged=[]
        mini = min(len(word1),len(word2))
        
        for i in range(mini):
            merged.append(word1[i])
            merged.append(word2[i])
        
        if mini == len(word1) and mini == len(word2):

            return "".join(merged)
        elif mini == len(word1):
            return "".join(merged[:] + word2[mini:])

        elif mini == len(word2):
            return "".join(merged[:] + word1[mini:])

o1=Solution()
print(o1.mergeAlternately(word1 = "abc", word2 = "pqr"))
print(o1.mergeAlternately(word1 = "ab", word2 = "pqrs"))
print(o1.mergeAlternately( word1 = "abcd", word2 = "pq"))
