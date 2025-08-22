class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashm_s = {}
        hashm_t = {}
        
        for i in range(len(s)):
            if s[i] not in hashm_s:
                hashm_s[s[i]] = 1
            else:
                hashm_s[s[i]] += 1
                
            if t[i] not in hashm_t:
                hashm_t[t[i]] = 1
            else:
                hashm_t[t[i]] += 1
                
        return hashm_s == hashm_t
