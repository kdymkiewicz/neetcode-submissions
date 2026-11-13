class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past_n_i = {}

        for i,n in enumerate(nums):
            diff = target-n

            if diff in past_n_i:
                return [past_n_i[diff],i]
            
            past_n_i[n]=i

        return []