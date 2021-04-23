from typing import Tuple

from TreeBuilder import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.helper(root)[0]

    def helper(self, node: TreeNode) -> Tuple[int, int]:  # diameter, height
        if node is None:
            return 0, 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        return max(left[1] + right[1], left[0], right[0]), 1 + max(left[1], right[1])


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize

    Test.test([Solution().diameterOfBinaryTree], [
        (deserialize('[1,null,3,2]'), 2),
        (deserialize('[5,4,7]'), 2),
        (deserialize('[1,2,3,4,5]'), 3),
        (deserialize('[1,2]'), 1),
        (deserialize('[1]'), 0),
    ])
