class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            if j != len(nums) - 1:
                postfix *= nums[j+1]
            
            res[j] = postfix * prefix[j]
        
        return res
