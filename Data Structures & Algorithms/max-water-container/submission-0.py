class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_h = 0

        l,r = 0,len(heights)-1

        while l < r:

            curr_height = (r-l) * min(heights[l],heights[r])
            if curr_height > max_h:
                max_h = curr_height

            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1

        return max_h