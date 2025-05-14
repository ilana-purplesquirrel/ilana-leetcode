# in-class solution

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        #edge cases

        # if k is zero, there's no way to fit a pair of numbers in the window:
        if k == 0: return False

        # if the list is too small, there's no room for finding a pair of numbers at all
        if len(nums) <= 1: return False


        # (now we can assume that the list is >= len 2)

        # keep track of numbers in the window inside of a set:
        window = set()
        window_size = k
        # set up a loop i from 0 through len(nums):
        for i in range(0, len(nums)):
            #print(window)
            cur_val = nums[i]
            # if cur_val is in the window: return True
            if cur_val in window:
                return True

            #   ex [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
            if len(window) >= window_size:
                # remove the previous first value of the set, which would be nums[i-window_size]
                window.remove(nums[i-window_size])

            # add a new value: window.add(nums[i])
            window.add(nums[i])

        # return false if we get here
        return False


