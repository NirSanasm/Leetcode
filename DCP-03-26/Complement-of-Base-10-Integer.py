1class Solution:
2    def bitwiseComplement(self, n: int) -> int:
3
4        binary_string = list(bin(n)[2:])
5
6
7        for i in range(len(binary_string)):
8            if binary_string[i] == "0":
9                binary_string[i] = "1"
10            else:
11                binary_string[i] = "0"
12
13        return int("".join(binary_string),2)
14                
15        