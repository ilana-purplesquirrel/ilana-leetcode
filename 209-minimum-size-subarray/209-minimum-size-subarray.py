# modified from NeetCode

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, cur_window_sum_total = 0, 0
        smallest_window_len = float("inf")

        # target = 6
        # [2,3,1,2,4,3]
        for r in range(0,len(nums)):
            cur_window_sum_total += nums[r]
            while cur_window_sum_total >= target:
                cur_window_len = r - l + 1
                smallest_window_len = min(cur_window_len, smallest_window_len)
                cur_window_sum_total -= nums[l]
                l += 1

        return 0 if smallest_window_len == float("inf") else smallest_window_len
    