class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v1 in enumerate(nums):
            for j,v2 in enumerate(nums[i+1:]):
                # print("nums[i+1:]")
                # print(nums[i+1:])
                # print(f"i={i},j={j+1}")
                if v1 + v2 == target:
                    return [i,j+i+1]
        
        return []

    
# [5,5]
# target = 10
# [0,1]

# nums=[3,4,5,6]
# target=7
# [0,1]