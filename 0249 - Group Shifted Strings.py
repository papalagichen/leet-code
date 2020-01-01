import collections
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = {}
        for s in strings:
            key = tuple()
            for i in range(len(s) - 1):
                diff = ord(s[i]) - ord(s[i + 1])
                key += (diff + 26 if diff < 0 else diff,)
            if key not in groups:
                groups[key] = []
            groups.get(key).append(s)
        return list(groups.values())


class Solution2:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strings:
            groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)].append(s)
        return list(groups.values())


if __name__ == '__main__':
    import Test

    Test.test([Solution().groupStrings, Solution2().groupStrings], [
        (["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], [
            ["abc", "bcd", "xyz"],
            ["az", "ba"],  # 1 - 26 = -25 + 26 = 1, 2 - 1 = 1
            ["acef"],
            ["a", "z"]
        ]),
        (["ab", "ba"], [["ab"], ["ba"]]),
        ([], []),
    ])
