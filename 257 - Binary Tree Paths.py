class Solution:
    def binaryTreePaths(self, root):
        paths, stack = [], [root]
        if root is None:
            return paths
        while stack:
            n = stack[-1]
            if n.left and not hasattr(n.left, 'done'):
                stack.append(n.left)
            elif n.right and not hasattr(n.right, 'done'):
                stack.append(n.right)
            else:
                if n.left is None and n.right is None:
                    paths.append('->'.join([str(x.val) for x in stack]))
                stack.pop().done = True
        return paths


if __name__ == '__main__':
    import Test
    import TreeBuilder

    Test.test(Solution().binaryTreePaths, [
        (TreeBuilder.build({1: [{2: [None, {5: None}]},
                                {3: None}]}), ["1->2->5", "1->3"]),
    ])
