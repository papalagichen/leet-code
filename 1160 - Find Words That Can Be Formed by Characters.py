import collections
from typing import List


# Character count dictionary. Time: O(nm). Space: O(p)
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for w in words:
            d = {}
            for c in chars:
                d[c] = d.get(c, 0) + 1
            for c in w:
                if d.get(c, 0) > 0:
                    d[c] -= 1
                else:
                    break
            else:
                ans += len(w)
        return ans


# Sorted array. Time: O(m * n lg n ). Space: O(1)
class Solution2:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = sorted(chars)
        ans = 0
        for w in [sorted(w) for w in words]:
            i, j = 0, 0
            while i < len(w):
                if j >= len(chars) or w[i] < chars[j]:
                    break
                if w[i] > chars[j]:
                    j += 1
                    continue
                i, j = i + 1, j + 1
            else:
                ans += len(w)
        return ans


#
class Solution3:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans, chars_counter = 0, collections.Counter(chars)
        for word in words:
            word_counter = collections.Counter(word)
            for c in word_counter:
                if word_counter[c] > chars_counter[c]:
                    break
            else:
                ans += len(word)
        return ans


if __name__ == '__main__':
    import Test

    Test.test([Solution().countCharacters, Solution2().countCharacters], [
        ((["cat", "bt", "hat", "tree"], 'atach'), 6),
        ((["hello", "world", "leetcode"], 'welldonehoneyr'), 10),
    ])
