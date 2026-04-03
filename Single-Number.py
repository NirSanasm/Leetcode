1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3
4        xor = 0
5
6        for n in nums:
7            xor = xor ^ n
8
9        return xor
10        