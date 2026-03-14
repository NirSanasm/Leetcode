1class Solution:
2    def getHappyString(self, n: int, k: int) -> str:
3        res = []
4        
5        def backtrack(s):
6            if len(s) == n:
7                res.append(s)
8                return
9            
10            for ch in ['a','b','c']:
11                if not s or s[-1] != ch:
12                    backtrack(s + ch)
13        
14        backtrack("")
15        
16        if k > len(res):
17            return ""
18        
19        return res[k-1]