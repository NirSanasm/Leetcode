1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        answer = [1] * len(nums)
4
5        prefix = 1
6        for i in range(len(nums)):
7            answer[i] = prefix
8            prefix *= nums[i]
9
10        suffix = 1
11        for i in range(len(nums)-1, -1, -1):
12            answer[i] = answer[i] * suffix
13            suffix = nums[i] * suffix
14        
15        return answer