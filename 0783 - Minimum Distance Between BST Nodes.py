import sys
from typing import List

from TreeBuilder import TreeNode


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        min_diff = sys.maxsize
        node_values = self.dfs(root)
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


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize

    Test.test(Solution().minDiffInBST, [
        (deserialize('[4,2,6,1,3,null,null]'), 1),
        (deserialize('[2,1,6]'), 1),
        (deserialize('[96,12,null,null,13,null,52,29,null,null,null]'), 1),
    ])
