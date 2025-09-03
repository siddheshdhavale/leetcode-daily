class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # i+1
        # starting point - storage
        ans = []    # empty array
        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums)-1 and nums[i] + 1 == nums[i+1]:
                i += 1
            if start != nums[i]:
                ans.append(str(start) + '->' + str(nums[i]))
            else:
                ans.append(str(nums[i]))
            
            i += 1
        
        return ans
        # tc: o(n)
        # sc: o(n)
