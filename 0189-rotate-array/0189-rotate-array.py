class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        # rotating by the length of the array is the same as rotation by 0; no effect

        # modulo operator:
        # example: len == 7, k=52
        # 52 / 7, what's the remainer?
        # 52 % 7 = 3

        # idea: split the orginal nums array
        # into two arrays:
        # ex: nums = [1,2,3,4,5,6,7]
        # k=3
        # s1 first split: from nums[-3:]
        # ex: [5:]
        # s2 second spilt: from nums[0:4]
        # [1, 2, 3, 4]

        # now that we have two splits:
        # add first split to the second:
        # s1 + s2
        # [5, 6, 7, 1, 2, 3, 4]



        # algorithm:

        # [-1,-100,3,99]
        # k=2
        # kmod = len(nums) % k
        # kmod = 2
        kmod = k % len(nums)
        #print(kmod)
        # s1 = nums[-kmod:]
        s1 = nums[-kmod:]
        #print(s1)
        # s2 = nums[0:kmod]
        s2 = nums[0:-kmod]
        #print(s2)
        # nums = s1+s2
        temp = s1+s2
        nums[:] = temp[:]
