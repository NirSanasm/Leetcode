1class Solution:
2    def findDifferentBinaryString(self, nums: List[str]) -> str:
3        n = len(nums)
4
5        list_of_bin = {}
6
7        def generate_binary_strings(n, prefix=""):
8            if n == 0:
9                list_of_bin[prefix] = "Not Found"
10            else:
11                generate_binary_strings(n - 1, prefix + "0")
12                generate_binary_strings(n - 1, prefix + "1")
13        
14        generate_binary_strings(n)
15
16        for n in nums:
17            list_of_bin[n] = "Found"
18        
19        for k, v in list_of_bin.items():
20            if v == "Not Found":
21                return k
22        