1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3      
4        half_of_nums = len(nums)/2
5
6
7            
8        freq = {}
9
10        for i in nums:
11            freq[i] = freq.get(i, 0) + 1
12        
13        for k, v in freq.items():
14            if v >= half_of_nums:
15                return k
16
17        
18
19
20        
21
22
23
24
25        