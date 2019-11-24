class Solution:
    def inorderTraversal(self, root):
        s = []
        if root:
            stack = [root]
            while len(stack) > 0:
                n = stack[-1]
                if n.left and not hasattr(n.left, 'done'):
                    while n.left:
                        n = n.left
                        n.done = True
                        stack.append(n)
                n = stack.pop()
                s.append(n.val)
                if n.right:
                    stack.append(n.right)
        return s


class Solution2:
    def inorderTraversal(self, root):
        s, stack, current = [], [], root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                n = stack.pop()
                s.append(n.val)
                current = n.right
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

    Test.test((Solution().inorderTraversal, Solution2().inorderTraversal), [
        (tree, [4, 2, 5, 1, 3, 6]),
        (tree2, [1, 3, 2]),
    ])
