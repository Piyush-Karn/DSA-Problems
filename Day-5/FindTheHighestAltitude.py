#Leetcode Problem Link :- https://leetcode.com/problems/find-the-highest-altitude/description/
from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0,0)
        HighestAlt=0
        currentalt=sum(gain[:2])
        HighestAlt=max(HighestAlt,currentalt)
        for i in range(2,len(gain)):
            currentalt += gain[i]
            HighestAlt=max(HighestAlt,currentalt)
        return HighestAlt

