#Leetcode Problem Link :- https://leetcode.com/problems/maximum-average-subarray-i/description/
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowsum = sum(nums[:k])
        maxavg = windowsum/k
        for i in range(k,len(nums)):
            windowsum += nums[i] - nums[i-k]
            maxavg=max(maxavg,windowsum/k)
        return maxavg

o1=Solution()
print(o1.findMaxAverage([1,12,-5,-6,50,3],4))
