# modified from NeetCode:
# O(N^2) time

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        for i in range(len(s)):
            count, max_freq = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                max_freq = max(max_freq, count[s[j]])
                #if count[s[j]] > max_freq:
                #    max_freq = count[s[j]]

                cur_window_len = (j - i + 1)
                cur_num_subsitutions_needed = cur_window_len - max_freq
                # AABABBA
                # i=0, j=6
                # max_freq (A) was 4
                # cur_window_len is 7
                # number of substitutions needed is 3
                if cur_num_subsitutions_needed <= k:
                    result = max(result, cur_window_len)
        return result

