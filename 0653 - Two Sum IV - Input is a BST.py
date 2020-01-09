import bisect
from typing import List

from TreeBuilder import TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        node_values = self.dfs(root)
        for i in range(len(node_values)):
            index = bisect.bisect_left(node_values, k - node_values[i])
            if i != index and index < len(node_values) and node_values[index] == k - node_values[i]:
                return True
        return False

    def dfs(self, node: TreeNode) -> List[int]:
        node_values = []
        if node.left:
            node_values += self.dfs(node.left)
        node_values.append(node.val)
        if node.right:
            node_values += self.dfs(node.right)
        return node_values


class Solution2:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        node_values = self.dfs(root)
        i, j = 0, len(node_values) - 1
        while i != j and node_values[i] + node_values[j] != k:
            if node_values[i] + node_values[j] > k:
                j -= 1
            else:
                i += 1
        return i != j and node_values[i] + node_values[j] == k

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

    Test.test([Solution().findTarget, Solution2().findTarget], [
        ((deserialize('[5,3,6,2,4,null,7]'), 9), True),
        ((deserialize('[1]'), 2), False),
    ])
