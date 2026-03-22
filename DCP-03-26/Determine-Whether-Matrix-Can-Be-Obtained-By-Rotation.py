1class Solution:
2    def findRotation(self, mat, target):
3        
4        def rotate(matrix):
5           
6            n = len(matrix)
7            new = [[0]*n for _ in range(n)]
8            
9            for i in range(n):
10                for j in range(n):
11                    new[j][n - 1 - i] = matrix[i][j]
12            
13            return new
14        
15        for _ in range(4):  
16            if mat == target:
17                return True
18            mat = rotate(mat)
19        
20        return False