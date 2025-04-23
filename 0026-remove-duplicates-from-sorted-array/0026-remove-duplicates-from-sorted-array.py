class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # edge case:
        if len(nums) == 1:
            return 1

        lastval = nums[0]
        inpos = 1
        writepos = 1
        while inpos < len(nums):
            if nums[inpos] == lastval:
                # nothing to write
                pass
            else:
                lastval = nums[inpos]
                nums[writepos] = lastval
                writepos += 1
            
            inpos += 1
        
        return writepos