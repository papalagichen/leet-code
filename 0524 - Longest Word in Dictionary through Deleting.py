from typing import List


# Two pointers. Time: O(n * m). Space: O(1)
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longest_word = ''
        for word in d:
            if len(longest_word) <= len(word) and self.is_subsequence(s, word):
                longest_word = min(longest_word, word) if len(longest_word) == len(word) else word
        return longest_word

    def is_subsequence(self, s: str, word: str) -> bool:
        i = 0
        for c in s:
            if i < len(word) and c == word[i]:
                i += 1
        return i == len(word)


# Leetcode discussion solution
class Solution2:
    def findLongestWord(self, s, d):
        best = ''
        for x in d:
            if (-len(x), x) < (-len(best), best):
                it = iter(s)
                if all(c in it for c in x):
                    best = x
        return best


if __name__ == '__main__':
    import Test

    Test.test([Solution().findLongestWord, Solution2().findLongestWord], [
        (('abpcplea', ["ale", "apple", "monkey", "plea"]), 'apple'),
        (('abpcplea', ["a", "b", "c"]), 'a'),
        (('defg', ["a", "b", "c"]), ''),
        (('bab', ["ba", "ab", "a", "b"]), 'ab')
    ])
