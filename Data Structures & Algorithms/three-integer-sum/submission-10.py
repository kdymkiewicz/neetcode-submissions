# O(n^3) time complexity solution

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
        # triplets = set()

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 triplets.add(tuple(sorted([nums[i],nums[j],nums[k]])))


        # return [list(t) for t in triplets]


# Sorting plus two pointers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        triplets = set()

        for i in range(len(nums)):
            
            num = nums[i]
            l,r = i+1, len(nums)-1

            while l < r:

                curr_sum = num + nums[l] + nums[r]
                if curr_sum == 0:
                    triplets.add((num,nums[l],nums[r]))
                    l += 1
                    r -= 1
                
                if curr_sum > 0:
                    r -= 1

                if curr_sum < 0:
                    l += 1

        return [list(triplet) for triplet in triplets]


