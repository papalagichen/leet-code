class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        for c in sorted(citations, reverse=True):
            if c > 0:
                if c > h:
                    h += 1
                else:
                    break
        return h


if __name__ == '__main__':
    import Test

    Test.test(Solution().hIndex, [
        ([0, 1, 3, 5, 6], 3),
        ([0, 1, 3, 6], 2),
        ([5], 1),
        ([5, 6], 2),
        ([0], 0),
    ])
