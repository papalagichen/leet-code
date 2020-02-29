from typing import List


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        lengths = sorted(list(set(len(x) for x in words)))
        hashes = set(hash(x) for x in words)
        results = []
        for i in range(len(text) - lengths[0] + 1):
            for length in [x for x in lengths if x + i <= len(text)]:
                if hash(text[i:i + length]) in hashes:
                    results.append([i, i + length - 1])
        return results


if __name__ == '__main__':
    import Test

    Test.test(Solution().indexPairs, [
        (("thestoryofleetcodeandme", ["story", "fleet", "leetcode"]), [[3, 7], [9, 13], [10, 17]]),
        (("ababa", ["aba", "ab"]), [[0, 1], [0, 2], [2, 3], [2, 4]]),
    ])
