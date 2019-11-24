class Solution:
    def isSameTree(self, p, q):
        return self.breadth_first_traversal(p) == self.breadth_first_traversal(q)

    def breadth_first_traversal(self, tree_node):
        s = ''
        if tree_node is None:
            return s
        queue = [tree_node]
        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                s += str(node.val)
                queue.append(node.left if node.left else None)
                queue.append(node.right if node.right else None)
            else:
                s += '#'
        return s


class Solution2:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    from TreeBuilder import build
    import Test

    Test.test((Solution().isSameTree, Solution2().isSameTree), [
        ((build({1: [{2: [{4: None},
                          {5: None}]},
                     {3: [None,
                          {6: None}]}]}),
          build({1: [{2: [{4: None},
                          {5: None}]},
                     {3: [None,
                          {6: None}]}]})),
         True),
        ((build({1: [{2: [{4: None},
                          {5: None}]},
                     {3: [None,
                          {6: None}]}]}),
          build({1: [{2: [{4: None},
                          {5: None}]},
                     {3: [{6: None},
                          None]}]})),
         False),
    ])
