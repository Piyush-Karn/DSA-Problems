# Leetcode Problem Link -> https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True  
        return False


o1=Solution()
print(o1.increasingTriplet([1,2,3,4,5]))
print(o1.increasingTriplet([5,4,3,2,1]))
print(o1.increasingTriplet([2,1,5,0,4,6]))
print(o1.increasingTriplet([0,4,2,1,0,-1,-3]))
