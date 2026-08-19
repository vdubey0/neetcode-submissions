import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        unique_elements = list(counts.keys())
        heap = [(counts[val], val) for val in unique_elements[:k]]
        heapq.heapify(heap)

        for i in range(k, len(unique_elements)):
            val = unique_elements[i]
            heapq.heappushpop(heap, (counts[val], val))
        
        return [item[1] for item in heap]