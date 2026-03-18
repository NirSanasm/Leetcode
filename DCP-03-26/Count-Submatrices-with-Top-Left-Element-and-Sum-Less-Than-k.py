1class Solution:
2    def countSubmatrices(self, grid, k):
3        m = len(grid)
4        n = len(grid[0])
5        count = 0
6
7        for i in range(m):
8            for j in range(n):
9
10                if i > 0:
11                    grid[i][j] += grid[i-1][j]
12
13                if j > 0:
14                    grid[i][j] += grid[i][j-1]
15
16                if i > 0 and j > 0:
17                    grid[i][j] -= grid[i-1][j-1]
18
19                if grid[i][j] <= k:
20                    count += 1
21
22        return count