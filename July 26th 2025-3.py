class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        # simultaneous iteration through all strings
        for i in range(len(strs[0])):    # going through every char in first str:
            for s in strs:  # iterating through every single string and making sure whether every string has the exact same char at index i
                if i == len(s) or s[i] != strs[0][i]:
                    return res
        # what if out of bounds: prev if i == len(s)
            # adding char to our result
            res += strs[0][i]
        return res
