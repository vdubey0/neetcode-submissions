class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        k = len(nums)


        while i <= j:
            if nums[j] == val:
                j -= 1
                k -= 1
                continue

            if nums[i] == val:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                j -= 1

                k -= 1
            
            i += 1

        return k
