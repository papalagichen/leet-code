class Solution:
    def isBalanced(self, root):
        return root is None or abs(self.treeHeight(root.left) - self.treeHeight(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def treeHeight(self, node):
        if node is None:
            return 0
        if hasattr(node, 'height'):
            return node.height
        node.height = 1 + max(self.treeHeight(node.left), self.treeHeight(node.right))
        return node.height


if __name__ == '__main__':
    import Test
    from TreeBuilder import build

    Test.test(Solution().isBalanced, [
        (None, True),
        (build({1: None}), True),
        (build({1: [{2: None},
                    None]}), True),
        (build({1: [{2: [{3: None},
                         None]},
                    None]}), False),
        (build({3: [{9: None},
                    {20: [{15: None},
                          {7: None}]}]}), True),
        (build({3: [{9: None},
                    {20: [{15: None},
                          {7: [{8: None},
                               None]}]}]}), False),
        (build({1: [{2: [{3: [{4: None},
                              None]},
                         None]},
                    {2: [None,
                         {3: [None,
                              {4: None}]}]}]}), False),
    ])
