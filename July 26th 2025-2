class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0   # i ptr -> assigned to end of str, len ptr -> assigned to 0
        # Phase 1: eliminating leading white spaces
        while i>= 0 and s[i] == " ":    # while i is in bounds
            i -= 1  # decrement ptr
        # Phase 2: counting char: determining len
        while i >= 0 and s[i] != " ":
            length += 1 # increment length count
            i -= 1
        return length
