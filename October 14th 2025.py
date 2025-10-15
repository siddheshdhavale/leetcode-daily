class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if empty grid, no need to run graph algo as no islands
        if not grid:
            return 0

        # dimensions of grid
        rows, cols = len(grid), len(grid[0])

        # visited positions
        visit = set()   # can use 2d grid as well, but set() is easy
        islands = 0 # counting no of islands

        # bfs algo
        def bfs(r, c):  # this is not recursive but iterative, so we need a ds for memory
            q = collections.deque() # q is normally used for bfs
            visit.add((r, c))
            q.append((r,c))

            # while q is not empty, expand our island:
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # left right up down directions

                for dr, dc in directions:
                    # checking if this pos is in bounds
                    r, c = row + dr, col + dc
                    if ((r) in range(rows) and
                        (c) in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:   # mark as visited
                    # running bfs on this row and col
                    bfs(r, c)
                    islands += 1    # only increment no of islands if the number has not been visited.
        return islands
