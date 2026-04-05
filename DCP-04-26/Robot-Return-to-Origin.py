1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3        count_u = 0
4        count_d = 0
5        count_l = 0
6        count_r = 0
7
8        for char in moves:
9            if char == "L":
10                count_l += 1
11            elif char == "R":
12                count_r += 1
13            elif char == "U":
14                count_u += 1
15            else:
16                count_d += 1
17
18        return count_u == count_d and count_l == count_r
19        