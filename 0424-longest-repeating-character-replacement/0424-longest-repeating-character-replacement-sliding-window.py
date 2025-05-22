# modified from NeetCode
# O(N) time
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        
        l = 0
        max_freq = 0
        for r in range(0,len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])
            #if count[s[j]] > max_freq:
            #    max_freq = count[s[j]]

            cur_window_len = (r - l + 1)
            cur_num_substitutions_needed = cur_window_len - max_freq
            while cur_num_substitutions_needed > k:
                count[s[l]] -= 1
                l += 1
            
            # we have potentially moved l towards the end of the string,
            # so we need to recalcuate the current window length:
            new_window_len = (r - l + 1)
            
            result = max(result, new_window_len)

        return result




