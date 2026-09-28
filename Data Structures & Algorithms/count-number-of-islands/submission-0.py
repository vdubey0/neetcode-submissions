class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def dfs(i, j):
            if i >= len(grid) or i < 0:
                return

            if j >= len(grid[0]) or j < 0:
                return

            if grid[i][j] == '0':
                return
            
            if (i, j) in visited:
                return

            visited.add((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    print(i, j)
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands


            