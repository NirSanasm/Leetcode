1class Solution:
2    def isValid(self, s: str) -> bool:
3
4        mapping = {
5            '(':')',
6            '{':'}',
7            '[':']'
8        }
9
10        mapping2 = {
11            ')':'(',
12            '}':'{',
13            ']':'['
14        }
15
16        item = []
17        
18        for char in s:
19            if char in mapping:
20                item.append(char)
21            else:
22                if item and item[-1] == mapping2[char]:
23                    item.pop()
24                else:
25                    return False
26
27        return len(item) == 0