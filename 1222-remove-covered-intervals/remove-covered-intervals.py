class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda interval: (interval[0], -interval[1]))

        res = r = 0 

        for st, end in intervals:
            res += end > r
            r = max(r, end)

        return res