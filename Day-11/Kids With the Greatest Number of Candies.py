# Leetcode Problem Link -> https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        result = []
        for i in candies:
            if (i + extraCandies) >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result

o1=Solution()
print(o1.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
print(o1.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))
print(o1.kidsWithCandies(candies = [12,1,12], extraCandies = 10))