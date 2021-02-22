from TreeBuilder import TreeNode


class Solution:
    def __init__(self):
        self.max_univalue_length = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.max_univalue_length

    def dfs(self, node: TreeNode) -> int:
        if node is None:
            return 0

        left_length = self.dfs(node.left)
        right_length = self.dfs(node.right)

        if node.left and node.val == node.left.val:
            left_length += 1
        else:
            left_length = 0

        if node.right and node.val == node.right.val:
            right_length += 1
        else:
            right_length = 0

        self.max_univalue_length = max(self.max_univalue_length, left_length + right_length)

        return max(left_length, right_length)


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize
    from TreeBuilder import TreeNode

    Test.test([Solution().longestUnivaluePath], [
        ((deserialize('[5,4,5,1,1,5]')), 2),
        ((deserialize('[4,4,5,1,1,5]')), 1),
        ((deserialize('[1,4,5,4,4,5]')), 2),
        ((deserialize('[5,5,5,1,1,null,3,1,null,null,null,null,null,1]')), 2),
    ])
