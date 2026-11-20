class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        new_arr = []

        i, j = 0, n

        while j < len(nums):

            new_arr.append(nums[i])
            new_arr.append(nums[j])

            i += 1
            j += 1

        return new_arr