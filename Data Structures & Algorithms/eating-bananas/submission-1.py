import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles) - 1
        min_k = float('inf')

        while l <= r:
            m = (l + r) // 2

            time = 0
            for pile in piles:
                time += int(math.ceil(pile / (m+1)))
            
            if time > h:
                l = m + 1
            elif time <= h:
                min_k = m
                r = m - 1
        
        return min_k + 1

