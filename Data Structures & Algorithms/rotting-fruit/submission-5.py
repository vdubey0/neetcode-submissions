from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        num_fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append(((i, j), 0))
                if grid[i][j] == 1:
                    num_fresh += 1

        if not q and num_fresh == 0:
            return 0

        mins = 0        
        while q:
            (row, col), mins = q.popleft()

            for d in directions:
                nr = d[0] + row
                nc = d[1] + col

                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                
                if grid[nr][nc] in [0, 2]:
                    continue

                grid[nr][nc] = 2
                num_fresh -= 1

                q.append(((nr, nc), mins+1))
            
        return -1 if num_fresh > 0 else mins
