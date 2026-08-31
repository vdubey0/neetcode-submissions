class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak = 0
        max_streak = 0

        for num in nums:
            if num == 1:
                streak += 1
                max_streak = max(streak, max_streak)
            else:
                streak = 0

        return max_streak