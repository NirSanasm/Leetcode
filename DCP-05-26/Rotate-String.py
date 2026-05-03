1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3        
4        for i in range(len(s)):
5            if s[i+1:] + s[0:i+1] == goal:
6                return True
7            
8        return False