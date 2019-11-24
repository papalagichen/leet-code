class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        root.level = 1
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is None and node.right is None:
                return node.level
            if node.left:
                node.left.level = node.level + 1
                queue.append(node.left)
            if node.right:
                node.right.level = node.level + 1
                queue.append(node.right)


class Solution2:
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None or root.right is None:
            return 1 + self.minDepth(root.right) + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


if __name__ == '__main__':
    from TreeBuilder import build
    import Test

    Test.test((Solution().minDepth, Solution2().minDepth), [
        (None, 0),
        (build({1: None}), 1),
        (build({1: [{2: [{3: None},
                         {4: None}]},
                    {2: [{4: None},
                         {3: None}]}]}), 3),
        (build({1: [{2: [{4: None},
                         {5: None}]},
                    {3: [None,
                         {6: None}]}]}), 3),
        (build({1: [{2: [{3: None},
                         None]},
                    {3: [{2: None},
                         None]}]}), 3),
        (build({1: [{2: [None,
                         {3: None}]},
                    {2: [{3: None},
                         None]}]}), 3),
        (build({5: [{4: [None,
                         {1: [{2: None},
                              None]}]},
                    {1: [None,
                         {4: [{2: None},
                              None]}]}]}), 4),
        (build({2: [{3: [{4: None},
                         {5: [{8: None},
                              {9: None}]}]},
                    {3: [{5: [{9: None},
                              {8: None}]},
                         {4: None}]}]}), 3),
    ])
