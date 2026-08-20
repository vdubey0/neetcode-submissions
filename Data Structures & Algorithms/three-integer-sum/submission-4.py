class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        for i in range(len(nums)):
            root = nums[i]

            seen = set()

            for j in range(i + 1, len(nums)):
                complement = -root - nums[j]

                if complement in seen:
                    triplet = tuple(sorted([root, nums[j], complement]))
                    triplets.add(triplet)
                else:
                    seen.add(nums[j])

        return [list(t) for t in triplets]
