class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # goal: 
        # find num of boats that can carry all people in input list;
        # boats can have up to two people: at least 1, 2 people mx
        # constraints: limit will be >= highest input weight

        # idea: two pointer?
        

        # sort input array:
        people.sort() # time complexity O (n log n)

        boat_count = 0



        # [3,5,3,4] ->
        # [3, 3, 4, 5]

        # [2, 6, 7, 11, 15, 16] limit = 16
        #  j                 i


        # set up our two-pointer loop:
        # outer loop: have one pointer i at the greatest current weight (the end of the list);
        beg, end = 0, len(people) - 1 

        #[3,3,4,5] limit 5
        while end >= beg:
            if end == beg:
                # put it in it's own boat
                boat_count += 1
                # end -= 1 # make them cross
                break

            # if the people[end] is at the limit, put that person in a single boat; boat_count++ and move end inwards
            if people[end] == limit:
                    boat_count += 1
                    end -= 1

            # otherwise, if less than limit: 
            else:

                # test against the lightest element
                if people[end] + people[beg] <= limit:
                    boat_count += 1
            #       move both pointers inwards
                    end -= 1
                    beg += 1
                else:
            #       send people[end] as its own boat
            #       move end inwards (end--)
                    end -= 1
                    boat_count += 1
        
        return boat_count


# time complexity:
# O(n log n) + O(n)
# which term is more significant? O(n log n)
# so  O(n log n) time

