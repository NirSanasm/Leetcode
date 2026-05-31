1class Solution:
2    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
3        
4        asteroids.sort()
5
6        for num in asteroids:
7
8            if mass >= num:
9
10                mass += num
11
12            else:
13
14                return False
15
16        return True