from typing import List

from TreeBuilder import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        nodes = [root]
        values = []
        while len(nodes) > 0:
            total = 0
            nodes2 = []
            for n in nodes:
                total += n.val
                if n.left:
                    nodes2.append(n.left)
                if n.right:
                    nodes2.append(n.right)
            values.append(total / len(nodes))
            nodes = nodes2
        return values


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize

    Test.test([Solution().averageOfLevels], [
        (deserialize('[3,9,20,15,7]'), [3, 14.5, 11]),
    ])
