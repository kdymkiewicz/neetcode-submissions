class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} # we store remaining target as key, and index of the number as value
        for i,n in enumerate(nums):
            # If current number is in the dict, meaning the current number == remaining value
            if n in d:
                # return the indices, starting from the earlier one, then the current one
                return [d[n],i]
            
            # update the dict with a remaining value as the key and index as value
            d[target-n] = i
        
        return []