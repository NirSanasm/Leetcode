1class Solution:
2    def titleToNumber(self, columnTitle: str) -> int:
3        result = 0
4        times = len(columnTitle)
5        for char in columnTitle:
6            val = ord(char.lower()) - 96
7            mul = 26 ** (times-1)
8            result += val * mul
9            times -= 1
10
11        return result
12        