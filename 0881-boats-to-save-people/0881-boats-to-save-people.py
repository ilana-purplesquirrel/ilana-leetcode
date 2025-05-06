# inspired by NeetCode

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # count and return the minimum integer number of boats required.

        num_boats = 0

        # set this up as a two-pointer problem on sorted input data

        # sorting will add O(n log n) time complexity
        people.sort()

        l, r = 0, len(people) - 1

        # walk through the list, moving l at most one step right, or right at most one step left, as long as the pointers haven't crossed;
        while l <= r:


        # if l and r have met, just add this one remaining person to a boat, and ++ count

            if l == r:
                # one of the two final states:
                # in this state, we only have one person left
                num_boats += 1
                l += 1 # trigger end of loop
            else:

            
            
                # start by evaluating the greatest remaining weight
                # check the remaining available weight vs the limit that we're given
                remainder = limit - people[r]

                # try to add the least-most available weight; 
                if remainder >= people[l]:

                    # if possible, move left and right to next items and ++ count
                    num_boats += 1
                    l += 1
                    r -= 1
                else:
                    # if not possible, just move right and ++ count
                    num_boats += 1
                    r -= 1

        # return count
        return num_boats
    