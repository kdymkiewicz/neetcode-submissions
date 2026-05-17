# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         freq = {}

#         for n in nums:
#             freq[n] = freq.get(n,0)+1
        
#         return list(dict(sorted(freq.items(),key=lambda t:-t[1])).keys())[:k]
        
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []

        for num in count.keys():
            # Frequency first, then the number because comparison of tulpes is left to right
            heapq.heappush(heap, (count[num], num))

            if len(heap) > k:
                # remove the smallest frequency 
                heapq.heappop(heap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res