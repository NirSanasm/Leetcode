1import math
2
3class Solution:
4    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
5
6        def can_finish(T):
7            total = 0
8            for t in workerTimes:
9                val = (2 * T) // t
10                x = int((math.sqrt(1 + 4 * val) - 1) // 2)
11                total += x
12                if total >= mountainHeight:
13                    return True
14            return False
15
16        left, right = 0, 10**18
17        ans = right
18
19        while left <= right:
20            mid = (left + right) // 2
21            if can_finish(mid):
22                ans = mid
23                right = mid - 1
24            else:
25                left = mid + 1
26
27        return ans