# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, node: TreeNode) -> int:
        if node is None:
            return 0
        s = 0
        if node.left:
            s += self.sumOfLeftLeaves(node.left)
            if node.left.left is None and node.left.right is None:
                s += node.left.val
        if node.right:
            s += self.sumOfLeftLeaves(node.right)
        return s
