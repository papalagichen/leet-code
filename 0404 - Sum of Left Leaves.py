from TreeBuilder import TreeNode


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
