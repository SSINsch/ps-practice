from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.depth = max(self.depth, left + 1)
            self.depth = max(self.depth, right + 1)

            return max(left, right) + 1

        dfs(root)
        return self.depth
