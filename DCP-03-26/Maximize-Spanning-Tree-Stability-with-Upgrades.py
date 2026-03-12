1class DSU:
2    def __init__(self, n):
3        self.parent = list(range(n))
4        self.rank = [0]*n
5
6    def find(self, x):
7        if self.parent[x] != x:
8            self.parent[x] = self.find(self.parent[x])
9        return self.parent[x]
10
11    def union(self, a, b):
12        pa, pb = self.find(a), self.find(b)
13        if pa == pb:
14            return False
15        if self.rank[pa] < self.rank[pb]:
16            pa, pb = pb, pa
17        self.parent[pb] = pa
18        if self.rank[pa] == self.rank[pb]:
19            self.rank[pa] += 1
20        return True
21
22
23class Solution:
24    def maxStability(self, n, edges, k):
25
26        def can(x):
27            dsu = DSU(n)
28            used = 0
29            upgrades = 0
30
31            optional = []
32
33            for u, v, s, must in edges:
34                if must == 1:
35                    if s < x:
36                        return False
37                    if not dsu.union(u, v):
38                        return False
39                    used += 1
40                else:
41                    optional.append((u, v, s))
42
43            normal = []
44            upgrade = []
45
46            for u, v, s in optional:
47                if s >= x:
48                    normal.append((u, v))
49                elif 2*s >= x:
50                    upgrade.append((u, v))
51
52            for u, v in normal:
53                if dsu.union(u, v):
54                    used += 1
55
56            for u, v in upgrade:
57                if upgrades == k:
58                    break
59                if dsu.union(u, v):
60                    used += 1
61                    upgrades += 1
62
63            return used == n-1
64
65        left, right = 1, 200000
66        ans = -1
67
68        while left <= right:
69            mid = (left + right) // 2
70            if can(mid):
71                ans = mid
72                left = mid + 1
73            else:
74                right = mid - 1
75
76        return ans