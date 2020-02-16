from typing import Union

from TreeBuilder import TreeNode


# BFS. Time: O(h). Space: O(1)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_bst(root, None, None)

    def is_valid_bst(self, root: TreeNode, minimum: Union[None, int], maximum: Union[None, int]) -> bool:
        if root is None:
            return True
        if (minimum is not None and minimum >= root.val) or (maximum is not None and maximum <= root.val):
            return False
        return self.is_valid_bst(root.left, minimum, root.val) and self.is_valid_bst(root.right, root.val, maximum)


if __name__ == '__main__':
    import Test
    import TreeBuilder

    Test.test(Solution().isValidBST, [
        (TreeBuilder.deserialize('[2,1,3]'), True),
        (TreeBuilder.deserialize('[5,1,4,null,null,3,6]'), False),
    ])
