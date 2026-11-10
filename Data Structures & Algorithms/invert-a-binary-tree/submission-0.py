class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        # Swap left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
