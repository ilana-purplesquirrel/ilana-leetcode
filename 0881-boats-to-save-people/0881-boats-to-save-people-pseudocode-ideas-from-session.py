class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # initialy: sort input
        # we'll use sort(); O(n log(n)) time complexity; O(1) space

        #[3,5,3,4] -> 
        #[3,3,4,5], limit 5

        # compare the values to the limit;
        # start with the largest value;
        # if you can, add the smallest value
        # otherwise, assign the large value to one boat

        # Can start with two pointers. One at the beginning of the array and one at the end an compare to see if it goes over the limit

        # initialy
        # num_boats = 0
        # l, r = 0, len(nums)-1

        # while l <= r:
        #   [3,3,4,5], limit 5
        #   check conditions:
        #   cur_weight = nums[l] + nums[r]
        #   if cur_weight == limit:
        #       incr num_boats
        #       move both left and inwards

        #   if cur_weight > limit:
        #       cur_weight is too high:
        #       incr num_boats
        #       r -= 1

        #   else if cur_weight < limit:
        #       move left by 1
        #       new_weight = nums[l] + nums[r]
        