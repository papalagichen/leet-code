from NAryTreeBuilder import NAryTreeNode


class Solution:
    def maxDepth(self, root: NAryTreeNode) -> int:
        depth = 1
        if root is not None:
            for c in root.children:
                depth = max(depth, 1 + self.maxDepth(c))
        return depth


if __name__ == '__main__':
    import Test
    from NAryTreeBuilder import deserialize

    Test.test(Solution().maxDepth, [
        (deserialize('[1,null,3,2,4,null,5,6]'), 3),
        (deserialize('[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]'), 5),
    ])
