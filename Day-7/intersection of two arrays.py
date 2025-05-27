# Leetcode Problem Link -> https://leetcode.com/problems/intersection-of-two-arrays-ii/
from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        result = []
        
        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1
                
        return result

# Test cases
o1 = Solution()
print(o1.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))        
print(o1.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))    
print(o1.intersect([3,1,2], [1,1]))                          
