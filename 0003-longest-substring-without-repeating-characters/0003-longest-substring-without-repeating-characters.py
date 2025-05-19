class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        l, r = 0, 1
        chars = {}
        chars[s[l]] = l
        max_len = 0

        while r < len(s):
            cur_char = s[r]
            if cur_char not in chars:
                chars[cur_char] = r
                r += 1
                max_len = max(max_len, r-l)
            else:
                # reset to last seen char position
                l = chars[cur_char] + 1
                r = l
                chars = {}

        return max_len