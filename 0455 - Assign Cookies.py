from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        i, j, content = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                content += 1
            else:
                j += 1
        return content


if __name__ == '__main__':
    import Test

    Test.test(Solution().findContentChildren, [
        (([1, 2, 3], [1, 1]), 1),
        (([1, 2], [1, 2, 3]), 2),
    ])
