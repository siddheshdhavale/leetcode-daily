class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # two pointer sliding window (O(n))
        l, total = 0, 0
        res = float("inf")  # if we dont find an array that sums up to a target, return default val of 0

        for r in range(len(nums)):
            # Sliding win
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)   # size of res (r - l + 1), minimize result of size and itself
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res
