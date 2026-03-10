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
11            if zeros_left == 0:
12                return 1 if (last_element == 1 and ones_left <= limit) else 0
13          
14            if ones_left == 0:
15                return 1 if (last_element == 0 and zeros_left <= limit) else 0
16          
17            if last_element == 0:
18                total_ways = count_arrays(zeros_left - 1, ones_left, 0) + \
19                            count_arrays(zeros_left - 1, ones_left, 1)
20                if zeros_left - limit - 1 >= 0:
21                    total_ways -= count_arrays(zeros_left - limit - 1, ones_left, 1)
22                return total_ways
23            else:
24                total_ways = count_arrays(zeros_left, ones_left - 1, 0) + \
25                            count_arrays(zeros_left, ones_left - 1, 1)
26                if ones_left - limit - 1 >= 0:
27                    total_ways -= count_arrays(zeros_left, ones_left - limit - 1, 0)
28                return total_ways
29      
30        result = (count_arrays(zero, one, 0) + count_arrays(zero, one, 1)) % MOD
31      
32        count_arrays.cache_clear()
33      
34        return result