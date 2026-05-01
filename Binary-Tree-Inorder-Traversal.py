1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9
10        res = []
11
12        if not root:
13            return []
14
15        res.extend(self.inorderTraversal(root.left))
16        res.append(root.val)
17        res.extend(self.inorderTraversal(root.right))
18
19        return res
20        