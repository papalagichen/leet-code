from TreeBuilder import TreeNode

"""
     3
   2   3
    3   1
"""


# Brute Force Recursive DFS. Time: O(2^n). Space: O(1)
class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.helper(root, True), self.helper(root, False))

    def helper(self, node: TreeNode, rob: bool) -> int:
        if node is None:
            return 0
        if rob:
            money = node.val + self.helper(node.left, False) + self.helper(node.right, False)
        else:
            money = max(
                self.helper(node.left, True) + self.helper(node.right, True),
                self.helper(node.left, True) + self.helper(node.right, False),
                self.helper(node.left, False) + self.helper(node.right, True),
                self.helper(node.left, False) + self.helper(node.right, False),
            )
        return money


# Dynamic Programming. Time: O(n). Space: O(n)
class Solution2:
    def rob(self, root: TreeNode) -> int:
        return max(self.helper(root, True), self.helper(root, False))

    def helper(self, node: TreeNode, rob: bool) -> int:
        if node is None:
            return 0
        if rob and hasattr(node, 'rob_max_money'):
            return getattr(node, 'rob_max_money')
        elif not rob and hasattr(node, 'no_rob_max_money'):
            return getattr(node, 'no_rob_max_money')
        if rob:
            money = node.val + self.helper(node.left, False) + self.helper(node.right, False)
            setattr(node, 'rob_max_money', money)
        else:
            money = max(
                self.helper(node.left, True) + self.helper(node.right, True),
                self.helper(node.left, True) + self.helper(node.right, False),
                self.helper(node.left, False) + self.helper(node.right, True),
                self.helper(node.left, False) + self.helper(node.right, False),
            )
            setattr(node, 'no_rob_max_money', money)
        return money


if __name__ == '__main__':
    import Test
    import TreeBuilder

    Test.test([Solution().rob, Solution2().rob], [
        (TreeBuilder.deserialize('[3,2,3,null,3,null,1]'), 7),
        (TreeBuilder.deserialize('[3,4,5,1,3,null,1]'), 9),
    ])
