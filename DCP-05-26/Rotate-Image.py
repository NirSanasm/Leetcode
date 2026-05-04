1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6
7        n = len(matrix)
8
9        for i in range(n):
10            for j in range(i, n):
11                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
12
13        for i in range(n):
14            matrix[i].reverse()
15        