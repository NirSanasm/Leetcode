1class Solution:
2
3
4    def climbStairs(self, n: int) -> int:
5        if n <= 2:
6            return n
7        
8        
9        prev = 1
10        curr = 2
11
12        for i in range(3, n+1):
13            temp = curr + prev
14            prev, curr = curr, temp
15
16        return curr
17
18
19
20
21
22        