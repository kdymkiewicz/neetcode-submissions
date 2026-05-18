class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        unique = set(nums)
        sorted_unique = sorted(list(unique))

        print(sorted_unique)

        last = sorted_unique[0] 
        counter = 1
        max_l = []

        for n in sorted_unique[1:]:
            if last+1!=n:
                print("reset")
                print('current counter: ')
                print(counter)
                max_l.append(counter)
                counter = 1
            else:
                print(n)
                print("counter ++")
                counter += 1             

            last = n
        
        max_l.append(counter)

        return max(max_l)

