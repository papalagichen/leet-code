"""
aacaba
a acaba
aa caba
aac aba *
aaca ba *
aacab a
"""


# Two passes. Time: O(n). Space: O(n)
class Solution:
    def numSplits(self, s: str) -> int:
        first_count, second_count = {}, {}
        for c in s:
            second_count[c] = second_count.get(c, 0) + 1
        split_count = 0
        for c in s:
            first_count[c] = first_count.get(c, 0) + 1
            second_count[c] = second_count.get(c, 0) - 1
            if second_count[c] == 0:
                del second_count[c]
            if len(first_count) == len(second_count):
                split_count += 1
        return split_count


if __name__ == '__main__':
    import Test

    Test.test([Solution().numSplits], [
        ("aacaba", 2),
    ])
