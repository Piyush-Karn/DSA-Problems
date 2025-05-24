# LeetCode Problem: https://leetcode.com/problems/container-with-most-water/description/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxvol = 0  # Stores the maximum area found

        # Try all possible pairs of lines (brute-force approach)
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                # Water is limited by the shorter line
                minheight = min(height[i], height[j])

                # Width is the horizontal distance between lines
                width = j - i

                # Area = minheight * width
                temp = minheight * width

                # Update max area if current is greater
                maxvol = max(maxvol, temp)

        return maxvol

        # Time Complexity: O(n^2)
        # This brute-force approach checks all combinations of line pairs.
        # It works for small inputs but is inefficient for large lists
        # and will cause a TLE (Time Limit Exceeded) on LeetCode.
