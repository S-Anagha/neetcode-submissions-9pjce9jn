class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        numofi = 0
        if not grid:
            return 0
        def dfs(r, c):
            grid[r][c] = "0"
            for nr, nc in directions:
                if nr+r >= 0 and nr+r < rows and nc+c >= 0 and nc+c < cols and grid[nr+r][nc+c] == "1":
                    dfs(nr+r,nc+c)

        for ro in range(rows):
            for co in range(cols):
                if grid[ro][co] == "1":
                    numofi += 1
                    dfs(ro,co)

        return numofi


        