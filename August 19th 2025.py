class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        letters = collections.Counter(magazine)

        for char in ransomNote:
            if char not in letters or letters[char] <= 0:
                return False
            letters[char] -= 1
        return True
