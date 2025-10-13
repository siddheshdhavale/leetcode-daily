class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two ptr approach (less memory)
        # using ascii val to determin char alphanum
        # T.C: O(n), S.C: O(1)
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))







        '''
        # using Built-in functions
        newStr = "" # using extra mem here
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]   # [::1] syntax for reversing a string, and using extra mem here
        '''
