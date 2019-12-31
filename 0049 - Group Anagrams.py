from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups.get(key).append(s)
        return list(groups.values())


if __name__ == '__main__':
    import Test

    Test.test(Solution().groupAnagrams, [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ]),
    ])
