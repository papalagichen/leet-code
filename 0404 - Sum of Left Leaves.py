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


class Solution2:
    def sumOfLeftLeaves(self, node: TreeNode) -> int:
        if node is None:
            return 0
        if node.left is not None and node.left.left is None and node.left.right is None:
            left = node.left.val
        else:
            left = self.sumOfLeftLeaves(node.left)
        return left + self.sumOfLeftLeaves(node.right)


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize
    from TreeBuilder import TreeNode

    Test.test([Solution().sumOfLeftLeaves, Solution2().sumOfLeftLeaves], [
        ((deserialize('[3,9,20,null,null,15,7]')), 24),
    ])
