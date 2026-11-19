class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

        num1_set = set(nums1)

        num2_set = set(nums2)


        val1 = list(num1_set - num2_set)

        val2 = list(num2_set - num1_set)

        return [val1, val2]


        