# LeetCode Problem: https://leetcode.com/problems/container-with-most-water/description/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h * w)

            # Move the pointer that has the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

o1 = Solution()
print(o1.maxArea([1,8,6,2,5,4,8,3,7]))
print(o1.maxArea([1,1]))