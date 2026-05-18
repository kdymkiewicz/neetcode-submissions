class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = []
        for i in range(len(nums)):
            p = 1
            for j in range(len(nums)):
                if i != j:
                    p = p * nums[j]
            prod.append(p)
        
        return prod