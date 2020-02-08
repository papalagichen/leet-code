from TreeBuilder import TreeNode


# Recursive traversal + backtracking.
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        return (self.rangeSumBST(root.left, L, R) if root.val >= L else 0) + \
               (root.val if L <= root.val <= R else 0) + \
               (self.rangeSumBST(root.right, L, R) if root.val <= R else 0)


# Iterative traversal + backtracking.
class Solution2:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        p = root
        stack = []
        total = 0
        while p or stack:
            if p is None:
                p = stack.pop()
            elif p.val >= L:
                stack.append(p)
                p = p.left
                continue
            if L <= p.val <= R:
                total += p.val
            elif p.val > R:
                break
            p = p.right
        return total


if __name__ == '__main__':
    import Test
    import TreeBuilder

    Test.test([Solution().rangeSumBST, Solution2().rangeSumBST], [
        ((TreeBuilder.deserialize('[10,5,15,3,7,null,18]'), 7, 15), 32),
        ((TreeBuilder.deserialize('[10,5,15,3,7,13,18,1,null,6]'), 6, 10), 23),
    ])
