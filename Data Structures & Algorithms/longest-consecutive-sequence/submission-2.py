class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_elements = set(nums)
        max_streak = 0

        for num in unique_elements:
            if num - 1 not in unique_elements:
                streak = 1
                curr = num + 1
                while curr in unique_elements:
                    curr += 1
                    streak += 1
                
                max_streak = max(streak, max_streak)
        
        return max_streak