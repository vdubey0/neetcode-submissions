class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                pop_ix, pop_temp = stack.pop()
                res[pop_ix] = (i - pop_ix)

            stack.append((i, temp))

        return res