# from NeetCode
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # example: abcaekcisn2cbc58pwabcabcbbwkewabcababcabcbbcbb
            #                       l     r 
            #            r  l
            # r and l are the fence "sections"
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
