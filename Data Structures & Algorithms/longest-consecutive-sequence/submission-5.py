class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        max_len = 0

        for num in unique_nums:
            if num - 1 not in unique_nums:
                curr_len = 1
                curr = num + 1
                while curr in unique_nums:
                    curr_len += 1
                    curr += 1
            
                max_len = max(max_len, curr_len)
        
        return max_len