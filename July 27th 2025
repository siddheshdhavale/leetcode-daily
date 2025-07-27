class Solution:
    def reverseWords(self, s: str) -> str:
        str_builder = collections.deque()   # using deque as append to left in constant t
        start, i = -1, 0

        while i < len(s):
            if s[i] != " ":
                start = i
                while i < len(s) and s[i] != " ":
                    i += 1
                str_builder.appendleft(s[start: i])
                i -= 1
            i += 1
        return " ".join(str_builder)
        
        '''
        words = s.split()
        words.reverse()
        
        return " ".join(words)
        '''
