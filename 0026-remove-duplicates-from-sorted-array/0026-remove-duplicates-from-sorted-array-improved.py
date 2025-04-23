class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ln = len(nums)

        # edge case:
        if ln == 1:
            return 1

        lastval = nums[0]
        inpos = 1
        writepos = 1

        for inpos in range(1,ln):
            
            if nums[inpos] != lastval:
                lastval = nums[inpos]
                nums[writepos] = lastval
                writepos += 1

        
        return writepos