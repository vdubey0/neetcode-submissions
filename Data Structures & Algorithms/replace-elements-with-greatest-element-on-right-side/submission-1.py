class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        curr_max = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            res[i] = curr_max
            curr_max = max(curr_max, arr[i])

        return res