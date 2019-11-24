class Solution:
    def levelOrder(self, root):
        s = []
        if root is None:
            return s
        queue = [root]
        last_level = 0
        root.level = 1
        while len(queue) > 0:
            n = queue.pop(0)
            if n.level == last_level:
                s[-1].append(n.val)
            else:
                s.append([n.val])
            last_level = n.level
            if n.left:
                n.left.level = last_level + 1
                queue.append(n.left)
            if n.right:
                n.right.level = last_level + 1
                queue.append(n.right)
        return s


if __name__ == '__main__':
    import Test
    from TreeBuilder import build

    Test.test((Solution().levelOrder,), [
        (build({3: [{9: None},
                    {20: [{15: None},
                          {7: None}]}]}), [[3],
                                           [9, 20],
                                           [15, 7]
                                           ])
    ])
