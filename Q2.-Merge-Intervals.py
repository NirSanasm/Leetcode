1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        
4        intervals = sorted(intervals, key= lambda x: x[0])
5
6        merged = []
7
8        for interval in intervals:
9
10            if not merged or merged[-1][-1] < interval[0]:
11                merged.append(interval)
12            else:
13                merged[-1][-1] = max(merged[-1][-1], interval[-1])
14
15        
16        return merged
17
18
19
20            
21            
22
23
24        