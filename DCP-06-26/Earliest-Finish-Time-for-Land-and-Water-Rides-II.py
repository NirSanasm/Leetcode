1class Solution:
2    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
3
4
5        res = float('inf')
6        water_min_start = float('inf')
7
8        for i, j in zip(waterStartTime, waterDuration):
9            water_min_start = min(water_min_start, i + j)
10
11
12        land_min_start = float('inf')
13
14        for i, j in zip(landStartTime, landDuration):
15            land_min_start = min(land_min_start, i + j)
16
17        water_first = float('inf')
18
19        for i, j in zip(landStartTime, landDuration):
20
21            water_first = min(water_first, max(water_min_start, i) + j)
22
23        res = min(res, water_first)
24
25
26        land_first = float('inf')
27
28        for i, j in zip(waterStartTime, waterDuration):
29
30            land_first = min(land_first, max(land_min_start, i) + j)
31
32
33        res = min(res, land_first)
34
35        return res