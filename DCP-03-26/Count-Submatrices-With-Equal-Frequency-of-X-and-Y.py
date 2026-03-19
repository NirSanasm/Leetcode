1class Solution:
2    def numberOfSubmatrices(self, grid):
3        m = len(grid)
4        n = len(grid[0])
5
6        balance = [[0]*n for _ in range(m)]
7        countX = [[0]*n for _ in range(m)]
8
9        ans = 0
10
11        for i in range(m):
12            for j in range(n):
13
14                # Convert values
15                val = 0
16                if grid[i][j] == 'X':
17                    val = 1
18                elif grid[i][j] == 'Y':
19                    val = -1
20
21                x = 1 if grid[i][j] == 'X' else 0
22
23                # Build prefix
24                balance[i][j] = val
25                countX[i][j] = x
26
27                if i > 0:
28                    balance[i][j] += balance[i-1][j]
29                    countX[i][j] += countX[i-1][j]
30
31                if j > 0:
32                    balance[i][j] += balance[i][j-1]
33                    countX[i][j] += countX[i][j-1]
34
35                if i > 0 and j > 0:
36                    balance[i][j] -= balance[i-1][j-1]
37                    countX[i][j] -= countX[i-1][j-1]
38
39                # Check conditions
40                if balance[i][j] == 0 and countX[i][j] > 0:
41                    ans += 1
42
43        return ans