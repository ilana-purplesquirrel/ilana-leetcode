# in-class O(N^2)



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # edge cases
        if len(s) == 1:
            return 1

        if len(s) == 0:
            return 0

        # setup
        max_len = 0
        cur_len = 0
        seen = {}

        # example: abcaekcisn2cbcbbpwabcabcbbwkewabcababcabcbbcbb

        for i in range(0,len(s)):
            seen = {}
            seen[ s[i] ] = 1
            cur_len = 1
            for j in range(i+1, len(s)):
                if s[j] not in seen:
                    seen[ s[j] ] = 1
                    cur_len += 1
                else:
                    break
            
            max_len = max(max_len, cur_len)

        return max_len

