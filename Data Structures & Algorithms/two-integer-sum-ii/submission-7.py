class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute force

        # for j in range(len(numbers)):
        #     for k in range(j+1,len(numbers)):
        #         if numbers[j]+numbers[k] == target:
        #             # since its 1 indexed, then shift +1
        #             return [j+1,k+1]

        # return []

        # Two pointer solution. 
        # This leverages the fact that the array is sorted.

        l,r = 0, len(numbers)-1

        while l != r:

            cur_sum = numbers[l]+numbers[r]

            if cur_sum < target:
                l += 1
            elif cur_sum > target:
                r -= 1
            else:
                return [l+1,r+1]
        
        return []




