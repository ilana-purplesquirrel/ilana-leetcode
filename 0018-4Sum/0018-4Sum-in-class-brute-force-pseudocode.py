class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    



    # sample output: [ [1,3,6,2], [3,45,23,42] ]

    # error handling: if we have less than len 4, error


# [1,0,-1,0,-2,2]
#       ^ _  _ _ 

    # brute-force:
    # use for loops:
    # one outer loop and 3 inner loops

    # for a from 0 through length of nums (len(n) - 4) -- we don't need to go through the entire array, because we need at least 3 more elements after this one for b, c, d: O(n)

    #   for b from index 1 -> len - 3: O(n)
    #      for c from index 2 -> len-2 : O(n)
    #         for d from index 3 -> len-1: 
    #           O(n-1) -> O(n) 
    #           use a set to store quadruplets

# O(n^4) means: even for our limited input len <= 200, we are looking at least 1,600,000 steps!
