class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output_count = 0
        p1, p2 = 0, 0
        out_s = ""
        while len(out_s) < (len(word1) + len(word2)):
            choice = len(out_s) % 2
            if choice == 0:
                if p1 < len(word1):
                    out_s += word1[p1]
                    p1 += 1
                else:
                    out_s += word2[p2]
                    p2 += 1
            else:
                if p2 < len(word2):
                    out_s += word2[p2]
                    p2 += 1
                else:
                    out_s += word1[p1]
                    p1 += 1

        return out_s
