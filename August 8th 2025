class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        CharSet = set() # set automatically checks duplicates
        l = 0
        res = 0

        for r in range(len(s)): # right ptr cont be changing
            while s[r] in CharSet:  # while duplicate
                CharSet.remove(s[l])    # remove the leftmost charecter
                l += 1
            CharSet.add(s[r])    # adding this rightmost char to our set
            res = max(res, r - l + 1)   # r - l + 1 making cur window size > than what it is
        return res


        '''
        CharSet = set()
        # Sliding Window
        l = 0
        res = 0

        for r in range(len(s)): # right ptr cont be changing
            while s[r] in CharSet:  # while duplicate
                CharSet.remove(s[l])    # remove the leftmost character
                l += 1
            CharSet.add(s[r])   # adding this rightmost char to our set
            res = max(res, r - l + 1)   # r - l + 1 making cur window size > than what it is
        return res
        '''
