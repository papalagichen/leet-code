from TreeBuilder import TreeNode


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        nodes = [root]
        while len(nodes) > 0:
            root = nodes.pop(0)
            if root.right:
                nodes.append(root.right)
            if root.left:
                nodes.append(root.left)
        return root.val


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize
    from TreeBuilder import TreeNode

    Test.test([Solution().findBottomLeftValue], [
        ((deserialize('[2,1,3]')), 1),
        ((deserialize('[1,2,3,4,null,5,6,null,null,7]')), 7),
    ])
