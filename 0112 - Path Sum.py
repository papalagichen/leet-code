class Solution:
    def hasPathSum(self, root, s):
        if root is None:
            return False
        queue = [root]
        root.rest = s
        while len(queue) > 0:
            node = queue.pop(0)
            if not node.left and not node.right and node.val == node.rest:
                return True
            if node.left:
                node.left.rest = node.rest - node.val
                queue.append(node.left)
            if node.right:
                node.right.rest = node.rest - node.val
                queue.append(node.right)
        return False


class Solution2:
    def hasPathSum(self, root, s):
        if root is None:
            return False
        if root.val == s and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, s - root.val) or self.hasPathSum(root.right, s - root.val)


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize
    from TreeBuilder import TreeNode

    tree = deserialize('[5,4,8,11,null,13,4,7,2,null,null,null,1]')

    Test.test([Solution().hasPathSum, Solution2().hasPathSum], [
        ((None, 0), False),
        ((tree, 22), True),
        ((tree, 26), True),
        ((tree, 9), False),
        ((TreeNode(8), 8), True)
    ])
