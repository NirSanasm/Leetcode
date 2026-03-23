1class Solution:
2    def removeStars(self, s: str) -> str:
3
4        ans = []
5
6        for char in s:
7            if char is "*":
8                if ans:
9                    ans.pop()
10            
11            else:
12                ans.append(char)
13        
14
15        return ''.join(ans)
16        