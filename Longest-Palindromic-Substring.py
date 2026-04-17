1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3
4        max_palindrome = ""
5        
6        for i in range(len(s)):
7            l, r = i, i
8            while l >= 0 and r < len(s) and s[l] == s[r]:
9                if r - l + 1 > len(max_palindrome):
10                    max_palindrome = s[l:r+1]
11                l -= 1
12                r += 1
13
14            l, r = i, i + 1
15            while l >= 0 and r < len(s) and s[l] == s[r]:
16                if r - l + 1 > len(max_palindrome):
17                    max_palindrome = s[l:r+1]
18                l -= 1
19                r += 1
20
21        return max_palindrome
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36        