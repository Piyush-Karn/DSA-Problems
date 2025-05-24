from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outputList=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    outputList.append(i)
                    outputList.append(j)
        return outputList

o1 = Solution()
print(o1.twoSum([2,7,11,15],9))

