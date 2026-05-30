1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3        res = [[1]]
4
5        for i in range(numRows-1):
6            temp = [0] + res[-1] + [0]
7            arr = []
8            for j in range(len(temp)-1):
9                arr.append(temp[j]+temp[j+1])
10            res.append(arr)
11
12        return res
13
14
15        