class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for j in range(len(numbers)):
            for k in range(j+1,len(numbers)):
                if numbers[j]+numbers[k] == target:
                    # since its 1 indexed, then shift +1
                    return [j+1,k+1]

        return []