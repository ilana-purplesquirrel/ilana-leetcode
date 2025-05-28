# from NeetCode

# time complexity:

# O(n log(n)) + O(n^2)*O(n log(n))

# O(n^2)*O(n log(n))

# O(n^3 log(n))


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                subStr = s2[i : j + 1]
                subStr = sorted(subStr)
                if subStr == s1:
                    return True
        return False

