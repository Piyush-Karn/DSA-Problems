#Leetcode Problem Link :- https://leetcode.com/problems/check-if-n-and-its-double-exist/

from typing import List
class Solution():
    def checkIfExist(self, arr: List[int]) -> bool:
        myset = set()
        for i in range(0,len(arr)):
            if 2*arr[i] in myset or (arr[i]%2 == 0 and arr[i]//2 in myset) :
                return True
            myset.add(arr[i])
        return False

