class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        
        d = {} # string : list[strings]
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted in d:
                d[s_sorted].append(s)
            else:
                d[s_sorted] = [s]
        
        result = []
        for s_sorted in d.keys():
            result.append(d[s_sorted])
        
        return result
