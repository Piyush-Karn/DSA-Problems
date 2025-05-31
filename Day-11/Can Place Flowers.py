# Leetcode Problem Link -> https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True  

        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0 or flowerbed[i - 1] == 0)
                empty_right = (i == length - 1 or flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True

        return n == 0

        


o1=Solution()
print(o1.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(o1.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
print(o1.canPlaceFlowers(flowerbed = [1,0,1,0,1,0,1], n = 1))
print(o1.canPlaceFlowers(flowerbed = [1,0,1,0,1,0,1], n = 0))
print(o1.canPlaceFlowers(flowerbed = [1,0,0,0,1,0,1], n = 1))
print(o1.canPlaceFlowers(flowerbed = [0,0,1,0,1], n = 1))

