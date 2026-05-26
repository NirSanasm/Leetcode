1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3
4        seen = set()
5        special = set()
6
7        for char in word:
8            seen.add(char)
9            if char.lower() in seen and char.upper() in seen:
10                special.add(char.lower())
11
12        return len(special)
13        