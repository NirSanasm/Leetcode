1class Solution:
2    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
3
4        prefixes = set()
5        longest = 0
6
7        for i in range(len(arr1)):
8            prefix = ""
9            str_arr = str(arr1[i])
10
11            for char in str_arr:
12                prefix += char
13                prefixes.add(prefix)
14
15
16        for i in range(len(arr2)):
17
18            prefix = ""
19            str_arr = str(arr2[i])
20
21            for char in str_arr:
22                prefix += char
23                if prefix in prefixes:
24                    longest = max(len(prefix), longest)
25                else:
26                    break
27        return longest
28
29
30        
31        