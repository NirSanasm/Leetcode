class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isSymetry(root1, root2):

            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False

            return (
                isSymetry(root1.left, root2.right)
                and
                isSymetry(root1.right, root2.left)
            )

        if not root:
            return True

        return isSymetry(root.left, root.right)