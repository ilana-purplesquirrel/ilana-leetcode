class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        l = len(s)
        if l==1:
            return

        ia = 0
        ib = l - 1

        while ia < ib:
            temp = s[ia]
            s[ia] = s[ib]
            s[ib] = temp

            ia += 1
            ib -= 1
        
        return
    
        # time complexity: O(n)
        # space complexity: O(1)
        
