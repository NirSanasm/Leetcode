1class Solution:
2    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
3        for l in mat:
4            n = len(l)
5            for i in range(n):
6                if l[i] != l[(i + k) % n]:
7                    return False
8        return True
9
10
11
12
13        