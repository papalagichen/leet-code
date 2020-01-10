from typing import Generator
from typing import List
from typing import Set

from TreeBuilder import TreeNode


# Time O(n + m), Space O(n)
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        return self.find_target(root2, target, set(self.dfs(root1)))

    def dfs(self, node: TreeNode) -> List[int]:
        if node is None:
            return []
        return self.dfs(node.left) + [node.val] + self.dfs(node.right)

    def find_target(self, node: TreeNode, target, value_set: Set[int]) -> bool:
        return node is not None \
               and (target - node.val in value_set
                    or self.find_target(node.left, target, value_set)
                    or self.find_target(node.right, target, value_set))


# Time O(n + m), Space O(n + m)
class Solution2:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        node_values1 = self.dfs(root1)
        node_values2 = self.dfs(root2)

        i, j = 0, len(node_values2) - 1

        while i < len(node_values1) and j >= 0:
            value1 = node_values1[i]
            value2 = node_values2[j]

            if value1 + value2 == target:
                return True
            elif value1 + value2 < target:
                i += 1
            else:
                j -= 1
        return False

    def dfs(self, node: TreeNode) -> List[int]:
        if node is None:
            return []
        return self.dfs(node.left) + [node.val] + self.dfs(node.right)


# Time O(n + m), Space O(1)
class Solution3:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        generator1 = self.traverse_from_smallest(root1)
        generator2 = self.traverse_from_largest(root2)

        try:
            value1 = next(generator1)
            value2 = next(generator2)

            while True:
                if value1 + value2 == target:
                    return True
                if value1 + value2 < target:
                    value1 = next(generator1)
                else:
                    value2 = next(generator2)
        except StopIteration:
            return False

    def traverse_from_smallest(self, node: TreeNode) -> Generator:
        if node.left:
            yield from self.traverse_from_smallest(node.left)
        yield node.val
        if node.right:
            yield from self.traverse_from_smallest(node.right)

    def traverse_from_largest(self, node: TreeNode) -> Generator:
        if node.right:
            yield from self.traverse_from_largest(node.right)
        yield node.val
        if node.left:
            yield from self.traverse_from_largest(node.left)


if __name__ == '__main__':
    import Test
    from TreeBuilder import deserialize

    Test.test([Solution().twoSumBSTs, Solution2().twoSumBSTs, Solution3().twoSumBSTs], [
        ((deserialize('[2,1,4]'), deserialize('[1,0,3]'), 5), True),
        ((deserialize('[0,-10,10]'), deserialize('[5,1,7,0,2]'), 18), False),
        ((
             deserialize(
                 '[-610851256,-653710341,370681985,-684322521,null,-99709414,945937000,-723663811,null,-580534514,'
                 '175879876,684879230,961162608,-937470592,null,null,-300171034,26171351,216952004,586959211,'
                 '722844782,953939489,989534661,null,-766632327,-375831089,-216679007,-10713080,103126520,null,'
                 '343409064,540698705,660693010,null,894076654,null,null,null,null,-813292023,null,-496932482,'
                 '-304607959,-228730335,-126869030,-78270931,22440306,84915568,null,307851156,null,434200343,null,'
                 'null,null,846779650,null,-826002807,null,null,-483519915,-334445856,null,null,null,-135095123,null,'
                 'null,null,null,null,83812730,null,null,null,null,null,836900978,null,-893449855,-819573989,null,'
                 '-442688630,null,null,null,null,40242181,null,null,null,-901146738]'),
             deserialize(
                 '[-789314604,-844978429,-362754072,-884801305,-842381632,-478151046,61096204,null,null,null,'
                 'null,-745017955,-445455117,-206589393,512329594,null,-740359122,-466990471,-420769635,'
                 '-317219442,-108708327,388674482,844021027,null,-533290204,null,null,-422661229,null,null,'
                 '-209171221,-112908812,null,296061830,484713586,674571946,994804552,-692388982,null,null,'
                 'null,null,null,null,null,188484963,386640458,399688904,null,583260301,808930864,962289719,'
                 'null,null,-619367458,null,null,null,null,null,null,524969019,589842534,739755144,null,'
                 '954377409,null,null,null,null,540622433,null,null,null,748416803,939513678,null,null,'
                 '568310964]'),
             68839864
         ), True),
    ])
