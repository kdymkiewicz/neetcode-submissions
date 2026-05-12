from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for s in strs:
            f = tuple(sorted(s))
            groups[f].append(s)
            
        return list(groups.values())