class Solution:
    def isHappy(self, n: int) -> bool:
        # Hashset for visited no tracking
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            # True condition:
            if n == 1:
                return True
        return False
        
    def sumOfSquares(self, n: int) -> int:
            # computing sum of squares:
            # 19 -> 19%10 -> 9, & 19//10 -> 1 in code division
            # square these, and add them together
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
