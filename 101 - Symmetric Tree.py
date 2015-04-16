from TreeBuilder import build


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.areSymmetric(root.left, root.right)

    def areSymmetric(self, tree1, tree2):
        if tree1 is None or tree2 is None:
            return tree1 is None and tree2 is None
        if tree1.val != tree2.val:
            return False
        return self.areSymmetric(tree1.left, tree2.right) and self.areSymmetric(tree1.right, tree2.left)


class Solution2:
    def isSymmetric(self, root):
        if root is None:
            return True
        queue = [root.left, root.right]
        while len(queue) > 0:
            a, b = queue.pop(0), queue.pop(0)
            if a is None and b is None:
                continue
            if a is None or b is None or a.val != b.val:
                return False
            queue.extend([a.left, b.right, a.right, b.left])
        return True


if __name__ == '__main__':
    import Test

    Test.test((Solution().isSymmetric, Solution2().isSymmetric), [
        (None, True),
        (build({1: None}), True),
        (build({1: [{2: None},
                    {2: None}]}), True),
        (build({1: [{2: [{3: None},  # 1223443
                         {4: None}]},
                    {2: [{4: None},
                         {3: None}]}]}), True),
        (build({1: [{2: [{4: None},
                         {5: None}]},
                    {3: [None,
                         {6: None}]}]}), False),
        (build({1: [{2: [{3: None},
                         None]},
                    {3: [{2: None},
                         None]}]}), False),
        (build({1: [{2: [None,
                         {3: None}]},
                    {2: [{3: None},
                         None]}]}), True),
        (build({5: [{4: [None,
                         {1: [{2: None},
                              None]}]},
                    {1: [None,
                         {4: [{2: None},
                              None]}]}]}), False),
        (build({2: [{3: [{4: None},
                         {5: [{8: None},
                              {9: None}]}]},
                    {3: [{5: [{9: None},
                              {8: None}]},
                         {4: None}]}]}), True),
        (build({1: [{2: [None,
                         {3: None}]},
                    {2: [None,
                         {3: None}]}]}), False),
        (build({4: [{57: [None,
                          {67: [None,
                                {97: None}]}]},
                    {57: [{67: [{97: None},
                                None]},
                          None]}]}), True),
        (build({2: [{3: [{4: None},
                         {5: [{8: None},
                              {9: None}]}]},
                    {3: [{5: None},
                         {4: [{9: None},
                              {8: None}]}]}]}), False),
    ])
