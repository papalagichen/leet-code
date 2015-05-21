class BSTIterator:
    def __init__(self, root):
        self.root = root
        self.stack = [root] if root else []

    def inorder_traversal(self):
        if self.root:
            while len(self.stack) > 0:
                n = self.stack[-1]
                if n.left and not hasattr(n.left, 'done'):
                    while n.left:
                        n = n.left
                        n.done = True
                        self.stack.append(n)
                n = self.stack.pop()
                if n.right:
                    self.stack.append(n.right)
                yield n.val

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        return next(self.inorder_traversal())


class BSTIterator2:
    def __init__(self, root):
        self.root = root
        self.stack = [root] if root else []
        self.done_stack = []

    def inorder_traversal(self):
        while self.root and len(self.stack) > 0:
            n = self.stack[-1]
            if n.left and n not in self.done_stack:
                self.stack.append(n.left)
                self.done_stack.append(n)
            else:
                n = self.stack.pop()
                if len(self.done_stack) > 0 and n is self.done_stack[-1]:
                    self.done_stack.pop()
                if n.right:
                    self.stack.append(n.right)
                yield n.val

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        return next(self.inorder_traversal())


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

    i, a = BSTIterator(tree), []
    while i.hasNext():
        i_next = i.next()
        a.append(i_next)
    Test.equal([4, 2, 5, 1, 3, 6], a)

    i, a = BSTIterator(tree2), []
    while i.hasNext():
        a.append(i.next())
    Test.equal([1, 3, 2], a)

    i, a = BSTIterator(None), []
    while i.hasNext():
        a.append(i.next())
    Test.equal([], a)

    i, a = BSTIterator2(tree), []
    while i.hasNext():
        i_next = i.next()
        a.append(i_next)
    Test.equal([4, 2, 5, 1, 3, 6], a)

    i, a = BSTIterator2(tree2), []
    while i.hasNext():
        a.append(i.next())
    Test.equal([1, 3, 2], a)

    i, a = BSTIterator2(None), []
    while i.hasNext():
        a.append(i.next())
    Test.equal([], a)
