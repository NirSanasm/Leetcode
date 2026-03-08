1class Solution:
2    def findDifferentBinaryString(self, nums: List[str]) -> str:
3        l=[]
4        for i in range(len(nums)):
5            if nums[i][i]=='0':
6                l.append('1')
7            else:
8                l.append('0')
9        return ''.join(l)