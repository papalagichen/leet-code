import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        return self.traverse(root, root, sys.maxsize)[1]

    def traverse(self, node, prev_node, min_diff):
        if node.left:
            prev_node, min_diff = self.traverse(node.left, prev_node, min_diff)

        diff = abs(prev_node.val - node.val)
        if 0 < diff < min_diff:
            min_diff = diff
        prev_node = node

        if node.right:
            prev_node, min_diff = self.traverse(node.right, prev_node, min_diff)

        return prev_node, min_diff
