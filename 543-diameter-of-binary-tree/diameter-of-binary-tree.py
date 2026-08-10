# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def calculate_height(node):
            if not node:
                return 0
            
            # Recursively find the height of left and right subtrees
            left_h = calculate_height(node.left)
            right_h = calculate_height(node.right)
            
            # Update the global diameter if the path through 
            # this node is larger than what we've seen so far
            self.max_diameter = max(self.max_diameter, left_h + right_h)
            
            # Return the height of this node to its parent
            return 1 + max(left_h, right_h)
        
        calculate_height(root)
        return self.max_diameter
        