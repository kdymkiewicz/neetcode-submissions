class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1:
            return 1
        
        max_l = 0

        for i in range(len(s)):
            for j in range(i,len(s)):

                sub_s = s[i:j+1]
                if len(set(sub_s)) == len(sub_s):
                    max_l = max(max_l,len(sub_s))
        
        return max_l