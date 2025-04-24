class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i1 in range(0,len(numbers)):
            cur1 = numbers[i1]
            for i2 in range(1,len(numbers)):
                if cur1 + numbers[i2] == target:
                    return[i1+1, i2+1]
        
        return [0,0]