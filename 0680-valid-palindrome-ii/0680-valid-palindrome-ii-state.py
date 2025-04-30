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

        alternate_skip_l_choice = -1
        alternate_skip_r_choice = -1


        correction_count = 0

        while l < r and correction_count <= 2:

            if s[l] != s[r]:
                # print(f"mismatch: l at '{s[l]}', r at '{s[r]}'")

                #123456789
                #abcdedcba
#                return is_normal_palindrome((l+1),r) or is_normal_palindrome(l,(r+1))

                if correction_count == 1:
                    # redo our previous choice

                    # print(f"  alternate choice: try advancing right, correction count == {correction_count}")

                    l, r = alternate_skip_l_choice, alternate_skip_r_choice
                    correction_count += 1
                elif correction_count == 0:
                    # try skipping the left

                    # save the other choice
                    alternate_skip_l_choice = l
                    alternate_skip_r_choice = r - 1

                    l = l + 1
                    correction_count += 1
                    # print(f"  advanced left, correction count == {correction_count}")
                else:
                    # correction count is too high
                    # print("  advancement didn't help, fail")
                    return False
                
            else:
                l, r = l + 1, r - 1

        if correction_count <= 2:
            return True
        else:
            return False

