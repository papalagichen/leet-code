from TreeBuilder import TreeNode


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize

    Test.test([Solution().mergeTrees], [
        ((deserialize('[1,3,2,5]'), deserialize('[2,1,3,null,4,null,7]')), deserialize('[3,4,5,5,4,null,7]')),
    ])
