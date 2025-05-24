# LeetCode Problem: https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outputList = []

        # Check every pair of numbers in the list
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # If the sum of the pair equals the target, store their indices
                if nums[i] + nums[j] == target:
                    outputList.append(i)
                    outputList.append(j)
        
        return outputList

# Example usage
o1 = Solution()
print(o1.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
