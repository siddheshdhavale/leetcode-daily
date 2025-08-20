class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}    # using hashmaps in python
        for i in range(len(s)):
            c1, c2 = s[i], t[i] # Char 1 is from string s, and char 2 s from str t
            
            if((c1 in mapST and mapST[c1] != c2) or
               (c2 in mapTS and mapTS[c2] != c1)):
                return False
            
            mapST[c1] = c2
            mapTS[c2] = c1
            
        return True
