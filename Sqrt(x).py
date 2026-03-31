1class Solution:
2    def mySqrt(self, x: int) -> int:
3        low = 0
4        high = x
5        ans = -1
6
7        while low <= high:
8            mid = (low + high) // 2
9            midsq = mid * mid
10
11            if midsq == x:
12                return mid
13            elif midsq > x:
14                high = mid - 1
15            else:
16                ans = mid
17                low = mid + 1
18
19        return ans