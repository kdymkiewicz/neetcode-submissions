class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i,v1 in enumerate(nums):
        #     for j,v2 in enumerate(nums[i+1:]):
        #         if v1 + v2 == target:
        #             return [i,j+i+1]
        
        # return []

        past_n_i = {}

        for i,n in enumerate(nums):
            diff = target-n

            if diff in past_n_i:
                return [past_n_i[diff],i]
            
            past_n_i[n]=i

        return []