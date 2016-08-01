class Solution(object):
    def invertTree(self, root):
        if root:
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        return root


if __name__ == '__main__':
    import Test
    import TreeBuilder

    Test.test(Solution().invertTree, [
        (TreeBuilder.build({4: [{2: [{1: None},
                                     {3: None}]},
                                {7: [{6: None},
                                     {9: None}]}]}),
         TreeBuilder.build({4: [{7: [{9: None},
                                     {6: None}]},
                                {2: [{3: None},
                                     {1: None}]}]})),
    ])
