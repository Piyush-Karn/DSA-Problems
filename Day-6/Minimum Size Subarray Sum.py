# Leetcode Problem Link -> https://leetcode.com/problems/minimum-size-subarray-sum/description/

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_len = float('inf')

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len

o1=Solution()
print(o1.minSubArrayLen(7,[2,3,1,2,4,3]))
print(o1.minSubArrayLen(4,[1,4,4]))
print(o1.minSubArrayLen(11,[1,1,1,1,1,1,1,1]))
