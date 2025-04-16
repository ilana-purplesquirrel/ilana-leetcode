class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Constraints:

        # 1 <= s.length <= 2 * 105
        # s consists only of printable ASCII characters.

        # edge case:
        # discuss clarifying questions!
        if len(s) == 1:
            return True

        # A phrase is a palindrome if, after converting all uppercase letters
        # into lowercase letters and removing all non-alphanumeric characters,
        # it reads the same forward and backward.
        # Alphanumeric characters include letters and numbers.

        cleaned_s = ""
        for c in s:
            if c.isalnum():
                cleaned_s += c.upper()

        # another edge case:
        if len(cleaned_s) == 1:
            return True

        # brute force:
        # create a reversed copy of the string and compare it to the orginal

        rev_s = ""
        for i in range(len(cleaned_s) - 1, -1, -1):
            rev_s += cleaned_s[i]
        
        result = True if (rev_s == cleaned_s) else False
        return result
    
        # time complexity: O(N)
        # space complexity: O(N)


