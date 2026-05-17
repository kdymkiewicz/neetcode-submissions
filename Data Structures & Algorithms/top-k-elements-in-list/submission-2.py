class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)

        return [num for num, freq in sorted_items[:k]]

# # heap queue version
# from typing import List
# import heapq

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}

#         for num in nums:
#             count[num] = 1 + count.get(num, 0)

#         heap = []

#         for num in count.keys():
#             # Frequency first, then the number because comparison of tulpes is left to right
#             heapq.heappush(heap, (count[num], num))

#             if len(heap) > k:
#                 # remove the smallest frequency 
#                 heapq.heappop(heap)

#         res = []

#         for i in range(k):
#             res.append(heapq.heappop(heap)[1])

#         return res