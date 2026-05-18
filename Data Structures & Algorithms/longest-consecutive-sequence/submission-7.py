class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        numbers_set = set(nums)

        for starting_number in nums:
            current_streak = 0
            current_number = starting_number

            while current_number in numbers_set:
                current_streak += 1
                current_number += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak