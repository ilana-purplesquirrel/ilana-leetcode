class Solution:
    def validPalindrome(self, s: str) -> bool:

    
        # TODO ! fails at
        # "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"

        
        if len(s) == 1:
            return True
        
        l, r = 0, len(s) - 1
        correction_count = 0

        while l < r and correction_count <= 1:

            if s[l] != s[r]:
                print(f"mismatch: l at '{s[l]}', r at '{s[r]}'")
                # try skipping the left, then the right
                if s[l+1] == s[r]:
                    l += 1
                    correction_count += 1
                    print(f"  advanced left, correction count == {correction_count}")
                elif s[l] == s[r-1]:
                    r -= 1
                    correction_count += 1
                    print(f"  advanced right, correction count == {correction_count}")
                else:
                    print("  advancement didn't help, fail")
                    return False
            else:
                l, r = l + 1, r - 1

        if correction_count <= 1:
            return True
        else:
            return False


