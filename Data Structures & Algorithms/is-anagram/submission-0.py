def dict_from_str(s):
    d = dict()
    for i in s:
        d[i] = d.get(i,0)+1
    
    return d


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = dict_from_str(s)        
        dt = dict_from_str(t)

        return ds == dt