import copy
from typing import List

from TreeBuilder import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.helper(root, sum, [])

    def helper(self, node: TreeNode, sum: int, nums: List[int]) -> int:
        if node is None:
            return 0
        nums = copy.copy(nums)
        nums.append(node.val)
        count = 0
        s = 0
        for n in nums[::-1]:
            s += n
            if s == sum:
                count += 1
        return count + self.helper(node.left, sum, nums) + self.helper(node.right, sum, nums)


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize
    from TreeBuilder import TreeNode

    Test.test(Solution().pathSum, [
        ((deserialize('[10,5,-3,3,2,null,11,3,-2,null,1]'), 8), 3),
        ((deserialize('[5,4,8,11,null,13,4,7,2,null,null,5,1]'), 22), 3),
        ((deserialize('[5,4,8]'), 9), 1),
        ((deserialize('[5,4,8]'), 13), 1),
        ((deserialize('[5,4,8]'), 5), 1),
        ((deserialize('[5,4,8]'), 10), 0),
        ((deserialize('[5,5,8]'), 5), 2),
    ])
