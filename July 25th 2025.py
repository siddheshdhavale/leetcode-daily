class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last index nums1
        last = m + n - 1

        # merge in reverse order
        # indexses start at 0, hence [n-1], [m-1]
        while m > 0 and n > 0:  # while there are numbers left in both the arrays:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                # updating our pointers decrementing m and n
                m -= 1
            else:   # if both were equal or if nums2 was greater:
                nums1[last] = nums2[n - 1]
                # updating our pointers decrementing n
                n -= 1
            #regardless of any ele insertion, decrement last
            last -= 1

        # edge case 3: if more leftower elements in nums2, fill them directly in nums1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1     # updating ptrs, decrementing n and last 
