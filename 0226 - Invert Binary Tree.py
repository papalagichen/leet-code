class Solution(object):
    def invertTree(self, root):
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        return root


if __name__ == '__main__':
    import Test
    import TreeBuilder

    Test.test(Solution().invertTree, [
        (TreeBuilder.deserialize('[4,2,7,1,3,6,9]'), TreeBuilder.deserialize('[4,7,2,9,6,3,1]')),
    ])
