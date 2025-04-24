class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # target = 9

        # 2, 7, 11, 15
        # l         r
        
        # we got 17
        
        # l      r
        # 13: still too big

        # l  r
        # 2+7 = 9, success, return

        # sort l, r? No! already sorted!

        # -----

        # initial phase / setup
        # two pointers, l and r
        # start l = 0, r at the other end, = len(nums)-1
        l=0
        r=len(numbers)-1


        # while loop-- while l < r
        while l<r:
        #   does l+r == target?
        #   (Check if the number at left position + number at right position == target)
            cur_sum = numbers[l] + numbers[r]
            if cur_sum == target:

        #      true: 
        #           return a list with l+1 and r+1
                return [l+1, r+1]

        #      false:
            else:
        #           Check if the sum is less than / equal to the target
                if cur_sum <= target:
        #               less:
        #                   Left += 1
                    l += 1

        #               greater:
                else:
        #                   right -= 1
                    r -= 1 

        # return [] (optional, we know we'll never get here)
        return []


        # ------
        # target=9
        # 2, 7, 7, 11, 15
        # l            r
        # l         r
        # l     r
        # (return)

        # O(kn)
        # k * O(n)
        # O(n)

        # O(n/2)
        # 1/2 * O(n)
        # O(n)



         