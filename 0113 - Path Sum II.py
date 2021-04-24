from typing import List

from TreeBuilder import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        if targetSum == root.val and root.left is None and root.right is None:
            return [[root.val]]
        paths = []
        for path in self.pathSum(root.left, targetSum - root.val) + self.pathSum(root.right, targetSum - root.val):
            paths.append([root.val] + path)
        return paths


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize
    from TreeBuilder import TreeNode

    Test.test(Solution().pathSum, [
        ((deserialize('[5,4,8,11,null,13,4,7,2,null,null,5,1]'), 22), [[5, 4, 11, 2], [5, 8, 4, 5]]),
        ((deserialize('[1,2,3]'), 5), []),
        ((deserialize('[1,2]'), 0), []),
    ])
