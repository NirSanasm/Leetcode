class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        max_so_far = sum(nums[:k])

        curr_sum = max_so_far

        for i in range(k, len(nums)):

            curr_sum += nums[i]

            curr_sum -= nums[i - k]

            max_so_far = max(curr_sum, max_so_far)

        return max_so_far/k
        