class Solution:
    def intToRoman(self, num: int) -> str:
        # List instead of Hashmap as we need it in asc ord
        symbolList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]

        res = ""
        for sym, val in reversed(symbolList):
            if num // val:
                count = num // val
                res += (sym * count)    # count of adding sym to str
                num = num % val
        return res
