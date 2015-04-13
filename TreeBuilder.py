class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return preorder_traversal(self)

    def __cmp__(self, other):
        return cmp(str(self), str(other))


def build(nodes):
    if nodes and len(nodes.keys()) > 0:
        node_value = nodes.keys()[0]
        self = TreeNode(node_value)
        if nodes[node_value] and len(nodes[node_value]) == 2:
            self.left = build(nodes[node_value][0])
            self.right = build(nodes[node_value][1])
        return self
    return None


def breadth_first_traversal(tree_node):
    s = ''
    if tree_node is None:
        return s
    queue = [tree_node]
    while len(queue) > 0:
        n = queue.pop(0)
        s += str(n.val)
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)
    return s


def preorder_traversal(tree_node, left_to_right=True):
    s = ''
    if tree_node is None:
        return s
    stack = [tree_node]
    while len(stack) > 0:
        n = stack.pop()
        s += str(n.val)
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)
    return s


def inorder_traversal(tree_node, left_to_right=True):
    s = ''
    if tree_node:
        stack = [tree_node]
        while len(stack) > 0:
            n = stack[-1]
            if n.left and not hasattr(n.left, 'done'):
                while n.left:
                    n = n.left
                    stack.append(n)
            n = stack.pop()
            n.done = True
            s += str(n.val)
            if n.right:
                stack.append(n.right)
    return s


def postorder_traversal(tree_node, left_to_right=True):
    s = ''
    if tree_node:
        stack = [tree_node]
        while len(stack) > 0:
            n = stack[-1]
            if n.left and not hasattr(n.left, 'done'):
                stack.append(n.left)
            elif n.right and not hasattr(n.right, 'done'):
                stack.append(n.right)
            else:
                n = stack.pop()
                n.done = True
                s += str(n.val)
    return s


if __name__ == '__main__':
    import Test

    tree = build({1: [{2: [{4: None},
                           {5: None}]},
                      {3: [None,
                           {6: None}]}]})

    Test.test(breadth_first_traversal, [
        (tree, '123456'),
    ])
    Test.test(preorder_traversal, [
        (tree, '124536'),
    ])
    Test.test(inorder_traversal, [
        (tree, '425136')
    ])
    Test.test(postorder_traversal, [
        (tree, '452631'),
    ])
