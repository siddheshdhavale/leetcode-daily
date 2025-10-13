class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        res = len(points)
        prev = points[0]

        for i in range(1, len(points)):
            points[i], points[i - 1]
            cur = points[i]

            if cur[0] <= prev[1]:
                res -= 1
                # merge and store in prev
                # to merge take min of end of cur and min of prev
                prev = [cur[0], min(cur[1], prev[1])]
            else:
                prev = cur


        return res
