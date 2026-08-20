class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while l < r:
                complement = -nums[i]

                if nums[l] + nums[r] < complement:
                    l += 1
                elif nums[l] + nums[r] > complement:
                    r -= 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return triplets
        
        