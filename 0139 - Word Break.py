from functools import lru_cache
from typing import List
from typing import Set

"""
can_break(i) = current substring in dict and can_break(i - 1)
"""


# Brute Force. Time: O(n^n). Space: O(n)
class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        return self.helper(s, set(word_dict), 0)

    def helper(self, s: str, word_dict: Set[str], start: int) -> bool:
        if start == len(s):
            return True
        for i in range(len(s), start, -1):
            if s[start:i] in word_dict and self.helper(s, word_dict, i):
                return True
        return False


# Dynamic Programming Recursive Version. Time: O(n). Space: O(n)
class Solution2:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        return self.helper(s, set(word_dict), 0, [None] * len(s))

    def helper(self, s: str, word_dict: Set[str], start: int, can_break: List[bool]) -> bool:
        if start == len(s):
            return True
        if can_break[start] is not None:
            return can_break[start]
        for i in range(len(s), start, -1):
            if s[start:i] in word_dict and self.helper(s, word_dict, i, can_break):
                can_break[start] = True
                break
        else:
            can_break[start] = False
        return can_break[start]


# Dynamic Programming with lru_cache. Time: O(n). Space: O(n)
class Solution3:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        self.word_dict = set(word_dict)
        return self.helper(s, 0)

    @lru_cache()
    def helper(self, s: str, start: int) -> bool:
        if start == len(s):
            return True
        for i in range(len(s), start, -1):
            if s[start:i] in self.word_dict and self.helper(s, i):
                return True
        return False


if __name__ == '__main__':
    import Test

    Test.test([Solution2().wordBreak, Solution3().wordBreak], [
        (("leetcode", ["leet", "code"]), True),
        (("applepenapple", ["apple", "pen"]), True),
        (("catsandog", ["cats", "dog", "sand", "and", "cat"]), False),
        (("bc", ["cb"]), False),
        (("bb", ["a", "b", "bbb", "bbbb"]), True),
        (("ab", ["a", "b"]), True),
        (("aaaaaaa", ["aaaa", "aaa"]), True),
        (("abcd", ["a", "abc", "b", "cd"]), True),
        ((
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
             ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
         ), False),
        ((
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]
         ), False),
    ])
