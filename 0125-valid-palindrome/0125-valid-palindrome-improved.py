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



        # start two indexes, a and b, at either end
        left = 0
        right = len(s) - 1

 

        while left < right:


            while (not s[left].isalnum()) and left < right:
                left += 1

            while (not s[right].isalnum()) and right > left:
                right -= 1

            if s[left].upper() != s[right].upper():
                return False
            
            left, right = left + 1, right - 1
            
        return True
    
        # time complexity: O(N)
        # space complexity: O(1)


