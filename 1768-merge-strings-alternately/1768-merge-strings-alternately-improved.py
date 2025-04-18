class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # inspired by NeetCode

        p1, p2 = 0, 0
        out_s = ""

        max_round = 0
        if len(word1) >= len(word2):
            max_round = len(word1)
        else:
            max_round = len(word2)

        current_round = 0

        while current_round < max_round:

            if p1 < len(word1):
                out_s += word1[p1]
                p1 += 1
            
            if p2 < len(word2):
                out_s += word2[p2]
                p2 += 1
            
            current_round += 1

        return out_s
