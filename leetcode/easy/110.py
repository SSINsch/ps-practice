from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balanced(root: Optional[TreeNode]) -> int:
            if not root:
                return True

            left = check_balanced(root.left)
            right = check_balanced(root.right)

            # already unbalanced left
            if left is False:
                return False

            # already unbalanced right
            if right is False:
                return False

            # if height gap more than 1
            if abs(left - right) > 1:
                return False

            # if balanced, return (height of the subtree + 1)
            return max(left, right) + 1

        return check_balanced(root) > 0