1class Solution:
2    def furthestDistanceFromOrigin(self, moves: str) -> int:
3
4        L = moves.count('L')
5        R = moves.count('R')
6        
7        return abs(L - R) + moves.count('_')
8        