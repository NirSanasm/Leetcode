1class Solution:
2    def plusOne(self, digits):
3        n = len(digits)
4        
5        for i in range(n - 1, -1, -1):
6            if digits[i] < 9:
7                digits[i] += 1
8                return digits
9            digits[i] = 0
10        
11        # If all digits were 9
12        return [1] + digits        