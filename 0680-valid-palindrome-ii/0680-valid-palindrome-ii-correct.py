class Solution:
    def validPalindrome(self, s: str) -> bool:



        if len(s) == 1:
            return True
        
        def is_normal_palindrome(l:int, r:int):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True


        l, r = 0, len(s) - 1
        # correction_count = 0

        while l < r:# and correction_count <= 1:

            if s[l] != s[r]:
                # print(f"mismatch: l at '{s[l]}', r at '{s[r]}'")
                # try skipping the left, then the right

                #123456789
                #abcdedcba
#                return is_normal_palindrome((l+1),r) or is_normal_palindrome(l,(r+1))

                if is_normal_palindrome((l+1),r):
                    # print(f"  advanced left, correction count == {correction_count}")
                    # correction_count += 1
                    return True
                elif  is_normal_palindrome(l,(r-1)):
                    # print(f"  advanced right, correction count == {correction_count}")
                    # correction_count += 1
                    return True
                else:
                    # print("  advancement didn't help, fail")
                    return False
            else:
                l, r = l + 1, r - 1

        # if correction_count <= 1:
        #     return True
        # else:
        #     return False

        return True
