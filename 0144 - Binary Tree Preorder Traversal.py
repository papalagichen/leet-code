class Solution:
    def preorderTraversal(self, root):
        s = []
        if root:
            stack = [root]
            while len(stack) > 0:
                n = stack.pop()
                s.append(n.val)
                if n.right:
                    stack.append(n.right)
                if n.left:
                    stack.append(n.left)
        return s


if __name__ == '__main__':
    import Test
    from TreeBuilder import build

    tree = build({1: [{2: [{4: None},
                           {5: None}]},
                      {3: [None,
                           {6: None}]}]})
    tree2 = build({1: [None,
                       {2: [{3: None},
                            None]}]})

    Test.test(Solution().preorderTraversal, [
        (tree, [1, 2, 4, 5, 3, 6]),
        (tree2, [1, 2, 3]),
    ])
