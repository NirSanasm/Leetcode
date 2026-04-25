1class Solution:
2    def fib(self, n: int) -> int:
3
4      
5        if n <=1:
6            return n
7    
8        a, b = 0 , 1
9
10        for _ in range(2, n+1):
11            a , b = b , b+a
12
13        return b
14
15        