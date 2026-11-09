# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:

        def convert(low, high):

            if low > high:
                return 

            mid = (low + high) // 2

            node = TreeNode(val=nums[mid])

            node.left = convert(low, mid - 1)

            node.right = convert(mid + 1, high)

            return node




        return convert(0, len(nums) - 1)
        