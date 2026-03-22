1import numpy as np
2
3class Solution:
4    def findRotation(self, mat, target):
5        
6        rotated = mat
7        
8        # check 0° rotation first
9        if np.array_equal(rotated, target):
10            return True
11        
12        for i in range(3):
13            rotated = np.rot90(rotated, k=-1)
14            if np.array_equal(rotated, target):
15                return True
16        
17        return False