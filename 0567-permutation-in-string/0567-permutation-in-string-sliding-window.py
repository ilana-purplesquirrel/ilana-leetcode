# modified from NeetCode

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # s1 = 'aaajj'
        # s1Count[0] = 3
        # s1Count[9] = 2
        
        # initial setup
        s1Count, s2Count = [0] * 26, [0] * 26


        # create two arrays, each for each of 26 letters
        # the sliding window that moves through s2 is going to be exactly len(s1) wide, because we are looking for s1 permutations, which would all be len(s1)
        # this loop counts the numbers of letters in
        #    - all of s1
        #    - and a len(s2)-wide sliding window that will scan s2, starting at the beginning of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0

        # for every lowercase letter, check that the count of that letter exactly matches between s1Count and s2Count:
        for i in range(26):
            # terniary operator
            #matches += (1 if s1Count[i] == s2Count[i] else 0)
            if s1Count[i] == s2Count[i]:
                matches += 1
            else:
                0




        # this loop slides a sliding window over s2, from left to right;
        # (the sliding window is exactly len(s1) wide)
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # update matches based on the new rightmost character, at s2[r]:
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            # update match, without having to scan through all of s1Count vs s2Count:

            # if the new letter at s2[r] has gotten us a new match, increase matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # otherwise, if the new letter at s2[r] has lost a match, decrease matches;
            # We've added a letter at the right side; did adding that take what was a match, and unbalance it? unbalancing would be a different of one.
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # now, do almost the same thing with moving the left-hand sliding window boundary to the right, and loosing a character from the sliding window:
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            # once again, if there is now a match for the counts of this particular letter, increase matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # otherwise, if, by decreasing the s2 count of this letter, we've lost a match, decrease the matches variable by one;

            # s1Count[index] == s2Count[index] + 1
            # in other words, if s1Count for this letter is now too big by one, because we just lost a match, decr. matches
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
        
            # move l to the next position, for the upcoming sliding window iteration:
            l += 1

        # matches was updating inside the loop;
        # so this is one last required check here, to see if we got exact matches for each letter's count
        #return matches == 26
        if matches == 26:
            return True
        else:
            return False

# Time Complexity:
# O(26) + O(n)
# so, O(n) for n = len(s1)

# Space Complexity:
# O(1)
