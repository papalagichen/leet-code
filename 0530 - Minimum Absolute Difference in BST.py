import sys
from typing import List
from typing import Tuple

from TreeBuilder import TreeNode


# Time O(n), Space O(n)
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        node_values = self.dfs(root)
        min_diff = sys.maxsize
        for i in range(len(node_values) - 1):
            min_diff = min(min_diff, node_values[i + 1] - node_values[i])
        return min_diff

    def dfs(self, node: TreeNode) -> List[int]:
        node_values = []
        if node.left:
            node_values += self.dfs(node.left)
        node_values.append(node.val)
        if node.right:
            node_values += self.dfs(node.right)
        return node_values


# Time O(n), Space O(1)
class Solution2:
    def getMinimumDifference(self, root: TreeNode) -> int:
        return self.traverse(root)[0]

    def traverse(self, node: TreeNode) -> Tuple[int, int, int]:
        min_abs_diff, min_value, max_value = sys.maxsize, node.val, node.val
        if node.left:
            sub_min_abs_diff, sub_min_value, sub_max_value = self.traverse(node.left)
            min_abs_diff = min(min_abs_diff, sub_min_abs_diff, node.val - sub_max_value)
            min_value = min(min_value, sub_min_value)
        if node.right:
            sub_min_abs_diff, sub_min_value, sub_max_value = self.traverse(node.right)
            min_abs_diff = min(min_abs_diff, sub_min_abs_diff, sub_min_value - node.val)
            max_value = max(max_value, sub_max_value)
        return min_abs_diff, min_value, max_value


# Time O(n), Space O(1)
class Solution3:
    def getMinimumDifference(self, root: TreeNode) -> int:
        return self.traverse(root, root, sys.maxsize)[1]

    def traverse(self, node, prev_node, min_diff):
        if node.left:
            prev_node, min_diff = self.traverse(node.left, prev_node, min_diff)
        if prev_node is not node:
            min_diff = min(min_diff, abs(prev_node.val - node.val))
        prev_node = node
        if node.right:
            prev_node, min_diff = self.traverse(node.right, prev_node, min_diff)
        return prev_node, min_diff


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize

    Test.test([Solution().getMinimumDifference, Solution2().getMinimumDifference, Solution3().getMinimumDifference], [
        (deserialize('[1,null,3,2]'), 1),
        (deserialize('[5,4,7]'), 1),
    ])
