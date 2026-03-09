1class Solution:
2    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
3 
4        from functools import cache
5      
6        MOD = 10**9 + 7
7      
8        @cache
9        def count_arrays(zeros_left: int, ones_left: int, last_element: int) -> int:
10 
11            
12            if zeros_left == 0:
13
14                return 1 if (last_element == 1 and ones_left <= limit) else 0
15          
16  
17            if ones_left == 0:
18
19                return 1 if (last_element == 0 and zeros_left <= limit) else 0
20          
21            if last_element == 0:
22                total_ways = count_arrays(zeros_left - 1, ones_left, 0) + \
23                            count_arrays(zeros_left - 1, ones_left, 1)
24              
25  
26                if zeros_left - limit - 1 >= 0:
27                    total_ways -= count_arrays(zeros_left - limit - 1, ones_left, 1)
28              
29                return total_ways
30          
31            else:
32                total_ways = count_arrays(zeros_left, ones_left - 1, 0) + \
33                            count_arrays(zeros_left, ones_left - 1, 1)
34              
35        
36                if ones_left - limit - 1 >= 0:
37                    total_ways -= count_arrays(zeros_left, ones_left - limit - 1, 0)
38              
39                return total_ways
40      
41        result = (count_arrays(zero, one, 0) + count_arrays(zero, one, 1)) % MOD
42      
43        count_arrays.cache_clear()
44      
45        return result