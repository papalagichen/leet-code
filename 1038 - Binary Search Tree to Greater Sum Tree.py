from TreeBuilder import TreeNode


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.modify_tree(root, self.get_tree_sum(root))
        return root

    def get_tree_sum(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return self.get_tree_sum(node.left) + node.val + self.get_tree_sum(node.right)

    def modify_tree(self, node: TreeNode, tree_sum) -> int:
        if node is None:
            return tree_sum
        tree_sum = self.modify_tree(node.left, tree_sum)
        node.val, tree_sum = tree_sum, tree_sum - node.val
        return self.modify_tree(node.right, tree_sum)


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize

    Test.test(Solution().bstToGst, [
        (
            deserialize('[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'),
            deserialize('[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]'),
        ),
    ])
