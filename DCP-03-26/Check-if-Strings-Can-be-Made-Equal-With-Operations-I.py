1class Solution:
2    def canBeEqual(self, s1: str, s2: str) -> bool:
3        
4        even_s1 = sorted([s1[0], s1[2]])
5        even_s2 = sorted([s2[0], s2[2]])
6        
7        odd_s1 = sorted([s1[1], s1[3]])
8        odd_s2 = sorted([s2[1], s2[3]])
9        
10        return even_s1 == even_s2 and odd_s1 == odd_s2
11        
12
13        