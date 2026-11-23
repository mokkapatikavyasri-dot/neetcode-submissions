class Solution:
    def maxPathSum(self, root):
        self.maximum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            current_sum = node.val + left + right

            self.maximum = max(self.maximum, current_sum)

            return node.val + max(left, right)

        dfs(root)

        return self.maximum
