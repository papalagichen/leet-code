from TreeBuilder import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        queue = [s]
        while len(queue) > 0:
            node = queue.pop(0)
            if node is None:
                continue
            if node.val == t.val and self.dfs(node, t):
                return True
            queue.append(node.left)
            queue.append(node.right)
        return False

    def dfs(self, node1: TreeNode, node2: TreeNode) -> bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        return self.dfs(node1.left, node2.left) and self.dfs(node1.right, node2.right)


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize

    Test.test(Solution().isSubtree, [
        ((deserialize('[3,4,5,1,2]'), deserialize('[4,1,2]')), True),
        ((deserialize('[3,4,5,1,2]'), deserialize('[4,1,3]')), False),
        # ((deserialize(''), deserialize('')), 3),
    ])
