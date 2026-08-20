class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = -1

        while l < r:
            if heights[l] < heights[r]:
                max_area = max(max_area, heights[l] * (r-l))
                l += 1
            else:
                max_area = max(max_area, heights[r] * (r-l))
                r -= 1
        
        return max_area
