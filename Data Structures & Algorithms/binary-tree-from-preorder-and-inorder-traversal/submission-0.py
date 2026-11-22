class Solution:
    def buildTree(self, preorder, inorder):
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_index = 0

        def build(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_index]
            self.pre_index += 1

            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
