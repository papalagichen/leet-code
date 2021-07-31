from typing import List

"""
a b ba bca bda bdca
1 1  2   3   3    4

a ab ac bd abc abd abdd
1  2  2  1   3   3    4
"""


# Dynamic Programming. Time: O(n lg n + nk). Space: O(n)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        mem = {}
        for w in sorted(words, key=len):
            mem[w] = max(mem.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(mem.values())


if __name__ == '__main__':
    import Test

    Test.test([Solution().longestStrChain], [
        (["a", "b", "ba", "bca", "bda", "bdca"], 4),
        (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
        (["abcd", "dbqca"], 1),
        (["a", "ab", "ac", "bd", "abc", "abd", "abdd"], 4),
    ])
