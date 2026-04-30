1import heapq
2class Solution:
3    def lastStoneWeight(self, stones: List[int]) -> int:
4
5        max_heap = [-s for s in stones]
6
7        heapq.heapify(max_heap)
8
9        while len(max_heap) > 1:
10            y = -heapq.heappop(max_heap)
11            x = -heapq.heappop(max_heap)
12
13            if x!= y:
14                heapq.heappush(max_heap, -(y-x))
15
16        return -max_heap[0] if max_heap else 0
17        