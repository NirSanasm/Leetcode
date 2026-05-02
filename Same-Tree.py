1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8
9    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
10
11        if not p and not q:
12            return True
13        
14        if not p or not q:
15            return False
16
17        if p.val != q.val:
18            return False
19
20        return (
21            self.isSameTree(p.left, q.left) and
22            self.isSameTree(p.right, q.right)
23        )
24        
25       
26
27        
28        