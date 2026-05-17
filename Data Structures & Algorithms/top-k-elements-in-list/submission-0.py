class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for n in nums:
            freq[n] = freq.get(n,0)+1
        
        return list(dict(sorted(freq.items(),key=lambda t:-t[1])).keys())[:k]
        