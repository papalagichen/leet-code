class Solution:
    def postorderTraversal(self, root):
        s = []
        if root:
            stack = [root]
            while len(stack) > 0:
                n = stack[-1]
                if n.left and not hasattr(n.left, 'done'):
                    stack.append(n.left)
                elif n.right and not hasattr(n.right, 'done'):
                    stack.append(n.right)
                else:
                    n = stack.pop()
                    n.done = True
                    s.append(n.val)
        return s


class Solution2:
    def postorderTraversal(self, root):
        s = []
        if root:
            stack = [root]
            done_stack = []
            while len(stack) > 0:
                n = stack[-1]
                if n.left and n.left not in done_stack:
                    stack.append(n.left)
                elif n.right and n.right not in done_stack:
                    stack.append(n.right)
                else:
                    n = stack.pop()
                    done_stack.append(n)
                    s.append(n.val)
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

    Test.test((Solution().postorderTraversal, Solution2().postorderTraversal), [
        (tree, [4, 5, 2, 6, 3, 1]),
        (tree2, [3, 2, 1]),
    ])
