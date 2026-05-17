def get_n(s):
    ri = s.find(">")

    n = s[1:ri]
    return int(n), len(n)+2


class Solution:

    def encode(self, strs: List[str]) -> str:
        e_str = ""

        for s in strs:
            n = len(s)
            e_str += "<"+str(n)+">"+s

        return e_str

    def decode(self, s: str) -> List[str]:
        decoded = []
        if s:
            n,offset = get_n(s)

            decoded.append(s[offset:n+offset])

            rem = s[n+offset:]

            while len(rem) > 0:
                n,offset = get_n(rem)
                decoded.append(rem[offset:n+offset])

                rem = rem[n+offset:]
        
        return decoded
